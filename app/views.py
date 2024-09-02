from django.shortcuts import render
from .models import Student


# Create your views here.


def index(request):
    # Method-1 inserting new record
    # student = Student(name='John Doe', city='New York', age=20)
    # student.save()

    # Method-2 inserting new record
    # student = Student()
    # student.name = 'Hassan Ali'
    # student.city = 'Lahore'
    # student.age = 24
    # student.save()

    # Fetching data from database

    std = Student.objects.all()  # Fetch all objects

    context = {'data': std}

    print(context)

    return render(request, 'home.html', context)
