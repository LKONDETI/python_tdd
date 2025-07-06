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
| [Two Sum](https://leetcode.com/problems/two-sum/) | [Video](https://www.youtube.com/watch?v=UXDSeD9mN-k) | O(n) | O(n) | Hash Set |
| [Two Sum II (Input Array Is Sorted)](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Video](https://www.youtube.com/watch?v=Q2Tw6gcVEwc) | O(n) | O(1) | Two Pointer |
| [3 Sum](https://leetcode.com/problems/3sum/) | [Video](https://www.youtube.com/watch?v=jzZsG8n2R9A) | O(n²) | O(1) / O(n) | Two Pointer |
| [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Video](https://www.youtube.com/watch?v=1pkOgXD63yU) | - | - | - |
| [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Video](https://www.youtube.com/watch?v=3OamzN90kPg) | O(n) | O(n) | - |
| [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/) | [Video](https://www.youtube.com/watch?v=ypn0aZ0nrL4) | O(n) | O(n) | Sliding Window |
| [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | [Video](https://www.youtube.com/watch?v=bNvIQI2wAjk) | O(n) | O(1) | Prefix Product |
| [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [Video](https://www.youtube.com/watch?v=5WZl3MMT0Eg) | - | - | - |
| [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | [Video](https://www.youtube.com/watch?v=lXVy6YWFcRM) | O(n) | O(1) | Dynamic Programming |
| [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | [Video](https://www.youtube.com/watch?v=nIVW4P8b1VA) | - | - | - |
| [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | [Video](https://www.youtube.com/watch?v=U8XENwh8Oy8) | - | - | - |
| [Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/) | [Video](https://www.youtube.com/watch?v=41gyzVIx-ds) | O(n) | O(1) | Array |
| [Can Place Flowers](https://leetcode.com/problems/can-place-flowers/) | [Video](https://www.youtube.com/watch?v=ZGxqqjljpUI&t=130s) | O(n) | O(1) | Array |
| [Kids With the Greatest Number of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | [Video](https://www.youtube.com/watch?v=9K_Am2sQwv0) | O(n) | O(n) | Array |
| [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Video](https://www.youtube.com/watch?v=DEJAZBq0FDA) | O(n) | O(1) | Two Pointer |
| [Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | [Video](https://www.youtube.com/watch?v=Jg4zXJAH_Kg) | O(n) | O(1) | Two Pointer |
| [Majority Element](https://leetcode.com/problems/majority-element/) | [Video](https://www.youtube.com/watch?v=7pnhv842keE) | O(n) | O(1) | Two Pointer |
| [Rotate Array](https://leetcode.com/problems/rotate-array/) | [Video](https://www.youtube.com/watch?v=BHr381Guz3Y&ab_channel=NeetCode) | O(n) | O(n) | Two Pointer |
| [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | [Video](https://www.youtube.com/watch?v=UuiTKBwPgAo) | O(n) | O(1) | Two Pointer |
| [Remove Element](https://leetcode.com/problems/remove-element/) | [Video](https://www.youtube.com/watch?v=R9zj3m2hZAI) | O(n) | O(1) | Two Pointer |
| [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | [Video](https://www.youtube.com/watch?v=u89i60lYx8U) | O(n) | O(1) | Prefix Sum |
| [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | [Video](https://www.youtube.com/watch?v=P1Ic85RarKY) | O(m+n) | O(1) | Two Pointer |
| [Single Number](https://leetcode.com/problems/single-number/) | [Video](https://www.youtube.com/watch?v=qMPX1AOa83k) | O(n) | O(1) | Bit Manipulation |
| [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [Video](https://www.youtube.com/watch?v=aayNRwUN3Do) | O(n) | O(1) | Two Pointer |
| [Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) | [Video](https://www.youtube.com/watch?v=R1URUB6_y2k) | O(n) | O(1) | Sliding Window |
| [Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/) | [Video](https://www.youtube.com/watch?v=2p-ySDvyzLg) | O(n) | O(1) | Prefix Sum |
| [Maximum Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) | [Video](https://www.youtube.com/watch?v=FzvK5uuaki8) | O(n) | O(n) | Hash Map |
| [Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/) | [Video](https://www.youtube.com/watch?v=oypp_RzI69w) | O(n + m) | O(n + m) | Hash Set |
| [Plus One](https://leetcode.com/problems/plus-one/) | [Video](https://www.youtube.com/watch?v=jIaA8boiG1s) | O(n) | O(1) | simulation of manual addition (digit-wise traversal from right to left) |
| [Find First and Last Position in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [Video](https://www.youtube.com/watch?v=4sQL7R5ySUU) | O(log(n)) | O(1) | Binary Search |

## String

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Video](https://www.youtube.com/watch?v=FCbOzdHKW18&ab_channel=GregHogg) | O(n) | O(n) | Sliding Window |
| [Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) | [Video](https://www.youtube.com/watch?v=7yF-U1hLEqQ&ab_channel=NeetCode) | O(n) | O(k) | Hash map |
| [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | [Video](https://www.youtube.com/watch?v=jSto0O4AJbM&ab_channel=NeetCode) | O(n) | O(n) | Sliding Window |
| [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Video](https://www.youtube.com/watch?v=9UtInBqnCgA) | O(s + t) | O(s + t) | Hash Map |
| [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | [Video](https://www.youtube.com/watch?v=WTzjTskDFMg&ab_channel=NeetCode) | O(n) | O(n) | Stack |
| [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Video](https://www.youtube.com/watch?v=jJXJ16kPFWg) | O(n) | O(1) | Two-pointer |
| [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | [Video](https://www.youtube.com/watch?v=0sWShKIJoo4) | O(n) | O(n) | Vertical scanning |
| [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/) | [Video](https://www.youtube.com/watch?v=rBENYgWy3xU) | O(n) | O(1) | Hash Map |
| [Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | [Video](https://www.youtube.com/watch?v=RApd40quMtA) | O(n) | O(1) | Two-pointer |
| [String Compression](https://leetcode.com/problems/string-compression/) | [Video](https://www.youtube.com/watch?v=V3welyTMqVM) | O(n) | O(1) | Two Pointer |
| [Removing Stars from a String](https://leetcode.com/problems/removing-stars-from-a-string/) | [Video](https://www.youtube.com/watch?v=6i_WeknfdVg) | O(n) | O(n) | Stack |
| [Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/) | [Video](https://www.youtube.com/watch?v=4yGzF8hGJtI) | O(n) | O(1) | Hash Map |
| [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/) | [Video](https://www.youtube.com/watch?v=sYcOK51hl-A) | O(n) | O(n) | String Manipulation |
| [Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/) | [Video](https://www.youtube.com/watch?v=4n1l1k1oW6g) | O(n) | O(n) | Two Pointer |
| [Is Subsequence](https://leetcode.com/problems/is-subsequence/) | [Video](https://www.youtube.com/watch?v=PwDqpOMwg6U) | O(n) | O(1) | Two Pointer |
| [Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | [Video](https://www.youtube.com/watch?v=Jt3xhLzq0iQ) | O(n + m) | O(1) | Math |
| [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/) | [Video](https://www.youtube.com/watch?v=9xT1J9G7qRA) | O(n) | O(1) | Two Pointer |
| [Decode String](https://leetcode.com/problems/decode-string/) | [Video](https://www.youtube.com/watch?v=qB0zZpBJlh8) | O(n) | O(n) | Stack |
| [Word Pattern](https://leetcode.com/problems/word-pattern/) | [Video](https://www.youtube.com/watch?v=W_akoecmCbM&ab_channel=NeetCode) | O(n) | O(m) where m is the length of the words | Hash map |
| [Ransom Note](https://leetcode.com/problems/ransom-note/) | [Video](https://www.youtube.com/watch?v=i3bvxJyUB40&ab_channel=GregHogg) | O(n+m) | O(k) | Hash map |
| [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | [Video](https://www.youtube.com/watch?v=vzdNOK2oB2E) | O(m*n) | O(m*n) | Hash map |
| [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) | [Video](https://www.youtube.com/watch?v=XYQecbcd6_c) | O(n**2) | O(1) | Dynamic Programming(Alternative) |

## Tree

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Video](https://www.youtube.com/watch?v=Hr5cWUld4vU&ab_channel=NeetCode) | O(n) | O(n) or O(log n) | DFS |
| [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Video](https://www.youtube.com/watch?v=PwjF3RO9djY&ab_channel=GregHogg) | O(n) | O(n) | In-order traversal |
| [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | [Video](https://www.youtube.com/watch?v=Z2Q6UsVIyxY) | O(n) | O(n) | DFS |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Video](https://www.youtube.com/watch?v=6ZnyEApgFYg) | O(n) | O(n) | BFS |
| [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | [Video](https://www.youtube.com/watch?v=MzQzY0iP3GU&ab_channel=ShaheerShukur) | O(n) | O(h) | DFS |
| [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | [Video](https://www.youtube.com/watch?v=nKggNAiEpBE) | O(n) | O(h) | DFS |
| [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | [Video](https://www.youtube.com/watch?v=3jvWodd7ht0) | O(n) | O(h) | DFS |
| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Video](https://www.youtube.com/watch?v=hTM3phVI6YQ) | O(n) | O(h) | BFS/DFS |
| [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | [Video](https://www.youtube.com/watch?v=KcNt6v_56cc) | O(h) | O(h) | Recursion |
| [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [Video](https://www.youtube.com/watch?v=7cp5imvDzl4) | O(n) | O(h) | DFS |

## Dynamic Programming

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | [Video](https://www.youtube.com/watch?v=Y0lT9Fck7qI&t=6s&ab_channel=NeetCode) | O(n) | O(n) | Bottom-up |
| [Coin Change](https://leetcode.com/problems/coin-change/) | [Video](https://www.youtube.com/watch?v=koE9ly1CFDc&t=37s&ab_channel=GregHogg) | O(N*M) | O(A) | Bottom-up |
| [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | [Video](https://www.youtube.com/watch?v=cjWnW0hdF1Y) | O(n²) | O(n) | Bottom-up |
| [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | [Video](https://www.youtube.com/watch?v=Ua0GhsJSlWM) | O(m*n) | O(m*n) | Bottom-up |
| [Word Break](https://leetcode.com/problems/word-break/) | [Video](https://www.youtube.com/watch?v=Sx9NNgInc3A) | O(n² * m) | O(n) | Bottom-up |
| [Combination Sum](https://leetcode.com/problems/combination-sum/) | [Video](https://www.youtube.com/watch?v=dw2nMCxG0ik) | O(N*M) | O(M) | Backtracking |
| [House Robber](https://leetcode.com/problems/house-robber/) | [Video](https://www.youtube.com/watch?v=kIII1uT6F8Y) | O(n) | O(1) | Bottom-up |
| [House Robber II](https://leetcode.com/problems/house-robber-ii/) | [Video](https://www.youtube.com/watch?v=rWAJCfYYOvM&t=6s) | O(n) | O(1) | Bottom-up |
| [Decode Ways](https://leetcode.com/problems/decode-ways/) | [Video](https://www.youtube.com/watch?v=6aEyTjOwlJU) | O(n) | O(1) | Bottom-up |
| [Unique Paths](https://leetcode.com/problems/unique-paths/) | [Video](https://www.youtube.com/watch?v=IlEsdxuD4lY) | O(n) | O(1) | Bottom-up |
| [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | [Video](https://www.youtube.com/watch?v=ZFuagJEpeEU) | O(n * target) | O(n * target) | Bottom-up |
| [Jump Game](https://leetcode.com/problems/jump-game/) | [Video](https://www.youtube.com/watch?v=Yan0cv2cLy8) | O(n) | O(1) | Greedy |
| [Subsets](https://leetcode.com/problems/subsets/) | [Video](http://youtube.com/watch?v=REOH22Xwdkk) | O(n·2ⁿ) | O(n·2ⁿ) | Backtracking |
| [Permutations](https://leetcode.com/problems/permutations/) | [Video](http://youtube.com/watch?v=s7AvT7cGdSo) | O(n!) | O(n!) | Backtracking |
| [Nth Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/) | [Video](https://www.youtube.com/watch?v=UZRkpGk943Q) | O(n) | O(1) | Bottom-up |
| [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | [Video](https://www.youtube.com/watch?v=ktmzAZWkEZ0) | O(n) | O(n) | Bottom-up |
| [Edit Distance](https://leetcode.com/problems/edit-distance/) | [Video](https://www.youtube.com/watch?v=XYi2-LPrwm4) | O(m * n) | O(m * n) | DP |

## Graph

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Clone Graph](https://leetcode.com/problems/clone-graph/) | [Video](https://www.youtube.com/watch?v=mQeF6bN8hMk&ab_channel=NeetCode) | O(V + E) | O(V + E) | DFS |
| [Number of Islands](https://leetcode.com/problems/number-of-islands/) | [Video](https://www.youtube.com/watch?v=pV2kpPD66nE) | O(m * n) | O(m * n) | BFS |
| [Course Schedule](https://leetcode.com/problems/course-schedule/) | [Video](https://www.youtube.com/watch?v=EgI5nU9etnU) | O(numCourses + prerequisites) | O(numCourses + prerequisites) | DFS |
| [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | [Video](https://www.youtube.com/watch?v=Akt3glAwyfY) | O(prereq + numCourses) | O(prereq + numCourses) | Topological Sort |

## Matrix

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | [Video](https://www.youtube.com/watch?v=y704fEOx0s0) | O(n * m) | O(n * m) | BFS |
| [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) | [Video](https://www.youtube.com/watch?v=9z2BunfoZ5Y) | O(n·m) | O(n·m) | DFS |
| [Flood Fill](https://leetcode.com/problems/flood-fill/) | [Video](https://www.youtube.com/watch?v=hEZ8uGqaC2c) | O(n*m) | O(n*m) | DFS |
| [Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/) | [Video](https://www.youtube.com/watch?v=R2vRz1Y6i8o) | O(n^2) | O(n^2) | Hash Map |

## Linked List

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Reverse a Linked List](https://leetcode.com/problems/reverse-linked-list/) | [Video](https://www.youtube.com/watch?v=KRxeMng7fBU) | O(n) | O(1) | Iterative |
| [Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | [Video](https://www.youtube.com/watch?v=Qk0zUZW-U_M) | O(n) | O(1) | Iterative |
| [Detect Cycle in a Linked List](https://leetcode.com/problems/linked-list-cycle/) | [Video](https://www.youtube.com/watch?v=gBTe7lFR3vc&ab_channel=NeetCode) | O(n) | O(1) | Fast and Slow pointers |
| [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/) | [Video](https://www.youtube.com/watch?v=WT0O4TTjyNc) | O(n) | O(1) | Fast and Slow algorithm |
| [Even Odd Linked List](https://leetcode.com/problems/odd-even-linked-list/) | [Video](https://www.youtube.com/watch?v=k52H4XP5_pk) | O(n) | O(1) | Iterative |
| [Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/) | [Video](https://www.youtube.com/watch?v=doj95MelfSA) | O(n) | O(1) | slow and fast algorithm |

## Binary Problems

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) | [Video](https://www.youtube.com/watch?v=_pUidg9gQyA) | O(1) | O(1) | Bit Manipulation |
| [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | [Video](https://www.youtube.com/watch?v=5Km3utixwZs) | O(1) | O(1) | Bit Manipulation |
| [Counting Bits](https://leetcode.com/problems/counting-bits/) | [Video](https://www.youtube.com/watch?v=RyBM56RIWrM) | O(n log n) | O(n) | Bit Manipulation |
| [Missing Number](https://leetcode.com/problems/missing-number/) | [Video](https://www.youtube.com/watch?v=WnPLSRLSANE&ab_channel=NeetCode) | O(n) | O(1) | Bit Manipulation |
| [Reverse Bits](https://leetcode.com/problems/reverse-bits/) | [Video](https://www.youtube.com/watch?v=UcoN6UjAI64&ab_channel=NeetCode) | O(1) | O(1) | Bit Manipulation |
| [Add Binary](https://leetcode.com/problems/add-binary/description/) | [Video](https://www.youtube.com/watch?v=keuWJ47xG8g## Tree

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | [Video](https://www.youtube.com/watch?v=Hr5cWUld4vU&ab_channel=NeetCode) | O(n) | O(n) or O(log n) | DFS |
| [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | [Video](https://www.youtube.com/watch?v=PwjF3RO9djY&ab_channel=GregHogg) | O(n) | O(n) | In-order traversal |
| [Path Sum II](https://leetcode.com/problems/path-sum-ii/) | [Video](https://www.youtube.com/watch?v=Z2Q6UsVIyxY) | O(n) | O(n) | DFS |
| [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | [Video](https://www.youtube.com/watch?v=6ZnyEApgFYg) | O(n) | O(n) | BFS |
| [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) | [Video](https://www.youtube.com/watch?v=MzQzY0iP3GU&ab_channel=ShaheerShukur) | O(n) | O(h) | DFS |
| [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) | [Video](https://www.youtube.com/watch?v=nKggNAiEpBE) | O(n) | O(h) | DFS |
| [Leaf-Similar Trees](https://leetcode.com/problems/leaf-similar-trees/) | [Video](https://www.youtube.com/watch?v=3jvWodd7ht0) | O(n) | O(h) | DFS |
| [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [Video](https://www.youtube.com/watch?v=hTM3phVI6YQ) | O(n) | O(h) | BFS/DFS |
| [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) | [Video](https://www.youtube.com/watch?v=KcNt6v_56cc) | O(h) | O(h) | Recursion |
| [Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | [Video](https://www.youtube.com/watch?v=7cp5imvDzl4) | O(n) | O(h) | DFS) | O(max(len(a), len(b))) | O(max(len(a), len(b))) | Bit Manipulation |

## Heap

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Video](https://www.youtube.com/watch?v=XEmy13g1Qxc&ab_channel=NeetCode) | O(n) | O(1) | Quick Select |

## Prefix Sum

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/) | [Video](https://www.youtube.com/watch?v=2pndAmo_sMA&ab_channel=NeetCodeIO) | O(1) | O(n) | Prefix Sum |
| [Contiguous Array](https://leetcode.com/problems/contiguous-array/) | [Video](https://www.youtube.com/watch?v=agB1LyObUNE&ab_channel=NeetCodeIO) | O(n) | O(n) | Prefix Sum |
| [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | [Video](https://www.youtube.com/watch?v=fFVZt-6sgyo&ab_channel=NeetCode) | O(n) | O(n) | Prefix Sum |

## Sliding Window

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | [Video](https://www.youtube.com/watch?v=UdUUnoiLkPg&ab_channel=GregHogg) | O(n) | O(1) | Sliding Window |
| [Maximum Number of Vowels in a Substring of Given Length](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) | [Video](https://www.youtube.com/watch?v=kEfPSzgL-Ss) | O(n) | O(1) | Sliding Window |

## Interval

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | [Video](https://www.youtube.com/watch?v=44H3cEC2fFM&ab_channel=NeetCode) | O(n log n) | O(n) | Sorting |

## Miscellaneous

| Problem | Video | Time Complexity | Space Complexity | Approach |
|---------|-------|-----------------|------------------|----------|
| [Happy Number](https://leetcode.com/problems/happy-number/) | [Video](https://www.youtube.com/watch?v=ljz85bxOYJ0&ab_channel=NeetCode) | O(n) | O(n) | Hash Set |
| [Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/) | [Video](https://www.youtube.com/watch?v=68a1Dc_qVq4&ab_channel=NeetCode) | O(n + m) | O(n) | Monotonic Stack |
| [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | [Video](https://www.youtube.com/watch?v=yubRKwixN-U) | O(log n) | O(1) | Arithmetic |
| [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | [Video](https://www.youtube.com/watch?v=3jdxYj3DD98) | O(n) | O(1) | Arithmetic |
| [Integer to Roman](https://leetcode.com/problems/integer-to-roman/) | [Video](https://www.youtube.com/watch?v=ohBNdSJyLh8) | O(n) | O(1) | Arithmetic |
| [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | - | O(log n) | O(1) | Binary Search |
| [Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) | [Video](https://www.youtube.com/watch?v=6rrgCVjLwUg) | O(log n) | O(1) | Binary Search |
| [Asteroid Collision](https://leetcode.com/problems/asteroid-collision/) | [Video](https://www.youtube.com/watch?v=4No53MxxruE) | O(n) | O(n) | Stack |
| [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/) | [Video](https://www.youtube.com/watch?v=4KcZOGPjJ9Q) | O(1) (amortized) | O(n) | Queue |
| [Fizz Buzz](https://leetcode.com/problems/fizz-buzz/) | [Video](https://www.youtube.com/watch?v=QPZ0pIK_wsc) | O(n) | O(1) | Simulation |
| [Sqrt(x)](https://leetcode.com/problems/sqrtx/) | [Video](https://www.youtube.com/watch?v=zdMhGxRWutQ) | O(logn) | O(1) | Binary Search |

---

