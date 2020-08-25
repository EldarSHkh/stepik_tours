from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'index.html', {}
        )


class DepartureView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'departure.html', {}
        )


class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'tour.html',
        )
