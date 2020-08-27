from django.urls import path
from django.contrib import admin
from app_tours.views import MainView, DepartureView, TourView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('departure/<str:departure_id>/', DepartureView.as_view()),
    path('tour/<int:id>/', TourView.as_view()),
]
