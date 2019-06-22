from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import MusicNotes
from .forms import MusicNotesForm


def home_page(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def music_notes(request):
    music_notes_list = MusicNotes.objects.all().order_by('-created_date')
    return render(request, 'music_notes.html', {'music_notes_list': music_notes_list})

@login_required(login_url='/login/')
def music_notes_details(request, pk):
    notes = get_object_or_404(MusicNotes, pk=pk)
    return render(request, 'music_notes_details.html', {'music_notes': notes})

@login_required(login_url='/login/')
def add_music_notes(request):
    if request.method == 'POST':
        form = MusicNotesForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('music_notes')
    else:
        form = MusicNotesForm()
    return render(request, 'add_music_notes.html', {'form': form})

@login_required(login_url='/login/')
def delete_music_notes(request, pk):
    notes = get_object_or_404(MusicNotes, pk=pk)
    if request.method == 'POST':
        notes.delete()
        return redirect('music_notes')
    return render(request, 'delete_music_notes.html', {'music_notes': notes})

@login_required(login_url='/login/')
def edit_music_notes(request, pk):
    notes = get_object_or_404(MusicNotes, pk=pk)
    old_title = notes.title
    if request.method == 'POST':
        form = MusicNotesForm(request.POST, request.FILES, instance=notes)
        if form.is_valid():
            notes.edit_notes(old_title)
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('music_notes')
    else:
        form = MusicNotesForm(instance=notes)
    return render(request, 'add_music_notes.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            return render(request, 'login.html', {'error_message': 'Login lub hasło nieprawidłowe. Spróbuj ponownie.'})
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home_page')
