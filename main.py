import csv
import matplotlib.pyplot as plt

with open ('dart_hits.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
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

user_input = input('Choose an option: \n1. Plots \n2. Analyze Data \n3. Exit \nEnter your choice: ')

if int(user_input) == 1:
    user_input_2 = input('Choose an option: \n1. Scatter plot for Player 1 \n2. Scatter plot for Player 2 \n3. Scatter plot for Player 3 \n4. Scatter plot for all three players \n5. Stacked bar chart showing score distribution for each player \n6. Go back \nEnter your choice: ')

    if int(user_input_2) == 1:
        fig, ax = plt.subplots()

        ax.scatter(player_1_x_coords, player_1_y_coords, color = 'black', marker = '+')
        
        ax.set_title('Dart Hits for Player 1', pad = 15, color = 'red')
        ax.set_xlabel('X', loc = 'right')
        ax.set_ylabel('Y', loc = 'top', rotation = 'horizontal')
        ax.axis([-4, 4, -4, 4])
        ax.tick_params(colors = 'blue')
        ax.xaxis.label.set_color('blue')
        ax.yaxis.label.set_color('blue')
        ax.spines['left'].set_color('black')
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_color('black')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        plt.show()

    if int(user_input_2) == 2:
        fig, ax = plt.subplots()

        ax.scatter(player_2_x_coords, player_2_y_coords, color = 'green', marker = 'x')
        
        ax.set_title('Dart Hits for Player 2', pad = 15, color = 'red')
        ax.set_xlabel('X', loc = 'right')
        ax.set_ylabel('Y', loc = 'top', rotation = 'horizontal')
        ax.axis([-4, 4, -4, 4])
        ax.tick_params(colors = 'blue')
        ax.xaxis.label.set_color('blue')
        ax.yaxis.label.set_color('blue')
        ax.spines['left'].set_color('black')
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_color('black')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        plt.show()

    if int(user_input_2) == 3:
        fig, ax = plt.subplots()

        ax.scatter(player_3_x_coords, player_3_y_coords, color = 'blue', marker = 'o')
        
        ax.set_title('Dart Hits for Player 3', pad = 15, color = 'red')
        ax.set_xlabel('X', loc = 'right')
        ax.set_ylabel('Y', loc = 'top', rotation = 'horizontal')
        ax.axis([-4, 4, -4, 4])
        ax.tick_params(colors = 'blue')
        ax.xaxis.label.set_color('blue')
        ax.yaxis.label.set_color('blue')
        ax.spines['left'].set_color('black')
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_color('black')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        plt.show()

    if int(user_input_2) == 4:
        fig, ax = plt.subplots()

        ax.scatter(player_1_x_coords, player_1_y_coords, color = 'black', marker = '+')
        ax.scatter(player_2_x_coords, player_2_y_coords, color = 'green', marker = 'x')
        ax.scatter(player_3_x_coords, player_3_y_coords, color = 'blue', marker = 'o')
        
        ax.set_title('Dart Hits for All Players', pad = 15, color = 'red')
        ax.set_xlabel('X', loc = 'right')
        ax.set_ylabel('Y', loc = 'top', rotation = 'horizontal')
        ax.axis([-4, 4, -4, 4])
        ax.tick_params(colors = 'blue')
        ax.xaxis.label.set_color('blue')
        ax.yaxis.label.set_color('blue')
        ax.spines['left'].set_color('black')
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_color('black')
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')

        plt.show()

    if int(user_input_2) == 5:
        pass

    if int(user_input_2) == 6:
        pass

if int(user_input) == 2:
    pass

if int(user_input) == 3:
    pass