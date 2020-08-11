% ingredientes
ingredientes(sopa_de_cebolla,[cebolla,caldo,agua]).
ingredientes(bizcocho_vainilla,[huevo,mantequilla,azucar,harina,vainilla]).
ingredientes(pizza,[harina,sal,agua,aceite,levadura]).

% procedimientos
procedimientos(sopa_de_cebolla,[pelar,cortar,hervir]).
procedimientos(bizcocho_vainilla,[agregar,mezclar,batir,hornear]).
procedimientos(pizza,[mezclar,batir,mezclar_aceite,amazar,reposar,dar_forma,preparar,hornear]).

pertenece(X,[X|_]).
pertenece(X,[_|Cola]):-pertenece(X,Cola).

en_la_lista([],_).
en_la_lista([H|T],L) :- en_la_lista(T,L), pertenece(H,L).

not_in_the_list([],_).
not_in_the_list([H|T],L) :- not_in_the_list(T,L), not(pertenece(H,L)).

%%%% P R I M E R   P U N T O
contiene_el_ingrediente(Ingrediente,Salida) 
  :- ingredientes(Salida,L),
     pertenece(Ingrediente,L),
     write(Salida),nl,fail.

%%%% S E G U N D O   P U N T O
contiene_al_menos_tres(X) 
  :- ingredientes(Salida,L),
     en_la_lista(L,X),
     write(Salida),nl,fail.

%%%% T E R C E R  P U N T O
contiene_herramienta(Herramienta,Salida) 
  :- procedimientos(Salida,L),
     pertenece(Herramienta,L),
     write(Salida),nl,fail.

%%%% C U A R T O  P U N T O
no_tiene_herramienta(Herramienta,Salida) 
  :- procedimientos(Salida,L),
     not(pertenece(Herramienta,L)),
     write(Salida),nl,fail.

%%%% Q U I N T O  P U N T O
no_tiene_ingrediente(Ingrediente,Salida) 
  :- ingredientes(Salida,L),
     not(pertenece(Ingrediente,L)),
     write(Salida),nl,fail.

%%%% S E X T O  P U N T O
no_tiene_ingrediente_ni_herramienta(Ingrediente, Herramienta,Salida)
  :- ingredientes(Salida,L),
     not(pertenece(Ingrediente,L)),
     procedimientos(Salida,L2),
     not(pertenece(Herramienta,L2)),
     write(Salida),nl,fail.

%%%% E X T R A
no_tiene_varios_ingredientes(X) 
  :- ingredientes(Salida,L),
     not_in_the_list(L,X),
     write(Salida),nl,fail.
