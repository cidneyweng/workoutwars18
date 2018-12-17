# workoutwarsapp/urls.py
from django.conf.urls import url
from workoutwarsapp import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

favicon_view = RedirectView.as_view(url='/static/images/myfavicon.ico', permanent=True)

urlpatterns = [
    # home page
    url(r'^$', views.HomePageView.as_view()),

    # authentication pages
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^signup/$', views.signup, name='signup',),

    # workout pages
    url(r'^add/$', views.addworkout, name='add',),
    url(r'^scoreboard/$', views.scoreboard, name='scoreboard',),
    url(r'^indiv/(?P<username>[\w.\-]+)/', views.indiv, name='indiv',),

    url(r'^feed/', views.feed, name='feed',),
    url(r'^feedscore/', views.feedscore, name='feedscore',),

    url(r'^rankings/$', views.rankings, name='rankings',),
    url(r'^coach/$', views.coach, name='coach',),

    #favicon
    url(r'^favicon\.ico$', favicon_view,)
]

