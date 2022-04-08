•	Iterate over the first twenty items in the labeled_entries list:
	o	Print each item's stop.
	o	Print each item's date.
	o	Print each item's riders.

# Iterate over the first twenty items in labeled_entries
for item in labeled_entries[:20]:
    # Print each item's stop
    print(item.stop)

    # Print each item's date
    print(item.date)

    # Print each item's riders
    print(item.riders)
