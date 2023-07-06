# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

class Ancestral_Stories:
    def __init__(self, story_title, age_group, moral_lessons):
        self.story_title = story_title
        self.age_group = age_group
        self.moral_lessons = moral_lessons
    def folk_tell_story(self):
        return f"Once upon a time, in a land far away, there was a {self.story_title}, a captivating tale that imparts valuable moral lessons to {self.age_group}."
class Story(Ancestral_Stories):
    def __init__(self, story_title, age_group, moral_lessons, length):
        super().__init__(story_title, age_group, moral_lessons)
        self.length = length
    def get_story(self):
        return f"Once upon a time, in a land of {self.story_title}, there lived a brave hero who embarked on a quest to save the kingdom from impending doom. This {self.length}-page story is filled with suspense, action, and important life lessons."
class Story_Teller(Ancestral_Stories):
    def __init__(self, story_title, age_group, moral_lessons, name_story_teller):
        super().__init__(story_title, age_group, moral_lessons)
        self.name_story_teller = name_story_teller
    def tell_story(self):
        return f"Welcome, dear listeners! I am {self.name_story_teller}, a skilled storyteller. Today, I will transport you to the magical world of {self.story_title}. Prepare to be captivated by the enchanting characters, moral teachings, and the power of imagination."
class Translator(Ancestral_Stories):
    def __init__(self, story_title, age_group, moral_lessons, language):
        super().__init__(story_title, age_group, moral_lessons)
        self.language = language
    def translate(self):
        return f"Behold, the tale of {self.story_title} translated into {self.language}! Through the art of translation, we bring this timeless story to a wider audience, spreading its profound moral lessons and cultural richness."
# Create an instance of Ancestral_Stories
ancestral_story = Ancestral_Stories("The Magical Forest", "Children", "Respect for Nature")
# Create an instance of Story
story = Story("The Hero's Journey", "Young Adults", "Courage, Perseverance", 100)
# Create an instance of Story_Teller
storyteller = Story_Teller("The Chronicles of Narnia", "All Ages", "Friendship, Imagination", "Lucy")
# Create an instance of Translator
# translator = Translator("Cinderella", "Children", "Kindness, Resilience", "French")
translator = Translator("The Lion King", "Children", "Courage, Identity", "Spanish")
# Access the methods of each class
print(ancestral_story.folk_tell_story())
print(story.get_story())
print(storyteller.tell_story())
print(translator.translate())

# PseudoCode
# input = moral_Lesson, length, age_group,name
# output = transalating the stories in differnet languages
# process = create a class containing the attributes, identify its different
#  characters together with the one they have in common and come up with the methods needed

class AncestralStories:
    def __init__(self,moral_lesson, age_group,name):
        self.name = name
        self.moral_Lesson = moral_lesson 
        self.age_group = age_group
      
    def story_info(self):
        return f"${self.name} is a great book with an informative ${self.moral_lesson}"
    
class Story(AncestralStories):
    def __init__(self,moral_lesson, age_group,name, length):
        super.__init__(self,moral_lesson, age_group,name)
        self.length = length

    def get_story(): 
        return f"The story "  
    

class StoryTeller(AncestralStories):
    def __init__(self,moral_lesson, age_group,name, length):
        super().__init__(self,moral_lesson, age_group,name)
        self.length = length

    def tell_story(): 
        return f"The story "   
       

class TranslatorObject(AncestralStories) :
    def __init__(self,moral_lesson, age_group,name, length):
        super().__init__(self,moral_lesson, age_group,name)
        self.length = length

    def translate(): 
        return f"The story "  




# 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

# 3. **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to
# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

