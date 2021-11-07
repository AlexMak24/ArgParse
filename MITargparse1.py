import argparse
parser=argparse.ArgumentParser()
parser.add_argument('Name',help='Your name')
parser.add_argument('Sex',help='Your sex')
parser.add_argument('height',type=int,help='Your Height')
parser.add_argument('weight',type=int,help='Your weight')
parser.add_argument('duration_of_sleep',choices=['Less_than_7_hours','7-8_hours','More_than_8_hours'],help='How_many_hours_do_you_sleep?')
parser.add_argument('number_of_meals',choices=['1_meal','2-3_meals','4-5_meals'],help='How_many_meals_do_you_have_per_day?')
parser.add_argument('f_and_v',choices=['I_do_not_eat_these_products_regularly','Less_than_500_grams','More_than_500_grams'],help='How many fresh fruits and vegetables do you eat during the day? I do not eat these products regularly, Less than 500 grams, More than 500 grams')
parser.add_argument('number_of_steps',choices=['Less_than_5_thousand_steps','5-10_thousand_steps','More_than_10_thousand_steps'],help='number_of_steps_per_day')
parser.add_argument('healthmonitoring',choices=['Not','Yes,I_have_been_undergoing_medical_examination_in_the_last_3_years','Yes,_but_I_do_not_see_a_doctor'],  help='Do you monitor your health? Not; Yes, I have been undergoing medical examination in the last 3 years (1 point), Yes, but I do not see a doctor')
parser.add_argument('mood',choices=['Good','Neutral','Bad'], help='What is your mood today')
parser.add_argument('happiness',choices=['During_the_week','During_the_month','During_the_year']   ,help='When was the last time you had a state of happiness? During the week (1 point), During the month (1 point), During the year')

args=parser.parse_args()
IBM=(int(args.weight)/(int(args.height))**2)
mark=0
if IBM<=24.9 and 18.5>=IBM:
    mark=mark+1
if args.duration_of_sleep=='7-8_hours':
    mark=mark+1
if args.number_of_meals=='4-5_meals':
    mark=mark+1
if args.f_and_v=='More_than_500_grams':
    mark=mark+1
if args.number_of_steps=='More_than_10_thousand_steps':
    mark=mark+1
if args.healthmonitoring=='Yes,_I_have_been_undergoing_medical_examination_in_the_last_3_years':
    mark=mark+1
if args.mood=='Good':
    mark=mark+1
if args.happiness=='During_the_week':
    mark=mark+1
if mark<=7 and 5<=mark:
    print('Your_health_index_is_[5-7]/8,_which_means_that_you_are_on_the_right_track!')
if mark<=4 and 0<=mark:
    print('[0-4] points Your healthy lifestyle index is [0-4]/8 🤢, you need to rethink your healthy lifestyle!')
if mark==8:
    print('8 points Your index of a healthy lifestyle is 8/8, which means that you are a true leader in a healthy lifestyle!')
print(mark)

