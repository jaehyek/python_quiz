
'''

---------------------------------------------------------------------------------------------------------
def fib(i):
    if i<2: return 1
    return fib(i-1)+fib(i-2)
But can reduce the time complexity by save the return value in list:

def fibonacci(n, fib=[0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n+1):
            fib.append(fib[i-1]+fib[i-2])
    return fib[n]
or using DP:

class dpFib(object):
    def __init__(self):
        self.__result = {0: 0, 1: 1}

    def fib(self, x):
        if x in self.__result:
            return self.__result[x]

        r = self.fib(x-1) + self.fib(x-2)
        self.__result[x] = r
        return r

dpfib = dpFib()
print(dpfib.fib(x=8181))


-------------------------------------------------------------------------------------------------------------------

Using BFS, code:

def bfs(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    start = queue.pop(0)
    yield start
    visited.add(start)
    queue += [vertex for vertex in graph[start] - set(queue) - visited]
    yield from bfs(graph, queue, visited=visited)


def bfs_paths(graph, queue, goal):
    if not queue:
        return
    (start, path) = queue.pop(0)
    if start == goal:
        yield path
    queue += [(vertex, path + [vertex]) for vertex in graph[start] - set(path)]
    yield from bfs_paths(graph, queue, goal)


graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E']),
}

print(repr([vertex for vertex in bfs(graph, ['A'])]))
print(repr([path for path in bfs_paths(graph, [('A', ['A'])], 'F')]))
Output:

['A', 'C', 'B', 'F', 'D', 'E']
[['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

-------------------------------------------------------------------------------------------------------------------

[f(n) = \begin{cases} f(5)+f(4)+f(3)+f(2)+f(1)+f(0), & \mbox{if }i\mbox{ = 6} \
f(4)+f(3)+f(2)+f(1)+f(0), & \mbox{if }i\mbox{ = 5} \
f(3)+f(2)+f(1)+f(0), & \mbox{if }i\mbox{ = 4} \
f(2)+f(1)+f(0), & \mbox{if }i\mbox{ = 3} \
f(1)+f(0), & \mbox{if }i\mbox{ = 2} \\ f(0), & \mbox{if }i\mbox{ = 1} \
1, & \mbox{if }i\mbox{ = 0} \
\end{cases}]

/* 
 * Filename :coins.cpp
 * Description: solve coin combinations using dynamic programing
 * Complier: g++
 */
#include <iostream>
#include <string>
#include <cmath>
#include <vector>

using namespace std;

/****************************************************************
 * coin Combinations: using dynamic programming
 *
 * Basic idea:
 * dp[i][j] = sum(dp[i-1][j-k*coins[i-1]]) for k = 1,2,..., j/coins[i-1]
 * dp[0][j] = 1 for j = 0, 1, 2, ..., sum
 * 
 * Input:
 * coins[] - array store all values of the coins
 * coinKinds - how many kinds of coins there are
 * sum - the number you want to construct using coins
 *
 * Output:
 * the number of combinations using coins construct sum
 *
 * Usage:
 * c[3] = {1, 2, 5};
 * int result = coinCombinations(c, 3, 10);
 *
 ****************************************************************/
int coinCombinations(int coins[], int coinKinds, int sum)
{
    // 2-D array using vector: is equal to: dp[coinKinds+1][sum+1] = {0};
    vector<vector<int> > dp(coinKinds + 1);
    for (int i = 0; i <= coinKinds; ++i)
    {
        dp[i].resize(sum + 1);
    }
    for (int i = 0; i <= coinKinds; ++i)
    {
        for (int j = 0; j <= sum; ++j)
        {
            dp[i][j] = 0;
        }
    }

    //init: dp[i][0] = 1; i = 0, 1, 2 ..., coinKinds
    //Notice: dp[0][0] must be 1, althongh it make no sense that
    //using 0 kinds of coins construct 0 has one way. but it the foundation
    //of iteration. without it everything based on it goes wrong
    for (int i = 0; i <= coinKinds; ++i)
    {
        dp[i][0] = 1;
    }

    // iteration: dp[i][j] = sum(dp[i-1][j - k*coins[i-1]])
    // k = 0, 1, 2, ... , j / coins[i-1]
    for (int i = 1; i <= coinKinds; ++i)
    {
        for (int j = 1; j <= sum; ++j)
        {
            dp[i][j] = 0;
            for (int k = 0; k <= j / coins[i-1]; ++k)
            {
                dp[i][j] += dp[i-1][j - k * coins[i-1]];
            }
        }
    }

    return dp[coinKinds][sum];
}
(2) If n=610, how many possible ways are there to arrive exactly at the finishing point?

int main()
{
    int coins[6] = {1, 2, 3, 4, 5, 6};
    int sum = 610;
    int result = coinCombinations(coins, 6, 610);
    cout << "using 6 kinds of coins construct 610, combinations are: " << endl;
    cout << result << endl;
    return 0;
}

answer is 1064412205

'''
from math import factorial
def calculate_combinations(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

totaldist = 7
count = 0



