from datetime import datetime, timedelta
import matplotlib.pyplot as plt

TIME_DELTA = -7

activities = open("./satoshi_activity.txt", "r").readlines()


active_hours = [(datetime.fromtimestamp(int(date_string)) + timedelta(hours=TIME_DELTA)).hour for date_string in activities]
hours_chount = [active_hours.count(hour) for hour in range(24)]

print(len(activities))

xpoints = [i for i in range(24)]
ypoints = hours_chount

plt.bar(xpoints, ypoints)
plt.xticks(xpoints)
plt.yticks(ypoints)
plt.title("Satoshi Nakamoto active hours UTC" + str(TIME_DELTA))
plt.xlabel("Hour")
plt.ylabel("Numbers of interactions")
plt.show()