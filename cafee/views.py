from django.shortcuts import render
from cafe.models import Enquiry,burgers,beverage,sandwich,frenchfries,dessert,pizzas
def index(request):
    data={}
    try:
        if request.method=="POST":
            name=(request.POST['name'])
            number=(request.POST['number'])
            members=(request.POST['members'])
            date=(request.POST['date'])
            obj=Enquiry(name=name,number=number,members=members,date=date,)
            obj.save()
    except:
        pass
    return render (request,'index.html',data)

def burger(request):
    obj=burgers.objects.all()
    data={
        'obj':obj
    }
    return render (request,'burger.html',data)

def beverages(request):
    obj1=beverage.objects.all()
    data={
        'obj1':obj1
    }
    return render (request,'beverages.html',data)

def sandwiches(request):
    obj2=sandwich.objects.all()
    data={
        'obj2':obj2
    }
    return render(request,'sandwiches.html',data)

def fries(request):
    obj3=frenchfries.objects.all()
    data={
        'obj3':obj3
    }
    return render(request,'fries.html',data)

def desserts(request):
    obj4=dessert.objects.all()
    data={
        'obj4':obj4
    }
    return render(request,'desserts.html',data)

def pizza(request):
    obj5=pizzas.objects.all()
    data={
        'obj5':obj5
    }
    return render(request,'pizza.html',data)
