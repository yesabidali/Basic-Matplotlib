## What is Paradigms?
Programming paradigms are different ways or styles in which a given program or programming language can be organized. Each paradigm consists of certain structures, features, and opinions about how common programming problems should be tackled

## Types of Programming Paradigms
- Imepative 
- Declarative
- Functional
- Object-Oriented Programming
- Hybrid
- Event-Driven 

<ins>Imperative</ins> : It provide detail instructions to achieve a task. It’s like giving a robot step-by-step commands to complete an action.

Example: In robotics, where precise control is essential, imperative programming ensures that every motor, sensor, and action follows a well-defined sequence

***Let's understand with Python code***

```
steps = ["Move forward", "Turn left", "Pick up object"]
for step in steps:
    print(f"Robot executing: {step}")
```
<ins>Declarative</ins> : Declarative programming focuses on what needs to be done, not how to do it. This abstraction simplifies complex operations

Example: In cloud infrastructure management, tools like Terraform let you declare the desired state of resources without worrying about implementation details. Or Famework Like React 

***Let's understand with code***

```
SELECT * FROM customers WHERE purchase_history > 1000;
```
<ins>Functional</ins> : Functional programming revolves around pure functions and immutability, making it ideal for concurrent and data-intensive applications.

Example: 
In AI pipelines, functional paradigms ensure predictable transformations, enabling reliable model training. Or Netflix remmondation engine

***Let’s understand with Python code***

``` 
def square(x):
    return x * x

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
```

<ins>Object-Oriented Programming OOP'S</ins> :  It uses objects and classes to structure software programs and increase reusability of code.

Example: Autonomous vehicles like Tesla rely on OOP to simulate environments.

***Let’s understand with Python code. How e-commerce plateform uses OOP's*** 

```
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name}: ${self.price}")

item = Product("Laptop", 999.99)
item.display_info()
```
<ins>Hybrid Paradigms</ins> : It follows Hybrid Approach and uses combinations programming paradigms. Like functional + OOP and Imperative + Declarative

Real World Example: Programing Languages like Python and Java Scripts using Hybrid Programming Paradigms

<ins>Event Driven Paradigms</ins> : Event Driven Programming (EDP) is a programming paradigm where the flow of the program is determined by events, such as user actions (mouse clicks, key presses)

Real World Example: JavaScript's best example for Event Driven Paradigms which makes it easy to respond to user interactions, such as clicking on a button, in real-time.

## Why Programming Paradigms matters

- Managing Complexity
- Enabling Scalabity
- Ensuring Maintainability

Managing Complexity: Modern software is more complex let's take a example of Social Media plateform it handle millions of active user and handle large data in real time

Enabling Scalabity: Scalabity is very essential for modern technologies. Let's take a example of e-commerce site. Amazon in Black Friday Sale it manage millions of transaction per second and update inventory Real time

Ensuring Maintainability: In large-scale projects, maintainability is key. Consider a project with a codebase consits hundreds of thousands of lines. 
Without a consistent paradigm, even minor updates can introduce bugs, slow development, and increase costs.