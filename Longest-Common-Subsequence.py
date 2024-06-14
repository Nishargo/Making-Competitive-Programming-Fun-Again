# A longest common subsequence (LCS) is the longest subsequence that is common in all given input sequences. 
# In a given set of sequences, the goal is to find a common subsequence of all the sequences of maximal length.
# Or in easier words, the goal is generating all possible subsequences and finding the longest among them that is present in both strings.
# Example: "ace" is a subsequence of "abcdef".
# We will use recursion to solve the problem.
# At first, we will create a recursive function.
# Then we will decide on the conditions based on the first characters of the strings.
# Depending on the conditions, we will run the next recursive function.

# X: First sequence (string), Y: Second sequence (string), m: Length of the first sequence X, n: Length of the second sequence Y
def lcs(X, Y, m, n):
 # Base case
    if m == 0 or n == 0:
        return 0
      # Recursive case
      # X[m-1] == Y[n-1]: This condition checks if the last characters of the current substrings X and Y are the same. 
      # The indices m-1 and n-1 are used because string indices in Python are zero-based.

    elif X[m-1] == Y[n-1]:
        return 1 + lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))


if __name__ == '__main__':
    S1 = "AGGTABK"
    S2 = "GXTXAYBL"
    print("Length of LCS is", lcs(S1, S2, len(S1), len(S2)))
