import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

@dataclass
class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///bot.db")

    def __post_init__(self):
        if self.BOT_TOKEN == "":
            raise ValueError("BOT_TOKEN environment variable is required")

config = Config()
