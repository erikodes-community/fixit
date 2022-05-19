def fix_economy(people):
    fixit_fund = 0
    for person in people:
        fixit_fund += person.money
        person.money -= person.money

    for person in people:
        if person == 'erikodes':
            person.money += fixit_fund
            fixit_fund = 0

    print('done')
