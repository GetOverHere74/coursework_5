import json
import os
from abc import ABC, abstractmethod
from config import DATA_PATH


class BaseWorker(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass

    @abstractmethod
    def select_vacancy(self, keyword):
        pass

class JSONWorker(BaseWorker):
    def __init__(self, file_name):
        self.file_path = os.path.join(DATA_PATH, file_name)
        self.prepare()

    def prepare(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def add_vacancy(self, vacancy):
        pass

    def add_vacancies(self, vacancies):
        pass

    def del_vacancy(self, vacancy):
        pass

    def select_vacancy(self, keyword):
        pass