class Wildlife{
    constructor() {
      this.lifespan = 0;
      this.prey_migration = false;
      this.carnivore = ["lion", "leopard", "jaguar", "hyena"];
      this.omnivore = ["bear", "raccoon"];
      this.herbivore = ["sheep", "goat", "cow", "giraffe", "gazelle"];
      this.prey = [];
      this.predator = [];
      this.predator_migration = true;
    }
    predators_prey(animal_name) {
      if (this.carnivore.includes(animal_name)) {
        this.predator.push(animal_name);
        return `${animal_name} is a predator.`;
      } else {
        this.prey.push(animal_name);
        return `${animal_name} is a prey.`;
      }
    }
    animal_lifespan(animal_name) {
      if (this.carnivore.includes(animal_name)) {
        this.lifespan = "0-15";
      } else if (this.omnivore.includes(animal_name)) {
        this.lifespan = "0-25";
      } else if (this.herbivore.includes(animal_name)) {
        this.lifespan = "0-30";
      } else {
        return `${animal_name} is not found.`;
      }
      return this.lifespan;
    }
    track_migration(animal_name) {
      if (this.prey.includes(animal_name)) {
        this.prey_migration = true;
        if (this.prey_migration) {
          this.predator_migration = true;
          return `${animal_name} is migrating.`;
        } else {
          this.predator_migration = false;
        }
      } else {
        this.predator_migration = false;
        return `${animal_name} is not found.`;
      }
    }
  }
let wildlife = new Wildlife();
console.log(wildlife.predators_prey("lion"));
console.log(wildlife.predators_prey("deer"));
console.log(wildlife.animal_lifespan("tiger"));
console.log(wildlife.track_migration("bear"));
console.log(wildlife.track_migration("elephant"));




# 4. **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.


# 5. Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.
# 6. Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.

# 7. Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.

# 8. Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.


// **Wildlife Preservation:** You're a wildlife conservationist working on a
// program to track different species in a national park. Each species has its own
// characteristics and behaviors, such as its diet, typical lifespan, migration
// patterns, etc. Some species might be predators, others prey. You'll need to
// create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
// these classes might relate to each other through inheritance.
class Wildlife {
    constructor() {
      this.lifespan = 0;
      this.prey_migration = false;
      this.carnivore = ["lion", "leopard", "jaguar", "hyena"];
      this.omnivore = ["bear", "raccoon"];
      this.herbivore = ["sheep", "goat", "cow", "giraffe", "gazelle"];
      this.prey = [];
      this.predator = [];
      this.predator_migration = true;
    }
    predators_prey(animal_name) {
      if (this.carnivore.includes(animal_name)) {
        this.predator.push(animal_name);
        return `${animal_name} is a predator.`;
      } else {
        this.prey.push(animal_name);
        return `${animal_name} is a prey.`;
      }
    }
    animal_lifespan(animal_name) {
      if (this.carnivore.includes(animal_name)) {
        this.lifespan = "0-15";
      } else if (this.omnivore.includes(animal_name)) {
        this.lifespan = "0-25";
      } else if (this.herbivore.includes(animal_name)) {
        this.lifespan = "0-30";
      } else {
        return `${animal_name} is not found.`;
      }
      return this.lifespan;
    }
    track_migration(animal_name) {
      if (this.prey.includes(animal_name)) {
        this.prey_migration = true;
        if (this.prey_migration) {
          this.predator_migration = true;
          return `${animal_name} is migrating.`;
        } else {
          this.predator_migration = false;
        }
      } else {
        this.predator_migration = false;
        return `${animal_name} is not found.`;
      }
    }
  }
  let wildlife = new Wildlife();
  console.log(wildlife.predators_prey("lion"));
  console.log(wildlife.predators_prey("deer"));
  console.log(wildlife.animal_lifespan("tiger"));
  console.log(wildlife.track_migration("bear"));
  console.log(wildlife.track_migration("elephant"));
