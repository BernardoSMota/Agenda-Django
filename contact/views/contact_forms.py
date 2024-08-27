from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from contact.models import Contact
from contact.forms import ContactForm

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, request.FILES)
        context = {
             'form_action': form_action,
             'form': form,
             'action': 'CREATE'
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id=contact.pk)
            
        return render(request=request, 
                      template_name="contact/create.html",
                      context=context)
    

    context = {
        'form': ContactForm(),
        'form_action': form_action,
        'action': 'CREATE'


    }

    return render(request=request, 
                  template_name="contact/create.html",
                  context=context)


@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True, owner=request.user)
    current_id = contact.pk

    form_action = reverse('contact:update', args= (contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
             'form_action': form_action,
             'form': form,
             'current_id': current_id,
             'action': 'UPDATE'
        }

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=current_id)
            
        return render(request=request, 
                      template_name="contact/create.html",
                      context=context)
    

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
        'current_id': current_id,
        'action': 'UPDATE'

    }

    return render(request=request, 
                  template_name="contact/create.html",
                  context=context)


@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, show=True, owner=request.user)
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    context = {
        'contact': contact,
        'confirmation': confirmation,
    }

    return render(request=request, template_name='contact/contact.html', context=context)