import time
import random
import math
import copy
# import numpy
# import panda
import pygame
import ctypes
import _pickle
import os.path
import os

print("Loading... please wait. This may take a while.")
print("Please do not click on this window while the game is loading.")
pygame.init()


def new_game():
    save_data = {"Position": 4, "Party": [], "Name": "LordQuaggan"}
    save_data["Party"].append(
        Character(save_data["Name"], 1, 8, 8, 8, 8, 8, 8, [["Physical", "Melee", 2], ["Magical", "Ranged", 2]]))
    save_data["Party"].append(Character("WaterWizard", 1, 4, 8, 4, 12, 12, 10, [["Magical", "Ranged", 3]]))
    save_data["StoryProgress"] = {}
    save_data["Inventory"] = {}
    save_data["Inventory"]["HealthPotion"] = 1
    save_data["Inventory"]["Gold"] = 10
    temp_data = {"EncounterData": {}, "ActiveScreen": "Encounter"}
    temp_data["EncounterData"]["Type"] = "Dialogue"
    temp_data["EncounterData"]["Background"] = "BlankWhite"
    temp_data["EncounterData"]["Character"] = "None"
    temp_data["EncounterData"]["Dialogue"] = []
    temp_data["EncounterData"]["Dialogue"].append(
        ["A LOUD, FRANTIC KNOCK ON THE DOOR SUDDENLY WAKES YOU UP", ["GET OUT OF BED AND ANSWER IT", 2, ["Character","WaterWizard"]], ["COVER YOUR EARS WITH A PILLOW AND TRY TO GO BACK TO SLEEP", 1]])
    temp_data["EncounterData"]["Dialogue"].append(["THE KNOCKING INCREASES, IT'S NO USE", ["GIVE IN AND GET UP", 2, ["Character","WaterWizard"]], ["KEEP TRYING TO GO BACK TO SLEEP", 1]])
    temp_data["EncounterData"]["Dialogue"].append(["YOU OPEN THE DOOR TO SEE YOUR OLD FRIEND QUIN THE WATER MAGE.\nHE HAS BEEN MISSING FOR WEEKS", ["SAY HELLO", 3],["ASK HIM WHERE ON EARTH HE HAS BEEN! THE WHOLE TOWN HAS BEEN LOOKING FOR HIM!",4]])
    temp_data["EncounterData"]["Dialogue"].append(
        ["QUIN GREETS YOU CORDIALLY AND BEGINS HIS TALE", ["CONTINUE", 5]])
    temp_data["EncounterData"]["Dialogue"].append(
        ["QUIN SHUSHES YOU AND BEGINS HIS TALE", ["CONTINUE", 5]])
    temp_data["EncounterData"]["Dialogue"].append(
        ["'A MONTH AGO WHEN THE GREAT FOUNTAIN BROKE AND THE FLOW OF WATER STOPPED,\nI STARTED RESEARCHING EVERYTHING ABOUT THE ANCIENT OBJECT'", ["CONTINUE", 6]])
    temp_data["EncounterData"]["Dialogue"].append(
        ["'AS YOU HAVE NO DOUBT REALISED BY NOW, THIS TRAGEDY IS NO SIMPLE TRIFLE.\nSPEED WAS OF THE UTMOST IMPORTANCE, PEOPLE WERE ALREADY BEGINNING TO GO THIRSTY'",
            ["CONTINUE", 7]])
    temp_data["EncounterData"]["Dialogue"].append([
            "'SO, AS TIME WAS OF THE ESSENCE, I RAN TO THE GREAT LIBRARY\nAND SPENT A MONTH THERE RESEARCHING THIS PHENOMENON WHEN I FOUND THIS;'",
            ["LOOK CLOSER AT THE OBJECT HE IS HOLDING", 8],["ASK HIM TO GET TO THE POINT ALREADY",9]])
    temp_data["EncounterData"]["Dialogue"].append([
        "YOU SEE A BOOK WITH THE TITLE 'AQA REVISION GUIDE TO FOUNTAIN REPAIR' BRANDED ACROSS THE FRONT",
        ["ASK HIM TO CONTINUE WITH HIS TALE", 10], ["ASK HIM TO GET TO THE POINT ALREADY", 9]])
    temp_data["EncounterData"]["Dialogue"].append([
        "HE LOOKS AT YOU WITH A SLIGHTLY HURT EXPRESSION, AND THEN PROCEEDS TO GET TO THE POINT",
        ["PHEW", 10]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'ANYWAY, IN THIS BOOK IT STATES THAT TO REPAIR THE GREAT FOUNTAIN INSIDE THE PYRAMID OF LIFE,\nONE MUST COLLECT 4 JIGSAW PIECES AND COMBINE THEM'",
        ["'ASK HIM WHERE THESE JIGSAW PIECES ARE'", 11]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'WELL, TURNS OUT THE LOCATIONS OF THE JIGSAW PIECES WASN'T PART OF THE AQA SPEC,\nBUT LUCKILY THEY HAVE IT WRITTEN IN THIS OCR TEXTBOOK HERE'",
        ["REPEAT YOUR QUESTION", 12]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'OKAY, OKAY. THEY ARE HERE, HERE, HERE AND HERE.' HIS FINGER JABS AT TO PAGES SEEMINGLY RANDOMLY\nALL AROUND THE EDGES OF THE DESERT",
        ["ASK HIM WHY HE HASN'T ALREADY REPAIRED THE FOUNTAIN", 13],["ASK WHY HE CAME TO YOU",13]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'WELL...' HE LOOKS EMBARRASSED 'I WENT TO THE LOCATION AND WAS MET WITH A FEARSOME TROLL,\nWHO WAS NOT IN THE MOOD TO GIVE HIS PRECIOUS SHINY JIGSAW PIECE AWAY'",
        ["ASK HIM IF HE EXPECTS YOU TO HELP",14]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'WELL... I SUPPOSE... WELL YES, TO BE FRANK, I WAS CONSIDERING SETTING UP A GUILD'",
        ["SAY THAT SOUNDS LIKE A GREAT IDEA", 15],["SAY THAT SOUNDS LIKE A WASTE OF TIME, EFFORT AND MONEY",15]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'WELL, IN FACT, I ALREADY HAVE. I NAMED IT THE LEAGUE OF DOWSERS! I HAVE NO CHANCE OF PAYING OFF\nMY MAGI UNI DEBT NOW, BUT I THINK IT WAS WORTH IT, THAT IS, IF YOU WERE TO JOIN IT WOULD BE'",
        ["SAY THAT YOU WOULD BE HAPPY TO JOIN IN ON HIS QUEST", 16], ["ASK WHAT'S IN IT FOR YOU", 17]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'HURRAY! LET'S GO COLLECT SOME JIGSAW PIECES AND SAVE THE WORLD!'",
        ["EXIT", -1]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'NOT HAVING TO LIVE IN A DESERT@ NOT HAVING TO WORRY EVERY DAY\nIF THE SHIPMENTS OF WATER SUPPLIES HAVE GOTTEN LOST@ BEING A HERO@'",
        ["AGREE AND JOIN", 16],["DECLARE THAT YOU ARE STILL NOT CONVINCED",18]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'OKAY, YOU HAVE PUSHED ME THIS FAR, THAT'S IT. TIME TO BREAK THE FOURTH WALL;\nLOOK, YOU STARTED THIS GAME, IF YOU DIDN'T WANT TO PLAY IT, WHY DID THE HELL YOU CLICK RUN@'",
        ["AGREE AND JOIN (THIS IS THE ONLY OPTION, YOU TERRIBLE PERSON)", 16]])
    save_data, temp_data = init_encounter(save_data, temp_data)

    temp_data["EncounterContent"] = {}
    temp_data["EncounterContent"][3] = {}
    temp_data["EncounterContent"][3]["Type"] = "Dialogue"
    temp_data["EncounterContent"][3]["Background"] = "Town2"
    temp_data["EncounterContent"][3]["Character"] = "None"
    temp_data["EncounterContent"][3]["Dialogue"] = []
    temp_data["EncounterContent"][3]["Dialogue"].append(
        ["WELCOME TO THE VILLAGE OF TENAGRA", ["SHOPS", 1, ["Background", "Town"]], ["TAVERN", 2],
         ["LEAVE", -1]])
    temp_data["EncounterContent"][3]["Dialogue"].append(
        ["SHOPS ARE CLOSED RIGHT NOW, PLEASE COME BACK LATER", ["GO BACK", 0, ["Background", "Town2"]]])
    temp_data["EncounterContent"][3]["Dialogue"].append(
        ["TAVERN CLOSED RIGHT NOW, PLEASE COME BACK LATER", ["GO BACK", 0]])

    temp_data["EncounterContent"][4] = {}
    temp_data["EncounterContent"][4]["Type"] = "Dialogue"
    temp_data["EncounterContent"][4]["Background"] = "Town2"
    temp_data["EncounterContent"][4]["Character"] = "None"
    temp_data["EncounterContent"][4]["Dialogue"] = []
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["WELCOME TO THE VILLAGE OF NIBIRU", ["SHOPS", 1, ["Background", "Town"]], ["GUILD HALL", 2], ["TAVERN", 3],
         ["LEAVE", -1]])
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["SHOPS ARE CLOSED RIGHT NOW, PLEASE COME BACK LATER", ["GO BACK", 0, ["Background", "Town2"]]])
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["GUILD HALL IS UNDER REPAIRS, PLEASE COME BACK LATER", ["GO BACK", 0]])
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["TAVERN CLOSED RIGHT NOW, PLEASE COME BACK LATER", ["GO BACK", 0]])

    temp_data["EncounterContent"][5] = {}
    temp_data["EncounterContent"][5]["Type"] = "Dialogue"
    temp_data["EncounterContent"][5]["Background"] = "WaterfallDried"
    temp_data["EncounterContent"][5]["Character"] = "WaterWizard"
    temp_data["EncounterContent"][5]["Dialogue"] = []
    temp_data["EncounterContent"][5]["Dialogue"].append(
        [
            "YOU SEE A MAN CLAD IN BLUE ROBES STARING AT AN ANCIENT CLIFFSIDE, 'THERE USED TO BE A WATERFALL HERE YOU KNOW, SHAME HOW THINGS HAVE TURNED OUT'",
            ["'IT REALLY IS'", 1], ["'I HATE WATER'", -1],
            ["LEAVE", -1]])
    temp_data["EncounterContent"][5]["Dialogue"].append(
        ["'I HEARD A RUMOUR THAT A GUILD IS STARTING IN NIBIRU TO FIX THIS MESS'", ["'PERHAPS WE SHOULD JOIN'", 2],
         ["'YEAH I ACTUALLY PREFER THE SAND'", -1]])
    temp_data["EncounterContent"][5]["Dialogue"].append(
        ["'YEAH, I'LL MEET YOU BACK IN NIBIRU'", ["'I'LL SEE YOU THERE'", -1]])

    temp_data["EncounterContent"][6] = {}
    temp_data["EncounterContent"][6]["Type"] = "Dialogue"
    temp_data["EncounterContent"][6]["Background"] = "Town2"
    temp_data["EncounterContent"][6]["Character"] = "None"
    temp_data["EncounterContent"][6]["Dialogue"] = []
    temp_data["EncounterContent"][6]["Dialogue"].append(
        ["WELCOME TO THE VILLAGE OF LEDONIA", ["SHOPS", 1, ["Background", "Town"]], ["TAVERN", 2],
         ["LEAVE", -1]])
    temp_data["EncounterContent"][6]["Dialogue"].append(
        ["SHOPS ARE CLOSED RIGHT NOW, PLEASE COME BACK LATER", ["GO BACK", 0, ["Background", "Town2"]]])
    temp_data["EncounterContent"][6]["Dialogue"].append(
        ["TAVERN CLOSED RIGHT NOW, PLEASE COME BACK LATER", ["GO BACK", 0]])

    temp_data["EncounterContent"]["RandomEncounters"]=[]
    temp_data["EncounterContent"]["RandomEncounters"].append({})
    temp_data["EncounterContent"]["RandomEncounters"][0]["Type"] = "Battle"
    temp_data["EncounterContent"]["RandomEncounters"][0]["EnemyParty"] = []
    temp_data["EncounterContent"]["RandomEncounters"][0]["EnemyParty"].append(
        Character("Goblin", 1, 8, 4, 10, 2, 2, 6, [["Physical", "Melee", 1]]))
    temp_data["EncounterContent"]["RandomEncounters"][0]["EnemyParty"].append(
        Character("Goblin", 1, 8, 4, 10, 2, 2, 6, [["Physical", "Melee", 1]]))
    temp_data["EncounterContent"]["RandomEncounters"][0]["EnemyParty"].append(
        Character("Goblin", 1, 8, 4, 10, 2, 2, 6, [["Physical", "Melee", 1]]))

    temp_data["PositionData"] = []
    temp_data["PositionData"].append([[43, 125], [-1, 2, 3, -1]])  # Links are done up down left right -1 means no link
    temp_data["PositionData"].append([[122, 229], [-1, -1, 2, -1]])
    temp_data["PositionData"].append([[144, 152], [1, 4, 3, 0]])
    temp_data["PositionData"].append([[173, 40], [2, -1, -1, 0]])
    temp_data["PositionData"].append([[224, 229], [-1, 5, -1, 2]])
    temp_data["PositionData"].append([[319, 184], [-1, 8, 7, 4]])
    temp_data["PositionData"].append([[321, 22], [7, -1, -1, -1]])
    temp_data["PositionData"].append([[365, 104], [5, 8, 6, -1]])
    temp_data["PositionData"].append([[394, 162], [-1, -1, 7, 5]])
    temp_data["AnimateTick"] = 0
    temp_data["Moving"] = [False, 0, 0]
    save_data["Encounters"] = []
    temp_data["Airships"] = []
    to_delete = []
    for i in range(0, 5):
        save_data["Encounters"].append([random.randint(0, len(temp_data["PositionData"]) - 1), -1])
        while save_data["Encounters"][i][1] == -1:
            save_data["Encounters"][i][1] = random.choice(temp_data["PositionData"][save_data["Encounters"][i][0]][1])
        for i2 in range(0, i):
            if save_data["Encounters"][i2] == save_data["Encounters"][i]:
                to_delete.append(i)
    for i in range(0, len(to_delete)):
        if len(save_data["Encounters"])>0:
            save_data["Encounters"].pop(to_delete[i] - i)
    return save_data, temp_data


