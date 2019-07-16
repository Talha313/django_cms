from django.conf.urls import url

from mysite.apps.webapp import views

app_name = 'webapp'

urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='signup'),
    url(r'^$', views.IndexView.as_view(), name='home'),

    # url(r'^about$', views.AboutView.as_view(template_name="about.html")),

    url(r'^employment-attorneys-jesse-unruh.html/?$', views.AboutView.as_view(template_name="about.html")),

    # url(r'^about/?$', views.AboutView.as_view(), name='about'),
    url(r'^jet-contact.html/?$', views.ContactView.as_view(), name='contact'),
    url(r'^subscribe$', views.SubscribeView.as_view(), name='subscribe'),
    url(r'^service_contact$', views.ServiceContactView.as_view(), name='service-contact'),
    url(r'^dashboard/?$', views.Dashboard.as_view(), name='dashboard'),

    # url(r'^flsa-claims-attorney-florida.html/$', views.FLSAView.as_view(), name='flsa-claims-attorney-florida.html'),
    # url('disability-lawyer-florida.html', views.DisabilityView.as_view(), name='disability-lawyer-florida.html'),
    # url('discrimination-attorney-florida.html/', views.DiscriminationView.as_view(), name='discrimination-attorney-florida.html'),
    # url('flsa-employment-attorney-florida.html/', views.PriceView.as_view(), name='flsa-employment-attorney-florida.html'),
    # url('fixed-fee-employment-contracts.html/', views.FeeView.as_view(), name='fixed-fee-employment-contracts.html'),
    # url('fixed-fee-litigation-defense.html/$', views.DoView.as_view(), name='fixed-fee-litigation-defense.html'),
    # path('page/', include('django.contrib.flatpages.urls')),

]
