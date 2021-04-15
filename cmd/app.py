def readSerial(serial_obj=None):
    s = 'random string'
    return s


def writeSerial(s, serial_obj=None):
    # com with serial
    res = 'res'
    return res


def SolveCommand(s):
    if s[:4] != 'amk#' or s[-1] != '!' or s[5] != '@':
        # print(s[:3], '--', s[-1])
        # display popup message here
        return 'syntax error'
    cmd_no = s[4]
    data = s[6:-1]
    return cmd_no, data


# print(SolveCommand(input('enter command :')))


def CreateCommand(no, data=''):
    return 'amk#'+str(no)+'@'+str(data)+'!'


# print(CreateCommand(9, 'ok'))