class DisplayManager:
    def __init__(self):
        self.Images = {}
        ctypes.windll.user32.SetProcessDPIAware()
        self.ScreenRes = (1920, 1080)
        self.Window = pygame.display.set_mode(self.ScreenRes, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.GameRes = (480, 270)
        self.ResRatio = (self.ScreenRes[0] // self.GameRes[0], self.ScreenRes[1] // self.GameRes[1])

    def load_images(self):
        for Image in os.listdir("Images"):
            self.Images[Image[:-4]] = pygame.image.load(r"Images\{0}".format(Image)).convert_alpha()
            self.Images[Image[:-4]] = pygame.transform.scale(self.Images[Image[:-4]],
                                                             (self.Images[Image[:-4]].get_size()[0] * self.ResRatio[0],
                                                              self.Images[Image[:-4]].get_size()[1] * self.ResRatio[1]))

    def place_image(self, image_id, x, y, *x_flip):
        if x_flip == ():
            x_flip = False
        if image_id in self.Images.keys():
            y = self.GameRes[1] - y - (self.Images[image_id].get_size()[1] / self.ResRatio[1])
            if x_flip:
                self.Window.blit(pygame.transform.flip(self.Images[image_id], True, False), (int(x) * self.ResRatio[0],
                                                                                             int(y) * self.ResRatio[1]))
            else:
                self.Window.blit(self.Images[image_id],
                                 (int(x) * self.ResRatio[0], int(y) * self.ResRatio[1]))
        else:
            print(
                "ERROR: Image " + image_id + " has not been loaded. Make sure you have placed the image in the images "
                                             "folder and spelt the file name correctly.")

    def place_text(self, text, x, y):
        x2 = x
        for Letter in text:
            if Letter in self.Images.keys():
                y2 = self.GameRes[1] - y - (self.Images[Letter].get_size()[1] / self.ResRatio[1])
                self.Window.blit(self.Images[Letter], (round(x2) * self.ResRatio[0], round(y2) * self.ResRatio[1]))
                x2 += (self.Images[Letter].get_size()[0] / self.ResRatio[0]) + 1
            elif Letter == "\n":
                y += -6
                x2 = x
            elif Letter == " ":
                x2 += 4
            else:
                print(
                    "ERROR: Character " + Letter + " has not been loaded. Make sure the character is "
                                                   "present in the images folder.")

    def place_rectangle(self, colour, x, y, width, height):
        y = self.GameRes[1] - y - height
        pygame.draw.rect(self.Window, colour,
                         (int(x) * self.ResRatio[0], int(y) * self.ResRatio[1], int(width) * self.ResRatio[0],
                          int(height) * self.ResRatio[1]))

    def update(self):
        pygame.event.get()
        pygame.display.update()
        self.place_image("Blank", 0, 0)


class SoundManager:
    def __init__(self):
        self.Sounds = {}
        pygame.mixer.set_num_channels(4)

    def load_sounds(self):
        for Sound in os.listdir("Sounds"):
            self.Sounds[Sound[:-4]] = pygame.mixer.Sound(r"Sounds\{0}".format(Sound))

    def play_sound(self, sound_id, loops):
        if sound_id in self.Sounds.keys():
            self.Sounds[sound_id].play(loops=loops)
        else:
            print(
                "ERROR: Sound " + sound_id + " has not been loaded. Make sure you have placed the sound in "
                                             "the sounds folder and spelt the file name correctly.")

    @staticmethod
    def stop_sounds():
        pygame.mixer.stop()


class Character:
    def __init__(self, name, level, strength, constitution, dexterity, intelligence, wisdom, charisma, attacks):
        self.name = name
        self.level = level
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.attacks = attacks
        # Initialises variables to be set in update_stats to prevent pycharm from having a fit
        self.mods = {}
        self.health_max = 0
        self.dodge_bonus = 0
        self.attack_bonus = 0
        self.spell_bonus = 0
        self.stamina_max = 0
        self.stamina_regen = 0
        self.mana_max = 0
        self.mana_regen = 0
        self.health_current = 0
        self.stamina_current = 0
        self.mana_current = 0
        self.initiative_bonus=0
        self.unspent_points=-5
        self.lvl_up()

    def lvl_up(self):
        self.unspent_points+=5
        self.mods = {"Strength": self.strength // 4,
                     "Constitution": self.constitution // 4,
                     "Dexterity": self.dexterity // 4,
                     "Intelligence": self.intelligence // 4,
                     "Wisdom": self.wisdom // 4,
                     "Charisma": self.charisma // 4}
        self.health_max = (self.mods["Constitution"] + 10 + (self.mods["Constitution"] + 5) * (self.level - 1))
        self.dodge_bonus = self.mods["Dexterity"] + 10
        self.attack_bonus = (self.mods["Dexterity"] * 2)
        self.spell_bonus = (self.mods["Charisma"] * 2)
        self.stamina_max = self.level * 10 + self.mods["Strength"] * 5
        self.stamina_regen = self.level + self.mods["Constitution"] * 2
        self.mana_max = self.level * 10 + self.mods["Wisdom"] * 5
        self.mana_regen = self.level + self.mods["Intelligence"] * 2
        self.health_current = self.health_max
        self.stamina_current = self.stamina_max
        self.mana_current = self.mana_max
        self.initiative_bonus=self.mods["Dexterity"]*5+self.mods["Charisma"]*2


def save(data):
    _pickle.dump(data, open(r"Saves\SaveFile.sav", "wb"))


def load():
    for SaveFile in os.listdir("Saves"):
        save_data = _pickle.load(open(r"Saves\{0}".format(SaveFile), "rb"))
        return save_data
    print("ERROR: save file not present")
    return "ERROR"


def overworld(screen, mixer, save_data, temp_data):
    temp_data["ActiveScreen"] = "Overworld"
    temp_data["EncounterData"] = None
    screen.place_image("Map", 0, 0)
    if not temp_data["Moving"][0]:
        screen.place_image("Flag2", temp_data["PositionData"][save_data["Position"]][0][0],
                           temp_data["PositionData"][save_data["Position"]][0][1])
        input_keys = pygame.key.get_pressed()
        if input_keys[pygame.K_w] and not (temp_data["PositionData"][save_data["Position"]][1][0] == -1):
            mixer.play_sound("ExampleSound", 0)
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][0]
        elif input_keys[pygame.K_d] and not (temp_data["PositionData"][save_data["Position"]][1][1] == -1):
            mixer.play_sound("ExampleSound", 0)
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][1]
        elif input_keys[pygame.K_s] and not (temp_data["PositionData"][save_data["Position"]][1][2] == -1):
            mixer.play_sound("ExampleSound", 0)
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][2]
        elif input_keys[pygame.K_a] and not (temp_data["PositionData"][save_data["Position"]][1][3] == -1):
            mixer.play_sound("ExampleSound", 0)
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][3]
        elif input_keys[pygame.K_SPACE]:
            mixer.play_sound("ExampleSound", 0)
            try:
                temp_data["EncounterData"] = copy.deepcopy(temp_data["EncounterContent"][save_data["Position"]])
                save_data, temp_data = init_encounter(save_data, temp_data)
            except KeyError:
                pass
        elif input_keys[pygame.K_i]:
            temp_data["ActiveScreen"] = "Inventory"
            while input_keys[pygame.K_i]:
                screen.update()
                input_keys = pygame.key.get_pressed()
        elif input_keys[pygame.K_ESCAPE]:
            temp_data["ActiveScreen"] = "Settings"
            while input_keys[pygame.K_ESCAPE]:
                screen.update()
                input_keys = pygame.key.get_pressed()
    else:
        if temp_data["Moving"][2] == 30:
            save_data["Position"] = temp_data["Moving"][1]
            temp_data["Moving"] = [False, 0, 0]
        elif temp_data["Moving"][2]==15:
            for temp_encounter in save_data["Encounters"]:
                if temp_data["Moving"][1] in temp_encounter and save_data["Position"] in temp_encounter:
                    temp_data["EncounterData"]=copy.deepcopy(random.choice(temp_data["EncounterContent"]["RandomEncounters"]))
                    save_data, temp_data = init_encounter(save_data, temp_data)
                    save_data["Encounters"].remove(temp_encounter)
        if not temp_data["ActiveScreen"]=="Encounter" and temp_data["Moving"][0]:
            temp_data["Moving"][2] += 1
            screen.place_image("Flag2",
                               (temp_data["PositionData"][temp_data["Moving"][1]][0][0] * (temp_data["Moving"][2]) +
                                temp_data["PositionData"][save_data["Position"]][0][0] * (
                                        30 - temp_data["Moving"][2])) / 30,
                               (temp_data["PositionData"][temp_data["Moving"][1]][0][1] * (temp_data["Moving"][2]) +
                                temp_data["PositionData"][save_data["Position"]][0][1] * (
                                        30 - temp_data["Moving"][2])) / 30)
    for temp_encounter in save_data["Encounters"]:
        screen.place_image("Alert1", (temp_data["PositionData"][temp_encounter[0]][0][0] +
                                      temp_data["PositionData"][temp_encounter[1]][0][0]) / 2 - 1,
                           (temp_data["PositionData"][temp_encounter[0]][0][1] +
                            temp_data["PositionData"][temp_encounter[1]][0][1]) / 2 + 6 + math.sin(
                               temp_data["AnimateTick"] / 35) * -0.9)
        screen.place_image("Alert2", (temp_data["PositionData"][temp_encounter[0]][0][0] +
                                      temp_data["PositionData"][temp_encounter[1]][0][0]) / 2,
                           (temp_data["PositionData"][temp_encounter[0]][0][1] +
                            temp_data["PositionData"][temp_encounter[1]][0][1]) / 2)
    if random.randint(0, 2500) == 0:
        temp_data["Airships"].append([-20, random.randint(0, 270)])
    to_delete = []
    for AirshipNum in range(0, len(temp_data["Airships"])):
        screen.place_image("Airship", temp_data["Airships"][AirshipNum][0], temp_data["Airships"][AirshipNum][1])
        temp_data["Airships"][AirshipNum][0] += 0.2
        if temp_data["Airships"][AirshipNum][0] > 500:
            to_delete.append(AirshipNum)
    for i in to_delete:
        temp_data["Airships"].pop(i)
    return save_data, temp_data


