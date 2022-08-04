from utils.event_type import EventType


class Event:
    def __init__(self, event_datetime='', event_type=EventType.OTHER,
                 event_name='', event_members=None, event_place=''):
        if event_members is None:
            event_members = []
        self.event_datetime = event_datetime
        self.event_type = event_type
        self.event_name = event_name
        self.event_members = event_members
        self.event_place = event_place

    def __repr__(self):
        return f'{self.event_type} {self.event_place} {self.event_members} {self.event_datetime} {self.event_name}'

    def __str__(self):
        return f'From str {self.event_type} {self.event_place} {self.event_members} {self.event_datetime} {self.event_name}'
