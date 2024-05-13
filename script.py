# Creating Brunch, Early Bird, Dinner and Kids menus
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

# Brunch Menu
brunch_items = {
  'pancakes': 7.50, 
  'waffles': 9.00, 
  'burger': 11.00, 
  'home fries': 4.50, 
  'coffee': 1.50, 
  'espresso': 3.00, 
  'tea': 1.00, 
  'mimosa': 10.50, 
  'orange juice': 3.50
}
brunch = Menu('Brunch', brunch_items, 11, 16)

# Early Bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 
  'salad and breadsticks (serves 2, no refills)': 14.00, 
  'pizza with quattro formaggi': 9.00, 
  'duck ragu': 17.50,
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 1.50, 'espresso': 3.00,
}
early_bird = Menu('Early Bird', early_bird_items, 15, 18)

# Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 
  'caesar salad': 16.00, 
  'pizza with quattro formaggi': 11.00, 
  'duck ragu': 19.50, 
  'mushroom ravioli (vegan)': 13.50, 
  'coffee': 2.00, 
  'espresso': 3.00,
}
dinner = Menu('Dinner', dinner_items, 17, 23)

# Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 
  'fusilli with wild mushrooms': 12.00, 
  'apple juice': 3.00
}
kids = Menu('Kids', kids_items, 11, 21)
#---------------------------------------------------#