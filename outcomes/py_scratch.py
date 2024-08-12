import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import random
from fractions import Fraction

# Problem 1: Carlos is organizing a book fair and needs to distribute promotional flyers.
def problem1():
    person_a = sm.random_person()
    total_flyers = random.randint(300, 400)
    flyers_per_classroom = random.randint(20, 30)
    leftover_flyers = random.randint(10, 30)
    flyers_distributed = total_flyers - leftover_flyers
    classrooms = flyers_distributed // flyers_per_classroom
    
    problem = (f'{person_a.name} is organizing a book fair and needs to distribute promotional flyers. '
               f'{person_a.subj_pronoun().capitalize()} prints {total_flyers} flyers and plans to give out {flyers_per_classroom} flyers per classroom. '
               f'After distributing flyers to all the classrooms, {person_a.subj_pronoun()} has {leftover_flyers} flyers left. How many classrooms did '
               f'{person_a.subj_pronoun()} distribute the flyers to?')
    
    solution = (f'To find out how many classrooms {person_a.name} distributed the flyers to, we first subtract the leftover flyers from the total number '
                f'of printed flyers. So, {total_flyers} - {leftover_flyers} gives us {flyers_distributed} flyers that were distributed. Then, '
                f'we divide this number by the number of flyers per classroom: {flyers_distributed} / {flyers_per_classroom} equals {classrooms}. '
                f'Therefore, {person_a.name} distributed flyers to {classrooms} classrooms.')
    
    return problem, solution

# Problem 2: Sophie is planting a garden.
def problem2():
    person_a = sm.random_person()
    tomato_rows = random.randint(3, 5)
    tomato_plants_per_row = random.randint(10, 20)
    carrot_rows = random.randint(4, 6)
    carrot_plants_per_row = random.randint(5, 10)
    bean_rows = random.randint(2, 4)
    bean_plants_per_row = random.randint(8, 12)
    
    total_tomato_plants = tomato_rows * tomato_plants_per_row
    total_carrot_plants = carrot_rows * carrot_plants_per_row
    total_bean_plants = bean_rows * bean_plants_per_row
    total_plants = total_tomato_plants + total_carrot_plants + total_bean_plants
    
    problem = (f'{person_a.name} is planting a garden. {person_a.subj_pronoun().capitalize()} has {tomato_rows} rows, each with {tomato_plants_per_row} tomato plants. '
               f'{person_a.subj_pronoun().capitalize()} also plants {carrot_rows} rows of carrots, each with {carrot_plants_per_row} plants. If {person_a.subj_pronoun()} plants '
               f'{bean_rows} more rows of beans with {bean_plants_per_row} plants each, how many plants does {person_a.subj_pronoun()} have in total?')
    
    solution = (f'To find the total number of plants {person_a.name} has, we start by calculating the total number of tomato plants. '
                f'{tomato_rows} rows of tomatoes with {tomato_plants_per_row} plants each give us {total_tomato_plants} tomato plants. '
                f'Next, we calculate the total number of carrot plants: {carrot_rows} rows with {carrot_plants_per_row} plants each give us {total_carrot_plants} carrot plants. '
                f'Finally, the total number of bean plants: {bean_rows} rows with {bean_plants_per_row} plants each give us {total_bean_plants} bean plants. '
                f'Adding these all together, {total_tomato_plants} + {total_carrot_plants} + {total_bean_plants} gives us {total_plants} plants in total. '
                f'Therefore, {person_a.name} has {total_plants} plants in total.')
    
    return problem, solution

# Problem 3: A bakery makes 240 muffins every day.
def problem3():
    person_a = sm.random_person()
    total_muffins = random.randint(200, 300)
    morning_fraction = random.choice([Fraction(2, 5), Fraction(3, 5), Fraction(4, 5)])
    afternoon_fraction = random.choice([Fraction(1, 4), Fraction(1, 3)])
    
    morning_sales = int(morning_fraction * total_muffins)
    remaining_muffins = total_muffins - morning_sales
    afternoon_sales = int(afternoon_fraction * remaining_muffins)
    unsold_muffins = remaining_muffins - afternoon_sales
    
    problem = (f'A bakery makes {total_muffins} muffins every day. They sell {morning_fraction} of them in the morning and '
               f'{afternoon_fraction} of the remaining muffins in the afternoon. How many muffins are left unsold at the end of the day?')
    
    solution = (f'To find out how many muffins are left unsold at the end of the day, we first calculate the number of muffins sold in the morning. '
                f'The bakery sells {morning_fraction} of {total_muffins} muffins, which is {morning_sales} muffins. '
                f'Next, we calculate the remaining muffins after the morning sales: {total_muffins} - {morning_sales} gives us {remaining_muffins} muffins. '
                f'Then, we calculate the number of muffins sold in the afternoon: {afternoon_fraction} of {remaining_muffins} muffins is {afternoon_sales} muffins. '
                f'Finally, we subtract the afternoon sales from the remaining muffins to find the number of muffins left unsold: '
                f'{remaining_muffins} - {afternoon_sales} equals {unsold_muffins}. Therefore, there are {unsold_muffins} muffins left unsold at the end of the day.')
    
    return problem, solution

