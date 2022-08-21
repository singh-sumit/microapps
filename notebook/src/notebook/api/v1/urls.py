from django.urls import path, include

urlpatterns=[
    path('note/', include('notebook.api.v1.note.urls')),
]