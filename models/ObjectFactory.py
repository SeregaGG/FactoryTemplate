import random

from models.Event import Event
import datetime

from entitys.event_type import EventType
from services.generators import generate_random_word
from entitys.members_names import members


class ObjectFactory:
    def __init__(self, start: str, end: str):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        self._date_range = [start_date + datetime.timedelta(x) for x in
                            range((end_date - start_date).days + 1)]  # + 1 последний день

    def generate_object_list(self, object_type, events_count) -> list:
        object_generator = self._get_generator(object_type)
        return object_generator(self._date_range, events_count)

    @classmethod
    def _get_generator(cls, object_type):
        match object_type.__qualname__:
            case Event.__qualname__:
                return cls.event_generator
            case _:
                raise ValueError('Unknown type')

    @staticmethod
    def event_generator(data_range: list[datetime.datetime], events_count=4) -> list[Event]:
        event_list = []
        for i in range(0, events_count):
            tz = datetime.timezone(offset=datetime.timedelta(hours=0))

            event_body = {
                'event_datetime': (
                            random.choice(data_range) + datetime.timedelta(hours=random.randint(0, 24))).astimezone(tz),
                'event_type': random.choice(list(EventType)),
                'event_name': generate_random_word(100, 20),
                'event_members': [random.choice(members) for x in range(random.randint(2, 5))],
                # может быть несколько участников с одинаковым именем
                'event_place': generate_random_word(10)
            }
            current_event = Event(**event_body)
            event_list.append(current_event)
        return event_list
