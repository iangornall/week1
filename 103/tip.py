bill = float(raw_input('Total bill amount? '))
service = raw_input('Level of service? (good, fair or bad) ')
tip = {'good': .2, 'fair': .15, 'bad': .1}
tip_amount = bill * tip[service]
print 'Tip amount: $%.2f' % tip_amount