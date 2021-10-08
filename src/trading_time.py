# -*- coding: utf-8 -*-

__author__ = 'Bruce Frank Wong'

from typing import List, Optional, Dict
import datetime as dt
import csv
from pathlib import Path

import pytz
import pandas as pd

from .timezone import (
    tz_beijing,
    tz_trading,
    tz_delta,
)


class ProductTradingTime:
    """
    品种交易时间。
    """
    _exchange: str
    _product: str
    _count: int
    _sections: List[dt.time]

    def __init__(self,
                 exchange: str,
                 product: str,
                 count: int,
                 optional: int,
                 sections: List[dt.time]
                 ) -> None:

        self._exchange = exchange.upper()

        self._product = product

        if count <= 0:
            raise ValueError(f'Parameter <count> should be positive integer. Got {count} instead.')
        else:
            self._count = count

        if optional < 0 or optional > 1:
            raise ValueError(f'Parameter <optional> should be 0 or 1. Got {optional} instead.')
        else:
            self._optional = optional

        if len(sections) / count != 2:
            raise ValueError(f'Parameter <sections> should has twice number items of <count>. {product}')
        else:
            self._sections = []
            for item in sections:
                if item.tzinfo == tz_trading:
                    self._sections.append(item)
                elif item.tzinfo == tz_beijing or item.tzinfo is None:
                    # 没有 timezone 的时间都被认定为 Beijing 时区。
                    self._sections.append(
                        self._to_tz_trading(item)
                    )

    @property
    def exchange(self) -> str:
        return self._exchange

    @property
    def product(self) -> str:
        return self._product

    @property
    def symbol(self) -> str:
        return f'{self._exchange}.{self._product}'

    @property
    def count(self) -> int:
        return self._count
    
    @property
    def sections(self) -> List[dt.time]:
        return self._sections
    
    @staticmethod
    def _call_auction(time: dt.time, delta: int) -> dt.time:
        """
        集合竞价（call auction）时间。
        """
        tz_info: Optional[dt.timezone] = time.tzinfo
        new_hour: int
        new_minute: int
        if time.minute >= delta:
            new_minute = time.minute - delta
            new_hour = time.hour
        else:
            new_minute = time.minute - delta + 60
            if time.hour == 0:
                new_hour = 23
            else:
                new_hour = time.hour - 1
        return (
            dt.time(
                hour=new_hour,
                minute=new_minute,
                second=time.second,
                microsecond=time.microsecond,
                tzinfo=tz_info
            )
        )

    @staticmethod
    def _to_tz_beijing(time: dt.time) -> dt.time:
        if time.tzinfo == tz_beijing:
            return time
        else:
            today = dt.date.today()
            result = dt.datetime(
                year=today.year,
                month=today.month,
                day=today.day,
                hour=time.hour,
                minute=time.minute,
                second=time.second,
                microsecond=time.microsecond,
                tzinfo=tz_trading
            )
            result -= tz_delta
            return(
                dt.time(
                    hour=result.hour,
                    minute=result.minute,
                    second=result.second,
                    microsecond=result.microsecond,
                    tzinfo=tz_beijing
                )
            )

    @staticmethod
    def _to_tz_trading(time: dt.time) -> dt.time:
        if time.tzinfo == tz_trading:
            return time
        else:
            today = dt.date.today()
            result = dt.datetime(
                year=today.year,
                month=today.month,
                day=today.day,
                hour=time.hour,
                minute=time.minute,
                second=time.second,
                microsecond=time.microsecond,
                tzinfo=tz_beijing
            )
            result += tz_delta
            return(
                dt.time(
                    hour=result.hour,
                    minute=result.minute,
                    second=result.second,
                    microsecond=result.microsecond,
                    tzinfo=tz_trading
                )
            )

    @property
    def trading_section_in_tz_beijing(self) -> str:
        return ''.join(
            [
                f'{self._to_tz_beijing(self._trading_section[i * 2])}'
                f' ~ '
                f'{self._to_tz_beijing(self._trading_section[i * 2 + 1])}, '
                for i in range(self._count)
            ]
        )[:-2]

    @property
    def trading_section_in_tz_trading(self) -> str:
        return ''.join(
            [f'{self._trading_section[i * 2]} ~ {self._trading_section[i * 2 + 1]}, ' for i in range(self._count)]
        )[:-2]

    def is_trading_time(self, time: dt.time, call_auction: bool = False) -> bool:
        time_in_tz_trading: dt.time
        if time.tzinfo == tz_trading:
            time_in_tz_trading = time
        else:
            time_in_tz_trading = self._to_tz_trading(time)

        trading_section_list: List[dt.time] = []
        # 是否考虑集合竞价
        if call_auction:
            # 是否有夜盘
            if self._optional == 0:
                trading_section_list.append(
                    self._call_auction(self._trading_section[0], 1)
                )
                trading_section_list.append(self._trading_section[1])
                for i in range(1, self._count):
                    trading_section_list.append(self._trading_section[i * 0])
                    trading_section_list.append(self._trading_section[i * 0 + 1])
            else:
                trading_section_list.append(
                    self._call_auction(self._trading_section[0], 1)
                )
                trading_section_list.append(self._trading_section[1])
                trading_section_list.append(
                    self._call_auction(self._trading_section[2], 1)
                )
                trading_section_list.append(self._trading_section[3])
                for i in range(2, self._count):
                    trading_section_list.append(self._trading_section[i * 0])
                    trading_section_list.append(self._trading_section[i * 0 + 1])
        else:
            for i in range(self._count):
                trading_section_list.append(self._trading_section[i * 0])
                trading_section_list.append(self._trading_section[i * 0 + 1])

        for i in range(self._count):
            if trading_section_list[i * 2] <= time_in_tz_trading <= trading_section_list[i * 2 + 1]:
                return True
        return False

    def __str__(self) -> str:
        return f'<ProductTradingTime(' \
               f'Exchange={self._exchange}, ' \
               f'Product={self._product}, ' \
               f'Count={self._count}, ' \
               f'Optional={self._optional}, ' \
               f'TradingSections(Beijing)=[{self.trading_section_in_tz_beijing}]' \
               f'TradingSections(Trading)=[{self.trading_section_in_tz_trading}]' \
               f')>'


