import datetime

current_time = datetime.datetime.now()


date_format = current_time.strftime("%b %d %Y")

timestamp = current_time.timestamp()

# Formater les secondes avec des virgules et en notation scientifique
second = f"{timestamp:,.4f}"
scientific = f"{timestamp:.2e}"


print(f"Seconds since January 1, 1970: {second} or {scientific} in scientific notation")
print(date_format)
