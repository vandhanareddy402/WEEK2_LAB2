
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practise string manipulation, loops, conditionals, and random selection while creating an interactive game.

## 📝 Tasks

### 🛠️  Set Up the Game

#### Description
Create the basic structure for your Hangman game. Define a list of possible words and set up variables to track the game state.

#### Requirements
Completed program should:

- Contain a predefined list of at least 5 words
- Randomly select one word for the player to guess
- Initialise variables to track guessed letters and remaining attempts

### 🛠️  Implement the Game Loop

#### Description
Write the main loop that allows the player to guess letters, updates the game state, and displays progress after each guess.

#### Requirements
Completed program should:

- Prompt the player to guess a letter each turn
- Display the current progress (e.g., `_ a _ _ m a n`)
- Track and display the number of incorrect guesses remaining
- Prevent repeated guesses of the same letter

Example:
```
Word: _ a _ _ m a n
Guesses left: 4
Guessed letters: a, n, m
```

### 🛠️  Handle Game Endings

#### Description
Detect when the player has either guessed the word or run out of attempts, and display an appropriate message.

#### Requirements
Completed program should:

- End the game when the word is fully guessed or attempts reach zero
- Display a congratulatory message if the player wins
- Display the correct word and a loss message if the player loses

Example output:
```
Congratulations! You guessed the word: hangman
```
or
```
Game over! The word was: hangman
```
