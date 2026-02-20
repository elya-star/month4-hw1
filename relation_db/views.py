from django.views.generic import ListView
from . import models


class RelationDBView(ListView):
    model = models.Person
    template_name = "relation_db.html"
    context_object_name = "name_person"

