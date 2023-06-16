from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User=get_user_model()



class Base(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class News(Base):
    title=models.CharField(max_length=100)
    content=RichTextField(blank=True,null=True,help_text="use in english")
    is_active=models.BooleanField(default=True)
    image=models.ImageField(upload_to='news')
    created_by=models.CharField(max_length=30)
    slug=models.SlugField(blank=True)
    category=models.ForeignKey('Category' , on_delete=models.CASCADE,related_name='news')
    

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name_plural=_('News')
    
    def save(self, *args, **kwargs):
        self.slug=self.title.replace(' ', '-')
        super(News, self).save(*args, **kwargs)
        


class Category(Base):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural=_('Category')

class Settings(Base):
    logo=models.ImageField(upload_to='settings',null=True,blank=True)
    num1=models.CharField(max_length=50)
    num2=models.CharField(max_length=50)
    adress=models.CharField(max_length=100)
    email=models.EmailField()
    facebook=models.URLField()
    twitter=models.URLField()
    instagram=models.URLField()
    linkedin=models.URLField()
    work_time1=models.CharField( max_length=50,blank=True,null=True )
    work_time2=models.CharField( max_length=50 ,blank=True,null=True )

    
    class Meta:
        verbose_name_plural=_('Settings')


class Contact(Base):
        name=models.CharField(max_length=20)
        email=models.EmailField()
        number=models.CharField(max_length=50)
        comment=models.TextField()

        def __str__(self):
           return self.name
    


        class Meta:
            verbose_name_plural=_('Contact')

class Subscriber(Base):
    email=models.EmailField(max_length=254)
    is_active=models.BooleanField(default=True)
    def __str__(self):
           return self.email
    


    class Meta:
        verbose_name_plural=_('Subscriber')

class Services(Base):
    title=models.CharField(max_length=50)
    description=RichTextField(max_length=5000,help_text='About this service')
    is_active=models.BooleanField(default=True)
    icon_class=models.CharField(max_length=400,null=True,blank=True)
    service_image=models.ImageField(upload_to='service_images',blank=True,null=True)

    def __str__(self):
           return self.title
    


    class Meta:
        verbose_name_plural=_('Services')


class Doctors(Base):
    image=models.ImageField(upload_to='doctors',null=True )
    fullname=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    experience=models.CharField(max_length=100)
    age=models.IntegerField()
    location=models.CharField(max_length=300)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    description=models.TextField()
    education=models.TextField()
    
    def __str__(self):
           return self.fullname

    class Meta:
        verbose_name_plural=_('Doctors')

    

class Appointment(Base):
     name=models.CharField(max_length=100)
     email=models.EmailField()
     doctor=models.ForeignKey(Doctors, on_delete=models.CASCADE)
     date=models.DateField()
     time=models.TimeField()
     problem=models.TextField()
    #  position=models.ForeignKey(Doctors,on_delete=models.CASCADE, blank=True, null=True)


     def __str__(self):
        return self.name

     class Meta:
        verbose_name_plural=_('Appointment')

class Comment(Base):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    post=models.ForeignKey(News,on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title
    class Meta:
        verbose_name_plural = _('Comments')


    



#  maybe will be avaible
# class Product(Base):
#     title=models.CharField(max_length=100)
#     description=models.TextField(max_length=1000)
#     image=models.ImageField(upload_to='products')
#     price=models.IntegerField()
#     category=models.ForeignKey(Category,on_delete=models.CASCADE)

#     def __str__(self):
#            return self.title

#     class Meta:
#         verbose_name_plural=_('Product')


# class Basket(Base):
#      user=models.ForeignKey(User, related_name='basket',on_delete=models.CASCADE)
#      product=models.ForeignKey(Product, related_name='basket', on_delete=models.CASCADE)
#      quantity=models.IntegerField(default=1)
#      total_price=models.IntegerField(default=0)
#      is_active=models.BooleanField(default=True)

#      def __str__(self):
#            return self.product.title

#      class Meta:
#         verbose_name_plural=_('Basket')

    



# Create your models here.
