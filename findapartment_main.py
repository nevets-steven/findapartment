# functions below

def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed == True:
        print(f'Welcome to GC Property Management! Looking up listings in '
              f'{city} for {min_beds} bedroom apartments that allow pets, all within a budget'
              f'of ${max_rent} per month...')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in '
              f'{city} for {min_beds} bedroom apartments, all within a budget'
              f'of ${max_rent} per month...')

def apt_search2(city, max_rent, min_beds=1, pets_allowed=False):
    if pets_allowed == True:
        print(f'Welcome to GC Property Management! Looking up listings in\n '
              f'{city} for {min_beds} bedroom apartments that allow pets, all within a budget\n'
              f'of ${max_rent} per month...')
    else:
        print(f'Welcome to GC Property Management! Looking up listings in\n'
              f'{city} for {min_beds} bedroom apartments, all within a budget\n'
              f'of ${max_rent} per month...')

#function calls below

apt_search2('Detroit', 1000)  # min_beds/pets_allowed omitted
apt_search2('Detroit', 1000, 2) # pets allowed omitted
apt_search2(city='Detroit', max_rent=1000, pets_allowed=True) # min_beds omitted

plus_one_hundred = lambda a : a + 100
print(plus_one_hundred(100))  # 200

square_num = lambda b : b**2
print(square_num(4))  # 16

concatenate = lambda str : '- ' + str
print(concatenate("Task 1"))

divide_by_three = lambda c : c / 3
print(divide_by_three(27))


