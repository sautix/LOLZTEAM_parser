import requests
from bs4 import BeautifulSoup

def get_info():
    
    cookies = {
        'dfuid': '69586183a406a42e6f82e6a6b4482ac1',
        'xf_session': '3d4972f665b96c3d65ce6ed9faa27983',
        '_ga': 'GA1.1.1572736551.1701090291',
        '_ym_uid': '17010902914776125',
        '_ym_d': '1701090291',
        '_ym_isad': '2',
        '_ga_J7RS527GFK': 'GS1.1.1701090290.1.1.1701090302.0.0.0',
    }

    headers = {
        'authority': 'zelenka.guru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'dfuid=69586183a406a42e6f82e6a6b4482ac1; xf_session=3d4972f665b96c3d65ce6ed9faa27983; _ga=GA1.1.1572736551.1701090291; _ym_uid=17010902914776125; _ym_d=1701090291; _ym_isad=2; _ga_J7RS527GFK=GS1.1.1701090290.1.1.1701090302.0.0.0',
        'if-modified-since': 'Monday, 27-Nov-2023 13:05:00 GMT',
        'referer': 'https://zelenka.guru/',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    users = list()
    for i in range(1, 190):
        print(f'Начинаю парсинг {i} страницы.')
        url = f"https://zelenka.guru/online/?type=registered&page={i}"
        s = requests.Session()
        response = s.get(url=url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        members = soup.find_all("div", class_="member")
        for member in members:
            username_elem = member.find('h3', class_='username')
            username = username_elem.text
            href = username_elem.find('a').get('href')
            url = "https://zelenka.guru/" + href
            previous_likes = member.find('span', class_="counterIcon likeCounterIcon")
            likes = previous_likes.findNext().text.replace(" ", '')
            if int(likes) < 200:
                print(f'У {username} мало симп.')
            elif username in users:
                print(f'Пользователь {username} уже добавлен')
            else:
                users.append(username)
                print(f'Пользователь {username} прошел по условиям.')
                with open("users.txt", 'a') as file:
                    file.write('Имя пользователя: ' + username + '\n' + 'Ссылка на профиль: ' + url + '\n' + 'Кол-во симпатий: ' + likes + '\n\n')
    print(f'Спаршено {len(users)} пользователей.')

def main():
    get_info()

if __name__ == "__main__":
    main()