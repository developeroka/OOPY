# OOP Design Goals

## Robustness

* Having the right output for anticipated inputs.
* Able to handle unexpected inputs not explicitly defined for its application.

## Adaptability

* Able to evolve over time in response to changing conditions in its environment.
* Ability of software to run with minimal change on different hardware and OS platform.

## Reusability

* Same code should be usable as a component of different systems in various applications

# OOP Design Goals Facilitators

## Modularity

1. Different components must interact correctly
2. Different components must be well organized
3. Different components are divided into separate functional units
4. Collection of closely related functions and classed defined together in a single file
5. Support Robustness; it's easier to test & debug separate components before integration
6. Structure imposed by modularity helps enable software reusability

## Abstraction

1. Distill to fundamental parts
2. Involves naming and explaining functionality
3. Abstract Data Types (ADT) is a mathematical model of a Data Structure that specifies the data stores, the operations supported and types of parameters of operations; **specifies what** each operation does **but not how**.

## Encapsulation

1. Components shouldn't reveal internal details of implementation
2. Freedom to implement details of components without concern that other programmer will write code that depends on those details
3. Yields robustness and adaptability because it allows implementation details of parts of the program to change without affecting other parts, thus making it easier to fix bugs or add new functionality with local changes to a component.
4. Python provides loose support for encapsulation (`_var` is assumed non-public)