//   **African Cuisine:** You're creating a recipe app specifically for African cuisine.
// The app needs to handle recipes from different African countries, each with its
// unique ingredients, preparation time, cooking method, and nutritional
// information. Consider creating a `Recipe` class, and think about how you might
// create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
// `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
// methods.
class Recipes {
  constructor() {
    this.recipes = [];
    this.ingredients = {};
    this.prepTime = {};
    this.cookingMethod = {};
    this.nutritionalInfo = {};
  }
  addRecipe(nameRecipe, listOfIngredients, prepTime, cookingMethod, nutritionalInfo) {
    if (nameRecipe && listOfIngredients && prepTime && cookingMethod && nutritionalInfo) {
      this.recipes.push(nameRecipe);
      this.ingredients[nameRecipe] = listOfIngredients;
      this.prepTime[nameRecipe] = prepTime;
      this.cookingMethod[nameRecipe] = cookingMethod;
      this.nutritionalInfo[nameRecipe] = nutritionalInfo;
      return "Recipe added successfully";
    } else {
      return "Fill all needed fields";
    }
  }
  getRecipe(nameRecipe) {
    if (this.recipes.includes(nameRecipe)) {
      return `${nameRecipe}\nIngredients:\n${this.ingredients[nameRecipe]}\nPrep Time:\n${this.prepTime[nameRecipe]}\nCooking Method:\n${this.cookingMethod[nameRecipe]}\nNutritional Information:\n${this.nutritionalInfo[nameRecipe]}`;
    } else {
      return `${nameRecipe} not found`;
    }
  }
}
const recipeBook = new Recipes();
console.log(recipeBook.addRecipe(
  "Chocolate Cake",
  ["flour", "sugar", "cocoa powder", "baking powder", "eggs", "milk", "vegetable oil", "vanilla extract"],
  "1 hour",
  "Baking",
  "Calories: 350 per serving"
));
console.log(recipeBook.addRecipe(
  "Spaghetti Carbonara",
  ["spaghetti", "bacon", "eggs", "Parmesan cheese", "black pepper", "salt"],
  "30 minutes",
  "Boiling, frying",
  "Calories: 450 per serving"
));
console.log(recipeBook.getRecipe("Chocolate Cake"));
console.log(recipeBook.getRecipe("Spaghetti Carbonara"));
console.log(recipeBook.getRecipe("Pancakes"));
// **African Music Festival:** You're in charge of organizing a Pan-African music
//  festival. Many artists from different countries, each with their own musical style
//  and instruments, are scheduled to perform. You need to write a program to
// manage the festival lineup, schedule, and stage arrangements. Think about how
// you might model the `Artist`, `Performance`, and `Stage` classes, and consider
// how you might use inheritance if there are different types of performances or
// stages.
class MusicFestival {
  constructor() {
    this.artists = [];
    this.genre = ['hiphop', 'reggae', 'R&B', 'acoustic'];
    this.instruments = [];
    this.lineUp = [];
  }
}
class Stage extends MusicFestival {
  constructor() {
    super();
    this.lights = 'white';
    this.instrument = ['Drum', 'microphone'];
  }
  addToLineUp(musicType) {
    if (this.genre.includes(musicType)) {
      this.lineUp.push(musicType);
    } else {
      return 'This music type is not available';
    }
  }
  stageManagement() {
    if (this.genre == 'hip hop') {
      this.lights = 'Blue lights';
      return this.lights;
    } else if (this.genre == 'reggae') {
      this.lights = 'Green lights';
      return this.lights;
    } else if (this.genre == 'R&B') {
      this.lights = 'Bright lights';
      return this.lights;
    } else {
      return this.lights;
    }
  }
  instrumentAssign() {
    if (this.genre == 'hiphop') {
      this.instrument.push('bass');
      return this.instrument;
    } else if (this.genre == 'R&B') {
      this.instrument.push('saxophone');
      return this.instrument;
    } else if (this.genre == 'reggae') {
      this.instrument.push('lead');
      return this.instrument;
    } else {
      return this.instrument;
    }
  }
}
const festival = new MusicFestival();
const stage = new Stage();
stage.addToLineUp('hiphop');
stage.addToLineUp('reggae');
console.log(stage.lineUp);
console.log(stage.stageManagement());
console.log(stage.instrumentAssign());
// #**Ancestral Stories:** In many African cultures, the art of storytelling is passed
//  down from generation to generation. Imagine you're creating an application that
// records these oral stories and translates them into different languages. The
// stories vary by length, moral lessons, and the age group they are intended for.
// Think about how you would model `Story`, `StoryTeller`, and `Translator`
// objects, and how inheritance might come into play if there are different types of
// stories or storytellers.
class Story {
  constructor(title, genre, length, moralLessons, groupAge, language) {
    this.title = title;
    this.genre = genre;
    this.length = length;
    this.moralLessons = moralLessons;
    this.groupAge = groupAge;
    this.language = language;
  }
  translate(expectedLanguage) {
    this.expectedLanguage = expectedLanguage;
    if (this.language !== expectedLanguage) {
      console.log(`Translate "${this.title}" into ${this.expectedLanguage}`);
    } else {
      console.log(`The story "${this.title}" is already in ${this.expectedLanguage}`);
    }
  }
}
const story = new Story("Born a crime", "setbook", "1hr", "respecting the elders", 18, "Swahili");
story.translate("English");
class StoryTeller extends Story {
  constructor(title, genre, length, moralLessons, groupAge, language, name, nationality, storytellerAge) {
    super(title, genre, length, moralLessons, groupAge, language);
    this.storytellerAge = storytellerAge;
    this.name = name;
    this.nationality = nationality;
  }
  StoryTellerDetails() {
    console.log(`${this.title} was written by ${this.name} from ${this.nationality} and they are ${this.storytellerAge} years old.`);
  }
}
const storyTeller = new StoryTeller(
  "Decolonize mind",
  "trickster",
  "1hr",
  "being creative",
  21,
  "English",
  "Ngugi wa Thiong'o",
  "Kenyan",
  56
);
storyTeller.StoryTellerDetails();
// Create a class called Product with attributes for name, price, and quantity.
// Implement a method to calculate the total value of the product (price * quantity).
// Create multiple objects of the Product class and calculate their total values
class Product{
  constructor(name,price,quantity){
    this.name=name
    this.price=price
    this.quantity=quantity
  }
  calculateTotalValue(){
    let totalValue = 0
    if(this.name && this.price && this.quantity){
      totalValue = this.price * this.quantity
      return totalValue
    }
    else {
      return null
    }
  }
}
const product1 = new Product("Apples", 0.5, 10);
const product2 = new Product("Bananas", 0.3, 15);
const product3 = new Product("Oranges", 0.4, 8);
console.log(`Total value of ${product1.name}: $${product1.calculateTotalValue()}`);
console.log(`Total value of ${product2.name}: $${product2.calculateTotalValue()}`);
console.log(`Total value of ${product3.name}: $${product3.calculateTotalValue()}`);
// Implement a class called Student with attributes for name, age, and grades (a
// list of integers). Include methods to calculate the average grade, display the
// student information, and determine if the student has passed (average grade >=
// 60). Create objects for the Student class and demonstrate the usage of these
//  methods.
class Student{
  constructor( name, age, grades){
      this.name = name
      this.age = age
      this. grades = grades
      this.avg_grade = ""
      this.above_avg = {}
      this.below_avg = {}
  }
  average_grade(){
    let total = 0
    for(let i = 0 ; i <= this.grades.length ; i++){
      total += i
    }
      let average = total / this.grades.length
      this.avg_grade = average
      return average
  }
  information(name){
      if( name == this.name){
          return `${name} is ${this.age} and had a mean score of ${this.avg_grade}`}
  }
  score(){
      if( this.avg_grade >= 60){
          this.above_avg[this.name] = this.avg_grade
          return this.above_avg
      }
      else{
        this.below_avg[this.name] = this.average_grade
        return this.below_avg
      }
  }
}
let student1 = new Student("Mary", 22, [22,56,80,87,98])
console.log(student1.average_grade())
console.log(student1.information("Mary"))
console.log(student1.score())





