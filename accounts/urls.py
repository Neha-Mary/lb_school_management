from django.urls import include, path
from .views import *


urlpatterns = [path('ac/login/', CustomLoginView.as_view(), name='custom-login'),
            
]