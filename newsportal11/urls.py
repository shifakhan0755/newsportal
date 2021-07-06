"""newsportal11 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/',views.search,name='search'),
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('entertainment/',views.NewsEntertainment,name='entertainment'),
    path('state/', views.State, name='state'),
    path('bollywood/',views.bollywood,name='bollywood'),
    path('hollywood/',views.hollywood,name='hollywood'),
    path('ncr/',views.ncr,name='ncr'),
    path('about/',views.about,name='about'),
    path('uttarpradesh/',views.uttarpradesh,name='uttarpradesh'),
    path('television/',views.television,name='television'),
    path('bihar/',views.bihar,name='bihar'),
    path('uttarakhand/', views.uttarakhand, name='uttarakhand'),
    path('jharkhand/', views.jharkhand, name='jharkhand'),
    path('rajasthan/', views.rajasthan, name='rajasthan'),
    path('career/',views.career,name='career'),
    path('madhyapradesh/', views.madhyapradesh, name='madhyapradesh'),
    path('maharashtra/', views.maharashtra, name='maharashtra'),
    path('haryana/', views.haryana, name='haryana'),
    path('country/',views.country,name='country'),
    path('ipl/',views.ipl,name='ipl'),
    path('corona/',views.corona,name='corona'),
    path('chhattisgrah/', views.chhattisgrah, name='chhattisgrah'),
    path('himachalpradesh/', views.himachalpradesh, name='himachalpradesh'),
    path('product-detail/<slug:slug>/',views.NewsDetailEntertainment,name='entertainment-detail'),
    path('tag/<slug:slug>/', views.tagged, name='togged'),
    path('tag/<slug:state_slug>/', views.StateDetail, name='togged_StateDetail'),
    #path('product-detail/<int:pk>/', views.NewsDetailEntertainment, name='entertainment-detail'),
    path('state-detail/<slug:slug>/', views.StateDetail, name='state-detail'),
    path('corona-detail/<slug:slug>/', views.CoronaDetail, name='corona-detail'),
    path('ipl-detail/<slug:slug>/', views.IPLDetail, name='ipl-detail'),
    path('career-detail/<slug:slug>/',views.CareerDetail,name='career-detail'),
    path('world-detail/<slug:slug>/',views.WorldDetail,name='world-detail'),
    path('logout/',views.user_logout,name='logout'),
    path('signin/',views.user_signup,name='signin'),
    path('login/', views.user_login, name='login'),
    path('adminpannel11/',include('adminpannel.urls')),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
