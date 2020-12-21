class Food:
    def __init__(self, line):
        ingredients, allergens = line.strip()[:-1].split(' (contains ')
        self.ingredients = set(ingredients.split(' '))
        self.allergens = set(allergens.split(', '))


with open('input.txt') as f:
    foods = [Food(line) for line in f.readlines()]

possibly_containing = {}
for allergen in set.union(*(f.allergens for f in foods)):
    possibly_containing[allergen] = set.intersection(*(f.ingredients for f in foods if allergen in f.allergens))

# part 1
print(len([ingredient for f in foods for ingredient in f.ingredients
           if ingredient not in set.union(*(i for i in possibly_containing.values()))]))

# part 2
while any(len(ingredients) > 1 for ingredients in possibly_containing.values()):
    for allergen in possibly_containing.keys():
        possibly_containing[allergen] = possibly_containing[allergen] - set(
            list(ing)[0] for a, ing in possibly_containing.items() if a != allergen and len(ing) == 1)

print(','.join(list(possibly_containing[a])[0] for a in sorted(possibly_containing.keys())))
