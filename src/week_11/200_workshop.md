---
name: "Workshop notes"
---

## Design Exercises

This workshop provides hands-on experiences in object-oriented design using two advanced design patterns:
- **Command Pattern**: Used to decouple the object that invokes the operation (the _Invoker_) from the one that knows how to perform it (the _Receiver_).
- **Abstract Factory Pattern**: Used to create families of related objects without being coupled to their concrete classes.

---
#### Exercise A

The Command pattern encapsulates a request as an object, allowing you to parameterise clients with different requests, queue or log these requests. It promotes clean separation of concerns, ease of extension, and the flexibility to add functionalities like undo/redo and command logging. In this exercise, we’ll design part of a smart home automation system—a system where a central controller (like a smart remote) executes commands (such as turning lights on or off) that are encapsulated into objects. We’ll also cover how to incorporate macro commands (aggregating several actions into one) and the undo functionality.

Imagine a smart home where you don’t want a single smartphone tap to individually control various devices—lights, fans, security cameras, and more. Instead, you build a system where each device operation is packaged into a command. Want to set the house to "Good Night" mode? For example, a macro command can aggregate multiple commands: turn off all lights, lock all doors, set the security alarm, etc. 

This approach makes our home automation extendable. If tomorrow a new device is introduced (like a smart thermostat), you simply create a new command without altering the remote controller's implementation. 

This exercise helps illustrate both single-device commands and aggregated operations. Your task is to create a class diagram and then implement the classes in C# using the key components of the Command pattern:

- **Command Interface (ICommand):** 
	- `ICommand` Declares methods for executing and undoing an operation.
    
- **Concrete Commands:**  
	- Classes like `LightOnCommand`, `LightOffCommand`, and `MacroCommand` implement `ICommand` to bind a receiver with a specific action.
	- Macro commands allow you to group multiple commands into one aggregated command. For instance, a "Good Night" command can aggregate turning off lights, turning on security, and so on.
    
- **Receiver:**  
	- The actual object that performs the operations (in our example, a `Light`).
    
- **Invoker:**
	- The controller (here, a `RemoteControl`) that triggers commands.
    
- **Client:**  
	- The piece that creates concrete command objects and assembles the object structure.

This diagram should show:
- The `ICommand` interface that all commands implement.
- Concrete commands (`LightOnCommand`, `LightOffCommand`, and `MacroCommand`) that encapsulate actions on the receiver (`Light`).
- The `RemoteControl` acting as the Invoker that sets and triggers commands.

---

#### Exercise B

The Abstract Factory pattern provides an interface for creating families of related or dependent objects without specifying their concrete classes. By grouping individual factories that share a common theme, it allows client code to be decoupled from the specific classes that implement the products. In other words, this pattern lets you produce a set of related objects that work together seamlessly, even if the concrete implementations differ.

Imagine an automotive manufacturing system where different production lines are tasked with assembling vehicles for various market segments. For instance, the design requirements for a high-performance sports car are markedly different from those for a family SUV:

- Sports Car Production:
    - **Engine:** A high-performance engine with tuned parameters for speed.
    - **Tires:** Low-profile tires offering superior grip and handling.
- SUV Production:
    - **Engine:** An engine optimised for torque and fuel efficiency.
    - **Tires:** All-terrain tires designed for durability and off-road performance.

In this exercise, the system must select the appropriate *factory* to produce a family of parts (engine, tire, and possibly other components) that match the vehicle's design requirements. The Abstract Factory pattern fits well here—each concrete vehicle parts factory produces related parts for its specific market segment, protecting the client code from needing to know the details of each part's implementation.

Your task is to create a class diagram and *optionally* implement the classes in C# using the key components of the Abstract Factory pattern. This diagram should illustrate:
- The product interfaces (`IEngine` and `ITire`) and their concrete implementations.
- The abstract factory interface (`IVehiclePartsFactory`) and its concrete factories (`SportsCarFactory` and `SuvFactory`).
- The client (`VehicleAssembler`), which uses the abstract factory interface to obtain products without directly depending on concrete classes.

