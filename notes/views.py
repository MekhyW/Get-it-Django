from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        if not tag.startswith('#'):
            tag = '#' + tag
        new_note = Note.objects.create(title=title, details=content, tag=tag)
        new_note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
        return render(request, 'notes/index.html', {'notes': all_notes})


def delete(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')