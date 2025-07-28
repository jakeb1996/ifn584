---
name: "Workshop solutions"
---

## Programming exercises

#### Exercise A

1.

```cs
using System;
using static System.Console;
class TestLoadedDice
{
   static void Main()
   {
      const int MAX = 7;
      const int MIN = 1;
      const int THROWS = 1000;
      int ran;
      int roll;
      int count;
      Random ranGenerator = new Random();
      count = 0;
      for(roll = 0; roll < THROWS; ++roll)
      {
         ran = ranGenerator.Next(MIN, MAX);
         Die die1 = new Die(ran);
         ran = ranGenerator.Next(MIN, MAX);
         Die die2 = new Die(ran);
         if(die1.DieVal > die2.DieVal)
            ++count;
      }
      WriteLine("After " + THROWS + " throws with two regular dice,");
      WriteLine("     the first die beat the second " + count + " times");
      count = 0;
      for(roll = 0; roll < THROWS; ++roll)
      {
         ran = ranGenerator.Next(MIN, MAX);
         Die die1 = new Die(ran);
         ran = ranGenerator.Next(MIN, MAX);
         Die die2 = new LoadedDie(ran);
         if(die1.DieVal > die2.DieVal)
            ++count;
      }
      WriteLine("After " + THROWS + " throws with one loaded die,");
      WriteLine("     the first die beat the second " + count + " times");
   }
}

class Die
{
   public int DieVal {get; set;}
   public Die(int v)
   {
      DieVal = v;
   }
}

class LoadedDie : Die
{
   private int INVALID1 = 1;
   private int INVALID2 = 2;
   private int VALID = 3;
   public LoadedDie(int v) : base(v)
   {
      if(v == INVALID1 || v == INVALID2)
         DieVal = VALID;
   }
}
```

#### Exercise B

1.

```cs
class Card
{
   private string suitString;
   private string valString;
   private int suit;
   private int val;
   private readonly string[] VALARRAY = {"", "Ace", "2", "3", "4",
     "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"};
   private readonly string[] SUITARRAY = {"", "spades", "hearts",
     "diamonds", "clubs"};
   public Card(int s, int v)
   {
      suit = s;
      val = v;
      suitString = SUITARRAY[s];
      valString = VALARRAY[v];
   }
   public string SuitString
   {
      get
      {
         return suitString;
      }
   }
   public string ValString
   {
      get
      {
         return valString;
      }
   }
   public int Suit
   {
      get
      {   
         return suit;
      }
   }
   public int Val
   {
      get
      {
         return val;
      }
   }
}
```

2.

```cs
abstract class CardGame
{
   const int SUITS = 4;
   const int VALS = 13;
   const int CARDS_IN_DECK = SUITS * VALS;
   protected Card[] deck = new Card[CARDS_IN_DECK];
   public CardGame(int c)
   {
      CardsToDeal = c;
      int suit;
      int val;
      int pos = 0;
      for(suit = 0; suit < SUITS; ++ suit)
         for(val = 0; val < VALS; ++val)
         {
            deck[pos]  = new Card(suit + 1, val + 1);
            ++pos;
         }
   }
   public int CardsToDeal {get; set;}
   public abstract void DisplayDescription();
   public abstract void Deal();
}
```

3.

```cs
class Poker : CardGame
{
   public Poker() : base(5)
   {
   }
   public override void DisplayDescription()
   {
      WriteLine("\nPoker is a betting and bluffing game; the best hand wins");
   }
   public override void Deal()
   {
      int[] cards = new int[CardsToDeal];
      int x;
      int y;
      Random ranGenerator = new Random();
      for(x = 0; x < CardsToDeal; ++x)
      {
         cards[x] = ranGenerator.Next(0, 52);
         for(y = 0; y < x; ++y)
            if(cards[x] == cards[y])
               --x;
      }
      for(x = 0; x < CardsToDeal; ++x)
         WriteLine("Card #" + (x + 1) + " " + deck[cards[x]].ValString +
         " of " + deck[cards[x]].SuitString);
   }         
}

class Bridge : CardGame
{
   public Bridge() : base(13)
   {
   }
   public override void DisplayDescription()
   {
      WriteLine("\nBridge requires bidding and taking tricks");
   }
   public override void Deal()
   {
      int[] cards = new int[CardsToDeal];
      int x;
      int y;
      Random ranGenerator = new Random();
      for(x = 0; x < CardsToDeal; ++x)
      {
         cards[x] = ranGenerator.Next(0, 52);
         for(y = 0; y < x; ++y)
            if(cards[x] == cards[y])
               --x;
      }
      for(x = 0; x < CardsToDeal; ++x)
         WriteLine("Card #" + (x + 1) + " " + deck[cards[x]].ValString +
         " of " + deck[cards[x]].SuitString);
   }         
}
```

4.

```cs
class PlayCardGames
{
   static void Main()
   {
      CardGame aPokerGame = new Poker();
      aPokerGame.DisplayDescription();
      aPokerGame.Deal();
      CardGame aBridgeGame = new Bridge();
      aBridgeGame.DisplayDescription();
      aBridgeGame.Deal();
   }
}
```