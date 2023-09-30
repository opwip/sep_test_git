group = []
counter = 0
while True:
    name = input('name=')
    surname = input('surname=')
    date_of_birth = input('date of birth=')

    student = {'id': counter, 'name': name, 'surname': surname, 'date_of_birth': date_of_birth}
    group.append(student)
    counter += 1