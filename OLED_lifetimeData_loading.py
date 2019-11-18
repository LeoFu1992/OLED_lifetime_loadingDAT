import os
def downloadA():
    lt = []
    with open('A.DAT', 'r') as f:
        for data in f:
            data = data.strip()
            lt.append(data)
    lt.remove(lt[1])
    with open('LifetimeA.csv', 'w', encoding='utf-8') as file:
        for a in range(0, len(lt)-1, 1):
            file.write(lt[a] + ',' + '\n')
def downloadB():
    lt = []
    with open('B.DAT', 'r') as f:
        for data in f:
            data = data.strip()
            lt.append(data)
    lt.remove(lt[1])
    with open('LifetimeB.csv', 'w', encoding='utf-8') as file:
        for a in range(0, len(lt)-1, 1):
            file.write(lt[a] + ',' + '\n')
def downloadC():
    lt = []
    with open('C.DAT', 'r') as f:
        for data in f:
            data = data.strip()
            lt.append(data)
    lt.remove(lt[1])
    with open('LifetimeC.csv', 'w', encoding='utf-8') as file:
        for a in range(0, len(lt)-1, 1):
            file.write(lt[a] + ',' + '\n')
def downloadD():
    lt = []
    with open('D.DAT', 'r') as f:
        for data in f:
            data = data.strip()
            lt.append(data)
    lt.remove(lt[1])
    with open('LifetimeD.csv', 'w', encoding='utf-8') as file:
        for a in range(0, len(lt)-1, 1):
            file.write(lt[a] + ',' + '\n')
if os.path.isfile('A.DAT'):
    if os.path.isfile('B.DAT'):
        if os.path.isfile('C.DAT'):
            if os.path.isfile('D.DAT'):
                downloadA()
                downloadB()
                downloadC()
                downloadD()
            else:
                downloadA()
                downloadB()
                downloadC()
        else:
            if os.path.isfile('D.DAT'):
                downloadA()
                downloadB()
                downloadD()
            else:
                downloadA()
                downloadB()
    else:
        if os.path.isfile('C.DAT'):
            if os.path.isfile('D.DAT'):
                downloadA()
                downloadC()
                downloadD()
            else:
                downloadA()
                downloadC()
        else:
            if os.path.isfile('D.DAT'):
                downloadA()
                downloadD()
            else:
                downloadA()
else:
    if os.path.isfile('B.DAT'):
        if os.path.isfile('C.DAT'):
            if os.path.isfile('D.DAT'):
                downloadB()
                downloadC()
                downloadD()
            else:
                downloadB()
                downloadC()
        else:
            if os.path.isfile('D.DAT'):
                downloadB()
                downloadD()
            else:
                downloadB()
    else:
        if os.path.isfile('C.DAT'):
            if os.path.isfile('D.DAT'):
                downloadC()
                downloadD()
            else:
                downloadC()
        else:
            if os.path.isfile('D.DAT'):
                downloadD()