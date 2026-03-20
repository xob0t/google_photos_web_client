from dataclasses import dataclass

from .utils import safe_get


@dataclass
class GeoLocation:
    coordinates: list[float] | None = None
    name: str | None = None
    map_thumb: str | None = None

    @classmethod
    def from_data(cls, item_data):
        return cls(
            coordinates=safe_get(item_data, 0, 9, 0) or safe_get(item_data, 0, 13, 0),
            name=safe_get(item_data, 0, 13, 2, 0, 1, 0, 0),
            map_thumb=safe_get(item_data, 1),
        )


@dataclass
class LibraryItem:
    media_key: str
    timestamp: int
    timezone_offset: int
    creation_timestamp: int
    dedup_key: str
    thumbnail_url: str
    res_width: int
    res_height: int
    is_partial_upload: bool
    is_archived: bool
    is_favorite: bool
    video_duration: int | None
    description_short: str | None
    live_photo_duration: int | None
    is_owned: bool
    geo_location: GeoLocation

    @classmethod
    def from_data(cls, item_data):
        # Parse geo_location if present
        geo_location = GeoLocation(
            coordinates=safe_get(item_data, -1, "129168200", 1, 0),
            name=safe_get(item_data, -1, "129168200", 1, 4, 0, 1, 0, 0),
        )

        return cls(
            media_key=safe_get(item_data, 0),
            timestamp=safe_get(item_data, 2),
            timezone_offset=safe_get(item_data, 4),
            creation_timestamp=safe_get(item_data, 5),
            dedup_key=safe_get(item_data, 3),
            thumbnail_url=safe_get(item_data, 1, 0),
            res_width=safe_get(item_data, 1, 1),
            res_height=safe_get(item_data, 1, 2),
            is_partial_upload=safe_get(item_data, 12, 0) == 20,
            is_archived=safe_get(item_data, 13),
            is_favorite=safe_get(item_data, -1, "163238866", 0),
            video_duration=safe_get(item_data, -1, "76647426", 0),
            description_short=safe_get(item_data, -1, "396644657", 0),
            live_photo_duration=safe_get(item_data, -1, "146008172", 1),
            is_owned=not any(27 in sub_array for sub_array in safe_get(item_data, 7, default=[])),
            geo_location=geo_location,
        )


@dataclass
class LibraryTimelinePage:
    items: list[LibraryItem]
    next_page_id: str | None
    last_item_timestamp: int | None

    @classmethod
    def from_data(cls, data):
        return cls(
            items=[LibraryItem.from_data(item) for item in safe_get(data, 0, default=[])],
            next_page_id=safe_get(data, 1),
            last_item_timestamp=safe_get(data, 2) and int(safe_get(data, 2)),
        )


@dataclass
class LibraryGenericPage:
    items: list[LibraryItem]
    next_page_id: str | None

    @classmethod
    def from_data(cls, data):
        return cls(
            items=[LibraryItem.from_data(item) for item in safe_get(data, 0) or []],
            next_page_id=safe_get(data, 1),
        )


@dataclass
class TrashItem:
    media_key: str
    thumbnail_url: str
    res_width: int
    res_height: int
    timestamp: int
    dedup_key: str
    timezone_offset: int
    creation_timestamp: int
    video_duration: int | None

    @classmethod
    def from_data(cls, item_data):
        return cls(
            media_key=safe_get(item_data, 0),
            thumbnail_url=safe_get(item_data, 1, 0),
            res_width=safe_get(item_data, 1, 1),
            res_height=safe_get(item_data, 1, 2),
            timestamp=safe_get(item_data, 2),
            dedup_key=safe_get(item_data, 3),
            timezone_offset=safe_get(item_data, 4),
            creation_timestamp=safe_get(item_data, 5),
            video_duration=safe_get(item_data, -1, "76647426", 0),
        )


@dataclass
class TrashPage:
    items: list[TrashItem]
    next_page_id: str | None

    @classmethod
    def from_data(cls, data):
        return cls(
            items=[TrashItem.from_data(item) for item in safe_get(data, 0) or []],
            next_page_id=safe_get(data, 1),
        )


