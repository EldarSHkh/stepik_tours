from django.http import Http404, HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render
from django.views import View

import random

from app_tours.data import departures, description, tours, title, subtitle


class MainView(View):
    def get(self, request, *args, **kwargs):
        random_tour_id = random.sample(range(1, len(tours)), 6)
        tour = {tour_id: tours[tour_id] for tour_id in random_tour_id}
        context = {
            "title": title,
            "subtitile": subtitle,
            "description": description,
            'departures': departures,
            'active': '',
            "tours": tour,

        }
        return render(
            request, 'index.html', context=context)


class DepartureView(View):

    def get(self, request, departure):
        if departure not in departures.keys():
            raise Http404
        departure_tours = {key: value for key, value in tours.items() if value['departure'] == departure}
        list_tour = departure_tours.values()
        max_cost = max(list_tour, key=lambda x: x['price'])
        min_cost = min(list_tour, key=lambda x: x['price'])
        max_nights = max(list_tour, key=lambda x: x['nights'])
        min_nights = min(list_tour, key=lambda x: x['nights'])
        context = {'title': title,
                   'tour_title': departures[departure],
                   'active': departure,
                   'departure': departures[departure],
                   'departure_tours': departure_tours,
                   'tour_count': len(departure_tours),
                   'max_cost': max_cost['price'],
                   'max_nights': max_nights['nights'],
                   'min_cost': min_cost['price'],
                   'min_nights': min_nights['nights'],
                   'departures': departures,
                   }

        return render(request, 'departure.html', context=context)


class TourView(View):
    def get(self, request, id):
        if id not in tours:
            raise Http404

        tour_title = tours[id]["title"]
        description = tours[id]["description"]
        departure = departures[tours[id]['departure']]
        picture = tours[id]["picture"]
        price = tours[id]["price"]
        stars = tours[id]["stars"]
        country = tours[id]["country"]
        nights = tours[id]["nights"]
        date = tours[id]["date"]

        context = {
            "tour_title": tour_title,
            "title": title,
            "description": description,
            "departure": departure,
            "picture": picture,
            "price": price,
            "stars": stars,
            "country": country,
            "nights": nights,
            "date": date,
            'active': departure,
            'departures': departures
        }

        return render(
            request, 'tour.html', context=context
        )


def my_handler404(request, exception):
    return HttpResponseNotFound('404')


def my_handler500(request):
    return HttpResponseServerError('500')
