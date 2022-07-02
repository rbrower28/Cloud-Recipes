
class Recipe:
    """ This is the class that serves as a model for newly-added
    recipes. The firebase_admin library handles this class
    and turns it either into readable json or into compatible
    No-SQL data for online storage.
    """

    def __init__(self, name, ingredients, instructions):
        """ Sets up the recipe from the parameters.
        The name will be a string,
        The ingredients will be an array,
        and the Instructions will be a dictionary with the
        number of instruction as the dict key.
        """

        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions


    def from_dict(self, source):
        """ This actually isn't used in the database file, but
        allows for future connectivity with porting database
        files back into python format for formatting and restorage.
        """

        self.name = list(source.keys())[0]
        self.ingredients = source.ingredients
        self.instructions = source.instructions


    def to_dict(self):
        """ This turns the class data into a python dictionary that
        can either be used to easily display information or to export
        it to another form of storage.
        """

        return {
            self.name: {
                "ingredients": self.ingredients,
                "instructions": self.instructions
            }
        }


    def __repr__(self):
        return(
            f'City(\
                name={self.name}, \
                ingredients={self.ingredients}, \
                instructions={self.instructions} \
            )'
        )