# Problem 4: Emma and her friends are making friendship bracelets.
def problem4():
    name1, subj_pronoun1, obj_pronoun1, poss_pronoun1 = get_random_name_and_pronoun()
    name2, subj_pronoun2, obj_pronoun2, poss_pronoun2 = get_random_name_and_pronoun()
    rate1 = random.randint(3, 5)
    hours1 = random.randint(2, 4)
    rate2 = random.randint(4, 6)
    hours2 = random.randint(1, 3)
    
    bracelets1 = rate1 * hours1
    bracelets2 = rate2 * hours2
    total_bracelets = bracelets1 + bracelets2
    
    problem = (f'{name1} and {name2} are making friendship bracelets. {name1} can make {rate1} bracelets per hour, and {person_a.subj_pronoun()1} works for {hours1} hours. '
               f'{name2} makes {rate2} bracelets per hour and works for {hours2} hours. How many bracelets do they make together?')
    
    solution = (f'To find out how many bracelets {name1} and {name2} make together, we start by calculating the number of bracelets {name1} makes. '
                f'{name1} makes {rate1} bracelets per hour for {hours1} hours, which gives us {bracelets1} bracelets. '
                f'Next, we calculate the number of bracelets {name2} makes: {name2} makes {rate2} bracelets per hour for {hours2} hours, which gives us {bracelets2} bracelets. '
                f'Adding these two amounts together, {bracelets1} + {bracelets2} gives us {total_bracelets} bracelets. '
                f'Therefore, {name1} and {name2} make {total_bracelets} bracelets together.')
    
    return problem, solution

# Problem 5: David is filling a swimming pool.
def problem5():
    person_a = sm.random_person()
    rate = random.randint(100, 200)
    initial_minutes = random.randint(20, 40)
    additional_minutes = random.randint(10, 20)
    
    total_minutes = initial_minutes + additional_minutes
    total_intervals = total_minutes // 5
    total_water = total_intervals * rate
    
    problem = (f'{person_a.name} is filling a swimming pool. {person_a.subj_pronoun().capitalize()} fills it at a rate of {rate} liters every 5 minutes. '
               f'After filling it for {initial_minutes} minutes, {person_a.subj_pronoun()} takes a break and then fills it for another {additional_minutes} minutes. '
               f'How many liters of water are in the pool?')
    
    solution = (f'To find out how many liters of water are in the pool, we first calculate the total time {person_a.name} spends filling the pool. '
                f'{initial_minutes} minutes plus {additional_minutes} minutes gives us a total of {total_minutes} minutes. '
                f'Next, we calculate the number of 5-minute intervals in the total time: {total_minutes} divided by 5 equals {total_intervals} intervals. '
                f'Finally, we calculate the total amount of water: {total_intervals} intervals times {rate} liters per interval equals {total_water} liters. '
                f'Therefore, there are {total_water} liters of water in the pool.')
    
    return problem, solution


# Problem 6: Quinn is planting trees in an orchard.
def problem6():
    person_a = sm.random_person()
    rows = random.randint(3, 7)
    trees_per_row = random.randint(8, 15)
    extra_trees = random.randint(5, 10)
    
    total_trees = (rows * trees_per_row) + extra_trees
    
    problem = (f'{person_a.name} is planting trees in an orchard. {person_a.subj_pronoun().capitalize()} plants {rows} rows of trees, with {trees_per_row} trees per row. '
               f'{person_a.subj_pronoun().capitalize()} also plants {extra_trees} extra trees. How many trees does {person_a.name} plant in total?')
    
    solution = (f'To find out how many trees {person_a.name} plants in total, we first calculate the number of trees in the rows. '
                f'{rows} rows multiplied by {trees_per_row} trees per row equals {rows * trees_per_row} trees. '
                f'Adding the extra trees, {rows * trees_per_row} + {extra_trees} equals {total_trees} trees. '
                f'Therefore, {person_a.name} plants {total_trees} trees in total.')
    
    return problem, solution

# Problem 7: Jamie is mixing fruit juice.
def problem7():
    person_a = sm.random_person()
    initial_volume = random.randint(2, 5)
    additional_volume = Fraction(random.randint(1, 3), random.randint(2, 4))
    bottles = random.randint(4, 6)
    
    total_volume = initial_volume + additional_volume
    volume_per_bottle = total_volume / bottles
    
    problem = (f'{person_a.name} is mixing fruit juice. {person_a.subj_pronoun().capitalize()} starts with {initial_volume} liters of juice and adds '
               f'{additional_volume} liters more. {person_a.subj_pronoun().capitalize()} then pours the juice equally into {bottles} bottles. '
               f'How much juice is in each bottle?')
    
    solution = (f'To find out how much juice is in each bottle, we first calculate the total volume of juice. '
                f'{initial_volume} liters plus {additional_volume} liters equals {total_volume} liters. '
                f'Next, we divide the total volume by the number of bottles: {total_volume} liters divided by {bottles} bottles equals '
                f'{volume_per_bottle} liters per bottle. Therefore, each bottle contains {volume_per_bottle} liters of juice.')
    
    return problem, solution

