import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from recipe import Recipe

cred = credentials.Certificate("cloud-recipes-rbrower-d83cf795140d.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'recipes').document(u'Bread')

# doc_ref.set({
#     u'1': u'Flour',
#     u'2': u'Water',
#     u'3': u'Yeast',
#     u'4': u'Milk',
#     u'5': u'Salt',
#     u'6': u'Egg',
#     u'7': u'Oil'
# })

bread = Recipe(
    "Bread",
    ["Flour", "Water", "Yeast", "Milk", "Salt", "Egg", "Oil"],
    {
        1: "Stir together dry ingredients.",
        2: "Add water, egg and oil and stir.",
        3: "Knead dough until spongy but firm.",
        4: "Bake until browned and cripsy on the outside."
    }
)

doc_ref.set(bread.to_dict())



recipes_ref = db.collection(u'recipes')
docs = recipes_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')