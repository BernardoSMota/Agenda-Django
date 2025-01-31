from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator

from contact.models import Contact

def index(request):

    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }

    return render(
        request=request,
        template_name='contact/index.html',
        context=context,
    )


def contact(request, contact_id):
    # single_contact = Contact.objects.get(id=contact_id)
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    if single_contact.show:
        context = {
        'contact': single_contact,
        'site_title': f'{single_contact.first_name} {single_contact.last_name} - '
        }

    return render(
        request=request,
        template_name='contact/contact.html',
        context=context,
    )

def search(request):

    search_value = request.GET.get('q', '').rstrip().lstrip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).order_by('-id').filter(Q(first_name__icontains=search_value) | Q(last_name__icontains=search_value) | Q(phone__icontains=search_value))

    paginator = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Search - ',
        'search_value': search_value
    }

    return render(
        request=request,
        template_name='contact/index.html',
        context=context,
    )

