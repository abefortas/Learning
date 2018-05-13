def build_car(make, model, year, **options):
    '''creates dictionary with car features'''
    car = {}
    car['make'] = make
    car['model'] = model
    car['year'] = year
    for key, value in options.items():
        car[key] = value
    return car

mycar = build_car('Volkswagen', 'Tiguan', 2015, tow_package = 'yes', heated_seats = 'yes')

print(mycar)