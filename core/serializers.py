from core.models import Logo, Header_title, HomepageHero, text_for_brief, HomepageBrief, Service, KeyFeature, Client, Project, Publication, Blog, Event, Testimonial, FAQ, ContactDetails, CompanyPages
from rest_framework import serializers

class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'

class Header_titleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header_title
        fields = '__all__'

class HomepageHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageHero
        fields = '__all__'

class text_for_briefSerializer(serializers.ModelSerializer):
    class Meta:
        model = text_for_brief
        fields = '__all__'

class HomepageBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomepageBrief
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class KeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = '__all__'
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class ContactDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactDetails
        fields = '__all__'

class CompanyPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyPages
        fields = '__all__'