from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from ..models import Resource_Type

def resourceTypeList(request):

    all_types = Resource_Type.objects.all()
    context = { 'all_types' : all_types }
    print("CONTEXT", context)
    return render(request, 'sourcery/resourceTypeList.html', context)