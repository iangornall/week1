want = 'yes'
coins = 0
while want == 'yes':
    print 'You have %d coins' % coins
    want = raw_input('Do you want another? (yes or no) ')
    coins += 1
print 'Bye'