#!/usr/bin/env python
import pdb
import numpy as np

# compute angular separation in degree
def angsep(ra1,dec1,ra2,dec2):
	ra11 = np.radians(ra1)
	dec11 = np.radians(dec1)
	ra22 = np.radians(ra2)
	dec22 = np.radians(dec2)
	y = np.cos(np.pi/2.-dec11)*np.cos(np.pi/2.-dec22) \
		+ np.sin(np.pi/2.-dec11)*np.sin(np.pi/2.-dec22)*np.cos(ra11-ra22)
	return np.degrees(np.arccos(y))

def angsep2radiff(asep,dec):
	asep = np.radians(asep)	# convert degree to radian
	dec = np.radians(dec)
	sign = asep/abs(asep)
	dra = np.degrees(np.arccos((np.cos(asep) - (np.cos(np.pi/2.-dec))**2) / (np.sin(np.pi/2.-dec))**2.))*sign
	return dra	# in degree


# convert hh:mm:ss, dd:mm:ss to degress
def hms2radec(rah,ram,ras,decd,decm,decs):
	ra = (rah+ram/60.+ras/3600.)*15.
	minus = decd < 0
	plus = decd >= 0
	dec = np.zeros(len(ra))
	dec[plus] = decd[plus]+decm[plus]/60.+decs[plus]/3600.
	dec[minus] = decd[minus]-decm[minus]/60.-decs[minus]/3600.
	return ra,dec
