import datetime as dt

def excel_date(date1):
    temp = dt.datetime(1899, 12, 30)    # Note, not 31st Dec but 30th!
    delta = date1 - temp
    return float(delta.days) + (float(delta.seconds) / 86400)

print(excel_date(dt.datetime.now))

# Doesn't work and not my code