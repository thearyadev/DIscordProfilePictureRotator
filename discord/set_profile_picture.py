import base64

import requests
from requests import Response

cookies = {
    '__dcfduid': '66162370afe211edb177ab37dd516f19',
    '__sdcfduid': '66162371afe211edb177ab37dd516f190227965e7a735474a7f234ca3d2cee4dbbee7348f16712d6cf7740f07e927605',
    'locale': 'en-US',
    '__cf_bm': '8EbSNNGMbPjnNLs1eIjbcBMYhBlhvonm369l7XLH1Ko-1678644357-0-Ac6pGiKxKcPi77qKXcLxNtt+DxAA7TRlo8VfVLDQmlJfeKVcjyK5Whops7++JUMABlEChafjR5g73GNjidz4UwIwY1IggB0X2C/Z0o1AD3up9YPdraBOcnHr3w5Uuul57A==',
    'OptanonConsent': 'isIABGlobal=false&datestamp=Sun+Mar+12+2023+14%3A05%3A56+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1',
    '__cfruid': '8462ccc97b93110a64aef262980fdc86193c6e69-1678644443',
}

headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': None,
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/channels/@me',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="112", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/113.0.0.0',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTMuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMTIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vYXBwLmdldGZvcmVzdC5pby8iLCJyZWZlcnJpbmdfZG9tYWluIjoiYXBwLmdldGZvcmVzdC5pbyIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxNzk4ODIsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',
}

json_data = {
    'avatar': 'data:image/png;base64,',
}


def set_profile_picture(*, auth_token: str, image: bytes) -> Response:
    headers["authorization"] = auth_token
    return requests.patch(
        'https://discord.com/api/v9/users/@me',
        cookies=cookies,
        headers=headers,
        json={"avatar": json_data["avatar"] + base64.b64encode(image).decode("utf-8")}
    )
