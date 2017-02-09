print "Tempo di volo"
print
print "Determina la durata massima di volo conoscendo "
print "la quantita' di carburante ed il consumo orario. "
print 

quantita = raw_input("Carburante (in galloni): ")
consumo = raw_input("Consumo orario (in galloni/h): ")
q = float(quantita)
c = float(consumo)

print
print


if  q > 0 and c > 0:

	h = q/c
	m = (float(h)-int(h))*60
	s = (float(m)-int(m))*60

	print "Tempo di volo:", int(h), "h", int(m), "m", int(s), "s"


else : 
	print "ERRORE"
