# Puzzle Solved by :AnietieLEssien
    #Date:17-Jan-2023
    #created for: challenge mentioned in the        comment.'''

#Puzzle solved by AnietieLEssien

# Get whole number(s) from input, or use
# 1 to 10
for N in [int(n)
          for n in input().split()
          if n.isdecimal()] or range(1,11):

  # Generare powers of 2: 2^1, 2^2, ..., 2^N
  powers = tuple(2**i for i in range(1,N+1))

  # For modulus values 1, 3, 5, ...
  for M in range(1,N*2,2):
    # Get remainders for the powers of 2
    rems = tuple(map(lambda i: i%M, powers))

    # If all remainder values are unique...
    if len(set(rems)) == N:
      # Output the result
      print(f'For {N=} the smallest M is '
            f'{M}.\n{N} remainders:',
            sorted(rems),'',
            sep='\n')
      # And stop looking for M
      break
    



# Oma Falk's description...
'''
For a given N find the smallest M so that all N powers of 2 (i.e., p equal to 2, 4, 8, 16) have different results for p mod M

Example for N = 4

p     p%3    p%4    p%5
--    ---    ---    ---
2      2      2      2
4      1      0      4
8      2      0      3
16     1      0      1

M is 5 because in the last col all results are different


Note: For N = 8 M is 11

'''
