from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:note_id>', views.delete, name='delete'),
    path('edit/<int:note_id>', views.edit, name='edit'),
    path('listalltags', views.listalltags, name='listalltags'),
    path('listtag/<int:tag_id>', views.listtag, name='listtag'),
]