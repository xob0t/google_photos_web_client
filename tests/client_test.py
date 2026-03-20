import unittest
from pathlib import Path

from gpwc import Client, payloads
from gpwc.models import DriveMedia


class TestClient(unittest.TestCase):
    def setUp(self):
        self.cookies_txt = "cookies.txt"

    def test_execute(self):
        """Client test."""
        drive_items = [
            # DriveMedia(media_key="1HOyHxyVOZECsBRm9clwkIyuE4dor58kU", mime_type="image/png"),
            DriveMedia(media_key="1fvNq1OaFO9104mAW_jY3sQ9ViXOFgGw8", mime_type="video/*"),
        ]
        payload = payloads.ImportMediaFromDrive(drive_items)
        client = Client(self.cookies_txt)
        response = payload.execute(client)
        for item in response.data:
            print(item)

    def test_SavePartnerSharedMedia(self):
        """Client test."""
        payload = payloads.SavePartnerSharedMedia(["AF1QipPVohB4XLMXCBmpN9nEYb7ewda6gjr-vWspJQWH"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request(payload)
            print(response.data)
        print(response)

    def test_GetPartnerSharedMedia(self):
        """Client test."""
        payload = payloads.GetPartnerSharedMedia(
            partner_actor_id="AF1QipOessuM__vZcZP5eOkmfQzMomlp",
            gaia_id="114233748566422460664",
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_SaveSharedMediaToLibrary(self):
        """Client test."""
        payload = payloads.SaveSharedMediaToLibrary(
            item_media_keys=["AF1QipMFIpE8fcRbp0AB7URjmtHLzONOQP44UWibI04"],
            album_media_key="AF1QipNWPWmn9NwDw8Vo8UajUQnkMfoTWFUwhNqdf4UCC5afnRCpaQSG629V47Z-kpTXyA",
            auth_key="Tm5hb3IzY0ZtY283Nlk1cng1aktEVlNhWW4xLUdR",
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_CheckDownloadToken(self):
        """Client test."""
        payload = payloads.CheckDownloadToken("1171e428-86ff-4645-bdef-ed9ba7950d12")
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
            resp = client.session.get(r.data.download_url)
            print(resp.status_code)
            with Path("file.zip").open("wb") as f:
                f.write(resp.content)
        print(response)

    def test_GetDownloadToken(self):
        """Client test."""
        payload = payloads.GetDownloadToken(["AF1QipNX93h-CBi0yOcWkFIyoHngW6YxBsH9L4fl_3zR"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetStorageQuota(self):
        """Client test."""
        payload = payloads.GetStorageQuota()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_AddItemsToExistingSharedAlbum(self):
        """Client test."""
        payload = payloads.AddItemsToExistingSharedAlbum(
            ["AF1QipNX93h-CBi0yOcWkFIyoHngW6YxBsH9L4fl_3zR"],
            "AF1QipOJPRPltt98zAzSiZKsSSMlRCwYrsvwIzz498j0KXz3HUpbGdpZOt_4V-iYdogRCA",
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_AddItemsToExistingAlbum(self):
        """Client test."""
        payload = payloads.AddItemsToExistingAlbum(
            ["AF1QipNX93h-CBi0yOcWkFIyoHngW6YxBsH9L4fl_3zR"],
            "AF1QipMoOvrCbXgb0tA5j4dy6Cpx6OycXUulbWpvMaBD",
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_AddItemsToNewAlbum(self):
        """Client test."""
        payload = payloads.AddItemsToNewAlbum(["AF1QipNX93h-CBi0yOcWkFIyoHngW6YxBsH9L4fl_3zR"], "erereas")
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_RemoveItemsFromAlbum(self):
        """Client test."""
        payload = payloads.RemoveItemsFromAlbum(["AF1QipN0qzQQnoKTCpU8tYmM_gN4yTzXOnrR02yHukAR"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetSharedLinksPage(self):
        """Client test."""
        payload = payloads.GetSharedLinksPage()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetAlbumPage(self):
        """Client test."""
        payload = payloads.GetAlbumPage("AF1QipO2JImn8daK0DKtTXZiHBU_PZErGciuD9MSbj8P")
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetAlbumsPage(self):
        """Client test."""
        payload = payloads.GetAlbumsPage()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetTrashItems(self):
        """Client test."""
        payload = payloads.GetTrashPage()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetFavoriteItems(self):
        """Client test."""
        payload = payloads.GetTrashPage()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_DeleteItemGeoData(self):
        """Client test."""
        payload = payloads.DeleteItemGeoData(
            dedup_keys=["Z8oFaP_a9WU09xZvLvdknZOUW0Y:19132b13941"],
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_SetItemGeoData(self):
        """Client test."""
        payload = payloads.SetItemGeoData(
            dedup_keys=["Z8oFaP_a9WU09xZvLvdknZOUW0Y:19132b13941"],
            center_point=[407127752, -740059728],
            visible_point_1=[404765780, -742588429],
            visible_point_2=[409177049, -737001689],
            scale=1,
            gmaps_place_id="ChIJOwg_06VPwokRYv534QaPC8g",
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_SetItemDescription(self):
        """Client test."""
        payload = payloads.SetItemDescription(
            dedup_key="Z8oFaP_a9WU09xZvLvdknZOUW0Y:19132b13941",
            description="__test__",
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_SetItemTimestamp(self):
        """Client test."""
        payload = payloads.SetItemTimestamp(
            dedup_key="Z8oFaP_a9WU09xZvLvdknZOUW0Y:19132b13941",
            timestamp=936270900,
            timezone_offset=19800,
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_UnArchive(self):
        """Client test."""
        payload = payloads.UnArchive(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_SetArchive(self):
        """Client test."""
        payload = payloads.SetArchive(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_UnFavorite(self):
        """Client test."""
        payload = payloads.UnFavorite(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_SetFavorite(self):
        """Client test."""
        payload = payloads.SetFavorite(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_CreateAlbum(self):
        """Client test."""
        payload = payloads.CreateAlbum("__TEST__")
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_RestoreFromTrash(self):
        """Client test."""
        payload = payloads.RestoreFromTrash(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_MoveToTrash(self):
        """Client test."""
        payload = payloads.MoveToTrash(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetBatchMediaInfo(self):
        """Client test."""
        payload = payloads.GetBatchMediaInfo(
            [
                "AF1QipN-pG0lbvzcuWrM2V4cMgorke21AVWIL-KPSj4P",
                "AF1QipMohHAqtyGq4IQsgYrnGvnaQG8e5E4Hzu3YBG6x",
            ]
        )
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetRemoteMatchesByHash(self):
        """Client test."""
        payload = payloads.GetRemoteMatchesByHash(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetItemInfoExt(self):
        """Client test."""
        payload = payloads.GetItemInfoExt("AF1QipN-pG0lbvzcuWrM2V4cMgorke21AVWIL-KPSj4P")
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetItemInfo(self):
        """Client test."""
        payload = payloads.GetItemInfo("AF1QipPngr1BjPGq2U5jWvsr9HoDQTFv8HPf_QPD06s_")
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetLibraryPageByTakenDate(self):
        """Client test."""
        payload = payloads.GetLibraryPageByTakenDate()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request(payload)
            print(response.data)

    def test_GetLibarayPageByUploadedDate(self):
        """Client context test."""
        payload = payloads.GetLibarayPageByUploadedDate()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetUnsupportedVideos(self):
        """Client test."""
        payload = payloads.GetUnsupportedVideos()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([payload])
        for r in response:
            print(r.data)
        print(response)

    def test_GetUnsupportedVideoDownloadUrl(self):
        """Client test."""
        # First get the list of unsupported videos
        list_payload = payloads.GetUnsupportedVideos()
        with Client(self.cookies_txt) as client:
            list_response = client.send_api_request([list_payload])
            media_keys = [item.media_key for item in list_response[0].data.items[:2]]
            # Then get the download URL for the first 2
            dl_payload = payloads.GetUnsupportedVideoDownloadUrl(media_keys)
            dl_response = client.send_api_request([dl_payload])
            for r in dl_response:
                print(r.data)
            print(dl_response)


if __name__ == "__main__":
    unittest.main()
