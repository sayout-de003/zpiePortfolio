# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from .models import HomepageHero, Service, KeyFeature, Client, Project, Publication, Blog, Event, Testimonial, FAQ, Logo, Header_title
# from .models import ContactDetails, CompanyPages , Address ,  text_for_brief , HomepageBrief
# def basepage(request):
#     context = {
#         'logo': Logo.objects.first(),
#         'header_title': Header_title.objects.filter(is_active=True).first(),
#         'services': Service.objects.filter(is_active=True),
#         'contact_details': ContactDetails.objects.filter(is_active=True),
#         'company_pages': CompanyPages.objects.filter(is_active=True),
#         'address': Address.objects.filter(is_active=True).first(),
#     }
#     return render(request, 'core/base.html', context)

# # core/views.py

# # def homepage(request):
# #     # 1. Base Context (Required for Navbar & Footer in base.html)
# #     base_context = {
# #         'logo': Logo.objects.filter(is_active=True).first(),
# #         'header_title': Header_title.objects.filter(is_active=True).first(),
# #         'company_pages': CompanyPages.objects.filter(is_active=True),
# #         'contact_details': ContactDetails.objects.filter(is_active=True),
# #         'address': Address.objects.filter(is_active=True).first(),
# #     }

# #     # 2. Homepage Specific Context
# #     home_context = {
# #         'hero': HomepageHero.objects.filter(is_active=True).first(),
# #         'text_for_brief': text_for_brief.objects.all(),
# #         'homepage_brief': HomepageBrief.objects.filter(is_active=True).first(),
# #         'services': Service.objects.filter(is_active=True),
# #         'key_features': KeyFeature.objects.all(),
# #         'clients': Client.objects.all(),
# #         'projects': Project.objects.filter(is_active=True),
# #         'publications': Publication.objects.all(),
# #         'blogs': Blog.objects.all(),
# #         'events': Event.objects.all(),
# #         'testimonials': Testimonial.objects.all(),
# #         'faqs': FAQ.objects.filter(is_active=True),
# #     }

# #     # 3. Merge contexts so both are available in the template
# #     context = {**base_context, **home_context}

# #     return render(request, 'core/homepage.html', context)



# from django.shortcuts import render
# from .models import HomepageHero, text_for_brief, HomepageBrief, Service, KeyFeature, Client, Project, Publication, Blog, Event, Testimonial, FAQ

# def homepage(request):
#     home_context = {
#         'hero': HomepageHero.objects.filter(is_active=True).first(),
#         'text_for_brief': text_for_brief.objects.all(),
#         'homepage_brief': HomepageBrief.objects.filter(is_active=True).first(),
#         'services': Service.objects.filter(is_active=True),
#         'key_features': KeyFeature.objects.all(),
#         'clients': Client.objects.all(),
#         'projects': Project.objects.filter(is_active=True),
#         'publications': Publication.objects.all(),
#         'blogs': Blog.objects.all(),
#         'events': Event.objects.all(),
#         'testimonials': Testimonial.objects.all(),
#         'faqs': FAQ.objects.filter(is_active=True),
#     }

#     return render(request, 'core/homepage.html', home_context)


# def servicepage(request):
#     context = {
#         'services': Service.objects.filter(is_active=True),
#     }
#     return render(request, 'core/service.html', context)

# def projectpage(request):
#     context = {
#         'projects': Project.objects.filter(is_active=True),
#     }
#     return render(request, 'core/project.html', context)

# def publicationpage(request):
#     context = {
#         'publications': Publication.objects.all(),
#     }
#     return render(request, 'core/publication.html', context)

# def blogpage(request):
#     context = {
#         'blogs': Blog.objects.all(),
#     }
#     return render(request, 'core/blog.html', context)

# def eventpage(request):
#     context = {
#         'events': Event.objects.all(),
#     }
#     return render(request, 'core/event.html', context)

# def testimonialpage(request):
#     context = {
#         'testimonials': Testimonial.objects.all(),
#     }
#     return render(request, 'core/testimonial.html', context)

# def faqpage(request):
#     context = {
#         'faqs': FAQ.objects.filter(is_active=True),
#     }
#     return render(request, 'core/faq.html', context)

# def contactpage(request):
#     context = {
#         'contact_details': ContactDetails.objects.filter(is_active=True),
#     }
#     return render(request, 'core/contact.html', context)    

# def aboutpage(request):
#     # context = {
#     #     'about': About.objects.filter(is_active=True).first(),
#     # }
#     return render(request, 'core/about.html')



from django.shortcuts import render
from .models import (
    HomepageHero, Service, KeyFeature, Client, Project, Publication, 
    Blog, Event, Testimonial, FAQ, Logo, Header_title, 
    ContactDetails, CompanyPages, Address, text_for_brief, HomepageBrief , DemoCategory,DemoWebsite , AboutUs
)

# Optional: You can use this helper function if you want to reuse code, 
# or just paste this logic into every view as shown below.
def get_base_context():
    return {
        'logo': Logo.objects.first(),
        # Fixed: Added .objects.first() and removed is_active filter
        'header_title': Header_title.objects.first(),
        # Fixed: Removed .filter(is_active=True) because model has no such field
        'company_pages': CompanyPages.objects.all(),
        # Fixed: Removed .filter(is_active=True)
        'contact_details': ContactDetails.objects.all(),
        # Fixed: Removed .filter(is_active=True)
        'address': Address.objects.first(),
        # This one is correct (Service has is_active)
        'services': Service.objects.filter(is_active=True),

    }

