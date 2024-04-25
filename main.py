import csv
import matplotlib.pyplot as plt
import numpy as np

try:
    with open ('dart_hits.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        list = [[element for element in row] for row in csv_reader]

except FileNotFoundError:
    print('dart_hits.csv file not found!')

else:
    x_coords = [float(list[i][1]) for i in range(1, len(list))]

    y_coords = [float(list[i][2]) for i in range(1, len(list))]

    player_1_x_coords = [x_coords[i] for i in range(0, len(x_coords), 3)]

    player_2_x_coords = [x_coords[i] for i in range(1, len(x_coords), 3)]

    player_3_x_coords = [x_coords[i] for i in range(2, len(x_coords), 3)]
        
    player_1_y_coords = [y_coords[i] for i in range(0, len(y_coords), 3)]

    player_2_y_coords = [y_coords[i] for i in range(1, len(y_coords), 3)]

    player_3_y_coords = [y_coords[i] for i in range(2, len(y_coords), 3)]

    num_of_10_for_p1 = 0
    num_of_5_for_p1 = 0
    num_of_1_for_p1 = 0
    num_of_0_for_p1 = 0
    for i in range(len(player_1_x_coords)):
        radius_p1 = (player_1_x_coords[i]**2 + player_1_y_coords[i]**2)**0.5
        if radius_p1 <= 1:
            num_of_10_for_p1 += 1
        elif radius_p1 <= 2:
            num_of_5_for_p1 += 1
        elif radius_p1 <= 3:
            num_of_1_for_p1 += 1
        else:
            num_of_0_for_p1 += 1

    num_of_10_for_p2 = 0
    num_of_5_for_p2 = 0
    num_of_1_for_p2 = 0
    num_of_0_for_p2 = 0
    for i in range(len(player_2_x_coords)):
        radius_p2 = (player_2_x_coords[i]**2 + player_2_y_coords[i]**2)**0.5
        if radius_p2 <= 1:
            num_of_10_for_p2 += 1
        elif radius_p2 <= 2:
            num_of_5_for_p2 += 1
        elif radius_p2 <= 3:
            num_of_1_for_p2 += 1
        else:
            num_of_0_for_p2 += 1

    num_of_10_for_p3 = 0
    num_of_5_for_p3 = 0
    num_of_1_for_p3 = 0
    num_of_0_for_p3 = 0
    for i in range(len(player_3_x_coords)):
        radius_p3 = (player_3_x_coords[i]**2 + player_3_y_coords[i]**2)**0.5
        if radius_p3 <= 1:
            num_of_10_for_p3 += 1
        elif radius_p3 <= 2:
            num_of_5_for_p3 += 1
        elif radius_p3 <= 3:
            num_of_1_for_p3 += 1
        else:
            num_of_0_for_p3 += 1

    while True:
        user_input = input('Choose an option: \n1. Plots \n2. Analyze Data \n3. Exit \nEnter your choice: ')
        
        try:
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

                    ax.scatter(player_2_x_coords, player_2_y_coords, color = 'black', marker = '+')
                    
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

                    ax.scatter(player_3_x_coords, player_3_y_coords, color = 'black', marker = '+')
                    
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
                    x_params = ['Player 1', 'Player 2', 'Player 3']
                    point_10 = np.array([num_of_10_for_p1, num_of_10_for_p2, num_of_10_for_p3])
                    point_5 = np.array([num_of_5_for_p1, num_of_5_for_p2, num_of_5_for_p3])
                    point_1 = np.array([num_of_1_for_p1, num_of_1_for_p2, num_of_1_for_p3])
                    point_0 = np.array([num_of_0_for_p1, num_of_0_for_p2, num_of_0_for_p3])

                    plt.title('Frequency of Hits')
                    plt.xlabel('Players')
                    plt.ylabel('Frequency')

                    plt.bar(x_params, point_10, color = 'red')
                    plt.bar(x_params, point_5, bottom = point_10, color = 'blue')
                    plt.bar(x_params, point_1, bottom = point_5 + point_10, color = 'green')
                    plt.bar(x_params, point_0, bottom = point_1 + point_5 + point_10, color = 'purple')

                    plt.legend(["10", "5", "1", "0"], loc = 'upper right')

                    plt.show()

                if int(user_input_2) == 6:
                    continue

            if int(user_input) == 2:
                def calculateOverallScore(point_10, point_5, point_1, player):
                    print(f'Overall score for {player}: {point_10 * 10 + point_5 * 5 + point_1 * 1}')
                calculateOverallScore(num_of_10_for_p1, num_of_5_for_p1, num_of_1_for_p1, 'Player 1')
                calculateOverallScore(num_of_10_for_p2, num_of_5_for_p2, num_of_1_for_p2, 'Player 2')
                calculateOverallScore(num_of_10_for_p3, num_of_5_for_p3, num_of_1_for_p3, 'Player 3')

                def calculateAverageDisplacement(_x_coords, _y_coords, player):
                    total_x_coords = 0
                    for i in range(len(_x_coords)):
                        total_x_coords += _x_coords[i]
                        average_x_coords = total_x_coords/len(_x_coords)
                    
                    total_y_coords = 0
                    for i in range(len(_y_coords)):
                        total_y_coords += _y_coords[i]
                        average_y_coords = total_y_coords/len(_y_coords)
                    
                    print(f'Average displacement for {player}: ({round(average_x_coords, 2)}, {round(average_y_coords, 2)})')

                calculateAverageDisplacement(player_1_x_coords, player_1_y_coords, 'Player 1')
                calculateAverageDisplacement(player_2_x_coords, player_2_y_coords, 'Player 2')
                calculateAverageDisplacement(player_3_x_coords, player_3_y_coords, 'Player 3')

                print('...And the Winner with the highest score is... Player 1! \nCongratulations to Player 1 on winning the Dart Contest!')

                break

            if int(user_input) == 3:
                print('Exiting...')
                break

        except ValueError:
            print('Invalid Error!')
            continue