# Problem 8: Avery is cutting pieces of ribbon.
def problem8():
    person_a = sm.random_person()
    total_ribbon = Fraction(random.randint(8, 12), 1)
    piece_length = Fraction(random.randint(1, 3), random.randint(2, 4))
    
    num_pieces = total_ribbon // piece_length
    leftover_ribbon = total_ribbon % piece_length
    
    problem = (f'{person_a.name} has {total_ribbon} meters of ribbon. {person_a.subj_pronoun().capitalize()} cuts pieces that are {piece_length} meters long. '
               f'How many full pieces can {person_a.subj_pronoun()} cut and how much ribbon will be left over?')
    
    solution = (f'To find out how many full pieces {person_a.name} can cut, we divide the total length of the ribbon by the length of each piece. '
                f'{total_ribbon} meters divided by {piece_length} meters per piece equals {num_pieces} full pieces. '
                f'The leftover ribbon is the remainder of this division, which is {leftover_ribbon} meters. '
                f'Therefore, {person_a.name} can cut {num_pieces} full pieces and will have {leftover_ribbon} meters of ribbon left over.')
    
    return problem, solution

# Problem 9: Casey is arranging flowers in vases.
def problem9():
    person_a = sm.random_person()
    flowers_per_vase = random.randint(6, 12)
    vases = random.randint(5, 10)
    extra_flowers = random.randint(3, 8)
    
    total_flowers = (flowers_per_vase * vases) + extra_flowers
    
    problem = (f'{person_a.name} is arranging flowers in vases. {person_a.subj_pronoun().capitalize()} puts {flowers_per_vase} flowers in each of {vases} vases. '
               f'{person_a.subj_pronoun().capitalize()} also has {extra_flowers} extra flowers. How many flowers does {person_a.name} have in total?')
    
    solution = (f'To find out how many flowers {person_a.name} has in total, we first calculate the number of flowers in the vases. '
                f'{flowers_per_vase} flowers per vase multiplied by {vases} vases equals {flowers_per_vase * vases} flowers. '
                f'Adding the extra flowers, {flowers_per_vase * vases} + {extra_flowers} equals {total_flowers} flowers. '
                f'Therefore, {person_a.name} has {total_flowers} flowers in total.')
    
    return problem, solution

# Problem 10: Morgan is painting a mural.
def problem10():
    person_a = sm.random_person()
    initial_area = random.randint(20, 30)
    additional_area = random.randint(10, 15)
    paint_cans = random.randint(4, 6)
    
    total_area = initial_area + additional_area
    area_per_can = total_area / paint_cans
    
    problem = (f'{person_a.name} is painting a mural. {person_a.subj_pronoun().capitalize()} paints an initial area of {initial_area} square meters and then paints '
               f'an additional {additional_area} square meters. If {person_a.subj_pronoun()} uses {paint_cans} cans of paint to cover the entire area, '
               f'how many square meters does each can of paint cover on average?')
    
    solution = (f'To find out how many square meters each can of paint covers on average, we first calculate the total area painted. '
                f'{initial_area} square meters plus {additional_area} square meters equals {total_area} square meters. '
                f'Next, we divide the total area by the number of paint cans: {total_area} square meters divided by {paint_cans} cans equals '
                f'{area_per_can} square meters per can. Therefore, each can of paint covers {area_per_can} square meters on average.')
    
    return problem, solution

# Problem 11: Riley is stacking books.
def problem11():
    person_a = sm.random_person()
    books_per_stack = random.randint(5, 10)
    total_stacks = random.randint(6, 12)
    used_books = random.randint(10, 20)
    
    total_books = books_per_stack * total_stacks
    remaining_books = total_books - used_books
    
    problem = (f'{person_a.name} is stacking books in the library. {person_a.subj_pronoun().capitalize()} makes stacks of {books_per_stack} books each. '
               f'There are {total_stacks} stacks in total. After using {used_books} books for a display, how many books are left in the stacks?')
    
    solution = (f'To find out how many books are left in the stacks, we first calculate the total number of books. '
                f'{books_per_stack} books per stack multiplied by {total_stacks} stacks equals {total_books} books. '
                f'Then we subtract the used books: {total_books} - {used_books} equals {remaining_books}. '
                f'Therefore, there are {remaining_books} books left in the stacks.')
    
    return problem, solution

# Problem 12: Cameron is filling water bottles.
def problem12():
    person_a = sm.random_person()
    bottles = random.randint(10, 20)
    capacity_per_bottle = random.randint(500, 1000)  # milliliters
    used_capacity = random.randint(2000, 4000)
    
    total_capacity = bottles * capacity_per_bottle
    remaining_capacity = total_capacity - used_capacity
    
    problem = (f'{person_a.name} is filling water bottles. Each of the {bottles} bottles can hold {capacity_per_bottle} milliliters of water. '
               f'After using {used_capacity} milliliters for another purpose, how much water is left in the bottles?')
    
    solution = (f'To find out how much water is left in the bottles, we first calculate the total capacity of all the bottles. '
                f'{bottles} bottles multiplied by {capacity_per_bottle} milliliters per bottle equals {total_capacity} milliliters. '
                f'Then we subtract the used capacity: {total_capacity} - {used_capacity} equals {remaining_capacity} milliliters. '
                f'Therefore, there are {remaining_capacity} milliliters of water left in the bottles.')
    
    return problem, solution

