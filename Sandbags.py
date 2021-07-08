print('Sandbags Calculator helps you calculate the number of sangbags you need to protect your home from flood')
L=int(input('• How many linear feet of protection on ground do you need to protect your home with sandbags? '))
H=int(input('• What is the projected flood height in your area? '))
SL=15
SW=11
SH=3
NL = (L*12+4*SL)/SL
NH = (H*12+4*SH)/SH
print(NL)
print(NH)
print('Total number of sandbags you need = ', round(NL*NH))
