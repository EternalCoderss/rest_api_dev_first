from django.urls import path, include


from .views import students

urlpatterns = [
    path('', students),
]