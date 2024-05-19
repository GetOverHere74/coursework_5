from abc import ABC, abstractmethod


class BaseAPI(ABC):
    @abstractmethod
    def get_vacancies(self, keyword, count):
        pass


class HHApi(BaseAPI):
    def __init__(self):
        pass

    def get_vacancies(self, keyword, count):
        pass

my_api = HHApi().get_vacancies(user_input, user_count)
