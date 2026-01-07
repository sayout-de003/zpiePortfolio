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


from .models import DemoCategory, DemoWebsite

class DemoWebsiteInline(admin.TabularInline):
    model = DemoWebsite
    extra = 1
    fields = ("title", "demo_url", "link_text", "is_active")
    show_change_link = True


@admin.register(DemoCategory)
class DemoCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title",)
    inlines = [DemoWebsiteInline]


@admin.register(DemoWebsite)
class DemoWebsiteAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "demo_url", "is_active", "created_at")
    list_filter = ("category", "is_active")
    search_fields = ("title", "category__title")
    ordering = ("category", "title")
#njfa