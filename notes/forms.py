from django import forms


class NoteForm(forms.Form):
    title = forms.CharField(label='Название')
    text = forms.CharField(label='Текст заметки', widget=forms.TextInput())
