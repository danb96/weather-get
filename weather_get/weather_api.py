import requests
from typing import AnyStr, Dict


class WeatherApi(object):
    def __init__(self, url: AnyStr, api_key: AnyStr):
        self._url = url
        self._api_key = api_key

    def _call_api(self, endpoint: AnyStr, params: Dict[AnyStr, AnyStr]) -> Dict[AnyStr, AnyStr]:
        response = requests.get(
            url=f"https://{self._url}/{endpoint}",
            params={
                "key": self._api_key,
                **params,
            },
        )

        response.raise_for_status()
        return response.json()

    @staticmethod
    def __bool_convert_yn(value: bool) -> AnyStr:
        return {
            True: "yes",
            False: "no",
        }[value]

    def get_current(self, locale: AnyStr, air_quality: bool = False) -> Dict[AnyStr, AnyStr]:
        aqi = self.__bool_convert_yn(air_quality)

        return self._call_api(
            endpoint="current.json",
            params={
                "q": locale,
                "aqi": aqi
            }
        )

    def get_forecast(self, locale: AnyStr, days: int, air_quality: bool = False, weather_alerts: bool = False) -> Dict[AnyStr, AnyStr]:
        assert 0 < days <= 10
        aqi = self.__bool_convert_yn(air_quality)
        alerts = self.__bool_convert_yn(weather_alerts)

        return self._call_api(
            endpoint="forecast.json",
            params={
                "q": locale,
                "aqi": aqi,
                "alerts": alerts,
                "days": days,
            }
        )
