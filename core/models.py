from email.policy import default
from enum import unique
from turtle import title
from django.db import models

# Create your models here.

# models needed in base.html
class Logo(models.Model):
    logo = models.ImageField(upload_to='logo/')
    def __str__(self):
        return self.logo.url

class Header_title(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField()
    bg_image = models.ImageField(upload_to='header/', blank = True , null = True) #through the heaser to show any bg image if want optional
    def __str__(self):
        return self.title


# Home page custom models
#  0. header from base.html
#  1. herosection 
#  2. brief section
#  3. service section (autoamtic handles in hone page using service model){for service in service model} - when service will be added it will be shown in that home with title ans short desc
#  4. key feature section (automatic handels in home page using keyf feature model) { for key_eature in key_features}
#  5. clients section horizontal scrolling with logo (automatic handels in home page using client model) { for client in client model}  
#  6. Project section (automatic handels in home page using project model) { for project in project model} - when project will be added it will be shown in that home with title ans short desc
#  7. Recent Publication - case study or research paper section (automatic handels in home page using publication model) { for publication in publication model} - when publication will be added it will be shown in that home with title ans short desc
#  8. Recent Blog - blog section (automatic handels in home page using blog model) { for blog in blog model} - when blog will be added it will be shown in that home with title ans short desc
#  9. Recent Event - event section (automatic handels in home page using event model) { for event in event model} - when event will be added it will be shown in that home with title ans short desc
#  10. Recent Testimonial - testimonial section (automatic handels in home page using testimonial model) { for testimonial in testimonial model} - when testimonial will be added it will be shown in that home with title ans short desc
#  11. Recent FAQ - FAQ section (automatic handels in home page using FAQ model) { for FAQ in FAQ model} - when FAQ will be added it will be shown in that home with title ans short desc
#  12. contact form section
#  13.footer from base.html



class HomepageHero(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(
        upload_to="homepage/hero/",
        null=True,
        blank=True
    )

    button_text = models.CharField(max_length=200, blank=True)
    button_url = models.URLField(blank=True)
    button_target = models.CharField(
        max_length=20,
        choices=[("_self", "Same Tab"), ("_blank", "New Tab")],
        default="_self"
    )

    button_color = models.CharField(max_length=50, blank=True)
    button_background_color = models.CharField(max_length=50, blank=True)
    button_border_color = models.CharField(max_length=50, blank=True)
    button_border_radius = models.CharField(max_length=20, blank=True)
    button_border_width = models.CharField(max_length=20, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Homepage Hero"


class text_for_brief(models.Model):
    identifier = models.CharField(
        max_length=100,
        unique=True,
        help_text="Example: homepage_brief_title"
    )
    title = models.CharField(max_length=200, default = "Brief about us")

    def __str__(self):
        return self.identifier


class HomepageBrief(models.Model):
    identifier = models.CharField(
        max_length=100,
        help_text="Unique key for frontend (e.g. who_we_are, what_we_build)"
    )

    title = models.CharField(max_length=200)

    short_description = models.TextField()
    url = models.URLField(blank=True, null = True, help_text="Add the url of the page to redirect to when the brief is clicked")

    bg_video = models.FileField(
        upload_to="homepage/brief/",
        null=True,
        blank=True
    )

    bg_image = models.ImageField(
        upload_to="homepage/brief/",
        null=True,
        blank=True
    )


    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"Homepage Brief – {self.identifier}"


class ContactFormHomePage(models.Model):
    identifier = models.CharField(
        max_length=100,
        help_text="Unique key for frontend (e.g. contact_form_home_page)"
    )
    # name of the person who want to contact us
    name = models.CharField(max_length=200)
    # comapny name he wants to contact
    company_name = models.CharField(max_length=200)
    # email of the person who want to contact us
    email = models.EmailField()
    # phone number of the person who want to contact us
    phone = models.CharField(max_length=20)
    # subject of the message
    subjectMessage = models.CharField(max_length=200)
    # message of the person who want to contact us
    message = models.TextField()
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name






from django.db import models
from django.utils.text import slugify


class Service(models.Model):
    title = models.CharField(
        max_length=200,
        unique=True
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
        allow_unicode=True
    )

    short_description = models.CharField(
        max_length=300,
        blank=True
    )

    description = models.TextField()

    logo_icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Lucide icon name (e.g. code, cloud, brain)"
    )

    banner_image = models.ImageField(
        upload_to="services/banner/",
        null=True,
        blank=True
    )

    banner_video = models.FileField(
        upload_to="services/banner/",
        null=True,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def save(self, *args, **kwargs):
        """
        Auto-generate unique slug from title (only if empty)
        """
        if not self.slug:
            base_slug = slugify(self.title, allow_unicode=True)
            slug = base_slug
            counter = 1

            while Service.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



# key features
class KeyFeature(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='key_feature/' , null = True , blank = True)
    def __str__(self):
        return self.title


        
# clients 
class Client(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='client/')
    url = models.URLField(blank=True, null = True)
    def __str__(self):
        return self.name

# projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    shortDesc = models.CharField(max_length=300, null = True , blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to='project/')
    url = models.URLField(blank=True, null = True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

# publications
class Publication(models.Model):
    title = models.CharField(max_length=200)
    shortDesc = models.CharField(max_length=300, null = True , blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to='publication/')
    url = models.URLField(blank=True, null = True)

    def __str__(self):
        return self.title

# blogs
class Blog(models.Model):
    title = models.CharField(max_length=200)
    shortDesc = models.CharField(max_length=300, null = True , blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/')
    url = models.URLField(blank=True, null = True)
    def __str__(self):
        return self.title

# events        
class Event(models.Model):
    title = models.CharField(max_length=200)
    shortDesc = models.CharField(max_length=300, null = True , blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to='event/')
    url = models.URLField(blank=True, null = True)
    def __str__(self):
        return self.title

# testimonials
class Testimonial(models.Model):
    title = models.CharField(max_length=200)
    shortDesc = models.CharField(max_length=300, null = True , blank = True)
    description = models.TextField()
    image = models.ImageField(upload_to='testimonial/', blank=True, null=True)
    url = models.URLField(blank=True, null = True)
    def __str__(self):
        return self.title

# faq
class FAQ(models.Model):
    title = models.CharField(max_length=200)
    shortDesc = models.CharField(max_length=300, null = True , blank = True)    
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

from django.db import models
from django.core.exceptions import ValidationError

class ContactType(models.Model):
    name = models.CharField(max_length=50, unique=True, help_text="e.g. phone, email, map, website")
    requires_url = models.BooleanField(default=True, help_text="Uncheck if this type does NOT need URL (e.g. phone/email)")
    lucideicon = models.CharField(max_length=50, blank=True, help_text="Lucide icon name (e.g. phone, email, map-pin)")

    def __str__(self):
        return self.name


class ContactDetails(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='contactdetails/')
    type = models.ForeignKey(ContactType, on_delete=models.CASCADE, related_name="contacts")
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    # validation
    def clean(self):
    # safety checks to prevent admin crash
        if not self.type:
            return

        if self.type.requires_url and not self.url:
            raise ValidationError({
                "url": f"URL is required for contact type '{self.type.name}'."
        })


class CompanyPages(models.Model):
    title = models.CharField(max_length=200)            
    description = models.TextField()
    image = models.ImageField(upload_to='companypage/')
    url = models.URLField(blank=True, null = True)
    def __str__(self):
        return self.title

  


class Address(models.Model):
    address = models.TextField()
    google_map_url = models.URLField(blank=True, null = True)
    def __str__(self):
        return self.address


from django.db import models


class DemoCategory(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        help_text="Example: Restaurant, Pet Shop, E-commerce"
    )
    description = models.CharField(
        max_length=255,
        blank=True
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class DemoWebsite(models.Model):
    category = models.ForeignKey(
        DemoCategory,
        on_delete=models.CASCADE,
        related_name="demos"
    )
    title = models.CharField(
        max_length=200,
        help_text="Example: Modern Restaurant Website"
    )
    demo_url = models.URLField()
    link_text = models.CharField(
        max_length=100,
        default="View Demo"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.category.title})"
