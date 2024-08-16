import pprint
import sys
sys.path.append('/home/slye/mat-106-bank/outcomes/')
import slye_math as sm
import random
from fractions import Fraction

def run_G1():

    def contractor_selection():
        # TODO: Eliminate possibility of equal costs
        # TODO: Make 2nd contractor always more, but 50% chance of discount making sense
        person = sm.random_person()
        contractor1_rate = random.randint(50, 80)
        contractor2_rate = random.randint(55, 85)
        discount = random.randint(30, 50)
        hours = random.randint(8, 16)

        contractor1_cost = contractor1_rate * hours
        contractor2_cost = (contractor2_rate * hours) - discount
        cost_difference = abs(contractor1_cost - contractor2_cost)

        problem = (f"{person.name}'s mom is trying to find a contractor to work on their house. The first contractor charges ${contractor1_rate} per hour. "
                f"The second contractor charges ${contractor2_rate} per hour, but there is a ${discount} discount on the total bill if chosen. "
                f"If {person.poss_adjective()} mom needs the contractor to work for {hours} hours, how much more will the total bill come to if they choose the second contractor instead of the first?")

        solution = (f"To find the total cost for each contractor, we multiply the hourly rate by the number of hours needed. "
                    f"The total cost for the first contractor is ${contractor1_rate} per hour multiplied by {hours} hours, which equals ${contractor1_cost}. "
                    f"The total cost for the second contractor is ${contractor2_rate} per hour multiplied by {hours} hours minus the ${discount} discount, which equals ${contractor2_cost}. "
                    f"The difference in cost between the two contractors is ${cost_difference}. Therefore, the total bill will be ${cost_difference} more if they choose the second contractor.")

        return problem, solution

    def cookie_stand():
        person = sm.random_person()
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

        problem = (f"{person.name} runs a small cookie stand every weekend. This weekend, {person.subj_pronoun()} started by baking {trays_initial} trays of cookies. "
                f"Each tray fits {cookies_per_tray} cookies at a time. On Friday, {person.subj_pronoun()} sold {sold_friday} cookies. So, {person.subj_pronoun()} decided to make {extra_trays} more trays of cookies on Saturday morning. "
                f"{person.subj_pronoun()} sold {sold_saturday} more cookies on Saturday, and {sold_sunday} more cookies on Sunday. {person.subj_pronoun()} decides to bring the extra remaining cookies to school to share with {person.poss_adjective()} class on Monday. "
                f"How many cookies does {person.subj_pronoun()} have to share with {person.poss_adjective()} class?")

        solution = (f"To find out how many cookies {person.name} has to share with {person.poss_adjective()} class, we first calculate the total number of cookies baked. "
                    f"{trays_initial} trays multiplied by {cookies_per_tray} cookies per tray equals {initial_cookies} cookies. "
                    f"Then, {person.subj_pronoun()} baked {extra_trays} more trays of cookies, which adds another {extra_cookies} cookies. "
                    f"The total number of cookies is {total_cookies}. Subtracting the cookies sold on Friday, Saturday, and Sunday, which totals {sold_friday + sold_saturday + sold_sunday}, "
                    f"there are {remaining_cookies} cookies left. Therefore, {person.name} has {remaining_cookies} cookies to share with {person.poss_adjective()} class.")

        return problem, solution

    def christmas_decorations():
        person = sm.random_person()
        spool1 = random.randint(1, 3)
        spool2 = Fraction(random.randint(1, 3), random.randint(2, 4))
        project1 = Fraction(random.randint(1, 2), random.randint(2, 4))
        project2 = Fraction(random.randint(1, 2), random.randint(3, 4))
        project3 = Fraction(random.randint(1, 2), random.randint(1, 3))
        total_twine = spool1 + spool2
        total_needed = project1 + project2 + project3
        has_enough = total_twine >= total_needed

        problem = (f"{person.name} is making some Christmas decorations with twine, but {person.subj_pronoun()} is running out of twine to use! "
                f"{person.subj_pronoun().capitalize()} measures {person.poss_adjective()} remaining twine before starting {person.poss_adjective()} projects. "
                f"{person.subj_pronoun()} has {spool1} ft of twine on one spool, and {spool2} ft of twine on another spool. {person.poss_adjective()} first project requires {project1} ft of twine, "
                f"{person.poss_adjective()} second project requires {project2} ft, and {person.poss_adjective()} third project requires {project3} ft. Will {person.name} have enough twine to make all three projects? Why or why not?")

        solution = (f"To find out if {person.name} has enough twine to complete all three projects, we first calculate the total amount of twine available. "
                    f"{spool1} ft plus {spool2} ft equals {total_twine} ft of twine. Then, we add up the amount of twine needed for each project. "
                    f"{project1} ft plus {project2} ft plus {project3} ft equals {total_needed} ft of twine needed. "
                    f"{person.name} {'has' if has_enough else 'does not have'} enough twine to complete all three projects because {person.subj_pronoun()} needs {total_needed} ft but only has {total_twine} ft.")

        return problem, solution

    def walking_distance():
        person = sm.random_person()
        distance1 = Fraction(random.randint(1, 3), random.randint(3, 5))
        distance2 = Fraction(random.randint(1, 2), random.randint(4, 6))
        backtrack = Fraction(random.randint(1, 2), random.randint(4, 8))
        total_distance = distance1 + distance2 - backtrack

        problem = (f"{person.name} is walking down a straight road from {person.poss_adjective()} house to the market. "
                f"{person.subj_pronoun().capitalize()} walks {distance1} mi. before taking a rest. Then, {person.subj_pronoun()} keeps walking another {distance2} mi. "
                f"At that point, {person.subj_pronoun()} realizes that {person.subj_pronoun()} already walked past the market, and backtracks {backtrack} mi. to get to the market. "
                f"How far is it from {person.name}'s house to the market?")

        solution = (f"To find out the total distance from {person.name}'s house to the market, we add the distances {person.subj_pronoun()} walked and then subtract the distance {person.subj_pronoun()} backtracked. "
                    f"{distance1} mi. plus {distance2} mi. equals {distance1 + distance2} mi. Then, subtracting the {backtrack} mi. backtracked, we get {total_distance} mi. "
                    f"Therefore, the total distance from {person.name}'s house to the market is {total_distance} mi.")

        return problem, solution

    def student_fractions():
        freshman_fraction = Fraction(1, 6)
        sophomore_fraction = Fraction(random.randint(3, 7), 12)
        junior_fraction = Fraction(random.randint(1, 3), 3)
        total_students = freshman_fraction + sophomore_fraction + junior_fraction
        senior_fraction = 1 - total_students

        problem = (f"Mountain View High School has four types of students: freshman, sophomores, juniors, and seniors. If the student body is {freshman_fraction} freshmen, "
                f"{sophomore_fraction} sophomores, and {junior_fraction} juniors, what fraction of the student body is made up of seniors?")

        solution = (f"To find out what fraction of the student body is seniors, we first add the fractions representing the freshmen, sophomores, and juniors. "
                    f"{freshman_fraction} plus {sophomore_fraction} plus {junior_fraction} equals {total_students}. "
                    f"The fraction of seniors is found by subtracting this total from 1, which equals {senior_fraction}. "
                    f"Therefore, the fraction of the student body that is seniors is {senior_fraction}.")

        return problem, solution

    def bebsi_production():
        person = sm.random_person()
        cans_per_hour = random.randint(10000, 20000)
        cans_per_case = random.randint(20, 30)
        hours = random.randint(2, 5)
        total_cans = cans_per_hour * hours
        total_cases = total_cans // cans_per_case

        problem = (f"{person.name}'s family works at Bebsi Co., where {cans_per_hour} cans of Bebsi are produced each hour. "
                f"The cans are packed in cases containing {cans_per_case} cans each. "
                f"How many cases could be filled with the cans produced in {hours} hours?")

        solution = (f"To find out how many cases could be filled, we first calculate the total number of cans produced in {hours} hours. "
                    f"{cans_per_hour} cans per hour multiplied by {hours} hours equals {total_cans} cans. "
                    f"Dividing this by {cans_per_case} cans per case, we get {total_cases} cases. "
                    f"Therefore, {total_cases} cases could be filled with the cans produced in {hours} hours.")

        return problem, solution

    def walking_to_bathroom():
        person = sm.random_person()
        art_room_distance = random.randint(100, 150)
        music_room_distance_fraction = Fraction(random.randint(1, 3), random.randint(3, 5))
        gym_distance = random.randint(300, 400)
        bathroom_distance = random.randint(40, 60)

        music_room_distance = music_room_distance_fraction * gym_distance
        classroom_to_bathroom_distance = art_room_distance + music_room_distance + bathroom_distance

        problem = (f"{person.name} is walking down a straight hallway from {person.poss_adjective()} classroom to the bathroom. "
                f"{person.poss_adjective().capitalize()} classroom is at the very end of the hall. The art room is {art_room_distance} feet from {person.poss_adjective()} classroom. "
                f"The music room is {music_room_distance_fraction} of the way from the art room to the gym. "
                f"It is another {bathroom_distance} feet from the music room to the bathroom. If the gym is {gym_distance} feet from {person.poss_adjective()} classroom, how far is it from {person.poss_adjective()} classroom to the bathroom?")

        solution = (f"To find out how far it is from {person.name}'s classroom to the bathroom, we first calculate the distance from the art room to the music room. "
                    f"The music room is {music_room_distance_fraction} of the distance from the art room to the gym, which is {music_room_distance} feet. "
                    f"Adding the distances: {art_room_distance} feet (art room) + {music_room_distance} feet (music room) + {bathroom_distance} feet (to bathroom) = {classroom_to_bathroom_distance} feet. "
                    f"Therefore, the distance from {person.name}'s classroom to the bathroom is {classroom_to_bathroom_distance} feet.")

        return problem, solution

    def buying_house():
        person = sm.random_person()
        house_price = random.randint(200000, 300000)
        down_payment = random.randint(20000, 40000)
        monthly_payments = random.randint(180, 300)

        remaining_amount = house_price - down_payment
        monthly_payment_amount = remaining_amount // monthly_payments

        problem = (f"{person.name}'s family is buying a new house. The agreed-upon price for the house at the time of closing is ${house_price}. "
                f"The bank requires an immediate down payment of ${down_payment}. The remaining amount will be paid over {monthly_payments} equal monthly payments. "
                f"Assuming there is no interest involved, how much will {person.name}'s family need to pay each month?")

        solution = (f"To find out how much {person.name}'s family will need to pay each month, we first subtract the down payment from the house price to find the remaining amount. "
                    f"${house_price} minus ${down_payment} equals ${remaining_amount}. Dividing this by {monthly_payments} monthly payments, we get ${monthly_payment_amount} per month. "
                    f"Therefore, {person.name}'s family will need to pay ${monthly_payment_amount} each month.")

        return problem, solution
    
    def age_comparisons():
        person = sm.random_person()
        bert_age = random.randint(10, 20)
        alfonso_age = bert_age + 5
        callie_age = bert_age * 2
        diane_age = callie_age + 6
        elaine_age = random.randint(12, 18)
        diane_multiplier = diane_age // elaine_age

        problem = (f"{person.name} is five years younger than Alfonso. Callie is twice as old as {person.obj_pronoun()}. Diane is 6 years older than Callie. "
                f"Elaine is {diane_multiplier} times younger than Diane. If Elaine is {elaine_age} years old, how old is Alfonso?")

        solution = (f"To find out how old Alfonso is, we first calculate the ages of the other characters. "
                    f"{person.name} is {bert_age} years old, so Alfonso is {bert_age} + 5 = {alfonso_age} years old. "
                    f"Callie is twice as old as {person.name}, which is {bert_age} * 2 = {callie_age} years old. "
                    f"Diane is 6 years older than Callie, which is {callie_age} + 6 = {diane_age} years old. "
                    f"Elaine is {diane_multiplier} times younger than Diane, so Diane's age divided by the multiplier gives {elaine_age} years old. "
                    f"Therefore, Alfonso is {alfonso_age} years old.")

        return problem, solution

    def arcade_games():
        person = sm.random_person()
        play_cost = 2
        piggy_bank = random.randint(5, 15)
        cards_price = 5
        cards_per_sale = 3
        cards_sold = random.randint(15, 30)
        
        money_earned = (cards_sold // cards_per_sale) * cards_price
        total_money = piggy_bank + money_earned
        full_games = total_money // play_cost

        problem = (f"{person.name} is working hard to make money in order to play {person.poss_adjective()} favorite arcade game. Each play session costs ${play_cost}. "
                f"Right now, {person.subj_pronoun()} has ${piggy_bank} in {person.poss_adjective()} piggy bank. To raise money, {person.subj_pronoun()} is selling cards: "
                f"${cards_price} for every {cards_per_sale} cards. If {person.name} sells {cards_sold} cards, how many full games of {person.poss_adjective()} favorite arcade game can {person.subj_pronoun()} play?")

        solution = (f"To find out how many full games {person.name} can play, we first calculate the money earned from selling cards. "
                    f"{cards_sold} cards divided by {cards_per_sale} cards per sale equals {cards_sold // cards_per_sale} sales. "
                    f"Multiplying this by ${cards_price} per sale, we get ${money_earned}. Adding this to the ${piggy_bank} already in the piggy bank, "
                    f"we get a total of ${total_money}. Dividing this by the cost per game, ${play_cost}, we get {full_games} full games. "
                    f"Therefore, {person.name} can play {full_games} full games of {person.poss_adjective()} favorite arcade game.")

        return problem, solution
     
    prob_sol = [contractor_selection(), cookie_stand(), christmas_decorations(), walking_distance(), student_fractions(),
                bebsi_production(), walking_to_bathroom(), buying_house(), age_comparisons(), arcade_games()]

    return {
            'p1_prob': prob_sol[0][0],
            'p1_sol': prob_sol[0][1],
            'p2_prob': prob_sol[1][0],
            'p2_sol': prob_sol[1][1],
            'p3_prob': prob_sol[2][0],
            'p3_sol': prob_sol[2][1],
            'p4_prob': prob_sol[3][0],
            'p4_sol': prob_sol[3][1],
            'p5_prob': prob_sol[4][0],
            'p5_sol': prob_sol[4][1],
            'p6_prob': prob_sol[5][0],
            'p6_sol': prob_sol[5][1],
            'p7_prob': prob_sol[6][0],
            'p7_sol': prob_sol[6][1],
            'p8_prob': prob_sol[7][0],
            'p8_sol': prob_sol[7][1],
            'p9_prob': prob_sol[8][0],
            'p9_sol': prob_sol[8][1],
            'p10_prob': prob_sol[9][0],
            'p10_sol': prob_sol[9][1],
    }

pprint.pprint(run_G1())