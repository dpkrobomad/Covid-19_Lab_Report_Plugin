from django.contrib.auth.views import LoginView


from django.contrib import admin
from django.urls import path,include
from . import views
admin.site.site_header = 'Lab Report Portal'
admin.site.site_title = 'Lab Report Portal | By Deepak R'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('404/',views.home,name='home'),
    path('upload/',views.upload,name='upload'),
    path('report/<int:id>',views.get_report),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', views.logout_view,name='logout'),
]
