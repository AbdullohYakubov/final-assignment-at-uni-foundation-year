import csv

# user_input = input('Choose an option: \n1. Plots \n2. Analyze Data \n3. Exit \nEnter your choice: 1')
# if user_input.isnumeric() == 1:
#     user_input_2 = input('Choose an option: \n1. Scatter plot for Player 1 \n2. Scatter plot for Player 2 \n3. Scatter plot for Player 3 \n4. Scatter plot for all three players \n5. Stacked bar chart showing score distribution for each player \n6. Go back \nEnter your choice: ')

with open ('dart_hits.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    # list = [' '.join([element for element in row]) for row in csv_reader]
    list = []
    for row in csv_reader:
        for element in row:
            list.append(element)

# x_coords = [list[i] for i in range(4, len(list), 3)]
x_coords = []
for i in range(4, len(list), 3):
    x_coords.append(float(list[i]))
print(x_coords)

y_coords = []
for i in range(5, len(list), 3):
    y_coords.append(float(list[i]))
# print(y_coords)

player_1_x_coords = []
for i in range(0, len(x_coords), 3):
    player_1_x_coords.append(float(list[i]))
# print(player_1_x_coords)

player_2_x_coords = []
for i in range(1, len(x_coords), 3):
    player_2_x_coords.append(float(list[i]))
# print(player_2_x_coords)

player_3_x_coords = []
for i in range(2, len(x_coords), 3):
    player_3_x_coords.append(float(list[i]))
# print(player_3_x_coords)
    
player_1_y_coords = []
for i in range(0, len(y_coords), 3):
    player_1_y_coords.append(float(list[i]))
# print(player_1_y_coords)

player_2_y_coords = []
for i in range(1, len(y_coords), 3):
    player_2_y_coords.append(float(list[i]))
# print(player_2_y_coords)

player_3_y_coords = []
for i in range(2, len(y_coords), 3):
    player_3_y_coords.append(float(list[i]))
# print(player_3_y_coords)