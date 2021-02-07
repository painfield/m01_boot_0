def clear():
    print('\033[2J')

def position(line,column=None):
    if column is None:
        column = 1
    print('\033[{};{}H'.format(line, column),end='')
    
def lineDel(line=None,column=None):
    if line is not None:
        position(line,column)
    print('\033[K',end='')
    
def Format(line=None,column=None,*formato):
    estilo = {'reset':'0','bold':'1','italic':'3','underline':'4','blink':'5','reverse':'6',\
              'DFblack':'30','DFred':'31','DFgreen':'32','DFyellow':'33','DFblue':'34','DFmagenta':'35','DFcyan':'36','DFwhite':'37',\
              'DBblack':'40','DBred':'41','DBgreen':'42','DByellow':'43','DBblue':'44','DBmagenta':'45','DBcyan':'46','DBwhite':'47',\
              'BFblack':'90','BFred':'91','BFgreen':'92','BFyellow':'93','BFblue':'94','BFmagenta':'95','BFcyan':'96','BFwhite':'97',\
              'BBblack':'100','BBred':'101','BBgreen':'102','BByellow':'103','BBblue':'104','BBmagenta':'105','BBcyan':'106','BBwhite':'107',}
    if type(line) is int:
        if type(column) is int:
            Print('\033[',line,column)
        else:
            Print('\033['+estilo[column]+';',line,1)
    else:
        Print('\033['+estilo[line]+';')
        if column is not None:
            Print(estilo[column]+';')
    for style in formato:
        if style in estilo:
            Print(estilo[style]+';')
    Print('\bm')
    
def Print(cadena,line=None,column=None,delEnd=False):
    if line is not None:
        position(line,column)
    if delEnd:
        lineDel()
    print(cadena,end='')

def Input(cadena,line=None,column=None,delEnd=True):
    if line is not None:
        position(line,column)
    if delEnd:
        lineDel()
    return input(cadena)