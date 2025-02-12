#75 g salted butter
#350 g flour
#150 ml milk


scones = int(input("How many scones do you want?"))

butter = float((75/10) * scones)
flour = float((350/10) * scones)
milk = float((150/10) * scones)

cups_butter = (butter * (1/3 /75))
cups_flour = (flour * (1 / 150))
cups_milk = (milk * (1/2 / 100))




print("To make", scones,"scones you will need:", cups_butter, "cups of butter", cups_flour, "cups of flour and", cups_milk, "cups of milk")