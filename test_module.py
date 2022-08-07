# content of test_module.py
import datetime
import json
from utils.event_type import EventType

from utils.generators import generate_random_word


def test_word_generator(random_len):
    test_word = generate_random_word(random_len)
    assert len(test_word) == random_len


def test_events_struct(event_list_serialize):
    with open(f'{event_list_serialize}.json', 'r') as fp:
        data = json.load(fp)
        for date_key, event_list in data.items():
            for event in event_list:
                assert 'event_datetime' in event
                assert 'event_type' in event
                assert 'event_name' in event
                assert 'event_members' in event
                assert 'event_place' in event
                assert event.get('event_type') != EventType.OTHER.value


def test_events_valid_data(event_list_generator):
    for event in event_list_generator[0]:
        assert len(event.event_name) <= 100
        list_event_name = event.event_name.split(' ')
        assert len(max(list_event_name, key=lambda x: len(x))) <= 20
