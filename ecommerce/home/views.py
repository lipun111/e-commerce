from django.shortcuts import render,redirect
from home.forms import ContactForm, UserRegistrationForm, LoginForm, GuestForm
from django.contrib.auth import authenticate, login
from .models import Contact, GuestEmail
from django.utils.http import is_safe_url
# Create your views here.

def home_View(request):
    return render(request,'home/home.html')


def register_view(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/register.html', {'form':form})



def contact_View(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('home')
    else:
        form =ContactForm()
    return render(request,'home/contact.html', {'form':form})

def about_View(request):
    return render(request, 'home/about.html')


def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form':form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                if redirect_path == next_:
                    return redirect('/carts/checkout')
                return redirect(redirect_path)
            else:
                return redirect('/')
        else:
            form = LoginForm()
            print('User Not Valid')

    return render(request, 'user/login.html', context)


def guest_register_view(request):
    form = GuestForm(request.POST or None)
    context = {
        'form':form
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if form.is_valid():
        email  = request.POST['email']
        new_guest_email = GuestEmail.objects.create(email=email)
        request.session['guest_email_id'] = new_guest_email.id
        if is_safe_url(redirect_path, request.get_host()):
            if redirect_path == next_:
                return redirect('/carts/checkout')
            return redirect(redirect_path)
        else:
            return redirect('register')

    return redirect('register')
