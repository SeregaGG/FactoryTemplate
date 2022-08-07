import random

import pytest
from ObjectFactory.ObjectFactory import ObjectFactory
from Serializers.ObjectSerializer import ObjectSerializer
from ObjectsToGenerate.Event import Event


@pytest.fixture(scope='function', params=[('2020-02-20', '2020-03-20', 100, 'file_name1'), ('2020-04-20', '2020-06-20', 300, 'file_name2')])
def event_list_generator(request):
    og = ObjectFactory(request.param[0], request.param[1])
    events_count = request.param[2]
    event_list: list[Event] = og.generate_object_list(Event, events_count)
    return event_list, request.param[3]


@pytest.fixture(scope='function')
def event_list_serialize(event_list_generator):
    event_list, file_name = event_list_generator
    serializer = ObjectSerializer()
    serializer.serialize(event_list, file_name)
    return file_name


@pytest.fixture(scope='function')
def random_len():
    return random.randint(1, 10)
