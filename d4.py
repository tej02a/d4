def print_solution(board, N):
  for i in range(N):
    for j in range(N):
      if board[i][j]:
        print("Q", end=" ")
      else:
        print("_", end=" ")
    print()
  print("\n\n")

def is_safe(board, row, col, N):
  for i in range(col):
    if board[row][i]:
      return False

  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j]:
      return False

  for i, j in zip(range(row, N, 1), range(col, -1, -1)):
    if board[i][j]:
      return False

  return True

def solve_n_queen(board, col, N):
  if col >= N:
    print_solution(board, N)
    return

  for i in range(N):
    if is_safe(board, i, col, N):
      board[i][col] = 1
      solve_n_queen(board, col + 1, N)
      board[i][col] = 0

def main():
  n = int(input("Enter the size of the board: "))
  board = [[0 for _ in range(n)] for _ in range(n)]
  solve_n_queen(board, 0, n)

if __name__ == "__main__":
  main()
