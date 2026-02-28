from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

#класс чтобы читать файл .env
class Settings(BaseSettings):
  bot_token: SecretStr
  model_config: SettingsConfigDict = SettingsConfigDict(
      env_file='.env',
      env_file_enconding='utf-8'
  )


config = Settings()
