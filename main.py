
from game import Game

FILE_PATH = 'state.json'

def main():
    #pull test
    game = Game(FILE_PATH)
    game.run_quiz()     

if __name__ == '__main__':
    main()