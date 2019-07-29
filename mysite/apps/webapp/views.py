from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

from accounts.decorators import check_recaptcha
from accounts.forms import UserForm
from mysite.apps.webapp.forms import ContactForm, SubscribeForm
from mysite.apps.webapp.models import *


class IndexView(TemplateView):
    template_name = 'home.html'
    form_class = UserForm

    def get(self, request):
        litigations = Litigation.objects.filter(is_active=True)
        print(litigations)
        testimonial = Testimonial.objects.last()
        clients = Client.objects.filter(is_active=True)
        return render(request, self.template_name,
                      {'litigations': litigations, 'testimonial': testimonial, 'clients': clients, 'home': 'active',
                       'form': self.form_class})


class AboutView(TemplateView):
    template_name = 'about.html'

    def get(self, request):
        # import pdb;pdb.set_trace()
        abouts = About.objects.filter(is_active=True)
        print(abouts)
        return render(request, self.template_name, {'abouts': abouts, 'about': 'active'})


class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, {'contact': 'active', 'form': ContactForm()})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            messages.success(request, 'Thanks You for contacting with us, We will contact you shortly.')
        return render(request, self.template_name, {'form': form})


class SubscribeView(TemplateView):
    # template_name = 'contact.html'

    def post(self, request):
        form = SubscribeForm(request.POST)
        url = request.POST.get('url')
        if form.is_valid() and request.recaptcha_is_valid:
            form.save()
            messages.success(request, 'Successfully Subscribed!')

        return redirect(url)


class FLSAView(TemplateView):
    template_name = 'flsa-claims-attorney-florida.html'

    def get(self, request):
        object = FlsaClaim.objects.last()
        print(object, "dhdhhdhdhdhdh")
        return render(request, self.template_name, {"object": object, 'services': 'active'})


class DisabilityView(TemplateView):
    template_name = 'disability-lawyer-florida.html'

    def get(self, request):
        return render(request, self.template_name, {'services': 'active'})


class DiscriminationView(TemplateView):
    template_name = 'discrimination-attorney-florida.html'

    def get(self, request):
        return render(request, self.template_name, {'services': 'active'})


class PriceView(TemplateView):
    template_name = 'flsa-employment-attorney-florida.html'

    def get(self, request):
        return render(request, self.template_name, {'services': 'active'})


class FeeView(TemplateView):
    template_name = "fixed-fee-employment-contracts.html"

    def get(self, request):
        return render(request, self.template_name, {'services': 'active'})

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        question = request.POST.get('question')
        print(first_name, last_name, email, question)

        contact = ServicesContact(firstName=first_name, lastName=last_name, email=email, question=question)
        contact.save()
        return render(request, self.template_name)


class DoView(TemplateView):
    template_name = "fixed-fee-litigation-defense.html"

    def get(self, request):
        return render(request, self.template_name, {'services': 'active'})


class ServiceContactView(TemplateView):
    # template_name = 'contact.html'

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        question = request.POST.get('question')
        url = request.POST.get('url')
        contact = ServicesContact(firstName=first_name, lastName=last_name, email=email, question=question)
        contact.save()
        return redirect(url)
