#Δημιουργία μια συνάρτησης meta
def meta(lista):

# Εάν η lista είναι άδεια,δεν υπάρχουν μεταθέσεις
    if len(lista) == 0:
        return []

# Εάν υπάρχει μόνο ένα στοιχείο στην lista,τότε υπάρχει μόνο μια μετάθεση
    if len(lista) == 1:
        return [lista]

    k = []  # άδεια λίστα η οποία θα αποθηκεύει την  μετάθεση

    for i in range(len(lista)):
        n = lista[i]
        remLista = lista[:i] + lista[i + 1:]

#Δημιουργία όλων των μεταθέσεων όπου το n είναι το πρώτο στοιχείο
        for p in meta(remLista):
            k.append([n] + p)
    return k


# Δημιούργια λίστας text η οποία θα δέχεται το input του χρήστη το οποίο θα μετατρέπεται απο string σε λίστα
text = []
text = input("Δώσε n χαρακτήρες χωρισμένους με κόμμα(π.χ.:α,β,γ):")
text = text.split(',')

for p in meta(text):
    print(p)