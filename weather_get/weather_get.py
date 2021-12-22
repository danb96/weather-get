import yaml
from weather_get import WeatherApi
from pprint import pprint


CONFIG = "config/config.yml"


def main():
    with open(CONFIG, "r") as conf_file:
        config = yaml.safe_load(conf_file)
    print(config)

    api_config = config["api"]
    api_key = api_config["apikey"]
    url = api_config["url"]
    api_version = api_config["version"]

    api = WeatherApi(url=f"{url}/{api_version}", api_key=api_key)
    pprint(api.get_current(locale="London"))
    pprint(api.get_forecast(locale="London", days=3))


if __name__ == "__main__":
    main()
