thonfrom bs4 import BeautifulSoup

class DataParser:
    def __init__(self):
        pass
    
    def parse_user_info(self, soup: BeautifulSoup):
        user_info = soup.find('div', {'class': 'user-info'})
        user_id = user_info.get('data-user-id')
        username = user_info.find('h1', {'class': 'username'}).text
        nickname = user_info.find('span', {'class': 'nickname'}).text
        avatar_url = user_info.find('img', {'class': 'avatar'}).get('src')
        bio = user_info.find('p', {'class': 'bio'}).text
        
        return {
            'id': user_id,
            'username': username,
            'nickname': nickname,
            'avatar': avatar_url,
            'bio': bio
        }