@dataclass
class RemoteMatch:
    hash: str
    media_key: str
    thumb: str
    res_width: int
    res_height: int
    timestamp: int
    dedup_key: str
    timezone_offset: int
    creation_timestamp: int
    video_duration: int | None
    camera_info: str | None

    @classmethod
    def from_data(cls, item_data):
        return cls(
            hash=safe_get(item_data, 0),
            media_key=safe_get(item_data, 1, 0),
            thumb=safe_get(item_data, 1, 1, 0),
            res_width=safe_get(item_data, 1, 1, 1),
            res_height=safe_get(item_data, 1, 1, 2),
            timestamp=safe_get(item_data, 1, 2),
            dedup_key=safe_get(item_data, 1, 3),
            timezone_offset=safe_get(item_data, 1, 4),
            creation_timestamp=safe_get(item_data, 1, 5),
            video_duration=safe_get(item_data, 1, -1, "76647426", 0),
            camera_info=safe_get(item_data, 1, 1, 8),
        )


@dataclass
class ItemInfo:
    media_key: str
    dedup_key: str
    res_width: int
    res_height: int
    is_partial_upload: bool
    timestamp: int
    timezone_offset: int
    creation_timestamp: int
    download_url: str
    download_original_url: str
    saved_to_your_photos: bool
    is_archived: bool
    space_taken: int
    is_original_quality: bool
    is_favorite: bool
    thumbnail_url: str
    description_full: str
    video_duration: int | None
    live_photo_duration: int | None
    live_photo_video_download_url: str | None
    trash_timestamp: int | None

    @classmethod
    def from_data(cls, item_data):
        """
        Constructs an ItemInfo instance from the given nested item_data structure.
        Uses safe_get to safely access nested values.
        """
        return cls(
            media_key=safe_get(item_data, 0, 0),
            dedup_key=safe_get(item_data, 0, 3),
            res_width=safe_get(item_data, 0, 1, 1),
            res_height=safe_get(item_data, 0, 1, 2),
            is_partial_upload=safe_get(item_data, 0, 12, 0) == 20,
            timestamp=safe_get(item_data, 0, 2),
            timezone_offset=safe_get(item_data, 0, 4),
            creation_timestamp=safe_get(item_data, 0, 5),
            download_url=safe_get(item_data, 1),
            download_original_url=safe_get(item_data, 7),
            saved_to_your_photos=len(safe_get(item_data, 0, 15, "163238866", default=[])) > 0,
            is_archived=safe_get(item_data, 0, 13),
            space_taken=safe_get(item_data, 0, 15, "318563170", 0, 1),
            is_original_quality=safe_get(item_data, 0, 15, "318563170", 0, 2) == 2,
            is_favorite=safe_get(item_data, 0, 15, "163238866", 0),
            video_duration=safe_get(item_data, 0, 15, "76647426", 0),
            live_photo_duration=safe_get(item_data, 0, 15, "146008172", 1),
            live_photo_video_download_url=safe_get(item_data, 0, 15, "146008172", 3),
            trash_timestamp=safe_get(item_data, 0, 15, "225032867", 0),
            description_full=safe_get(item_data, 10),
            thumbnail_url=safe_get(item_data, 12),
        )


@dataclass
class Actor:
    actor_id: str | None
    gaia_id: str | None
    name: str | None
    gender: str | None
    profile_photo_url: str | None

    @classmethod
    def from_data(cls, data):
        return cls(
            actor_id=safe_get(data, 0),
            gaia_id=safe_get(data, 1),
            name=safe_get(data, 11, 0),
            gender=safe_get(data, 11, 2),
            profile_photo_url=safe_get(data, 12, 0),
        )


