from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('contactus.html', views.contactus, name='contactus'),
    path('login.html', views.login, name='login'),
    path('verification.html', views.verification, name='verification'),
    path('search.html', views.search, name='search'),
    path('afterloginpg.html', views.afterloginpg, name='afterloginpg'),
    path('otp.html', views.otp, name='otp'),
    path('forgot.html', views.forgot, name='forgot'),
    path('newpass.html', views.newpass, name='newpass'),
    path('record.html', views.record, name='record'),
    path('download', views.download, name='download'),
    path('Ulogin', views.Ulogin, name='Ulogin'),
    path('Otp_Send', views.otp_send, name='otp_send'),
    path('submit', views.submit_record, name='submit_record'),
    path('Otp_Check', views.resetpass, name='resetpass'),
    path('newpass', views.newpass, name='newpass'),
    path('search_submit', views.search_submit, name='search_submit'),
    path('verify', views.verify, name='verify'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)