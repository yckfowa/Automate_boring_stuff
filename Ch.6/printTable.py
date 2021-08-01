table_data = [['apples', 'oranges', 'cherries', 'bananas'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

# http://pythontutor.com/visualize.html#mode=display - visualizing the steps of how the code works


def print_table(table):
    # initialize list fill with 0 to later determine the width
    col_widths = [0] * len(table)

    # compare each words in the table to find the max_length then store in the col_widths
        for x in table[y]:
            col_widths[y] = max(col_widths[y], len(x))
    # print out the element and rjust wit the col_widths
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(col_widths[y]), end=' ')
        print()
        x += 1


print_table(table_data)
