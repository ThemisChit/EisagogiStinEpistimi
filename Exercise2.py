#Δηλώνουμε μία μεταβλητή i ως το input  του χρήστη
i = input("Write something:")

#Αρχικοποιούμε μια μεταβλήτη count
count = 0

#Για κάθε a που υπάρχει στο input i ο οποίος είναι μη εκτυπώσιμος ή κενός,αύξησε το count κατά 1
for a in i:
    if (a.isprintable()) == False or (' ' in a) == True:
        count += 1

#Άνοιγμα αρχείου ώστε να γράψουμε σε αυτό(αν δεν υπάρχει το αρχείο,το δημιουργεί)
f= open('arxeio.txt', 'w+')

#Γράψιμο στο αρχείο των αριθμό των μη εκτυπώσιμων και κενών χαρακτήρων
f.write('The number of non-printable characters and spaces are %d' %count)

#Κλείσμο του αρχείου
f.close()


