import ply.lex as lex

tokens = (
    'BLOCK',
)


def t_BLOCK(t):
    r'\{\%\ block\ \S+\ \%\}([\s\S]*)\{\%\ endblock\ \%\}'
    return t


# def t_LINE(t):
#     r'([^\*\_\n])+'
#     return t


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

if __name__ == '__main__':
    # 测试数据
    s = '''
{% block funciton %}
param string
{% endblock %}
    '''

    lexer.input(s)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
