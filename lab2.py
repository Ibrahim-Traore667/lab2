'''
Ibrahim Traore 
 
05/09/24

this program is to calculate human age in animals age

'''

# human age to dog age 

human_age = float(input("Please enter the age: "))
dog_age = (human_age) * 7
dog_age_totaldays = (human_age) * 7 * 360


dog_years = int(dog_age_totaldays) // 360
remaining_days = dog_age_totaldays % 360
dog_months = int(remaining_days) // 30
dog_days = int(remaining_days) % 30

print ('your dog age is', (dog_years) ,'years' , (dog_months) , 'months' , (dog_days), 'days')

# human age to cat age

human_age = float(input("Please enter the age: "))
cat_age = human_age / 9
cat_age_totaldays = (cat_age) * 360

cat_years = int(cat_age_totaldays // 360)
remaining_days = cat_age_totaldays % 360
cat_months = int(remaining_days // 30)
cat_days = int(remaining_days % 30)

print('your cat age is', cat_years, 'years', cat_months, 'months', cat_days, 'days')

# human age to horse age

human_age = float(input("Please enter the age: "))
horse_age = 3 * (((human_age ** 2 - 47) / 7) + 12)
horse_age_totaldays = horse_age * 360

horse_years = int(horse_age_totaldays // 360)
remaining_days = horse_age_totaldays % 360
horse_months = int(remaining_days // 30)
horse_days = int(remaining_days % 30)

print(f'Your horse age is {horse_years} years, {horse_months} months, and {horse_days} days')



