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

def resourceForm(request):
    '''
    [Renders the add new department form template]
    '''
    current_user = request.user
    all_types = Resource_Type.objects.filter(user_id=current_user.id)
    return render(request, 'sourcery/addResource.html', {'all_types':all_types})

def addResource(request):
    print("hello")
    user = request.user
    title = request.POST["resource_title"]
    url = request.POST["resource_url"]
    image = request.POST["resource_image"]
    note = request.POST["resource_note"]
    resource_type_id = request.POST["type"]
    print("**************", resource_type_id)
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

    return HttpResponseRedirect(reverse('sourcery:index'))

    #  if request.method == 'GET':
    #     payment_form = AddPaymentForm()
    #     template_name = 'profile/add_payment.html'
    #     return render(request, template_name, {'payment_form': payment_form})

    
    # if request.method == "POST":
    #     customer = request.user.id
    #     name = request.POST["name"]
    #     accountNumber = request.POST["accountNumber"]

    # with connection.cursor() as cursor:
    #     cursor.execute("INSERT into website_paymenttype VALUES(%s, %s, %s, %s, %s)", [None, name, accountNumber, None, customer])
    #     return HttpResponseRedirect(reverse('website:profile'))