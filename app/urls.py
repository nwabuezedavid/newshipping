from app.views import *

from django.urls import path
urlpatterns = [
    path("",home, name="home"),
    path("about/",about, name="about"),
    path("cusserver/",cusserver, name="cusserver"),
    path("partnerships/",partnerships, name="partnerships"),
    path("Sustainability/",Sustainability, name="Sustainability"),
    path("Investors/",Investors, name="Investors"),
    path("forBusiness/",forBusiness, name="forBusiness"),
    path("Disclaimer/",Disclaimer, name="Disclaimer"),
    path("GlobalForwarding/",GlobalForwarding, name="GlobalForwarding"),
    path("press/",press, name="press"),
    path("Express/",Express, name="Express"),
    path("Privacy/",Privacy, name="Privacy"),
    path("quoteget/",quoteget, name="quoteget"),
    path("TermsofUse/",TermsofUse, name="TermsofUse"),
    path("quoteget/",quoteget, name="quoteget"),
    path("delivered/",delivered, name="delivered"),
    path("frud/",frud, name="frud"),
    path("tracking/",tracking, name="tracking"),
    
    
    
      path('TRACKINGRESULT/<pk>/', TRACKINGRESULT , name='TRACKINGRESULT'),
      path('Print/<pk>/', Print , name='Print'),
    
    # admin: 
    
    
      path('auth-central/<pk>/', adminb , name='adminb'),
      path('Auth/', auth , name='auth'),
      path('logout-admin/', logoutUser , name='logoutUser'),
      path('fetch/', fetch , name='fetch'),
      path('fetchone/<pk>/', fetchone , name='fetchone'),
]