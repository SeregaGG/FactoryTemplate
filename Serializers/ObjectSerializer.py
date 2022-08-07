from ObjectsToGenerate.Event import Event
from utils.event_type import EventType
from itertools import groupby
import json


class ObjectSerializer:

    def serialize(self, current_object, file_name):
        serializer = self._get_serializer(current_object[0])
        return serializer(current_object, file_name)

    @classmethod
    def _get_serializer(cls, current_object):
        match type(current_object).__qualname__:
            case Event.__qualname__:
                return cls.event_serializer
            case _:
                raise ValueError('Unknown type.')

    @staticmethod
    def event_serializer(event_list: list[Event], file_name):
        keyfunc = lambda x: x.event_datetime.strftime('%Y-%m-%d')
        event_list = sorted(event_list, key=keyfunc)
        event_body = {}

        for date, events in groupby(event_list, keyfunc):
            grouped_event_list: list[Event] = []
            for event in events:
                if event.event_type.value == EventType.OTHER.value:
                    continue
                grouped_event_list.append(event)
                serializable_grouped_event_list = [x.as_dict() for x in grouped_event_list]
                event_body.update({date: serializable_grouped_event_list})

        with open(f'{file_name}.json', 'w') as fp:
            json.dump(event_body, fp)