@dataclass
class Album:
    media_key: str
    owner_actor_id: str | None
    title: str | None
    thumbnail_url: str
    item_count: int
    is_shared: bool
    creation_timestamp: int
    modified_timestamp: int
    timestamp_range: list[int | None] | None

    @classmethod
    def from_data(cls, item_data):
        return cls(
            media_key=safe_get(item_data, 0),
            owner_actor_id=safe_get(item_data, 6, 0),
            title=safe_get(item_data, -1, "72930366", 1),
            thumbnail_url=safe_get(item_data, 1, 0),
            item_count=safe_get(item_data, -1, "72930366", 3),
            creation_timestamp=safe_get(item_data, -1, "72930366", 2, 4),
            modified_timestamp=safe_get(item_data, -1, "72930366", 2, 9),
            timestamp_range=[
                safe_get(item_data, -1, "72930366", 2, 5),
                safe_get(item_data, -1, "72930366", 2, 6),
            ],
            is_shared=safe_get(item_data, -1, "72930366", 4) or False,
        )


@dataclass
class AlbumsPage:
    items: list[Album]
    next_page_id: str | None

    @classmethod
    def from_data(cls, data):
        return cls(
            items=[Album.from_data(item) for item in safe_get(data, 0) or []],
            next_page_id=safe_get(data, 1),
        )


@dataclass
class SharedLink:
    thumbnail_url: str
    item_count: int
    creation_timestamp: int
    media_key: str
    auth_key: str
    link_id: str
    members: list[Actor]
    owner: Actor

    @classmethod
    def from_data(cls, data):
        return cls(
            thumbnail_url=safe_get(data, 2, 0),
            item_count=safe_get(data, 3),
            creation_timestamp=safe_get(data, 4),
            media_key=safe_get(data, 6),
            auth_key=safe_get(data, 7),
            link_id=safe_get(data, 17),
            members=[Actor.from_data(actor_data) for actor_data in safe_get(data, 9) or []],
            owner=Actor.from_data(safe_get(data, 10, 0)),
        )


@dataclass
class SharedLinksPage:
    items: list[SharedLink]
    next_page_id: str | None

    @classmethod
    def from_data(cls, data):
        return cls(
            items=[SharedLink.from_data(item) for item in safe_get(data, 0) or []],
            next_page_id=safe_get(data, 1),
        )


@dataclass
class ItemInfoExt:
    media_key: str | None
    dedup_key: str | None
    description_full: str | None
    file_name: str | None
    timestamp: int | None
    timezone_offset: int | None
    size: int | None
    res_width: int | None
    res_height: int | None
    camera_info: str | int | None
    albums: list[Album]
    source: list[str | None]
    space_taken: int | None
    is_original_quality: bool | None
    saved_to_your_photos: bool
    owner: Actor | None
    geo_location: GeoLocation | None
    other: str | None

    @classmethod
    def from_data(cls, item_data):
        source = []

        source_map = {
            1: "mobile",
            2: "web",
            3: "shared",
            4: "partnerShared",
            7: "drive",
            8: "pc",
            11: "gmail",
        }

        source_secondary_map = {
            1: "android",
            3: "ios",
        }

        source.append(source_map.get(safe_get(item_data, 0, 27, 0)))
        source.append(source_secondary_map.get(safe_get(item_data, 0, 27, 1, 2)))

        owner = None
        if safe_get(item_data, 0, 27):
            owner = Actor.from_data(safe_get(item_data, 0, 27, 3, 0) or safe_get(item_data, 0, 27, 4, 0))
        if not owner or not owner.actor_id:
            owner = Actor.from_data(safe_get(item_data, 0, 28))

        return cls(
            media_key=safe_get(item_data, 0, 0),
            dedup_key=safe_get(item_data, 0, 11),
            description_full=safe_get(item_data, 0, 1),
            file_name=safe_get(item_data, 0, 2),
            timestamp=safe_get(item_data, 0, 3),
            timezone_offset=safe_get(item_data, 0, 4),
            size=safe_get(item_data, 0, 5),
            res_width=safe_get(item_data, 0, 6),
            res_height=safe_get(item_data, 0, 7),
            camera_info=safe_get(item_data, 0, 23),
            albums=[Album.from_data(album_data) for album_data in safe_get(item_data, 0, 19) or []],
            source=source,
            space_taken=safe_get(item_data, 0, 30, 1),
            is_original_quality=safe_get(item_data, 0, 30, 2) == 2,
            saved_to_your_photos=len(
                [sub_array for sub_array in safe_get(item_data, 0, 12, default=[]) if 20 in sub_array]
            )
            == 0,
            owner=owner,
            geo_location=GeoLocation.from_data(item_data),
            other=safe_get(item_data, 0, 31),
        )


