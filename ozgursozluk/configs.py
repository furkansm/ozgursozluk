from os import environ
from typing import Final


SECRET_KEY: Final = environ.get("OZGURSOZLUK_SECRET_KEY", "Some secret string")

DEFAULT_THEME: Final = "light"
DEFAULT_DISPLAY_PINNED_TOPICS: Final = "true"
DEFAULT_DISPLAY_AUTHOR_NICKNAMES: Final = "false"
DEFAULT_EKSI_SOZLUK_BASE_URL: Final = "https://eksisozluk.com"

themes: Final = [
   "light",
   "dark",
   "amoled",
   "violet",
   "gruvbox",
   "gruvboxlight",
   "discord",
   "startpage",
]
eksi_sozluk_base_urls: Final = [
    "https://eksisozluk.com",
    "https://eksisozluk42.com",
    "https://eksisozluk1923.com",
    "https://eksisozluk2023.com",
]