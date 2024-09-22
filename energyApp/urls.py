from django.urls import path
from . import views

urlpatterns = [
    # Float routes with parameters
    path('set-device-usage/<value1>/<value2>/<value3>/<value4>/<value5>/', views.add_float_data, name='add_float_data'),
    path('device-usage-values/', views.get_float_data, name='get_float_data'),

    # Boolean routes with parameters
    path('set-switch/<str:bool1>/<str:bool2>/<str:bool3>/', views.add_boolean_data, name='add_boolean_data'),
    path('switch-state-values/', views.get_boolean_data, name='get_boolean_data'),
]
