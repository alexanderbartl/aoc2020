class Food:
    def __init__(self, line):
        ingredients, allergens = line.strip()[:-1].split(' (contains ')
        self.ingredients = set(ingredients.split(' '))
        self.allergens = set(allergens.split(', '))


with open('input.txt') as f:
    foods = [Food(line) for line in f.readlines()]

all_allergens = set.union(*(f.allergens for f in foods))
all_ingredients = set.union(*(f.ingredients for f in foods))
not_containing = {}
possibly_containing = {}
for allergen in all_allergens:
    not_containing[allergen] = set.union(*(f.ingredients for f in foods if allergen in f.allergens)) \
                               - set.intersection(*(f.ingredients for f in foods if allergen in f.allergens))
    possibly_containing[allergen] = set.intersection(*(f.ingredients for f in foods if allergen in f.allergens))

not_containing_anything = set()
for allergen, ingredients in not_containing.items():
    somewhere_else = set.union(*possibly_containing.values())
    not_containing_anything = not_containing_anything.union(
        set([ingredient for ingredient in ingredients if ingredient not in somewhere_else]))

print(sum(1 if ingredient in f.ingredients else 0 for f in foods for ingredient in not_containing_anything))
