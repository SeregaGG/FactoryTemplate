import random

import pytest
from ObjectFactory.ObjectFactory import ObjectFactory
from Serializers.ObjectSerializer import ObjectSerializer
from ObjectsToGenerate.Event import Event


@pytest.fixture(scope='function')
def event_list_generator():
    start_date = '2020-02-20'
    end_date = '2020-03-20'
    og = ObjectFactory(start_date, end_date)
    events_count = 40
    event_list: list[Event] = og.generate_object_list(Event, events_count)
    return event_list


@pytest.fixture(scope='function')
def event_list_serialize(event_list_generator):
    file_name = 'default'
    serializer = ObjectSerializer()
    serializer.serialize(event_list_generator, file_name)
    return file_name


@pytest.fixture(scope='function')
def random_len():
    return random.randint(1, 10)
