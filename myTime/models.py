from django.db import models
# from myTime.utils import getTodaysHours

from datetime import datetime 

# CONSTANTS
WEEKDAYS = (
    (0, 'Sun'),
    (1, 'Mon'),
    (2, 'Tues'),
    (3, 'Wed'),
    (4, 'Thurs'),
    (5, 'Fri'),
    (6, 'Sat')
  )


# MODELS 

class DailyHours(models.Model):
  day = models.IntegerField(blank=False, choices=WEEKDAYS)
  opening = models.DateTimeField(blank=False)
  closing = models.DateTimeField(blank=False)

  # Returns the number of time periods from open to close
  # Param - periodLength - Minutes
  def getNumTimePeriods(self, periodLength=15):
    return int((self.closing - self.opening).seconds/60/periodLength) 

  # Returns the number of 15 minute offsets/periods before opening time
  # --> IF there is an earlier opening time in the week, otherwise returns 0
  # Param - periodLength - Minutes
  def getOffset(self, periodLength=15):
    earlierOpening = self.location_set.first().hours.order_by('opening').first().opening
    numPeriods = int((self.opening - earlierOpening).seconds/60/periodLength) 

    return [p for p in range(numPeriods)]

  def getDayOfWeek(self):
    return WEEKDAYS[self.day][1]

  class Meta:
    ordering = ['day', 'opening']


class Location(models.Model):
  name = models.CharField(max_length=50, blank=False)
  token = models.CharField(max_length=25, blank=False)
  max_capacity = models.IntegerField(blank=False)

  # FKs
  hours = models.ManyToManyField('DailyHours')
  reservations = models.ManyToManyField('Reservation')
  reports = models.ManyToManyField('Report')

  # Hours helpers
  def getOpeningDatetime(self):
    today = datetime.today().strftime('%w')
    return self.hours.filter(day=today).first().opening
  
  def getClosingDatetime(self):
    today = datetime.today().strftime('%w')
    return self.hours.filter(day=today).first().closing
  
  def getTodaysHours(self):
    return "{}am - {}pm".format(self.getOpeningDatetime().hour%12, self.getClosingDatetime().hour%12)

  class Meta:
    ordering = ['name']


class Reservation(models.Model):
  day = models.IntegerField(blank=False, choices=WEEKDAYS)
  start_time = models.DateTimeField(blank=False)
  end_time = models.DateTimeField(blank=False)
  reserved_at = models.DateTimeField(default=datetime.now, blank=False)

  class Meta:
    ordering = ['day', 'start_time']


class Report(models.Model):
  is_full = models.BooleanField(default=True, blank=False)
  wait_time_minutes = models.IntegerField(blank=True)   # User does not have to report wait time 
  reported_at = models.DateTimeField(default=datetime.now, blank=False)

  class Meta:
    ordering = ['reported_at']
