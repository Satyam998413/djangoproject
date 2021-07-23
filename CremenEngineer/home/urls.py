from django.contrib import admin
from django.urls import path
from home import views


admin.site.site_header = "Satyam Baranwal Admin"
admin.site.site_title = "Satyam Baranwal Admin Portal"
admin.site.index_title = "Welcome to CremenEngineers User Satyam Baranwal"

urlpatterns = [
    path('',views.index,name='home'),
    
    path("Accounts", views.accounts, name='Accounts'),
    path("Mechanical_Engineering", views.mechanical, name='Mechanical_Engineering'),
    path("Civil_Engineering", views.civil, name='Civil_Engineering'),
    path("Electrical_Engineering", views.electrical, name='Electrical_Engineering'),
    path("Computer_Science", views.cs, name='Computer_Science'),
    # path('',views.index,name='home'),
    path("videos",views.videos,name='videos'),
    # path('',views.index,name='home'),
    # path('',views.index,name='home'),
]