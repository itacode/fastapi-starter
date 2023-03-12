from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    UPLOAD_FOLDER: str
    MY_SERVICE_DB_USER: str
    MY_SERVICE_DB_PASSWORD: str
    MY_SERVICE_DB_HOST: str
    MY_SERVICE_DB_PORT: str
    MY_SERVICE_DB_NAME: str

    def get_db_url(self):
        return (
            f"mysql+pymysql://{self.MY_SERVICE_DB_USER}"
            + f":{self.MY_SERVICE_DB_PASSWORD}"
            + f"@{self.MY_SERVICE_DB_HOST}"
            + f":{self.MY_SERVICE_DB_PORT}"
            + f"/{self.MY_SERVICE_DB_NAME}"
        )


settings = Settings()