def init_encounter(save_data, temp_data):
    temp_data["ActiveScreen"] = "Encounter"
    if temp_data["EncounterData"]["Type"] == "Battle":
        temp_data["EncounterData"]["Turn"] = 0
        temp_data["EncounterData"]["UIPos"] = 0
        temp_data["EncounterData"]["Selection"] = {"Attack": 0, "Enemy": 0}
        temp_data["EncounterData"]["AttackAnimProg"] = 0
    elif temp_data["EncounterData"]["Type"] == "Dialogue":
        temp_data["PageNumber"] = 0
    return save_data, temp_data


def encounter(screen, mixer, save_data, temp_data):
    if temp_data["EncounterData"]["Type"] == "Battle":
        screen.place_image("EncounterBack", 0, 0)
        for i in range(len(save_data["Party"]) - 1, -1, -1):
            if not (temp_data["EncounterData"]["AttackAnimProg"] > 0 and temp_data["EncounterData"]["Turn"] == i):
                if not save_data["Party"][i].name == save_data["Name"]:
                    screen.place_image(save_data["Party"][i].name,
                                       i * 30 + 40,
                                       i * 60 + 40)
                else:
                    screen.place_image("Spellsword",
                                       i * 30 + 40,
                                       i * 60 + 40)
                offset = 0
                screen.place_rectangle((0, 0, 0), i * 30 + 40, i * 60 + 120, 48, 5)
                screen.place_rectangle((255, 0, 0), i * 30 + 40, i * 60 + 120, (save_data["Party"][i].health_current /
                                                                                save_data["Party"][i].health_max) * 48,
                                       5)
                offset += 6
                physical = False
                magical = False
                for Attack in save_data["Party"][i].attacks:
                    if "Physical" in Attack:
                        physical = True
                    elif "Magical" in Attack:
                        magical = True
                if physical:
                    screen.place_rectangle((0, 0, 0), i * 30 + 40, i * 60 + 120 - offset, 48, 5)
                    screen.place_rectangle((0, 255, 0), i * 30 + 40, i * 60 + 120 - offset,
                                           (save_data["Party"][i].stamina_current /
                                            save_data["Party"][i].stamina_max) * 48, 5)
                    offset += 6
                if magical:
                    screen.place_rectangle((0, 0, 0), i * 30 + 40, i * 60 + 120 - offset, 48, 5)
                    screen.place_rectangle((0, 0, 255), i * 30 + 40, i * 60 + 120 - offset,
                                           (save_data["Party"][i].mana_current /
                                            save_data["Party"][i].mana_max) * 48, 5)
                    offset += 6
            else:
                if save_data["Party"][i].attacks[temp_data["EncounterData"]["Selection"]["Attack"]][1] == "Melee":
                    if not save_data["Party"][i].name == save_data["Name"]:
                        screen.place_image(save_data["Party"][i].name,
                                           ((i * 30 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                            ((temp_data["EncounterData"]["Selection"]["Enemy"]) * -30 + 400) *
                                            temp_data["EncounterData"][
                                                "AttackAnimProg"]) / 30,
                                           ((i * 60 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                            (temp_data["EncounterData"]["Selection"]["Enemy"] * 60 + 40) *
                                            temp_data["EncounterData"][
                                                "AttackAnimProg"]) / 30)
                    else:
                        screen.place_image("Spellsword",
                                           ((i * 30 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                            ((temp_data["EncounterData"]["Selection"]["Enemy"]) * -30 + 400) *
                                            temp_data["EncounterData"][
                                                "AttackAnimProg"]) / 30,
                                           ((i * 60 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                            ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 60 + 40) *
                                            temp_data["EncounterData"][
                                                "AttackAnimProg"]) / 30)
                else:
                    if not save_data["Party"][i].name == save_data["Name"]:
                        screen.place_image(save_data["Party"][i].name,
                                           i * 30 + 40,
                                           i * 60 + 40)
                    else:
                        screen.place_image("Spellsword",
                                           i * 30 + 40,
                                           i * 60 + 40)
                    screen.place_image("ProjectileMagic",
                                       ((i * 30 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * -30 + 400) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,
                                       ((i * 60 + 64) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 60 + 64) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30)
        for i in range(len(temp_data["EncounterData"]["EnemyParty"]) - 1, -1, -1):
            if not (temp_data["EncounterData"]["AttackAnimProg"] > 0 and temp_data["EncounterData"]["Turn"] - len(
                    save_data["Party"]) == i):
                screen.place_image(temp_data["EncounterData"]["EnemyParty"][i].name,
                                   i * - 30 + 400,
                                   i * 60 + 40, True)
                offset = 0
                screen.place_rectangle((0, 0, 0), i * -30 + 400, i * 60 + 120 - offset, 48, 5)
                screen.place_rectangle((255, 0, 0), i * -30 + 400, i * 60 + 120 - offset,
                                       (temp_data["EncounterData"]["EnemyParty"][i].health_current /
                                        temp_data["EncounterData"]["EnemyParty"][i].health_max) * 48, 5)
                offset += 6
                physical = False
                magical = False
                for Attack in temp_data["EncounterData"]["EnemyParty"][i].attacks:
                    if "Physical" in Attack:
                        physical = True
                    elif "Magical" in Attack:
                        magical = True
                if physical:
                    screen.place_rectangle((0, 0, 0), i * -30 + 400, i * 60 + 120 - offset, 48, 5)
                    screen.place_rectangle((0, 255, 0), i * -30 + 400, i * 60 + 120 - offset,
                                           (temp_data["EncounterData"]["EnemyParty"][i].stamina_current /
                                            temp_data["EncounterData"]["EnemyParty"][i].stamina_max) * 48, 5)
                    offset += 6
                if magical:
                    screen.place_rectangle((0, 0, 0), i * -30 + 400, i * 60 + 120 - offset, 48, 5)
                    screen.place_rectangle((0, 0, 255), i * -30 + 400, i * 60 + 120 - offset,
                                           (temp_data["EncounterData"]["EnemyParty"][i].mana_current /
                                            temp_data["EncounterData"]["EnemyParty"][i].mana_max) * 48, 5)
                    offset += 6
            else:
                if temp_data["EncounterData"]["EnemyParty"][i].attacks[
                    temp_data["EncounterData"]["Selection"]["Attack"]][1] == "Melee":
                    screen.place_image(temp_data["EncounterData"]["EnemyParty"][i].name,
                                       ((i * -30 + 400) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 30 + 40) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,
                                       ((i * 60 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        (temp_data["EncounterData"]["Selection"]["Enemy"] * 60 + 40) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,True)
                else:
                    screen.place_image(temp_data["EncounterData"]["EnemyParty"][i].name,
                                       i * - 30 + 400,
                                       i * 60 + 40, True)
                    screen.place_image("ProjectileMagic",
                                       ((i * -30 + 400) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 30 + 40) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,
                                       ((i * 60 + 64) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        (temp_data["EncounterData"]["Selection"]["Enemy"] * 60 + 64) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30, True)
        if temp_data["EncounterData"]["Turn"] < len(save_data["Party"]) and temp_data["EncounterData"][
            "AttackAnimProg"] == 0:
            if temp_data["EncounterData"]["UIPos"] == 0:
                for OptionNum in range(0, len(save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks)):
                    screen.place_text(str(OptionNum + 1) + "; " +
                                      save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[OptionNum][
                                          0].upper() + " " +
                                      save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[OptionNum][
                                          1].upper() + " (" +
                                      str(save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[OptionNum][
                                              2]) + " " +
                                      "DMG)", 10,
                                      30 - OptionNum * 10)
                    input_keys = pygame.key.get_pressed()
                    if input_keys[pygame.K_1] and len(
                            save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks) > 0:
                        temp_data["EncounterData"]["Selection"]["Attack"] = 0
                        temp_data["EncounterData"]["UIPos"] += 1
                        mixer.play_sound("ExampleSound", 0)
                    elif input_keys[pygame.K_2] and len(
                            save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks) > 1:
                        temp_data["EncounterData"]["Selection"]["Attack"] = 1
                        temp_data["EncounterData"]["UIPos"] += 1
                        mixer.play_sound("ExampleSound", 0)
                    elif input_keys[pygame.K_3] and len(
                            save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks) > 2:
                        temp_data["EncounterData"]["Selection"]["Attack"] = 2
                        temp_data["EncounterData"]["UIPos"] += 1
                        mixer.play_sound("ExampleSound", 0)
                    while input_keys[pygame.K_1] or input_keys[pygame.K_2] or input_keys[pygame.K_3]:
                        input_keys = pygame.key.get_pressed()
                        pygame.event.get()
            elif temp_data["EncounterData"]["UIPos"] == 1:
                for OptionNum in range(0, len(temp_data["EncounterData"]["EnemyParty"])):
                    screen.place_text(str(OptionNum + 1) + "; " +
                                      temp_data["EncounterData"]["EnemyParty"][OptionNum].name.upper() + " (" + str(
                        temp_data["EncounterData"]["EnemyParty"][OptionNum].health_current) + " HP)", 10,
                                      30 - OptionNum * 10)
                input_keys = pygame.key.get_pressed()
                if input_keys[pygame.K_1] and len(temp_data["EncounterData"]["EnemyParty"]) > 0:
                    temp_data["EncounterData"]["Selection"]["Enemy"] = 0
                    temp_data["EncounterData"]["UIPos"] = 0
                    temp_data["EncounterData"]["AttackAnimProg"] = 1
                    mixer.play_sound("ExampleSound", 0)
                elif input_keys[pygame.K_2] and len(temp_data["EncounterData"]["EnemyParty"]) > 1:
                    temp_data["EncounterData"]["Selection"]["Enemy"] = 1
                    temp_data["EncounterData"]["UIPos"] = 0
                    temp_data["EncounterData"]["AttackAnimProg"] = 1
                    mixer.play_sound("ExampleSound", 0)
                elif input_keys[pygame.K_3] and len(temp_data["EncounterData"]["EnemyParty"]) > 2:
                    temp_data["EncounterData"]["Selection"]["Enemy"] = 2
                    temp_data["EncounterData"]["UIPos"] = 0
                    temp_data["EncounterData"]["AttackAnimProg"] = 1
                    mixer.play_sound("ExampleSound", 0)
        elif temp_data["EncounterData"]["AttackAnimProg"] == 0:
            temp_data["EncounterData"]["Selection"]["Enemy"]=random.randrange(0,len(save_data["Party"]))
            temp_data["EncounterData"]["Selection"]["Attack"] = random.randrange(
                0, len(temp_data["EncounterData"]["EnemyParty"][
                           temp_data["EncounterData"]["Turn"]-len(save_data["Party"])].attacks))
            temp_data["EncounterData"]["AttackAnimProg"] = 1
        else:
            if temp_data["EncounterData"]["AttackAnimProg"] < 30:
                temp_data["EncounterData"]["AttackAnimProg"] += 1
            else:
                temp_data["EncounterData"]["AttackAnimProg"] = 0
                if temp_data["EncounterData"]["Turn"]<len(save_data["Party"]):
                    temp_data["EncounterData"]["EnemyParty"][
                        temp_data["EncounterData"]["Selection"]["Enemy"]].health_current-=\
                        save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[
                            temp_data["EncounterData"]["Selection"]["Attack"]][2]
                    if temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current<=0:
                        temp_data["EncounterData"]["EnemyParty"].pop(temp_data["EncounterData"]["Selection"]["Enemy"])
                        if len(temp_data["EncounterData"]["EnemyParty"])<1:
                            temp_data["ActiveScreen"]="Overworld"
                else:
                    save_data["Party"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current-=\
                        temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Turn"]-len(
                            save_data["Party"])].attacks[
                            temp_data["EncounterData"]["Selection"]["Attack"]][2]
                    if save_data["Party"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current<=0:
                        save_data["Party"].pop(temp_data["EncounterData"]["Selection"]["Enemy"])
                        if len(save_data["Party"]) < 1:
                            pygame.quit()
                            while True:
                                pass
                temp_data["EncounterData"]["Turn"] += 1
                if temp_data["EncounterData"]["Turn"] > len(
                        save_data["Party"]) + len(temp_data["EncounterData"]["EnemyParty"])-1:
                    temp_data["EncounterData"]["Turn"] = 0
    #
    #
    # Non-battle code
    elif temp_data["EncounterData"]["Type"] == "Dialogue":
        screen.place_image(temp_data["EncounterData"]["Background"], 0, 0)
        if not temp_data["EncounterData"]["Character"] == "None":
            screen.place_image(temp_data["EncounterData"]["Character"], 50, 100)
        if not temp_data["PageNumber"] == -1:
            screen.place_text(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][0], 10, 80)
            for OptionNum in range(0, len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) - 1):
                screen.place_text(str(OptionNum + 1) + "; " +
                                  temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][OptionNum + 1][0], 10,
                                  60 - OptionNum * 10)
        else:
            temp_data["ActiveScreen"] = "Overworld"
            return save_data, temp_data
        input_keys = pygame.key.get_pressed()
        if input_keys[pygame.K_1] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 1:
            if len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][1]) > 2:
                for i in range(2, len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][1])):
                    temp_data["EncounterData"][
                        temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][1][i][0]] = temp_data[
                        "EncounterData"]["Dialogue"][temp_data["PageNumber"]][1][i][1]
            temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][1][1]
            mixer.play_sound("ExampleSound", 0)
        elif input_keys[pygame.K_2] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 2:
            if len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2]) > 2:
                for i in range(2, len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2])):
                    temp_data["EncounterData"][
                        temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2][i][0]] = [
                        temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2][i][1]]
            temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2][1]
            mixer.play_sound("ExampleSound", 0)
        elif input_keys[pygame.K_3] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 3:
            if len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3]) > 2:
                for i in range(2, len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3])):
                    if temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][0] in temp_data[
                        "EncounterData"].keys():
                        temp_data["EncounterData"][
                            temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][0]] = [
                            temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][1]]
                    elif temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][0] in save_data.keys():
                        if temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][0] == "Inventory":
                            if temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][1] in save_data[
                                "Inventory"].keys():
                                save_data["Inventory"][temp_data["EncounterData"]["Dialogue"][
                                    temp_data["PageNumber"]][3][i][1]] += temp_data["EncounterData"][
                                    "Dialogue"][temp_data["PageNumber"]][3][i][2]
                        elif temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][0]=="Party":
                            if  temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][1]=="health_current":
                                for i2 in range(0,len(save_data["Party"])):
                                    save_data["Party"][i2].health_current=temp_data["EncounterData"][
                                    "Dialogue"][temp_data["PageNumber"]][3][i][2]
                            elif  temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][1]=="stamina_current":
                                for i2 in range(0,len(save_data["Party"])):
                                    save_data["Party"][i2].stamina_current=temp_data["EncounterData"][
                                    "Dialogue"][temp_data["PageNumber"]][3][i][2]
                            elif  temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][1]=="mana_current":
                                for i2 in range(0,len(save_data["Party"])):
                                    save_data["Party"][i2].mana_current=temp_data["EncounterData"][
                                    "Dialogue"][temp_data["PageNumber"]][3][i][2]
                        else:
                            save_data[
                                temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][0]] = [
                                temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][i][1]]
            temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][1]
            mixer.play_sound("ExampleSound", 0)
        elif input_keys[pygame.K_4] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 4:
            if len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4]) > 2:
                for i in range(2, len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4])):
                    temp_data["EncounterData"][
                        temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4][i][0]] = [
                        temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4][i][1]]
            temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4][1]
            mixer.play_sound("ExampleSound", 0)
        while input_keys[pygame.K_1] or input_keys[pygame.K_2] or input_keys[pygame.K_3] or input_keys[pygame.K_4]:
            input_keys = pygame.key.get_pressed()
            pygame.event.get()
    return save_data, temp_data


