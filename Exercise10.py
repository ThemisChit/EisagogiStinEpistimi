#Δύο λίστες,μία για τους χαρακτήρες που ανοίγουν μία παρένθεση και μία για αυτούς που την κλείνουν
open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

# Δημίουργια της συνάρτησης parentheses που ελέγχει τις παρενθέσεις
def parentheses(k):
    stack = []
    for i in k:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            thesi = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[thesi] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Οι παρενθέσεις είναι λάθος."
    if len(stack) == 0:
        return "Οι παρενθέσεις είναι σωστές."
    else:
        return "Οι παρενθέσεις είναι λάθος."


protasi = input("Γράψε κάτι:")
print(protasi, "-", parentheses(protasi))