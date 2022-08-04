import string
from ObjectsToGenerate.Event import Event
import datetime
import random
from utils.event_type import EventType
from utils.members_names import members


def event_generator(data_range: list[datetime.datetime], events_count=4) -> list[Event]:
    event_list = []
    for i in range(0, events_count):
        tz = datetime.timezone(offset=datetime.timedelta(hours=random.randint(-12, 14)))

        event_name = ''
        while len(event_name) < 100:
            last_segment_len = 100 - len(event_name)
            if last_segment_len <= 20:
                event_name += generate_random_word(last_segment_len)
                break
            segment_len = random.randint(1, 20)
            event_name += generate_random_word(segment_len) + ' '

        event_body = {
            'event_datetime': (random.choice(data_range) + datetime.timedelta(hours=random.randint(0, 24))).astimezone(tz),
            'event_type': random.choice(list(EventType)),
            'event_name': event_name,
            'event_members': [random.choice(members) for x in range(random.randint(2, 5))],
            # может быть несколько участников с одинаковым именем
            'event_place': generate_random_word(10)
        }
        current_event = Event(**event_body)
        event_list.append(current_event)
    return event_list


def generate_random_word(word_len):
    symbols = string.ascii_letters + string.digits
    return ''.join(random.choice(symbols) for x in range(word_len))
