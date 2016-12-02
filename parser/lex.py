import ply.lex as lex

tokens = (
    # markdown
    'HEAD',
    'QUOTE',
    'OLIST',
    'ULIST',
    'BOLD',
    'ITALIC',

    # function
    'DOLLAR',  # $
    'LEFT_PAREN',  # (
    'RIGHT_PAREN',  # )
    'LEFT_BRACE',  # {
    'RIGHT_BRACE',  # }

    'WORD',
    'EMPTY',
    'CR',

    # symbol
    # 'COMMA',
    # 'SEMI',
)

# Markdown
t_HEAD = r'^(?m)\#{1,6} '
t_QUOTE = r'(?m)^\> '
t_OLIST = r'(?m)^\d+\.\ '
t_ULIST = r'(?m)^(\*|-)\ '
t_BOLD = r'\*\*'

# Function
t_DOLLAR = r'\$'
t_LEFT_PAREN = r'\('
t_RIGHT_PAREN = r'\)'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_ITALIC = r'\_\_'

# t_LINE = r'([^\*\_\n])+'
t_EMPTY = r'\s+'
t_WORD = r'\w+'


def t_CR(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t


def t_error(t):
    print('Illegal character "%s"' % t.value[0])
    print(t)
    t.lexer.skip(1)


lexer = lex.lex(debug=False)

if __name__ == '__main__':
    # 测试数据
    s = '''
# 123

1. xxx
2. aaaa

$center {
code
}
   '''

    lexer.input(s)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
