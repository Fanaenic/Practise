from django.shortcuts import render
from .models import Vacancy, Resume
from .parser import parse_habr_vacancies, parse_habr_resumes

def index(request):
    return render(request, 'main/index.html')

def vacancies(request):
    query = request.GET.get('query', 'python')  # Пример запроса по умолчанию
    vacancies_list = parse_habr_vacancies(query)
    
    # Сохранение данных в базу данных
    for vacancy_data in vacancies_list:
        Vacancy.objects.create(
            title=vacancy_data['name'],
            company=vacancy_data['company'],
            location=vacancy_data['add'][0],  # Предположим, что первый элемент в "add" это местоположение
            salary=vacancy_data['salary'],
            description=', '.join(vacancy_data['add'][1:]),  # Описание объединяем в одну строку
            url=vacancy_data['link'],
            source='Habr Career'
        )

    return render(request, 'main/vacancies.html', {'vacancies': vacancies_list, 'query': query})

def resumes(request):
    query = 'python developer'  # Укажите свой запрос здесь, если необходимо
    resumes_list = parse_habr_resumes(query)
    
    # Сохранение данных в базу данных
    for resume_data in resumes_list:
        Resume.objects.create(
            name=resume_data['name'],
            skills=', '.join(resume_data['skills']),  # Навыки объединяем в одну строку
            experience=resume_data['add'],  # Предположим, что это опыт работы
            education='',  # Добавьте соответствующее поле, если нужно
            desired_position=resume_data['post'],  # Предположим, что это желаемая должность
            url=resume_data['link'],
            source='Habr Career'
        )

    return render(request, 'main/resumes.html', {'resumes': resumes_list})
