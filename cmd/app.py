import serial
port = '/dev/ttyS0'
ard = serial.Serial(port, 9600, timeout=5)


def readSerial(serial_obj=None):
    msg = ard.read(ard.inWaiting())
    return msg


def writeSerial(s, serial_obj=None):
    ard.write(setTemp1)
    time.sleep(6)
    # com with serial


def SolveCommand(s):
    if s[:4] != 'amk#' or s[-1] != '!' or s[5] != '@':
        # display popup message here
        return 'syntax error'
    cmd_no = s[4]
    data = s[6:-1]
    return cmd_no, data


def CreateCommand(no, data=''):
    return 'amk#'+str(no)+'@'+str(data)+'!'


while True:
    op = '''-------------------------------------
    0: exit
    1: setSQL
    2: autoSQL
    3: getPWM
    4: setPWM
    5: listen
    '''
    print(op)

    c = int(input('Enter choice : '))

    if c == 0:
        # set sql
        sql = input('enter sql value')
        # -- validate sql value here
        cmd = CreateCommand(3, sql)
        writeSerial(cmd)
        res = readSerial()
        no, data = SolveCommand(res)

        if no == '4':
            print('setted to :', data)
        else:
            print('error in set sql -->', data)

    elif c == 1:
        # auto sql
        cmd = CreateCommand(1)
        writeSerial(cmd)
        res = readSerial()
        no, data = SolveCommand(res)

        if no == '2':
            print('auto sql  :', data)
        else:
            print('error in auto sql -->', data)

    elif c == 2:
        # get pwm
        cmd = CreateCommand(8)
        writeSerial(cmd)
        res = readSerial()
        no, data = SolveCommand(res)

        if no == '9':
            print('setted to :', data)
        else:
            print('error in getpwm -->', data)

    elif c == 3:
        # set pwm
        # not defined yet

    elif c == 4:
        pass

    elif c == 5:
        res = readSerial()
        print(res)

    else:
        print('invalid command')
