from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect, get_object_or_404
from . import models
from .forms import Shop

def hp(request):

    if request.method == "POST":
        form = Shop(request.POST)
        if form.is_valid():
            new_star = form.save() 
            return bye(request,str(new_star.pk))

    else:
        form = Shop()
    return render(request,'starshop/hp.html', {"form": form})
    
def bye(request,key):
        return render(request,'starshop/bye.html',context={"star": get_object_or_404(models.Star, pk=key)})

def basic(request):
     return render(request,'starshop/basic.html',context={'star_list':models.Star.objects.all()})