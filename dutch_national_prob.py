class Node:
    def __init__(self weight: int, value: int, next: 'Node' = None):
        self.weight = weight
        self.value = value
        self.next = next

def solve_dutch_national_problem(head: Node, capacity: int) -> int:
    n = 0
    current = head
    while current is not None:
        n += 1
        current = current.next

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        current = head
        for w in range(capacity + 1):
            if current.weight <= w:
                dp[i][w] = max(dp[i - 1][w], current.value + dp[i - 1][w - current.weight])
            else:
                dp[i][w] = dp[i - 1][w]
            current = current.next

    return dp[n][capacity]