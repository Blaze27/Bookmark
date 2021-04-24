from django.urls import path
from . import views


app_name = 'bookmarkApp'


urlpatterns = [
    path('', views.Index.as_view(), name = "index"),
    path('bookmark-detail/<int:pk>', views.BookmarkDetail.as_view(), name="bookmark-detail"),
    path('add-bookmark', views.create_bookmark, name="add-bookmark"),
    path('all-folders', views.FolderList.as_view(), name="all-folder"),
    path('edit-bookmark/<int:pk>', views.edit_bookmark, name="edit-bookmark"),
    path('delete-bookmark/<int:pk>', views.delete_bookmark, name="delete-bookmark"),
]
