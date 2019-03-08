from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from sourcery.models import Resource_Type

from django.contrib.auth.decorators import login_required

@login_required
def resourceTypeList(request):
    current_user = request.user
    all_types = Resource_Type.objects.filter(user_id=current_user.id)
    context = { 'all_types' : all_types }
    print("all_typesssss", all_types)
    return render(request, 'sourcery/resourceTypeList.html', context)