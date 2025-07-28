---
name: "Workshop solutions"
---

## Programming exercises

#### Exercise A

1.

```cs
class Die
{
   public int DieVal {get; set;}
   public Die(int v)
   {
      DieVal = v;
   }
}
```

2.

```cs
class TwoDice
{
   static void Main()
   {
      const int MAX = 7;
      const int MIN = 1;
      int ran;
      Random ranGenerator = new Random();
      ran = ranGenerator.Next(MIN, MAX);
      Die die1 = new Die(ran);
      ran = ranGenerator.Next(MIN, MAX);
      Die die2 = new Die(ran);
      WriteLine("The two die values are " + die1.DieVal +
         " and " + die2.DieVal);
   }
}
```

3.

```cs
class FiveDice
{
   static void Main()
   {
      const int MAX = 7;
      const int MIN = 1;
      const int NUMDICE = 5;
      int ran;
      Die[] computer = new Die[NUMDICE];
      Die[] player = new Die[NUMDICE];
      Random ranGenerator = new Random();
      int compMatch;
      int playerMatch;
      int count;
      for(count = 0; count < NUMDICE; ++count)
      {
         ran = ranGenerator.Next(MIN, MAX);
         computer[count] = new Die(ran);
         ran = ranGenerator.Next(MIN, MAX);
         player[count] = new Die(ran);
      }
      Write("Computer's dice: ");
      for(count = 0; count < NUMDICE; ++count)
         Write(computer[count].DieVal + "  ");
      WriteLine();
      Write("Player's dice:   ");
      for(count = 0; count < NUMDICE; ++count)
         Write(player[count].DieVal + "  ");
      WriteLine();
      compMatch = HowManySame(computer, NUMDICE);
      playerMatch = HowManySame(player, NUMDICE);
      if(compMatch == 1)
         WriteLine("Computer has nothing");
      else
         WriteLine("  Computer has " + compMatch + " of a kind");
      if(playerMatch == 1)
         WriteLine("  Player has nothing");
      else
         WriteLine("Player has " + playerMatch + " of a kind");
      if(compMatch > playerMatch)
         WriteLine("Computer wins");
      else
         if(compMatch < playerMatch)
            WriteLine("Player wins");
         else
            WriteLine("It's a tie");
   }    

   public static int HowManySame(Die[] die, int num)
   {
      int[] same = new int[num];
      int x, y;
      int highest;
      for(x = 0; x < num; ++x)
        same[x] = 1; // every die matches itself
      for(x = 0; x < num - 1; ++x)
      {
         for(y = x + 1; y < num; ++y)
            if(die[x].DieVal == die[y].DieVal)
            {
               same[x]++;
            }
      }
      highest = same[0];
      for(x = 1; x < num; ++x)
         if(same[x] > highest)
            highest = same[x];
      return highest;
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
class DisplayTwoCards
{
   static void Main()
   {
      const int SUITS = 4;
      const int VALS = 13;
      Random ranGenerator = new Random();
      int ranSuit1;
      int ranVal1;
      int ranSuit2;
      int ranVal2;
      ranSuit1 = ranGenerator.Next(1, SUITS+1);
      ranVal1 = ranGenerator.Next(1, VALS+1);
      Card card1 = new Card(ranSuit1, ranVal1);
      ranSuit2 = ranGenerator.Next(1, SUITS+1);
      ranVal2 = ranGenerator.Next(1, VALS+1);
      while(ranSuit1 == ranSuit2 && ranVal1 == ranVal2)
      {
        ranSuit2 = ranGenerator.Next(1, SUITS+1);
        ranVal2 = ranGenerator.Next(1, VALS+1);
      }
      Card card2 = new Card(ranSuit2, ranVal2);
      WriteLine("Card 1 is " + card1.ValString + " of " + card1.SuitString);
      WriteLine("Card 2 is " + card2.ValString + " of " + card2.SuitString);
      if(card1.Val > card2.Val)
         WriteLine("Card 1 is greater");
      else
         if(card2.Val > card1.Val)
            WriteLine("Card 2 is greater");
         else
            WriteLine("Card values are the same");
   }
}
```

3.

```cs
class WarCardGame
{
   static void Main()
   {
      const int SUITS = 4;
      const int VALS = 13;
      const int CARDS_IN_DECK = SUITS * VALS;
      const int HANDS = CARDS_IN_DECK / 2;
      Random ranGenerator = new Random();
      int hand;
      int suit;
      int val;
      int pos;
      int computerScore = 0;
      int playerScore = 0;
      int randomPlayer;
      int randomComp;
      Card[] deck = new Card[CARDS_IN_DECK];
      Card computerCard = new Card(0, 0);
      Card playerCard = new Card(0, 0);
      bool[] used = new bool[CARDS_IN_DECK];
      pos = 0;
      for(suit = 0; suit < SUITS; ++ suit)
         for(val = 0; val < VALS; ++val)
         {
            deck[pos]  = new Card(suit + 1, val + 1);
            ++pos;
         }
      for(hand = 0; hand < CARDS_IN_DECK; ++hand)
         used[hand] = false;
      for(hand = 0; hand < HANDS; ++ hand)
      {
         randomComp = ranGenerator.Next(0, deck.Length);
         while(used[randomComp] == true)
            randomComp = ranGenerator.Next(0, deck.Length);
         used[randomComp] = true;
         computerCard = deck[randomComp];
         randomPlayer = ranGenerator.Next(0, deck.Length);
         while(used[randomPlayer] == true)
            randomPlayer = ranGenerator.Next(0, deck.Length); 
         used[randomPlayer] = true;
         playerCard = deck[randomPlayer];
         WriteLine("Computer's card is " + computerCard.ValString +
                   " of " + computerCard.SuitString);
         WriteLine("Player's card is " + playerCard.ValString +
                   " of " + playerCard.SuitString);
         if(computerCard.Val > playerCard.Val)
         {
            WriteLine("   Computer wins");
            computerScore += 2;
         }
         else
         {
            if(playerCard.Val > computerCard.Val)
            {
               WriteLine("   Player wins");
               playerScore += 2;
            }
            else
            {
               WriteLine("   It's a tie");
               computerScore += 1;
               playerScore += 1;
            }
         }
         WriteLine("   Computer " + computerScore + "  Player " + playerScore);
         if(hand < HANDS - 1)
         {
            WriteLine("Press Enter to continue");
            ReadLine();
         }
         else
            WriteLine("Good game!");
      }
   }
}
```