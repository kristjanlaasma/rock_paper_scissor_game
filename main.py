#main.py
from game import game, read_scores, statistics

def main():
    """Käivitab koodi"""
    read_scores()
    statistics()
    game()

if __name__ == "__main__":
    main()
