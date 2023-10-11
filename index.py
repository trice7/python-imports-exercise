# from appliances.kitchen import Dishwasher
# from appliances.laundry import Dryer
# from appliances.laundry import Washer
# from appliances.kitchen.utility import Refrigerator
from appliances import DishWasher, Washer, Dryer, Refrigerator, CoffeeMaker, CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

tuna_can = CanOpener("red")
tuna_can.open_can()
