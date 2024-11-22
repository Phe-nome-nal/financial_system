from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('interest_rate_risk/search', interest_rate_risk_search),
    path('interest_rate_risk/test', interest_rate_risk_test),
    path('currency_risk/search', currency_risk_search),
    path('currency_risk/test', currency_risk_test),
    path('stock_price_risk/search', stock_price_risk_search),
    path('stock_price_risk/test', stock_price_risk_test),
    path('smart_interest_rate_risk', smart_interest_rate_risk),
    path('smart_currency_risk', smart_currency_risk),
    path('smart_stock_price_risk', smart_stock_price_risk),
]
