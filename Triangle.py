print("\nTYPES OF TRIANGLE \n")

for rows in range (0,10):
    for cols in range (0,rows+1):
        print("*", end=" ")
    print("\r")
print("___________________________\n")

# OUTPUT:

# TYPES OF TRIANGLE

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *
# ___________________________

for rows in reversed(range (0,10)):
    for cols in range (0,rows+1):
        print("*", end=" ")
    print("\r")
print("___________________________\n")

# OUTPUT:
# * * * * * * * * * *
# * * * * * * * * *
# * * * * * * * *
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# ___________________________

n=10
k=2*n-2 #No. of spaces
for rows in range (0,n):
    for cols in range (0,k):
        print(end=" ")
    k=k-2
    for cols in range(0,rows+1):
        print("*",end=" ")
    print("\r")
print("___________________________\n")

# OUTPUT:
#                   *
#                 * *
#               * * *
#             * * * *
#           * * * * *
#         * * * * * *
#       * * * * * * *
#     * * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * *
# ___________________________

n=10
k=0 #No. of spaces
for rows in reversed(range (0,n)):
    for cols in range (0,k):
        print(end=" ")
    k=k+2
    for cols in range(0,rows+1):
        print("*",end=" ")
    print("\r")
print("___________________________\n")

# OUTPUT:
# * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * * *
#       * * * * * * *
#         * * * * * *
#           * * * * *
#             * * * *
#               * * *
#                 * *
#                   *
# ___________________________

n=10
k=n-1 #No. of spaces
for rows in range (0,n):
    for cols in range (0,k):
        print(end=" ")
    k=k-1
    for cols in range(0,rows+1):
        print("*",end=" ")
    print("\r")
print("___________________________\n")

# OUTPUT:
#          *
#         * *
#        * * *
#       * * * *
#      * * * * *
#     * * * * * *
#    * * * * * * *
#   * * * * * * * *
#  * * * * * * * * *
# * * * * * * * * * *
# ___________________________

n=10
k=0  #No. of spaces
for rows in reversed(range (0,n)):
    for cols in range (0,k):
        print(end=" ")
    k=k+1
    for cols in range(0,rows+1):
        print("*",end=" ")
    print("\r")
print("___________________________\n")

# OUTPUT:
# * * * * * * * * * *
#  * * * * * * * * *
#   * * * * * * * *
#    * * * * * * *
#     * * * * * *
#      * * * * *
#       * * * *
#        * * *
#         * *
#          *
# ___________________________