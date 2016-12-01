import ply.yacc as yacc

from .lex import tokens

_tokens = tokens

precedence = (
    # ('left', 'PLUS', 'MINUS'),
    # ('left', 'TIMES', 'DIVIDE'),
)


def wrapper(type, values=None, **kwargs):
    _temp = {
        'type': type,
        'values': values if values else []
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
                   | line CR
                   | cr
                   | func
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
            p[0]['line'].append(p[1])
    elif len(p) == 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = wrapper('LINE', [])
        if p[2]:
            p[0]['values'].append(p[2])


def p_expression_line_clip(p):
    ''' line_clip : bold
                  | italic
                  | raw_line
    '''
    p[0] = p[1]


def p_expression_bold(p):
    ''' bold : BOLD LINE BOLD '''
    p[0] = wrapper('BOLD', [p[2]])


def p_expression_italic(p):
    ''' italic : ITALIC LINE ITALIC '''
    p[0] = wrapper('ITALIC', p[2])


def p_expression_raw_line(p):
    ''' raw_line : LINE '''
    p[0] = wrapper('RAW', [p[1]])


def p_expression_cr(p):
    ''' cr : CR '''
    p[0] = wrapper('CR', [])


def multiline_process(p, typestr):
    if len(p) == 5 and p[3]:
        if not p[1]:
            p[1] = wrapper(typestr, [])
        p[1]['values'].append(p[3].strip())
        p[0] = p[1]
    elif len(p) == 4 and p[2]:
        p[0] = wrapper(typestr, [p[2].strip()])


def p_expression_quotes(p):
    ''' quotes : quotes QUOTE LINE CR
               | QUOTE LINE CR
    '''
    multiline_process(p, 'QUOTE')


def p_expression_olists(p):
    ''' olists : olists OLIST LINE CR
               | OLIST LINE CR
    '''
    multiline_process(p, 'OLIST')


def p_expression_ulists(p):
    ''' ulists : ulists ULIST LINE CR
               | ULIST LINE CR
    '''
    multiline_process(p, 'ULIST')


def p_expression_head(p):
    '''headline : HEAD LINE CR'''
    p[0] = wrapper('HEADING', [p[2].strip()], level=len(p[1]))


def p_expression_func(p):
    '''func : FUNC'''
    p[0] = wrapper('FUNC', ['func'])


def p_error(p):
    print("Syntax error in input")
    print(p)


parser = yacc.yacc()
