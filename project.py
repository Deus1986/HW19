import pydantic
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    remote_url: str = 'http://hub.browserstack.com/wd/hub'
    app: str = 'bs://sample.app'
    browser_platform: str = 'android'
    timeout: float = 4.0


config = Config()
