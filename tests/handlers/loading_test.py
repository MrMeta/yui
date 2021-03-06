import datetime

import pytest

from yui.handlers.loading.monday import get_holiday_name
from yui.handlers.loading.weekend import weekend_loading_percent


def test_weekend_loading_percent():
    kirito_birthday = datetime.datetime(2008, 10, 7)

    mon = kirito_birthday - datetime.timedelta(days=1)
    tue = kirito_birthday
    wed = kirito_birthday + datetime.timedelta(days=1)
    thu = kirito_birthday + datetime.timedelta(days=2)
    fri = kirito_birthday + datetime.timedelta(days=3)
    sat = kirito_birthday + datetime.timedelta(days=4)
    sun = kirito_birthday + datetime.timedelta(days=5)

    assert weekend_loading_percent(mon) == 0.0
    assert weekend_loading_percent(tue) == 20.0
    assert weekend_loading_percent(wed) == 40.0
    assert weekend_loading_percent(thu) == 60.0
    assert weekend_loading_percent(fri) == 80.0
    assert weekend_loading_percent(sat) == 100.0
    assert weekend_loading_percent(sun) == 100.0


@pytest.mark.asyncio
async def test_get_holiday_name():
    jan_first = datetime.datetime(2018, 1, 1)  # Holiday
    jan_second = datetime.datetime(2018, 1, 2)  # Not holiday

    holiday = await get_holiday_name(jan_first)
    assert holiday is not None and type(holiday) == str

    holiday = await get_holiday_name(jan_second)
    assert holiday is None
