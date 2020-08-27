from django.http import Http404
from django.shortcuts import render
from django.views import View
from app_tours.data import departures, description, tours, title, subtitle


class MainView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": title,
            "subtitile": subtitle,
            "description": description
        }
        return render(
            request, 'index.html', context=context)


class DepartureView(View):
    def get(self, request, departure_id):
        if departure_id not in departures:
            raise Http404
        context = {
            "departure": departures[departure_id]
        }

        return render(
            request, 'departure.html', context=context
        )


class TourView(View):
    def get(self, request, id):
        if id not in tours:
            raise Http404

        title = tours[id]["title"]
        description = tours[id]["description"]
        departure = tours[id]["departure"]
        picture = tours[id]["picture"]
        price = tours[id]["price"]
        stars = tours[id]["stars"]
        country = tours[id]["country"]
        nights = tours[id]["nights"]
        date = tours[id]["date"]

        context = {
            "title": title,
            "description": description,
            "departure": departure,
            "picture": picture,
            "price": price,
            "stars": stars,
            "country": country,
            "nights": nights,
            "date": date
        }

        return render(
            request, 'tour.html', context=context
        )
