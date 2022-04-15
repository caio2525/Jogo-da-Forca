import random

board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
|   |
    |
    |
=========''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman():
    def random_word(self):
        with open('./palavras.txt', 'rt') as arquivo:
            words = arquivo.readlines()
        self.word= words[random.randint(0,len(words))].strip()

    def initialize(self):
        self.letras_erradas = []
        self.letras_corretas = []
        self.hidden_word = ['-' for i in range(len(self.word))]

    def game_over(self):
        if( len(self.letras_erradas) == 7 ):
            return True
        return False

    def game_won(self):
        if(''.join(self.hidden_word) == self.word):
            return True
        return False

    def print_game(self):
        print(board[len(self.letras_erradas)])
        print('Palavra: ', ''.join(self.hidden_word))
        print('\nLetras Erradas:')
        for i in range(len(self.letras_erradas)):
            print(self.letras_erradas[i])
        print('\nLetras Corretas:')
        for i in range(len(self.letras_corretas)):
            print(self.letras_corretas[i])

    def guess(self):
        letra = input('\nDigite uma letra: ')
        indices = [i for i, x in enumerate(self.word) if x == letra]
        if(len(indices) == 0):
            self.letras_erradas.append(letra)
        else:
            self.letras_corretas.append(letra)
            for i in indices:
                self.hidden_word[i] = letra

    def play(self):
        self.random_word()
        self.initialize()
        while(True):
            if(self.game_over()):
                print('\nGame over! Você perdeu.')
                print('A palavra era ' + self.word)
                break

            if(self.game_won()):
                print ('\nParabéns! Você venceu!!')
                break

            self.print_game()
            self.guess()

        print ('\nFoi bom jogar com você! Agora vá estudar!\n')

game = Hangman()
game.play()
