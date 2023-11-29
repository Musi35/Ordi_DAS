from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.pagina_login, name='login'),
    path('logout/', views.pagina_logout, name='logout'),
    path('get_data/', views.get_data, name='get_data'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('tabla/', views.tabla, name='tabla'),
]