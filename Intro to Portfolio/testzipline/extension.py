import pandas as pd
from zipline.data.bundles import register
from zipline.data.bundles.csvdir import csvdir_equities

register(
    'Bundle_name',
    csvdir_equities(
        ['daily'],
        '/home/yakub/Documents/Python/Intro to Portfolio/testzipline/daily/BTC.csv'
    ),
    calendar_name='XBTC',
)
