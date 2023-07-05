from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import get_user_model,login,authenticate,logout
from .models import person,addr

user=get_user_model()


# Create your views here.
def home(request):
    return render(request,'home/index.html')
    

def about(request):
    return render(request,'home/about.html')

def reg(request):
     if request.method == 'POST':
        phone_number = request.POST.get('phone')
        password=request.POST.get('pwd')
        user_bio=request.POST.get('userbio')
        myuser=user.objects.create_user(phone_number,password)
        myuser.save()
        messages.success(request,"new user created successfully..")
        return render(request,'home/reg.html')
     else:
           return render(request,'home/reg.html')
  

def signup(request):
    if request.method=='POST':
        phone=request.POST.get('phone')
        password=request.POST.get('pwd')       
        u=authenticate(request,phone_number=phone,password=password)
        if u is not None:
            login(request,u)
            context={"uu":u}
            messages.success(request,'Login successfully..')
            return render(request,'home/login.html',context)
            print(user)
        else:
            messages.warning(request,"invalid credentials!")
            return render(request,'home/login.html')
    else:
        logout(request)
        return render(request,'home/login.html')
        

def customer(request):
    if request.method=="POST":
        name=request.POST.get('cname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        cu=person(name=name,phone=phone,email=email)
        cu.save()
        messages.info(request,"Customer added Successfully...")
        return render(request,'home/customers.html')
    else:
        cc=addr.objects.all().prefetch_related('person_id')
        dd=addr.objects.filter(person_id=1)
        per=person.objects.all()
        context={"cc":cc,
                 "dd":dd,
                 "per":per}
        return render(request,'home/customers.html',context)

def updateperson(request,id):
    personobj=person.objects.get(pk=id).delete()
    return redirect('loginpage')