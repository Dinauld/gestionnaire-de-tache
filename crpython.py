"""nom = "Dinauld"
age = 25
taille = 1.73
est_alternant = False

print (nom)
print (age)
print (taille)
print (est_alternant)"""

'''for i in range(5,10):
    print ("repetition n°", 2)'''


'''fruits = ["bananes", "mangues", "pomme"]
print (fruits[1])'''

# Créer une liste vide pour stocker les tâches
tasks = []

# Fonction pour ajouter une tâche
def add_task():
    task = input("Entrez une nouvelle tâche : ")
    tasks.append(task)
    print("Tâche ajoutée.")

# Fonction pour marquer une tâche comme terminée
def complete_task():
    display_tasks()
    task_index = int(input("Entrez le numéro de la tâche terminée : ")) - 1
    if 0 <= task_index < len(tasks):
        print(f"La tâche '{tasks[task_index]}' est marquée comme terminée.")
        del tasks[task_index]
    else:
        print("Numéro de tâche invalide.")

# Fonction pour supprimer une tâche
def delete_task():
    display_tasks()
    task_index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"La tâche '{deleted_task}' a été supprimée.")
    else:
        print("Numéro de tâche invalide.")

# Fonction pour afficher la liste des tâches
def display_tasks():
    if tasks:
        print("Liste des tâches :")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("Aucune tâche pour le moment.")

# Boucle principale
while True:
    print("\nMenu :")
    print("1. Ajouter une tâche")
    print("2. Marquer une tâche comme terminée")
    print("3. Supprimer une tâche")
    print("4. Afficher la liste des tâches")
    print("5. Quitter")

    choice = input("Choisissez une option : ")

    if choice == "1":
        add_task()
    elif choice == "2":
        complete_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        print("Merci d'avoir utilisé le gestionnaire de tâches. Au revoir!")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")
