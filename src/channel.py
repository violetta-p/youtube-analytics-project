import json
import os
from googleapiclient.discovery import build

# channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
# channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel

api_key: str = os.getenv('YOU_TUBE_API')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
