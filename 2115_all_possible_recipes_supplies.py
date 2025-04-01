from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        made_recipes = set()
        recipe_map = dict(zip(recipes, ingredients)) # zip it so they stay bundled together

        progress = True
        while progress:
            progress = False
            keys = list(recipe_map.keys())  # Create a copy of keys to iterate over
            for recipe in keys:
                all_ingredients_available = True

                for ing in recipe_map[recipe]:
                    if ing not in available:
                        all_ingredients_available = False
                        break  # No need to check further

                if all_ingredients_available:
                    available.add(recipe)
                    made_recipes.add(recipe)
                    del recipe_map[recipe]
                    progress = True  # We made progress this round

        return list(made_recipes)

sol = Solution()
r = sol.findAllRecipes(
    ["bread", "sandwich"],
    [["yeast", "flour"], ["bread", "flour"]],
    ["yeast", "flour", "meat"]
)
print(r)  # Output: ['bread', 'sandwich']
