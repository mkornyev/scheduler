from django.core.management.base import BaseCommand
from datetime import datetime
from myTime.models import DailyHours, Location, Reservation, Report


# POPULATE SCRIPT

class Command(BaseCommand):
    args = '<this func takes no args>'
    help = 'A populate script for the current locations & hours.'

    def _destroyLocations(self):
      locCnt = Location.objects.count()
      Location.objects.all().delete()

      hoursCnt = DailyHours.objects.count()
      DailyHours.objects.all().delete()

      resCnt = Reservation.objects.count()
      Reservation.objects.all().delete()

      repCnt = Report.objects.count()
      Report.objects.all().delete()

      print("{} Locations, {} Hours, {} Reservations, and {} Reports Deleted".format(locCnt, hoursCnt, resCnt, repCnt))

    def handle(self, *args, **options):
      self._destroyLocations()