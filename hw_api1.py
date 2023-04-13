import requests

URL = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'

def get_smartest_hero(url: str) -> str:
    resp = requests.get(url)
    filtered_list = []
    for i in resp.json():
        if i['name'] in ('Hulk', 'Captain America', 'Thanos'):
            filtered_list.append(i)

    intl = 0
    intl_hero = ''
    for i in filtered_list:                
        if i['powerstats']['intelligence'] > intl:
            intl_hero = i['name']
            intl = i['powerstats']['intelligence']
    
    return intl_hero


if __name__ == '__main__':
    print(get_smartest_hero(URL))
