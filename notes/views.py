from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Note


def index(request):
    #return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        new_note = Note.objects.create(title=title, details=content)
        new_note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        print(all_notes)
        return render(request, 'notes/index.html', {'notes': all_notes})