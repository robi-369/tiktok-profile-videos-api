thonfrom bs4 import BeautifulSoup

class VideoExtractor:
    def __init__(self):
        pass
    
    def extract_video_data(self, soup: BeautifulSoup):
        video_data = []
        for video in soup.find_all('div', {'class': 'video-feed'}):
            video_url = video.find('a', {'class': 'video-url'}).get('href')
            description = video.find('div', {'class': 'video-description'}).text
            music = self.extract_music_info(video)
            stats = self.extract_video_stats(video)

            video_data.append({
                'videoUrl': video_url,
                'description': description,
                'music': music,
                'stats': stats
            })
        return video_data

    def extract_music_info(self, video):
        music = video.find('div', {'class': 'music-info'})
        title = music.find('span', {'class': 'music-title'}).text
        author = music.find('span', {'class': 'music-author'}).text
        music_id = music.get('data-music-id')
        return {
            'title': title,
            'author': author,
            'id': music_id
        }

    def extract_video_stats(self, video):
        likes = int(video.find('span', {'class': 'likes'}).text)
        comments = int(video.find('span', {'class': 'comments'}).text)
        shares = int(video.find('span', {'class': 'shares'}).text)
        plays = int(video.find('span', {'class': 'plays'}).text)
        hashtags = [hashtag.text for hashtag in video.find_all('span', {'class': 'hashtag'})]
        
        return {
            'likes': likes,
            'comments': comments,
            'shares': shares,
            'plays': plays,
            'hashtags': hashtags
        }