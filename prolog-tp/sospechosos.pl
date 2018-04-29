vive_en_la_mansion(agatha).

vive_en_la_mansion(carnicero).

vive_en_la_mansion(charles).

la_persona_odia_a(charles,Persona):- vive_en_la_mansion(Persona), not(la_persona_odia_a(agatha,Persona)).

la_persona_odia_a(agatha,Persona):- vive_en_la_mansion(Persona), not(Persona==carnicero).

la_persona_odia_a(carnicero,Persona):- vive_en_la_mansion(Persona), la_persona_odia_a(agatha,Persona).

es_mas_rico_que(Persona, agatha):- not(la_persona_odia_a(carnicero,Persona)),vive_en_la_mansion(Persona).

el_asesino_es(Persona, agatha):- la_persona_odia_a(Persona,agatha), not(es_mas_rico_que(Persona, agatha)).