# Problem 13: Taylor is organizing chairs for a school event.
def problem13():
    person_a = sm.random_person()
    rows = random.randint(5, 10)
    chairs_per_row = random.randint(10, 20)
    removed_chairs = random.randint(10, 20)
    
    total_chairs = rows * chairs_per_row
    remaining_chairs = total_chairs - removed_chairs
    
    problem = (f'{person_a.name} is organizing chairs for a school event. There are {rows} rows of chairs, with {chairs_per_row} chairs per row. '
               f'If {person_a.subj_pronoun()} removes {removed_chairs} chairs for another activity, how many chairs are left?')
    
    solution = (f'To find out how many chairs are left, we first calculate the total number of chairs. '
                f'{rows} rows multiplied by {chairs_per_row} chairs per row equals {total_chairs} chairs. '
                f'Then we subtract the removed chairs: {total_chairs} - {removed_chairs} equals {remaining_chairs}. '
                f'Therefore, there are {remaining_chairs} chairs left.')
    
    return problem, solution

# Problem 14: Jordan is preparing gift bags for a party.
def problem14():
    person_a = sm.random_person()
    bags = random.randint(10, 20)
    items_per_bag = random.randint(5, 10)
    additional_items = random.randint(15, 25)
    
    total_items = bags * items_per_bag
    new_total_items = total_items + additional_items
    
    problem = (f'{person_a.name} is preparing gift bags for a party. {person_a.subj_pronoun().capitalize()} makes {bags} bags, each containing {items_per_bag} items. '
               f'If {person_a.subj_pronoun()} adds {additional_items} more items to the bags, how many items are there in total?')
    
    solution = (f'To find out how many items are there in total, we first calculate the initial number of items. '
                f'{bags} bags multiplied by {items_per_bag} items per bag equals {total_items} items. '
                f'Then we add the additional items: {total_items} + {additional_items} equals {new_total_items}. '
                f'Therefore, there are {new_total_items} items in total.')
    
    return problem, solution

# Problem 15: Avery is baking cookies for a bake sale.
def problem15():
    person_a = sm.random_person()
    batches = random.randint(5, 10)
    cookies_per_batch = random.randint(12, 24)
    broken_cookies = random.randint(5, 15)
    
    total_cookies = batches * cookies_per_batch
    remaining_cookies = total_cookies - broken_cookies
    
    problem = (f'{person_a.name} is baking cookies for a bake sale. {person_a.subj_pronoun().capitalize()} bakes {batches} batches of cookies, with {cookies_per_batch} cookies per batch. '
               f'If {person_a.subj_pronoun()} breaks {broken_cookies} cookies, how many cookies are left for the sale?')
    
    solution = (f'To find out how many cookies are left for the sale, we first calculate the total number of cookies. '
                f'{batches} batches multiplied by {cookies_per_batch} cookies per batch equals {total_cookies} cookies. '
                f'Then we subtract the broken cookies: {total_cookies} - {broken_cookies} equals {remaining_cookies}. '
                f'Therefore, there are {remaining_cookies} cookies left for the sale.')
    
    return problem, solution

def problem16():
    person_a = sm.random_person()
    plan1_cost = random.randint(20, 40)
    plan2_cost = random.randint(25, 45)
    plan2_discount = random.randint(5, 15)
    months = random.randint(6, 12)
    
    total_cost_plan1 = plan1_cost * months
    total_cost_plan2 = (plan2_cost * months) - plan2_discount
    
    more_expensive_plan = 'Plan 1' if total_cost_plan1 > total_cost_plan2 else 'Plan 2'
    cost_difference = abs(total_cost_plan1 - total_cost_plan2)
    
    problem = (f'{person_a.name} is comparing the cost of two phone plans. Plan 1 costs ${plan1_cost} per month. '
               f'Plan 2 costs ${plan2_cost} per month, but there is a ${plan2_discount} discount applied once after signing up. '
               f'If {person_a.name} needs the plan for {months} months, which plan is more expensive and by how much?')
    
    solution = (f'To find out which plan is more expensive, we first calculate the total cost for each plan. '
                f'The total cost for Plan 1 is {plan1_cost} dollars per month multiplied by {months} months, which equals ${total_cost_plan1}. '
                f'The total cost for Plan 2 is {plan2_cost} dollars per month multiplied by {months} months, minus the ${plan2_discount} discount, '
                f'which equals ${total_cost_plan2}. Comparing the two, {more_expensive_plan} is more expensive by ${cost_difference}.')
    
    return problem, solution

