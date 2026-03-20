import logging
import uuid
from typing import Any

import requests
from requests.adapters import HTTPAdapter, Retry


def safe_get(data: dict | list, *keys: Any, default: Any = None) -> Any:
    """
    Safely retrieve a value from a nested dictionary or list using a sequence of keys/indices.
    If any key or index is missing, return the default value.

    :param data: The nested dictionary or list to search.
    :param keys: A sequence of keys/indices to navigate through the nested structure.
    :param default: The value to return if the path is not found (default is None).
    :return: The value at the specified path or the default value if the path is invalid.
    """
    current = data
    for key in keys:
        if (isinstance(current, dict) and key in current) or (
            isinstance(current, list) and isinstance(key, int) and -len(current) <= key < len(current)
        ):
            current = current[key]
        else:
            return default
    return current


def generate_id() -> str:
    return uuid.uuid4().hex


def get_nested(data: list | dict, *indices: tuple[int], default: bool = None):
    """
    Safely get a nested value from lists or dictionaries using a sequence of
    indices/keys without throwing errors for missing paths.
    """
    current = data
    for idx in indices:
        if current is None:
            return default
        try:
            current = current[idx]
        except (IndexError, KeyError, TypeError):
            return default
    return current


def new_session_with_retries() -> requests.Session:
    """Create a new request session with retry mechanism"""
    # https://stackoverflow.com/questions/23267409/how-to-implement-retry-mechanism-into-python-requests-library
    headers = {
        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
    }
    s = requests.Session()
    s.headers.update(headers)
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    s.mount("http://", adapter)
    s.mount("https://", adapter)
    return s


def create_logger(log_level: str) -> logging.Logger:
    """Create main logger"""
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="%H:%M:%S",
    )
    return logging.getLogger("main")
