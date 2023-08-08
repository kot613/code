"""
Напиши программу, которая проходит сайты по списку, скачивает файлы robots.txt и sitemap.xml и сохраняет на диск.
В случае если файл не найден, выводится сообщение об этом.
Файл зі списком сайтів знаходиться save_robots_and_sitemap_from_site/data.txt
"""
import requests
import shutil
import os

DIR = 'save_robots_and_sitemap_from_site'
lst_site = []

with open(f"{DIR}/data.txt", 'r', encoding='utf-8') as data:
    for line in data.readlines():
        lst_site.append(line.replace('\n', ''))


def save_data(domain, name):
    r = requests.get(f"{domain}/{name}", stream=True)

    if r.status_code == 200:
        filename = f"{domain.partition('//')[-1][:-1].replace('.', '_')}_{name}"
        name_for_write = os.path.join(DIR, filename)
        with open(name_for_write, 'wb') as f:
            # Декодируем поток данных на основе заголовка content-encoding
            r.raw.decode_content = True
            # Копируем поток данных из интернета в файл с помощью модуля shutil
            shutil.copyfileobj(r.raw, f)
        print(f"Файл {name} записано")
    else:
        print(f"Файл {name} не знайдено")


for site in lst_site:
    print('Працюемо з сайтом ', site)
    save_data(site, 'robots.txt')
    save_data(site, 'sitemap.xml')




