import pytest
import json
import os
from src.vacancy import Vacancy
from src.worker import JSONWorker


@pytest.fixture
def json_worker(tmp_path):
    file_path = tmp_path / "test_vacancies.json"
    return JSONWorker(file_path)


@pytest.fixture
def sample_vacancy():
    return Vacancy("Python Developer", "example.com", {"from": 50000, "to": 70000}, "Москва", "Python",
                   "SQL")


def test_add_vacancy(json_worker, sample_vacancy):
    json_worker.add_vacancy(sample_vacancy)
    with open(json_worker.file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        assert len(data) == 1
        assert data[0]['title'] == sample_vacancy.title


def test_add_vacancies(json_worker, sample_vacancy):
    vacancies = [sample_vacancy, sample_vacancy]
    json_worker.add_vacancies(vacancies)
    with open(json_worker.file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        assert len(data) == 2
        assert data[0]['title'] == sample_vacancy.title
        assert data[1]['title'] == sample_vacancy.title


def test_del_vacancy(json_worker, sample_vacancy):
    json_worker.add_vacancy(sample_vacancy)
    json_worker.del_vacancy(sample_vacancy)
    with open(json_worker.file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        assert len(data) == 1


def test_select_vacancy(json_worker, sample_vacancy):
    json_worker.add_vacancy(sample_vacancy)
    selected_vacancies = json_worker.select_vacancy("Developer")
    assert len(selected_vacancies) == 1
    assert selected_vacancies[0].title == sample_vacancy.title
