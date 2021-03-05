from django.urls import path
from .views import home_page, decode_page, encrypt_page


urlpatterns = [
    path('', home_page, name='home'),

    path('decode/', decode_page, name='decode'),

    path('encrypt/', encrypt_page, name='encrypt'),
]