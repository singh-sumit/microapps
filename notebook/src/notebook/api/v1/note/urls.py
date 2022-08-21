from django.urls import path

# url = api/v1/note/
from notebook.api.v1.note.views import NoteHomeAPIView

urlpatterns=[
    path('', NoteHomeAPIView.as_view(), name='note_home'),
]