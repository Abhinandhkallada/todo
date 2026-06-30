from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('addtask',views.add_task,name='addtask'),
    path('delete/<int:id>',views.delete_task,name='delete'),
    path('update/<int:id>',views.update_task,name='update')
]