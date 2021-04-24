from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Bookmark, Folder
from .forms import FolderForm, BookmarkForm
from django.contrib import messages
# Create your views here.


class Index(ListView):
    model = Bookmark

class BookmarkDetail(DetailView):
    model = Bookmark

class FolderList(ListView):
    model = Folder



def create_bookmark(request):
    bookmark_form = BookmarkForm(request.POST or None)
    folder_form = FolderForm(request.POST or None)

    if bookmark_form.is_valid() and folder_form.is_valid():
        bookmark = bookmark_form.save(commit=False)
        folder, created = Folder.objects.get_or_create(folder_name=folder_form.cleaned_data['folder_name'])
        bookmark.folder = folder
        bookmark.save()
        bookmark_form.save_m2m()
        messages.success(request, 'Bookmark added succesfully')
        return redirect('bookmarkApp:index')
    
    Context = {
        'bookmark_form' : bookmark_form,
        'folder_form' : folder_form,
    }

    return render(request, "bookmarkApp/add_bookmark.html" , context=Context)


def edit_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, id=pk)
    folder = get_object_or_404(Folder, id = bookmark.id)

    bookmark_form = BookmarkForm(request.POST or None, instance=bookmark)
    folder_form = FolderForm(request.POST or None, instance=folder)

    if bookmark_form.is_valid() and folder_form.is_valid():
        bookmark = bookmark_form.save(commit=False)
        folder, created = Folder.objects.get_or_create(folder_name=folder_form.cleaned_data['folder_name'])
        bookmark.folder = folder
        bookmark.save()
        bookmark_form.save_m2m()
        messages.success(request, 'Bookmark edited succesfully')
        return redirect('bookmarkApp:index')
    
    Context = {
        'bookmark_form' : bookmark_form,
        'folder_form' : folder_form,
    }

    return render(request, "bookmarkApp/add_bookmark.html" , context=Context)


def delete_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, id=pk)
    bookmark.delete()
    messages.success(request, 'Bookmark deleted succesfully')
    return redirect('bookmarkApp:index')



