---
name: "Workshop solutions"
---

## Programming exercises

#### Exercise A

```cs
class DirectoryInformation
{
   static void Main()
   {
      string directory;
      string[] files;
      int x;
      const string END = "end";
      Write("Enter a directory >> ");
      directory = ReadLine();
      while(directory != END)
      {
         if(Directory.Exists(directory))
         {
            files = Directory.GetFiles(directory);
            if(files.Length == 0)
                WriteLine("There are no files in this directory: " + directory);
            else
            {
                WriteLine(directory + " contains the following files");
                for(x = 0; x < files.Length; ++x)
                   WriteLine("  " + files[x]);
             }
         }
         else
         {
            WriteLine("Directory " + directory + " does not exist");
         }
         Write("\nEnter another directory or type " + END + " to quit >> ");
         directory = ReadLine();
      }
   }
}
```

#### Exercise B

```cs
class FileComparison
{
   static void Main()
   {
      const string WORD_FILE = @"C:\CSharp\Chapter14\Quote.docx";
      const string NOTEPAD_FILE = @"C:\CSharp\Chapter14\Quote.txt";
      long wordSize;
      long notepadSize;
      double ratio;
      FileInfo wordInfo = new FileInfo(WORD_FILE);
      FileInfo notepadInfo = new FileInfo(NOTEPAD_FILE);
      wordSize = wordInfo.Length;
      notepadSize = notepadInfo.Length;
      WriteLine("The size of the Word file is " + wordSize +
          "\nand the size of the Notepad file is " + notepadSize);
      ratio = (double)notepadSize / wordSize;
      WriteLine("The Notepad file is {0} of the size of the Word file",
                ratio.ToString("P2"));
   }
}
```

#### Exercise C

1.

```cs
class WritePatientRecords
{
   static void Main()
   {
      const char DELIM = ',';
      const string END = "999";
      const string FILENAME = "Patients.txt";
      Patient patient = new Patient();
      FileStream outFile = new FileStream(FILENAME,
                                          FileMode.Create, FileAccess.Write);
      StreamWriter writer = new StreamWriter(outFile);
      Write("Enter patient ID number or " + END +
         " to quit >> ");
      patient.IdNum = ReadLine();
      while(patient.IdNum != END)
      {
         Write("Enter last name >> ");
         patient.Name = ReadLine();
         Write("Enter balance >> ");
         patient.Balance = Convert.ToDouble(ReadLine());
         writer.WriteLine(patient.IdNum + DELIM + patient.Name +
            DELIM + patient.Balance);
         Write("Enter next patient ID number or " +
            END + " to quit >> ");
         patient.IdNum = ReadLine();
      }
      writer.Close();
      outFile.Close();
   }
}
   
class Patient
{
   public string IdNum {get; set;}
   public string Name  {get; set;}
   public double Balance {get; set;}
   public new string ToString()
   {
      return ("#" + IdNum + ',' + Name + ',' + Balance);
   }
}
```

2.

```cs
class ReadPatientRecords
{
   static void Main()
   {
      const char DELIM = ',';
      const string FILENAME = "Patients.txt";
      Patient patient = new Patient();
      FileStream inFile = new FileStream(FILENAME,
                                         FileMode.Open, FileAccess.Read);
      StreamReader reader = new StreamReader(inFile);
      string recordIn;
      string[] fields;
      WriteLine("\n{0,-10}{1,-18}{2,10}\n", "IdNumber", "Name", "Balance"); 
      recordIn = reader.ReadLine();
      while(recordIn != null)
      {
         fields = recordIn.Split(DELIM);
         patient.IdNum = fields[0];
         patient.Name = fields[1];
         patient.Balance = Convert.ToDouble(fields[2]);
         WriteLine("{0,-10}{1,-18}{2, 10}", patient.IdNum,
                   patient.Name, patient.Balance.ToString("C"));
         recordIn = reader.ReadLine();
      }
      
      reader.Close(); 
      inFile.Close();
   }
}
```

3.

```cs
class FindPatientRecords
{
   static void Main()
   {
      const char DELIM = ',';
      const string FILENAME = "Patients.txt";
      Patient patient = new Patient();
      FileStream inFile = new FileStream(FILENAME,
                                         FileMode.Open, FileAccess.Read);
      StreamReader reader = new StreamReader(inFile);
      string recordIn;
      string[] fields;
      string request;
      bool found = false;
      Write("Enter patient ID number to find >> ");
      request = ReadLine();
      WriteLine("\n{0,-10}{1,-18}{2,10}\n", "ID Number", "Name", "Balance"); 
      recordIn = reader.ReadLine();
      while(recordIn != null)
      {
         fields = recordIn.Split(DELIM);
         patient.IdNum = fields[0];
         patient.Name = fields[1];
         patient.Balance = Convert.ToDouble(fields[2]);
         if(patient.IdNum.Equals(request))
         {
            WriteLine("{0,-10}{1,-18}{2, 10}", patient.IdNum,
                      patient.Name, patient.Balance.ToString("C"));
            found = true;
         }
         recordIn = reader.ReadLine();
      }
      if(!found)
         WriteLine("No records found for {0}", request);
      reader.Close(); 
      inFile.Close();
   }
}
```

4.

```cs
class FindPatientRecords2
{
   static void Main()
   {
      const char DELIM = ',';
      const string FILENAME = "Patients.txt";
      Patient patient = new Patient();
      FileStream inFile = new FileStream(FILENAME,
                                         FileMode.Open, FileAccess.Read);
      StreamReader reader = new StreamReader(inFile);
      string recordIn;
      string[] fields;
      string request;
      double requestedBal = 0;
      bool found = false;
      Write("Enter minimum balance to display >> ");
      request = ReadLine();
      while(!double.TryParse(request, out requestedBal))
      {
         WriteLine("Wrong format. Please renter balance >> ");
         request = ReadLine();
      }
      WriteLine("\n{0,-10}{1,-18}{2,10}\n", "ID Number", "Name", "Balance"); 
      recordIn = reader.ReadLine();
      while(recordIn != null)
      {
         fields = recordIn.Split(DELIM);
         patient.IdNum = fields[0];
         patient.Name = fields[1];
         patient.Balance = Convert.ToDouble(fields[2]);
         if(patient.Balance >= requestedBal)
         {
            WriteLine("{0,-10}{1,-18}{2, 10}", patient.IdNum,
                      patient.Name, patient.Balance.ToString("C"));
            found = true;
         }
         recordIn = reader.ReadLine();
      }
      if(!found)
         WriteLine("No records found with balance greater than {0}",
                   requestedBal);
      reader.Close(); 
      inFile.Close();
   }
}
```