# Problem 17: Kendall is making fruit punch.
def problem17():
    person_a = sm.random_person()
    fruit_juice_liters = random.randint(3, 6)
    soda_liters = Fraction(random.randint(2, 4), random.randint(1, 3))
    water_liters = Fraction(random.randint(1, 3), random.randint(1, 2))
    cups_per_liter = 4
    
    total_liters = fruit_juice_liters + soda_liters + water_liters
    total_cups = total_liters * cups_per_liter
    
    problem = (f'{person_a.name} is making fruit punch. {person_a.subj_pronoun().capitalize()} mixes {fruit_juice_liters} liters of fruit juice, '
               f'{soda_liters} liters of soda, and {water_liters} liters of water. If each liter of punch can fill 4 cups, '
               f'how many cups of punch does {person_a.name} make in total?')
    
    solution = (f'To find out how many cups of punch {person_a.name} makes in total, we first calculate the total volume of the punch. '
                f'{fruit_juice_liters} liters of fruit juice plus {soda_liters} liters of soda plus {water_liters} liters of water equals {total_liters} liters. '
                f'Since each liter fills 4 cups, we multiply {total_liters} liters by 4 cups per liter, which equals {total_cups} cups of punch. '
                f'Therefore, {person_a.name} makes {total_cups} cups of punch in total.')
    
    return problem, solution

# Problem 18: Dakota is saving money for a bike.
def problem18():
    person_a = sm.random_person()
    initial_savings = random.randint(50, 100)
    weekly_savings = random.randint(10, 20)
    weeks = random.randint(8, 16)
    bike_cost = random.randint(250, 400)
    
    total_savings = initial_savings + (weekly_savings * weeks)
    enough_savings = total_savings >= bike_cost
    extra_needed = max(0, bike_cost - total_savings)
    
    problem = (f'{person_a.name} is saving money to buy a bike that costs ${bike_cost}. {person_a.subj_pronoun().capitalize()} starts with ${initial_savings} and saves '
               f'${weekly_savings} each week. After {weeks} weeks, does {person_a.name} have enough money to buy the bike? If not, how much more does {person_a.subj_pronoun()} need?')
    
    solution = (f'To find out if {person_a.name} has enough money, we first calculate the total savings. '
                f'{initial_savings} dollars plus {weekly_savings} dollars per week multiplied by {weeks} weeks equals ${total_savings}. '
                f'The cost of the bike is ${bike_cost}. Since {person_a.name} has {"enough" if enough_savings else "not enough"} money, {person_a.subj_pronoun()} '
                f'{"can" if enough_savings else "cannot"} buy the bike. If not, {person_a.subj_pronoun()} needs ${extra_needed} more.')
    
    return problem, solution

# Problem 19: Jordan is organizing a charity run.
def problem19():
    person_a = sm.random_person()
    total_distance = random.randint(10, 20)
    first_leg = Fraction(random.randint(1, 3), 2)
    second_leg = Fraction(random.randint(2, 4), 3)
    remaining_distance = total_distance - (first_leg + second_leg)
    
    problem = (f'{person_a.name} is organizing a charity run. The total distance is {total_distance} kilometers. '
               f'The first leg of the run is {first_leg} kilometers, and the second leg is {second_leg} kilometers. '
               f'How many kilometers are left for the remaining distance?')
    
    solution = (f'To find out how many kilometers are left for the remaining distance, we first add the distances of the first and second legs. '
                f'{first_leg} kilometers plus {second_leg} kilometers equals {first_leg + second_leg} kilometers. '
                f'Subtracting this from the total distance, {total_distance} kilometers minus {first_leg + second_leg} kilometers equals {remaining_distance} kilometers. '
                f'Therefore, there are {remaining_distance} kilometers left for the remaining distance.')
    
    return problem, solution

# Problem 20: Skyler is baking pies.
def problem20():
    person_a = sm.random_person()
    pies = random.randint(3, 6)
    slices_per_pie = random.randint(6, 8)
    eaten_slices = random.randint(10, 15)
    
    total_slices = pies * slices_per_pie
    remaining_slices = total_slices - eaten_slices
    
    problem = (f'{person_a.name} is baking pies for a party. {person_a.subj_pronoun().capitalize()} bakes {pies} pies, each cut into {slices_per_pie} slices. '
               f'If {person_a.subj_pronoun()} and {person_a.poss_adjective()} friends eat {eaten_slices} slices, how many slices are left?')
    
    solution = (f'To find out how many slices are left, we first calculate the total number of slices. '
                f'{pies} pies multiplied by {slices_per_pie} slices per pie equals {total_slices} slices. '
                f'Subtracting the eaten slices, {total_slices} - {eaten_slices} equals {remaining_slices} slices. '
                f'Therefore, there are {remaining_slices} slices left.')
    
    return problem, solution

# Problem 21: Samantha's mom is trying to find a contractor to work on their house.
def problem21():
    person_a = sm.random_person()
    contractor1_rate = random.randint(50, 80)
    contractor2_rate = random.randint(55, 85)
    discount = random.randint(30, 50)
    hours = random.randint(8, 16)

    contractor1_cost = contractor1_rate * hours
    contractor2_cost = (contractor2_rate * hours) - discount
    cost_difference = abs(contractor1_cost - contractor2_cost)

    problem = (f'{person_a.name}\'s mom is trying to find a contractor to work on their house. The first contractor charges ${contractor1_rate} per hour. '
               f'The second contractor charges ${contractor2_rate} per hour, but there is a ${discount} discount on the total bill if chosen. '
               f'If {person_a.poss_adjective()} mom needs the contractor to work for {hours} hours, how much more will the total bill come to if they choose the second contractor instead of the first?')

    solution = (f'To find the total cost for each contractor, we multiply the hourly rate by the number of hours needed. '
                f'The total cost for the first contractor is ${contractor1_rate} per hour multiplied by {hours} hours, which equals ${contractor1_cost}. '
                f'The total cost for the second contractor is ${contractor2_rate} per hour multiplied by {hours} hours minus the ${discount} discount, which equals ${contractor2_cost}. '
                f'The difference in cost between the two contractors is ${cost_difference}. Therefore, the total bill will be ${cost_difference} more if they choose the second contractor.')

    return problem, solution

