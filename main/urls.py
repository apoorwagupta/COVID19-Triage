from django.urls import path
from . import views
from .views import autosuggest
urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.dashboard, name="dashboard"), #path returns an element for inclusion in urlpatterns.
    path("login/", views.login, name="login"),#In order to perform URL reversing, you’ll need to use named URL pattern
    path('logout', views.logout, name='logout'), #When naming URL patterns, choose names that are unlikely to clash with other applications’ choice of names.
    path("add_patient/", views.add_patient, name="add_patient"),# If you call your URL pattern comment and another application does the same thing,
    path("patient_list/", views.patient_list, name="patient_list"),#the URL that reverse() finds depends on whichever pattern is last in your project’s urlpatterns list.
    path("patient/<str:pk>", views.patient, name="patient"),
    path("autosuggest/", views.autosuggest, name="autosuggest"),
    path("autodoctor/", views.autodoctor, name="autodoctor"),
    path("info/", views.info, name="info"),
]


  # path("", views.dashboard, name="dashboard"),
   # path("login/", views.login, name="login"),