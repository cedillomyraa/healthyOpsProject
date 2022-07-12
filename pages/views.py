from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CatalogPageView(TemplateView):
    template_name = 'catalog.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

class SignupPageView(TemplateView):
    template_name = 'signup.html'

class CartPageView(TemplateView):
    template_name = 'cart.html'