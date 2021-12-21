import requests
import yaml
import json


CONFIG = "config/config.yml"


def main():
    with open(CONFIG, "r") as conf_file:
        config = yaml.safe_load(conf_file)
    print(config)

    api_config = config["api"]
    api_key = api_config["apikey"]
    url = api_config["url"]
    api_version = api_config["version"]

    response = requests.get(
        url=f"https://{url}/{api_version}/current.json",
        params={
            "key": api_key,
            "q": "London",
            "days": 1,
            "api": "no",
            "alerts": "no"
        }
    )

    print(json.dumps(response.json(), indent=2))


if __name__ == "__main__":
    main()
