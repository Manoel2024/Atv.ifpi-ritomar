print("Em que ano voçê nasceu?")
nascimento = input()
nascimento = int(nascimento)
print("Para qual ano voçê quer saber sua idade?")
futuro = input()
futuro = int(futuro)
idade = futuro - nascimento
print ("em", futuro, "voçê terá", idade, "anos!")