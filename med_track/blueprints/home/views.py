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
    yesterday_start = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - timedelta(days=1)
    unixtime_start = time.mktime(yesterday_start.timetuple()) * 1000
    yesterday_stop = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=1)
    unixtime_stop = time.mktime(yesterday_stop.timetuple()) * 1000

    res = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start,
        "end_absolute": unixtime_stop,
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
    res = res.json()
    left_medicine_yesterday1 = res["queries"][0]['results'][0]['values'][-1][1]
    right_medicine_yesterday1 = res["queries"][0]['results'][1]['values'][-1][1]
    dayMonthYear1 = datetime.utcfromtimestamp(unixtime_start/1000 + 25200).strftime('วันที่ %d/%m/%Y') # GMT+7 %H:%M:%S

    # -----------------------------------------------------------------------------------------------------------------
    yesterday_start = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - timedelta(days=2)
    unixtime_start = time.mktime(yesterday_start.timetuple()) * 1000
    yesterday_stop = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=2)
    unixtime_stop = time.mktime(yesterday_stop.timetuple()) * 1000

    res = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start,
        "end_absolute": unixtime_stop,
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
    res = res.json()
    left_medicine_yesterday2 = res["queries"][0]['results'][0]['values'][-1][1]
    right_medicine_yesterday2 = res["queries"][0]['results'][1]['values'][-1][1]
    dayMonthYear2 = datetime.utcfromtimestamp(unixtime_start/1000 + 25200).strftime('วันที่ %d/%m/%Y') # GMT+7 %H:%M:%S

    # -----------------------------------------------------------------------------------------------------------------
    yesterday_start = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - timedelta(days=3)
    unixtime_start = time.mktime(yesterday_start.timetuple()) * 1000
    yesterday_stop = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=3)
    unixtime_stop = time.mktime(yesterday_stop.timetuple()) * 1000

    res = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start,
        "end_absolute": unixtime_stop,
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
    res = res.json()
    left_medicine_yesterday3 = res["queries"][0]['results'][0]['values'][-1][1]
    right_medicine_yesterday3 = res["queries"][0]['results'][1]['values'][-1][1]
    dayMonthYear3 = datetime.utcfromtimestamp(unixtime_start/1000 + 25200).strftime('วันที่ %d/%m/%Y') # GMT+7 %H:%M:%S

    # -----------------------------------------------------------------------------------------------------------------
    yesterday_start = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - timedelta(days=4)
    unixtime_start = time.mktime(yesterday_start.timetuple()) * 1000
    yesterday_stop = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=4)
    unixtime_stop = time.mktime(yesterday_stop.timetuple()) * 1000

    res = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start,
        "end_absolute": unixtime_stop,
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
    res = res.json()
    left_medicine_yesterday4 = res["queries"][0]['results'][0]['values'][-1][1]
    right_medicine_yesterday4 = res["queries"][0]['results'][1]['values'][-1][1]
    dayMonthYear4 = datetime.utcfromtimestamp(unixtime_start/1000 + 25200).strftime('วันที่ %d/%m/%Y') # GMT+7 %H:%M:%S

    # -----------------------------------------------------------------------------------------------------------------
    yesterday_start = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0) - timedelta(days=5)
    unixtime_start = time.mktime(yesterday_start.timetuple()) * 1000
    yesterday_stop = datetime.now().replace(hour=23,minute=59,second=59,microsecond=0) - timedelta(days=5)
    unixtime_stop = time.mktime(yesterday_stop.timetuple()) * 1000

    res = requests.post("https://api.netpie.io/v2/feed/api/v1/datapoints/query", 
        headers={
        "Content-Type": "application/json; charset=utf-8", 
        "Authorization": "Device 3df7ac47-5055-43f0-8c3b-dca2e8fee6bd:fF2cxnCsWzEHk91Be6jGWj6xsJ5vqYPm"
        }, 
        json={
        "start_absolute": unixtime_start,
        "end_absolute": unixtime_stop,
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
    res = res.json()
    left_medicine_yesterday5 = res["queries"][0]['results'][0]['values'][-1][1]
    right_medicine_yesterday5 = res["queries"][0]['results'][1]['values'][-1][1]
    dayMonthYear5 = datetime.utcfromtimestamp(unixtime_start/1000 + 25200).strftime('วันที่ %d/%m/%Y') # GMT+7 %H:%M:%S


    return render_template(
        "home/index.html",
        left_medicine=left_medicine,
        right_medicine=right_medicine,
        name=name,
        picture=picture,
        left_medicine_yesterday1=left_medicine_yesterday1,
        right_medicine_yesterday1=right_medicine_yesterday1,
        dayMonthYear1=dayMonthYear1,
        left_medicine_yesterday2=left_medicine_yesterday2,
        right_medicine_yesterday2=right_medicine_yesterday2,
        dayMonthYear2=dayMonthYear2,
        left_medicine_yesterday3=left_medicine_yesterday3,
        right_medicine_yesterday3=right_medicine_yesterday3,
        dayMonthYear3=dayMonthYear3,
        left_medicine_yesterday4=left_medicine_yesterday4,
        right_medicine_yesterday4=right_medicine_yesterday4,
        dayMonthYear4=dayMonthYear4,
        left_medicine_yesterday5=left_medicine_yesterday5,
        right_medicine_yesterday5=right_medicine_yesterday5,
        dayMonthYear5=dayMonthYear5
    )
