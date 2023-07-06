from django.urls import path, re_path
from .views import CafeHome, ShowDish

app_name = 'cafe'

urlpatterns = [
    path('', CafeHome.as_view(), name='home'),
    path('dish/<int:id>/<slug:slug>/', ShowDish.as_view(), name='dish'),
]

