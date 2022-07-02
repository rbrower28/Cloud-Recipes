import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from recipe import Recipe


class Database:

    def __init__(self):
        """ Sets up the connection to the firebase cloud storage.
        Separates the meals, desserts, and snacks collections into
        their own variables for reference.
        """

        self.cred = credentials.Certificate("cloud-recipes-rbrower-d83cf795140d.json")
        firebase_admin.initialize_app(self.cred)

        self.db = firestore.client()

        self.meals = self.db.collection("meals")
        self.desserts = self.db.collection("desserts")
        self.snacks = self.db.collection("snacks")


    def set_recipe(self):
        """ Creates a new instance of Recipe and populates it
        with the necessary information. The firebase_admin
        library then uses the dict format to populate a document
        for the NoSQL database.
        """

        rec_name = input("What is your recipe for? ").capitalize()

        print("What kind of food is this?")
        print("1. Meal \n2. Dessert \n3. Snack")
        collection_num = input()
        collection_dict = {"1": self.meals, "2": self.desserts, "3": self.snacks}

        # Creates a new document in the right place
        doc = collection_dict[collection_num].document(rec_name)

        # Gets ingredients until the user types Q to end
        resp = None
        rec_ingredients = []

        print("Please type the ingredients: (Q to end)")
        while resp != "Q":
            resp = input()
            if resp != "Q":
                rec_ingredients.append(resp)

        # Gets instructions until the user types Q to end
        resp = None
        rec_instructions = {}
        count = 1

        print("Please type the instructions: (Q to end)")
        while resp != "Q":
            resp = input()
            if resp != "Q":
                rec_instructions[str(count)] = resp
                count += 1

        # Generates new instance of Recipe
        recipe = Recipe(
            name=rec_name,
            ingredients=rec_ingredients,
            instructions=rec_instructions
        )

        # Displays the dict format to user and stores it on the cloud.
        print(recipe.to_dict())
        doc.set(recipe.to_dict())


    def get_recipes(self, collection=""):
        """ Retrieves the recipes from the cloud and displays them
        for us. If the collection is specified, it will just retreive
        the recipes from that collection. If not, it will just get
        all the recipes in their sections.
        """

        if collection:
            collections_dict = {"1": self.meals, "2": self.desserts, "3": self.snacks}
            docs = collections_dict[collection].stream()

            for doc in docs:
                print(doc.to_dict())

        else:
            meals_docs = self.meals.stream()
            desserts_docs = self.desserts.stream()
            snacks_docs = self.snacks.stream()

            print("Meals =>")
            for doc in meals_docs:
                print(doc.to_dict())

            print("Desserts =>")
            for doc in desserts_docs:
                print(doc.to_dict())

            print("Snacks =>")
            for doc in snacks_docs:
                print(doc.to_dict())


    def delete_recipe(self):
        """ Deletes the specified recipe. First figures out
        What collection it is then asks for the recipe name.
        Takes those two things to populate the delete command.
        """

        print("Which kind of recipe would you like to delete?")
        col = input("1. Meal\n2. Dessert\n3. Snack")

        self.get_recipes(col)

        rec = input("\nName the recipe you would like to delete:\n")

        collections_dict = {"1": self.meals, "2": self.desserts, "3": self.snacks}
        collections_dict[col].document(rec).delete()

        print("Recipe successfully deleted.")