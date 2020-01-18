# -*- coding:utf-8 -*-
from django.urls import path
from .views import ShoppingCarView
from .settlement_view import SettlementView

urlpatterns = [
    path('shopping_car/', ShoppingCarView.as_view()),
    path('settlement/', SettlementView.as_view())
]
