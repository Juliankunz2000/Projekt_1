import random

questions_1 = ["Seine Mutter, die umarmt er - Seine Partnerin, die... ", 'Wen gewisse Umstände misstrauisch gemacht haben, der kommt zu der Vermutung „Hier ist etwas ...“?',
                "Was machen nicht nur Musiker, wenn sie jemanden scharf zurechtweisen?",
                "Geht die Amphibie reichlich resolut vor, dann ist ...?", 'Ein „Longsleeve“ kennt der Online-Duden als die langärmelige Version vom ...?',
                "Laut Statistischem Bundesamt wurden 2016 und 2020 an welchem Datum auffällig weniger Kinder geboren als im Schnitt?",
                "Bezogen auf die Mengenanteile der drei Hauptzutaten nennt man ...?", "Wer taucht seit dem 14. Januar 2024 vermehrt in den Schlagzeilen der internationalen Regenbogenpresse auf?",
                "In welcher Sportart müssen die Athleten die Wurfuhr im Blick haben?", "Mit wem hatten Paul Janke, Detlef Soost, Ingolf Lück, Pascal Hens und Bastian Bielendorfer nachweislich engen Körperkontakt?",
                'Ein eisernes Element mit sechs „Zähnen“, die für die sechs Stadtteile stehen sollen, befindet sich am ...?', "Einen praktischen Frunk findet man in vielen ...?",
                'In wessen Metier fällt die Fertigkeit, etwas fachgerecht „aus der Decke zu schlagen“?', "Was ist zuweilen mit einem Schlupfriemen ausgestattet?",
               'Wer bot einst über sein Weingut die Tropfen „Klöbener Krötenpfuhl“, „Oberföhringer Vogelspinne“ und „Hupfheimer Jungferngärtchen“ an?']
wrong_answers_1 = [["pfar er", "kardinn al", "passt or"], ["müde", "bequem", "träge"],
                    ["Standpunkt flöten", "Ansicht trommeln", "Auffassung orgeln"], ["die Kröte körte", "die Unke ukne", "der Salamander samalander"],
                    ["Cocktailkleid", "Hawaiihemd", "Büstenhalter"], ["29. April", "29. Juni", "29. August"], ["Rührei auch 1-2-3-Ei", "Grießbrei auch 1-2-3-Brei", "Glühwein auch 1-2-3-Wein"],
                    ["Andrea Doria", "Gorch Fock", "Santa Maria"], ["Handball", "Völkerball", "Fußball"], ["Evelyn Burdecki", "Laura Wontorra", "Verona Pooth"], ["Kühlergrill Londoner Taxis", "Kutschblock Wiener Fiaker", "Eingang zur Pariser Métro"],
                    ["E-Zahnbürsten", "E-Zigaretten", "E-Mails"], ["Konditor", "Bergmann", "Golfer"],
                    ["Automotoren", "Ruderboote", "Armbanduhren"], ["CDU", "DFB", "ADAC"]]
right_answers_1 = ["küsst er", "faul", "Meinung geigen", "der Frosch forsch", "T-Shirt", "29. Februar", "Mürbeteig auch 1-2-3-Teig", "Queen Mary", "Basketball",
                    "Ekaterina Leonova", "Bug venezianischer Gondeln", "E-Autos", "Weidmann", "Lederstiefel", "DRK"]


Kontostand = 0
Joker = 2
round = 1


# Ab hier

possible_choices = [wrong_answers_1[round-1][0], right_answers_1[round-1], wrong_answers_1[round-1][1],
                     wrong_answers_1[round-1][2]]


choice1 = random.choice(possible_choices)
index = possible_choices.index(choice1)
possible_choices.pop(index)
choice2 = random.choice(possible_choices)
index = possible_choices.index(choice2)
possible_choices.pop(index)
choice3 = random.choice(possible_choices)
index = possible_choices.index(choice3)
possible_choices.pop(index)
choice4 = random.choice(possible_choices)
index = possible_choices.index(choice4)
possible_choices.pop(index)

print(f"Frage {round}: " + questions_1[round-1])
print(f"A: {choice1}")
print(f"B: {choice2}")
print(f"C: {choice3}")
print(f"D: {choice4}")
print('Für den 50:50 Joker, gebe "x" ein!')

antwort = input("Gib hier deine Antwort ein: ")

if antwort == "A" and (choice1 == right_answers_1[round - 1]):
    print("Herzlichen Glückwunsch, die Antwort ist richtig!")
elif antwort == "B" and (choice2 == right_answers_1[round-1]):
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
elif antwort == "C" and (choice3 == right_answers_1[round-1]):
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
elif antwort == "D" and (choice4 == right_answers_1[round-1]):
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
elif antwort == "x":
    possible_choices = [wrong_answers_1[round-1][0], right_answers_1[round-1]]
    choice1 = random.choice(possible_choices)
    index = possible_choices.index(choice1)
    possible_choices.pop(index)
    choice2 = random.choice(possible_choices)
    index = possible_choices.index(choice2)
    possible_choices.pop(index)
    print(f"Frage {round}: " + questions_1[round - 1])
    print(f"A: {choice1}")
    print(f"B: {choice2}")
    antwort = input("Gib hier deine Antwort ein: ")
    if antwort == "A" and (choice1 == right_answers_1[round-1]):
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
    elif antwort == "B" and (choice2 == right_answers_1[round-1]):
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
    else:
        print("Die Antwort ist leider falsch!")
else:
    print("Die Antwort ist leider falsch!")





