# -*- coding: utf-8 -*
##
## Copyright (c) 2014 Rodolphe Breard
## 
## Permission to use, copy, modify, and/or distribute this software for any
## purpose with or without fee is hereby granted, provided that the above
## copyright notice and this permission notice appear in all copies.
## 
## THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
## WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
## MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
## ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
## WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
## ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
## OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
##

from ryzomapi.sas import get

class RyzomDate:
    __ticks_per_hour = 1800
    __hours_per_day = 24
    __days_per_week = 6
    __days_per_month = 30
    __month_per_cycle = 12
    __cycles_per_year = 4
    __start_year = 2567

    __offset = 61 * __hours_per_day * __ticks_per_hour
    __months = ('Winderly', 'Germinally', 'Folially', 'Floris', 'Medis', 'Thermis', 'Harvestor', 'Frutor', 'Fallenor', 'Pluvia', 'Mystia', 'Nivia')
    __days = ('Prima', 'Dua', 'Tria', 'Quarta', 'Quinteth', 'Holeth')
    __locales = {'en': {'ac': 'AC', 'num': ('st', 'nd', 'rd', 'th')},
                 'fr': {'ac': 'CA', 'num': ('er', 'nd', 'ème', 'ème')},
                 'de': {'ac': 'AZ', 'num': ('.', '.', '.', '.')}}

    def __init__(self, tick=None):
        if tick is None:
            tick = int(get('time', format='xml').find('server_tick').text)
        self.locale_name = 'en'
        self.tick = int(tick)

        tick = self.tick - self.__offset
        hours = round(tick / self.__ticks_per_hour)
        days = round(hours / self.__hours_per_day)
        months = round(days / self.__days_per_month)
        cycles = round(months / self.__month_per_cycle)
        years = round(cycles / self.__cycles_per_year)

        self.year = self.__start_year + years
        self.cycle = cycles % self.__cycles_per_year
        self.month = self.__months[int(months % self.__month_per_cycle) - 1]
        self.day = days % self.__days_per_month
        self.hour = hours % self.__hours_per_day
        self.day_of_week = self.__days[int(self.day % self.__days_per_week) - 1]

    def __str__(self):
        self.cycle_numeral = self.__locales[self.locale_name]['num'][int(self.cycle) - 1]
        self.ac = self.__locales[self.locale_name]['ac']
        return '%(hour)dh - %(day_of_week)s, %(month)s %(day)d, %(cycle)d%(cycle_numeral)s %(ac)s %(year)d' % self.__dict__

    def locale(self, locale):
        if locale not in self.__locales:
            raise ValueError('%s: unknown locale' % locale)
        self.locale_name = locale
        return self
