import csv
import matplotlib.pyplot as plt

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

data_titles = [list[i] for i in range(3)]

x_coords = [float(list[i]) for i in range(4, len(list), 3)]

y_coords = [float(list[i]) for i in range(5, len(list), 3)]

player_1_x_coords = [float(x_coords[i]) for i in range(0, len(x_coords), 3)]

player_2_x_coords = [float(x_coords[i]) for i in range(1, len(x_coords), 3)]

player_3_x_coords = [float(x_coords[i]) for i in range(2, len(x_coords), 3)]
    
player_1_y_coords = [float(y_coords[i]) for i in range(0, len(y_coords), 3)]

player_2_y_coords = [float(y_coords[i]) for i in range(1, len(y_coords), 3)]

player_3_y_coords = [float(y_coords[i]) for i in range(2, len(y_coords), 3)]