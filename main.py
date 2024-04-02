import tls_client
import time
import datetime
import os

red = '\x1b[31m(-)\x1b[0m'
blue = '\x1b[34m(+)\x1b[0m'
green = '\x1b[32m(+)\x1b[0m'
yellow = '\x1b[33m(!)\x1b[0m'

def get_timestamp():
    time_idk = datetime.datetime.now().strftime('%H:%M:%S')
    timestamp = f'[\x1b[90m{time_idk}\x1b[0m]'
    return timestamp

class DiscordSession:
    def __init__(self, client_identifier="chrome112"):
        self.session = tls_client.Session(client_identifier=client_identifier, random_tls_extension_order=True)

    def post(self, url, headers):
        return self.session.post(url, headers=headers)

class LootBoxOpener:
    lootbox_items = {
        "1214340999644446726": "Quack!!",
        "1214340999644446724": "⮕⬆⬇⮕⬆⬇",
        "1214340999644446722": "Wump Shell",
        "1214340999644446720": "Buster Blade",
        "1214340999644446725": "Power Helmet",
        "1214340999644446723": "Speed Boost",
        "1214340999644446721": "Cute Plushie",
        "1214340999644446728": "Dream Hammer",
        "1214340999644446727": "OHHHHH BANANA"
    }

    def __init__(self, discord_session, token):
        self.discord_session = discord_session
        self.token = token
        self.headers = {
            'authority': 'discord.com',
            'accept': '*/*',
            'accept-language': 'en-US',
            'authorization': token,
            'origin': 'https://discord.com',
            'referer': 'https://discord.com/channels/1222747973205758002/1224417703100551169',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9037 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US',
            'x-discord-timezone': 'Asia/Calcutta',
            'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDM3Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MzEiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMzcgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyODA3MDAsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQ1MzY5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        }

    def open_lootbox(self):
        response = self.discord_session.post('https://discord.com/api/v9/users/@me/lootboxes/open', headers=self.headers)
        if 'rate limited' in response.text:
            print(f"{get_timestamp()} {yellow} You Are Being Rate Limited!")
            time.sleep(2)
        elif response.status_code == 200:
            opened_item = response.json().get('opened_item')
            if opened_item in self.lootbox_items:
                print(f"{get_timestamp()} {green} Successfully Opened A Lootbox : {self.lootbox_items[opened_item]}")
            else:
                print(f"{get_timestamp()} {red} An Unknown Item Was Received.")
        else:
            print(f'{get_timestamp()} {red} An Error Occurred : {response.status_code} - {response.text}')

def main():
    token = input(f"{get_timestamp()} {blue} Please Enter Your Account Token : ")
    discord_session = DiscordSession()
    lootbox_opener = LootBoxOpener(discord_session, token)
    
    while True:
        lootbox_opener.open_lootbox()
        time.sleep(1)

if __name__ == "__main__":
    os.system("cls")
    main()
