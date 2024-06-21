from random import randint

first1, second2, third3 = int(input("first :", "second :", "third :"))

resulta1, resulta2, resulta3 = randint(0, 9), randint(0, 9), randint(0, 9)


print("Imong bet:", first1, second2, third3)
print("Resulta: ", resulta1, resulta2, resulta3)

if first1 == resulta1 and second2 == resulta2 and third3 == resulta3:
    print("You win! Perfect match!")

elif (first1 == resulta1 and second2 == resulta3 and third3 == resulta2) or \
     (first1 == resulta3 and second2 == resulta1 and third3 == resulta2) or \
     (first1 == resulta3 and second2 == resulta2 and third3 == resulta3) or \
     (first1 == resulta3 and second2 == resulta1):
    print("Partial win! Unique combination!")

else:
    print("Patad patad pud sig ober think nga makadaug! Better luck next time!")