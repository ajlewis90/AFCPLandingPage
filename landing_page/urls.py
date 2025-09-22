from django.urls import path, include
from . import views as landing_page_views

app_name='landing_page'

urlpatterns = [

    #url(r'^$', landing_page_views.display_landing_page, name='display_landing_page'),

    path('', landing_page_views.display_landing_page, name='landing_page'),

    #path('businesses/', landing_page_views.display_b2b_signup_page, name='b2b_signup_page'),

    path('add-contact/', landing_page_views.add_contact, name='add_contact'),

    path('add-business-contact/', landing_page_views.add_business_contact, name='add_business_contact'),
     
]