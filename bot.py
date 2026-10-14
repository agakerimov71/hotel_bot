# Бот приветствия гостей гостиницы "Северная звезда"
import datetime
import re
import sys

HOTEL = "Северная звезда"
TEXTS = {
    "ru": ["Доброй ночи", "Доброе утро", "Добрый день", "Добрый вечер"],
    "en": ["Good night", "Good morning", "Good afternoon", "Good evening"],
}


def chast_dnya(hour, lang="ru"):
    t = TEXTS[lang]
    for i, granica in enumerate([6, 12, 18]):
        if hour < granica:
            return t[i]
    return t[3]


def nomer_ok(room):
    # номер комнаты в гостинице всегда из трех цифр
    return bool(re.fullmatch(r"\d{3}", room))


def greet(name, room=None, lang="ru", vip=False):
    hour = datetime.datetime.now().hour
    text = chast_dnya(hour, lang) + ", " + name + "!"
    if room:
        if lang == "ru":
            text += f" Ваш номер {room}, ключ на стойке регистрации."
        else:
            text += f" Your room is {room}. Enjoy your stay!"
    if vip:
        text += " Для вас открыт лаунж на 5 этаже."
    return text


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "гость"
    try:
        room = sys.argv[2]
    except IndexError:
        room = None
    if room and not nomer_ok(room):
        print("Номер комнаты из трех цифр, например 214")
        sys.exit(1)
    print(
        greet(
            name, room, "en" if "en" in sys.argv else "ru", "vip" in sys.argv
        )
    )  # vip из аргументов
