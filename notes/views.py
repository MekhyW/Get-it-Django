from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tagname = request.POST.get('tag')
        if not tagname.startswith('#'):
            tagname = '#' + tagname
        tag, created = Tag.objects.get_or_create(name=tagname)
        if created:
            tag.save()
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

def edit(request, note_id):
    pass

def listalltags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/listalltags.html', {'tags': all_tags})

def listtag(request, tag_id):
    pass