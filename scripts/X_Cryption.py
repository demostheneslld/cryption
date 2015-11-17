#########################################
########## CRYPTION IMPORTS #############
#########################################

allowed_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}','|',';','\'',':','"',',','.','/','<','>','?',' ']

def get_c_values(allowed_chars):
	import X_Cryption as cryption
	c_values = {}
	for i in range(0,len(cryption.allowed_chars)):
	    c_values[cryption.allowed_chars[i]] = i
	return c_values
