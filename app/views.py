from django.shortcuts import render, redirect # type: ignore
from django.core.mail import send_mail # type: ignore
from .models import GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion, Blog
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage # type: ignore

# Create your views here.
def index(request):

    general_info = GeneralInfo.objects.first()

    services = Service.objects.all()

    testimonials = Testimonial.objects.all()

    faqs = FrequentlyAskedQuestion.objects.all()

    recent_blogs = Blog.objects.all().order_by('-created_at')[:3]
    
    default_value = ''
    context = {
        'company_name': getattr(general_info, 'company_name', default_value),
        'location': getattr(general_info, 'location', default_value),
        'email': getattr(general_info, 'email', default_value),
        'phone': getattr(general_info, 'phone', default_value),
        'video_url': getattr(general_info, 'video_url', default_value),
        'twitter_url': getattr(general_info, 'twitter_url', default_value),
        'facebook_url': getattr(general_info, 'facebook_url', default_value),
        'instagram_url': getattr(general_info, 'instagram_url', default_value),
        'linkedln_url': getattr(general_info, 'linkedln_url', default_value),
        'open_hours': getattr(general_info, 'open_hours', default_value),

        'services': services,
        'testimonials':testimonials,
        'faqs':faqs,
        'recent_blogs':recent_blogs,
    }
    return render (request, 'index.html', context)

def contact_form(request):

    if request.method == 'POST':
        print('\nUser has submit a contact form\n')
    
    return redirect('home')

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    recent_blogs = Blog.objects.all().exclude(id=blog_id).order_by('-created_at')[:2]

    context = {'blog':blog, 'recent_blogs':recent_blogs,}
    return render(request, 'blog_details.html', context)

def blogs(request):

   all_blogs  = Blog.objects.all().order_by('-created_at')
   blogs_per_page = 3
   paginator = Paginator(all_blogs, blogs_per_page)
   
   page = request.GET.get('page')

   try:
       blogs = paginator.page(page)
   except PageNotAnInteger:
       blogs = paginator.page(1)
   except EmptyPage:
       blogs = paginator.page(paginator.num_pages)
       

   context = {'blogs':blogs, 'paginator':paginator, 'page':page}
   return render(request, 'blogs.html', context)