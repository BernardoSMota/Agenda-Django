from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),

    #contact
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),

    #user
    path('user/update/', views.user_update, name='update'),
    path('user/logout/', views.logout_view, name='logout'),
    path('user/login/', views.login_view, name='login'),
    path('user/create/', views.register, name='register')
]
