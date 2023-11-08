from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutUsView(TemplateView):
    template_name = 'aboutus.html'

class OurServicesView(TemplateView):
    template_name = 'ourservices.html'

class BlogsView(TemplateView):
    template_name = 'blogs.html'

class CareersView(TemplateView):
    template_name = 'careers.html'

class ContactUsView(TemplateView):
    template_name = 'contactus.html'

class BlogArticlesView(TemplateView):
    template_name = 'blog_articles.html'

class BlogAuthorsView(TemplateView):
    template_name = 'blogs.html#authors'
