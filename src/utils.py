from src.api import HHApi
from src.vacancy import Vacancy
from src.worker import JSONWorker


def user_interaction():
    """Метод для работы с пользователем"""
    api_hh = HHApi()
    keyword_user = input('Введите поисковый запрос: ')
    vacancies_info = api_hh.get_vacancies(keyword_user, 100)
    vacancies = Vacancy.create_vacancies(vacancies_info)
    result = sorted(vacancies)
    for vacancy in result:
        print(vacancy)

    file_worker = JSONWorker('vacancies.json')

    choice = input("Хотите сохранить найденные вакансии? (yes/no): ")
    if choice.lower() == 'yes':
        file_worker.add_vacancies(vacancies)
        print("Вакансии успешно сохранены!")
    else:
        print("Вакансии не сохранены.")

    search_keyword = input("Введите ключевое слово для поиска вакансий: ")
    found_vacancies = file_worker.select_vacancy(search_keyword)
    if found_vacancies:
        print(f"Найдены следующие вакансии по ключевому слову '{search_keyword}':")
        for vacancy in found_vacancies:
            print(vacancy)
    else:
        print(f"По ключевому слову '{search_keyword}' вакансий не найдено.")


if __name__ == '__main__':
    user_interaction()