8:35
# **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.
# pseudo code
# input
# story:title,genre,moral_lesson,age_group
# storyTeller:name, nationality,  age
# translator:languages
# process
# create a main class=story
# sub-class=storyTeller-tittle
# output
# translated stories
# storyteller details
class Story:
    def __init__(self):
        self.stories = []
    def add_story(self, title, genre, language, length_of_story, moral_of_story, age_group, content):
        if genre and language and length_of_story and moral_of_story and age_group and content and title:
            story = {
                "title": title,
                "language": language,
                "genre": genre,
                "length_of_story": length_of_story,
                "moral_of_story": moral_of_story,
                "age_group": age_group,
                "content": content
            }
            self.stories.append(story)
            print(f"{title} added successfully.")
        else:
            print("Please add all fields")
    def translate_story(self, expected_language, title):
        for story in self.stories:
            if story["title"] == title:
                if expected_language != story["language"]:
                    story["language"] = expected_language
                    print(f"The story titled {title} has been translated to {expected_language}.")
                else:
                    print(f"The story titled {title} is already in {expected_language}.")
                return
        print(f"{title} not found.")
class StoryTeller:
    def __init__(self):
        self.storyteller_details = []
        self.story = {}
    def add_storyteller_details(self, story, name, age, nationality):
        if story and name and age and nationality:
            self.story["name"] = name
            self.story["age"] = age
            self.story["nationality"] = nationality
            self.story["story"] = story
            self.storyteller_details.append(self.story)
        else:
            print("Storyteller not added.")
    def view_storyteller_details(self, story):
        for storyteller in self.storyteller_details:
            if storyteller["story"] == story:
                print(storyteller)
                return
        print(f"{story} not found.")
