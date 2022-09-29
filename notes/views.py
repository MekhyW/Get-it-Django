from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from .models import Note, Tag
import random


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tagname = request.POST.get('tag')
        if not tagname.startswith('#'):
            tagname = '#' + tagname
        tag, created = Tag.objects.get_or_create(name=tagname)
        if created:
            tag.color = random.randint(0, 16777215)
            tag.save()
        new_note = Note.objects.create(title=title, details=content, tag=tag)
        new_note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        for note in all_notes:
            note.tag.color = '{0:06X}'.format(note.tag.color)
            print(note.tag.color)
            note.rotate = random.randint(-6, 6)
        return render(request, 'notes/index.html', {'notes': all_notes})


def delete(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')

def edit(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.title = request.POST.get('titulo')
        note.details = request.POST.get('detalhes')
        tagname = request.POST.get('tag')
        if not tagname.startswith('#'):
            tagname = '#' + tagname
        tag, created = Tag.objects.get_or_create(name=tagname)
        if created:
            tag.save()
        note.tag = tag
        note.save()
        return redirect('index')
    else:
        return render(request, 'notes/edit.html', {'note': note})

def listalltags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/listalltags.html', {'tags': all_tags})

def listtag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    notes_with_tag = Note.objects.filter(tag=tag)
    return render(request, 'notes/listtag.html', {'notes_with_tag': notes_with_tag, 'tag': tag})


def handler404(request, *args, **argv):
    response = render('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response