import json
Alien_Dictionary = {
    "Moodi" : "Terrorist",
    "Sharma": "Cry",
    "Niazi" : "Revenge",
    "Zoordali" : "Corrupt",
    "Haramkhor" : "Afghani",
    "Lala" : "Laugh",
    "Sulu" : "Sit",
    "Woluo" : "Wait",
    "Lulo" : "Listen",
    "Wowo" : "What",
    "Hio" : "Hi",
    "Sosu" : "Salam"
}
def write_to_json():
    with open("Alien_Dict.json","w") as f:
        json.dump(Alien_Dictionary, f)
write_to_json()