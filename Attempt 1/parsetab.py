
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '7CD735908439EBD2C3787749C00A5DB9'
    
_lr_action_items = {'QUOTE':([0,2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[1,-17,-15,-16,-20,-18,-14,-22,-21,1,-4,1,1,-10,-12,-11,-9,-5,-13,]),'FLOAT':([0,2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[2,-17,-15,-16,-20,-18,-14,-22,-21,2,-4,2,2,-10,-12,-11,-9,-5,-13,]),'$end':([0,2,3,4,6,7,8,9,10,11,12,13,14,16,26,27,],[-19,-17,-15,-16,-20,-2,-18,-14,-3,-22,-21,0,-1,-4,-5,-13,]),'NUM':([0,2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[4,-17,-15,-16,-20,-18,-14,-22,-21,4,-4,4,4,-10,-12,-11,-9,-5,-13,]),'LPAREN':([0,1,2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[5,15,-17,-15,-16,-20,-18,-14,-22,-21,5,-4,5,5,-10,-12,-11,-9,-5,-13,]),'TRUE':([0,2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[6,-17,-15,-16,-20,-18,-14,-22,-21,6,-4,6,6,-10,-12,-11,-9,-5,-13,]),'TEXT':([0,2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[8,-17,-15,-16,-20,-18,-14,-22,-21,8,-4,8,8,-10,-12,-11,-9,-5,-13,]),'RPAREN':([2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,23,24,25,26,27,],[-17,-15,-16,-20,-18,-14,-22,-21,-8,-4,-8,-8,-10,-7,-11,-9,26,27,-6,-5,-13,]),'SIMB':([0,2,3,4,5,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[9,-17,-15,-16,17,-20,-18,-14,-22,-21,9,-4,9,9,-10,-12,-11,-9,-5,-13,]),'NIL':([0,2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[11,-17,-15,-16,-20,-18,-14,-22,-21,11,-4,11,11,-10,-12,-11,-9,-5,-13,]),'FALSE':([0,2,3,4,6,8,9,11,12,15,16,17,18,19,20,21,22,26,27,],[12,-17,-15,-16,-20,-18,-14,-22,-21,12,-4,12,12,-10,-12,-11,-9,-5,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'item':([15,17,18,],[18,18,18,]),'bool':([0,15,17,18,],[3,3,3,3,]),'quoted_list':([0,15,17,18,],[7,19,19,19,]),'list':([1,],[16,]),'empty':([15,17,18,],[20,20,20,]),'call':([0,15,17,18,],[10,21,21,21,]),'exp':([0,],[13,]),'atom':([0,15,17,18,],[14,22,22,22,]),'items':([15,17,18,],[23,24,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> atom','exp',1,'p_exp_atom','yacc.py',44),
  ('exp -> quoted_list','exp',1,'p_exp_qlist','yacc.py',48),
  ('exp -> call','exp',1,'p_exp_call','yacc.py',52),
  ('quoted_list -> QUOTE list','quoted_list',2,'p_quoted_list','yacc.py',56),
  ('list -> LPAREN items RPAREN','list',3,'p_list','yacc.py',61),
  ('items -> item items','items',2,'p_items','yacc.py',65),
  ('items -> empty','items',1,'p_items_empty','yacc.py',69),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',73),
  ('item -> atom','item',1,'p_item_atom','yacc.py',77),
  ('item -> quoted_list','item',1,'p_item_list','yacc.py',85),
  ('item -> call','item',1,'p_item_call','yacc.py',89),
  ('item -> empty','item',1,'p_item_empty','yacc.py',93),
  ('call -> LPAREN SIMB items RPAREN','call',4,'p_call','yacc.py',97),
  ('atom -> SIMB','atom',1,'p_atom_simbol','yacc.py',107),
  ('atom -> bool','atom',1,'p_atom_bool','yacc.py',111),
  ('atom -> NUM','atom',1,'p_atom_num','yacc.py',115),
  ('atom -> FLOAT','atom',1,'p_atom_float','yacc.py',119),
  ('atom -> TEXT','atom',1,'p_atom_word','yacc.py',123),
  ('atom -> <empty>','atom',0,'p_atom_empty','yacc.py',127),
  ('bool -> TRUE','bool',1,'p_true','yacc.py',131),
  ('bool -> FALSE','bool',1,'p_false','yacc.py',135),
  ('atom -> NIL','atom',1,'p_nil','yacc.py',139),
]
