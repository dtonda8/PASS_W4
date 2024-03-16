# PASS_W4
Welcome to week 4's coding activity
- Note: you're not allowed to use in-built lists, sets and dictionaries
- To run tests, open terminal then:
```sh
python3 run_tests.py # and follow command line instructions
# or 
python run_tests.py # and follow command line instructions
```
---

### Q1: Merge Sorted Lists
You are given two sorted `List`s, `list1` and `list2`.

Merge the two lists into one sorted `List`. 

Return the head of the merged linked list.

*Examples*

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Question to think about: How can we merge sorted queues?

---
### Q2: Time needed to Buy Tickets (adapted from [leetcode](https://leetcode.com/problems/time-needed-to-buy-tickets/description/))


There are `n` people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (`n` - 1)th person is at the back of the line.

You are given an array tickets where tickets[i] represents the number of tickets that the ith person would like to buy.

Each person takes exactly 1 second to __buy__ a ticket. A person can only buy 1 ticket at a time and has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. 

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

*Examples*

Input: tickets = [2,3,2], k = 2
Output: 6
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- first pass: [1, 2, 1] (t = 3)
- second pass: [0, 1, 0] (t = 6)

Input: tickets = [2,3,2], k = 1
Output: 7
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- first pass: [1, 2, 1] (t = 3)
- second pass: [0, 1, 0] (t = 6)
- second pass: [0, 0, 0] (t = 7)

Input: tickets = [2, 3, 4, 5], k = 0
Output: 5
- first pass: [1, 2, 3, 4] (t = 4)
- second pass (stops as soon as tickets[k] = 0): [0, 2, 3, 4] (t = 5)
