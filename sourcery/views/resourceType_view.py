from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from sourcery.models import Resource_Type
from sourcery.forms import Resource_Type_Form

from django.contrib.auth.decorators import login_required

@login_required
def resourceTypeList(request):
    current_user = request.user
    all_types = Resource_Type.objects.filter(user_id=current_user.id)
    context = { 'all_types' : all_types }
    print("all_typesssss", all_types)
    return render(request, 'sourcery/resourceTypeList.html', context)


def addResourceType(request):
    
    if request.method == "POST":
        user = request.user
        name = request.POST["resource_type_name"]

    new_resource_type = Resource_Type.objects.create(
        name = name,
        user = user
    )

    return HttpResponseRedirect(reverse('sourcery:index'))