def inventory(screen, mixer, save_data, temp_data):
    screen.place_image("BlankWhite", 0, 0)
    input_keys = pygame.key.get_pressed()
    for i in range(0,len(save_data["Party"])):
        offset=0
        screen.place_text(save_data["Party"][i].name.upper()+";",20+i*110,250+offset)
        offset+=20
        screen.place_text(str("LVL "+str(save_data["Party"][i].level)), 20+i*110,250-offset)
        if not save_data["Party"][i].name==save_data["Name"]:
            screen.place_image(save_data["Party"][i].name,20+i*110,250-offset-70)
        else:
            screen.place_image("Spellsword", 20+i*110, 250 - offset-70)
        offset+=80
        screen.place_text(str(save_data["Party"][i].health_current)+" OUT OF "+str(save_data["Party"][i].health_max)+" HP", 20+i*110,250-offset)
        physical = False
        magical = False
        for Attack in save_data["Party"][i].attacks:
            if "Physical" in Attack:
                physical = True
            elif "Magical" in Attack:
                magical = True
        if physical:
            offset+=10
            screen.place_text(
                str(save_data["Party"][i].stamina_current) + " OUT OF " + str(save_data["Party"][i].stamina_max) + " STAMINA",
                20+i*110, 250 - offset)
        if magical:
            offset += 10
            screen.place_text(
                str(save_data["Party"][i].mana_current) + " OUT OF " + str(save_data["Party"][i].mana_max) + " MANA",
                20+i*110, 250 - offset)
        offset=150
        screen.place_text(str(save_data["Party"][i].initiative_bonus) + " INITIATIVE BONUS",20+i*110, 250 - offset)
        offset+=10
        if physical:
            screen.place_text(str(save_data["Party"][i].attack_bonus) + " PHYSICAL BONUS", 20+i*110, 250 - offset)
            offset += 10
        if magical:
            screen.place_text(str(save_data["Party"][i].spell_bonus) + " MAGIC BONUS", 20+i*110, 250 - offset)
            offset += 10
        screen.place_text(str(save_data["Party"][i].initiative_bonus) + " DODGE BONUS", 20+i*110, 250 - offset)
    if input_keys[pygame.K_i]:
        temp_data["ActiveScreen"] = "Overworld"
        while input_keys[pygame.K_i]:
            screen.update()
            input_keys = pygame.key.get_pressed()
    return save_data, temp_data


