from django.contrib import admin
from core.models import News,Category,Services,Doctors
from modeltranslation.translator import translator,TranslationOptions

class NewsTranslationOptions(TranslationOptions):
    fields=(
        'title','content',
    )

class CategoryTranslationOptions(TranslationOptions):
    fields=('title',)

class ServicesTranslationOptions(TranslationOptions):
    fields=('title','description',)

class DoctorsTranslationOptions(TranslationOptions):
    fields=(
        'description','education','position',
    )

translator.register(News, NewsTranslationOptions)
translator.register(Category, CategoryTranslationOptions)   
translator.register(Services,ServicesTranslationOptions)
translator.register(Doctors,DoctorsTranslationOptions)