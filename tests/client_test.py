import unittest

from gpwc import Client, payloads


class TestClient(unittest.TestCase):
    def setUp(self):
        self.cookies_txt = "cookies.txt"

    def test_GetFavoriteItems(self):
        """Client test."""
        payload = payloads.GetFavoriteItems()
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_DeleteItemGeoData(self):
        """Client test."""
        payload = payloads.DeleteItemGeoData(
            dedup_keys=["Z8oFaP_a9WU09xZvLvdknZOUW0Y:19132b13941"],
        )
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
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
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_SetItemDescription(self):
        """Client test."""
        payload = payloads.SetItemDescription(
            dedup_key="Z8oFaP_a9WU09xZvLvdknZOUW0Y:19132b13941",
            description="__test__",
        )
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_SetItemTimestamp(self):
        """Client test."""
        payload = payloads.SetItemTimestamp(
            dedup_key="Z8oFaP_a9WU09xZvLvdknZOUW0Y:19132b13941",
            timestamp=936270900,
            timezone_offset=19800,
        )
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_UnArchive(self):
        """Client test."""
        payload = payloads.UnArchive(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_SetArchive(self):
        """Client test."""
        payload = payloads.SetArchive(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_UnFavorite(self):
        """Client test."""
        payload = payloads.UnFavorite(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_SetFavorite(self):
        """Client test."""
        payload = payloads.SetFavorite(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_CreateAlbum(self):
        """Client test."""
        payload = payloads.CreateAlbum("__TEST__")
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_RestoreFromTrash(self):
        """Client test."""
        payload = payloads.RestoreFromTrash(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_MoveToTrash(self):
        """Client test."""
        payload = payloads.MoveToTrash(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_GetBatchMediaInfo(self):
        """Client test."""
        payload = payloads.GetBatchMediaInfo(["AF1QipN-pG0lbvzcuWrM2V4cMgorke21AVWIL-KPSj4P", "AF1QipMohHAqtyGq4IQsgYrnGvnaQG8e5E4Hzu3YBG6x"])
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_GetRemoteMatchesByHash(self):
        """Client test."""
        payload = payloads.GetRemoteMatchesByHash(["0J7Wh1iXHA4BalGgYaK9sDyxkW4"])
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_GetItemInfoExt(self):
        """Client test."""
        payload = payloads.GetItemInfoExt("AF1QipN-pG0lbvzcuWrM2V4cMgorke21AVWIL-KPSj4P")
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_GetItemInfo(self):
        """Client test."""
        payload = payloads.GetItemInfo("AF1QipN-pG0lbvzcuWrM2V4cMgorke21AVWIL-KPSj4P")
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_client(self):
        """Client test."""
        payload = payloads.GetItemsByTakenDate()
        client = Client(self.cookies_txt)
        response = client.send_api_request([payload])[0]
        client.save_cookies_to_file()
        print(response)

    def test_client_context(self):
        """Client context test."""
        taken = payloads.GetItemsByTakenDate()
        uploaded = payloads.GetItemsByUploadedDate()
        with Client(self.cookies_txt) as client:
            response = client.send_api_request([taken, uploaded])
        for r in response:
            print(r.data)
        print(response)


if __name__ == "__main__":
    unittest.main()
