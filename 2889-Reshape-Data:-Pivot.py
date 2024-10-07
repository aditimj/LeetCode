import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    weather2 = weather.pivot(index='month',columns = 'city', values = 'temperature')
    return weather2


    