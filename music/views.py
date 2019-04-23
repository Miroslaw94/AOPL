from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


def music_notes(request):
    return render(request, 'music_notes.html')
