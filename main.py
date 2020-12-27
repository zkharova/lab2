import csv
import re

print('Добрый день!')
print('Ответьте, пожалуйста, на несколько вопросов. Если хотите пропустить вопрос, нажмите enter')

genre_input = input('Какой жанр игр Вам интересен?\n')
genre_in = list([genre.lstrip().capitalize() for genre in genre_input.split(',')])

category_input = input('Игры какой категории Вас интересуют?\n')
category_in = list([category.lstrip().title() for category in category_input.split(',')])

developer_input = input('Какой разработчик предпочтителен?\n')
developer_in = list([developer.lstrip().title() for developer in developer_input.split(',')])

platform_input = input('На какой платформе Вы будете играть?\n')
platform_in = list([platform.lstrip().lower() for platform in platform_input.split(',')])

year = input('Какой год выхода Вас интересует? (Можно ввести как конкретный год, так и промежуток: YYYY-YYYY)\n')
price = input('Введите цену игры в долларах (используйте < или >)\n')
ratings = input('Хороших отзывов должно быть больше, чем отрицательных? (Введите \'да\' или \'нет\')\n').lower()


def genre_checking(game_inv):
    return any(genre in game_inv for genre in genre_in) or (genre_in == [''])


def category_checking(game_inv):
    return any(category in game_inv for category in category_in) or (category_in == [''])


def developer_checking(game_inv):
    return any(developer in game_inv for developer in developer_in) or (developer_in == [''])


def platform_checking(game_inv):
    return any(platform in game_inv for platform in platform_in) or (platform_in == [''])


def year_checking(game_inv, year_in=year):
    if '-' in year_in:
        year_in = year_in.split('-')
        return year_in[0] <= game_inv <= year_in[1]
    else:
        return (game_inv == year_in) or (year_in == '')


def cost_checking(game_inv, price_in=price):
    if price_in == '':
        return 0.0 <= game_inv <= 422.0
    elif price_in[0] == '<':
        k = float(re.findall(r'[\d.]+', price_in)[0])
        return 0.0 <= game_inv <= k
    else:
        return price_in == game_inv


def ratings_checking(game_inv):
    return ((ratings == 'да') and (game_inv[0] > game_inv[1])) or (ratings == '')


with open('steam.csv', encoding='utf-8') as f, \
        open('result.txt', 'w', encoding='utf-8') as f1:
    reader = csv.reader(f)
    for line in reader:
        if line[0] == 'appid':
            continue

        game_genre_in = line[9].split(';') and line[10].split(';')
        game_category_in = line[8].split(';')
        game_developer_in = line[4].split(';')
        game_platform_in = line[6].split(';')
        game_year_in = line[2].split('-')[0]
        game_cost_in = float(line[17])
        game_ratings_in = [int(line[12]), int(line[13])]

        if (genre_checking(game_genre_in) and
                category_checking(game_category_in) and
                developer_checking(game_developer_in) and
                platform_checking(game_platform_in) and
                year_checking(game_year_in) and
                cost_checking(game_cost_in) and
                ratings_checking(game_ratings_in)):
            f1.write(line[1] + '\n')