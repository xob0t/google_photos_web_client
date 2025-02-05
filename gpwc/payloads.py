from typing import Literal, Optional
from abc import ABC

from .utils import generate_id


class Payload(ABC):
    rpcid: str
    data: list[str | None]
    payload_id: str
    parse_response: Optional[bool] = False

    def __init__(self):
        self.payload_id: str = generate_id()


class GetLibraryPageByTakenDate(Payload):
    def __init__(
        self,
        timestamp: Optional[int] = None,
        source: Optional[Literal["library", "archive", "both"]] = "both",
        page_id: Optional[str] = None,
        page_size: Optional[int] = 500,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        source_map = {"library": 1, "archive": 2, "both": 3}
        self.parse_response = parse_response
        self.rpcid = "lcxiM"
        self.data = [page_id, timestamp, page_size, None, 1, source_map[source]]


class GetLibarayPageByUploadedDate(Payload):
    def __init__(
        self,
        page_id: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "EzkLib"
        self.data = ["", [[4, "ra", 0, 0]], page_id]


class GetSearchPage(Payload):
    def __init__(
        self,
        query: str,
        page_id: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "EzkLib"
        self.data = [query, None, page_id]


class GetRemoteMatchesByHash(Payload):
    def __init__(
        self,
        hashes: list[str],
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "swbisb"
        self.data = [hashes, None, 3, 0]


class GetItemInfo(Payload):
    def __init__(
        self,
        media_key: str,
        album_media_key: Optional[str] = None,
        auth_key: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "VrseUb"
        self.data = [media_key, None, auth_key, None, album_media_key]


class GetItemInfoExt(Payload):
    def __init__(
        self,
        media_key: str,
        auth_key: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "fDcn4b"
        self.data = [media_key, 1, auth_key, None, 1]


class GetBatchMediaInfo(Payload):
    def __init__(
        self,
        media_keys: list[str],
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        keys = [[key] for key in media_keys]
        self.rpcid = "EWgK9e"
        self.data = [[[keys], [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, [], None, None, None, None, None, None, None, None, None, None, []]]]]


class MoveToTrash(Payload):
    def __init__(
        self,
        dedup_keys: list[str],
    ):
        super().__init__()
        self.rpcid = "XwAOJf"
        self.data = [None, 1, dedup_keys, 3]


class RestoreFromTrash(Payload):
    def __init__(
        self,
        dedup_keys: list[str],
    ):
        super().__init__()
        self.rpcid = "XwAOJf"
        self.data = [None, 3, dedup_keys, 2]


class CreateAlbum(Payload):
    def __init__(
        self,
        name: str,
    ):
        super().__init__()
        self.rpcid = "OXvT9d"
        self.data = [name, None, 2]


class SetFavorite(Payload):
    def __init__(
        self,
        dedup_keys: list[str],
    ):
        super().__init__()
        self.rpcid = "Ftfh0"
        dedup_keys_list = [[None, key] for key in dedup_keys]
        self.data = [dedup_keys_list, [1]]


class UnFavorite(Payload):
    def __init__(
        self,
        dedup_keys: list[str],
    ):
        super().__init__()
        self.rpcid = "Ftfh0"
        dedup_keys_list = [[None, key] for key in dedup_keys]
        self.data = [dedup_keys_list, [2]]


class SetArchive(Payload):
    def __init__(
        self,
        dedup_keys: list[str],
    ):
        super().__init__()
        self.rpcid = "w7TP3c"
        dedup_keys_list = [[None, [1], [None, key]] for key in dedup_keys]
        self.data = [dedup_keys_list, None, 1]


class UnArchive(Payload):
    def __init__(
        self,
        dedup_keys: list[str],
    ):
        super().__init__()
        self.rpcid = "w7TP3c"
        dedup_keys_list = [[None, [2], [None, key]] for key in dedup_keys]
        self.data = [dedup_keys_list, None, 1]


class SetItemTimestamp(Payload):
    def __init__(
        self,
        dedup_key: str,
        timestamp: int,
        timezone_offset: int,
    ):
        """Timestamp in epoch miliseconds
        Timesone as an offset e.g 19800 is GMT+05:30"""
        super().__init__()
        self.rpcid = "DaSgWe"
        self.data = [[[dedup_key, timestamp, timezone_offset]]]


class SetItemDescription(Payload):
    def __init__(
        self,
        dedup_key: str,
        description: str,
    ):
        super().__init__()
        self.rpcid = "AQNOFd"
        self.data = [None, description, dedup_key]


class SetItemGeoData(Payload):
    def __init__(
        self,
        dedup_keys: list[str],
        center_point: list[int],
        visible_point_1: list[str],
        visible_point_2: list[str],
        scale: int,
        gmaps_place_id: str,
    ):
        super().__init__()
        self.rpcid = "EtUHOe"
        dedup_key_list = [[None, key] for key in dedup_keys]
        self.data = [dedup_key_list, [2, center_point, [visible_point_1, visible_point_2], [None, None, scale], gmaps_place_id]]


class DeleteItemGeoData(Payload):
    def __init__(
        self,
        dedup_keys: list[str],
    ):
        super().__init__()
        self.rpcid = "EtUHOe"
        dedup_key_list = [[None, key] for key in dedup_keys]
        self.data = [dedup_key_list, [1]]


class GetFavoritesPage(Payload):
    def __init__(
        self,
        page_id: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "EzkLib"
        self.data = ["Favorites", [[5, "8", 0, 9]], page_id]


class GetTrashPage(Payload):
    def __init__(
        self,
        page_id: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "zy0IHe"
        self.data = [page_id]


class GetAlbumsPage(Payload):
    def __init__(
        self,
        page_id: Optional[str] = None,
        page_size: Optional[int] = 100,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "Z5xsfc"
        self.data = [page_id, None, None, None, 1, None, None, page_size, [2], 5]


class GetAlbumPage(Payload):
    def __init__(
        self,
        media_key: str,
        page_id: Optional[str] = None,
        authKey: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "snAcKc"
        self.data = [media_key, page_id, None, authKey]


class GetSharedLinksPage(Payload):
    def __init__(
        self,
        page_id: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "F2A0H"
        self.data = [page_id, None, 2, None, 3]


class RemoveItemsFromAlbum(Payload):
    def __init__(
        self,
        album_item_media_keys: list[str],
    ):
        super().__init__()
        self.rpcid = "ycV3Nd"
        self.data = [album_item_media_keys]


class AddItemsToNewAlbum(Payload):
    def __init__(
        self,
        item_media_keys: list[str],
        albumName: str,
    ):
        super().__init__()
        self.rpcid = "E1Cajb"
        self.data = [item_media_keys, None, albumName]


class AddItemsToExistingAlbum(Payload):
    def __init__(
        self,
        item_media_keys: list[str],
        album_media_key: str,
    ):
        super().__init__()
        self.rpcid = "E1Cajb"
        self.data = [item_media_keys, album_media_key]


class AddItemsToExistingSharedAlbum(Payload):
    def __init__(
        self,
        item_media_keys: list[str],
        album_media_key: str,
    ):
        super().__init__()
        self.rpcid = "laUYf"
        item_media_keys_list = [[[key]] for key in item_media_keys]
        self.data = [album_media_key, [2, None, item_media_keys_list, None, None, None, [1]]]


class GetStorageQuota(Payload):
    def __init__(
        self,
        parse_response: Optional[bool] = True,
    ):
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "EzwWhf"
        self.data = []


class GetDownloadToken(Payload):
    def __init__(
        self,
        item_media_keys: list[str],
    ):
        """Receives a token, which is then used to check if the dl url is ready with CheckDownloadToken"""
        super().__init__()
        self.rpcid = "yCLA7"
        self.data = [[[key] for key in item_media_keys]]


class CheckDownloadToken(Payload):
    def __init__(
        self,
        download_token: list[str],
        parse_response: Optional[bool] = True,
    ):
        """Returns a DL url if it is ready"""
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "dnv2s"
        self.data = [[download_token]]


class SaveSharedMediaToLibrary(Payload):
    def __init__(
        self,
        album_media_key: list[str],
        item_media_keys: list[str],
        auth_key: str,
    ):
        super().__init__()
        self.rpcid = "V8RKJ"
        self.data = [item_media_keys, auth_key, album_media_key]


class GetPartnerSharedMedia(Payload):
    def __init__(
        self,
        partner_actor_id: str,
        gaia_id: str,
        page_id: Optional[str] = None,
        parse_response: Optional[bool] = True,
    ):
        """Partner's actor_id, your account's gaia_id"""
        super().__init__()
        self.parse_response = parse_response
        self.rpcid = "e9T5je"
        self.data = [page_id, None, [None, [[[2, 1]]], [partner_actor_id], [None, gaia_id], 1]]


class SavePartnerSharedMedia(Payload):
    def __init__(
        self,
        item_media_keys: list[str],
    ):
        """Save partner shared media to library"""
        super().__init__()
        self.rpcid = "Es7fke"
        self.data = [[[key] for key in item_media_keys]]
