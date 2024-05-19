from django.urls import path
from Services import views
urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path('delete_url/<int:url_id>/',views.delete_url,name="delete_url")
]