# Problem 22: Katrina runs a small cookie stand every weekend.
def problem22():
    person_a = sm.random_person()
    trays_initial = random.randint(15, 25)
    cookies_per_tray = random.randint(10, 15)
    sold_friday = random.randint(80, 120)
    extra_trays = random.randint(1, 3)
    sold_saturday = random.randint(20, 30)
    sold_sunday = random.randint(10, 20)

    initial_cookies = trays_initial * cookies_per_tray
    extra_cookies = extra_trays * cookies_per_tray
    total_cookies = initial_cookies + extra_cookies
    remaining_cookies = total_cookies - (sold_friday + sold_saturday + sold_sunday)

    problem = (f'{person_a.name} runs a small cookie stand every weekend. This weekend, {person_a.subj_pronoun()} started by baking {trays_initial} trays of cookies. '
               f'Each tray fits {cookies_per_tray} cookies at a time. On Friday, {person_a.subj_pronoun()} sold {sold_friday} cookies. So, {person_a.subj_pronoun()} decided to make {extra_trays} more trays of cookies on Saturday morning. '
               f'{person_a.subj_pronoun()} sold {sold_saturday} more cookies on Saturday, and {sold_sunday} more cookies on Sunday. {person_a.subj_pronoun()} decides to bring the extra remaining cookies to school to share with {person_a.poss_adjective()} class on Monday. '
               f'How many cookies does {person_a.subj_pronoun()} have to share with {person_a.poss_adjective()} class?')

    solution = (f'To find out how many cookies {person_a.name} has to share with {person_a.poss_adjective()} class, we first calculate the total number of cookies baked. '
                f'{trays_initial} trays multiplied by {cookies_per_tray} cookies per tray equals {initial_cookies} cookies. '
                f'Then, {person_a.subj_pronoun()} baked {extra_trays} more trays of cookies, which adds another {extra_cookies} cookies. '
                f'The total number of cookies is {total_cookies}. Subtracting the cookies sold on Friday, Saturday, and Sunday, which totals {sold_friday + sold_saturday + sold_sunday}, '
                f'there are {remaining_cookies} cookies left. Therefore, {person_a.name} has {remaining_cookies} cookies to share with {person_a.poss_adjective()} class.')

    return problem, solution

# Problem 23: Cassie is making some Christmas decorations with twine.
def problem23():
    person_a = sm.random_person()
    spool1 = random.randint(1, 3)
    spool2 = Fraction(random.randint(1, 3), random.randint(2, 4))
    project1 = Fraction(random.randint(1, 2), random.randint(2, 4))
    project2 = Fraction(random.randint(1, 2), random.randint(3, 4))
    project3 = Fraction(random.randint(1, 2), random.randint(1, 3))
    total_twine = spool1 + spool2
    total_needed = project1 + project2 + project3
    has_enough = total_twine >= total_needed

    problem = (f'{person_a.name} is making some Christmas decorations with twine, but {person_a.subj_pronoun()} is running out of twine to use! {person_a.subj_pronoun()} measures {person_a.poss_adjective()} remaining twine before starting {person_a.poss_adjective()} projects. '
               f'{person_a.subj_pronoun()} has {spool1} ft of twine on one spool, and {spool2} ft of twine on another spool. {person_a.poss_adjective()} first project requires {project1} ft of twine, '
               f'{person_a.poss_adjective()} second project requires {project2} ft, and {person_a.poss_adjective()} third project requires {project3} ft. Will {person_a.name} have enough twine to make all three projects? Why or why not?')

    solution = (f'To find out if {person_a.name} has enough twine to complete all three projects, we first calculate the total amount of twine available. '
                f'{spool1} ft plus {spool2} ft equals {total_twine} ft of twine. Then, we add up the amount of twine needed for each project. '
                f'{project1} ft plus {project2} ft plus {project3} ft equals {total_needed} ft of twine needed. '
                f'{person_a.name} {"has" if has_enough else "does not have"} enough twine to complete all three projects because {person_a.subj_pronoun()} needs {total_needed} ft but only has {total_twine} ft.')

    return problem, solution

