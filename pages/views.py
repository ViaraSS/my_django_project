from django.views.generic import TemplateView


class AboutPageView(TemplateView):
    template_name = 'about.html'


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
