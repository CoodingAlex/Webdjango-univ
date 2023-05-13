from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    # acceder con: /polls/5/
    path("<int:pk>/detail/estaeslamejorpagina", views.DetailView.as_view(), name="detail"),
    # acceder con: /polls/5/results
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
     # acceder con: /polls/5/vote
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