@dataclass
class AlbumItem:
    media_key: str
    thumbnail_url: str
    res_width: int
    res_height: int
    timestamp: int
    dedup_key: str
    timezone_offset: int
    creation_timestamp: int
    live_photo_duration: int | None
    video_duration: int | None

    @classmethod
    def from_data(cls, data):
        return cls(
            media_key=safe_get(data, 0),
            thumbnail_url=safe_get(data, 1, 0),
            res_width=safe_get(data, 1, 1),
            res_height=safe_get(data, 1, 2),
            timestamp=safe_get(data, 2),
            dedup_key=safe_get(data, 3),
            timezone_offset=safe_get(data, 4),
            creation_timestamp=safe_get(data, 5),
            live_photo_duration=safe_get(data, -1, "146008172", 1),
            video_duration=safe_get(data, -1, "76647426", 0),
        )


@dataclass
class AlbumPage:
    items: list[AlbumItem]
    next_page_id: str | None
    media_key: str
    thumbnail_url: str
    title: str | None
    owner: Actor
    item_count: int
    last_activity_timestamp: int
    auth_key: str | None
    members: list[Actor]
    timestamp_range: list[int | None] | None

    @classmethod
    def from_data(cls, data):
        return cls(
            items=[AlbumItem.from_data(item) for item in safe_get(data, 1) or []],
            next_page_id=safe_get(data, 2),
            media_key=safe_get(data, 3, 0),
            thumbnail_url=safe_get(data, 3, 4, 0),
            title=safe_get(data, 3, 1),
            owner=Actor.from_data(safe_get(data, 3, 5)),
            timestamp_range=[safe_get(data, 3, 2, 5), safe_get(data, 3, 2, 6)],
            item_count=safe_get(data, 3, 21),
            last_activity_timestamp=safe_get(data, 3, 2, 9),
            auth_key=safe_get(data, 3, 19),
            members=[Actor.from_data(actor_data) for actor_data in safe_get(data, 3, 9) or []],
        )


@dataclass
class PartnerSharedItem:
    media_key: str
    thumbnail_url: str
    res_width: int
    res_height: int
    timestamp: int
    timezone_offset: int
    creation_timestamp: int
    dedup_key: str
    # is_saved: bool  # TODO: unknown parse path
    live_photo_duration: int | None
    video_duration: int | None

    @classmethod
    def from_data(cls, data):
        return cls(
            media_key=safe_get(data, 0),
            thumbnail_url=safe_get(data, 1, 0),
            res_width=safe_get(data, 1, 1),
            res_height=safe_get(data, 1, 2),
            timestamp=safe_get(data, 2),
            dedup_key=safe_get(data, 3),
            timezone_offset=safe_get(data, 4),
            creation_timestamp=safe_get(data, 5),
            live_photo_duration=safe_get(data, -1, "146008172", 1),
            video_duration=safe_get(data, -1, "76647426", 0),
        )


@dataclass
class PartnerSharedMediaPage:
    items: list[PartnerSharedItem]
    next_page_id: str | None
    members: list[Actor]
    partner_actor_id: str
    gaia_id: str

    @classmethod
    def from_data(cls, data):
        return cls(
            next_page_id=safe_get(data, 0),
            items=[PartnerSharedItem.from_data(item) for item in safe_get(data, 1) or []],
            members=[Actor.from_data(item) for item in safe_get(data, 2) or []],
            partner_actor_id=safe_get(data, 4),
            gaia_id=safe_get(data, 5),
        )


@dataclass
class ImportedDriveMedia:
    drive_key: str
    media_key: str
    dedup_key: str
    # TODO: parse more data field

    @classmethod
    def from_data(cls, data):
        return cls(
            drive_key=safe_get(data, 0),
            media_key=safe_get(data, 1, 0),
            dedup_key=safe_get(data, 1, 3),
        )


