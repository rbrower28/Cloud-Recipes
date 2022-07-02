from database import Database

class Start:
    """ Keeps track of recipes for you. Allows you to store, categorize,
    read, and delete your recipes.
    """

    def __init__(self):
        """ Creates an instance of the database. Sets up a boolean that
        tells the program when to stop running.
        """

        self.db = Database()
        self.run = True
        
        while self.run:
            self.run_main()


    def run_main(self):
        """ This will loop over again until the program is finished.
        """

        print("\n ====== Welcome to the Recipe Library! ======")
        print("\nChoose an option:")
        print("1. See Recipes\n2. Add a Recipe\n3. Delete a Recipe\n4. Quit")
        answer = input()

        if answer == "1":
            self.request_get()

        elif answer == "2":
            self.request_add()

        elif answer == "3":
            self.request_delete()

        elif answer == "4":
            self.run = False
            print("\nHave a great day!\n")


    def request_get(self):
        """ Refines the search, then sends it to the db class.
        """

        print("Which would you like to see?")
        print("1. Meals\n2. Desserts\n3. Snacks\n4. All")

        ans = input()

        if ans in ("1", "2", "3"):
            self.db.get_recipes(ans)

        elif ans == "4":
            self.db.get_recipes()


    def request_add(self):
        """ Calls the add function from the db class.
        """

        self.db.set_recipe()

    def request_delete(self):
        """ Calls the delete function from the db class.
        """

        self.db.delete_recipe()


if __name__ == "__main__":
    Start()