from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from sourcery.models import Resource_Type, Resource

from django.contrib.auth.decorators import login_required

@login_required
def resourceGrid(request, user_id, resource_type_id):
    current_user = request.user
    all_types = Resource_Type.objects.filter(user_id=current_user.id)
    all_resources = Resource.objects.filter(resource_type_id=resource_type_id)
    context = { 'all_resources' : all_resources , 'all_types' : all_types }
    print("CONTEEEEEEXXT", context)
    return render(request, 'sourcery/resourceGrid.html', context)

def addResource(request):
    
    if request.method == "POST":
        user = request.user
        title = request.POST["resource_title"]
        url = request.POST["resource_url"]
        image = request.POST["resource_image"]
        # title = request.POST["resource_type_name"]

    new_resource = Resource.objects.create(
        title = title,
        user = user,
        url = url,
        image = image,
    )

    return HttpResponseRedirect(reverse('sourcery:index'))