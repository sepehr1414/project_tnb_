from django.shortcuts import render
from .models import food

def food_list(request):
    food_list=food.objects.all()
    context= {
        "foods":food_list
      }
    return render(request,"foods/list.html",context)

def food_detail_view(request,id,*args,**kwargs):
    obj = food.objects.get(id=id)
    context={
        "obj":obj
    }
    return render(request,"foods/detail.html",context)