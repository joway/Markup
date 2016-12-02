import ply.yacc as yacc

from parser.lex import tokens

_tokens = tokens

precedence = (
    # ('left', 'PLUS', 'MINUS'),
    # ('left', 'TIMES', 'DIVIDE'),
)


def wrapper(_type, value, **kwargs):
    _temp = {
        'type': _type,
        'value': value
    }
    for k in kwargs:
        _temp[k] = kwargs[k]
    return _temp


def p_content(p):
    ''' content : content expression
                | expression
    '''
    if len(p) == 2 and p[1]:
        if not p[0]:
            p[0] = [p[1]]
        else:
            p[0].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = []
        if p[2]:
            p[0].append(p[2])


def p_expression(p):
    ''' expression : headline
                   | quotes
                   | ulists
                   | olists
                   | func
                   | func_with_params
                   | line CR
                   | cr
    '''
    p[0] = p[1]


def p_expression_line(p):
    ''' line : line line_clip
             | line_clip
    '''
    if len(p) == 2 and p[1]:
        if not p[0]:
            p[0] = wrapper('LINE', [p[1]])
        else:
            p[0]['value'].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = wrapper('LINE', [])
        if p[2]:
            p[0]['value'].append(p[2])


def p_expression_line_clip(p):
    ''' line_clip : bold
                  | italic
                  | sentence
    '''
    p[0] = p[1]


def p_expression_sentence(p):
    ''' sentence : sentence EMPTY
                 | sentence WORD
                 | WORD
                 | EMPTY
    '''
    if len(p) == 2 and p[1]:
        if not p[0]:
            p[0] = p[1]
        else:
            p[0] += p[1]
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = ''
        if p[2]:
            p[0] += p[2]


def p_expression_bold(p):
    ''' bold : BOLD sentence BOLD '''
    p[0] = wrapper('BOLD', p[2])


def p_expression_italic(p):
    ''' italic : ITALIC sentence ITALIC '''
    p[0] = wrapper('ITALIC', p[2])


def p_expression_params(p):
    ''' func_params : LEFT_PAREN sentence RIGHT_PAREN
               | EMPTY LEFT_PAREN sentence RIGHT_PAREN
               | LEFT_PAREN sentence RIGHT_PAREN EMPTY
               | EMPTY LEFT_PAREN sentence RIGHT_PAREN EMPTY
    '''
    if len(p) == 4:
        p[0] = p[2]
    elif len(p) == 5:
        if p[1] == '(':
            p[0] = p[2]
        else:
            p[0] = p[3]
    elif len(p) == 6:
        p[0] = p[3]


def p_expression_func_mark(p):
    ''' func_mark : DOLLAR WORD
             | DOLLAR WORD EMPTY
    '''
    p[0] = p[2]


def p_expression_func_block(p):
    ''' func_block : LEFT_BRACE content RIGHT_BRACE
                   | LEFT_BRACE content RIGHT_BRACE EMPTY
    '''
    p[0] = p[2]


def p_expression_func(p):
    ''' func : func_mark func_block
    '''
    p[0] = wrapper('FUNC', {
        'func_name': p[1],
        'func_body': p[2],
    })


def p_expression_func_with_params(p):
    ''' func_with_params : func_mark func_params func_block
    '''
    p[0] = wrapper('FUNC', [p[2], p[3]])


def p_expression_cr(p):
    ''' cr : CR '''
    p[0] = wrapper('CR', '')


def p_expression_quotes(p):
    ''' quotes : quotes QUOTE sentence cr
               | QUOTE sentence cr
    '''
    multiline_process(p, 'QUOTE')


def p_expression_olists(p):
    ''' olists : olists OLIST sentence cr
               | OLIST sentence cr
    '''
    multiline_process(p, 'OLIST')


def p_expression_ulists(p):
    ''' ulists : ulists ULIST sentence cr
               | ULIST sentence cr
    '''
    multiline_process(p, 'ULIST')


def p_expression_head(p):
    '''headline : HEAD sentence cr'''
    p[0] = wrapper('HEADING', p[2].strip(), level=len(p[1]))


def p_error(p):
    print("Syntax error in input")
    print(p)


def multiline_process(p, type_str):
    if len(p) == 5 and p[3]:
        if not p[1]:
            p[1] = wrapper(type_str, [])
        p[1]['value'].append(p[3].strip())
        p[0] = p[1]
    elif len(p) == 4 and p[2]:
        p[0] = wrapper(type_str, [p[2].strip()])


parser = yacc.yacc(debug=True)

if __name__ == '__main__':
    data = """
# 123
$center  {

code

}
$center(params1, params2){
code
}

"""
    result = parser.parse(data, debug=False)
    for i in result:
        print(i)
