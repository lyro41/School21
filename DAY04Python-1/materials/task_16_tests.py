from task16 import Booking, create_booking
import datetime
import json
    
    
def test_booking():
    try:
        Booking("abc", datetime.datetime(2022, 9, 1, 15), datetime.datetime(2022, 9, 1, 10))
    except ValueError:
        pass
    except:
        raise AssertionError("Если окончание брони - более раннее время, чем начало брони, нужно вызывать исключение ValueError")
    
    booking = Booking("abc", datetime.datetime(2022, 9, 1, 10), datetime.datetime(2022, 9, 1, 15, 5))
    assert booking.duration == 5 * 60 + 5, "атрибут duration считается неверно. Нужно в минутах. Гарантируется, что длина тестовой встречи кратна одной минуте"
    assert booking.start_date == "2022-09-01", "дата начала неправильная"
    assert booking.end_date == "2022-09-01", "дата окончания неправильная"
    assert booking.start_time == "10:00", "время начала неправильное"
    assert booking.end_time == "15:05", "время окончания неправильное"
    assert booking.room_name == "abc", "название комнаты изменилось"
    booking.start = datetime.datetime(2022, 9, 1, 9)
    assert booking.start_time == "09:00", "после того, как назначили новый start, время начала не поменялось"
    assert booking.duration == 6 * 60 + 5, "после того, как назначили новый start, продолжительность брони не поменялась"
    
    
    booking = Booking("abc", datetime.datetime(2022, 9, 1, 23), datetime.datetime(2022, 9, 2, 1, 5))
    assert booking.duration == 2 * 60 + 5, "атрибут duration считается неверно. Нужно в минутах. Гарантируется, что длина тестовой встречи кратна одной минуте"
    assert booking.start_date == "2022-09-01", "дата начала неправильная"
    assert booking.end_date == "2022-09-02", "дата окончания неправильная"
    assert booking.start_time == "23:00", "время начала неправильное"
    assert booking.end_time == "01:05", "время окончания неправильное"
    assert booking.room_name == "abc", "название комнаты изменилось"
    
    

def test_create_booking():
    def to_dict(b):
        return {
            "room_name": b.room_name,
            "start_date": b.start_date,
            "start_time": b.start_time,
            "end_date": b.end_date,
            "end_time": b.end_time,
            "duration": b.duration,
        }
    
    bad = [
        Booking("Вагнер", datetime.datetime(2022, 9, 1, 14), datetime.datetime(2022, 9, 1, 15, 15)),
        Booking("Вагнер", datetime.datetime(2022, 9, 1, 14), datetime.datetime(2022, 9, 1, 16, 15)),
        Booking("Вагнер", datetime.datetime(2022, 9, 1, 15), datetime.datetime(2022, 9, 1, 16, 15)),
        Booking("Вагнер", datetime.datetime(2022, 9, 1, 15, 10), datetime.datetime(2022, 9, 1, 15, 20)),
        Booking("Вагнер", datetime.datetime(2022, 9, 1, 22), datetime.datetime(2022, 9, 2, 1)),
        Booking("Вагнер", datetime.datetime(2022, 9, 2, 0, 3), datetime.datetime(2022, 9, 2, 1)),
    ]
    good = [
        Booking("Вагнер", datetime.datetime(2022, 10, 1, 14), datetime.datetime(2022, 10, 1, 15, 15)),
        Booking("Линдеманн", datetime.datetime(2022, 10, 1, 14), datetime.datetime(2022, 10, 1, 15, 15)),
        Booking("Бах", datetime.datetime(2022, 10, 1, 14), datetime.datetime(2022, 10, 1, 15, 15)),
    ]
    key_error = [
        Booking("Превед Медвед", datetime.datetime(2022, 10, 1, 14), datetime.datetime(2022, 10, 1, 15, 15)),
    ]
    
    for b in bad:
        answer = {
            "created": False,
            "msg": "Комната занята",
            "booking": to_dict(b),
        }
        result = json.loads(create_booking(b.room_name, b.start, b.end))
        assert result == answer, f"Попытка создать бронь на занятое время. Верный ответ должен быть (выводим в виде словаря): {answer}, ваш: {result}"
        
        
    for b in good:
        answer = {
            "created": True,
            "msg": "Бронирование создано",
            "booking": to_dict(b),
        }
        result = json.loads(create_booking(b.room_name, b.start, b.end))
        assert result == answer, f"Попытка создать бронь на свободное время. Верный ответ должен быть (выводим в виде словаря): {answer}, ваш: {result}"
        
    for b in key_error:
        answer = {
            "created": False,
            "msg": "Комната не найдена",
            "booking": to_dict(b),
        }
        result = json.loads(create_booking(b.room_name, b.start, b.end))
        assert result == answer, f"Попытка создать бронь в несуществующей комнате. Верный ответ должен быть (выводим в виде словаря): {answer}, ваш: {result}"


test_booking()
test_create_booking()
