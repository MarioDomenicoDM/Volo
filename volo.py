print "Tempo di volo"
print
print "Determina la durata massima di volo conoscendo "
print "la quantita' di carburante ed il consumo orario. "
print 

q = input("Carburante (in galloni): ")
c = input("Consumo orario (in galloni/h): ")
print
print


if q > c and q > 0 and c > 0:

	h = q/c
	m = (float(h)-int(h))*60
	s = (float(m)-int(m))*60

	print "Tempo di volo:", int(h), "h", int(m), "m", int(s), "s"


else : 
	print "ERRORE"
