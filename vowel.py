ch=raw_input()
if (ch>='a' and ch<='z') or (ch>='A' and ch<='z'):
	if ch in ['a','e','i','o','u','A','E','I','O','U']:
		print ('Vowel')
	else :
		print ('Consonant')
else:
	print ('invalid')
