import requests


class Brawlhalla:
    def __init__(self, api_key):
        self.api_key = api_key
        self.Player = Player(api_key)
        self.Legend = Legend(api_key)
        self.Clan = Clan(api_key)
        self.Ranking = Ranking(api_key)


class BaseType:
    BASE_URL = "https://api.brawlhalla.com"

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_key_param = f"?api_key={api_key}"


class Player(BaseType):
    def get(self, id):
        endpoint = f"{self.BASE_URL}/player/{id}/stats{self.api_key_param}"
        return requests.get(endpoint).json()

    def find(self):
        pass

    def get_ranked(self, id):
        endpoint = f"{self.BASE_URL}/player/{id}/ranked{self.api_key_param}"
        return requests.get(endpoint).json()


class Legend(BaseType):
    def get(self, id):
        endpoint = f"{self.BASE_URL}/legend/{id}/{self.api_key_param}"
        return requests.get(endpoint).json()

    def get_all(self):
        endpoint = f"{self.BASE_URL}/legend/all/{self.api_key_param}"
        return requests.get(endpoint).json()


class Leaderboards(BaseType):
    def get(self, bracket, location, page):
        endpoint = f"{self.BASE_URL}/rankings/{bracket}/{location}/{page}{self.api_key_param}"
        return requests.get(endpoint).json()


class Clan(BaseType):
    def get(self, id):
        endpoint = f"{self.BASE_URL}/clan/{id}/{self.api_key_param}"
        return requests.get(endpoint).json()


class Ranking(BaseType):
    def get(self, id):
        endpoint = f"{self.BASE_URL}/player/{id}/ranked/{self.api_key_param}"
        return requests.get(endpoint).json()
