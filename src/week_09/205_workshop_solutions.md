---
name: "Workshop solutions"
---

## Design exercises

#### Exercise A

```csharp
using System;

namespace TemplateMethodExample
{
    // Abstract base class defining the template method.
    abstract class DataProcessor
    {
        // Template method outlining the steps.
        public void ProcessData()
        {
            ReadData();
            ProcessDataCore();  // Step implemented by subclasses.
            WriteData();
        }

        protected virtual void ReadData()
        {
            Console.WriteLine("Reading data from the source...");
        }

        // Abstract step: must be implemented by subclasses.
        protected abstract void ProcessDataCore();

        protected virtual void WriteData()
        {
            Console.WriteLine("Writing processed data to the destination...");
        }
    }

    // Concrete subclass for processing CSV data.
    class CsvDataProcessor : DataProcessor
    {
        protected override void ProcessDataCore()
        {
            Console.WriteLine("Processing CSV data...");
        }
    }

    // Concrete subclass for processing XML data.
    class XmlDataProcessor : DataProcessor
    {
        protected override void ProcessDataCore()
        {
            Console.WriteLine("Processing XML data...");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            DataProcessor csvProcessor = new CsvDataProcessor();
            csvProcessor.ProcessData();

            Console.WriteLine();

            DataProcessor xmlProcessor = new XmlDataProcessor();
            xmlProcessor.ProcessData();
        }
    }
}
```


---
#### Exercise B

```csharp
using System;

namespace FactoryMethodExample
{
    // Interface for notification behavior.
    public interface INotification
    {
        void Notify();
    }

    // Concrete implementation for Email notification.
    public class EmailNotification : INotification
    {
        public void Notify()
        {
            Console.WriteLine("Sending an email notification.");
        }
    }

    // Concrete implementation for SMS notification.
    public class SMSNotification : INotification
    {
        public void Notify()
        {
            Console.WriteLine("Sending an SMS notification.");
        }
    }

    // Abstract factory class which defines the factory method.
    public abstract class NotificationFactory
    {
        // Factory Method responsible for object creation.
        public abstract INotification CreateNotification();

        public void SendNotification()
        {
            INotification notification = CreateNotification();
            notification.Notify();
        }
    }

    // Concrete factory for Email notifications.
    public class EmailNotificationFactory : NotificationFactory
    {
        public override INotification CreateNotification()
        {
            return new EmailNotification();
        }
    }

    // Concrete factory for SMS notifications.
    public class SMSNotificationFactory : NotificationFactory
    {
        public override INotification CreateNotification()
        {
            return new SMSNotification();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            // Using the Email Notification Factory.
            NotificationFactory emailFactory = new EmailNotificationFactory();
            emailFactory.SendNotification();

            Console.WriteLine();

            // Using the SMS Notification Factory.
            NotificationFactory smsFactory = new SMSNotificationFactory();
            smsFactory.SendNotification();
        }
    }
}
```

---
#### Exercise C

```csharp
using System;

namespace IntegratedExample
{
    // Step 1: Define the Notification Factory (Factory Method)
    public interface INotification
    {
        void Notify();
    }

    public class EmailNotification : INotification
    {
        public void Notify()
        {
            Console.WriteLine("Sending an email notification...");
        }
    }

    public class SMSNotification : INotification
    {
        public void Notify()
        {
            Console.WriteLine("Sending an SMS notification...");
        }
    }

    // Step 2: Define the Data Processor (Template Method)
    public abstract class DataProcessor
    {
        // Template method defining the data processing steps.
        public void ProcessData()
        {
            ReadData();
            ProcessDataCore(); // Delegated to subclasses.
            WriteData();
            SendNotification();
        }

        protected virtual void ReadData()
        {
            Console.WriteLine("Reading data from the source...");
        }
        protected abstract void ProcessDataCore();
        protected virtual void WriteData()
        {
            Console.WriteLine("Writing processed data to the destination...");
        }
        protected abstract INotification CreateNotification();
        protected void SendNotification()
        {
            INotification notification = CreateNotification();
            notification.Notify();
        }
    }

    public class CsvDataProcessor : DataProcessor
    {
        protected override void ProcessDataCore()
        {
            Console.WriteLine("Processing CSV data...");
        }

        protected override INotification CreateNotification()
        {
            return new EmailNotification(); // CSV uses Email Notification
        }
    }

    public class XmlDataProcessor : DataProcessor
    {
        protected override void ProcessDataCore()
        {
            Console.WriteLine("Processing XML data...");
        }

        protected override INotification CreateNotification()
        {
            return new SMSNotification(); // XML uses SMS Notification
        }
    }

    // Main Program
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Using CSV Processor with Email Notification:");
            DataProcessor csvProcessor = new CsvDataProcessor();
            csvProcessor.ProcessData();

            Console.WriteLine("\nUsing XML Processor with SMS Notification:");
            DataProcessor xmlProcessor = new XmlDataProcessor();
            xmlProcessor.ProcessData();
        }
    }
}
```