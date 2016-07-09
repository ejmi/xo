#!/usr/bin/env python2
def narysujplansze(arg):
	print '+ - - - +'
	print '|', arg[1], arg[2], arg[3], '|'
	print '|', arg[4], arg[5], arg[6], '|'
	print '|', arg[7], arg[8], arg[9], '|'
	print '+ - - - +'

#----------------------------------------------
plansza = {
	1: ' ',
	2: ' ',
	3: ' ',
	4: ' ',
	5: ' ',
	6: ' ',
	7: ' ',
	8: ' ',
	9: ' '
}
narysujplansze(plansza)	

#------- sprawdzam kto wygral ----------------------------------------------------------
def sprawdzCzyWygral(plansza):
	gracze = ['o', 'x']
	for gracz in gracze:
		if plansza[1] == gracz and plansza[2] == gracz and plansza[3] == gracz:
			return gracz
		if plansza[4] == gracz and plansza[5] == gracz and plansza[6] == gracz:
			return gracz
		if plansza[7] == gracz and plansza[8] == gracz and plansza[9] == gracz:
			return gracz
		if plansza[1] == gracz and plansza[4] == gracz and plansza[7] == gracz:
			return gracz
		if plansza[2] == gracz and plansza[5] == gracz and plansza[8] == gracz:
			return gracz
		if plansza[3] == gracz and plansza[6] == gracz and plansza[9] == gracz:
			return gracz
		if plansza[1] == gracz and plansza[5] == gracz and plansza[9] == gracz:
			return gracz						
		if plansza[3] == gracz and plansza[5] == gracz and plansza[7] == gracz:
			return gracz			

	liczbaZajetychPol = 0
	for klucz, wartosc in plansza.iteritems():
		if plansza[klucz] != ' ':
			liczbaZajetychPol += 1
	if liczbaZajetychPol == 9:
		return 'remis'



#---------------------------------------------------------------------------------------

gracz = 'o'
czygramy = True
while czygramy:
	print "aktualny gracz: " + gracz
	pole = int(raw_input('Podaj numer pola: '))
	if plansza[pole] != ' ':
		print 'pole jest juz zajete. wybierz inne'
		continue
	plansza[pole] = gracz
	narysujplansze(plansza)
	if gracz == 'o':
		gracz ='x'
	else:
		gracz = 'o'

	ktoWygral = sprawdzCzyWygral(plansza)
	if ktoWygral == 'o':
		czygramy = False
		print 'wygralo O'
	elif ktoWygral == 'x':
		czygramy = False
		print 'wygral X'	
	elif ktoWygral == 'remis':
		czygramy = False
		print 'jest remis!'

	