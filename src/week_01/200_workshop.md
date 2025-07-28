---
name: "Workshop notes"
---

## About workshops

IFN584 is not an introductory programming unit. It is anticipated that students have already acquired sound programming skills through prerequisite units. If you find that the programming exercises are excessively challenging to complete, it is advisable to first enrol in one of the prerequisites of this unit.

Each workshop consists of either programming or design exercises. Programming exercises are not marked, and the coding solutions to them will be released so that you can verify your own solutions after you finish. Design exercises are intended to facilitate feedback and enhance your project design. It is highly recommended that you complete all exercises, either during class or afterward.

---

## Choose a code editor

You are free to use any text editor or integrated development environment (IDE) to write C# programs for the workshop exercises and assignments in this unit.

If you are using Windows, Visual Studio ([https://visualstudio.microsoft.com/](https://visualstudio.microsoft.com/) is the best choice, however you can use Visual Studio Code if you prefer. The full Visual Studio provides graphical-based project setup and configuration, compared to VSCode which requires using the command palette and editing configuration files manually.

The cross-platform Visual Studio Code ([code.visualstudio.com](code.visualstudio.com)) is among the top choices for most developers. To edit the project created from the terminal, open the project directory from the code editor.

If you are using Linux or MacOS, Rider by JetBrains is another option. It is a full-fledged IDE that can be used to write and debug C#.

To ensure compatibility across various platforms (Windows, macOS, and Linux), we will use the .NET LTS 8.0 version in this unit.

## IDE Setup (Visual Studio)

## IDE Setup (Visual Studio Code or Rider)

Whether you are using VSCode or Rider, you will first need to install the .NET SDK to be able to compile and run C# applications.

Depending on whether you are using MacOS or Linux, the process will differ slightly.

### Install .NET SDK 8.0 (if not already installed)

- Download it from [dotnet.microsoft.com](https://dotnet.microsoft.com/en-us/download).
- Make sure to select the .NET 8.0 "Long Term Support" version.  
- Run the command `dotnet --version` from a terminal to verify the installation and version.

### Installing IDE and Creating Applications (Visual Studio Code)

TODO

### Installing IDE and Creating Applications (Rider)

You can obtain an educational license for Rider and the other JetBrains tools by applying with your QUT student email: https://www.jetbrains.com/community/education/#students/

Alternatively, you can install Rider in free/non-commercial mode.

1. After verifying your .NET installation, you can download and install Rider: https://www.jetbrains.com/rider/download/#section=macLinks.
2. Double-click the disk image (dmg) file to mount it, then drag Rider to the Applications directory.
3. Launch Rider from the search box or the launchpad.
4. When you run it for the first time, you will need to activate your educational license by logging in, or select the free option.

The disk image can be unmounted and deleted after installation.

To create a project for the weekly programming exercises, and for your assignments:

1. Launch Rider.
2. Select "New Solution" from the Welcome dialog. Alternatively, if you already have a window open, select File -> New Solution.
3. Enter a name for your project in the Solution Name and Project Name fields.
4. Be sure to select "C#" and "net8.0" as the languages and target frameworks respectively.
5. Click Create.

The interface is very similar to IntelliJ if you have used that previously. Compared to Visual Studio, functionality will be in different menus, but everything needed for the unit will be present.

### Creating Applications (Terminal)

All workshop exercises and assignments are text-based terminal applications. For example, to create a new C# console application named `ws1` follow these steps:

1. Open a terminal.
    - Windows: Use **Windows Terminal** (or Command Prompt, PowerShell).
    - macOS/Linux: Use **Terminal**.
2. Run the following command to create the project:

```shell
dotnet new console -n ws1
```

This will create a new directory named `ws1` with the basic structure for a C# console application.

3. Navigate into the project directory:

```shell
cd ws1
```

4. Run the application to test it:

```shell
dotnet run
```

This should display `Hello, World!` in the terminal, confirming that the project was created successfully.

---

## Programming exercises

In this first workshop, we will be creating some simple applications to help familiarise yourself with the C# programming language.

#### Exercise A

Create a program named "AskMyName". This program, as with all others in the unit will be a Console Application.

The goal of this program is to:
1. Prompt the user to enter their name.
2. Repeat the name back to the user.

You can start by writing the entire program with top-level statements for simplicity. We will cover classes and objects next week.

The functions that you will need for this program are:
- `Console.WriteLine()`: https://learn.microsoft.com/en-us/dotnet/api/system.console.writeline?view=net-8.0
- `Console.ReadLine()`: https://learn.microsoft.com/en-us/dotnet/api/system.console.readline?view=net-8.0

#### Exercise B

Your next task is to refactor the program you wrote in Exercise A to use a helper method (function) that displays a prompt, accepts input from the user, and returns it to the caller.

You should define this function as:
```c#
string PromptForString(string message);
```

This function should use the `Console.Write()` method to display the message to the terminal, and read the response from the user.

When dealing with 


### Exercise C

fibonnaci with function to prompt for integer

### Exercise D

factorial


This first workshop will help you review some of the basic OO concepts that you’ve learned from prerequisite units. The exercises cover basic OO mechanisms in C#, including class definition, object creations and usages.

#### Exercise A
1. Dice are used in many games. One die can be thrown to randomly show a value from 1 through 6. Design a `Die` class that can hold an integer data field for a value (from 1 to 6). Include an auto-implemented property that holds the value of the die and a constructor that requires a value for the die.
2. Write an application named `TwoDice` that generates random numbers for the value of two dice and displays their values.
3. Using the `Die` class, write an application named `FiveDice` that randomly “throws” five dice for the computer and five dice for a second player. Display the values and then decide who wins based on the following hierarchy of `Die` values.
    - Five of a kind
    - Four of a kind
    - Three of a kind
    - A pair

#### Exercise B
1. Playing cards are used in many computer games, including versions of such classics as solitaire, hearts, and poker. Create a class named `Card` that contains both numeric and string data fields to hold a suit (1 through 4 and “spades,” “hearts,” “diamonds,” or “clubs”) and both numeric and string data fields to hold a card value (1 to 13 and a string for the nonnumeric cards such as “queen”). Include `get` methods for each field.
2. Write an application named `DisplayTwoCards` that randomly selects two playing cards that are objects of the `Card` class. Generate a random number for each card’s suit and another random number for each card’s value. Do not allow the two cards to be identical in both suit and value. Display each card’s suit and value and a message that indicates which card has the higher value or that the two cards have equal values.
3. In the card game War, a deck of playing cards is divided between two players. Each player exposes a card; the player whose card has the higher value wins possession of both exposed cards. Create a game of War named `WarCardGame` that stores 52 `Card` class objects in an array to represent each of the standard cards in a 52-card deck. Play a game of War by revealing one card for the computer and one card for the player at a time. Award two points for the player whose card has the higher value. (For this game, the king is the highest card, followed by the queen and jack, then the numbers 10 down to 2, and finally the ace.) If the computer and player expose cards with equal values in the same turn, award one point to each. At the end of the game, all 52 cards should have been played only once, and the sum of the player’s and computer’s score will be 52.

