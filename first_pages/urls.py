from django.urls import path
from . import views

app_name = 'first_pages'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('random-first-page/', views.random_first_page, name='random_first_page'),
    path('additional-pages/<str:book_title>/<int:current_page>/', views.additional_pages, name='additional_pages'),
] 