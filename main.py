# Инициализация игры
usedCities = list()
playersFirstLetter = ''
playersCityName = ''
with open('USCities_ENG.txt') as citiesFile:
    cityNames = citiesFile.read().splitlines()
# проверка корректности введеного названия города
def checkCity(cityName, letter):
    if letter != '':
        while True:
            if cityName[0].lower() == letter.lower():
                usedCities.append(cityName)
                return cityName
            elif cityName[0] == '0':
                return '0'
            else:
                print("No, your city's name should start with '{0}' not with '{1}'".format(letter.upper(), cityName[0]))
                cityName = input("Try again: ")
    else:
        usedCities.append(cityName)
        return cityName
# меню игры
MenuString = """1) Start game
0) Exit"""
print(MenuString)
# начать игру
while True:
    playersChoice = input("Your choice: ")
    if playersChoice == '1':
        print("Game is started. Type 0 anytime to surrender")
        while True:
            playersCityName = input("Your city is: ")
            playersCityName = checkCity(playersCityName, playersFirstLetter)
            if playersCityName == '0':
                print("Seems like you gave up. Type 0 once more to leave the game or 1 to continue.")
                break
            else:
                GameIsTrue = True
                while GameIsTrue:
                    lastLetter = playersCityName[len(playersCityName) - 1]
                    for botCityName in cityNames:
                        if botCityName[0] == lastLetter.upper():
                            playersFirstLetter = botCityName[len(botCityName) - 1]
                            print("My city is {0}. Your letter is '{1}'".format(botCityName, playersFirstLetter.upper()))
                            usedCities.append(botCityName)
                            cityNames.remove(botCityName)
                            GameIsTrue = False
                            break
    elif playersChoice == '0':
        print("Seeya later")
        print(usedCities)
        break
    else:
        print("Didnt recognize your choice, try again!")