def settings(screen, mixer, save_data, temp_data):
    screen.place_image("Blank", 0, 0)
    input_keys = pygame.key.get_pressed()
    screen.update()
    if input_keys[pygame.K_ESCAPE]:
        temp_data["ActiveScreen"] = "Overworld"
        while input_keys[pygame.K_ESCAPE]:
            screen.update()
            input_keys = pygame.key.get_pressed()
    return save_data, temp_data


def main():
    screen = DisplayManager()
    screen.load_images()
    mixer = SoundManager()
    mixer.load_sounds()
    mixer.play_sound("DesertTheme1", -1)
    save_data, temp_data = new_game()
    while True:
        frame_time = time.time()
        if temp_data["ActiveScreen"] == "Encounter":
            save_data, temp_data = encounter(screen, mixer, save_data, temp_data)
        elif temp_data["ActiveScreen"] == "Inventory":
            save_data, temp_data = inventory(screen, mixer, save_data, temp_data)
        elif temp_data["ActiveScreen"] == "Overworld":
            save_data, temp_data = overworld(screen, mixer, save_data, temp_data)
        elif temp_data["ActiveScreen"] == "Settings":
            save_data, temp_data = settings(screen, mixer, save_data, temp_data)
        else:
            print("ERROR: Active screen is set to " + temp_data["ActiveScreen"] + " which does not exist")
        temp_data["AnimateTick"] += 1
        screen.update()
        if frame_time + 0.016 > time.time():
            time.sleep(0.017 - (time.time() - frame_time))


main()
