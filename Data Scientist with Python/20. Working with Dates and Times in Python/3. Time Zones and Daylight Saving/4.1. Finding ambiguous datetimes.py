# Finding ambiguous datetimes

# At the end of lesson 2, we saw something anomalous in our bike trip duration data. Let's see if we can identify what the problem might be.
# The data has is loaded as onebike_datetimes, and tz has already been imported from dateutil.

# Instructions

# •	Loop over the trips in onebike_datetimes:
# o	Print any rides whose start is ambiguous.
# o	Print any rides whose end is ambiguous.

# Loop over trips
for trip in onebike_datetimes:
  # Rides with ambiguous start
  if tz.datetime_ambiguous(trip['start']):
    print("Ambiguous start at " + str(trip['start']))
  # Rides with ambiguous end
  if tz.datetime_ambiguous(trip['end']):
    print("Ambiguous end at " + str(trip['end']))