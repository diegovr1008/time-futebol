from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from times import views as times_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', times_views.listar, name='listar'),
    path('cadastro/', times_views.cadastro, name='cadastro'),
    path('login/', auth_views.LoginView.as_view(template_name='times/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('adicionar/', times_views.adicionar, name='adicionar'),
    path('editar/<int:pk>/', times_views.editar, name='editar'),
    path('excluir/<int:pk>/', times_views.excluir, name='excluir'),
]