from django.urls import path, include
from .views import CreateView, DetailsView 

urlpatterns = [
    path('', CreateView.as_view()),
    path('<int:pk>/', DetailsView.as_view()),

]