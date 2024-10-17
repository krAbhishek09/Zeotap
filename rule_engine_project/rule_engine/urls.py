
from django.urls import path
from .views import create_rule_view, evaluate_rule_view

urlpatterns = [
    path('create/', create_rule_view, name='create_rule'),
    path('evaluate/', evaluate_rule_view, name='evaluate_rule'),
]
