from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from sourcery.models import Resource_Type, Resource

from django.contrib.auth.decorators import login_required

@login_required
def resourceGrid(request):
    all_types = Resource_Type.objects.all()
    all_resources = Resource.objects.all()
    context = { 'all_resources' : all_resources , 'all_types' : all_types }
    print("CONTEEEEEEXXT", context)
    return render(request, 'sourcery/resourceGrid.html', context)