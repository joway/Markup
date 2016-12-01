import ply.lex as lex

tokens = (
    'HEAD',
    'QUOTE',
    'OLIST',
    'ULIST',
    'BOLD',
    'ITALIC',
    'LINE',
    'CR',
    'FUNC'
)


def t_HEAD(t):
    r'(?m)^\#{1,6} '
    return t


def t_QUOTE(t):
    r'(?m)^\> '
    return t


def t_OLIST(t):
    r'(?m)^\d+\.\ '
    return t


def t_ULIST(t):
    r'(?m)^(\*|-)\ '
    return t


def t_BOLD(t):
    r'\*\*'
    return t


def t_ITALIC(t):
    r'\_\_'
    return t


def t_LINE(t):
    r'([^\*\_\n])+'
    return t


def t_CR(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t


def t_FUNC(t):
    r'{% (.+?) %}(.+?){% (.+?) %}'
    return t


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    print(t)
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == '__main__':
    # 测试数据
    s = '''
    # 一级标题

    ## 二级标题

    > 引用
    '''

    lexer.input(s)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
