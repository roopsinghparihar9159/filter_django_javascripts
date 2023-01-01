from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.list import ListView
from .models import State
# Create your views here.
class StateList(ListView):
    model = State
    template_name="mainapp/state_list.html"

    def get_queryset(self, *args, **kwargs):
        qs = super(StateList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

def jsonlink(request):
    query =list(State.objects.values()) 
    return JsonResponse(query,safe=False)