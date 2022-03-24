from turtle import left
from flask import render_template, session, redirect, url_for
from . import bp

import requests
import time
from datetime import datetime, timedelta

@bp.route("/")
def index():
    req = requests.get(
        "https://api.netpie.io/v2/device/shadow/data",
        auth=(
            "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm",
        ),
    )
    req = req.json()
    left_medicine = req["data"]["left"]
    right_medicine = req["data"]["right"]
    
    
    name = dict(session).get('profile')
    if not name:
        return redirect(url_for("account.home"))
    name = dict(session)["profile"]["name"]
    picture = dict(session)['profile']['picture']

    # -----------------------------------------------------------------------------------------------------------------
    dayMonthYear=0
    left_morning=0
    right_morning=0
    recentTime_morning=0
    left_noon=0
    right_noon=0
    recentTime_noon=0
    left_evening=0
    right_evening=0
    recentTime_evening=0
    left_bedtime=0
    right_bedtime=0
    recentTime_bedtime=0

    dayMonthYear1=0
    left_morning_yesterday1=0
    right_morning_yesterday1=0
    recentTime_morning_yesterday1=0
    left_noon_yesterday1=0
    right_noon_yesterday1=0
    recentTime_noon_yesterday1=0
    left_evening_yesterday1=0
    right_evening_yesterday1=0
    recentTime_evening_yesterday1=0
    left_bedtime_yesterday1=0
    right_bedtime_yesterday1=0
    recentTime_bedtime_yesterday1=0

    dayMonthYear2=0
    left_morning_yesterday2=0
    right_morning_yesterday2=0
    recentTime_morning_yesterday2=0
    left_noon_yesterday2=0
    right_noon_yesterday2=0
    recentTime_noon_yesterday2=0
    left_evening_yesterday2=0
    right_evening_yesterday2=0
    recentTime_evening_yesterday2=0
    left_bedtime_yesterday2=0
    right_bedtime_yesterday2=0
    recentTime_bedtime_yesterday2=0

    dayMonthYear3=0
    left_morning_yesterday3=0
    right_morning_yesterday3=0
    recentTime_morning_yesterday3=0
    left_noon_yesterday3=0
    right_noon_yesterday3=0
    recentTime_noon_yesterday3=0
    left_evening_yesterday3=0
    right_evening_yesterday3=0
    recentTime_evening_yesterday3=0
    left_bedtime_yesterday3=0
    right_bedtime_yesterday3=0
    recentTime_bedtime_yesterday3=0

    dayMonthYear4=0
    left_morning_yesterday4=0
    right_morning_yesterday4=0
    recentTime_morning_yesterday4=0
    left_noon_yesterday4=0
    right_noon_yesterday4=0
    recentTime_noon_yesterday4=0
    left_evening_yesterday4=0
    right_evening_yesterday4=0
    recentTime_evening_yesterday4=0
    left_bedtime_yesterday4=0
    right_bedtime_yesterday4=0
    recentTime_bedtime_yesterday4=0

    dayMonthYear5=0
    left_morning_yesterday5=0
    right_morning_yesterday5=0
    recentTime_morning_yesterday5=0
    left_noon_yesterday5=0
    right_noon_yesterday5=0
    recentTime_noon_yesterday5=0
    left_evening_yesterday5=0
    right_evening_yesterday5=0
    recentTime_evening_yesterday5=0
    left_bedtime_yesterday5=0
    right_bedtime_yesterday5=0
    recentTime_bedtime_yesterday5=0

    dayMonthYear6=0
    left_morning_yesterday6=0
    right_morning_yesterday6=0
    recentTime_morning_yesterday6=0
    left_noon_yesterday6=0
    right_noon_yesterday6=0
    recentTime_noon_yesterday6=0
    left_evening_yesterday6=0
    right_evening_yesterday6=0
    recentTime_evening_yesterday6=0
    left_bedtime_yesterday6=0
    right_bedtime_yesterday6=0
    recentTime_bedtime_yesterday6=0

    dayMonthYear7=0
    left_morning_yesterday7=0
    right_morning_yesterday7=0
    recentTime_morning_yesterday7=0
    left_noon_yesterday7=0
    right_noon_yesterday7=0
    recentTime_noon_yesterday7=0
    left_evening_yesterday7=0
    right_evening_yesterday7=0
    recentTime_evening_yesterday7=0
    left_bedtime_yesterday7=0
    right_bedtime_yesterday7=0
    recentTime_bedtime_yesterday7=0
    # -----------------------------------------------------------------------------------------------------------------

    start1 = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0)
    unixtime_start1 = time.mktime(start1.timetuple()) * 1000
    stop1 = datetime.now().replace(hour=10,minute=59,second=59,microsecond=0)
    unixtime_stop1 = time.mktime(stop1.timetuple()) * 1000

    start2 = datetime.now().replace(hour=11,minute=0,second=0,microsecond=0)
    unixtime_start2 = time.mktime(start2.timetuple()) * 1000
    stop2 = datetime.now().replace(hour=14,minute=59,second=59,microsecond=0)
    unixtime_stop2 = time.mktime(stop2.timetuple()) * 1000

    start3 = datetime.now().replace(hour=15,minute=0,second=0,microsecond=0)
    unixtime_start3 = time.mktime(start3.timetuple()) * 1000
    stop3 = datetime.now().replace(hour=18,minute=59,second=59,microsecond=0)
    unixtime_stop3 = time.mktime(stop3.timetuple()) * 1000

    start4 = datetime.now().replace(hour=19,minute=0,second=0,microsecond=0)
    unixtime_start4 = time.mktime(start4.timetuple()) * 1000
    stop4 = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0)
    unixtime_stop4 = time.mktime(stop4.timetuple()) * 1000

    res1 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start1,
        "end_absolute": unixtime_stop1,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res2 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start2,
        "end_absolute": unixtime_stop2,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res3 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start3,
        "end_absolute": unixtime_stop3,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res4 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start4,
        "end_absolute": unixtime_stop4,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })

    #aggregator first last avg sum
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    res4 = res4.json()

    dayMonthYear = datetime.utcfromtimestamp(unixtime_start1/1000 + 25200).strftime('วันที่: %d/%m/%y')

    try:
        right_morning = res1["queries"][0]['results'][0]['values'][-1][1]
        right_morning = res1["queries"][0]['results'][1]['values'][-1][1]
        recentTime_morning = res1["queries"][0]['results'][0]['values'][-1][0]
        recentTime_morning = datetime.utcfromtimestamp(recentTime_morning/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_morning = '-'
        right_morning = '-'
        recentTime_morning = 'เวลา: ไม่มีข้อมูล'

    try:
        left_noon = res2["queries"][0]['results'][0]['values'][-1][1]
        right_noon = res2["queries"][0]['results'][1]['values'][-1][1]
        recentTime_noon = res2["queries"][0]['results'][0]['values'][-1][0]
        recentTime_noon = datetime.utcfromtimestamp(recentTime_noon/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_noon = '-'
        right_noon = '-'
        recentTime_noon = 'เวลา: ไม่มีข้อมูล'

    try:
        left_evening = res3["queries"][0]['results'][0]['values'][-1][1]
        right_evening = res3["queries"][0]['results'][1]['values'][-1][1]
        recentTime_evening = res3["queries"][0]['results'][0]['values'][-1][0]
        recentTime_evening = datetime.utcfromtimestamp(recentTime_evening/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_evening = '-'
        right_evening = '-'
        recentTime_evening = 'เวลา: ไม่มีข้อมูล'
 
    try:
        left_bedtime = res4["queries"][0]['results'][0]['values'][-1][1]
        right_bedtime = res4["queries"][0]['results'][1]['values'][-1][1]
        recentTime_bedtime = res4["queries"][0]['results'][0]['values'][-1][0]
        recentTime_bedtime = datetime.utcfromtimestamp(recentTime_bedtime/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_bedtime = '-'
        right_bedtime = '-'
        recentTime_bedtime = 'เวลา: ไม่มีข้อมูล'

    # -----------------------------------------------------------------------------------------------------------------

    yesterday_start1 = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0) - timedelta(days=1)
    unixtime_start1 = time.mktime(yesterday_start1.timetuple()) * 1000
    yesterday_stop1 = datetime.now().replace(hour=10,minute=59,second=59,microsecond=0) - timedelta(days=1)
    unixtime_stop1 = time.mktime(yesterday_stop1.timetuple()) * 1000

    yesterday_start2 = datetime.now().replace(hour=11,minute=0,second=0,microsecond=0) - timedelta(days=1)
    unixtime_start2 = time.mktime(yesterday_start2.timetuple()) * 1000
    yesterday_stop2 = datetime.now().replace(hour=14,minute=59,second=59,microsecond=0) - timedelta(days=1)
    unixtime_stop2 = time.mktime(yesterday_stop2.timetuple()) * 1000

    yesterday_start3 = datetime.now().replace(hour=15,minute=0,second=0,microsecond=0) - timedelta(days=1)
    unixtime_start3 = time.mktime(yesterday_start3.timetuple()) * 1000
    yesterday_stop3 = datetime.now().replace(hour=18,minute=59,second=59,microsecond=0) - timedelta(days=1)
    unixtime_stop3 = time.mktime(yesterday_stop3.timetuple()) * 1000

    yesterday_start4 = datetime.now().replace(hour=19,minute=0,second=0,microsecond=0) - timedelta(days=1)
    unixtime_start4 = time.mktime(yesterday_start4.timetuple()) * 1000
    yesterday_stop4 = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=1)
    unixtime_stop4 = time.mktime(yesterday_stop4.timetuple()) * 1000

    res1 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start1,
        "end_absolute": unixtime_stop1,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res2 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start2,
        "end_absolute": unixtime_stop2,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res3 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start3,
        "end_absolute": unixtime_stop3,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res4 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start4,
        "end_absolute": unixtime_stop4,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })

    #aggregator first last avg sum
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    res4 = res4.json()

    dayMonthYear1 = datetime.utcfromtimestamp(unixtime_start1/1000 + 25200).strftime('วันที่: %d/%m/%y')

    try:
        left_morning_yesterday1 = res1["queries"][0]['results'][0]['values'][-1][1]
        right_morning_yesterday1 = res1["queries"][0]['results'][1]['values'][-1][1]
        recentTime_morning_yesterday1 = res1["queries"][0]['results'][0]['values'][-1][0]
        recentTime_morning_yesterday1 = datetime.utcfromtimestamp(recentTime_morning_yesterday1/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_morning_yesterday1 = '-'
        right_morning_yesterday1 = '-'
        recentTime_morning_yesterday1 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_noon_yesterday1 = res2["queries"][0]['results'][0]['values'][-1][1]
        right_noon_yesterday1 = res2["queries"][0]['results'][1]['values'][-1][1]
        recentTime_noon_yesterday1 = res2["queries"][0]['results'][0]['values'][-1][0]
        recentTime_noon_yesterday1 = datetime.utcfromtimestamp(recentTime_noon_yesterday1/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_noon_yesterday1 = '-'
        right_noon_yesterday1 = '-'
        recentTime_noon_yesterday1 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_evening_yesterday1 = res3["queries"][0]['results'][0]['values'][-1][1]
        right_evening_yesterday1 = res3["queries"][0]['results'][1]['values'][-1][1]
        recentTime_evening_yesterday1 = res3["queries"][0]['results'][0]['values'][-1][0]
        recentTime_evening_yesterday1 = datetime.utcfromtimestamp(recentTime_evening_yesterday1/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_evening_yesterday1 = '-'
        right_evening_yesterday1 = '-'
        recentTime_evening_yesterday1 = 'เวลา: ไม่มีข้อมูล'
 
    try:
        left_bedtime_yesterday1 = res4["queries"][0]['results'][0]['values'][-1][1]
        right_bedtime_yesterday1 = res4["queries"][0]['results'][1]['values'][-1][1]
        recentTime_bedtime_yesterday1 = res4["queries"][0]['results'][0]['values'][-1][0]
        recentTime_bedtime_yesterday1 = datetime.utcfromtimestamp(recentTime_bedtime_yesterday1/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_bedtime_yesterday1 = '-'
        right_bedtime_yesterday1 = '-'
        recentTime_bedtime_yesterday1 = 'เวลา: ไม่มีข้อมูล'

    # -----------------------------------------------------------------------------------------------------------------

    yesterday_start1 = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0) - timedelta(days=2)
    unixtime_start1 = time.mktime(yesterday_start1.timetuple()) * 1000
    yesterday_stop1 = datetime.now().replace(hour=10,minute=59,second=59,microsecond=0) - timedelta(days=2)
    unixtime_stop1 = time.mktime(yesterday_stop1.timetuple()) * 1000

    yesterday_start2 = datetime.now().replace(hour=11,minute=0,second=0,microsecond=0) - timedelta(days=2)
    unixtime_start2 = time.mktime(yesterday_start2.timetuple()) * 1000
    yesterday_stop2 = datetime.now().replace(hour=14,minute=59,second=59,microsecond=0) - timedelta(days=2)
    unixtime_stop2 = time.mktime(yesterday_stop2.timetuple()) * 1000

    yesterday_start3 = datetime.now().replace(hour=15,minute=0,second=0,microsecond=0) - timedelta(days=2)
    unixtime_start3 = time.mktime(yesterday_start3.timetuple()) * 1000
    yesterday_stop3 = datetime.now().replace(hour=18,minute=59,second=59,microsecond=0) - timedelta(days=2)
    unixtime_stop3 = time.mktime(yesterday_stop3.timetuple()) * 1000

    yesterday_start4 = datetime.now().replace(hour=19,minute=0,second=0,microsecond=0) - timedelta(days=2)
    unixtime_start4 = time.mktime(yesterday_start4.timetuple()) * 1000
    yesterday_stop4 = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=2)
    unixtime_stop4 = time.mktime(yesterday_stop4.timetuple()) * 1000

    res1 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start1,
        "end_absolute": unixtime_stop1,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res2 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start2,
        "end_absolute": unixtime_stop2,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res3 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start3,
        "end_absolute": unixtime_stop3,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res4 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start4,
        "end_absolute": unixtime_stop4,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })

    #aggregator first last avg sum
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    res4 = res4.json()

    dayMonthYear2 = datetime.utcfromtimestamp(unixtime_start1/1000 + 25200).strftime('วันที่: %d/%m/%y')

    try:
        left_morning_yesterday2 = res1["queries"][0]['results'][0]['values'][-1][1]
        right_morning_yesterday2 = res1["queries"][0]['results'][1]['values'][-1][1]
        recentTime_morning_yesterday2 = res1["queries"][0]['results'][0]['values'][-1][0]
        recentTime_morning_yesterday2 = datetime.utcfromtimestamp(recentTime_morning_yesterday2/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_morning_yesterday2 = '-'
        right_morning_yesterday2 = '-'
        recentTime_morning_yesterday2 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_noon_yesterday2 = res2["queries"][0]['results'][0]['values'][-1][1]
        right_noon_yesterday2 = res2["queries"][0]['results'][1]['values'][-1][1]
        recentTime_noon_yesterday2 = res2["queries"][0]['results'][0]['values'][-1][0]
        recentTime_noon_yesterday2 = datetime.utcfromtimestamp(recentTime_noon_yesterday2/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_noon_yesterday2 = '-'
        right_noon_yesterday2 = '-'
        recentTime_noon_yesterday2 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_evening_yesterday2 = res3["queries"][0]['results'][0]['values'][-1][1]
        right_evening_yesterday2 = res3["queries"][0]['results'][1]['values'][-1][1]
        recentTime_evening_yesterday2 = res3["queries"][0]['results'][0]['values'][-1][0]
        recentTime_evening_yesterday2 = datetime.utcfromtimestamp(recentTime_evening_yesterday2/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_evening_yesterday2 = '-'
        right_evening_yesterday2 = '-'
        recentTime_evening_yesterday2 = 'เวลา: ไม่มีข้อมูล'
 
    try:
        left_bedtime_yesterday2 = res4["queries"][0]['results'][0]['values'][-1][1]
        right_bedtime_yesterday2 = res4["queries"][0]['results'][1]['values'][-1][1]
        recentTime_bedtime_yesterday2 = res4["queries"][0]['results'][0]['values'][-1][0]
        recentTime_bedtime_yesterday2 = datetime.utcfromtimestamp(recentTime_bedtime_yesterday2/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_bedtime_yesterday2 = '-'
        right_bedtime_yesterday2 = '-'
        recentTime_bedtime_yesterday2 = 'เวลา: ไม่มีข้อมูล'

    # -----------------------------------------------------------------------------------------------------------------

    yesterday_start1 = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0) - timedelta(days=3)
    unixtime_start1 = time.mktime(yesterday_start1.timetuple()) * 1000
    yesterday_stop1 = datetime.now().replace(hour=10,minute=59,second=59,microsecond=0) - timedelta(days=3)
    unixtime_stop1 = time.mktime(yesterday_stop1.timetuple()) * 1000

    yesterday_start2 = datetime.now().replace(hour=11,minute=0,second=0,microsecond=0) - timedelta(days=3)
    unixtime_start2 = time.mktime(yesterday_start2.timetuple()) * 1000
    yesterday_stop2 = datetime.now().replace(hour=14,minute=59,second=59,microsecond=0) - timedelta(days=3)
    unixtime_stop2 = time.mktime(yesterday_stop2.timetuple()) * 1000

    yesterday_start3 = datetime.now().replace(hour=15,minute=0,second=0,microsecond=0) - timedelta(days=3)
    unixtime_start3 = time.mktime(yesterday_start3.timetuple()) * 1000
    yesterday_stop3 = datetime.now().replace(hour=18,minute=59,second=59,microsecond=0) - timedelta(days=3)
    unixtime_stop3 = time.mktime(yesterday_stop3.timetuple()) * 1000

    yesterday_start4 = datetime.now().replace(hour=19,minute=0,second=0,microsecond=0) - timedelta(days=3)
    unixtime_start4 = time.mktime(yesterday_start4.timetuple()) * 1000
    yesterday_stop4 = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=3)
    unixtime_stop4 = time.mktime(yesterday_stop4.timetuple()) * 1000

    res1 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start1,
        "end_absolute": unixtime_stop1,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res2 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start2,
        "end_absolute": unixtime_stop2,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res3 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start3,
        "end_absolute": unixtime_stop3,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res4 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start4,
        "end_absolute": unixtime_stop4,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })

    #aggregator first last avg sum
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    res4 = res4.json()

    dayMonthYear3 = datetime.utcfromtimestamp(unixtime_start1/1000 + 25200).strftime('วันที่: %d/%m/%y')

    try:
        left_morning_yesterday3 = res1["queries"][0]['results'][0]['values'][-1][1]
        right_morning_yesterday3 = res1["queries"][0]['results'][1]['values'][-1][1]
        recentTime_morning_yesterday3 = res1["queries"][0]['results'][0]['values'][-1][0]
        recentTime_morning_yesterday3 = datetime.utcfromtimestamp(recentTime_morning_yesterday3/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_morning_yesterday3 = '-'
        right_morning_yesterday3 = '-'
        recentTime_morning_yesterday3 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_noon_yesterday3 = res2["queries"][0]['results'][0]['values'][-1][1]
        right_noon_yesterday3 = res2["queries"][0]['results'][1]['values'][-1][1]
        recentTime_noon_yesterday3 = res2["queries"][0]['results'][0]['values'][-1][0]
        recentTime_noon_yesterday3 = datetime.utcfromtimestamp(recentTime_noon_yesterday3/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_noon_yesterday3 = '-'
        right_noon_yesterday3 = '-'
        recentTime_noon_yesterday3 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_evening_yesterday3 = res3["queries"][0]['results'][0]['values'][-1][1]
        right_evening_yesterday3 = res3["queries"][0]['results'][1]['values'][-1][1]
        recentTime_evening_yesterday3 = res3["queries"][0]['results'][0]['values'][-1][0]
        recentTime_evening_yesterday3 = datetime.utcfromtimestamp(recentTime_evening_yesterday3/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_evening_yesterday3 = '-'
        right_evening_yesterday3 = '-'
        recentTime_evening_yesterday3 = 'เวลา: ไม่มีข้อมูล'
 
    try:
        left_bedtime_yesterday3 = res4["queries"][0]['results'][0]['values'][-1][1]
        right_bedtime_yesterday3 = res4["queries"][0]['results'][1]['values'][-1][1]
        recentTime_bedtime_yesterday3 = res4["queries"][0]['results'][0]['values'][-1][0]
        recentTime_bedtime_yesterday3 = datetime.utcfromtimestamp(recentTime_bedtime_yesterday3/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_bedtime_yesterday3 = '-'
        right_bedtime_yesterday3 = '-'
        recentTime_bedtime_yesterday3 = 'เวลา: ไม่มีข้อมูล'

    # -----------------------------------------------------------------------------------------------------------------

    yesterday_start1 = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0) - timedelta(days=4)
    unixtime_start1 = time.mktime(yesterday_start1.timetuple()) * 1000
    yesterday_stop1 = datetime.now().replace(hour=10,minute=59,second=59,microsecond=0) - timedelta(days=4)
    unixtime_stop1 = time.mktime(yesterday_stop1.timetuple()) * 1000

    yesterday_start2 = datetime.now().replace(hour=11,minute=0,second=0,microsecond=0) - timedelta(days=4)
    unixtime_start2 = time.mktime(yesterday_start2.timetuple()) * 1000
    yesterday_stop2 = datetime.now().replace(hour=14,minute=59,second=59,microsecond=0) - timedelta(days=4)
    unixtime_stop2 = time.mktime(yesterday_stop2.timetuple()) * 1000

    yesterday_start3 = datetime.now().replace(hour=15,minute=0,second=0,microsecond=0) - timedelta(days=4)
    unixtime_start3 = time.mktime(yesterday_start3.timetuple()) * 1000
    yesterday_stop3 = datetime.now().replace(hour=18,minute=59,second=59,microsecond=0) - timedelta(days=4)
    unixtime_stop3 = time.mktime(yesterday_stop3.timetuple()) * 1000

    yesterday_start4 = datetime.now().replace(hour=19,minute=0,second=0,microsecond=0) - timedelta(days=4)
    unixtime_start4 = time.mktime(yesterday_start4.timetuple()) * 1000
    yesterday_stop4 = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=4)
    unixtime_stop4 = time.mktime(yesterday_stop4.timetuple()) * 1000

    res1 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start1,
        "end_absolute": unixtime_stop1,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res2 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start2,
        "end_absolute": unixtime_stop2,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res3 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start3,
        "end_absolute": unixtime_stop3,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res4 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start4,
        "end_absolute": unixtime_stop4,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })

    #aggregator first last avg sum
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    res4 = res4.json()

    dayMonthYear4 = datetime.utcfromtimestamp(unixtime_start1/1000 + 25200).strftime('วันที่: %d/%m/%y')

    try:
        left_morning_yesterday4 = res1["queries"][0]['results'][0]['values'][-1][1]
        right_morning_yesterday4 = res1["queries"][0]['results'][1]['values'][-1][1]
        recentTime_morning_yesterday4 = res1["queries"][0]['results'][0]['values'][-1][0]
        recentTime_morning_yesterday4 = datetime.utcfromtimestamp(recentTime_morning_yesterday4/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_morning_yesterday4 = '-'
        right_morning_yesterday4 = '-'
        recentTime_morning_yesterday4 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_noon_yesterday4 = res2["queries"][0]['results'][0]['values'][-1][1]
        right_noon_yesterday4 = res2["queries"][0]['results'][1]['values'][-1][1]
        recentTime_noon_yesterday4 = res2["queries"][0]['results'][0]['values'][-1][0]
        recentTime_noon_yesterday4 = datetime.utcfromtimestamp(recentTime_noon_yesterday4/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_noon_yesterday4 = '-'
        right_noon_yesterday4 = '-'
        recentTime_noon_yesterday4 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_evening_yesterday4 = res3["queries"][0]['results'][0]['values'][-1][1]
        right_evening_yesterday4 = res3["queries"][0]['results'][1]['values'][-1][1]
        recentTime_evening_yesterday4 = res3["queries"][0]['results'][0]['values'][-1][0]
        recentTime_evening_yesterday4 = datetime.utcfromtimestamp(recentTime_evening_yesterday4/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_evening_yesterday4 = '-'
        right_evening_yesterday4 = '-'
        recentTime_evening_yesterday4 = 'เวลา: ไม่มีข้อมูล'
 
    try:
        left_bedtime_yesterday4 = res4["queries"][0]['results'][0]['values'][-1][1]
        right_bedtime_yesterday4 = res4["queries"][0]['results'][1]['values'][-1][1]
        recentTime_bedtime_yesterday4 = res4["queries"][0]['results'][0]['values'][-1][0]
        recentTime_bedtime_yesterday4 = datetime.utcfromtimestamp(recentTime_bedtime_yesterday4/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_bedtime_yesterday4 = '-'
        right_bedtime_yesterday4 = '-'
        recentTime_bedtime_yesterday4 = 'เวลา: ไม่มีข้อมูล'

    # -----------------------------------------------------------------------------------------------------------------

    yesterday_start1 = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0) - timedelta(days=5)
    unixtime_start1 = time.mktime(yesterday_start1.timetuple()) * 1000
    yesterday_stop1 = datetime.now().replace(hour=10,minute=59,second=59,microsecond=0) - timedelta(days=5)
    unixtime_stop1 = time.mktime(yesterday_stop1.timetuple()) * 1000

    yesterday_start2 = datetime.now().replace(hour=11,minute=0,second=0,microsecond=0) - timedelta(days=5)
    unixtime_start2 = time.mktime(yesterday_start2.timetuple()) * 1000
    yesterday_stop2 = datetime.now().replace(hour=14,minute=59,second=59,microsecond=0) - timedelta(days=5)
    unixtime_stop2 = time.mktime(yesterday_stop2.timetuple()) * 1000

    yesterday_start3 = datetime.now().replace(hour=15,minute=0,second=0,microsecond=0) - timedelta(days=5)
    unixtime_start3 = time.mktime(yesterday_start3.timetuple()) * 1000
    yesterday_stop3 = datetime.now().replace(hour=18,minute=59,second=59,microsecond=0) - timedelta(days=5)
    unixtime_stop3 = time.mktime(yesterday_stop3.timetuple()) * 1000

    yesterday_start4 = datetime.now().replace(hour=19,minute=0,second=0,microsecond=0) - timedelta(days=5)
    unixtime_start4 = time.mktime(yesterday_start4.timetuple()) * 1000
    yesterday_stop4 = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=5)
    unixtime_stop4 = time.mktime(yesterday_stop4.timetuple()) * 1000

    res1 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start1,
        "end_absolute": unixtime_stop1,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res2 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start2,
        "end_absolute": unixtime_stop2,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res3 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start3,
        "end_absolute": unixtime_stop3,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res4 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start4,
        "end_absolute": unixtime_stop4,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })

    #aggregator first last avg sum
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    res4 = res4.json()

    dayMonthYear5 = datetime.utcfromtimestamp(unixtime_start1/1000 + 25200).strftime('วันที่: %d/%m/%y')

    try:
        left_morning_yesterday5 = res1["queries"][0]['results'][0]['values'][-1][1]
        right_morning_yesterday5 = res1["queries"][0]['results'][1]['values'][-1][1]
        recentTime_morning_yesterday5 = res1["queries"][0]['results'][0]['values'][-1][0]
        recentTime_morning_yesterday5 = datetime.utcfromtimestamp(recentTime_morning_yesterday5/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_morning_yesterday5 = '-'
        right_morning_yesterday5 = '-'
        recentTime_morning_yesterday5 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_noon_yesterday5 = res2["queries"][0]['results'][0]['values'][-1][1]
        right_noon_yesterday5 = res2["queries"][0]['results'][1]['values'][-1][1]
        recentTime_noon_yesterday5 = res2["queries"][0]['results'][0]['values'][-1][0]
        recentTime_noon_yesterday5 = datetime.utcfromtimestamp(recentTime_noon_yesterday5/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_noon_yesterday5 = '-'
        right_noon_yesterday5 = '-'
        recentTime_noon_yesterday5 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_evening_yesterday5 = res3["queries"][0]['results'][0]['values'][-1][1]
        right_evening_yesterday5 = res3["queries"][0]['results'][1]['values'][-1][1]
        recentTime_evening_yesterday5 = res3["queries"][0]['results'][0]['values'][-1][0]
        recentTime_evening_yesterday5 = datetime.utcfromtimestamp(recentTime_evening_yesterday5/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_evening_yesterday5 = '-'
        right_evening_yesterday5 = '-'
        recentTime_evening_yesterday5 = 'เวลา: ไม่มีข้อมูล'
 
    try:
        left_bedtime_yesterday5 = res4["queries"][0]['results'][0]['values'][-1][1]
        right_bedtime_yesterday5 = res4["queries"][0]['results'][1]['values'][-1][1]
        recentTime_bedtime_yesterday5 = res4["queries"][0]['results'][0]['values'][-1][0]
        recentTime_bedtime_yesterday5 = datetime.utcfromtimestamp(recentTime_bedtime_yesterday5/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_bedtime_yesterday5 = '-'
        right_bedtime_yesterday5 = '-'
        recentTime_bedtime_yesterday5 = 'เวลา: ไม่มีข้อมูล'

    # -----------------------------------------------------------------------------------------------------------------
    
    yesterday_start1 = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0) - timedelta(days=6)
    unixtime_start1 = time.mktime(yesterday_start1.timetuple()) * 1000
    yesterday_stop1 = datetime.now().replace(hour=10,minute=59,second=59,microsecond=0) - timedelta(days=6)
    unixtime_stop1 = time.mktime(yesterday_stop1.timetuple()) * 1000

    yesterday_start2 = datetime.now().replace(hour=11,minute=0,second=0,microsecond=0) - timedelta(days=6)
    unixtime_start2 = time.mktime(yesterday_start2.timetuple()) * 1000
    yesterday_stop2 = datetime.now().replace(hour=14,minute=59,second=59,microsecond=0) - timedelta(days=6)
    unixtime_stop2 = time.mktime(yesterday_stop2.timetuple()) * 1000

    yesterday_start3 = datetime.now().replace(hour=15,minute=0,second=0,microsecond=0) - timedelta(days=6)
    unixtime_start3 = time.mktime(yesterday_start3.timetuple()) * 1000
    yesterday_stop3 = datetime.now().replace(hour=18,minute=59,second=59,microsecond=0) - timedelta(days=6)
    unixtime_stop3 = time.mktime(yesterday_stop3.timetuple()) * 1000

    yesterday_start4 = datetime.now().replace(hour=19,minute=0,second=0,microsecond=0) - timedelta(days=6)
    unixtime_start4 = time.mktime(yesterday_start4.timetuple()) * 1000
    yesterday_stop4 = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=6)
    unixtime_stop4 = time.mktime(yesterday_stop4.timetuple()) * 1000

    res1 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start1,
        "end_absolute": unixtime_stop1,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res2 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start2,
        "end_absolute": unixtime_stop2,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res3 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start3,
        "end_absolute": unixtime_stop3,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res4 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start4,
        "end_absolute": unixtime_stop4,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })

    #aggregator first last avg sum
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    res4 = res4.json()

    dayMonthYear6 = datetime.utcfromtimestamp(unixtime_start1/1000 + 25200).strftime('วันที่: %d/%m/%y')

    try:
        left_morning_yesterday6 = res1["queries"][0]['results'][0]['values'][-1][1]
        right_morning_yesterday6 = res1["queries"][0]['results'][1]['values'][-1][1]
        recentTime_morning_yesterday6 = res1["queries"][0]['results'][0]['values'][-1][0]
        recentTime_morning_yesterday6 = datetime.utcfromtimestamp(recentTime_morning_yesterday6/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_morning_yesterday6 = '-'
        right_morning_yesterday6 = '-'
        recentTime_morning_yesterday5 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_noon_yesterday6 = res2["queries"][0]['results'][0]['values'][-1][1]
        right_noon_yesterday6 = res2["queries"][0]['results'][1]['values'][-1][1]
        recentTime_noon_yesterday6 = res2["queries"][0]['results'][0]['values'][-1][0]
        recentTime_noon_yesterday6 = datetime.utcfromtimestamp(recentTime_noon_yesterday6/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_noon_yesterday6 = '-'
        right_noon_yesterday6 = '-'
        recentTime_noon_yesterday6 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_evening_yesterday6 = res3["queries"][0]['results'][0]['values'][-1][1]
        right_evening_yesterday6 = res3["queries"][0]['results'][1]['values'][-1][1]
        recentTime_evening_yesterday6 = res3["queries"][0]['results'][0]['values'][-1][0]
        recentTime_evening_yesterday6 = datetime.utcfromtimestamp(recentTime_evening_yesterday6/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_evening_yesterday6 = '-'
        right_evening_yesterday6 = '-'
        recentTime_evening_yesterday6 = 'เวลา: ไม่มีข้อมูล'
 
    try:
        left_bedtime_yesterday6 = res4["queries"][0]['results'][0]['values'][-1][1]
        right_bedtime_yesterday6 = res4["queries"][0]['results'][1]['values'][-1][1]
        recentTime_bedtime_yesterday6 = res4["queries"][0]['results'][0]['values'][-1][0]
        recentTime_bedtime_yesterday6 = datetime.utcfromtimestamp(recentTime_bedtime_yesterday6/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_bedtime_yesterday6 = '-'
        right_bedtime_yesterday6 = '-'
        recentTime_bedtime_yesterday6 = 'เวลา: ไม่มีข้อมูล'

    # -----------------------------------------------------------------------------------------------------------------
    
    yesterday_start1 = datetime.now().replace(hour=6,minute=0,second=0,microsecond=0) - timedelta(days=7)
    unixtime_start1 = time.mktime(yesterday_start1.timetuple()) * 1000
    yesterday_stop1 = datetime.now().replace(hour=10,minute=59,second=59,microsecond=0) - timedelta(days=7)
    unixtime_stop1 = time.mktime(yesterday_stop1.timetuple()) * 1000

    yesterday_start2 = datetime.now().replace(hour=11,minute=0,second=0,microsecond=0) - timedelta(days=7)
    unixtime_start2 = time.mktime(yesterday_start2.timetuple()) * 1000
    yesterday_stop2 = datetime.now().replace(hour=14,minute=59,second=59,microsecond=0) - timedelta(days=7)
    unixtime_stop2 = time.mktime(yesterday_stop2.timetuple()) * 1000

    yesterday_start3 = datetime.now().replace(hour=15,minute=0,second=0,microsecond=0) - timedelta(days=7)
    unixtime_start3 = time.mktime(yesterday_start3.timetuple()) * 1000
    yesterday_stop3 = datetime.now().replace(hour=18,minute=59,second=59,microsecond=0) - timedelta(days=7)
    unixtime_stop3 = time.mktime(yesterday_stop3.timetuple()) * 1000

    yesterday_start4 = datetime.now().replace(hour=19,minute=0,second=0,microsecond=0) - timedelta(days=7)
    unixtime_start4 = time.mktime(yesterday_start4.timetuple()) * 1000
    yesterday_stop4 = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=7)
    unixtime_stop4 = time.mktime(yesterday_stop4.timetuple()) * 1000

    res1 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start1,
        "end_absolute": unixtime_stop1,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res2 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start2,
        "end_absolute": unixtime_stop2,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res3 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start3,
        "end_absolute": unixtime_stop3,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })
    res4 = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start4,
        "end_absolute": unixtime_stop4,
        "metrics": [
            {
            "name": "3df7ac47-5055-43f0-8c3b-dca2e8fee6bd",
            "tags": {
                "attr": [
                "left",
                "right"
                ]
            },
            "group_by": [
                {
                "name": "tag",
                "tags": [
                    "attr"
                ]
                }
            ],
            "aggregators": [
                {
                "name": "last",
                "sampling": {
                    "value": 1,
                    "unit": "hours"
                }
                }
            ]
            }
        ]
        })

    #aggregator first last avg sum
    res1 = res1.json()
    res2 = res2.json()
    res3 = res3.json()
    res4 = res4.json()

    dayMonthYear7 = datetime.utcfromtimestamp(unixtime_start1/1000 + 25200).strftime('วันที่: %d/%m/%y')

    try:
        left_morning_yesterday7 = res1["queries"][0]['results'][0]['values'][-1][1]
        right_morning_yesterday7 = res1["queries"][0]['results'][1]['values'][-1][1]
        recentTime_morning_yesterday7 = res1["queries"][0]['results'][0]['values'][-1][0]
        recentTime_morning_yesterday7 = datetime.utcfromtimestamp(recentTime_morning_yesterday7/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_morning_yesterday7 = '-'
        right_morning_yesterday7 = '-'
        recentTime_morning_yesterday7 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_noon_yesterday7 = res2["queries"][0]['results'][0]['values'][-1][1]
        right_noon_yesterday7 = res2["queries"][0]['results'][1]['values'][-1][1]
        recentTime_noon_yesterday7 = res2["queries"][0]['results'][0]['values'][-1][0]
        recentTime_noon_yesterday7 = datetime.utcfromtimestamp(recentTime_noon_yesterday7/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_noon_yesterday7 = '-'
        right_noon_yesterday7 = '-'
        recentTime_noon_yesterday7 = 'เวลา: ไม่มีข้อมูล'

    try:
        left_evening_yesterday7 = res3["queries"][0]['results'][0]['values'][-1][1]
        right_evening_yesterday7 = res3["queries"][0]['results'][1]['values'][-1][1]
        recentTime_evening_yesterday7 = res3["queries"][0]['results'][0]['values'][-1][0]
        recentTime_evening_yesterday7 = datetime.utcfromtimestamp(recentTime_evening_yesterday7/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_evening_yesterday7 = '-'
        right_evening_yesterday7 = '-'
        recentTime_evening_yesterday7 = 'เวลา: ไม่มีข้อมูล'
 
    try:
        left_bedtime_yesterday7 = res4["queries"][0]['results'][0]['values'][-1][1]
        right_bedtime_yesterday7 = res4["queries"][0]['results'][1]['values'][-1][1]
        recentTime_bedtime_yesterday7 = res4["queries"][0]['results'][0]['values'][-1][0]
        recentTime_bedtime_yesterday7 = datetime.utcfromtimestamp(recentTime_bedtime_yesterday7/1000 + 25200).strftime('เวลา: %H:%M:%S')
    except IndexError:
        left_bedtime_yesterday7 = '-'
        right_bedtime_yesterday7 = '-'
        recentTime_bedtime_yesterday7 = 'เวลา: ไม่มีข้อมูล'

    # -----------------------------------------------------------------------------------------------------------------


    return render_template(
        "home/index.html",
        left_medicine=left_medicine,
        right_medicine=right_medicine,
        name=name,
        picture=picture,

        dayMonthYear=dayMonthYear,
        left_morning=left_morning,
        right_morning=right_morning,
        recentTime_morning=recentTime_morning,
        left_noon=left_noon,
        right_noon=right_noon,
        recentTime_noon=recentTime_noon,
        left_evening=left_evening,
        right_evening=right_evening,
        recentTime_evening=recentTime_evening,
        left_bedtime=left_bedtime,
        right_bedtime=right_bedtime,
        recentTime_bedtime=recentTime_bedtime,

        dayMonthYear1=dayMonthYear1,
        left_morning_yesterday1=left_morning_yesterday1,
        right_morning_yesterday1=right_morning_yesterday1,
        recentTime_morning_yesterday1=recentTime_morning_yesterday1,
        left_noon_yesterday1=left_noon_yesterday1,
        right_noon_yesterday1=right_noon_yesterday1,
        recentTime_noon_yesterday1=recentTime_noon_yesterday1,
        left_evening_yesterday1=left_evening_yesterday1,
        right_evening_yesterday1=right_evening_yesterday1,
        recentTime_evening_yesterday1=recentTime_evening_yesterday1,
        left_bedtime_yesterday1=left_bedtime_yesterday1,
        right_bedtime_yesterday1=right_bedtime_yesterday1,
        recentTime_bedtime_yesterday1=recentTime_bedtime_yesterday1,

        dayMonthYear2=dayMonthYear2,
        left_morning_yesterday2=left_morning_yesterday2,
        right_morning_yesterday2=right_morning_yesterday2,
        recentTime_morning_yesterday2=recentTime_morning_yesterday2,
        left_noon_yesterday2=left_noon_yesterday2,
        right_noon_yesterday2=right_noon_yesterday2,
        recentTime_noon_yesterday2=recentTime_noon_yesterday2,
        left_evening_yesterday2=left_evening_yesterday2,
        right_evening_yesterday2=right_evening_yesterday2,
        recentTime_evening_yesterday2=recentTime_evening_yesterday2,
        left_bedtime_yesterday2=left_bedtime_yesterday2,
        right_bedtime_yesterday2=right_bedtime_yesterday2,
        recentTime_bedtime_yesterday2=recentTime_bedtime_yesterday2,

        dayMonthYear3=dayMonthYear3,
        left_morning_yesterday3=left_morning_yesterday3,
        right_morning_yesterday3=right_morning_yesterday3,
        recentTime_morning_yesterday3=recentTime_morning_yesterday3,
        left_noon_yesterday3=left_noon_yesterday3,
        right_noon_yesterday3=right_noon_yesterday3,
        recentTime_noon_yesterday3=recentTime_noon_yesterday3,
        left_evening_yesterday3=left_evening_yesterday3,
        right_evening_yesterday3=right_evening_yesterday3,
        recentTime_evening_yesterday3=recentTime_evening_yesterday3,
        left_bedtime_yesterday3=left_bedtime_yesterday3,
        right_bedtime_yesterday3=right_bedtime_yesterday3,
        recentTime_bedtime_yesterday3=recentTime_bedtime_yesterday3,

        dayMonthYear4=dayMonthYear4,
        left_morning_yesterday4=left_morning_yesterday4,
        right_morning_yesterday4=right_morning_yesterday4,
        recentTime_morning_yesterday4=recentTime_morning_yesterday4,
        left_noon_yesterday4=left_noon_yesterday4,
        right_noon_yesterday4=right_noon_yesterday4,
        recentTime_noon_yesterday4=recentTime_noon_yesterday4,
        left_evening_yesterday4=left_evening_yesterday4,
        right_evening_yesterday4=right_evening_yesterday4,
        recentTime_evening_yesterday4=recentTime_evening_yesterday4,
        left_bedtime_yesterday4=left_bedtime_yesterday4,
        right_bedtime_yesterday4=right_bedtime_yesterday4,
        recentTime_bedtime_yesterday4=recentTime_bedtime_yesterday4,

        dayMonthYear5=dayMonthYear5,
        left_morning_yesterday5=left_morning_yesterday5,
        right_morning_yesterday5=right_morning_yesterday5,
        recentTime_morning_yesterday5=recentTime_morning_yesterday5,
        left_noon_yesterday5=left_noon_yesterday5,
        right_noon_yesterday5=right_noon_yesterday5,
        recentTime_noon_yesterday5=recentTime_noon_yesterday5,
        left_evening_yesterday5=left_evening_yesterday5,
        right_evening_yesterday5=right_evening_yesterday5,
        recentTime_evening_yesterday5=recentTime_evening_yesterday5,
        left_bedtime_yesterday5=left_bedtime_yesterday5,
        right_bedtime_yesterday5=right_bedtime_yesterday5,
        recentTime_bedtime_yesterday5=recentTime_bedtime_yesterday5,

        dayMonthYear6=dayMonthYear6,
        left_morning_yesterday6=left_morning_yesterday6,
        right_morning_yesterday6=right_morning_yesterday6,
        recentTime_morning_yesterday6=recentTime_morning_yesterday6,
        left_noon_yesterday6=left_noon_yesterday6,
        right_noon_yesterday6=right_noon_yesterday6,
        recentTime_noon_yesterday6=recentTime_noon_yesterday6,
        left_evening_yesterday6=left_evening_yesterday6,
        right_evening_yesterday6=right_evening_yesterday6,
        recentTime_evening_yesterday6=recentTime_evening_yesterday6,
        left_bedtime_yesterday6=left_bedtime_yesterday6,
        right_bedtime_yesterday6=right_bedtime_yesterday6,
        recentTime_bedtime_yesterday6=recentTime_bedtime_yesterday6,

        dayMonthYear7=dayMonthYear7,
        left_morning_yesterday7=left_morning_yesterday7,
        right_morning_yesterday7=right_morning_yesterday7,
        recentTime_morning_yesterday7=recentTime_morning_yesterday7,
        left_noon_yesterday7=left_noon_yesterday7,
        right_noon_yesterday7=right_noon_yesterday7,
        recentTime_noon_yesterday7=recentTime_noon_yesterday7,
        left_evening_yesterday7=left_evening_yesterday7,
        right_evening_yesterday7=right_evening_yesterday7,
        recentTime_evening_yesterday7=recentTime_evening_yesterday7,
        left_bedtime_yesterday7=left_bedtime_yesterday7,
        right_bedtime_yesterday7=right_bedtime_yesterday7,
        recentTime_bedtime_yesterday7=recentTime_bedtime_yesterday7
    )
