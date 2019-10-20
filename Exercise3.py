file = 'ArxeioC'
list=[] #Δημιουργία λίστας
with open(file, 'r+') as f:
    trigger = False
    for line in f:
#Αναζήτηση στο αρχείο έαν αρχίζει με // ή /*, εάν υπάρχουν τα προσθέτει στην λίστα
        if line.startswith("//"):
            list.append(line)
        elif line.startswith("/*"):
            trigger = True
            list.append(line)
# Αναζήτηση στο αρχείο έαν υπάρχουν στην γραμμή τα // ή /*, εάν υπάρχουν τα προσθέτει στην λίστα
        elif line.find("/*") != -1:
            characters = line[line.find("/*"):len(line)]
            list.append(line)
        elif line.find("//") != -1:
            characters = line[line.find("//"):len(line)]
            list.append(characters)
        elif line.find("*/") != -1:
            trigger = False
            list.append(line)
        elif trigger == True :
            list.append(line)
print(list)
