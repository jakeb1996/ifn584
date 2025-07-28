---
name: "Workshop notes"
---

## Programming exercises

The exercises in this workshop will cover error handling mechanisms in C# with exception classes. The coding solutions to these exercises will be made available on Canvas, enabling you to validate your own solutions upon completion.

#### Exercise A

Create a program called `GuessingGameWithExceptionHandling` that generates a random number, allows a user to guess it, and displays a message indicating whether the guess is too low, too high, or correct. The user can continue to enter values until the correct guess is made. After the user guesses correctly, display the number of guesses made. Criticise the player for making a “dumb” guess. For example, if the player guesses that the random number is 4 and is told that the guess is too low, and then the player subsequently makes a guess lower than 4, display a message that the user should have known not to make such a low guess. Handle the `Exception` that is thrown when the user makes a non-numeric guess by displaying an appropriate message and setting the guess to 0 so that it counts as a guess that is too low.

#### Exercise B

Create a `NonLetterException` class that descends from `Exception`. The `Message string` for your new class should indicate that a non-letter character has been entered by a user. Create a game named `GuessAWordWithExceptionHandling` in which a user guesses letters to try to find a hidden word. Within the program, throw and catch a `NonLetterException` and display its message when a user enters a guess that is not a letter of the alphabet.