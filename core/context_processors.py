from .models import Logo, Header_title, CompanyPages, ContactDetails, Address, Service

def base_context(request):
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
