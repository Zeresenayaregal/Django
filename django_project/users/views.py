from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterationForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been created!')
            return redirect('login')
    else:
        form = UserRegisterationForm()
    return render(request, 'users/register.html', {'form':form})


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'users/profile.html') 
