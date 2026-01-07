def generate_ascii_art():
    height = 24
    width = 45
    
    for row in range(height):
        for column in range(width):
            char = ' '
            
            # Row 0: @@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@%%%%%%%%%%
            if row == 0:
                if 0 <= column <= 27:
                    char = '@'
                elif 28 <= column <= 32:
                    char = '%'
                elif 33 <= column <= 34:
                    char = '@'
                elif 35 <= column <= 44:
                    char = '%'
            
            # Row 1: @@@@@@@@@@@@@@@%******#%@@%%%%%%%%%%@@@@%%%%%
            elif row == 1:
                if 0 <= column <= 14:
                    char = '@'
                elif column == 15:
                    char = '%'
                elif 16 <= column <= 21:
                    char = '*'
                elif column == 22:
                    char = '#'
                elif column == 23:
                    char = '%'
                elif 24 <= column <= 25:
                    char = '@'
                elif 26 <= column <= 34:
                    char = '%'
                elif 35 <= column <= 38:
                    char = '@'
                elif 39 <= column <= 44:
                    char = '%'
            
            # Row 2: @@@@@@@@@@@@#****++++***+=+#%%%%%%%%%%%%%%%%
            elif row == 2:
                if 0 <= column <= 11:
                    char = '@'
                elif column == 12:
                    char = '#'
                elif 13 <= column <= 16:
                    char = '*'
                elif 17 <= column <= 20:
                    char = '+'
                elif 21 <= column <= 23:
                    char = '*'
                elif column == 24:
                    char = '='
                elif column == 25:
                    char = '+'
                elif column == 26:
                    char = '#'
                elif 27 <= column <= 44:
                    char = '%'
            
            # Row 3: @@@@@@@@@%#****++===========+%%%%%%%%%%%%%%%%
            elif row == 3:
                if 0 <= column <= 8:
                    char = '@'
                elif column == 9:
                    char = '%'
                elif column == 10:
                    char = '#'
                elif 11 <= column <= 14:
                    char = '*'
                elif 15 <= column <= 16:
                    char = '+'
                elif 17 <= column <= 25:
                    char = '='
                elif column == 26:
                    char = '+'
                elif 27 <= column <= 44:
                    char = '%'
            
            # Row 4: @@@@@@@@@#####*==-=+==-====++*%%%%%%%%%%%%%%%
            elif row == 4:
                if 0 <= column <= 8:
                    char = '@'
                elif 9 <= column <= 13:
                    char = '#'
                elif column == 14:
                    char = '*'
                elif 15 <= column <= 16:
                    char = '='
                elif column == 17:
                    char = '-'
                elif column == 18:
                    char = '='
                elif column == 19:
                    char = '+'
                elif column == 20:
                    char = '='
                elif column == 21:
                    char = '-'
                elif 22 <= column <= 25:
                    char = '='
                elif 26 <= column <= 27:
                    char = '+'
                elif column == 28:
                    char = '+'
                elif column == 29:
                    char = '*'
                elif 30 <= column <= 44:
                    char = '%'
            
            # Row 5: @@@@@@@@%%%%%##*+++++=======++#@@@@@%%%%%%%%%
            elif row == 5:
                if 0 <= column <= 7:
                    char = '@'
                elif 8 <= column <= 12:
                    char = '%'
                elif 13 <= column <= 14:
                    char = '#'
                elif column == 15:
                    char = '*'
                elif 16 <= column <= 20:
                    char = '+'
                elif 21 <= column <= 27:
                    char = '='
                elif 28 <= column <= 29:
                    char = '+'
                elif column == 30:
                    char = '#'
                elif 31 <= column <= 35:
                    char = '@'
                elif 36 <= column <= 44:
                    char = '%'
            
            # Row 6: @@@@@@@@%%%%%%%#*+========+++++#@@@@@@@%%%%%%
            elif row == 6:
                if 0 <= column <= 7:
                    char = '@'
                elif 8 <= column <= 14:
                    char = '%'
                elif column == 15:
                    char = '#'
                elif column == 16:
                    char = '*'
                elif column == 17:
                    char = '+'
                elif 18 <= column <= 25:
                    char = '='
                elif 26 <= column <= 30:
                    char = '+'
                elif column == 31:
                    char = '#'
                elif 32 <= column <= 38:
                    char = '@'
                elif 39 <= column <= 44:
                    char = '%'
            
            # Row 7: @@@@@@@@%%%@%%##*##**###****###+@@@@@@@@@@%%%
            elif row == 7:
                if 0 <= column <= 7:
                    char = '@'
                elif 8 <= column <= 10:
                    char = '%'
                elif column == 11:
                    char = '@'
                elif 12 <= column <= 13:
                    char = '%'
                elif 14 <= column <= 15:
                    char = '#'
                elif column == 16:
                    char = '*'
                elif column == 17:
                    char = '#'
                elif column == 18:
                    char = '*'
                elif column == 19:
                    char = '*'
                elif 20 <= column <= 22:
                    char = '#'
                elif 23 <= column <= 26:
                    char = '*'
                elif 27 <= column <= 29:
                    char = '#'
                elif column == 30:
                    char = '#'
                elif column == 31:
                    char = '#'
                elif 32 <= column <= 41:
                    char = '@'
                elif 42 <= column <= 44:
                    char = '%'
            
            # Row 8: @@@@@@@@@%%%%%****#%%@%#*=+*+#*+%@@@@@@@@@@@@
            elif row == 8:
                if 0 <= column <= 8:
                    char = '@'
                elif 9 <= column <= 13:
                    char = '%'
                elif 14 <= column <= 17:
                    char = '*'
                elif column == 18:
                    char = '#'
                elif column == 19:
                    char = '%'
                elif column == 20:
                    char = '@'
                elif column == 21:
                    char = '%'
                elif column == 22:
                    char = '#'
                elif column == 23:
                    char = '*'
                elif column == 24:
                    char = '='
                elif column == 25:
                    char = '+'
                elif column == 26:
                    char = '*'
                elif column == 27:
                    char = '+'
                elif column == 28:
                    char = '#'
                elif column == 29:
                    char = '*'
                elif column == 30:
                    char = '+'
                elif 31 <= column <= 44:
                    char = '@'
            
            # Row 9: @@@@@@@@@#*#%%****#**+++=-======*@@@@@@@@@@@@
            elif row == 9:
                if 0 <= column <= 8:
                    char = '@'
                elif column == 9:
                    char = '#'
                elif column == 10:
                    char = '*'
                elif column == 11:
                    char = '#'
                elif column == 12:
                    char = '%'
                elif 13 <= column <= 16:
                    char = '*'
                elif column == 17:
                    char = '#'
                elif column == 18:
                    char = '*'
                elif column == 19:
                    char = '*'
                elif 20 <= column <= 22:
                    char = '+'
                elif column == 23:
                    char = '='
                elif column == 24:
                    char = '-'
                elif 25 <= column <= 31:
                    char = '='
                elif column == 32:
                    char = '*'
                elif 33 <= column <= 44:
                    char = '@'
            
            # Row 10: @@@@@@@@%#*#*#**+======**======+*@@@@@@@@%%%%
            elif row == 10:
                if 0 <= column <= 7:
                    char = '@'
                elif column == 8:
                    char = '%'
                elif column == 9:
                    char = '#'
                elif column == 10:
                    char = '*'
                elif column == 11:
                    char = '#'
                elif column == 12:
                    char = '*'
                elif column == 13:
                    char = '#'
                elif 14 <= column <= 15:
                    char = '*'
                elif column == 16:
                    char = '*'
                elif column == 17:
                    char = '+'
                elif 18 <= column <= 23:
                    char = '='
                elif 24 <= column <= 25:
                    char = '*'
                elif column == 26:
                    char = '*'
                elif 27 <= column <= 32:
                    char = '='
                elif column == 33:
                    char = '+'
                elif column == 34:
                    char = '*'
                elif 35 <= column <= 42:
                    char = '@'
                elif 43 <= column <= 44:
                    char = '%'
            
            # Row 11: @@@@@@@%%*%%*##*****+++*%@%##+++#%@@@@%%%%%%%
            elif row == 11:
                if 0 <= column <= 6:
                    char = '@'
                elif 7 <= column <= 8:
                    char = '%'
                elif column == 9:
                    char = '*'
                elif column == 10:
                    char = '%'
                elif column == 11:
                    char = '%'
                elif column == 12:
                    char = '*'
                elif column == 13:
                    char = '#'
                elif column == 14:
                    char = '#'
                elif 15 <= column <= 19:
                    char = '*'
                elif 20 <= column <= 22:
                    char = '+'
                elif column == 23:
                    char = '*'
                elif column == 24:
                    char = '%'
                elif column == 25:
                    char = '@'
                elif column == 26:
                    char = '%'
                elif column == 27:
                    char = '#'
                elif column == 28:
                    char = '#'
                elif 29 <= column <= 31:
                    char = '+'
                elif column == 32:
                    char = '#'
                elif column == 33:
                    char = '%'
                elif 34 <= column <= 37:
                    char = '@'
                elif 38 <= column <= 44:
                    char = '%'
            
            # Row 12: %%%%%%%%%%***#%##*****+==+****+*#%%%%%%%%%%%%
            elif row == 12:
                if 0 <= column <= 9:
                    char = '%'
                elif 10 <= column <= 12:
                    char = '*'
                elif column == 13:
                    char = '#'
                elif column == 14:
                    char = '%'
                elif column == 15:
                    char = '#'
                elif column == 16:
                    char = '#'
                elif 17 <= column <= 21:
                    char = '*'
                elif column == 22:
                    char = '+'
                elif column == 23:
                    char = '='
                elif column == 24:
                    char = '='
                elif column == 25:
                    char = '+'
                elif 26 <= column <= 29:
                    char = '*'
                elif column == 30:
                    char = '+'
                elif column == 31:
                    char = '*'
                elif column == 32:
                    char = '#'
                elif 33 <= column <= 44:
                    char = '%'
            
            # Row 13: %%%%%%%%%%%##%#%####***####%%#%#%%%%%%%%%%%%%
            elif row == 13:
                if 0 <= column <= 10:
                    char = '%'
                elif 11 <= column <= 12:
                    char = '#'
                elif column == 13:
                    char = '%'
                elif column == 14:
                    char = '#'
                elif column == 15:
                    char = '%'
                elif 16 <= column <= 19:
                    char = '#'
                elif 20 <= column <= 22:
                    char = '*'
                elif 23 <= column <= 26:
                    char = '#'
                elif 27 <= column <= 30:
                    char = '%'
                elif column == 31:
                    char = '#'
                elif column == 32:
                    char = '%'
                elif column == 33:
                    char = '#'
                elif 34 <= column <= 44:
                    char = '%'
            
            # Row 14: %%@@@%@@@%%%%#%%######@@%#***#%#%%%%%%%%%%%%%
            elif row == 14:
                if 0 <= column <= 1:
                    char = '%'
                elif 2 <= column <= 4:
                    char = '@'
                elif column == 5:
                    char = '%'
                elif 6 <= column <= 8:
                    char = '@'
                elif 9 <= column <= 13:
                    char = '%'
                elif column == 14:
                    char = '#'
                elif column == 15:
                    char = '%'
                elif 16 <= column <= 21:
                    char = '#'
                elif 22 <= column <= 23:
                    char = '@'
                elif column == 24:
                    char = '@'
                elif column == 25:
                    char = '%'
                elif column == 26:
                    char = '#'
                elif 27 <= column <= 29:
                    char = '*'
                elif column == 30:
                    char = '#'
                elif column == 31:
                    char = '%'
                elif column == 32:
                    char = '#'
                elif 33 <= column <= 44:
                    char = '%'
            
            # Row 15: %%@@@@@@@%%%@%#%%%###%@@%%%@%%@@%%%%%%%%%%%%%
            elif row == 15:
                if 0 <= column <= 1:
                    char = '%'
                elif 2 <= column <= 8:
                    char = '@'
                elif 9 <= column <= 11:
                    char = '%'
                elif column == 12:
                    char = '@'
                elif column == 13:
                    char = '%'
                elif column == 14:
                    char = '#'
                elif 15 <= column <= 17:
                    char = '%'
                elif 18 <= column <= 20:
                    char = '#'
                elif 21 <= column <= 22:
                    char = '%'
                elif column == 23:
                    char = '@'
                elif column == 24:
                    char = '@'
                elif 25 <= column <= 27:
                    char = '%'
                elif 28 <= column <= 29:
                    char = '@'
                elif column == 30:
                    char = '%'
                elif column == 31:
                    char = '%'
                elif 32 <= column <= 33:
                    char = '@'
                elif column == 34:
                    char = '@'
                elif 35 <= column <= 44:
                    char = '%'
            
            # Row 16: %%%%%%@%%%%@@@**#%@@@%%%@@@%%%@@@%%%%%%%%%%%%%
            elif row == 16:
                if 0 <= column <= 5:
                    char = '%'
                elif column == 6:
                    char = '@'
                elif 7 <= column <= 10:
                    char = '%'
                elif 11 <= column <= 13:
                    char = '@'
                elif 14 <= column <= 15:
                    char = '*'
                elif column == 16:
                    char = '#'
                elif column == 17:
                    char = '%'
                elif 18 <= column <= 20:
                    char = '@'
                elif 21 <= column <= 23:
                    char = '%'
                elif 24 <= column <= 26:
                    char = '@'
                elif column == 27:
                    char = '%'
                elif column == 28:
                    char = '%'
                elif column == 29:
                    char = '%'
                elif 30 <= column <= 32:
                    char = '@'
                elif column == 33:
                    char = '%'
                elif 34 <= column <= 36:
                    char = '@'
                elif column == 37:
                    char = '%'
                elif 38 <= column <= 44:
                    char = '%'
            
            # Row 17: %%%%%%%%%%%#=**##%%%%%@@@@@@@@@**%%%%%%%%%%%%
            elif row == 17:
                if 0 <= column <= 10:
                    char = '%'
                elif column == 11:
                    char = '#'
                elif column == 12:
                    char = '='
                elif column == 13:
                    char = '*'
                elif column == 14:
                    char = '*'
                elif 15 <= column <= 16:
                    char = '#'
                elif column == 17:
                    char = '#'
                elif 18 <= column <= 22:
                    char = '%'
                elif 23 <= column <= 31:
                    char = '@'
                elif 32 <= column <= 33:
                    char = '*'
                elif column == 34:
                    char = '*'
                elif 35 <= column <= 44:
                    char = '%'
            
            # Row 18: %%%%%%%%-::-+***##%%#%@@@@@%##*---::-=*%%%%%%
            elif row == 18:
                if 0 <= column <= 7:
                    char = '%'
                elif column == 8:
                    char = '-'
                elif column == 9:
                    char = ':'
                elif column == 10:
                    char = ':'
                elif column == 11:
                    char = '-'
                elif column == 12:
                    char = '+'
                elif 13 <= column <= 15:
                    char = '*'
                elif 16 <= column <= 17:
                    char = '#'
                elif column == 18:
                    char = '#'
                elif column == 19:
                    char = '%'
                elif column == 20:
                    char = '%'
                elif column == 21:
                    char = '#'
                elif column == 22:
                    char = '%'
                elif 23 <= column <= 27:
                    char = '@'
                elif column == 28:
                    char = '%'
                elif column == 29:
                    char = '#'
                elif column == 30:
                    char = '#'
                elif column == 31:
                    char = '*'
                elif 32 <= column <= 34:
                    char = '-'
                elif column == 35:
                    char = '-'
                elif column == 36:
                    char = '-'
                elif column == 37:
                    char = ':'
                elif column == 38:
                    char = ':'
                elif column == 39:
                    char = '-'
                elif column == 40:
                    char = '='
                elif column == 41:
                    char = '*'
                elif 42 <= column <= 44:
                    char = '%'
            
            # Row 19: %%%%+::::-====+####%%%%#####***------:::::-+#
            elif row == 19:
                if 0 <= column <= 3:
                    char = '%'
                elif column == 4:
                    char = '+'
                elif 5 <= column <= 8:
                    char = ':'
                elif column == 9:
                    char = '-'
                elif 10 <= column <= 13:
                    char = '='
                elif column == 14:
                    char = '+'
                elif 15 <= column <= 18:
                    char = '#'
                elif 19 <= column <= 22:
                    char = '%'
                elif 23 <= column <= 27:
                    char = '#'
                elif 28 <= column <= 30:
                    char = '*'
                elif 31 <= column <= 36:
                    char = '-'
                elif 37 <= column <= 41:
                    char = ':'
                elif column == 42:
                    char = '-'
                elif column == 43:
                    char = '+'
                elif column == 44:
                    char = '#'
            
            # Row 20: #::::-----=-===+*##%%%%%%####*=---------:----
            elif row == 20:
                if column == 0:
                    char = '#'
                elif 1 <= column <= 4:
                    char = ':'
                elif 5 <= column <= 9:
                    char = '-'
                elif column == 10:
                    char = '='
                elif column == 11:
                    char = '-'
                elif 12 <= column <= 14:
                    char = '='
                elif column == 15:
                    char = '+'
                elif column == 16:
                    char = '*'
                elif column == 17:
                    char = '#'
                elif column == 18:
                    char = '#'
                elif 19 <= column <= 24:
                    char = '%'
                elif 25 <= column <= 28:
                    char = '#'
                elif column == 29:
                    char = '*'
                elif column == 30:
                    char = '='
                elif 31 <= column <= 39:
                    char = '-'
                elif column == 40:
                    char = ':'
                elif 41 <= column <= 44:
                    char = '-'
            
            # Row 21: ::::---:------===++**#%%#***+==------------:-
            elif row == 21:
                if 0 <= column <= 3:
                    char = ':'
                elif column == 4:
                    char = '-'
                elif column == 5:
                    char = '-'
                elif column == 6:
                    char = '-'
                elif column == 7:
                    char = ':'
                elif 8 <= column <= 13:
                    char = '-'
                elif 14 <= column <= 16:
                    char = '='
                elif 17 <= column <= 18:
                    char = '+'
                elif column == 19:
                    char = '+'
                elif 20 <= column <= 21:
                    char = '*'
                elif column == 22:
                    char = '*'
                elif column == 23:
                    char = '#'
                elif column == 24:
                    char = '%'
                elif column == 25:
                    char = '#'
                elif 26 <= column <= 28:
                    char = '*'
                elif column == 29:
                    char = '+'
                elif column == 30:
                    char = '='
                elif column == 31:
                    char = '='
                elif 32 <= column <= 43:
                    char = '-'
                elif column == 44:
                    char = ':'
            
            # Row 22: ------------------=+****+++++==-------------:
            elif row == 22:
                if 0 <= column <= 17:
                    char = '-'
                elif column == 18:
                    char = '='
                elif column == 19:
                    char = '+'
                elif 20 <= column <= 23:
                    char = '*'
                elif 24 <= column <= 28:
                    char = '+'
                elif column == 29:
                    char = '='
                elif column == 30:
                    char = '='
                elif 31 <= column <= 43:
                    char = '-'
                elif column == 44:
                    char = ':'
            
            # Row 23: --------------=-===============------:--:::--
            elif row == 23:
                if 0 <= column <= 13:
                    char = '-'
                elif column == 14:
                    char = '='
                elif column == 15:
                    char = '-'
                elif 16 <= column <= 28:
                    char = '='
                elif 29 <= column <= 34:
                    char = '-'
                elif column == 35:
                    char = ':'
                elif column == 36:
                    char = '-'
                elif column == 37:
                    char = '-'
                elif column == 38:
                    char = ':'
                elif column == 39:
                    char = ':'
                elif column == 40:
                    char = ':'
                elif 41 <= column <= 44:
                    char = '-'
            
            print(char, end='')
        print()

# Call the function to display the ASCII art
generate_ascii_art()
