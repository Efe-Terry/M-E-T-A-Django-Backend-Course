from django.shortcuts import render
from django.http import HttpResponse

def home(request, name):
    alx = {
        'program': 'Software Engineer',  
        'year': '2019',  
        'grade': '99%'  
    }
    nm = alx[name]
    dp1 = f'<h1>A L X</h1><p>Student Data: {alx}</p><h3>{name} : {alx[name]}</h3>'

    students = [
        {
            'number': '00',
            'name': 'Ben',
            'Course': 'Salesforce',
            'year': '2019',
            'grade': '98%',
        },
        {
            'number': '01',
            'name': 'Carl',
            'Course': 'SWE',
            'year': '2020',
            'grade': '100%',
        },
        {
            'number': '02',
            'name': 'Matt',
            'Course': 'Cloud Computing',
            'year': '2018',
            'grade': 'Loeading%',
        },
    ]
    dp2 = f'<h1>Students</h1><br/><h3>{students}</h3>'

    return HttpResponse(dp1 + dp2)

    def index(request):
        return HttpResponse('<h1>I N D E X - A L X - A P P</h1>')














































    """
    data = [
        {
            '1': 'number - 00',
            '2': 'name - Ben',
            '3': 'Course - Salesforce',
            '4': 'year - 2019',
            '5': 'grade - 98%',
        },
        {
            '1': '01',
            '2': 'Carl',
            '3': 'SWE',
            '4': '2020',
            '5': '100%',
        },
        {
            '1': '02',
            '2': 'Matt',
            '3': 'Cloud Computing',
            '4': '2018',
            '5': 'Loeading%',
        },
    ]

    for d1 in data:
        dd = data[1]
        for dt in data:
            ddd = data[0][1]

    dp3 = f'<h1>Students</h1><br/><h3>{ddd}</h3>'
    """