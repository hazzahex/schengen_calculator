from django.shortcuts import render, redirect
from datetime import timezone, datetime
from .utils import get_windows_trips, create_trip, get_window_start, get_trip, update_open_trip, update_trip
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


@login_required()
def home_view(request):
    trips = get_windows_trips()
    window_start = get_window_start()
    count = 0
    for trip in trips:
        update_open_trip(trip.pk)
        if trip.start_date.date() < window_start:
            days_in_window = (trip.end_date.date() - window_start).days
            print(f'Trip at end of window')
            print(f'Days in window: {days_in_window}')
            count += days_in_window
        else:
            count += trip.day_count
    progress = round((count / 90) * 100)
    context = {
        'trips': trips,
        'count': count,
        'progress': progress,
        'window_start': get_window_start()
    }
    return render(request, 'main/home.html', context=context)


@login_required()
def refresh_trip(request, trip_pk):
    print(trip_pk)
    update_open_trip(trip_pk)
    return redirect('home')


@login_required()
def new_trip_view(request):
    context = {}
    print("test")
    if request.method == "POST":
        print(request.POST.get("end_date"))
        if request.POST.get("end_date") == "":
            current_date = datetime.now().strftime("%Y-%m-%d")
            new_trip = create_trip(request.POST.get("name"), request.POST.get(
                "start_date"), current_date, request.POST.get("current") == "on")
        else:
            new_trip = create_trip(request.POST.get("name"), request.POST.get(
                "start_date"), request.POST.get("end_date"), request.POST.get("current") == "on")
        return redirect('home')
    else:
        return render(request, 'main/create_trip.html', context=context)


@login_required()
def trip_view(request, trip_pk):
    trip = get_trip(trip_pk)
    context = {
        'trip': trip
    }
    return render(request, 'main/trip.html', context=context)


@login_required()
def delete_trip(request, trip_pk):
    trip = get_trip(trip_pk)
    trip.delete()
    return redirect('home')


@login_required
def update_trip_view(request, trip_pk):
    if request.method == "POST":
        start_date = datetime.strptime(
            request.POST.get("start_date"), '%Y-%m-%d')
        end_date = datetime.strptime(request.POST.get("end_date"), '%Y-%m-%d')
        name = request.POST.get("name")
        current = request.POST.get("current") == "on"
        update_trip(trip_pk, name, start_date, end_date, current)
        return redirect('home')
    else:
        context = {
            'trip': get_trip(trip_pk)
        }
        return render(request, 'main/update_trip.html', context=context)
