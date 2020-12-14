from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('edit/<int:sl_no>', views.edit, name='edit'),
    # path('edit_todo/', views.edit_todo, name="todoedit")
    path('delete/<int:sl_no>', views.delete, name="delete")
]