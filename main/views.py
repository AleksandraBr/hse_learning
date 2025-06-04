from django.shortcuts import render
from .models import Student, Program, Manager, Classmate

def index(request):
    return render(request, 'main/index.html')

def about_me(request):
    student = Student.objects.first()
    return render(request, 'main/about_me.html', {'student': student})

def program(request):
    program = Program.objects.first()
    return render(request, 'main/program.html', {'program': program})

def management(request):
    academic_leader = Manager.objects.filter(role='academic').first()
    managers = Manager.objects.filter(role='manager')
    return render(request, 'main/management.html', {
        'academic_leader': academic_leader,
        'managers': managers
    })


def classmates(request):
    classmates_list = Classmate.objects.all().order_by('full_name')

    search_query = request.GET.get('search', '')
    if search_query:
        classmates_list = classmates_list.filter(full_name__icontains=search_query)

    return render(request, 'main/classmates.html', {
        'classmates': classmates_list,
        'search_query': search_query
    })
