kp = float(input(' quantos Km você percorreu? '))
da = int(input(' durante quantos dias? '))
r = 0.15*kp
vpd = 60*da
vap = r+vpd
print(' aluguel custa R$60,00/dia \n cada Km rodado custa R$0.15 ')
print(' você rodou {} Km. \n durante {} dias. \n total a pagar: R${} '.format(kp,da,vap))
