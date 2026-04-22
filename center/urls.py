from django.urls import path
from center import views

app_name = "center"

urlpatterns = [
    path("", views.center_list, name='list'),
    path("<int:id>/", views.center_detail, name='detail'),
    path("cerate/", views.center_create, name='create'),
    path("update/<int:id>/", views.center_update, name='update'),
    path("delete/<int:id>/", views.center_delete, name='delete'),
    path("<int:center_id>/storage/", views.StorageList.as_view(), name='storage-list'),
    path("storage/<int:pk>/", views.StorageDetail.as_view(), name='storage-detail'),
    path("<int:center_id>/storage/create/", views.StorageCreate.as_view(), name='storage-create'),
    path("storage/update/<int:pk>", views.StorageUpdate.as_view(), name='storage-update'),
    path("storage/delete/<int:pk>", views.StorageDelete.as_view(), name='storage-delete'),
]