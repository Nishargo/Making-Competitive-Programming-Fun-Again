Competitive Programming is the practice of solving well-defined algorithmic problems under strict time and memory constraints. Unlike normal coding, the goal is not just to “make it work”, but to build the fastest correct reasoning path from problem → solution → code.

This list of definitions focuses on why concepts are used.

1. What is an Algorithm?

An algorithm is a structured sequence of steps used to solve a problem in a finite amount of time. In Competitive Programming, an algorithm is essentially a decision-making strategy like given an input, how do we transform it into the correct output in the most efficient way?

For example, consider searching for a number in a list.

A naive approach checks every element one by one → O(n)
A smarter approach like binary search repeatedly halves the search space → O(log n)

The key idea is not just “searching faster”, but reducing unnecessary work by exploiting structure (like sorted order).

Algorithms are used because brute force solutions often exceed time limits when input size becomes large.

2. Why Data Structures Matter

A data structure is a way of organizing data so that operations like access, update, insertion, and deletion become efficient.

In CP, most problems are not solved by algorithms alone, they are solved by choosing the right data structure to support the algorithm.

Example:

Suppose you want to repeatedly check whether a value exists in a collection.

Using an array → O(n) per query (slow for large inputs)
Using a hash set → O(1) average per query (fast)

Same problem and a different structure results in a completely different performance.

3. Searching

Searching is the process of locating a target value in a dataset.

In Linear Search, one checks each element one by one and it is used when data is unsorted and input size is small. But there is a problem...it becomes too slow for large inputs.

On the other hand, Binary search works only when the data is sorted.
Instead of checking everything, it:

- Looks at the middle element
- Eliminates half of the search space
- Repeats

It works well because sorted order gives a monotonic structure. If a condition fails on one side, it will fail on all similar elements.

This idea is extremely powerful in CP and extends beyond arrays into:

- Answer searching problems
- Optimization problems
- Decision-based problems

4. Loops and Iteration

A loop is used to repeat a process multiple times.

In CP, loops are not just repetition; they are simulation tools.

For example:

- Traversing an array
- Simulating a process step-by-step
- Checking all possibilities

Loops are the foundation of brute force, and many optimized solutions start from a brute force loop and improve it.

5. Functions (Breaking Complexity)

A function is a reusable block of code that performs a specific task.

In Competitive Programming, functions are used to:

- Break large problems into smaller logical parts
- Avoid rewriting logic repeatedly (like DFS, BFS, binary search)
- Improve readability under time pressure

Example intuition:
Instead of rewriting graph traversal logic every time, you define:

dfs(node) → reusable exploration unit

Functions help convert thinking into modular building blocks.

6. Recursion (Thinking in Layers)

Recursion is when a function solves a problem by calling itself on smaller inputs. It is used when a problem can be broken into similar subproblems.

Example:

Factorial:

fact(n) = n * fact(n-1)

Recursion is powerful because it matches how many problems are structured:

- Trees naturally recurse
- Graph traversal uses recursion (DFS)
- Backtracking explores decision trees

7. Backtracking (Exploring All Possibilities)

Backtracking is a method of trying all possibilities and undoing choices when they don’t lead to a solution.

It is used when:

- You need all combinations or permutations
- There is no direct greedy or DP solution

Example intuition:

Imagine solving a maze:

Try a path
If it fails, go back
Try another path

This is backtracking.

It is powerful but expensive, so it is usually optimized with pruning.

8. Greedy Approach (Local Decisions)

A greedy algorithm makes the best possible choice at each step.

It is used when a local optimal choice leads to a global optimal solution.

Example:

Coin change (in some systems):
Always take the largest coin possible.

Greedy works only when there is no need to reconsider past decisions

9. Dynamic Programming (Memory + Optimization)

Dynamic Programming is used when the problem has overlapping subproblems and the same computation repeats multiple times

Instead of recomputing results, DP stores them.

Example:

Fibonacci:
Naive recursion recomputes values many times.

DP stores results:

f(1), f(2), f(3)… computed once

DP is essentially:

“Remember what you already solved”

It transforms exponential solutions into polynomial ones.

10. Graph Thinking (Relationships)

A graph represents connections between entities.

Used when:

Problems involve networks, paths, dependencies, or relationships
Example:
- Cities connected by roads
- Social networks
- Task dependencies
- Traversal methods:
1. BFS → explores layer by layer (shortest path in unweighted graphs)
2. DFS → explores deep paths first

Graphs are not just a data structure, they are a way of modeling reality.

11. Time Complexity (Why Solutions Fail)

Time complexity measures how fast an algorithm grows as input size increases. In CP, it determines whether your solution passes or TLEs.

It matters because a solution that works for 100 inputs may fail for 100,000 inputs.

Example:

O(n²) → fine for small n
O(n log n) → required for large n

CP is often about reducing complexity, not just writing logic.

12. Space Complexity (Memory Pressure)

Space complexity measures how much extra memory your solution uses.

It includes Arrays, maps, recursion stack, DP tables

It matters because even correct solutions can fail if memory limits are exceeded.

13. Debugging (Finding Truth in Logic)

Debugging is the process of finding why a correct idea fails in implementation. In CP, most bugs are not syntax errors, rather logical errors.

Common issues can be off-by-one errors, wrong base case and incorrect assumptions about constraints.
