Age = int(input('Сколько вам полных лет?'))

Genres = input('Какие жанры игр вы любите?')

Platform = input('Какой платформой вы пользуетесь?')

Categories = input('Какая категория игр вам интересна?')

Rating = input('Важен ли вам рейтинг игры?')

PriceMin = int(input('Напишите минимальную цену игры:'))

PriceMax = int(input('Напишите макимальную цену игры:'))

def check_platform():
    if any(platform in row[6].split(';') for platform in Platform) or Platform == ['']:
        return True
    else:
        return False

def check_category():
    if any(category in row[8].split(';') for category in Categories) or Categories == ['']:
        return True
    else:
        return False

def check_genre():
    if any(genre in row[9].split(';') for genre in Genres) or Genres == ['']:
        return True
    else:
        return False

if Rating == 'Да':
    Rating = True
else:
    Rating = False

def check_rating():
    if Rating is True:
        if row[12].isdigit() and row[13].isdigit():
            if (Rating is True) and coefficient_rating >= 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def check_price():
    if PriceMin <= float(row[17]) <= PriceMax:
        return True
    else:
        return False


with open('steam.csv', encoding='utf-8') as f, open('результат.txt', 'w', encoding='utf-8') as writing_result:
    writing_result.write('Игры для вас:\n')
    for row in f:
        row = row.split(',')
        if row[12].isdigit() and row[13].isdigit():
            if int(row[12]) > int(row[13]):
                coefficient_rating = int(row[12]) - int(row[13])
        if row[7].isdigit():
            if Age >= int(row[7]):
                if check_rating() and check_category() and check_genre() and check_platform() and check_price():
                    writing_result.write(row[1] + '\n' + 'Цена: ' + row[17] + '\n' + 'Категория: '
                                         + row[9] + '\n' + 'Рейтинг = ' + str(coefficient_rating)
                                         + '\n-----\n')
                if check_rating() and check_category() and check_genre() and check_platform() and check_price():
                    writing_result.write(row[1] + '\n' + 'Цена: ' + row[17] + '\n' + 'Категория: ' + row[9]
                                         + '\n-----\n')

print('Результат программы сохранен в файле "Результат"')
