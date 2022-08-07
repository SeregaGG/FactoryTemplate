import string
import random


def generate_random_word(max_len, segment_len=0):
    if not segment_len:
        segment_len = max_len
    symbols = string.ascii_letters + string.digits
    event_name = ''
    while len(event_name) < max_len:
        last_segment_len = max_len - len(event_name)
        if last_segment_len <= segment_len:
            event_name += ''.join(random.choice(symbols) for x in range(last_segment_len))
            break
        print(segment_len)
        current_segment_len = random.randint(1, segment_len)
        event_name += ''.join(random.choice(symbols) for x in range(current_segment_len)) + ' '
    return event_name

