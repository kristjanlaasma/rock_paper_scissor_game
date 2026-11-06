#game.py
import random
import csv

total_rounds = 0
player_rounds_won = 0
computer_rounds_won = 0

scores_file = "rps_results.csv"

def game():
    """Mängu põhi loogika"""

    global total_rounds, player_rounds_won, computer_rounds_won

    print("\n")
    print("1. Kivi")
    print("2. Paber")
    print("3. Käärid")

    player_choice = input("Tee oma valik: ")
    if player_choice == "1":
        player_choice = "Kivi"
    elif player_choice == "2":
        player_choice = "Paber"
    elif player_choice == "3":
        player_choice = "Käärid"
    else:
        print("Vale valik")
        new_round()

        
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "Kivi"
    elif computer_choice == 2:
        computer_choice = "Paber"
    elif computer_choice == 3:
         computer_choice = "Käärid"

    
    print("\n")
    print(f"Mängija valis {player_choice}")  
    print(f"Arvuti valis {computer_choice}")


    if player_choice == "Kivi" and computer_choice == "Kivi":
        print("Viik, mängitakse uus voor.")
        new_round()
    if player_choice == "Paber" and computer_choice == "Paber":
        print("Viik, mängitakse uus voor.")
        new_round()
    if player_choice == "Käärid" and computer_choice == "Käärid":
        print("Viik, mängitakse uus voor.")
        new_round()


    if player_choice == "Kivi" and computer_choice == "Paber":
        print("Arvuti võitis.")
        computer_rounds_won += 1
        total_rounds += 1
        new_round()
    if player_choice == "Paber" and computer_choice == "Käärid":
        print("Arvuti võitis.")
        computer_rounds_won += 1
        total_rounds += 1
        new_round()
    if player_choice == "Käärid" and computer_choice == "Kivi":
        print("Arvuti võitis.")
        computer_rounds_won += 1
        total_rounds += 1
        new_round()


    if player_choice == "Paber" and computer_choice == "Kivi":
        print("Mängija võitis.")
        player_rounds_won += 1
        total_rounds += 1
        new_round()
    if player_choice == "Käärid" and computer_choice == "Paber":
        print("Mängija võitis.")
        player_rounds_won += 1
        total_rounds += 1
        new_round()
    if player_choice == "Kivi" and computer_choice == "Käärid":
        print("Mängija võitis.")
        player_rounds_won += 1
        total_rounds += 1
        new_round()



def new_round():
    """Alustab uue vooru kui pole 5 arvesse läinud vooru mängitud"""
    if total_rounds < 5:
        print("Uus voor")
        game()       
    elif total_rounds == 5:
        game_over()
        



def game_over():
    """Lõpetab mängu ja ütleb võitja ja küsib kas uuesti mängida"""
    print("\n")
    print("Mäng läbi")

    global winner_statistics  
    winner = "" 
    if computer_rounds_won < player_rounds_won:
        winner = "Mängija"
        winner_statistics = "Player"
    if computer_rounds_won > player_rounds_won:
        winner = "Arvuti"
        winner_statistics = "Computer"

    print(f"Mängija võidud: {player_rounds_won}, arvuti võidud: {computer_rounds_won}, mängu võitis: {winner}")
    save_scores()
    restart_game()





def save_scores():
    """Küsib mängijalt nime ja salvestab mängude andmed faili"""
    name = input("Sisestake oma nimi: ")
    
    with open(scores_file, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, player_rounds_won, computer_rounds_won, winner_statistics])



def read_scores():
    """Loeb failist mitu mängu on mängitud ja väljastab selle"""
    try:
        with open(scores_file, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            games_played = list(reader)

        print("Mängud mängitud:", len(games_played))
    except FileNotFoundError:
        print("Mänge pole veel mängitud")
        return



def statistics():
    """Loeb mitu korda on võitnud arvuti ja mängija ning väljastab need."""
    try:
        count_computer = 0
        count_player = 0
        with open(scores_file, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                if row[3] == "Computer":
                    count_computer += 1
                elif row[3] == "Player":
                    count_player += 1


            print(f"Arvuti on võitnud: {count_computer} mängu")
            print(f"Mängija on võitnud: {count_player} mängu")
    except FileNotFoundError:
        print("Faili ei leitud statistika jaoks.")  




def restart_game():
    """Küsib kas mängija tahab uut mängu mängida"""
    choice = input("Kas soovid uuesti mängu? (j/e): ")

    if choice.lower() == "j":
        global total_rounds, player_rounds_won, computer_rounds_won

        total_rounds = 0
        player_rounds_won = 0
        computer_rounds_won = 0

        read_scores()
        statistics()
        game()

    else:
        return