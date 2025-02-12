days = int(input("Enter number of days: "))
hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
seconds = int(input("Enter number of seconds: "))

total_seconds = int((days * 86400) + (hours * 3600) + (minutes * 60) + seconds)

print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds", "is equal to", total_seconds, "seconds")