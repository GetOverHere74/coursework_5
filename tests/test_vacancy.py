import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy_with_salary():
    return Vacancy("Python Developer", "example.com", {"from": 50000, "to": 70000}, "Москва", "Python", "SQL")

@pytest.fixture
def vacancy_without_salary():
    return Vacancy("Backend Developer", "example.com", None, "Москва", "Django", "CRM")

def test_str_with_salary(vacancy_with_salary):
    expected_output = "Python Developer: Москва: 50000 --> 70000: example.com"
    assert str(vacancy_with_salary) == expected_output

def test_str_without_salary(vacancy_without_salary):
    expected_output = "Backend Developer: Москва: Не указана --> Не указана: example.com"
    assert str(vacancy_without_salary) == expected_output