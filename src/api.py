
import requests
from abc import ABC, abstractmethod


class BaseAPI(ABC):
    """Абстрактный класс для API запроса"""
    @abstractmethod
    def get_vacancies(self, keyword, count):
        pass


class HHApi(BaseAPI):
    """Класс для работы с API hh.ru"""
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.params = {
                       'text': '',
                       'page': 0,
                       'per_page': 100
        }

    def get_vacancies(self, keyword, count):
        self.params.update({'text': keyword})
        response = requests.get(self.url, params=self.params)
        return response.json()['items']

if __name__ == '__main__':
    my_api = HHApi().get_vacancies()
    response = my_api.get_vacancies()
    pass
