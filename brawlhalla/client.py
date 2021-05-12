import requests


class Brawlhalla:
    def __init__(self, api_key):
        self.api_key = api_key
        self.Player = Player(api_key)
        self.Legend = Legend(api_key)
        self.Clan = Clan(api_key)
        self.Ranking = Ranking(api_key)


class Player:
    BASE_URL = "https://api.brawlhalla.com"

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_key_param = f"?api_key={api_key}"

    def get(self, id=None):
        if id is None:
            return
        endpoint = f"{self.BASE_URL}/player/{id}/stats{self.api_key_param}"
        return requests.get(endpoint).json()

    def find(self):
        pass

    def get_ranked(self):
        if id is None:
            return
        endpoint = f"{self.BASE_URL}/player/{id}/ranked{self.api_key_param}"
        return requests.get(endpoint).json()


class Legend:
    BASE_URL = "https://api.brawlhalla.com"

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_key_param = f"?api_key={api_key}"

    def get(self, id=None):
        if id is None:
            return
        endpoint = f"{self.BASE_URL}/legend/{id}/{self.api_key_param}"
        return requests.get(endpoint).json()

    def get_all(self):
        endpoint = f"{self.BASE_URL}/legend/all/{self.api_key_param}"
        return requests.get(endpoint).json()


class Clan:
    BASE_URL = "https://api.brawlhalla.com"

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_key_param = f"?api_key={api_key}"

    def get(self, bracket=None, location=None, page=None):
        endpoint = (
            f"{self.BASE_URL}/rankings/{bracket}/{location}/{page}{self.api_key_param}"
        )
        return requests.get(endpoint).json()


class Ranking:
    BASE_URL = "https://api.brawlhalla.com"

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_key_param = f"?api_key={api_key}"

    def get(self, id=None):
        if id is None:
            return
        endpoint = f"{self.BASE_URL}/clan/{id}/{self.api_key_param}"
        return requests.get(endpoint).json()
