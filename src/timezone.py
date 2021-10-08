# -*- coding: utf-8 -*-

__author__ = 'Bruce Frank Wong'


import datetime as dt

__all__ = [
    'tz_beijing',
    'tz_trading',
    'to_tz_beijing',
    'to_tz_trading',
]


# 北京时间
tz_beijing: dt.timezone = dt.timezone(dt.timedelta(hours=8))

# 交易时间
tz_trading: dt.timezone = dt.timezone(dt.timedelta(hours=12))

# 时间差异
tz_delta: dt.timedelta = dt.timedelta(hours=4)

def to_tz_beijing(t: dt.time) -> dt.time:
    """
    转换为北京时间。
    如果 t 没有给定时区，判定为北京时间。
    """
    if t.tzinfo == tz_beijing:
        return t
    if t.tzinfo is None:
        return t.replace(tzinfo=tz_beijing)
    temp: dt.datetime = dt.datetime.combine(
        dt.date.today(),
        t
    ).astimezone(tz=tz_trading)
    return temp.astimezone(tz=tz_beijing).timetz()

def to_tz_trading(t: dt.time) -> dt.time:
    """
    转换为交易时间。
    如果 t 没有给定时区，判定为北京时间。
    """
    if t.tzinfo == tz_trading:
        return t
    if t.tzinfo is None:
        t = t.replace(tzinfo=tz_beijing)
    temp: dt.datetime = dt.datetime.combine(
        dt.date.today(),
        t
    ).astimezone(tz=tz_beijing)
    return temp.astimezone(tz=tz_trading).timetz()
