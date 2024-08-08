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


Kontostand_liste = [0, 50, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 500000, 1000000]
Joker = 2
round = 1


def Runde():
    possible_choices = [wrong_answers_1[round - 1][0], right_answers_1[round - 1], wrong_answers_1[round - 1][1],
                        wrong_answers_1[round - 1][2]]

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

    print(f"Frage {round}: " + questions_1[round - 1])
    print("--------------------------------------------------------------------------------------------")
    print(f"A: {choice1}")
    print(f"B: {choice2}")
    print(f"C: {choice3}")
    print(f"D: {choice4}")
    print("--------------------------------------------------------------------------------------------")
    print('Für den 50:50 Joker, gebe "x" ein!')
    print("--------------------------------------------------------------------------------------------")

    antwort = input("Gib hier deine Antwort ein: ")

    if antwort == "A" and (choice1 == right_answers_1[round - 1]):
        print("--------------------------------------------------------------------------------------------")
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
        return "ro"
    elif antwort == "B" and (choice2 == right_answers_1[round - 1]):
        print("--------------------------------------------------------------------------------------------")
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
        return "ro"
    elif antwort == "C" and (choice3 == right_answers_1[round - 1]):
        print("--------------------------------------------------------------------------------------------")
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
        return "ro"
    elif antwort == "D" and (choice4 == right_answers_1[round - 1]):
        print("--------------------------------------------------------------------------------------------")
        print("Herzlichen Glückwunsch, die Antwort ist richtig!")
        return "ro"
    elif antwort == "x" and (Joker > 0):
        possible_choices = [wrong_answers_1[round - 1][0], right_answers_1[round - 1]]
        choice1 = random.choice(possible_choices)
        index = possible_choices.index(choice1)
        possible_choices.pop(index)
        choice2 = random.choice(possible_choices)
        index = possible_choices.index(choice2)
        possible_choices.pop(index)
        print("--------------------------------------------------------------------------------------------")
        print(f"Frage {round}: " + questions_1[round - 1])
        print("--------------------------------------------------------------------------------------------")
        print(f"A: {choice1}")
        print(f"B: {choice2}")
        print("--------------------------------------------------------------------------------------------")
        antwort = input("Gib hier deine Antwort ein: ")
        if antwort == "A" and (choice1 == right_answers_1[round - 1]):
            print("--------------------------------------------------------------------------------------------")
            print("Herzlichen Glückwunsch, die Antwort ist richtig!")
            return "rm"
        elif antwort == "B" and (choice2 == right_answers_1[round - 1]):
            print("--------------------------------------------------------------------------------------------")
            print("Herzlichen Glückwunsch, die Antwort ist richtig!")
            return "rm"
        else:
            print("--------------------------------------------------------------------------------------------")
            print("Die Antwort ist leider falsch!")
            return "v"
    elif antwort == "x" and (Joker <= 0):
        print("--------------------------------------------------------------------------------------------")
        print("Du hast keinen Joker mehr!")
        return "v"
    else:
        print("--------------------------------------------------------------------------------------------")
        print("Die Antwort ist leider falsch!")
        return "v"


def process_result(result, round, Joker):
    if result == "ro" and round < 15:
        round += 1
        Kontostand = Kontostand_liste[round - 1]
        print("--------------------------------------------------------------------------------------------")
        print(f"Du hast noch {Joker} Joker übrig")
        print(f"Dein aktueller Gewinn beträgt: {Kontostand}")
        print("--------------------------------------------------------------------------------------------")
        return round, Joker
    elif result == "rm" and round < 15:
        round += 1
        Kontostand = Kontostand_liste[round - 1]
        Joker -= 1
        print("--------------------------------------------------------------------------------------------")
        print(f"Du hast noch {Joker} Joker übrig")
        print(f"Dein aktueller Gewinn beträgt: {Kontostand}")
        print("--------------------------------------------------------------------------------------------")
        return round, Joker
    elif result == "v":
        print("--------------------------------------------------------------------------------------------")
        print("Du bist leider ausgeschieden! Deine Antwort war falsch :(")
    if (round == 15 and result != "v"):
        print("--------------------------------------------------------------------------------------------")
        print("Du hast den Jackpot geknackt! Du hast 1 Millionen Euro gewonnen!!!")
        print("----------------------------------------")
        pass

Ergebnis_1 = Runde()
round, Joker = process_result(Ergebnis_1, round, Joker)
Ergebnis_2 = Runde()
round, Joker = process_result(Ergebnis_2, round, Joker)
Ergebnis_3 = Runde()
round, Joker = process_result(Ergebnis_3, round, Joker)
Ergebnis_4 = Runde()
round, Joker = process_result(Ergebnis_4, round, Joker)
Ergebnis_5 = Runde()
round, Joker = process_result(Ergebnis_5, round, Joker)
Ergebnis_6 = Runde()
round, Joker = process_result(Ergebnis_6, round, Joker)
Ergebnis_7 = Runde()
round, Joker = process_result(Ergebnis_7, round, Joker)
Ergebnis_8 = Runde()
round, Joker = process_result(Ergebnis_8, round, Joker)
Ergebnis_9 = Runde()
round, Joker = process_result(Ergebnis_9, round, Joker)
Ergebnis_10 = Runde()
round, Joker = process_result(Ergebnis_10, round, Joker)
Ergebnis_11 = Runde()
round, Joker = process_result(Ergebnis_11, round, Joker)
Ergebnis_12 = Runde()
round, Joker = process_result(Ergebnis_12, round, Joker)
Ergebnis_13 = Runde()
round, Joker = process_result(Ergebnis_13, round, Joker)
Ergebnis_14 = Runde()
round, Joker = process_result(Ergebnis_14, round, Joker)
Ergebnis_15 = Runde()
process_result(Ergebnis_15, round, Joker)





