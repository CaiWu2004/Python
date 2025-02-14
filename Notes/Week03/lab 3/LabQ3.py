snake_venomous = input("Is the snake venomous? (yes/no)" )
snake_size = input("is the snake small? (yes/no)" )
snake_mood = input("Is the snake aggressive? (yes/no)" )

if snake_venomous == "no":
    if snake_size == "yes":
        if snake_mood == "yes":
            print("This is a Matlab Mamba. Fun Fact: Commonly used to introduce mech-ies to working with snakes. They often hatch plots to catch their prey and enjoy graphical images.")
        else:
            print("This snake is a Verilog Viper. Fun Fact: Many people first see these snakes around architectures. Reports claim that they like to chew on circuit wires")
    else:
        if snake_mood == "yes":
            print("This is a C++ Cobra. Fun Fact: Evovled from the C serpents many years ago. Reports show they have weird habit of pointing at objects with their tails.")
        else:
            print("This snake is a C serpent. Fun Fact: Can be found in the sea. has the ability to control their memory, being able to allocate parts of their brain for certain tasks and permanently delete information form their memories")
else:
    if snake_size == "yes":
        if snake_mood == "yes":
            print("This snake is a Javascript Treesnake. Fun Fact: Despite its name, they are completely different from the Java Kingsnake. they like to lay on the nodes of a tree to browse through nearby animals for their next meal.")
        else:
            print( "This is a Java Kingsnake. Fun Facts: Very befitting of their name, they are objectively the most sophisticated snake species. One may even say they are very classy.")
    else:
        if snake_mood == "yes":
            print("This is a Assembly Anaconda. Fun Facts: Many people hate learning about these snakes, as they look very intimidating. In the Totally Official CS1114 Snake Register, they are said to love being in low level altitudes.")
        else:
            print( "This is a Python Python. Fun Facts: One of the largest and most famous snakes. However, they are pretty slow, and are commonly used to introduce people to learning about snakes.")

