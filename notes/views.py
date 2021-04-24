
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from notes.forms import NoteForm
from notes.models import Note
from notes.serializers import NoteSerializer

from .forms import NoteForm
from .models import Note


def save_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            Note.objects.create_note(form.cleaned_data['title'], form.cleaned_data['text'], request.user)
    return redirect('/')


def delete_note(request):
    id = request.GET.get("id", )
    note = Note.objects.get(id=id)
    note.delete()
    print(id)
    return redirect('/')


def note_list(request):
    if request.method == 'GET':
        snippets = Note.objects.all()
        serializer = NoteSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def note_detail(request, pk):
    try:
        snippet = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NoteSerializer(snippet)
        return JsonResponse(serializer.data)
