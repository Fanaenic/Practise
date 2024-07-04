import requests
from bs4 import BeautifulSoup

def parse_habr_vacancies(query):
    url = f'https://career.habr.com/vacancies?q={query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    vacancies = []
    for card in soup.find_all('div', class_='vacancy-card__inner'):
        vacancy_company = card.find('a', class_="link-comp link-comp--appearance-dark").text
        vacancy_name = card.find('a', class_='vacancy-card__title-link').text
        vacancy_add = card.find('div', class_='vacancy-card__meta')
        vacancy_salary = card.find('div', class_='vacancy-card__salary').text if card.find('div', class_='vacancy-card__salary') else 'Not specified'
        vacancy_link = 'https://career.habr.com' + card.find('a', class_='vacancy-card__title-link')['href']

        data = []
        for i in vacancy_add.find_all('span', class_='preserve-line'):
            data.append(i.text)

        vacancies.append({
            'name': vacancy_name,
            'company': vacancy_company,
            'add': data,
            'salary': vacancy_salary,
            'link': vacancy_link,
        })

    return vacancies

def parse_habr_resumes(query):
    url = f'https://career.habr.com/resumes?q={query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    resumes = []
    for card in soup.find_all('div', class_="resume-card__body"):
        resume_name = card.find('a', class_="resume-card__title-link").text
        resume_post = card.find('div', class_="resume-card__specialization").text
        resume_add = card.find('div', class_="resume-card__offer").text.strip()
        resume_skills = card.find_all('div', class_="content-section")
        resume_link = 'https://career.habr.com' + card.find('a', class_='resume-card__title-link')['href']

        
        skills = []
        for skill in resume_skills:
            skills.append(skill.text.strip())

        resumes.append({
            'name': resume_name,
            'post': resume_post,
            'add': resume_add,
            'skills': skills,
            'link':resume_link
        })

    return resumes


