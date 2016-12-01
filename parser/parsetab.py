
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '987A080F208E8B5346C39AAFDD2CA013'
    
_lr_action_items = {'BOLD':([0,1,2,3,4,5,6,7,9,13,14,15,16,17,18,23,24,25,29,35,36,37,38,40,41,42,43,44,],[8,-13,-11,-17,-6,-16,-8,-4,8,-10,8,-2,-5,-3,-12,35,-7,-9,-1,-14,-15,-21,-23,-24,-19,-20,-18,-22,]),'CR':([0,1,2,3,4,5,6,7,9,13,14,15,16,17,18,24,25,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,],[3,-13,-11,-17,-6,-16,-8,-4,24,-10,3,-2,-5,-3,-12,-7,-9,37,38,-1,40,41,42,43,-14,-15,-21,-23,44,-24,-19,-20,-18,-22,]),'ITALIC':([0,1,2,3,4,5,6,7,9,13,14,15,16,17,18,24,25,26,29,35,36,37,38,40,41,42,43,44,],[10,-13,-11,-17,-6,-16,-8,-4,10,-10,10,-2,-5,-3,-12,-7,-9,36,-1,-14,-15,-21,-23,-24,-19,-20,-18,-22,]),'LINE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,29,30,35,36,37,38,40,41,42,43,44,],[5,-13,-11,-17,-6,-16,-8,-4,23,5,26,27,28,-10,5,-2,-5,-3,-12,31,32,33,34,-7,-9,-1,39,-14,-15,-21,-23,-24,-19,-20,-18,-22,]),'$end':([3,4,6,7,14,15,16,17,24,29,37,38,40,41,42,43,44,],[-17,-6,-8,-4,0,-2,-5,-3,-7,-1,-21,-23,-24,-19,-20,-18,-22,]),'OLIST':([0,3,4,6,7,14,15,16,17,24,29,37,38,40,41,42,43,44,],[11,-17,21,-8,-4,11,-2,-5,-3,-7,-1,-21,-23,-24,-19,-20,-18,-22,]),'QUOTE':([0,3,4,6,7,14,15,16,17,24,29,37,38,40,41,42,43,44,],[20,-17,-6,-8,22,20,-2,-5,-3,-7,-1,-21,-23,-24,-19,-20,-18,-22,]),'HEAD':([0,3,4,6,7,14,15,16,17,24,29,37,38,40,41,42,43,44,],[19,-17,-6,-8,-4,19,-2,-5,-3,-7,-1,-21,-23,-24,-19,-20,-18,-22,]),'ULIST':([0,3,4,6,7,14,15,16,17,24,29,37,38,40,41,42,43,44,],[12,-17,-6,-8,-4,12,-2,30,-3,-7,-1,-21,-23,-24,-19,-20,-18,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bold':([0,9,14,],[2,2,2,]),'raw_line':([0,9,14,],[1,1,1,]),'italic':([0,9,14,],[18,18,18,]),'olists':([0,14,],[4,4,]),'cr':([0,14,],[6,6,]),'quotes':([0,14,],[7,7,]),'line':([0,14,],[9,9,]),'line_clip':([0,9,14,],[13,25,13,]),'content':([0,],[14,]),'expression':([0,14,],[15,29,]),'ulists':([0,14,],[16,16,]),'headline':([0,14,],[17,17,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> content","S'",1,None,None,None),
  ('content -> content expression','content',2,'p_content','yacc.py',14),
  ('content -> expression','content',1,'p_content','yacc.py',15),
  ('expression -> headline','expression',1,'p_expression','yacc.py',31),
  ('expression -> quotes','expression',1,'p_expression','yacc.py',32),
  ('expression -> ulists','expression',1,'p_expression','yacc.py',33),
  ('expression -> olists','expression',1,'p_expression','yacc.py',34),
  ('expression -> line CR','expression',2,'p_expression','yacc.py',35),
  ('expression -> cr','expression',1,'p_expression','yacc.py',36),
  ('line -> line line_clip','line',2,'p_expression_line','yacc.py',42),
  ('line -> line_clip','line',1,'p_expression_line','yacc.py',43),
  ('line_clip -> bold','line_clip',1,'p_expression_line_clip','yacc.py',65),
  ('line_clip -> italic','line_clip',1,'p_expression_line_clip','yacc.py',66),
  ('line_clip -> raw_line','line_clip',1,'p_expression_line_clip','yacc.py',67),
  ('bold -> BOLD LINE BOLD','bold',3,'p_expression_bold','yacc.py',74),
  ('italic -> ITALIC LINE ITALIC','italic',3,'p_expression_italic','yacc.py',82),
  ('raw_line -> LINE','raw_line',1,'p_expression_raw_line','yacc.py',90),
  ('cr -> CR','cr',1,'p_expression_cr','yacc.py',98),
  ('quotes -> quotes QUOTE LINE CR','quotes',4,'p_expression_quotes','yacc.py',121),
  ('quotes -> QUOTE LINE CR','quotes',3,'p_expression_quotes','yacc.py',122),
  ('olists -> olists OLIST LINE CR','olists',4,'p_expression_olists','yacc.py',128),
  ('olists -> OLIST LINE CR','olists',3,'p_expression_olists','yacc.py',129),
  ('ulists -> ulists ULIST LINE CR','ulists',4,'p_expression_ulists','yacc.py',135),
  ('ulists -> ULIST LINE CR','ulists',3,'p_expression_ulists','yacc.py',136),
  ('headline -> HEAD LINE CR','headline',3,'p_expression_head','yacc.py',142),
]