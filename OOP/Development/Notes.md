# Software Development

It consists of three (3) major steps:

1. Design
2. Implementation
3. Testing and Debugging

## Design

1. Decide workings of program into classes
2. How classes will interact
3. What data each class will store
4. What actions each class will perform

## Rules of Thumb:

1. Responsibilities
2. Independence
3. Behaviors

## Responsibilities

1. Different actors (division of labor)
2. Describe responsibilities using action verbs
3. Actors will be classes for the program

## Independence

1. Work for each class to be independent from others
2. Subdivide responsibilities between classes so that each class has autonomy over some aspect of the program
3. Give data to class with jurisdiction over actions that require access to this data

## Behaviors

1. Define behaviors of each class *carefully* and *precisely* so consequences of each action performed is well understood by other classes that interact with it
2. Behaviors will define methods that htis class performs
3. Set of behaviors for a class are the interface to the class, as they form the means for other pieces of code to interact with object from the class.

# Design Process

1. Iterates trough a action/actor cycle
2. Identify action (responsibility), then identify actor (component) to peform action
3. Design is complete when we have assigned all actions to actors
4. Using index cards guarantees small set of responsibilities (rember CRC's)

## UML Class Diagram

1. Consists of three portions: name, recommended instance variables, recommended methods of the class

# Testing and Debugging

1. Testing is to check correctneess of a program
2. Debugging is tracking execution of a program and discover errors in it

## Main strategies for testing

1. Top-down goes from the top to the bottom of the program hierarchy
2. Bottom-up goes from low level components to higher level
