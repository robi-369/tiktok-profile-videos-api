thonimport requests
from bs4 import BeautifulSoup
import json
from .extractors.video_extractor import VideoExtractor
from .utils.data_parser import DataParser
from .config.settings import SETTINGS

class TikTokScraper:
    def __init__(self, username=None, user_id=None, profile_url=None):
        self.username = username
        self.user_id = user_id
        self.profile_url = profile_url
        self.base_url = 'https://www.tiktok.com/'
        self.video_extractor = VideoExtractor()
        self.data_parser = DataParser()

    def fetch_profile_data(self):
        if self.username:
            url = f'{self.base_url}@{self.username}'
        elif self.user_id:
            url = f'{self.base_url}@{self.user_id}'
        elif self.profile_url:
            url = self.profile_url
        else:
            raise ValueError("No valid identifier provided (username, user_id, or profile_url).")
        
        response = requests.get(url)
        if response.status_code != 200:
            raise ConnectionError(f"Failed to fetch the profile: {response.status_code}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        video_data = self.video_extractor.extract_video_data(soup)
        user_info = self.data_parser.parse_user_info(soup)

        return video_data, user_info

    def save_data(self, video_data, user_info, output_file):
        data = {
            'user_info': user_info,
            'videos': video_data
        }
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {output_file}")