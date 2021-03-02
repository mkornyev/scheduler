from django.core.management.base import BaseCommand
from datetime import datetime
from myTime.models import DailyHours, Location, Reservation, Report


# POPULATE SCRIPT

class Command(BaseCommand):
    args = '<this func takes no args>'
    help = 'A populate script for the current locations & hours.'

    def _createLocations(self):

      # HOURS
      EIGHT_AM = datetime(1, 1, 1, 8, 0, 0, 0)  # 8am
      TEN_AM = datetime(1, 1, 1, 10, 0, 0, 0)    # 10am
      FIVE_PM = datetime(1, 1, 1, 17, 0, 0, 0)  # 5pm 
      SEVEN_PM = datetime(1, 1, 1, 19, 0, 0, 0) # 7pm 

      # WEIGAND
      weigand = Location.objects.create(
        name='CMU Weigand Gymnasium',
        token='weigand', 
        max_capacity=10
      )

      weigand.hours.add(
        DailyHours.objects.create(day=0, opening=TEN_AM, closing=FIVE_PM), # SUN
        DailyHours.objects.create(day=1, opening=EIGHT_AM, closing=SEVEN_PM), 
        DailyHours.objects.create(day=2, opening=EIGHT_AM, closing=SEVEN_PM), 
        DailyHours.objects.create(day=3, opening=EIGHT_AM, closing=SEVEN_PM), # WED
        DailyHours.objects.create(day=4, opening=EIGHT_AM, closing=SEVEN_PM), 
        DailyHours.objects.create(day=5, opening=EIGHT_AM, closing=SEVEN_PM), 
        DailyHours.objects.create(day=6, opening=TEN_AM, closing=FIVE_PM), # SAT
      )

      weigand.save()

      # WEIGHT ROOM
      gym = Location.objects.create(
        name='CMU Weight Room',
        token='gym', 
        max_capacity=15
      )

      gym.hours.add(
        DailyHours.objects.create(day=0, opening=TEN_AM, closing=FIVE_PM), # SUN
        DailyHours.objects.create(day=1, opening=EIGHT_AM, closing=SEVEN_PM), 
        DailyHours.objects.create(day=2, opening=EIGHT_AM, closing=SEVEN_PM), 
        DailyHours.objects.create(day=3, opening=EIGHT_AM, closing=SEVEN_PM), # WED
        DailyHours.objects.create(day=4, opening=EIGHT_AM, closing=SEVEN_PM), 
        DailyHours.objects.create(day=5, opening=EIGHT_AM, closing=SEVEN_PM), 
        DailyHours.objects.create(day=6, opening=TEN_AM, closing=FIVE_PM), # SAT
      )

      gym.save()

      # RESERVATIONS
      gym.reservations.add(
        Reservation.objects.create(day=1, start_time=EIGHT_AM, end_time=TEN_AM),
        Reservation.objects.create(day=3, start_time=EIGHT_AM, end_time=TEN_AM),
      )

      # REPORTS 
      gym.reports.add(
        Report.objects.create(is_full=True, wait_time_minutes=15),
        # Report.objects.create(is_full=False),
      )

    def handle(self, *args, **options):
      self._createLocations()