if __name__ == "__main__":
    story_app = Story()
    storyteller_app = StoryTeller()
    story_app.add_story("The Lion and the Mouse", "Fable", "English", "Short", "Helping Others", "Children",
                        "Once upon a time, there was a lion who was asleep in the forest...")
    storyteller_app.add_storyteller_details("The Lion and the Mouse", "John Smith", 40, "USA")
    story_app.translate_story("French", "The Lion and the Mouse")
    storyteller_app.view_storyteller_details("The Lion and the Mouse")
class Recipes:
    def __init__(self):
        self.recipes = []
        self.ingredients = {}
        self.prep_time = {}
        self.cooking_method = {}
        self.nutritional_info = {}
    def add_recipe(self, name_recipe, list_of_ingredients, prep_time, cooking_method, nutritional_info):
        if name_recipe and list_of_ingredients and prep_time and cooking_method and nutritional_info:
            self.recipes.append(name_recipe)
            self.ingredients[name_recipe] = list_of_ingredients
            self.prep_time[name_recipe] = prep_time
            self.cooking_method[name_recipe] = cooking_method
            self.nutritional_info[name_recipe] = nutritional_info
            return "Recipe added successfully"
        else:
            return "Fill all needed fields"
    def get_recipe(self, name_recipe):
        if name_recipe in self.recipes:
            return f"{name_recipe}\nIngredients: {self.ingredients[name_recipe]}\nPrep Time: {self.prep_time[name_recipe]}\nCooking Method: {self.cooking_method[name_recipe]}\nNutritional Information: {self.nutritional_info[name_recipe]}"
        else:
            return f"{name_recipe} not found"
