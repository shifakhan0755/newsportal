from django.contrib import admin
from .models import EntertainmentModel,CoronaModel,StateModel,IPLModel,CareerModel,WorldModel,ContactModel,News

# Register your models here.
@admin.register(EntertainmentModel)
class EntertainmentAdmin(admin.ModelAdmin):
    list_display = ['id','title','caption','description','date','d_description','category','s_image','s_vedio']



@admin.register(CoronaModel)
class CoronaAdmin(admin.ModelAdmin):
    list_display = ['id','title','caption','description','date','d_description','category','s_image','s_vedio']

@admin.register(StateModel)
class StateModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','caption','description','date','detail_description','category','s_image','s_vedio']

@admin.register(IPLModel)
class StateModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','caption','description','date','detail_description','s_image','s_vedio']

@admin.register(CareerModel)
class CareerModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','caption','description','date','detail_description','category','s_image','s_vedio']

@admin.register(WorldModel)
class CareerModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','caption','description','date','detail_description','s_image','s_vedio']

@admin.register(ContactModel)
class contactadmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','comment']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','caption','description','date','d_description','category','s_image','s_vedio']



