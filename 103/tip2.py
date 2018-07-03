bill = float(raw_input('Total bill amount? '))
service = raw_input('Level of service? (good, fair or bad) ')
people = float(raw_input('Split how many ways? '))
tip = {'good': .2, 'fair': .15, 'bad': .1}
tip_amount = bill * tip[service]
total = bill + tip_amount
split = total / people
print 'Tip amount: $%.2f' % tip_amount
print 'Total amount: $%.2f' % total
print 'Amount per person: $%.2f' % split