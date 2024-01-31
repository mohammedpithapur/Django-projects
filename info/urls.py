from django.urls import path
from . import views
# from .views import Add,HOME,Delete,Edit
from .views import HOME,Edit,Add,Delete,profEdit
urlpatterns = [
    path('', HOME.as_view(), name='home'),
    path('add/', Add.as_view(), name='Add'),
    path('delete/', Delete.as_view(), name='delete'),
    path('edit/<int:id>', Edit.as_view(), name='edit'),
    path('profedit/<int:id>', profEdit.as_view(), name='profedit'),
    path('profadmin/', views.profadmin, name="profadmin")
]