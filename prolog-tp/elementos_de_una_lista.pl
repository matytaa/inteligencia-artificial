cantidad_de_elementos([], L, L).

cantidad_de_elementos([_|Xs], N, L):-
          N2 is N + 1,
          cantidad_de_elementos(Xs, N2, L). %cantidad_de_elementos([a,b,c,d,e], 0, L).