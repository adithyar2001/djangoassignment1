from django.shortcuts import render,redirect
from .forms import signupform
from .models import usertable
from django.contrib.auth import authenticate, login as log,logout
from django.contrib.auth.models import User,auth

from django.core.mail import send_mail
# Create your views here.



# def signup(request):
#     form = signupform()
#     if request.method == "POST":
#         form = signupform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#     return render(request,"signup.html",{'form':form})
def signup(request):
    form = signupform(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            
            # password = form.cleaned_data['password']
            # confirm_password = form.cleaned_data['confirm_password']
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            if len(password)>=6 and password == confirm_password:
                form.save()
                return redirect('login')  # Redirect to a success page or login page
            else:
                ermsg = "Password must be greater than 6 letters and passwords must be same."
                return render(request, 'signup.html', {'form': form,'ermsg':ermsg})
    else:
        return render(request, 'signup.html', {'form': form})
    
def loginredirect(request):
            username=request.session['username']
            id=request.session['id']
            return render(request,"loginredirect.html",{'username':username,'id':id})
        
def userlogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        cr = usertable.objects.filter(username=username,password=password)
        if cr:
            user_details = usertable.objects.get(username=username,password=password) 
            id = user_details.id
            username = user_details.username
            email = user_details.email
            
            request.session['id']= id 
            request.session['username']=username
            request.session['email']=email
            send_mail(
                "login",
                "LOGIN SUCCESSFULL",
                "adithya54756@gmail.com",
                [email],
                fail_silently=False
            )
            return redirect("loginredirect") 
        else:
            cb = 'invalid login'
            return render(request,"login.html",{'cb':cb})
    else:
        return render(request,"login.html")

def login(request):
    return render(request,"login.html")

def delete(request,pk):
    cr  = usertable.objects.get(id = pk)
    cr.delete()
    return redirect("login")

def view(request):
    cr = usertable.objects.all()
    return render(request,"views.html",{'cr':cr})

def updateuser(request,pk):
    cr = usertable.objects.get(id=pk)
    form = signupform(instance = cr)
    if request.method=="POST":
        form = signupform(request.POST,instance=cr)
        if form.is_valid:
            form.save()
            return redirect("loginredirect") 
    return render(request,"update.html",{'form':form})

def userlogout(request):
    logout(request) 
    return redirect("login")

def detailview(request,pk):
    cr = usertable.objects.get(id=pk)
    return render(request,"detailview.html",{'cm':cr})

def adloginfunc(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('view')
        else:
            er = "invalid login"
            return render(request,"adminlogin.html",{'er':er})
    else:
        return render(request,"admin.html")

def adminlogin(request):
    return render(request,"adminlogin.html")
