# Tamagotchi Terminal Game
class Tamagotchi:
    def __init__(self, name, hunger=0, tiredness=0, boredom=0, dirtiness=0):
        self.name = name
        self.hunger = hunger
        self.tiredness = tiredness
        self.boredom = boredom
        self.dirtiness = dirtiness
        self.display = self.display_sleep()
    
    def _pass_time(self):
        self.hunger += 1
        self.tiredness += 1
        self.boredom += 1
        self.dirtiness += 1
    
    def _is_tired(self):
        return self.tiredness >= 10
    
    def _is_hungry(self):
        return self.hunger >= 10
    
    def _is_bored(self):
        return self.boredom >= 10
    
    def _is_dirty(self):
        return self.dirtiness >= 10
    
    def _is_sick(self):
        return self._is_tired() and self._is_hungry() and self._is_bored() and self._is_dirty()
    
    def _is_dead(self):
        return self.hunger >= 20 or self.tiredness >= 20 or self.boredom >= 20 or self.dirtiness >= 20
    
    def play(self):
        self.boredom -= 2
        self.tiredness += 1
        self.display = self.display_happy()
        self._pass_time()
    
    def eat(self):
        self.hunger -= 2
        self.dirtiness += 1
        self.display = self.display_eating()
        self._pass_time()
    
    def sleep(self):
        self.tiredness -= 2
        self.display = self.display_sleep()
        self._pass_time()
    
    def clean(self):
        self.dirtiness -= 2
        self.display = self.display_happy()
        self._pass_time()
    
    def report(self):
        print(f"{self.name} Report:")
        print(f"Hunger: {self.hunger}")
        print(f"Tiredness: {self.tiredness}")
        print(f"Boredom: {self.boredom}")
        print(f"Dirtiness: {self.dirtiness}")
        if self._is_sick():
            self.display = self.display_sick()
            print(f"{self.name} is sick!")
        if self._is_dead():
            self.display = self.display_dead()
            print(f"{self.name} is dead!")
            restart()

    def display_eating(self):
        return('''
            /\_/\\
            ( o.o )
              >^<
        ''')
    def display_shocked(self):
        return('''
            /\_/\\
            ( o.o )
            (")_(")
        ''')
    def display_happy(self):
        return ('''
            /\_/\\
            ( ^.^ )
            C(")(")
        ''')
    def display_sick(self):
        return ('''
            /\_/\\
            ( @.@ )
            C(")(")
        ''')
    def display_sleep(self):
        return ('''
            /\_/\\
            ( -.- )
            C(")(")
        ''')
    def display_dead(self):
        return ('''
            /\_/\\
            ( X.X )
            C(")(")
        ''')

def restart():
    print("\nDo you want to restart?")
    print("1. Yes")
    print("2. No")
    choice = input("> ")
    if choice == "1":
        play_game()
    elif choice == "2":
        print(f"Goodbye!")

def play_game():
    name = input("What do you want to name your Tamagotchi?\n")
    pet = Tamagotchi(name)
    
    while not pet._is_dead():
        print(pet.display)
        print("What do you want to do with your Tamagotchi?\n")
        print("1. Play")
        print("2. Eat")
        print("3. Sleep")
        print("4. Clean")
        print("5. Quit")
        choice = input("> ")
        
        if choice == "1":
            pet.play()
        elif choice == "2":
            pet.eat()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.clean()
        elif choice == "5":
            print(f"Goodbye, {pet.name}!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        pet.report()
    
play_game()