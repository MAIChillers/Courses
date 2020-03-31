import pandas as pd
import requests
from lxml import html

# pip3 install lxml

def get_schedule(group, func):
    for i in range(1, 19):
        get_schedule_weekend(group, i, func)


def get_schedule_weekend(group, weekend, func):
    url = "https://mai.ru/education/schedule/detail.php?group={}&week={}".format(group, weekend)
    html_text = requests.get(url).text
    with open("test.html", "w") as file:
        file.write(html_text)
    tree = html.fromstring(html_text)
    schedule_weekend = tree.xpath('//div[@class = "sc-table sc-table-day"]')
    for item_schedule in schedule_weekend:
        day = str(item_schedule.xpath('.//span[@class = "sc-day"]/text()')[0])
        schedule_weekend_detali = item_schedule.xpath(
            './/div[@class = "sc-table-col sc-table-detail-container"]')[0].xpath('..//div[@class = "sc-table-row"]')
        for item_detali in schedule_weekend_detali:
            time = str(item_detali.xpath(
                './/div[@class = "sc-table-col sc-item-time"]/text()')[0])
            type = str(item_detali.xpath(
                './/div[@class = "sc-table-col sc-item-type"]/text()')[0])
            title = str(item_detali.xpath(
                './/span[@class = "sc-title"]/text()')[0])
            auditory = str(item_detali.xpath(
                './/div[@class = "sc-table-col sc-item-location"]/text()')[0])
            try:
                lecturer = str(item_detali.xpath(
                    './/span[@class = "sc-lecturer"]/text()')[0])
            except IndexError:
                lecturer = " "

            lesson = type + ' ' + title + ' ' + auditory + ' ' + lecturer
            func(day, time, weekend, lesson)


def update_df(day, time, weekend, lesson):
    day_schedule_day = {
        'Пн': 'Понедельник',
        'Вт': 'Вторник',
        'Ср': 'Среда',
        'Чт': 'Четверг',
        'Пт': 'Пятница',
        'Сб': "Суббота"
    }
    time_lesson = {
        "09:00 – 10:30": '1-я пара',
        "10:45 – 12:15": '2-я пара',
        "13:00 – 14:30": '3-я пара',
        "14:45 – 16:15": '4-я пара',
        "16:30 – 18:00": '5-я пара',
        "18:15 – 19:45": '6-я пара'
    }
    if (lesson in df[day_schedule_day[day]][time_lesson[time]].keys()):
        df[day_schedule_day[day]][time_lesson[time]][lesson].append(weekend)
    else:
        df[day_schedule_day[day]][time_lesson[time]][lesson] = [weekend]


group = "М3О-201Б-18"
df = pd.DataFrame({
    'Понедельник': [{}, {}, {}, {}, {}, {}],
    'Вторник': [{}, {}, {}, {}, {}, {}],
    'Среда': [{}, {}, {}, {}, {}, {}],
    'Четверг': [{}, {}, {}, {}, {}, {}],
    'Пятница': [{}, {}, {}, {}, {}, {}],
    'Суббота': [{}, {}, {}, {}, {}, {}],
}, index=['1-я пара', '2-я пара', '3-я пара', '4-я пара', '5-я пара', '6-я пара'])

get_schedule(group, update_df)
print(df.to_csv())
