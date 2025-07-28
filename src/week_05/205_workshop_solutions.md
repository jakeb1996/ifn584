---
name: "Workshop solutions"
---

## Programming exercises

#### Exercise A

```cs
class GuessingGameWithExceptionHandling
{
   static void Main()
   {
      const int MIN = 1;
      const int MAX = 11;
      int guess;
      int count = 1;
      int lowest = MIN;
      int highest = MAX;
      Random RandomClass = new Random();
      int randomNumber;
      randomNumber = RandomClass.Next(MIN, MAX - 1);
      try
      {
         Write("Guess a number between {0} and {1} >> ", MIN, MAX);
         guess = Convert.ToInt32(ReadLine());
      }
      catch(Exception e)
      {
         guess = 0;
         WriteLine("You must enter a number. Setting your guess to 0.");
      }
      while(guess != randomNumber)
      {
         if(guess < MIN || guess > MAX)
            WriteLine("Your guess is out of range -- stay between {0} and {1}",
               MIN, MAX);
         if(count == 1)
         {
            if(guess < randomNumber)
               lowest = guess;
            else
               highest = guess;
         }
         else
         {
            if(guess <= lowest)
            {
               WriteLine("You already knew it was not {0} or less", lowest);
            }
            if(guess >= highest)
            {
               WriteLine("You already knew it was not {0} or more", highest);
            }
            if(guess < randomNumber && guess > lowest)
               lowest = guess;
            if(guess > randomNumber && guess < highest)
               highest = guess;
         }
         if(guess < randomNumber)
            WriteLine("Your guess was too low");
         else
            WriteLine("You guess was too high");
         try
         {
             Write("Guess again >> ");
             guess = Convert.ToInt32(ReadLine());
         }
         catch(Exception e)
         {
             guess = 0;
            WriteLine("You must enter a number. Setting your guess to 0.");
         }
         count++;          
      }
      WriteLine("Your guess was correct!");
      Write("You got it in {0} guess", count);
      if(count != 1)
         WriteLine("es");
   }
}
```

#### Exercise B

```cs
class GuessAWordWithExeptionHandling
{
   static void Main()
   {
      string[] words = {"apricot", "elephant", "tigress", "fortunate",
        "impossible", "historical", "colorful", "science"};
      char[] letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
      Random RandomClass = new Random();
      int randomNumber;
      randomNumber = RandomClass.Next(0, words.Length);
      string selectedWord = words[randomNumber];
      string guessedWord = "";
      string originalWord = selectedWord;
      string guess;
      char letter = ' ';
      int pos;
      char tempChar;
      int foundCount = 0;
      bool letterInWord = false;
      for(int a = 0; a < selectedWord.Length; ++a)
         guessedWord = guessedWord + "*";
      while(foundCount < selectedWord.Length)
      {
          WriteLine("Word: {0}", guessedWord);
          Write("Guess a letter >> ");
          try
          {
              guess = ReadLine();
              letter = Convert.ToChar(guess.Substring(0, 1));
              bool isLetter = false;
              for(int x = 0; x < letters.Length; ++x)
              {
                  if(letter == letters[x])
                  {
                     isLetter = true;
                     x = letters.Length;
                  }
              }
              letterInWord = false;
              if(!isLetter)
                  throw(new NonLetterException(letter));
              for(pos = 0; pos < selectedWord.Length; ++ pos)
              {
                tempChar = Convert.ToChar(selectedWord.Substring(pos, 1));
                if(tempChar == letter)
                {
                   guessedWord = guessedWord.Substring(0, pos) + letter +
                     guessedWord.Substring(pos + 1, (guessedWord.Length - 1 - pos));  
                   selectedWord = selectedWord.Substring(0, pos) + '?' +
                     selectedWord.Substring(pos + 1, (guessedWord.Length - 1 - pos));
                   ++foundCount;
                   letterInWord = true;
                }
              }
            }
            catch(NonLetterException e)
            {
               WriteLine("     " + e.Message);
            }     
         if(letterInWord)
             WriteLine("Yes! {0} is in the word", letter);
          else
             WriteLine("Sorry. {0} is not in the word", letter);
      }
      WriteLine("Good job! Word was {0}", originalWord);
    }   
     
}
class NonLetterException : Exception
{
    public NonLetterException(char c) : base("Not a letter : " + c)
    {
    }
}
```