from django.urls import path 
from Census import views
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('' , views.index,  name='index'),
    path('home/' , views.index,  name='index'),
    path('sign-up/', views.signup, name='signup'),
    path('logged/',views.logged,name='logged'),
    path('census',login_required(views.index2),name='index2')
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
handler404 = views.error_404
handler500 = views.error_500