# Problem 24: Kristi is walking down a straight road from her house to the market.
def problem24():
    person_a = sm.random_person()
    distance1 = Fraction(random.randint(1, 3), random.randint(3, 5))
    distance2 = Fraction(random.randint(1, 2), random.randint(4, 6))
    backtrack = Fraction(random.randint(1, 2), random.randint(4, 8))
    total_distance = distance1 + distance2 - backtrack

    problem = (f'{person_a.name} is walking down a straight road from {person_a.poss_adjective()} house to the market. {person_a.subj_pronoun().capitalize()} walks {distance1} mi. before taking a rest. '
               f'Then, {person_a.subj_pronoun()} keeps walking another {distance2} mi. At that point, {person_a.subj_pronoun()} realizes that {person_a.subj_pronoun()} already walked past the market, and backtracks {backtrack} mi. to get to the market. '
               f'How far is it from {person_a.name}\'s house to the market?')

    solution = (f'To find out the total distance from {person_a.name}\'s house to the market, we add the distances {person_a.subj_pronoun()} walked and then subtract the distance {person_a.subj_pronoun()} backtracked. '
                f'{distance1} mi. plus {distance2} mi. equals {distance1 + distance2} mi. Then, subtracting the {backtrack} mi. backtracked, we get {total_distance} mi. '
                f'Therefore, the total distance from {person_a.name}\'s house to the market is {total_distance} mi.')

    return problem, solution

# Problem 25: Mountain View High School has four types of students.
def problem25():
    freshman_fraction = Fraction(1, 6)
    sophomore_fraction = Fraction(random.randint(3, 7), 12)
    junior_fraction = Fraction(random.randint(1, 3), 3)
    total_students = freshman_fraction + sophomore_fraction + junior_fraction
    senior_fraction = 1 - total_students

    problem = (f'Mountain View High School has four types of students: freshman, sophomores, juniors, and seniors. If the student body is {freshman_fraction} freshmen, '
               f'{sophomore_fraction} sophomores, and {junior_fraction} juniors, what fraction of the student body is seniors?')

    solution = (f'To find out what fraction of the student body is seniors, we first add up the fractions of freshmen, sophomores, and juniors. '
                f'{freshman_fraction} freshmen plus {sophomore_fraction} sophomores plus {junior_fraction} juniors equals {total_students}. '
                f'The remaining fraction, which represents the seniors, is 1 minus {total_students}, which equals {senior_fraction}. '
                f'Therefore, the fraction of the student body that is seniors is {senior_fraction}.')

    return problem, solution

# Problem 26: Bebsi Co. produces cans of Bebsi each hour.
def problem26():
    cans_per_hour = random.randint(10000, 20000)
    cans_per_case = random.randint(20, 30)
    hours = random.randint(2, 5)
    total_cans = cans_per_hour * hours
    total_cases = total_cans // cans_per_case

    problem = (f'Bebsi Co. produces {cans_per_hour} cans of Bebsi each hour. Cans are packed in {cans_per_case} to a case. '
               f'How many cases could be filled with the cans produced in {hours} hours?')

    solution = (f'To find out how many cases could be filled, we first calculate the total number of cans produced in {hours} hours. '
                f'{cans_per_hour} cans per hour multiplied by {hours} hours equals {total_cans} cans. '
                f'Dividing this by {cans_per_case} cans per case, we get {total_cases} cases. '
                f'Therefore, {total_cases} cases could be filled with the cans produced in {hours} hours.')

    return problem, solution

# Problem 27: Ally is walking down a straight hallway from her classroom to the bathroom.
def problem27():
    person_a = sm.random_person()
    art_room_distance = random.randint(100, 150)
    music_room_distance_fraction = Fraction(random.randint(1, 3), random.randint(3, 5))
    gym_distance = random.randint(300, 400)
    bathroom_distance = random.randint(40, 60)

    music_room_distance = music_room_distance_fraction * gym_distance
    classroom_to_bathroom_distance = art_room_distance + music_room_distance + bathroom_distance

    problem = (f'{person_a.name} is walking down a straight hallway from {person_a.poss_adjective()} classroom to the bathroom. {person_a.poss_adjective().capitalize()} classroom is at the very end of the hall. '
               f'The art room is {art_room_distance} feet from {person_a.poss_adjective()} classroom. The music room is {music_room_distance_fraction} of the way from the art room to the gym. '
               f'It is another {bathroom_distance} feet from the music room to get to the bathroom. If the gym is {gym_distance} feet from {person_a.poss_adjective()} classroom, how far is it from {person_a.poss_adjective()} classroom to the bathroom?')

    solution = (f'To find out how far it is from {person_a.name}\'s classroom to the bathroom, we first calculate the distance from the art room to the music room. '
                f'The music room is {music_room_distance_fraction} of the distance from the art room to the gym, which is {music_room_distance} feet. '
                f'Adding the distances, {art_room_distance} feet plus {music_room_distance} feet plus {bathroom_distance} feet, we get {classroom_to_bathroom_distance} feet. '
                f'Therefore, the distance from {person_a.name}\'s classroom to the bathroom is {classroom_to_bathroom_distance} feet.')

    return problem, solution

