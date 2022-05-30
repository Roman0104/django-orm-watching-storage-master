from datacenter.models import Visit
from datacenter.models import get_duration, format_duration, is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = []

    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': localtime(visit.entered_at),
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(get_duration(visit))
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

