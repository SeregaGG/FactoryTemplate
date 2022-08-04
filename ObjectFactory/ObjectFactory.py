from ObjectsToGenerate.Event import Event
import datetime
from utils.generators import event_generator


class ObjectFactory:
    def __init__(self, start: str, end: str):
        start_date = datetime.datetime.strptime(start, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end, '%Y-%m-%d')
        self.date_range = [start_date + datetime.timedelta(x) for x in
                           range((end_date - start_date).days + 1)]  # + 1 последний день

    def generate_object_list(self, object_type, events_count) -> list:
        object_generator = self._get_generator(object_type)
        return object_generator(self.date_range, events_count)

    def _get_generator(self, object_type):
        match object_type.__qualname__:
            case Event.__qualname__:
                return event_generator
            case _:
                raise ValueError('Unknown type')