recipe_book = Recipes()
recipe_book.add_recipe(
    "Pasta Carbonara",
    ["Spaghetti", "Eggs", "Bacon", "Parmesan Cheese", "Black Pepper"],
    "20 minutes",
    "Boiling, frying",
    "Calories: 450, Protein: 15g, Fat: 20g, Carbs: 50g"
)
recipe_book.add_recipe(
    "Chicken Stir-Fry",
    ["Chicken Breast", "Bell Peppers", "Broccoli", "Soy Sauce", "Garlic", "Ginger"],
    "30 minutes",
    "Stir-frying",
    "Calories: 350, Protein: 25g, Fat: 10g, Carbs: 40g"
)
print(recipe_book.get_recipe("Pasta Carbonara"))
print(recipe_book.get_recipe("Chicken Stir-Fry"))
print(recipe_book.get_recipe("Nonexistent Recipe"))
class Wildlife:
    def __init__(self):
        self.lifespan = 0
        self.prey_migration = False
        self.carnivores = []
        self.omnivores = []
        self.herbivores = []
        self.prey = []
        self.predators = []
        self.predator_migration = True
    def predators_prey(self, animal_name):
        if animal_name in self.carnivores:
            self.predators.append(animal_name)
            return f"{animal_name} is a predator"
        else:
            self.prey.append(animal_name)
            return f"{animal_name} is a prey"
    def animal_lifespan(self, animal_name):
        if animal_name in self.carnivores:
            self.lifespan = range(0, 16)
        elif animal_name in self.omnivores:
            self.lifespan = range(0, 26)
        elif animal_name in self.herbivores:
            self.lifespan = range(0, 31)
        return self.lifespan
    def track_migration(self, animal_name):
        if animal_name in self.prey:
            self.prey_migration = True
            if self.prey_migration:
                self.predator_migration = True
                return f"{animal_name} is migrating"
            else:
                self.predator_migration = False
        else:
            self.predator_migration = False
            self.prey_migration = False
            return f"{animal_name} is not found"
wildlife = Wildlife()
wildlife.carnivores.extend(["Lion", "Tiger", "Wolf"])
wildlife.omnivores.extend(["Bear", "Raccoon"])
wildlife.herbivores.extend(["Deer", "Elephant"])
print(wildlife.predators_prey("Lion"))
print(wildlife.predators_prey("Deer"))
print(wildlife.animal_lifespan("Tiger"))
print(wildlife.track_migration("Bear"))
print(wildlife.track_migration("Elephant"))
class MusicFestival:
    def __init__(self):
        self.artists = []
        self.genres = ['hiphop', 'reggae', 'R&B', 'acoustic']
        self.instruments = []
        self.lineup = []
class Stage(MusicFestival):
    def __init__(self):
        super().__init__()
        self.lights = "white"
        self.instruments = ["Drum", "microphone"]
    def add_to_lineup(self, music_type):
        if music_type in self.genres:
            self.lineup.append(music_type)
        else:
            return "This music type is not available"
    def stage_management(self):
        if self.lineup:
            current_genre = self.lineup[-1]
            if current_genre == 'hiphop':
                self.lights = "Blue lights"
            elif current_genre == 'reggae':
                self.lights = "Green lights"
            elif current_genre == 'R&B':
                self.lights = "Bright lights"
        return self.lights
    def instrument_assign(self):
        if self.lineup:
            current_genre = self.lineup[-1]
            if current_genre == "hiphop":
                self.instruments.append('bass')
            elif current_genre == "R&B":
                self.instruments.append('saxophone')
            elif current_genre == 'reggae':
                self.instruments.append('lead')
        return self.instruments
festival = MusicFestival()
stage = Stage()
stage.add_to_lineup('hiphop')
stage.add_to_lineup('reggae')
print(stage.lineup)
print(stage.stage_management())
print(stage.instrument_assign())
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_value(self):
        total_value=0
        if self.name and self.price and self.quantity:
            total_value = self.price * self.quantity
            return total_value
        else:
            return None
product1 = Product("Phone", 50000, 2)
product2 = Product("Laptop", 500000, 1)
product3 = Product("Headphones", 2000, 5)
print(product1.calculate_total_value())
print(product2.calculate_total_value())
print(product3.calculate_total_value())
# Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self. grades = grades
        self.avg_grade = ""
        self.above_avg = {}
        self.below_avg = {}
    def average_grade(self):
        average = sum(self.grades) / len(self.grades)
        self.avg_grade = average
        return average
    def information(self, name):
        if name == self.name:
            return f'{name} is {self.age} and had a mean score of {self.avg_grade}'
    def score(self):
        if self.avg_grade >= 60:
            self.above_avg[self.name] = self.avg_grade
            return self.above_avg
        else :
            self.below_avg[self.name] = self.average_grade
            return self.below_avg
student1 = Student("Mary", 22, [22,56,80,87,98])
print(student1.average_grade())
print(student1.information("Mary"))
print(student1.score())