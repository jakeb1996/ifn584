---
name: "Workshop notes"
---

## Programming exercises

In this workshop, you will practice object-oriented programming (OOP) concepts in C#. You will create classes, define properties, and implement methods to solve problems using OOP principles. The exercises cover basic OO mechanisms in C#, including class definition, object creations and usages.

---

### Exercise A

Create a class named `Point` which represents a point in a two-dimensional space, with the following specification:

1. Two fields: `x` and `y`, both of type `double`. These fields should be `private`.
2. A constructor that takes two parameters to initialize the `x` and `y` fields.
3. Getter and setter methods for both `x` and `y` fields, allowing them to be accessed and modified publicly.
4. A method named `Set()` which updates both of the `x` and `y` fields at once. The method should not return any value.
5. A method named `DistanceTo` that takes another `Point` object as a parameter and calculates the Euclidean distance from the current point to the given point using the formula `distance(p1, p2) = sqrt((x2 - x1)^2 + (y2 - y1)^2)`, where `p1` is the current point and `p2` is the point passed as a parameter. You can use the `Math.Sqrt` method to calculate the square root and `Math.Pow` to calculate the power.`

Use the following code snippet to test your `Point` class:
```csharp
Point point1 = new Point(3, 4);
Point point2 = new Point(6, 8);
Console.WriteLine($"Point 1: ({point1.GetX()}, {point1.GetY()})");
Console.WriteLine($"Point 2: ({point2.GetX()}, {point2.GetY()})");
Console.WriteLine($"Distance between Point 1 and Point 2: {point1.DistanceTo(point2)}");

point1.Set(10, 15);
Console.WriteLine($"Point 1 after setting: ({point1.GetX()}, {point1.GetY()})");
```
   

### Exercise B

Create a class named `BankAccount` that meets the following requirements:

1. The class should have an `AccountNumber` property, which can be publiclly read, but only set when the object is created.
2. A `Balance` property that can be read publicly but can only be modified through deposit and withdrawal methods. The balance property should use the `decimal` type to handle currency values accurately.`
3. An `AccountHolderName` property that can be both read and written publicly.
4. The class should have a constructor that initializes the `AccountNumber` and `AccountHolderName`, and sets the balance to zero.
5. The aforementioned `Deposit()` and `Withdraw()` methods should be implemented to modify the balance. The `Deposit()` method should accept a decimal amount to add to the balance, and the `Withdraw()` method should accept a decimal amount to subtract from the balance, ensuring that the balance does not go negative. A boolean return value should indicate whether the withdrawal was successful (true) or not (false).

Use the following code snippet to test your `BankAccount` class:
```csharp

// Create a new bank account
BankAccount account = new BankAccount("123456", "John Doe");

// Display initial account details
Console.WriteLine($"Account Number: {account.AccountNumber}, Account Holder: {account.AccountHolderName}, Balance: {account.Balance:C}");

// Deposit money
account.Deposit(100);
Console.WriteLine($"After deposit, Balance: {account.Balance:C}");

// Withdraw money
Console.WriteLine(account.Withdraw(50) ? "Withdrawal successful." : "Withdrawal failed.");
Console.WriteLine($"After withdrawal, Balance: {account.Balance:C}");
```

### Exercise C

Extend your `BankAccount` class from Exercise B to meet the following requirements:
1. Override the `ToString()` method to return a string representation of the account details, including the account number, account holder name, and current balance. For example: `Account Number: 123456, Account Holder: John Doe, Balance: $100.00`. Use string interpolation for formatting.
2. Create a method named `Transfer()` that allows transferring funds from one account to another. The method should accept a `BankAccount` object and a decimal amount to transfer. It should check if the current account has enough balance to perform the transfer. If successful, it should deduct the amount from the current account and add it to the target account, returning a boolean indicating success or failure.

Write a test program to demonstrate the functionality of the `ToString()` and `Transfer()` methods, similar to that in Exercise C.


### Exercise D
1. Dice are used in many games. One die can be thrown to randomly show a value from 1 through 6. Design a `Die` class that can hold an integer data field for a value (from 1 to 6). Include an auto-implemented property that holds the value of the die and a constructor that requires a value for the die.
2. Write an application named `TwoDice` that generates random numbers for the value of two dice and displays their values.
3. Using the `Die` class, write an application named `FiveDice` that randomly “throws” five dice for the computer and five dice for a second player. Display the values and then decide who wins based on the following hierarchy of `Die` values.
    - Five of a kind
    - Four of a kind
    - Three of a kind
    - A pair

### Exercise E
1. Playing cards are used in many computer games, including versions of such classics as solitaire, hearts, and poker. Create a class named `Card` that contains both numeric and string data fields to hold a suit (1 through 4 and “spades,” “hearts,” “diamonds,” or “clubs”) and both numeric and string data fields to hold a card value (1 to 13 and a string for the nonnumeric cards such as “queen”). Include `get` methods for each field.
2. Write an application named `DisplayTwoCards` that randomly selects two playing cards that are objects of the `Card` class. Generate a random number for each card’s suit and another random number for each card’s value. Do not allow the two cards to be identical in both suit and value. Display each card’s suit and value and a message that indicates which card has the higher value or that the two cards have equal values.
3. In the card game War, a deck of playing cards is divided between two players. Each player exposes a card; the player whose card has the higher value wins possession of both exposed cards. Create a game of War named `WarCardGame` that stores 52 `Card` class objects in an array to represent each of the standard cards in a 52-card deck. Play a game of War by revealing one card for the computer and one card for the player at a time. Award two points for the player whose card has the higher value. (For this game, the king is the highest card, followed by the queen and jack, then the numbers 10 down to 2, and finally the ace.) If the computer and player expose cards with equal values in the same turn, award one point to each. At the end of the game, all 52 cards should have been played only once, and the sum of the player’s and computer’s score will be 52.


