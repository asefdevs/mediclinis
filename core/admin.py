from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from .models import (
    News,Category,Settings,Contact,Subscriber,Services,Doctors,Appointment,
    Comment,
)


# admin.site.register(News)

admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(Appointment)
admin.site.register(Comment)
@admin.register(Doctors)
class DoctorAdmin(TranslationAdmin):
    list_display=('fullname',)
@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display=('title',)


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_filter=('title','category','slug')
    list_display=('title','category')
    search_fields=('title','category')
    list_per_page=3


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):

    def has_delete_permission(self,request,obj=None):
        return False
    def has_add_permission(self,request):
        return False
    
@admin.register(Services)
class ServicesAdmin(TranslationAdmin):
    list_display=('title','description')



