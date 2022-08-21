from django.urls import path, include

urlpatterns=[
    path('v1/', include('notebook.api.v1.urls')),
]