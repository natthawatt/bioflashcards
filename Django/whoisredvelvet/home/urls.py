from django.urls import path

urlpatterns = [
    path('home/', home, name='The Home Page'),
    path('About/', About, name='about'),
]