def basepage(request):
    context = get_base_context()
    return render(request, 'core/base.html', context)

# def homepage(request):
#     # 1. Get Base Context
#     base_context = get_base_context()

#     # 2. Homepage Specific Context
#     home_context = {
#         'hero': HomepageHero.objects.filter(is_active=True).first(),
#         'text_for_brief': text_for_brief.objects.all(),
#         'homepage_brief': HomepageBrief.objects.filter(is_active=True).first(),
#         'key_features': KeyFeature.objects.all(),
#         'clients': Client.objects.all(),
#         'projects': Project.objects.filter(is_active=True),
#         'publications': Publication.objects.all(),
#         'blogs': Blog.objects.all(),
#         'events': Event.objects.all(),
#         'testimonials': Testimonial.objects.all(),
#         'faqs': FAQ.objects.filter(is_active=True),
#     }

#     # 3. Merge contexts
#     context = {**base_context, **home_context}
#     return render(request, 'core/homepage.html', context)




from .models import ContactFormHomePage

# def homepage(request):
#     if request.method == "POST":
#         ContactFormHomePage.objects.create(
#             identifier="homepage_contact",
#             name=request.POST.get("name"),
#             company_name=request.POST.get("company_name"),
#             email=request.POST.get("email"),
#             phone=request.POST.get("phone"),
#             subjectMessage=request.POST.get("subjectMessage"),
#             message=request.POST.get("message"),
#         )

#     base_context = get_base_context()

#     home_context = {
#         'hero': HomepageHero.objects.filter(is_active=True).first(),
#         'homepage_brief': HomepageBrief.objects.filter(is_active=True).first(),
#         'key_features': KeyFeature.objects.all(),
#         'clients': Client.objects.all(),
#         'projects': Project.objects.filter(is_active=True),
#         'blogs': Blog.objects.all(),
#         'testimonials': Testimonial.objects.all(),
#         'faqs': FAQ.objects.filter(is_active=True),
#     }

#     context = {**base_context, **home_context}
#     return render(request, 'core/homepage.html', context)




def homepage(request):
    # Handle homepage contact form
    if request.method == "POST":
        ContactFormHomePage.objects.create(
            identifier="homepage_contact",
            name=request.POST.get("name"),
            company_name=request.POST.get("company_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subjectMessage=request.POST.get("subjectMessage"),
            message=request.POST.get("message"),
        )

    base_context = get_base_context()

    home_context = {
        # HERO
        'hero': HomepageHero.objects.filter(is_active=True).first(),

        # ✅ FIXED: MULTIPLE HOMEPAGE BRIEFS
        'homepage_briefs': HomepageBrief.objects.filter(
            is_active=True
        ).order_by('id'),

        # OPTIONAL TEXT BLOCKS
        'text_for_brief': text_for_brief.objects.all(),

        # SECTIONS
        'key_features': KeyFeature.objects.all(),
        'clients': Client.objects.all(),
        'projects': Project.objects.filter(is_active=True).order_by('-id'),
        'blogs': Blog.objects.all().order_by('-id'),
        'testimonials': Testimonial.objects.all(),
        'faqs': FAQ.objects.filter(is_active=True),
        'about_us' : AboutUs.objects.all(),

         # ✅ DEMO WEBSITES SECTION
        "demo_categories": DemoCategory.objects.prefetch_related(
            "demos"
        ).filter(is_active=True),


    }

    context = {**base_context, **home_context}
    return render(request, 'core/homepage.html', context)



def servicepage(request):
    # Merge base context so the navbar/footer works here too
    context = {**get_base_context(), 'services': Service.objects.filter(is_active=True)}
    return render(request, 'core/services.html', context)

def projectpage(request):
    context = {**get_base_context(), 'projects': Project.objects.filter(is_active=True)}
    return render(request, 'core/projects.html', context)

def publicationpage(request):
    context = {**get_base_context(), 'publications': Publication.objects.all()}
    return render(request, 'core/publications.html', context)

def blogpage(request):
    context = {**get_base_context(), 'blogs': Blog.objects.all()}
    return render(request, 'core/blog.html', context)

def eventpage(request):
    context = {**get_base_context(), 'events': Event.objects.all()}
    return render(request, 'core/events.html', context)

def testimonialpage(request):
    context = {**get_base_context(), 'testimonials': Testimonial.objects.all()}
    return render(request, 'core/testimonials.html', context)

def faqpage(request):
    context = {**get_base_context(), 'faqs': FAQ.objects.filter(is_active=True)}
    return render(request, 'core/faq.html', context)

# def contactpage(request):
#     context = get_base_context() # Base context already has contact_details
#     return render(request, 'core/contact.html', context)    

# core/views.py
from django.shortcuts import render, redirect
from .models import ContactDetails, ContactFormHomePage # Assuming you store contact form submissions here

def contactpage(request):
    context = get_base_context() # Your existing helper
    
    if request.method == "POST":
        # Save the data
        ContactFormHomePage.objects.create(
            identifier="contact_page",
            name=request.POST.get("name"),
            company_name=request.POST.get("company_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subjectMessage=request.POST.get("subjectMessage"),
            message=request.POST.get("message"),
        )
        
        # Add a success flag to the context
        context['success'] = True
        
    return render(request, 'core/contact.html', context)

def aboutpage(request):
    context = get_base_context()
    return render(request, 'core/aboutUs.html', context)

from django.shortcuts import get_object_or_404

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    context = {**get_base_context(), 'service': service}
    return render(request, 'core/service_detail.html', context)
