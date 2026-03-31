

from models import Animal, Dog, Cat


def print_separator(title: str = "") -> None:
    """Print a decorative separator with an optional title."""
    width = 60
    if title:
        print(f"\n{'=' * 5} {title} {'=' * (width - len(title) - 7)}")
    else:
        print("=" * width)


def demonstrate_basic_usage() -> None:
    """Create individual objects and call their methods."""
    print_separator("Creating Objects")

    # Base class instance
    generic = Animal("Generic", 3, "Unknown")
    print(generic)
    print(generic.describe())
    print(generic.speak())

    # Dog instance
    rex = Dog("Rex", 4, breed="German Shepherd", is_trained=True)
    print(rex)
    print(rex.describe())
    print(rex.speak())
    print(rex.fetch("stick"))

    # Cat instance
    whiskers = Cat("Whiskers", 2, color="Orange", indoor=True)
    print(whiskers)
    print(whiskers.describe())
    print(whiskers.speak())
    print(whiskers.purr())


def demonstrate_polymorphism(animals: list) -> None:
    """
    Polymorphism: call speak() on every animal.
    Each object responds differently despite the same method call.
    """
    print_separator("Polymorphism — speak()")
    for animal in animals:
        print(animal.speak())


def demonstrate_iteration(animals: list) -> None:
    """Iterate over a list of Animal objects."""
    print_separator("Iterating over animal list")
    for i, animal in enumerate(animals, start=1):
        print(f"  [{i}] {animal.describe()}")


def demonstrate_birthday(animals: list) -> None:
    """Demonstrate a shared method from the base class."""
    print_separator("Birthday!")
    for animal in animals:
        animal.birthday()


def main() -> None:
    """Entry point — runs all demonstrations."""
    print_separator("Lab 7 — OOP in Python")

  
    # 1. Instantiate objects from each class
   
    dog1 = Dog("Rex",    4, breed="German Shepherd", is_trained=True)
    dog2 = Dog("Buddy",  2, breed="Golden Retriever", is_trained=False)
    cat1 = Cat("Luna",   3, color="Black",  indoor=True)
    cat2 = Cat("Shadow", 5, color="Grey",   indoor=False)
    generic_animal = Animal("Parrot", 1, "Bird")

    # 2. Store objects in a list
  
    animals = [dog1, dog2, cat1, cat2, generic_animal]

    # 3. Iterate and describe
   
    demonstrate_iteration(animals)


    # 4. Polymorphism
   
    demonstrate_polymorphism(animals)

    
    # 5. Unique (child-class) methods

    print_separator("Dog-specific methods")
    for animal in animals:
        if isinstance(animal, Dog):
            print(animal.fetch())

    print_separator("Cat-specific methods")
    for animal in animals:
        if isinstance(animal, Cat):
            print(animal.purr())

  
    # 6. Birthday (inherited method)
  
    demonstrate_birthday(animals)

  
    # 7. isinstance / type checks — polymorphism reinforced
   
    print_separator("Type checking")
    dogs = [a for a in animals if isinstance(a, Dog)]
    cats = [a for a in animals if isinstance(a, Cat)]
    print(f"Total animals : {len(animals)}")
    print(f"Dogs          : {len(dogs)}")
    print(f"Cats          : {len(cats)}")
    

    print_separator("Done")


if __name__ == "__main__":
    main()
