
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
        if not self.salary:
            self.salary_from = 0
            self.salary_to = 0
