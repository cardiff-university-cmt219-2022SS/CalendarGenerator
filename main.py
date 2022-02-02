# -*- coding: utf-8 -*-
# @Organization     : Cardiff School of Computer Science and Informatics
# @Project          : iCalendarGenerator
# @Author           : YuChen Liu
# @StudentNumber    : 21096441
# @Email            : LiuY282@cardiff.ac.uk
# @Time             : 01/02/2022 13:29
# @Function:
import uuid
from datetime import datetime, timedelta, timezone
from icalendar import Calendar, Event
from dicts import time_dict, course_dict

tz_utc_0 = timezone(timedelta(hours=0))
tz_utc_1 = timezone(timedelta(hours=1))

begin_year = 2022
begin_month = 1
begin_day = 31


def createEvent(lesson_name, location, desc, start, end, tzz, freq=None, ):
    # 创建事件/日程
    event = Event()
    event.add('summary', lesson_name)

    dt_now = datetime.now(tz=tzz)
    event.add('dtstart', start)
    event.add('dtend', end)
    # 创建时间
    event.add('dtstamp', dt_now)
    event.add('LOCATION', location)
    event.add('DESCRIPTION', desc)

    # UID保证唯一
    event['uid'] = str(uuid.uuid1()) + '_timetable4optionalmodule@cardiff.ac.uk'
    if freq:
        event.add('rrule', freq)
    # event.add('priority', 5)
    return event


