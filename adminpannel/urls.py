from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.careerModel,name='careerModel'),
    path('contactmodel/',views.contactModel,name='contactModel'),
    path('coronavirusmodel/',views.coronavirusModel,name='coronavirusModel'),
    path('entertainmentmodel/',views.entertainmentModel,name='entertainmentModel'),
    path('worldmodel/',views.worldModel,name='worldModel'),
    path('iplmodel/',views.iplModel,name='iplModel'),
    path('statemodel/',views.stateModel,name='stateModel'),
    path('delete/<int:id>/', views.delete_post, name='deletepost'),
    path('delete-contact/<int:id>/', views.delete_contact, name='deletecontact'),
    path('delete-coronavirus/<int:id>/', views.delete_coronavirus, name='deletecoronavirus'),
    path('delete-entertainment/<int:id>/', views.entertaindel, name='entertain'),
    path('delete-ipl/<int:id>/', views.ipldel, name='ipldel'),
    path('update/<int:id>/', views.updatenews,name='updatepost'),
    path('delete-state/<int:id>/', views.statedel, name='statedel'),
    path('update-state/<int:id>/', views.updatestate, name='updatestate'),
    path('delete-world/<int:id>/', views.worlddel, name='worlddel'),
    path('update-world/<int:id>/', views.updateworld, name='updateworld'),
    path('update-ipl/<int:id>/', views.updateipl, name='updateipl'),
    path('update-corona/<int:id>/', views.updatecorona,name='updatecorona'),
    path('up-entertainment/<int:id>/', views.updateentertainment, name='up-entertainment'),
    path('career-detail11/<int:pk>/', views.careerdetailmodel, name='career-detail1'),
    path('coronavirus-detail11/<int:pk>/', views.coronavirusdetailmodel, name='coronavirus-detail1'),
    path('sssss/<int:pk>/', views.statedetailmodel, name='sssss'),
    path('world-detail11/<int:pk>/', views.worlddetailmodel, name='world-detail1'),
    path('ipl-detail11/<int:pk>/', views.ipldetailmodel, name='ipl-detail11'),
    path('entertainment-detail11/<int:pk>/', views.entertainmentdetailmodel, name='enter-detail1'),
    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.Edit_profile),
    path('site-setting/',views.site_setting,name='site_setting'),
    path('user-detail/<int:id>/',views.user_detail,name='userdetail'),
    path('user-create/',views.user_create),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)