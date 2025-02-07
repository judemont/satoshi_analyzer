from datetime import datetime, timedelta
import matplotlib.pyplot as plt

TIME_DELTA = -5

activities = open("./satoshi_activity.txt", "r").readlines()


active_days = [(datetime.fromtimestamp(int(date_string)) + timedelta(hours=TIME_DELTA)).weekday() for date_string in activities]
days_chount = [active_days.count(hour) for hour in range(7)]

print(len(activities))

xpoints = [i for i in range(7)]
ypoints = days_chount

plt.bar(xpoints, ypoints)
plt.xticks(xpoints)
plt.yticks(ypoints)
plt.title("Satoshi Nakamoto active weekdays")
plt.xlabel("Day (Monday == 0 ... Sunday == 6)")
plt.ylabel("Numbers of interactions")
plt.show()