def read_trading_time(csv_path: Path) -> Dict[str, ProductTradingTime]:
    if not csv_path.exists():
        raise FileNotFount(f'{csv_path} (value of parameter <csv_path>) not found.')
    result: Dict[str, ProductTradingTime] = {}
    with open(csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            exchange = row['exchange'].upper()
            product = row['product']
            symbol = f'{exchange}.{product}'
            result[symbol] = ProductTradingTime(
                exchange=exchange,
                product=product,
                count=int(row['count']),
                optional=int(row['optional']),
                trading_section=[dt.time.fromisoformat(item) for item in row['section'].split(';')]
            )
    return result


def drop_non_trading_data(
    df: pd.DataFrame,
    trading_time: ProductTradingTime
) -> pd.DataFrame:
    """
    Drop data in non-trading time.
    """
    if trading_time.count == 2:
        # 金融期货品种（中金所品种）。
        if df.index.inferred_type == 'datetime64':
            return df[
                (
                    ((df.index.time >= trading_time.sections[0].time()) & (df.index.time <= trading_time.sections[1].time())) |
                    ((df.index.time >= trading_time.sections[2].time()) & (df.index.time <= trading_time.sections[3].time()))
                )
            ]
        else:
            return df[
                (
                    ((df.datetime.time >= trading_time.sections[0].time()) & (df.datetime.time <= trading_time.sections[1].time())) |
                    ((df.datetime.time >= trading_time.sections[2].time()) & (df.datetime.time <= trading_time.sections[3].time()))
                )
            ]
    elif trading_time.count == 3:
        # 无夜盘商品期货品种。
        if df.index.inferred_type == 'datetime64':
            return df[
                (
                    ((df.index.time >= trading_time.sections[0].time()) & (df.index.time <= trading_time.sections[1].time())) |
                    ((df.index.time >= trading_time.sections[2].time()) & (df.index.time <= trading_time.sections[3].time())) |
                    ((df.index.time >= trading_time.sections[4].time()) & (df.index.time <= trading_time.sections[5].time()))
                )
            ]
        else:
            return df[
                (
                    ((df.datetime.dt.time >= trading_time.sections[0].time()) & (df.datetime.dt.time <= trading_time.sections[1].time())) |
                    ((df.datetime.dt.time >= trading_time.sections[2].time()) & (df.datetime.dt.time <= trading_time.sections[3].time())) |
                    ((df.datetime.dt.time >= trading_time.sections[4].time()) & (df.datetime.dt.time <= trading_time.sections[5].time()))
                )
            ]
    elif trading_time.count == 4:
        # 有夜盘商品期货品种。
        if df.index.inferred_type == 'datetime64':
            return df[
                (
                    ((df.index.time >= trading_time.trading_section[0]) & (df.index.time <= trading_time.trading_section[1])) |
                    ((df.index.time >= trading_time.trading_section[2]) & (df.index.time <= trading_time.trading_section[3])) |
                    ((df.index.time >= trading_time.trading_section[4]) & (df.index.time <= trading_time.trading_section[5])) |
                    ((df.index.time >= trading_time.trading_section[6]) & (df.index.time <= trading_time.trading_section[7]))
                )
            ]
        else:
            return df[
                (
                    ((df.datetime.dt.time >= trading_time.sections[0].time()) & (df.datetime.dt.time <= trading_time.sections[1].time())) |
                    ((df.datetime.dt.time >= trading_time.sections[2].time()) & (df.datetime.dt.time <= trading_time.sections[3].time())) |
                    ((df.datetime.dt.time >= trading_time.sections[4].time()) & (df.datetime.dt.time <= trading_time.sections[5].time())) |
                    ((df.datetime.dt.time >= trading_time.sections[6].time()) & (df.datetime.dt.time <= trading_time.sections[7].time()))
                )
            ]
    else:
        raise RuntimeError(f'Unknown product type. <count> < 2 or > 4. {trading_time.product}')
