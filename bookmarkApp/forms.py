from django import forms

from .models import Bookmark, Folder

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = (
            'folder_name',
        )

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark

        fields = (
            'name', 
            'url',
            'description',
            'tag',
        )

