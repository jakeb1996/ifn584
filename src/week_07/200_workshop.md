---
name: "Workshop notes"
---

## Design exercises

This workshop provides hands-on experiences on object-oriented design through CRC cards. Sample solutions to these experiences will be made available on Canvas.

Here is a brief recap what CRC cards are from the lectures:
- **Class:** The name of the object (usually a noun).
- **Responsibilities:** What the object knows or does (usually verbs).
- **Collaborators:** Other objects that this object interacts with to fulfil its responsibilities.

These exercises will help you understand the basics of object-oriented design and how to use CRC cards to model a system. Remember, this is a simplified example, and a real-world library system would be much more complex.

---
#### Exercise A

We want to design a system that allows library members to borrow books. The system should track books, members, and borrowing transactions.

As a guideline, follow these steps to perform a CRC analysis:
###### Identify potential classes:
- Think about the key entities involved in the library system.
- Start with obvious nouns from the scenario.
- Examples: Book, Member, Library, BorrowingTransaction.
###### Create CRC cards:
- For each identified class, create a CRC card.
- Divide the card into three sections:
	- **Class name:** Write the class name at the top.
	- **Responsibilities:** List the things the class is responsible for doing. Use active verbs.
	- **Collaborators:** List the other classes that this class needs to work with to fulfil its responsibilities.
###### Brainstorm responsibilities:
- For each class, think about what it needs to do.
- Focus on high-level responsibilities, not implementation details.
- Examples:
	- **Book:** "Track book details," "Check availability".
	- **Member:** "Track member details," "Borrow a book".
	- **Library:** "Manage books," "Manage members," "Process borrowing transactions".
	- **BorrowingTransaction:** "Record borrowing details," "Track due date".
###### Identify collaborators:
- For each responsibility, determine which other classes are needed.
- Draw lines between the classes on your cards to show collaborations.
- Examples:
	- **Member** collaborates with **Library** to "Borrow a book".
	- **Library** collaborates with **Book** to "Check availability".
	- **Library** collaborates with **Member** to confirm member status.
	- **Library** collaborates with **BorrowingTransaction** to create a record.
	- **BorrowingTransaction** collaborates with **Book** and **Member** to record data.
###### Role-play scenarios:
- Walk through common scenarios, such as:
	- "A member borrows a book".
	- "A member returns a book".
	- "A librarian adds a new book".
	- "A librarian adds a new member".
- As you walk through the scenarios, trace the interactions between the classes using your CRC cards.
- Identify any missing responsibilities or collaborations.
###### Refine and iterate:
- Review your CRC cards and make adjustments.
- Look for classes with too many responsibilities (consider splitting them).
- Look for classes with too few responsibilities (consider merging them).
- Ensure each responsibility is clear and concise.
- Ensure that collaborations are necessary.

---
#### Exercise B

CRC cards are useful for brainstorming and initial design. They help you identify the main entities (classes), their roles (methods), and their interactions (collaborations). These serve as the foundation for the class diagram. Typically, a class name becomes the name of your class in the code, responsibilities become methods (functions) of your class, and collaborators indicate which classes need to interact with each other, resulting in relationships and parameter passing in your code.

You can use either a visual ([Excalidraw](https://excalidraw.com), [draw.io](https://www.drawio.com), [Lucidchart](https://www.lucidchart.com)) or script-based ([PlantUML](https://plantuml.com/), [Mermaid](https://mermaid.js.org)) diagramming tool.

To convert the CRC cards from Exercise A into a class diagram, follow these steps:
###### Transition to class definitions:
- Class names:
	- Take each CRC card and create a corresponding class definition.
	- Example: The "Book" CRC card becomes `public class Book { ... }` in C#.
- Responsibilities to methods:
	- For each responsibility listed on a CRC card, create a method within the corresponding class.
	- Example: "Track book details" on the "Book" card might translate to `public string GetDetails() { ... }`.
	- Consider the verb used in the responsibility to name the method (e.g., "check" becomes `CheckAvailability()`).
- Data (attributes/properties):
	- As you consider the responsibilities, identify the data that the class needs to hold.
	- Example: "Track book details" implies that the "Book" class needs to store the title, author, and ISBN. These become attributes (fields) or properties of the class.
	- Example: `public string Title {get; set;}`
- Data types:
	- Determine the data types of the attributes and method parameters (strings, integers, booleans, etc.).
- Constructors:
	- Consider if the class needs a constructor to initialize its attributes when an object is created.
	- Example: `public Book(string title, string author, string isbn) { ... }`.
###### Transition to class diagrams:
- Classes:
	- Represent each class as a rectangle in the diagram.
	- Write the class name inside the rectangle.
- Attributes/properties:
	- List the attributes/properties within the class rectangle.
	- Include the data type and visibility (e.g., `title: string`).
- Methods:
	- List the methods within the class rectangle.
	- Include the method name, parameters, and return type (e.g., `GetDetails(): string`).
- Relationships (collaborations):
	- Use lines and arrows to represent relationships between classes.
	- Association/dependency: A general "uses" relationship where one class uses another as a parameter (e.g., a "Library" uses a "Book"). Represented by a straight arrow line.
	- Aggregation/composition: A "has-a" relationship (e.g., a "Library" has many "Books"). Use a diamond shaped arrow.
	- Creation/instantiation: A "creates" relationship where one class creates an object of another class.  Represented by an dashed arrow line.
- Multiplicity (Optional):
	- Indicate the number of objects involved in a relationship (e.g., "1" or "0..\*").

---
#### Exercise C (optional)

You can continue developing C# class code based on the class diagram. Here are the steps you can follow:

- Class structure:
	- Create a separate class file for each class.
	- Use the class definition created in Exercise B.
- Attributes/properties:
	- Declare the attributes/properties as fields or properties within the class.
	- Use appropriate access modifiers (e.g., `public`, `private`).
- Methods:
	- Implement the methods based on the responsibilities and the class diagram.
	- Write the code to perform the actions defined by the responsibilities.
	- Pass the correct parameters into methods, based upon the class diagram.
- Constructors:
	- Implement the constructors to initialise the object's state.
- Relationships:
	- Implement the relationships by:
		- Storing references to other objects (e.g., a `Library` storing a list of `Book` objects).
		- Passing objects as parameters to methods.
- Logic:
	- Add the necessary logic to implement the behaviour of the class.
	- Handle edge cases and error conditions.
- Testing:
	- Write some tests to verify that the code works correctly.
