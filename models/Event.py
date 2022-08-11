import datetime

from entitys.event_type import EventType


class Event:
    def __init__(self, event_datetime=datetime.datetime.now(), event_type=EventType.OTHER,
                 event_name='', event_members=None, event_place=''):
        if event_members is None:
            event_members = []
        self._event_datetime: datetime.datetime = event_datetime
        self._event_type = event_type
        self._event_name = event_name
        self._event_members = event_members
        self._event_place = event_place

    def __repr__(self):
        return f'{self._event_type} {self._event_place} {self._event_members} {self._event_datetime} {self._event_name}'

    def __str__(self):
        return f'From str {self._event_type} {self._event_place} {self._event_members} {self._event_datetime} {self._event_name}'

    def as_dict(self):
        event_dict = {
            'event_datetime': self._event_datetime.strftime('%Y-%m-%d %H:%M:%S'),
            'event_type': self._event_type.value,
            'event_name': self._event_name,
            'event_members': self._event_members,
            'event_place': self._event_place
        }
        return event_dict

    @property
    def event_datetime(self):
        return self._event_datetime

    @property
    def event_type(self):
        return self._event_type

    @property
    def event_name(self):
        return self._event_name

    @property
    def event_members(self):
        return self._event_members

    @property
    def event_place(self):
        return self._event_place
