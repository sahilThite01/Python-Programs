row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

selected_position = map[row-1]
selected_position[column-1] = "X"

print(f"\n{row1}\n{row2}\n{row3}")