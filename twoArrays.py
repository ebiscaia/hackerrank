# Eduardo Biscaia de Queiroz
# 04/05/2023
#
# Complete the 'twoArrays' function below.
# The function is expected to return a STRING.
# The function accepts the following parameters:
# 1. Integer k
# 2. INTEGER_ARRAY A
# 3. INTEGER_ARRAY B
#


def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    i = 0
    while i < len(A):
        if A[i] + B[i] < k:
            return "NO"
        i += 1
    return "YES"


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'],'w')
    # q = int(input().strip())

    # for q_itr in range(q):
    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])

    # k = int(first_multiple_input[1])

    # A = list(map(int,input().rstrip().split()))

    # B = list(map(int,input().rstrip().split()))
    k = 5
    A = [1, 2, 2, 1]
    B = [3, 3, 3, 4]
    result = twoArrays(k, A, B)
    print(result)

    # fptr.write(result+"\n")

    # fptr.close()
