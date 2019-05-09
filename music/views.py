from django.shortcuts import render
from django.http import HttpResponseRedirect


def home_page(request):
    return render(request, 'home.html')

def music_notes(request):
    return render(request, 'music_notes.html')

def add_music_notes(request):
    if request.method == 'POST':
        return render(request, 'music_notes.html', {'music_notes_files': request.POST.get('title', '')})
        # Current return generates bug in normal site using. From next commit it will be changed to this one:
        # return HttpResponseRedirect('/nuty/', )
    return render(request, 'add_music_notes.html')
