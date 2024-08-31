n = int(input('Enter a value for the number of rows in the grid'))
m = int(input('Enter a value for the number of colums in the grid'))


numrec = (m * n * (n + 1) * (m + 1)) // 4

numsquare = m * (m + 1) * (3 * n - m + 1) // 6
           
print('The total number of rectangles =', numrec)
print('The total number of only rectangles =', (numrec - numsquare))
