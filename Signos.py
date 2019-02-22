print('>>> \033[1;31mSIGNOS\033[m <<<')
n=str(input('\nQual o seu nome?\n\t'))
d=int(input('\nPor favor digite o dia do seu nascimento:\n\t'))
m=str(input('\nPor favor digite o seu mês: \n\t'))


if str(m) == 'janeiro' and int(d) >= 21 or str(m) == 'fevereiro' and int(d) <= 19:
    print(n,' o seu signo é \033[46mAquário ♒\033[m')

elif str(m) == 'fevereiro' and int(d) >= 20 or str(m) == 'março' and int(d) <= 20:
    print(n,' o seu signo é \033[46mPeixes ♓\033[m')

elif str(m) == 'março' and int(d) >= 21 or str(m) == 'abril' and int(d) <= 20:
    print(n,' o seu signo é \033[46mÁries ♈\033[m')

elif str(m) == 'abril' and int(d) >= 21 or str(m) == 'maio' and int(d) <= 20:
    print(n,' o seu signo é \033[46mTouro ♉\033[m')

elif str(m) == 'maio' and int(d) >= 21 or str(m) == 'junho' and int(d) <= 20:
    print(n,' o seu signo é \033[46mGêmeos ♊\033[m')

elif str(m) == 'junho' and int(d) >= 21 or str(m) == 'julho' and int(d) <= 21:
    print(n,' o seu signo é \033[46mCâncer ♋\033[m')

elif str(m) == 'julho' and int(d) >= 22 or str(m) == 'agosto' and int(d) <= 22:
    print(n,' o seu signo é \033[46mLeâo ♌\033[m')

elif str(m) == 'agosto' and int(d) >= 23 or str(m) == 'setembro' and int(d) <= 22:
    print(n,' o seu signo é \033[46mVirgem ♍\033[m')

elif str(m) == 'setembro' and int(d) >= 23 or str(m) == 'outubro' and int(d) <= 22:
    print(n,' o seu signo é \033[46mLibra ♎\033[m')

elif str(m) == 'outubro' and int(d) >= 23 or str(m) == 'novembro' and int(d) <= 21:
    print(n,' o seu signo é \033[46mEscorpião ♏\033[m')

elif str(m) == 'novembro' and int(d) >= 22 or str(m) == 'dezembro' and int(d) <= 21:
    print(n,' o seu signo é \033[46mSagitário ♐\033[m')

elif str(m) == 'dezembro' and int(d) >= 22 or str(m) == 'janeiro' and int(d) <= 20:
    print(n,' o seu signo é \033[46mCapricórnio ♑\033[m')
