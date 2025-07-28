---
name: "Workshop notes"
---

## Design Exercises

The Composite pattern is a fundamental structural pattern for handling tree-like hierarchies. Its core strength lies in providing a uniform interface for both individual objects (leaves) and collections of objects (composites). By applying this pattern, you can significantly simplify client code, improve flexibility, and make complex hierarchical structures easier to manage and extend. Understanding the trade-offs, particularly around the design of the Component interface (Uniformity vs. Type Safety), is important for effective implementation. This workshop provides hands-on experiences in object-oriented design using the Composite patterns.

---
#### Exercise A

Let's consider a real-world scenario: Manufacturing Bill of Materials (BOM). A complex product, like an aircraft engine, is assembled from various sub-assemblies (like a fan module, compressor module, combustion chamber), which are themselves made of smaller sub-assemblies or individual parts (like turbine blades, bolts, sensors).
- **Parts:** These are the basic, indivisible components (e.g., a specific type of bolt, a sensor, a fan blade). They have properties like a Part Number, Description, and Manufacturing Cost.
- **Assemblies:** These are collections of parts and/or other assemblies (e.g., a Fan Assembly consists of blades, a hub, and fasteners; the Engine itself is the top-level assembly). An assembly also has properties like an Assembly Number and Description, but its cost is derived from the cost of its constituent components plus any assembly-specific costs (like labour).

Now, imagine you need to write code to:
- Calculate the total manufacturing cost of the entire engine.
- Generate a detailed report listing all components (parts and assemblies) down to the lowest level.
- Find all components that require a specific quality check procedure.

Without a unifying pattern, your code would likely become messy:
- You'd need separate classes for `Part` and `Assembly`.
- Methods like `CalculateTotalCost` would need `if/else` statements or type checks (`is Part` or `is Assembly`) to handle the different types.
- Traversing the hierarchy (e.g., for the detailed report) would require recursive functions that constantly check the type of the current node.

This leads to code that is hard to maintain, extend, and understand. If you introduce a new type (e.g., `Kit`, which is a packaged set of parts but not a full assembly), you'd have to modify all these conditional checks.

The Composite pattern introduces a shared abstraction (an interface or abstract class) that both individual objects (Leaves) and group objects (Composites) implement:

- **Component:**
    - Declares the interface for objects in the composition.
    - Provides a common interface for both Leaves and Composites.
    - May implement default behaviour for common operations.
    - (Optional but common) Declares an interface for accessing and managing child components (Add, Remove, GetChild).
- **Leaf:**
    - Represents the individual, indivisible objects in the composition (e.g., `Part`).
    - Implements the `Component` interface.
    - Has no children, so methods related to child management (Add, Remove) are typically not meaningful (they might do nothing or throw an exception).
    - Defines the behaviour for primitive objects.
- **Composite:**
    - Represents the complex objects that can contain children (e.g., `Assembly`).
    - Implements the `Component` interface.
    - Stores child components (Leaves or other Composites).
    - Implements child-related operations from the `Component` interface.
    - Implements operations defined in the `Component` interface by delegating them to its children (e.g., calculating cost by summing the costs of its children).
- **Client:**
    - Manipulates objects in the composition through the `Component` interface.
    - Doesn't need to (and ideally shouldn't) distinguish between Leaf and Composite objects when performing operations defined in the `Component` interface.

We can apply the Composite patten to the BOM Scenario. Your task is to create a class diagram then implement the classes in C#, following these steps:

- **Component:** `IProductComponent` (interface or abstract class)
    - Defines operations like `string GetName()`, `decimal CalculateCost()`, `void DisplayDetails(int indentLevel)`.
    - _Maybe_ defines `Add(IProductComponent component)`, `Remove(IProductComponent component)`. (We'll discuss the placement trade-offs later).
- **Leaf:** `Part` class
    - Implements `IProductComponent`.
    - Stores `partNumber`, `description`, `cost`.
    - `CalculateCost()` returns its direct `cost`.
    - `Add`/`Remove` would likely throw `NotSupportedException` if defined in the interface.
    - `DisplayDetails()` prints its own info.
- **Composite:** `Assembly` class
    - Implements `IProductComponent`.
    - Stores `assemblyNumber`, `description`, `assemblySpecificCost` (e.g., labour).
    - Contains a `List<IProductComponent>` to hold its children.
    - Implements `Add`, `Remove` to manage the children list.
    - `CalculateCost()` returns `assemblySpecificCost` plus the sum of `CalculateCost()` called on all its children.
    - `DisplayDetails()` prints its info and then recursively calls `DisplayDetails()` on its children.

---
#### Exercise B

In the previous tutorial, we explored the Composite pattern using a Bill of Materials example. We touched upon a key design decision: where to declare the methods for managing child components (like `Add`, `Remove`, `GetChild`). This decision impacts whether you prioritise:

1. **Uniformity:** Treating leaves and composites identically through the `Component` interface, even for child management operations (which leaves typically don't support).
2. **Type Safety:** Ensuring that child management operations can _only_ be called on objects that can actually have children (composites), often requiring clients to perform type checks or casts.

To understand the practical trade-offs, this exercise will guide you through implementing _both_ variants for the same scenario to compare and contrast the Uniformity and Type Safety approaches in the Composite pattern by implementing and analysing both.

In the following scenario, we'll model a simple organisational chart with hierarchy:

- **`IOrganizationUnit`:** The `Component` interface. All elements in the hierarchy will implement this. It needs a way to display the hierarchy.
- **`Employee`:** The `Leaf` class. Represents an individual employee with a name and title. Cannot contain other units.
- **`Department`:** The `Composite` class. Represents a department with a name, which can contain `Employee`s and other `Department`s.
 
There are some core operations to be considered:

- `Display(int indentLevel)`: To print the hierarchy structure.
- `AddUnit(IOrganizationUnit unit)`: To add a unit (Employee or Department) to a Department.
- `RemoveUnit(IOrganizationUnit unit)`: To remove a unit from a Department.

The critical difference between our two variants will be where `AddUnit` and `RemoveUnit` are declared.

###### Variant 1: Uniformity

In this variant, we place the child management operations (`AddUnit`, `RemoveUnit`) directly into the `Component` interface (`IOrganizationUnit`). This allows clients to attempt these operations on any `IOrganizationUnit` object. Leaves must provide an implementation, typically by throwing an exception.

Create a class diagram to represent your design, and *optionally* implement these classes in C#.

###### Variant 2: Type Safety

In this variant, child management operations (`AddUnit`, `RemoveUnit`) are declared _only_ in the `Composite` class (`Department`). They are _not_ part of the `Component` interface (`IOrganizationUnit`). Clients _must_ know they have a `Department` object (and likely cast to it) to modify its children.

Create a class diagram to represent your design, and *optionally* implement these classes in C#.

###### Comparison Summary

| **Feature**              | **Uniformity Variant**                                  | **Type Safety Variant**                                        |
| ------------------------ | ------------------------------------------------------- | -------------------------------------------------------------- |
| **Interface Design**     | `Component` includes child management (`Add`, `Remove`) | `Component` excludes child management                          |
| **Leaf Implement.**      | Must implement `Add`/`Remove` (e.g., throw exception)   | Does not implement `Add`/`Remove`                              |
| **Composite Implement.** | Implements `Add`/`Remove` from interface                | Implements `Add`/`Remove` as its own methods                   |
| **Client: Read Ops**     | Uniform (e.g., `Display()` called via interface)        | Uniform (e.g., `Display()` called via interface)               |
| **Client: Modify Ops**   | Can call `Add`/`Remove` on interface ref (risky)        | _Must_ check type & cast to `Composite` to call `Add`/`Remove` |
| **Error Handling**       | Runtime `NotSupportedException` on Leaf                 | Compile-time errors if calling on Leaf                         |
| **Primary Advantage**    | Simpler client code _if_ modifying known composites     | Prevents misuse of Leaves at compile time                      |
| **Primary Drawback**     | Runtime errors possible; "fat" interface                | More complex client code for modifications                     |
