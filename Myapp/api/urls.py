from django.conf.urls import url
import views

urlpatterns = [
    url(r'^email/', views.email),
    url(r'^send/', views.send_email)
]