# Problem 28: Your family is buying a new house.
def problem28():
    house_price = random.randint(200000, 300000)
    down_payment = random.randint(20000, 40000)
    monthly_payments = random.randint(180, 300)

    remaining_amount = house_price - down_payment
    monthly_payment_amount = remaining_amount // monthly_payments

    problem = (f'Your family is buying a new house. The agreed upon price for the house at the time of closing is ${house_price}. '
               f'The bank needs the first ${down_payment} immediately as a down payment. The remaining amount will be paid out over {monthly_payments} equal monthly payments. '
               f'Assuming there is no interest involved, how much will your family need to pay each month?')

    solution = (f'To find out how much your family will need to pay each month, we first subtract the down payment from the house price to find the remaining amount. '
                f'${house_price} minus ${down_payment} equals ${remaining_amount}. Dividing this by {monthly_payments} monthly payments, we get ${monthly_payment_amount} per month. '
                f'Therefore, your family will need to pay ${monthly_payment_amount} each month.')

    return problem, solution

# Problem 29: Bert is five years younger than Alfonso.
def problem29():
    # Get random names and pronouns for five different people
    name1, subj_pronoun1, obj_pronoun1, poss_pronoun1 = get_random_name_and_pronoun()
    name2, subj_pronoun2, obj_pronoun2, poss_pronoun2 = get_random_name_and_pronoun()
    name3, subj_pronoun3, obj_pronoun3, poss_pronoun3 = get_random_name_and_pronoun()
    name4, subj_pronoun4, obj_pronoun4, poss_pronoun4 = get_random_name_and_pronoun()
    name5, subj_pronoun5, obj_pronoun5, poss_pronoun5 = get_random_name_and_pronoun()

    # Randomize the age differences and Elaine's age
    age_diff1 = random.randint(3, 10)  # age difference between name1 and name2
    age_diff2 = random.randint(1, 5)   # age difference between name2 and name3
    age_diff3 = random.randint(4, 8)   # age difference between name3 and name4
    elaine_age = random.randint(12, 18) # Elaine's age

    # Calculate the ages
    name1_age = elaine_age * age_diff3
    name3_age = elaine_age + age_diff3
    name2_age = name3_age - age_diff2
    name4_age = name3_age + age_diff3
    name5_age = name1_age + age_diff1

    problem = (f'{name1} is {age_diff1} years younger than {name2}. {name3} is twice as old as {name1}. '
               f'{name4} is {age_diff3} years older than {name3}. {name5} is {age_diff2} times younger than {name4}. '
               f'If {name5} is {elaine_age} years old, how old is {name2}?')

    solution = (f'To find out how old {name2} is, we first calculate the ages of the other characters. '
                f'{name5} is {elaine_age} years old, so {name4} is {elaine_age} * {age_diff2} = {name4_age} years old. '
                f'{name3} is {name4_age} - {age_diff3} = {name3_age} years old. '
                f'{name1} is {elaine_age} / {age_diff3} = {name1_age} years old. '
                f'{name2} is {name3_age} - {age_diff2} = {name2_age} years old. '
                f'Therefore, {name2} is {name2_age} years old.')

    return problem, solution

# Problem 30: Greg is working hard to make money in order to play his favorite arcade game.
def problem30():
    person_a = sm.random_person()
    play_cost = 2
    piggy_bank = random.randint(5, 15)
    cards_price = 5
    cards_per_sale = 3
    cards_sold = random.randint(15, 30)
    
    money_earned = (cards_sold // cards_per_sale) * cards_price
    total_money = piggy_bank + money_earned
    full_games = total_money // play_cost

    problem = (f'{person_a.name} is working hard to make money in order to play {person_a.poss_adjective()} favorite arcade game. Each individual play session costs ${play_cost}. '
               f'Right now, {person_a.subj_pronoun()} has ${piggy_bank} in {person_a.poss_adjective()} piggy bank. To raise money, {person_a.subj_pronoun()} is selling Pokemon cards: '
               f'${cards_price} for every {cards_per_sale} cards. If {person_a.name} sells {cards_sold} cards, how many full games of {person_a.poss_adjective()} favorite arcade game can {person_a.subj_pronoun()} play?')

    solution = (f'To find out how many full games {person_a.name} can play, we first calculate the money earned from selling cards. '
                f'{cards_sold} cards divided by {cards_per_sale} cards per sale equals {cards_sold // cards_per_sale} sales. '
                f'Multiplying this by ${cards_price} per sale, we get ${money_earned}. Adding this to the ${piggy_bank} already in the piggy bank, '
                f'we get a total of ${total_money}. Dividing this by the cost per game, ${play_cost}, we get {full_games} full games. '
                f'Therefore, {person_a.name} can play {full_games} full games of {person_a.poss_adjective()} favorite arcade game.')

    return problem, solution


# Example of generating a random problem and solution
# problem, solution = problem1()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem2()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem3()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem4()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem5()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)


# problem, solution = problem6()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem7()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem8()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem9()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem10()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)


# problem, solution = problem11()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem12()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem13()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem14()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem15()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)


# problem, solution = problem16()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem17()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem18()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem19()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)

# problem, solution = problem20()
# print('\nProblem:')
# print(problem)
# print('\nSolution:')
# print(solution)


problem, solution = problem21()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

problem, solution = problem22()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

problem, solution = problem23()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

problem, solution = problem24()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

problem, solution = problem25()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)


problem, solution = problem26()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

problem, solution = problem27()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

problem, solution = problem28()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

problem, solution = problem29()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

problem, solution = problem30()
print('\nProblem:')
print(problem)
print('\nSolution:')
print(solution)

