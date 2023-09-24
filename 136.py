nome = str(input("\nEntre com o nome: "))
idade = int(input("\nEntre com a idade: "))

if (idade <= 10):
    print("\n",nome," pagara R$ 30 9 00")
elif(idade <= 29):
    print("\n", nome, " pagara R$ 60,00")
elif(idade <= 45): 
    print("\n", nome, " pagara R$ 120,00")
elif(idade <= 59):
    print("\n ", nome," pagara R$ 150,00")
elif(idade <= 65):
    print(" \n " , nome, " pagara R$ 250,00") 
else:
    print(" \n " , nome, " pagara R$ 400,00")
    

    
