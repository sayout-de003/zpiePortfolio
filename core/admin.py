from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import (
    Logo, Header_title, HomepageHero, text_for_brief, HomepageBrief,
    Service, KeyFeature, Client, Project, Publication, Blog,
    Event, Testimonial, FAQ, ContactDetails, ContactType, CompanyPages
)

admin.site.register(Logo)
admin.site.register(Header_title)
admin.site.register(HomepageHero)
admin.site.register(text_for_brief)
admin.site.register(HomepageBrief)
admin.site.register(Service)
admin.site.register(KeyFeature)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Blog)
admin.site.register(Event)
admin.site.register(Testimonial)
admin.site.register(FAQ)
admin.site.register(ContactType)
admin.site.register(ContactDetails)
admin.site.register(CompanyPages)
# admin.py
from .models import ContactFormHomePage

@admin.register(ContactFormHomePage)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "company_name", "subjectMessage")
    search_fields = ("name", "email", "company_name")
