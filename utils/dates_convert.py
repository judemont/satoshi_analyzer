from datetime import datetime

input_file = "satoshi_commits.txt"

output_file = "timestamps.txt"


date_format = "%a, %d %b %Y %H:%M:%S %z"


timestamps = []


with open(input_file, "r", encoding='utf-8') as file:
    for line in file:
        date_str = line.strip()[:-1]
        if date_str: 

            timestamp = int(datetime.strptime(date_str, date_format).timestamp())
            timestamps.append(timestamp)


with open(output_file, "w", encoding='utf-8') as file:
    for ts in timestamps:
        file.write(f"{ts}\n")

print(f"Timestamps have been written to {output_file}.")
