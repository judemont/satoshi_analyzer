from datetime import datetime, timedelta
import matplotlib.pyplot as plt

TIME_DELTA = 0

with open("./satoshi_activity.txt", "r") as file:
    activities = file.readlines()

active_days = [
    int((datetime.fromtimestamp(int(date_string.strip())) + timedelta(hours=TIME_DELTA)).timestamp() / 86400) for date_string in activities
]

for i in activities:
    print(datetime.fromtimestamp(int(i)).strftime("%d/%m/%Y"))

days_count = [active_days.count(day) for day in range(min(active_days), max(active_days) + 1)]

xpoints = list(range(min(active_days), max(active_days) + 1))
ypoints = days_count

plt.plot(xpoints, ypoints)

plt.title("Satoshi Nakamoto Active Days")
plt.xlabel("Date")
plt.ylabel("Number of Interactions")
plt.tight_layout()  # Ajuste le layout pour éviter le chevauchement
plt.show()
