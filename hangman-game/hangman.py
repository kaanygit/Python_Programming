import random



wordsList=["Ali","Ayse","Veli","Zeki","Ahmet","Kaan"]


def getWord():
    choiseWord=random.choice(wordsList)
    return choiseWord.upper()

def play(word):
    word_complecition="_"*len(word)
    guessed=False
    gussingWord=[]
    guessedLetters=[]
    tries=6
    print("Oynamaya Basla")
    print(display_hangman(tries))
    print(word_complecition)
    print("\n")
    
    while not guessed and tries>0:
        guess=input("Lütfen harf girişi yapınız : ",).upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessedLetters:
                print("Aaradığınız harf bulundu ",guess)
            elif guess not in word:
                print(guess,"kelime de bulunamadı")
                tries-=1
                guessedLetters.append(guess)
            else:
                print("İyi iş",guess,"kelimeyi buldun")
                guessedLetters.append(guess)
                wordsAsList=list(word_complecition)
                indices=[i for i,letter in enumerate(word) if letter==guess]
                for index in indices:
                    wordsAsList[index]=guess
                word_complecition="".join(wordsAsList)
                if "_" not in word_complecition:
                    guessed=True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in gussingWord:
                print("Kelimeyi buldun ",guess)
            elif guess!=word:
                print(guess,"kelimede yok")
                tries-=1
                guessedLetters.append(guess)
            else:
                guessed=True
                word_complecition=word
        else:
            print("Aradığınız harf bulunamadı")
            
        print(display_hangman(tries))
        print(word_complecition)
        print("\n")
    if guessed:
        print("Tebrikler bildin")
    else:
        print("Tekrar dene")

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word=getWord()
    play(word)
    while input("Play again (Y/N)").upper()=="Y":
        word=getWord()
        play(word)
        
    
if __name__=="__main__":
    main()