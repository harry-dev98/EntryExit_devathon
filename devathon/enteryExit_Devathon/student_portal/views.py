from django.shortcuts import render
from .forms import *
from .models import *

def studentportal(request):
    form = orderDetails()
    if request.method = "GET":
        form = orderDetails(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            data = orderDetails()
            data.rollNo =  cd['rollNo']
            data.itemName = cd['itemName']
            data.company = cd['company']
            data.deliveryGuyContact = cd['deliveryGuyContact']
            data.save()
            return redirect('thanks')
        else:
            return render(request, '',{'form':form})

    return render(request, '',{'form':form})

def thanks(request):
    render(request,'')
