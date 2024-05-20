import json
import os
from abc import ABC, abstractmethod
from config import DATA_PATH
from src.vacancy import Vacancy


class BaseWorker(ABC):
    """Абстрактный класс для работы с вакансиями"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def select_vacancy(self, keyword):
        pass

class JSONWorker(BaseWorker):
    """Класс для работы с вакансиями в формате JSON"""
    def __init__(self, file_name):
        self.file_path = os.path.join(DATA_PATH, file_name)
        self.prepare()

    def prepare(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump([], file)

    def add_vacancy(self, vacancy):
        with open(self.file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(vars(vacancy))
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancies(self, vacancies):
        with open(self.file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            for vacancy in vacancies:
                data.append(vars(vacancy))
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def del_vacancy(self, vacancy):
        with open(self.file_path, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data = [v for v in data if v != vars(vacancy)]
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)

    def select_vacancy(self, keyword):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            filtered_vacancies = [v for v in data if keyword.lower() in v['title'].lower() or keyword.lower() in v['requirements'].lower() or keyword.lower() in v['responsibility'].lower()]
            return [Vacancy(**v) for v in filtered_vacancies]