#Бот приветствия гостей гостиницы "Северная звезда"
import datetime

HOTEL = "Северная звезда"
TEXTS = ["Доброй ночи", "Доброе утро", "Добрый день", "Добрый вечер"]


def chast_dnya(hour):
    for l, granica in enumerate([6, 12, 18]):
        if hour < granica:
            return TEXTS[l]
    return TEXTS[3]


def greet(name):
    hour = datetime.datetime.now().hour
    return chast_dnya(hour) + ", " + name + "! Добро пожаловать в гостиницу " + HOTEL


if __name__ == "__main__":
    print(greet("гость"))
