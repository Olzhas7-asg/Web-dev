class Animal:
    """
    Base class representing a generic animal.

    Attributes
    ----------
    name : str
        The animal's name.
    age : int
        The animal's age in years.
    species : str
        The species name.
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        self.name = name
        self.age = age
        self.species = species


    # Instance methods
    

    def speak(self) -> str:
        """Return a generic sound. Overridden by child classes."""
        return f"{self.name} makes a sound."

    def describe(self) -> str:
        """Return a short description of the animal."""
        return (
            f"{self.name} is a {self.age}-year-old {self.species}."
        )

    def birthday(self) -> None:
        """Increment the animal's age by one year."""
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")

    
    # Dunder methods
   

    def __str__(self) -> str:
        return f"Animal({self.name!r}, age={self.age}, species={self.species!r})"

    def __repr__(self) -> str:
        return self.__str__()



# Child class 1 — Dog


class Dog(Animal):
    """
    Represents a dog.

    Extra attributes
    ----------------
    breed : str
        The dog's breed.
    is_trained : bool
        Whether the dog is trained.
    """

    def __init__(self, name: str, age: int, breed: str,
                 is_trained: bool = False) -> None:
        super().__init__(name, age, species="Dog")
        self.breed = breed
        self.is_trained = is_trained

   
    # Overridden method
   

    def speak(self) -> str:
        """Dogs bark."""
        return f"{self.name} says: Woof! 🐕"

   
    # Unique methods
    

    def fetch(self, item: str = "ball") -> str:
        """Return a message about the dog fetching an item."""
        if self.is_trained:
            return f"{self.name} fetches the {item} and brings it back!"
        return f"{self.name} chases the {item} but doesn't bring it back."

    def describe(self) -> str:
        """Extended description including breed."""
        base = super().describe()
        trained_status = "trained" if self.is_trained else "not yet trained"
        return f"{base} Breed: {self.breed}. {trained_status.capitalize()}."

    def __str__(self) -> str:
        return (
            f"Dog({self.name!r}, age={self.age}, "
            f"breed={self.breed!r}, trained={self.is_trained})"
        )



# Child class 2 — Cat


class Cat(Animal):
    """
    Represents a cat.

    Extra attributes
    ----------------
    indoor : bool
        Whether the cat lives indoors.
    color : str
        The cat's coat color.
    """

    def __init__(self, name: str, age: int, color: str,
                 indoor: bool = True) -> None:
        super().__init__(name, age, species="Cat")
        self.color = color
        self.indoor = indoor

    
    # Overridden method
   

    def speak(self) -> str:
        """Cats meow."""
        return f"{self.name} says: Meow~ 🐈"

   
    # Unique methods

    def purr(self) -> str:
        """Return a purring message."""
        return f"{self.name} purrs contentedly... purrrrr ♡"

    def describe(self) -> str:
        """Extended description including color and lifestyle."""
        base = super().describe()
        lifestyle = "indoor" if self.indoor else "outdoor"
        return f"{base} Color: {self.color}. Lives {lifestyle}."

    def __str__(self) -> str:
        return (
            f"Cat({self.name!r}, age={self.age}, "
            f"color={self.color!r}, indoor={self.indoor})"
        )
