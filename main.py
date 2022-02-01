import uuid
from datetime import datetime, timezone, timedelta
from icalendar import *


def cread_event(lesson_name, classroom, teacher, start, end):
    tz_utc_0 = timezone(timedelta(hours=0))
    # 创建事件/日程
    event = Event()
    event.add('summary', lesson_name)

    dt_now = datetime.now(tz=tz_utc_0)
    event.add('dtstart', start)
    event.add('dtend', end)
    # 创建时间
    event.add('dtstamp', dt_now)
    event.add('LOCATION', classroom)
    event.add('DESCRIPTION', '教师：' + teacher)

    # UID保证唯一
    event['uid'] = str(uuid.uuid1()) + '.cs.cf.ac.uk'

    return event


if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
