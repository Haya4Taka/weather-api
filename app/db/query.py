def get_hourly_climate(cursor, city_id, hours):
    """現在時刻からsizeで指定した時間分先の天候情報を１時間単位で取得する
    """
    stmt = (f'SELECT datetime, weather, weather_description, temp, humidity, pressure '
            f'FROM weather_hourly WHERE city_id = {city_id}')
    cursor.execute(stmt)
    result = cursor.fetchmany(size=hours)
    return result


def get_daily_climate(cursor, city_id, days):
    """現在の日付からsizeで指定した日付分先の天候情報を１日単位で取得する
    """
    stmt = (f'SELECT datetime, weather, weather_description, temp, humidity, pressure '
            f'FROM weather_daily WHERE city_id = {city_id}')
    cursor.execute(stmt)
    result = cursor.fetchmany(size=days)
    return result

