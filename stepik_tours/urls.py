from django.urls import path
from django.contrib import admin

from app_tours.views import MainView, DepartureView, TourView, my_handler404, my_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('departure/<str:departure>/', DepartureView.as_view(), name='departure'),
    path('tour/<int:id>/', TourView.as_view(), name='tour'),
]

handler404 = my_handler404
handler500 = my_handler500
