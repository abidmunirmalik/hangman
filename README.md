### Hangman Game written in Python

You can either guess a country or a capital.


### Playing game (loosing):
```
$ python3 main.py

 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
1. Countries
2. Capitals

Enter your choice:1

Country Name: ['-', '-', '-', '-', '-']
Missed Choices: []
Total Missed: 0


  +---+
      |
      |
      |
      |
      |
=========

Enter your choice: a

Country Name: ['-', '-', '-', '-', 'a']
Missed Choices: ['c', 'h', 'f', 'r', 't', 'w', 't']
Total Missed: 7


  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========

Sorry it was india, You lose.
```

### Playing game (winning):
```
Country Name: ['k', 'e', 'n', '-', 'a']
Missed Choices: ['i', 'c', 'd', 'o']
Total Missed: 4


  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
Enter your choice: y

Yes, it was kenya !!! Yay Hangman Saved and You Won !!!
```
