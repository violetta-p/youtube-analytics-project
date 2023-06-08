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
        self.__channel_id = channel_id
        self.title = None
        self.url = None
        self.description = None
        self.view_count = 0
        self.subscriber_count = 0
        self.video_count = 0

    #def print_info(self) -> None:
    #   """Выводит в консоль информацию о канале."""
    #   channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
    #   print(json.dumps(channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    def set_new_data(self):
        video_response = self.get_service()
        self.title: str = video_response['items'][0]['snippet']['title']
        self.url: str = video_response['items'][0]['snippet']['medium']['url']
        self.description: str = video_response['items'][0]['snippet']['description']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.video_count: int = video_response['items'][0]['statistics']['videoCount']
        self.subscriber_count: int = video_response['items'][0]['statistics']['subscriberCount']

    @classmethod
    def get_service(cls):
        video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=cls.channel_id
                                               ).execute()
        return video_response

    def to_json(self, file_name):
        data = {"channel_id": self.channel_id, "title": self.title,
                "url": self.url, "description": self.description,
                "view_count": self.view_count, "subscriber_count": self.subscriber_count,
                "video_count": self.video_count}

        with open(file_name, "w") as json_file:
            json.dump(data, json_file)



