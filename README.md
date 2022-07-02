# Overview

This simple recipe database will keep your recipe information safe
and easy to read whenever you want. Using Google Firebase, this
program lets you add new recipes and store them on the cloud. It
also lets you read any recipe and delete them if you want.

It is built in python using a class-based system, where one class
(main) manages user input and queries the other class (database)
for information. The database class interacts with the cloud
database, getting and setting information there. There is a third
class (recipe), which holds the framework for new data and exports
it correctly to be held in Firebase's NoSQL format.

[Software Demo Video](https://youtu.be/XRIFEBbZPbw)

# Cloud Database

The cloud database I used was Google Firebase. The layout structure
was divided between three collections which represent different
types of food you could make - Meals, Desserts, and Snacks.
Categorizing them allows you to more easily find the recipe
you are looking for.

Each collection is filled with "documents", each of which represents
one recipe. Each recipe holds a title, an array for the ingredients,
and a dictionary for the instructions, the key of each instruction
being the number of it's step.

# Development Environment

* Python 3.9
* Google Firebase

# Useful Websites

* [Firebase Documentation](https://firebase.google.com/docs/firestore/manage-data/add-data)
* [medium.com](https://medium.com/theleanprogrammer/connecting-firebase-6102ef4eca08)

# Future Work

* Modify Ingredients & Instructions
* Redisplay from Dict
* Visual UI