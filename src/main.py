# ██     ██ ███████  █████  ████████ ██   ██ ███████ ██████
# ██     ██ ██      ██   ██    ██    ██   ██ ██      ██   ██
# ██  █  ██ █████   ███████    ██    ███████ █████   ██████
# ██ ███ ██ ██      ██   ██    ██    ██   ██ ██      ██   ██
#  ███ ███  ███████ ██   ██    ██    ██   ██ ███████ ██   ██

# ████████ ██    ██ ██████  ████████ ██      ███████
#    ██    ██    ██ ██   ██    ██    ██      ██
#    ██    ██    ██ ██████     ██    ██      █████
#    ██    ██    ██ ██   ██    ██    ██      ██
#    ██     ██████  ██   ██    ██    ███████ ███████
#
# von Justus Seeck | (C) 2021

from rich import print
import urllib.request
import datetime
import json
import pyfiglet
import turtle

# ===================================================================
# FONTS: http://www.figlet.org/examples.html

# Zeitunterschied zur UTC
timeoffset = 2
# API Endpunkt für Wetterdaten
apiUrl = "https://api.open-meteo.com/v1/forecast?latitude=52.42&longitude=10.78&current_weather=true"

# Distanz und Stiftbreite für Turtle
distance = 5

# ===================================================================


# Formatiert String zu AsciiArt (wird als Maske für Zeichenfunktion verwendet)
def format2Ascii(text):
    return str(pyfiglet.figlet_format(str(text), font="banner3"))


# speichert die aktuelle Temperatur
def fetchTemp():
    # speichere aktuelle Zeit (UTC) in der Variable now
    now = datetime.datetime.now()
    # Läd Wetterdaten von API
    # erstellt ein Web-Request und wartet auf antwort
    with urllib.request.urlopen(apiUrl) as resp:
        # Lese den Body der Antwort aus
        replyData = resp.read()
        # erkenne Kodierung und dekodiere
        replyData = str(replyData.decode(resp.headers.get_content_charset()))

    # dekodierte Daten werden in Dictionary umgewandelt, damit man sie in PY als Array / Dictionary verwenden kann
    parsedData = json.loads(replyData)
    # Speichere die aktuelle temperatur in currentTemp

    # ALTE VERSION DER API
    #  currentTemp = parsedData["hourly"]["temperature_2m"][int(now.strftime("%H")) + timeoffset]

    # NEUE VERSION DER API
    currentTemp = parsedData["current_weather"]["temperature"]

    # gib die aktuelle Temperatur zurück
    return str(currentTemp)


# male die übergebenen String
def drawAscii(string, color):
    formattedString = format2Ascii(string)
    turtle.pencolor(color)
    splitString = formattedString.split("\n")
    # print(splitString)

    # Für jeden string (also jede Zeile) unten liegenden Code ausführen
    for i in splitString:
        print(i + "       LEN: " + str(len(i)))
        turtle.pensize(distance)
        # für Jeden Buchstaben folgenden code ausführen
        for j in i:
            turtle.penup()
            if j == " ":
                turtle.forward(distance)
            else:
                turtle.pendown()
                turtle.forward(distance)

        # Turtle bewegt sich zur ausgangsposition
        turtle.penup()
        turtle.left(180)
        turtle.forward(
            int(len(i)) * distance
        )  # verwende die Länge des Strings multipliziert mit der Stiftgröße (Stiftgröße = distance)
        # Turtle bewegt sich nach unten (Stiftgröße = Zeilengröße)
        turtle.left(90)
        turtle.forward(distance)
        turtle.left(90)

    # bewege turtle nach oben
    turtle.left(90)
    turtle.forward(len(splitString) * distance)
    turtle.right(90)


def main():
    # Speichere Wort in Variable text
    text = str(input("WORT EINGEBEN (!t für aktuelle Temperatur): "))
    # Wenn text == !t lade die aktuelle Temperatur von der API, hänge "C" an und zeichne diesen Wert
    if text.capitalize() == "!t".capitalize():
        drawAscii(fetchTemp() + " C", "red")
    # Wenn Text nicht '!t' ist, make eingegebenen Text
    else:
        drawAscii(text, "green")

    # Warte auf Enter, damit sich das Fenster nicht schließt
    input("Press Enter to continue...")


# Starte die Main funktion, wenn die .py Datei gestartet wird und nicht als Import verwendet wird
if __name__ == "__main__":
    main()
