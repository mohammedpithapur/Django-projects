from django.urls import path
from . import views
# from .views import Add,HOME,Delete,Edit
from .views import HOME,Edit
urlpatterns = [
    path('', HOME.as_view(), name='home'),
    # path('add/', Add.as_view(), name='Add'),
    # path('delete/', Delete.as_view(), name='delete'),
    path('edit/<id>', Edit.as_view(), name='edit'),
    path('admin/', views.admin, name="admin")
]