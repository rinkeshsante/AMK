def readSerial(serial_obj=None):
    s = 'random string'
    return s


def writeSerial(s, serial_obj=None):
    # com with serial
    res = 'res'
    return res


def SolveCommand(s):
    if s[:4] != 'amk#' or s[-1] != '!' or s[5] != '@':
        # display popup message here
        return 'syntax error'
    cmd_no = s[4]
    data = s[6:-1]
    return cmd_no, data


# print(SolveCommand(input('enter command :')))


def CreateCommand(no, data=''):
    return 'amk#'+str(no)+'@'+str(data)+'!'


# print(CreateCommand(9, 'ok'))

while True:
    op = '''-------------------------------------
    0: exit
    1: setSQL
    2: autoSQL
    3: getPWM
    4: setPWM
    5: listen
    6: send
    '''
    print(op)

    c = int(input('Enter choice : '))

    if c == 0:
        break

    elif c == 1:
        pass

    elif c == 2:
        pass

    elif c == 3:
        pass

    elif c == 4:
        pass

    elif c == 5:
        cmd = readSerial()
        no, data = SolveCommand(cmd)
        if no == 5:  # check cmd from hardware
            print('cmd error')
        print(data)

    elif c == 6:
        msg = input('enter message : ')
        cmd = CreateCommand(4, msg)  # check cmd from hardware
        op = writeSerial(cmd)
        print('op :', op)

    else:
        print('invalid command')