@dataclass
class ItemInfoBatch:
    media_key: str
    description_full: str
    file_name: str
    timestamp: int
    timezone_offset: int
    creation_timestamp: int
    size: int
    space_taken: int
    is_original_quality: bool

    @classmethod
    def from_data(cls, item_data):
        return cls(
            media_key=safe_get(item_data, 0),
            description_full=safe_get(item_data, 1, 2),
            file_name=safe_get(item_data, 1, 3),
            timestamp=safe_get(item_data, 1, 6),
            timezone_offset=safe_get(item_data, 1, 7),
            creation_timestamp=safe_get(item_data, 1, 8),
            size=safe_get(item_data, 1, 9),
            space_taken=safe_get(item_data, 1, -1, 1),
            is_original_quality=safe_get(item_data, 1, -1, 2) == 2,
        )


@dataclass
class StorageQuota:
    total_used: int
    total_available: int
    used_by_gphotos: int

    @classmethod
    def from_data(cls, item_data):
        return cls(
            total_used=safe_get(item_data, 6, 0),
            total_available=safe_get(item_data, 6, 1),
            used_by_gphotos=safe_get(item_data, 6, 3),
        )


@dataclass
class UnsupportedVideo:
    media_key: str
    file_name: str
    file_size: int
    timestamp: int
    thumbnail_url: str
    download_url: str
    dedup_key: str

    @classmethod
    def from_data(cls, item_data):
        return cls(
            media_key=safe_get(item_data, 0),
            file_name=safe_get(item_data, 1),
            file_size=safe_get(item_data, 2),
            timestamp=safe_get(item_data, 3),
            thumbnail_url=safe_get(item_data, 4),
            download_url=safe_get(item_data, 5),
            dedup_key=safe_get(item_data, 6),
        )


@dataclass
class UnsupportedVideosPage:
    items: list[UnsupportedVideo]
    next_page_token: str | None

    @classmethod
    def from_data(cls, data):
        return cls(
            items=[UnsupportedVideo.from_data(item) for item in safe_get(data, 1) or []],
            next_page_token=safe_get(data, 0) or None,
        )


@dataclass
class Download:
    file_name: str
    download_url: str
    download_size: int
    unzipped_size: int

    @classmethod
    def from_data(cls, item_data):
        return cls(
            file_name=safe_get(item_data, 0, 0, 0, 2, 0, 0),
            download_url=safe_get(item_data, 0, 0, 0, 2, 0, 1),
            download_size=safe_get(item_data, 0, 0, 0, 2, 0, 2),
            unzipped_size=safe_get(item_data, 0, 0, 0, 2, 0, 3),
        )


def parse_response_data(rpc_id: str, data: dict):
    match rpc_id:
        case "lcxiM":
            return LibraryTimelinePage.from_data(data)
        case "EzkLib":
            return LibraryGenericPage.from_data(data)
        case "swbisb":
            return [RemoteMatch.from_data(item) for item in safe_get(data, 0) or []]
        case "VrseUb":
            return ItemInfo.from_data(data)
        case "fDcn4b":
            return ItemInfoExt.from_data(data)
        case "zy0IHe":
            return TrashPage.from_data(data)
        case "EWgK9e":
            return [ItemInfoBatch.from_data(item) for item in safe_get(data, 0, 1) or []]
        case "Z5xsfc":
            return AlbumsPage.from_data(data)
        case "snAcKc":
            return AlbumPage.from_data(data)
        case "F2A0H":
            return SharedLinksPage.from_data(data)
        case "EzwWhf":
            return StorageQuota.from_data(data)
        case "dnv2s":
            return Download.from_data(data)
        case "e9T5je":
            return PartnerSharedMediaPage.from_data(data)
        case "SusGud":
            return [ImportedDriveMedia.from_data(item) for item in safe_get(data, 0) or []]
        case "TLvKMb":
            return UnsupportedVideosPage.from_data(data)
        case "pLFTfd":
            return safe_get(data, 0)
        case _:
            return {}
