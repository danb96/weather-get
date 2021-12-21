# Get Weather

This weather application uses the [weatherapi](https://www.weatherapi.com/) to retrieve current weather information and display it in the command line.

In order to use this application you must:

1. create an account with [weatherapi](https://www.weatherapi.com/) to generate an API key.
2. provide a config file at`config/config.yml` that looks like:

```yaml
api:
  url: api.weatherapi.com
  version: v1
  apikey: <apikey>
```