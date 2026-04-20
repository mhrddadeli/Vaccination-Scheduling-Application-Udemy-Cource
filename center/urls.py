from django.urls import path
from center import views

app_name = "center"

urlpatterns = [
    path("", views.center_list, name='list'),
    path("<int:id>/", views.center_detail, name='detail'),
    path("cerate/", views.center_create, name='create'),
    path("update/<int:id>", views.center_update, name='update'),
    path("delete/<int:id>", views.center_delete, name='delete'),
]