import random
kms = int(random.randrange(60, 120, 10))
kms_A_Mais = int(kms - 80)
if kms> 80:
    print(f"""
    Voce estava a {kms}
     então voce deve pagar {kms_A_Mais * 7}
     """)
else:
    print('voce não vai receber multa')