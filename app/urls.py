from django.urls import path
from app.views import HomeView, AboutUsView, OurServicesView, BlogsView, CareersView, ContactUsView, BlogArticlesView, BlogAuthorsView

app_name = 'app'
urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('aboutus', AboutUsView.as_view(), name='aboutus'),
    path('ourservices', OurServicesView.as_view(), name='ourservices'),
    path('blogs', BlogsView.as_view(), name='blogs'),
    path('careers', CareersView.as_view(), name='careers'),
    path('contactus', ContactUsView.as_view(), name='contactus'),
    path('blog_articles', BlogArticlesView.as_view(), name='blog_articles'),
    path('blog_authors', BlogAuthorsView.as_view(), name='blog_authors'),
]
