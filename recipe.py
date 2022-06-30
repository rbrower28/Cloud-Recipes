
class Recipe:

    def init(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions


    def from_dict(self, source):
        self.name = list(source.keys())[0]
        self.ingredients = source.ingredients
        self.instructions = source.instructions


    def to_dict(self):
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