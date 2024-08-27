from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from contact.forms import RegisterForm, RegisterUpdateForm

def register(request):   
    context = {
        'action': 'Create',
        'form': RegisterForm()
    }

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso')
            return redirect('contact:logout')
        
    return render(request=request, template_name='contact/register_user.html', context=context)


def login_view(request):
    form = AuthenticationForm(request)

    context = {'form': form,}

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        context['form'] = form

        if form.is_valid():
            user = form.get_user()

            login(request, user)

            messages.success(request, f'Usuário {user.username} conectado')

            return redirect('contact:index')
        
    return render(request=request, template_name='contact/login.html', context=context)


def logout_view(request):
    logout(request)

    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):

    form = RegisterUpdateForm(instance=request.user)

    context = {
        'form': form,
        'action': 'Update'
    }

    if request.method == 'POST':
        form = RegisterUpdateForm(data=request.POST, instance=request.user)
        context['form'] = form

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário atualizado com sucesso')

            return redirect('contact:index')



    return render(request=request, template_name='contact/register_user.html', context=context)