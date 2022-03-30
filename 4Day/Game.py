
selection = input("select cell to replace: (1-3+1-3)")

row1 = ["😃","😉","🥵"]
row2 = ["😷","🤧","😣"]
row3 = ["😑","🤠","😠"]

map = [row1, row2, row3]


vertical = int(selection[0])
horizonal = int(selection[1])
map[horizonal - 1][vertical - 1] = 'x'

# print(map)
print(f"{row1}\n{row2}\n{row3}\n")