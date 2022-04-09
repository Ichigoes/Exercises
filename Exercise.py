command_data = input().split("-")
command = command_data[0]
guest = command_data[1]
meal = command_data[2]

meals_dict = dict()

unliked_meals = 0

while command_data[0] != "Stop":

    if command_data[0] == "Stop":
        break

    if command == "Like":
        if guest not in meals_dict and meal not in meals_dict:
            meals_dict[guest] = [meal]
        elif guest in meals_dict and meal not in meals_dict:
            meals_dict[guest] += [meal]

    elif command == "Unlike":
        if guest not in meals_dict:
            print(f"{guest} is not at the party.")
        elif meal not in meals_dict[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        elif guest in meals_dict and meal in meals_dict[guest]:
            print(f"{guest} doesn't like the {meal}.")
            meals_dict[guest].remove(meal)
            unliked_meals += 1

    command_data = input().split("-")
    command = command_data[0]
    guest = command_data[1]
    meal = command_data[2]

for guest in meals_dict:
    print(f"{guest}: {', '.join(meals_dict[guest])}")
print(f"Unliked meals: {unliked_meals}")


