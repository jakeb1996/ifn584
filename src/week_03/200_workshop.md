---
name: "Workshop notes"
---

## Programming exercises

The exercises in this workshop will cover more advanced object-oriented mechanisms in C#, including inheritance, polymorphism, method overriding, and dynamic dispatch. The coding solutions to these exercises will be made available on Canvas, enabling you to validate your own solutions upon completion.

#### Exercise A

Design a `Die` class that can hold an integer data field for a value (from 1 to 6). Include an auto-implemented property that holds the value of the die and a constructor that requires a value for the die. Create a `LoadedDie` class that descends from `Die` and that can be used to give a player a slight advantage. A `LoadedDie` never rolls a 1 or a 2; if a client attempts to assign 1 or 2 to a loaded die’s value, the value is forced to 3. Create a program named `TestLoadedDice` that generates random values to simulate rolling two `Die` objects against each other 1,000 times and counts the number of times the first `Die` has a higher value than the other `Die`. Then, simulate rolling a `Die` object against a `LoadedDie` object 1,000 times and count the number of times the unloaded `Die` wins. Display the results.

#### Exercise B

1. Create a class named `Card` that represents a playing card in a standard deck. For each card, include the following:
    - A numeric data field to hold a suit number (1 through 4)
    - A string field to hold a suit name (`"spades"`, `"hearts"`, `"diamonds"`, or `"clubs"`)
    - A numeric data field to hold a card value (1 to 13)
    - A string field for the card value (`"Ace"`, `"2"`, `"3"`, `"Queen"`, and so on)

    Include properties to get and set the values of each field.

2. Create an abstract `CardGame` class that contains a property that holds the number of cards dealt to a player in a particular type of game. The class also contains an array of 52 `Card` objects, and the class constructor initialises the deck of 52 cards with appropriate values (for example, *King of Hearts*). The class also contains two abstract methods: `DisplayDescription()` and `Deal()`.
3. Create two child classes that extend `CardGame`. You can choose any games you prefer. For example, you might create a `Poker` class and a `Bridge` class. Create a constructor for each child class that initialises the field that holds the number of cards dealt according to the correct value for that game. (As examples, in standard poker, a player receives 5 cards, but in bridge, a player receives 13.) The `DisplayDescription()` method in each child class provides a very brief description of the game. The `Deal()` method displays the values for the correct number of randomly chosen `Card` objects for the `CardGame`. Make sure that no duplicate cards are displayed. For example, there can be only one King of Hearts in a deck.
4. Create an application named `PlayCardGames` that instantiates one object of each game type and demonstrates that the methods work correctly.