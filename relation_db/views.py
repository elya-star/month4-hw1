from django.shortcuts import render
from . import models


def relation_db(request):
    if request.method == 'GET':
        name_person = models.Person.objects.all()
        return render (
            request, 
            'relation_db.html', 
            {
                "name_person": name_person
            }
        )
# Create your views here.
