def fix_economy(people):
    fixit_fund = 0
    for person in people.keys():
        fixit_fund += people[person].money
        people[person].money = 0

    person = people['erikodes']
    person.money += fixit_fund
    fixit_fund = 0

    print('done')
