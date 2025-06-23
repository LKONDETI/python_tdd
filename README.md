# Code Katas with Python Unittest

## Introduction

Coding katas are short, repeatable programming challenges which are meant to exercise everything from your focus, to your workflow. This repository contains solutions to various LeetCode problems implemented in Python with comprehensive unit tests.

### Prerequisites

To run this project, you must have Python 3.6 or higher installed.

Begin by cloning this repository to your machine, and installing all dependencies:

```bash
git clone <repository-url>
cd python_tdd
pip install -r requirements.txt
```

## Testing

Run all tests in the project root:

```bash
python -m unittest discover tests -p '*_test.py'
```

Run a specific test file:

```bash
python -m unittest tests.specific_test_file
```

## Table of Contents

- [Array](#array)
- [String](#string)
- [Tree](#tree)
- [Dynamic Programming](#dynamic-programming)
- [Graph](#graph)
- [Matrix](#matrix)
- [Linked List](#linked-list)
- [Binary Problems](#binary-problems)
- [Heap](#heap)
- [Prefix Sum](#prefix-sum)
- [Sliding Window](#sliding-window)
- [Interval](#interval)
- [Miscellaneous](#miscellaneous)

---

## Array

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Two Sum | [Video](https://www.youtube.com/watch?v=UXDSeD9mN-k) | O(n) | O(n) | Hash Set |
| Two Sum II (Input Array Is Sorted) | [Video](https://www.youtube.com/watch?v=Q2Tw6gcVEwc) | O(n) | O(1) | Two Pointer |
| 3 Sum | [Video](https://www.youtube.com/watch?v=jzZsG8n2R9A) | O(n²) | O(1) / O(n) | Two Pointer |
| Best Time to Buy and Sell Stock | [Video](https://www.youtube.com/watch?v=1pkOgXD63yU) | - | - | - |
| Contains Duplicate | [Video](https://www.youtube.com/watch?v=3OamzN90kPg) | O(n) | O(n) | - |
| Contains Duplicate II | [Video](https://www.youtube.com/watch?v=ypn0aZ0nrL4) | O(n) | O(n) | Sliding Window |
| Product of Array Except Self | [Video](https://www.youtube.com/watch?v=bNvIQI2wAjk) | O(n) | O(1) | Prefix Product |
| Maximum Subarray | [Video](https://www.youtube.com/watch?v=5WZl3MMT0Eg) | - | - | - |
| Maximum Product Subarray | [Video](https://www.youtube.com/watch?v=lXVy6YWFcRM) | O(n) | O(1) | Dynamic Programming |
| Find Minimum in Rotated Sorted Array | [Video](https://www.youtube.com/watch?v=nIVW4P8b1VA) | - | - | - |
| Search in Rotated Sorted Array | [Video](https://www.youtube.com/watch?v=U8XENwh8Oy8) | - | - | - |
| Increasing Triplet Subsequence | [Video](https://www.youtube.com/watch?v=41gyzVIx-ds) | O(n) | O(1) | Array |
| Can Place Flowers | [Video](https://www.youtube.com/watch?v=ZGxqqjljpUI&t=130s) | O(n) | O(1) | Array |
| Kids With the Greatest Number of Candies | [Video](https://www.youtube.com/watch?v=9K_Am2sQwv0) | O(n) | O(n) | Array |
| Remove Duplicates from Sorted Array | [Video](https://www.youtube.com/watch?v=DEJAZBq0FDA) | O(n) | O(1) | Two Pointer |
| Remove Duplicates from Sorted Array II | [Video](https://www.youtube.com/watch?v=Jg4zXJAH_Kg) | O(n) | O(1) | Two Pointer |
| Majority Element | [Video](https://www.youtube.com/watch?v=7pnhv842keE) | O(n) | O(1) | Two Pointer |
| Rotate Array | [Video](https://www.youtube.com/watch?v=BHr381Guz3Y&ab_channel=NeetCode) | O(n) | O(n) | Two Pointer |
| Container With Most Water | [Video](https://www.youtube.com/watch?v=UuiTKBwPgAo) | O(n) | O(1) | Two Pointer |
| Remove Element | [Video](https://www.youtube.com/watch?v=R9zj3m2hZAI) | O(n) | O(1) | Two Pointer |
| Find Pivot Index | [Video](https://www.youtube.com/watch?v=u89i60lYx8U) | O(n) | O(1) | Prefix Sum |
| Merge Sorted Array | [Video](https://www.youtube.com/watch?v=P1Ic85RarKY) | O(m+n) | O(1) | Two Pointer |
| Single Number | [Video](https://www.youtube.com/watch?v=qMPX1AOa83k) | O(n) | O(1) | Bit Manipulation |
| Move Zeroes | [Video](https://www.youtube.com/watch?v=aayNRwUN3Do) | O(n) | O(1) | Two Pointer |
| Longest Subarray of 1's After Deleting One Element | [Video](https://www.youtube.com/watch?v=R1URUB6_y2k) | O(n) | O(1) | Sliding Window |
| Find the Highest Altitude | [Video](https://www.youtube.com/watch?v=2p-ySDvyzLg) | O(n) | O(1) | Prefix Sum |
| Maximum Number of K-Sum Pairs | [Video](https://www.youtube.com/watch?v=FzvK5uuaki8) | O(n) | O(n) | Hash Map |
| Find the Difference of Two Arrays | [Video](https://www.youtube.com/watch?v=oypp_RzI69w) | O(n + m) | O(n + m) | Hash Set |

## String

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Longest Substring Without Repeating Characters | [Video](https://www.youtube.com/watch?v=FCbOzdHKW18&ab_channel=GregHogg) | O(n) | O(n) | Sliding Window |
| Isomorphic Strings | [Video](https://www.youtube.com/watch?v=7yF-U1hLEqQ&ab_channel=NeetCode) | O(n) | O(k) | Hash map |
| Minimum Window Substring | [Video](https://www.youtube.com/watch?v=jSto0O4AJbM&ab_channel=NeetCode) | O(n) | O(n) | Sliding Window |
| Valid Anagram | [Video](https://www.youtube.com/watch?v=9UtInBqnCgA) | O(s + t) | O(s + t) | Hash Map |
| Valid Parentheses | [Video](https://www.youtube.com/watch?v=WTzjTskDFMg&ab_channel=NeetCode) | O(n) | O(n) | Stack |
| Valid Palindrome | [Video](https://www.youtube.com/watch?v=jJXJ16kPFWg) | O(n) | O(1) | Two-pointer |
| Longest Common Prefix | [Video](https://www.youtube.com/watch?v=0sWShKIJoo4) | O(n) | O(n) | Vertical scanning |
| First Unique Character in a String | [Video](https://www.youtube.com/watch?v=rBENYgWy3xU) | O(n) | O(1) | Hash Map |
| Find the Index of the First Occurrence in a String | [Video](https://www.youtube.com/watch?v=RApd40quMtA) | O(n) | O(1) | Two-pointer |
| String Compression | [Video](https://www.youtube.com/watch?v=V3welyTMqVM) | O(n) | O(1) | Two Pointer |
| Removing Stars from a String | [Video](https://www.youtube.com/watch?v=6i_WeknfdVg) | O(n) | O(n) | Stack |
| Determine if Two Strings Are Close | [Video](https://www.youtube.com/watch?v=4yGzF8hGJtI) | O(n) | O(1) | Hash Map |
| Reverse Words in a String | [Video](https://www.youtube.com/watch?v=sYcOK51hl-A) | O(n) | O(n) | String Manipulation |
| Merge Strings Alternatively | [Video](https://www.youtube.com/watch?v=4n1l1k1oW6g) | O(n) | O(n) | Two Pointer |
| Is Subsequence | [Video](https://www.youtube.com/watch?v=PwDqpOMwg6U) | O(n) | O(1) | Two Pointer |
| Greatest Common Divisor of Strings | [Video](https://www.youtube.com/watch?v=Jt3xhLzq0iQ) | O(n + m) | O(1) | Math |
| Reverse Vowels of a String | [Video](https://www.youtube.com/watch?v=9xT1J9G7qRA) | O(n) | O(1) | Two Pointer |
| Decode String | [Video](https://www.youtube.com/watch?v=qB0zZpBJlh8) | O(n) | O(n) | Stack |
| Word Pattern | [Video](https://www.youtube.com/watch?v=W_akoecmCbM&ab_channel=NeetCode) | O(n) | O(m) where m is the length of the words | Hash map |
| Ransom Note | [Video](https://www.youtube.com/watch?v=i3bvxJyUB40&ab_channel=GregHogg) | O(n+m) | O(k) | Hash map |

## Tree

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Binary Tree Maximum Path Sum | [Video](https://www.youtube.com/watch?v=Hr5cWUld4vU&ab_channel=NeetCode) | O(n) | O(n) or O(log n) | DFS |
| Kth Smallest Element in a BST | [Video](https://www.youtube.com/watch?v=PwjF3RO9djY&ab_channel=GregHogg) | O(n) | O(n) | In-order traversal |
| Path Sum II | [Video](https://www.youtube.com/watch?v=Z2Q6UsVIyxY) | O(n) | O(n) | DFS |
| Binary Tree Level Order Traversal | [Video](https://www.youtube.com/watch?v=6ZnyEApgFYg) | O(n) | O(n) | BFS |
| Binary Tree Paths | [Video](https://www.youtube.com/watch?v=MzQzY0iP3GU&ab_channel=ShaheerShukur) | O(n) | O(h) | DFS |
| Symmetric Tree | [Video](https://www.youtube.com/watch?v=nKggNAiEpBE) | O(n) | O(h) | DFS |
| Leaf-Similar Trees | [Video](https://www.youtube.com/watch?v=3jvWodd7ht0) | O(n) | O(h) | DFS |
| Maximum Depth of Binary Tree | [Video](https://www.youtube.com/watch?v=hTM3phVI6YQ) | O(n) | O(h) | BFS/DFS |
| Search in a Binary Search Tree | [Video](https://www.youtube.com/watch?v=KcNt6v_56cc) | O(h) | O(h) | Recursion |

## Dynamic Programming

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Climbing Stairs | [Video](https://www.youtube.com/watch?v=Y0lT9Fck7qI&t=6s&ab_channel=NeetCode) | O(n) | O(n) | Bottom-up |
| Coin Change | [Video](https://www.youtube.com/watch?v=koE9ly1CFDc&t=37s&ab_channel=GregHogg) | O(N*M) | O(A) | Bottom-up |
| Longest Increasing Subsequence | [Video](https://www.youtube.com/watch?v=cjWnW0hdF1Y) | O(n²) | O(n) | Bottom-up |
| Longest Common Subsequence | [Video](https://www.youtube.com/watch?v=Ua0GhsJSlWM) | O(m*n) | O(m*n) | Bottom-up |
| Word Break Problem | [Video](https://www.youtube.com/watch?v=Sx9NNgInc3A) | O(n² * m) | O(n) | Bottom-up |
| Combination Sum | [Video](https://www.youtube.com/watch?v=dw2nMCxG0ik) | O(N*M) | O(M) | Backtracking |
| House Robber | [Video](https://www.youtube.com/watch?v=kIII1uT6F8Y) | O(n) | O(1) | Bottom-up |
| House Robber II | [Video](https://www.youtube.com/watch?v=rWAJCfYYOvM&t=6s) | O(n) | O(1) | Bottom-up |
| Decode Ways | [Video](https://www.youtube.com/watch?v=6aEyTjOwlJU) | O(n) | O(1) | Bottom-up |
| Unique Paths | [Video](https://www.youtube.com/watch?v=IlEsdxuD4lY) | O(n) | O(1) | Bottom-up |
| Partition Equal Subset Sum | [Video](https://www.youtube.com/watch?v=ZFuagJEpeEU) | O(n * target) | O(n * target) | Bottom-up |
| Jump Game | [Video](https://www.youtube.com/watch?v=Yan0cv2cLy8) | O(n) | O(1) | Greedy |
| Subsets | [Video](http://youtube.com/watch?v=REOH22Xwdkk) | O(n·2ⁿ) | O(n·2ⁿ) | Backtracking |
| Permutations | [Video](http://youtube.com/watch?v=s7AvT7cGdSo) | O(n!) | O(n!) | Backtracking |
| Nth Tribonacci Number | [Video](https://www.youtube.com/watch?v=UZRkpGk943Q) | O(n) | O(1) | Bottom-up |

## Graph

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Clone Graph | [Video](https://www.youtube.com/watch?v=mQeF6bN8hMk&ab_channel=NeetCode) | O(V + E) | O(V + E) | DFS |
| Number of Islands | [Video](https://www.youtube.com/watch?v=pV2kpPD66nE) | O(m * n) | O(m * n) | BFS |
| Course Schedule | [Video](https://www.youtube.com/watch?v=EgI5nU9etnU) | O(numCourses + prerequisites) | O(numCourses + prerequisites) | DFS |
| Course Schedule II | [Video](https://www.youtube.com/watch?v=Akt3glAwyfY) | O(prereq + numCourses) | O(prereq + numCourses) | Topological Sort |

## Matrix

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Rotting Oranges | [Video](https://www.youtube.com/watch?v=y704fEOx0s0) | O(n * m) | O(n * m) | BFS |
| Surrounded Regions | [Video](https://www.youtube.com/watch?v=9z2BunfoZ5Y) | O(n·m) | O(n·m) | DFS |
| Flood Fill | [Video](https://www.youtube.com/watch?v=hEZ8uGqaC2c) | O(n*m) | O(n*m) | DFS |
| Equal Row and Column Pairs | [Video](https://www.youtube.com/watch?v=R2vRz1Y6i8o) | O(n^2) | O(n^2) | Hash Map |

## Linked List

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Reverse a Linked List | [Video](https://www.youtube.com/watch?v=KRxeMng7fBU) | O(n) | O(1) | Iterative |
| Reverse Linked List II | [Video](https://www.youtube.com/watch?v=Qk0zUZW-U_M) | O(n) | O(1) | Iterative |
| Detect Cycle in a Linked List | [Video](https://www.youtube.com/watch?v=gBTe7lFR3vc&ab_channel=NeetCode) | O(n) | O(1) | Fast and Slow pointers |
| Delete the Middle Node of a Linked List | [Video](https://www.youtube.com/watch?v=WT0O4TTjyNc) | O(n) | O(1) | Fast and Slow algorithm |
| Even Odd Linked List | [Video](https://www.youtube.com/watch?v=k52H4XP5_pk) | O(n) | O(1) | Iterative |

## Binary Problems

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Sum of Two Integers | [Video](https://www.youtube.com/watch?v=_pUidg9gQyA) | O(1) | O(1) | Bit Manipulation |
| Number of 1 Bits | [Video](https://www.youtube.com/watch?v=5Km3utixwZs) | O(1) | O(1) | Bit Manipulation |
| Counting Bits | [Video](https://www.youtube.com/watch?v=RyBM56RIWrM) | O(n log n) | O(n) | Bit Manipulation |
| Missing Number | [Video](https://www.youtube.com/watch?v=WnPLSRLSANE&ab_channel=NeetCode) | O(n) | O(1) | Bit Manipulation |
| Reverse Bits | [Video](https://www.youtube.com/watch?v=UcoN6UjAI64&ab_channel=NeetCode) | O(1) | O(1) | Bit Manipulation |

## Heap

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Kth Largest Element in an Array | [Video](https://www.youtube.com/watch?v=XEmy13g1Qxc&ab_channel=NeetCode) | O(n) | O(1) | Quick Select |

## Prefix Sum

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Range Sum Query - Immutable | [Video](https://www.youtube.com/watch?v=2pndAmo_sMA&ab_channel=NeetCodeIO) | O(1) | O(n) | Prefix Sum |
| Contiguous Array | [Video](https://www.youtube.com/watch?v=agB1LyObUNE&ab_channel=NeetCodeIO) | O(n) | O(n) | Prefix Sum |
| Subarray Sum Equals K | [Video](https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode) | O(n) | O(n) | Prefix Sum |

## Sliding Window

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Maximum Average Subarray I | [Video](https://www.youtube.com/watch?v=UdUUnoiLkPg&ab_channel=GregHogg) | O(n) | O(1) | Sliding Window |
| Maximum Number of Vowels in a Substring of Given Length | [Video](https://www.youtube.com/watch?v=kEfPSzgL-Ss) | O(n) | O(1) | Sliding Window |

## Interval

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Merge Intervals | [Video](https://www.youtube.com/watch?v=44H3cEC2fFM&ab_channel=NeetCode) | O(n log n) | O(n) | Sorting |

## Miscellaneous

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| Happy Number | [Video](https://www.youtube.com/watch?v=ljz85bxOYJ0&ab_channel=NeetCode) | O(n) | O(n) | Hash Set |
| Next Greater Element I | [Video](https://www.youtube.com/watch?v=68a1Dc_qVq4&ab_channel=NeetCode) | O(n + m) | O(n) | Monotonic Stack |
| Palindrome Number | [Video](https://www.youtube.com/watch?v=yubRKwixN-U) | O(log n) | O(1) | Arithmetic |
| Roman to Integer | [Video](https://www.youtube.com/watch?v=3jdxYj3DD98) | O(n) | O(1) | Arithmetic |
| Search Insert Position | - | O(log n) | O(1) | Binary Search |
| Guess Number Higher or Lower | [Video](https://www.youtube.com/watch?v=6rrgCVjLwUg) | O(log n) | O(1) | Binary Search |
| Asteroid Collision | [Video](https://www.youtube.com/watch?v=4No53MxxruE) | O(n) | O(n) | Stack |
| Number of Recent Calls | [Video](https://www.youtube.com/watch?v=4KcZOGPjJ9Q) | O(1) (amortized) | O(n) | Queue |
| Fizz Buzz | [Video](https://www.youtube.com/watch?v=QPZ0pIK_wsc) | O(n) | O(1) | Simulation |

---

