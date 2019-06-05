from django.shortcuts import render, redirect, get_object_or_404
from .models import MusicNotes
from .forms import NewMusicNotesForm


def home_page(request):
    return render(request, 'home.html')

def music_notes(request):
    music_notes_list = MusicNotes.objects.all().order_by('-created_date')
    return render(request, 'music_notes.html', {'music_notes_list': music_notes_list})

def music_notes_details(request, pk):
    notes = get_object_or_404(MusicNotes, pk=pk)
    return render(request, 'music_notes_details.html', {'music_notes': notes})

def add_music_notes(request):
    if request.method == 'POST':
        form = NewMusicNotesForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('music_notes')
    else:
        form = NewMusicNotesForm()
    return render(request, 'add_music_notes.html', {'form': form})
