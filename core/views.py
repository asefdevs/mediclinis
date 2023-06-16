from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from core.models import News,Category,Services,Doctors,Appointment,Comment
from core.forms import ContactForm,AppointmentForm,CommentForm
from django.db.models import Q

# Create your views here.

def home(request):
    context={
        # 'form':ContactForm(),
        'form': AppointmentForm(),
        'blog':News.objects.all().order_by('-created_at')[:3],
        'services': Services.objects.filter(is_active=True)[:3],

    }
    if request.method == 'POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'index.html',context)




def blogdetails(request, slug):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = News.objects.get(slug=slug)
            if request.user.is_authenticated:
                comment.user = request.user
            else:
                comment.user = None  # Set the user as anonymous
            comment.save()
            return redirect('blogdetails', slug=slug)  # Redirect to the same blog details page

    else:
        comment_form = CommentForm()

    context = {
        'comment_form': comment_form,
        'comments': Comment.objects.filter( post=News.objects.filter(slug=slug).first()),
        'single_blog': News.objects.get(slug=slug),
    }
    return render(request, 'blog-details.html', context)




def about(request):
    return render(request, 'about.html')


def booking(request):
    context={
        'doctors':Doctors.objects.all(),
        'appointments':Appointment.objects.all(),
    }
    return render(request,'booking-list.html',context)


def appointment(request):
    context={
        'form': AppointmentForm(),
    }
    if request.method == 'POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()    
    return render(request,'appointment.html',context)

def blog(request):
    context={
        'blog':News.objects.all().order_by('-created_at')[:3],
    }
    news_title = request.GET.get('news')
    start_date = request.GET.get('startdate')
    end_date = request.GET.get('enddate')
    category = request.GET.get('cat')
    context['categories'] = Category.objects.all()
    context['news'] = News.objects.filter(is_active=True).order_by('updated_at')


    if news_title and (start_date or end_date) and category:
        context['news'] = News.objects.filter(
        Q(title__icontains=news_title) | Q(content__icontains=news_title),
        created_at__range=[start_date, end_date], category__id=category
    )
    elif news_title:
        context['news'] = News.objects.filter(Q(title__icontains=news_title) | Q(content__icontains=news_title))
    elif start_date or end_date:
        context['news'] = News.objects.filter(created_at__range=[start_date, end_date])
    elif category:
        context['news'] = News.objects.filter(category__id=category)
    else:
        context['news'] = News.objects.filter(is_active=True).order_by('updated_at')


    return render(request, 'blog.html', context)



def contact(request):
    context={
        'form':ContactForm(),
    }
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'contact.html',context)


def search (request):
    query=request.GET.get('query')
    if query:
        blogs=News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        context={
            'title':'search',
            'query':query,
            'blogs':blogs

        }
        return render(request, 'search.html', context)
    else:
        HttpResponseRedirect(reverse('home')) 

def services(request):
    context={
        'services': Services.objects.filter(is_active=True)
    }
    return render(request, 'service.html', context)

def doctors(request):
    context={
        'doctors': Doctors.objects.all(),
    }

    return render(request, 'doctor.html', context)
def doctordetails(request,id):
    context={
        'doctor': Doctors.objects.get(id=id),
    }

    return render(request, 'doctor-details.html', context)

def service_details(request,id):
    context={
        'services': Services.objects.filter(is_active=True),
        'single_services': Services.objects.get(id=id)
    }
    return render(request, 'service-details.html',context)