from enum import Enum, auto


class EventType(Enum):
    def _generate_next_value_(self, start, count, last_values):
        return self

    PRIVATE = auto()
    MEETING = auto()
    CORPORATE = auto()
    OTHER = auto()
