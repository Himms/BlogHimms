
from django.urls import path 
from  . import views
app_name = himms



urlpatterns = [
    path('', frontpage, name = 'frontpage'),
   path("register", views.register_request, name="register")
   path('<slug:slug>/', post_detail, name = 'post_detail')

]
