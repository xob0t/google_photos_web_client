import json
import urllib.parse
from collections.abc import Iterable
from http.cookiejar import MozillaCookieJar
from pathlib import Path
from typing import Literal, overload

from lxml import html

from . import utils
from .models import ApiResponse
from .parser import parse_response_data
from .payloads import Payload


class Client:
    """Reverse engineered Google Photos web API client."""

    def __init__(
        self,
        cookies_txt_path: str | Path,
        log_level: Literal["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"] = "INFO",
        account_index: int = 0,
    ) -> None:
        """
        Args:
            cookies_txt_path: Path to a netscape cookies.txt file.
            log_level: Logging level.
            account_index: Index of the Google account to use when the cookies hold a
                multi-login session (the `N` in photos.google.com/u/N/).
        """
        self.cookies_txt_path = cookies_txt_path
        self.account_index = account_index
        self.base_path = f"/u/{account_index}/" if account_index else "/"
        self.logger = utils.create_logger(log_level)
        self.session = utils.new_session_with_retries()
        self.load_cookies_in_session()
        self.global_data = self.get_global_data()
        self.logger.info(f"Account: {self.global_data['oPEP7c']}")

    def __enter__(self):
        """Enter"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit"""

    def load_cookies_in_session(self) -> None:
        """Load cookies from cookies.txt and upate session cookies with them"""
        cookies = self.load_cookies_from_file(self.cookies_txt_path)
        self.session.cookies.update(cookies)

    def get_global_data(self) -> dict:
        """Get and parse global_data from photos.google.com page"""
        response = self.session.get(f"https://photos.google.com{self.base_path}")
        if self.account_index and f"/u/{self.account_index}/" not in response.url:
            raise ValueError(f"account_index {self.account_index} not found in cookies (redirected to {response.url})")
        return self.parse_main_page(response.text)

    def parse_main_page(self, page_body: str) -> dict:
        """Parse data from photos.google.com html body"""
        xml_page = html.fromstring(page_body)
        script_text: str = xml_page.xpath('//script[@data-id="_gd"]/text()')[0]
        script_json = script_text.replace("window.WIZ_global_data = ", "").rstrip().rstrip(";")
        return json.loads(script_json)

    def load_cookies_from_file(self, path: str | Path) -> MozillaCookieJar:
        """Load netscape cookies from file"""
        cookie_jar = MozillaCookieJar(path)
        cookie_jar.load(ignore_discard=True, ignore_expires=True)
        return cookie_jar

    def prepare_payload(self, payload: Payload) -> list:
        """Prepare payload for api request"""
        return [payload.rpcid, json.dumps(payload.data, separators=(",", ":")), None, payload.payload_id]

    @overload
    def send_api_request(self, payloads: Payload) -> ApiResponse: ...

    @overload
    def send_api_request(self, payloads: Iterable[Payload]) -> list[ApiResponse]: ...

    def send_api_request(self, payloads: Iterable[Payload] | Payload) -> list[ApiResponse] | ApiResponse:
        """Send an api request wiht rpc payloads"""

        _payloads = [payloads] if isinstance(payloads, Payload) else payloads

        querystring = {
            "rpcids": ",".join([payload.rpcid for payload in _payloads]),
            "source-path": self.base_path,
            "f.sid": self.global_data["FdrFJe"],
            "bl": self.global_data["cfb2h"],
            "rt": "c",
        }
        payload = {
            "f.req": json.dumps([[self.prepare_payload(payload) for payload in _payloads]], separators=(",", ":")),
            "at": self.global_data["SNlM0e"],
        }
        payload_encoded = "&".join(f"{key}={urllib.parse.quote(value, safe='')}" for key, value in payload.items())

        url = f"https://photos.google.com{self.global_data['Im6cmf']}/data/batchexecute"

        response = self.session.post(url, data=payload_encoded, params=querystring)

        response.raise_for_status()

        pared_responses = self.parse_api_response(response.text, _payloads)
        if isinstance(payloads, Payload):
            return pared_responses[0]
        return pared_responses

    def parse_api_response(self, response_body: str, payloads: Iterable[Payload]) -> list[ApiResponse]:
        """Parse api response"""
        responses = [json.loads(line) for line in response_body.split("\n") if "wrb.fr" in line]
        parsed_responses = []
        for response in responses:
            success = False
            response_data = response[0][2]
            if response_data:
                response_data = json.loads(response_data)
                success = True
            response_id = response[0][6]
            response_rpcid = response[0][1]
            parse_response = next(
                (payload.parse_response for payload in payloads if payload.payload_id == response_id), False
            )
            api_response = ApiResponse(
                rpcid=response_rpcid,
                success=success,
                response_id=response_id,
                data=parse_response_data(response_rpcid, response_data) if parse_response else response_data,
            )
            parsed_responses.append(api_response)
        return parsed_responses
