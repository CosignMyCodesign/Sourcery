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
    context = { 'all_resources' : all_resources , 'all_types' : all_types}
    return render(request, 'sourcery/resourceGrid.html', context)

def resourceForm(request):
    '''
    [Renders the add new department form template]
    '''
    current_user = request.user
    all_types = Resource_Type.objects.filter(user_id=current_user.id)
    return render(request, 'sourcery/addResource.html', {'all_types':all_types})

def addResource(request):

    user = request.user
    title = request.POST["resource_title"]
    url = request.POST["resource_url"]
    image = request.POST["resource_image"]
    note = request.POST["resource_note"]
    resource_type_id = request.POST["type"]
   
    resource_type_instance = Resource_Type.objects.get(id=resource_type_id)

    new_resource = Resource.objects.create(
        title = title,
        user = user,
        url = url,
        image = image,
        note = note,
        isCompleted = 0,
        resource_type = resource_type_instance

    )

    return HttpResponseRedirect(reverse('sourcery:resourceGrid', args=(resource_type_instance.id, user.id,)))


def editResourceForm(request, resource_id):
    current_user = request.user
    all_types = Resource_Type.objects.filter(user_id=current_user.id)

    resource = get_object_or_404(Resource, pk=resource_id)

    context = {'resource': resource, 'all_types': all_types}
    return render(request, 'sourcery/editResource.html', context)

def editResource( request, resource_id):
    current_user = request.user
    all_types = Resource_Type.objects.filter(user_id=current_user.id)
    resource = Resource.objects.get(id=resource_id)

    resource.title = request.POST['resource_title']
    resource.url = request.POST['resource_url']
    resource.image = request.POST['resource_image']
    resource.note = request.POST['resource_note']

    resource.save()
    return HttpResponseRedirect(reverse('sourcery:resourceGrid', args=(resource.resource_type.id, current_user.id,)))

def deleteResource(request, resource_id):
    current_user = request.user
    resource = get_object_or_404(Resource, pk=resource_id)

    resource.delete()
    return HttpResponseRedirect(reverse('sourcery:resourceGrid', args=(resource.resource_type.id, current_user.id,)))