if __name__ == "__main__":
    cal = Calendar()
    cal.add('prodid', '-//JH-L//JH-L Calendar//')
    cal.add('version', '2.0')

    cls_lst = [
        # 分布式和云计算 ok
        {
            'name': course_dict.get('CMT202'),
            'desc': 'Type: Practical(online)\n\nModule code: CMT202\n\nStaff member(s): Padraig Corcoran\n\n'
                    'https://tinyurl.com/bdf242yb: https://tinyurl.com/bdf242yb'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[1],  # 开课时间
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13],  # 2-10周
            'day': [1]  # 周一、周三
        },
        {
            'name': course_dict.get('CMT202'),
            'desc': 'Type: Practical(online)\n\nModule code: CMT202\n\nStaff member(s): Padraig Corcoran\n\n'
                    'https://tinyurl.com/bdf242yb: https://tinyurl.com/bdf242yb'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[18],  # 开课时间
            'week': [14],  # 第几周
            'day': [2]  # 一周的第几天
        },
        {
            'name': course_dict.get('CMT202'),
            'desc': 'Type: Practical(online)\n\nModule code: CMT202\n\nStaff member(s): Padraig Corcoran\n\n'
                    'Optional Online drop-in session\n\n'
                    'https://tinyurl.com/2sb8dwak: https://tinyurl.com/2sb8dwak'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[9],  # 开课时间
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13],  # 2-10周
            'day': [1]  # 周一、周三
        },
        # 数据库和建模 ok
        {
            'name': course_dict.get('CMT220'),
            'desc': 'Type: Seminar(online)\n\nModule code: CMT220\n\nStaff member(s): Irena Spasic'
                    '\n\nJoin Zoom meeting: https://cardiff.zoom.us/j/89016515833?pwd=dnZCOWw0NDgrNkdmc2pqaUFYOUNqdz09'
                    '\nMeeting ID: 890 1651 5833'
                    '\nPassword: 782362'
                    '\n\ntips：需要使用学校的zoom账号登录，否则没有权限进入会议。'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[11],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13],
            'day': [2]
        },
        {
            'name': course_dict.get('CMT220'),
            'desc': 'Type: Seminar(online)\n\nModule code: CMT220\n\nStaff member(s): Irena Spasic'
                    '\n\nJoin Zoom meeting: https://cardiff.zoom.us/j/89016515833?pwd=dnZCOWw0NDgrNkdmc2pqaUFYOUNqdz09'
                    '\nMeeting ID: 890 1651 5833'
                    '\nPassword: 782362'
                    '\n\ntips：需要使用学校的zoom账号登录，否则没有权限进入会议。'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[13],
            'week': [14],
            'day': [2]
        },
        # 数据可视化(group1 & group2) ok
        {
            'name': course_dict.get('CMT218'),
            'desc': 'Type: Seminar\n\nModule code:CMT218\n\nStaff member(s): Martin Chorley\n\nGroup 1\n\n'
                    'https://cardiff.zoom.us/j/86959746329?pwd=SFdzVnZOc2RzRmhBa3ZJZ3ZvVVdmQT09: https://cardiff.zoom.us/j/86959746329?pwd=SFdzVnZOc2RzRmhBa3ZJZ3ZvVVdmQT09'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': 'South/S/3.20',
            'time': time_dict[2],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13],
            'day': [2]
        },
        {
            'name': course_dict.get('CMT218'),
            'desc': 'Type: Seminar\n\nModule code:CMT218\n\nStaff member(s): Martin Chorley\n\nGroup 2\n\n'
                    'https://cardiff.zoom.us/j/86959746329?pwd=SFdzVnZOc2RzRmhBa3ZJZ3ZvVVdmQT09: https://cardiff.zoom.us/j/86959746329?pwd=SFdzVnZOc2RzRmhBa3ZJZ3ZvVVdmQT09'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': 'South/S/3.20',
            'time': time_dict[7],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13],
            'day': [2]
        },
        {
            'name': course_dict.get('CMT218'),
            'desc': 'Type: Practical (Online)\n\nModule code:CMT218\n\nStaff member(s): Martin Chorley\n\n'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[1],
            'week': [14],
            'day': [2]
        },
        # 人机交互 ok
        {  # 前三周周二课：线上
            'name': course_dict.get('CMT206'),
            'desc': 'Type: Seminar (Online)\n\nModule code:CMT206\n\nStaff member(s): Alia Abdelmoty\n\n'
                    ''
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[5],
            'week': [1, 2, 3],
            'day': [2]
        },
        {  # 第四周开始周二课：线下(S/2.22)
            'name': course_dict.get('CMT206'),
            'desc': 'Type: Seminar\n\nModule code:CMT206\n\nStaff member(s): Alia Abdelmoty\n\n'
                    ''
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': 'South/S/2.22',
            'time': time_dict[15],
            'week': [4, 5, 6, 8, 9],
            'day': [2]
        },
        {  # 周四的课从第二周开始上，可选的
            'name': course_dict.get('CMT206'),
            'desc': 'Type: Practical (Online)\n\nModule code:CMT206\n\nStaff member(s): Alia Abdelmoty\n\n'
                    'Optional drop in session'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[14],
            'week': [2, 3, 4, 5],
            'day': [4]
        },
        # 数据结构与算法 ok
        {  # 不同讲师
            'name': course_dict.get('CMT219'),
            'desc': 'Type: Practical\n\nModule code: CMT219\n\nStaff member(s): Matthew Morgan'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': 'South/S/3.20',
            'time': time_dict[4],
            'week': [1, 2, 3],
            'day': [4]
        },
        {  # 不同讲师
            'name': course_dict.get('CMT219'),
            'desc': 'Type: Practical\n\nModule code: CMT219\n\nStaff member(s): Daniela Tsaneva'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': 'South/S/3.20',
            'time': time_dict[16],
            'week': [4, 5, 13, 14],
            'day': [4]
        },
        {  # 不同讲师
            'name': course_dict.get('CMT219'),
            'desc': 'Type: Practical (online)\n\nModule code: CMT219\n\nStaff member(s): Neetesh Saxena'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[17],
            'week': [6, 8, 9],
            'day': [4]
        },
        # Topics, Research and Skills ok
        {
            'name': course_dict.get('CMT222'),
            'desc': 'Type: Seminar (online)\n\nModule code: CMT222\n\nStaff member(s): Martin Chorley'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[10],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13, 14],
            'day': [4]
        },
        {
            'name': course_dict.get('CMT221'),
            'desc': 'Type: Seminar (online)\n\nModule code: CMT221\n\nStaff member(s): Martin Chorley'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[10],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13, 14],
            'day': [4]
        },
        # CMT313 ok
        {
            'name': course_dict.get('CMT313'),
            'desc': 'Type: Self Study\n\nModule code: CMT313\n\nStaff member(s): Phillips, Helen'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': 'South/S/3.20',
            'time': time_dict[8],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13, 14],
            'day': [3]
        },
        {
            'name': course_dict.get('CMT313'),
            'desc': 'Type: Workshop(online)\n\nModule code: CMT313\n\nStaff member(s): Daniela Tsaneva, Matthew Moloughney, Phillips, Helen'
                    '\n\nhttps://tinyurl.com/2p89f2ad: https://tinyurl.com/2p89f2ad'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[3],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13, 14],
            'day': [5]
        },
        # CMT312 ok
        {
            'name': course_dict.get('CMT312'),
            'desc': 'Type: Self Study\n\nModule code: CMT312'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': 'South/S/3.20',
            'time': time_dict[6],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13, 14],
            'day': [3]
        },
        {
            'name': course_dict.get('CMT312'),
            'desc': 'Type: Workshop(online)\n\nModule code: CMT312\n\nStaff member(s): Catherine Teehan, Natalia Edwards, Phillips, Helen, Wendy Ivins'
                    '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
            'location': '',
            'time': time_dict[3],
            'week': [1, 2, 3, 4, 5, 6, 8, 9, 13, 14],
            'day': [5]
        },
        # CMT224 社交计算
        {
            'name': course_dict.get('CMT224'),
            'desc': 'Type: Workshop\n\nModule code: CMT224\n\nStaff member(s): Liam Turner'
                    '\n\nLast synchronised on 2022-02-02 at 21:25 GMT',
            'location': 'South/S/2.22',
            'time': time_dict[2],
            'week': [1, 2, 3, 4, 5, 8, 9, 13, 14],
            'day': [3]
        },
        {
            'name': course_dict.get('CMT224'),
            'desc': 'Type: Workshop(online)\n\nModule code: CMT224\n\nStaff member(s): Liam Turner'
                    '\n\nLast synchronised on 2022-02-02 at 21:25 GMT',
            'location': 'South/S/2.22',
            'time': time_dict[1],
            'week': [6],
            'day': [3]
        },
        ###########################
        # {
        #     'name': course_dict.get('CMT219'),
        #     'desc': 'Type: \n\nModule code: \n\nStaff member(s): '
        #             '\n\nLast synchronised on 2022-02-01 at 14:06 GMT',
        #     'location': '',
        #     'time': time_dict[5],
        #     'week': [],
        #     'day': [4]
        # },
    ]

    begin_date = datetime(begin_year, begin_month, begin_day)
    for lesson in cls_lst:
        # 课程开始时间(s1小时，s2分钟)，课程结束时间(e1小时，e2分钟)
        # name, teacher, room = f'{lesson["name"]}-{lesson["room"]}', lesson['teacher'], lesson['room']
        name, desc, location = lesson['name'], lesson['desc'], lesson['location']
        s1, s2 = lesson['time'][0]
        e1, e2 = lesson['time'][-1]
        for week in lesson['week']:
            # 第N周
            week_delta = timedelta(days=(week - 1) * 7)
            for day in lesson['day']:
                # 周N
                day_delta = timedelta(days=(day - 1))
                new_date = begin_date + week_delta + day_delta
                # 上课的年月日
                new_year, new_month, new_day = new_date.year, new_date.month, new_date.day
                ymd = [new_year, new_month, new_day]
                # 课程开始时间和结束时间
                if week < 9:
                    start = datetime(*ymd, s1, s2, tzinfo=tz_utc_0)
                    end = datetime(*ymd, e1, e2, tzinfo=tz_utc_0)
                    cal.add_component(createEvent(name, location, desc, start, end, tz_utc_0))
                else:
                    start = datetime(*ymd, s1, s2, tzinfo=tz_utc_1)
                    end = datetime(*ymd, e1, e2, tzinfo=tz_utc_1)
                    cal.add_component(createEvent(name, location, desc, start, end, tz_utc_1))

    with open('OptionalModules.ics', 'wb') as f:
        f.write(cal.to_ical())
