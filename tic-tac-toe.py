theboard={'top-l':' ','top-m':' ','top-r':' ',
          'mid-l':' ','mid-m':' ','mid-r':' ',
          'low-l':' ','low-m':' ','low-r':' '}
def printboard(theboard):
    print(theboard['top-l']+'|'+theboard['top-m']+'|'+theboard['top-r'])
    print('-+--+-')
    print(theboard['mid-l']+'|'+theboard['mid-m']+'|'+theboard['mid-r'])
    print('-+--+-')
    print(theboard['low-l']+'|'+theboard['low-m']+'|'+theboard['low-r'])
turn='X'
for i in range(9):
    printboard(theboard)
    print('Turn for'+turn+'which space u want to move?')
    move=input()
    theboard[move]=turn
    if turn=='X':
        turn= 'O'
    else:
        turn='X'

printboard(theboard)
