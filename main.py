from ObjectFactory.ObjectFactory import ObjectFactory
from Serializers.ObjectSerializer import ObjectSerializer
from ObjectsToGenerate.Event import Event
import argparse


def command_line_init():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start_date', help='Start of period')
    parser.add_argument('--end_date', help='End of period')
    parser.add_argument('--file_name', help='Name for output json file with objects grouped by dates')
    args = parser.parse_args()
    start_date = '2020-02-20'
    end_date = '2020-03-20'
    file_name = 'default'
    if args.start_date and args.end_date:
        start_date = args.start_date
        end_date = args.end_date
    if args.file_name:
        file_name = args.file_name

    return start_date, end_date, file_name


if __name__ == '__main__':
    start_date, end_date, file_name = command_line_init()
    og = ObjectFactory(start_date, end_date)
    event_list: list[Event] = og.generate_object_list(Event, 4)
    serializer = ObjectSerializer()
    serializer.serialize(event_list, file_name)
