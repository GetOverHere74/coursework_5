class Vacancy:
    """Класс принимает вакансии и фильтрует по названию, ссылке, зарплате, городу, требованиям"""

    def __init__(self, title, url, salary, city, requirements, responsibility):
        self.title = title
        self.url = url
        self.salary = salary
        self.city = city
        self.requirements = requirements
        self.responsibility = responsibility
        self.validate()

    def validate(self):
        """Функция для валидации по зарплате и требованиям"""
        if not self.salary:
            self.salary_from = 0
            self.salary_to = 0
            return

        if self.salary['from']:
            self.salary_from = 0
        else:
            self.salary_from = self.salary['from']

        if self.salary['to']:
            self.salary_to = 0
        else:
            self.salary_to = self.salary['to']

        if not self.requirements:
            self.requirements = ""

        if self.responsibility:
            self.responsibility = ""

    @classmethod
    def create_vacancies(cls, vacancies_data):
        instances = []
        for vac_info in vacancies_data:
            title = vac_info['name']
            url = vac_info['alternate_url']
            salary = vac_info['salary']
            requirements = vac_info['snippet']['requirement']
            responsibility = vac_info['snippet']['responsibility']
            city = vac_info['area']['name']
            vacancy = cls(title, url, salary, city, requirements, responsibility)
            instances.append(vacancy)

        return instances

    def __lt__(self, other):
        """Метод для сравнения вакансий"""
        if self.salary_from:
            if self.salary_from < other.salary_from:
                return True
            else:
                return False
        else:
            if other.salary_from:
                return False

    def __str__(self):
        return f"{self.title}: {self.city}: {self.salary_from}--> {self.salary_to}: {self.url}"
