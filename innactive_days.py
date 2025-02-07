from datetime import datetime, timedelta
TIME_DELTA = -6

with open("./satoshi_activity.txt", "r") as file:
    activities = file.readlines()

# Convertir les dates en jours
active_days = [
    int((datetime.fromtimestamp(int(date_string.strip())) + timedelta(hours=TIME_DELTA)).timestamp() / 86400) for date_string in activities
]
innactives = []

innactives_temp = []
for i in range(min(active_days), max(active_days)):
    if i not in active_days:
        innactives_temp.append(i)
    else:
        # print(innactives_temp)
        if len(innactives_temp) >= 1 and max(innactives_temp) - min(innactives_temp) <= 0:
            innactives.append((min(innactives_temp), max(innactives_temp)))
        innactives_temp = []

for a in innactives:
    print(datetime.fromtimestamp(a[0] * 86400).strftime("%d/%m/%Y") + " - " + datetime.fromtimestamp(a[1] * 86400).strftime("%d/%m/%Y") + " : " + str(a[1]-a[0]))