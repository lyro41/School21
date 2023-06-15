import datetime
    
    
def register_booking(booking):
    bookings = {
        "Вагнер": [
            (datetime.datetime(2022, 9, 1, 10), datetime.datetime(2022, 9, 1, 11)),
            (datetime.datetime(2022, 9, 1, 15), datetime.datetime(2022, 9, 1, 15, 20)),
            (datetime.datetime(2022, 9, 1, 23), datetime.datetime(2022, 9, 2, 7)),
        ],
        "Линдеманн": [
            (datetime.datetime(2022, 9, 1, 10), datetime.datetime(2022, 9, 1, 10, 15)),
        ],
        "Бах": [],
    }
    if booking.room_name not in bookings:
        raise KeyError()
    free = True
    for tpl in bookings[booking.room_name]:
        if tpl[0] <= booking.start < tpl[1] or tpl[0] < booking.end <= tpl[1]:
            free = False
        if booking.start <= tpl[1] and booking.end >= tpl[0]:
            free = False
    return free