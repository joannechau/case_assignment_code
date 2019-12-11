---
title: Case Assignment - Code Documentation
author: Joanne Chau
date: 11 December 2019
---

# Description

The premise of this code is to assign case markings to nouns in sentences by understanding the local domains which license such case assignments. Using a TSL (Tier-based, strictly local) approach of case assignment as suggested by Mai Ha Vu, Nazila Shafiei and Thomas Graf, I analyzed acceptable local domains of case assignments in phrase structure trees.

The code successfully assigns nominative case marking, accusative case marking and genitive case marking. It is still in development for dative case marking and more complicated sentences.

---

# Prerequisites

- Machine that supports Python 3.

- BFS (Breadth First Search) of the tree (for non-linguistics users)

	- Users should be able to list every node of a binary tree from top down, left to right fashion. If a node only has one child, make that child the right branched child, and have an empty left branch.

![Breadth First Search](https://github.com/joannechau/case_assignment_code/blob/master/BFS.png =100x20)

- Semantic Bracketing (for linguistics users)

	- Users should be able to reiterate a binary tree into semantic bracketing for the input of the tree. If a node only has one child, make that child the right branched child, and have an empty left branch.

![Sample Tree](Small)

The BFS reading is TP, T', T, VP, DP, V', V, DP

The semantic bracketing would be [TP [T$'$ [T [VP [DP] [V' [V] [DP]]]]]

---

# Installation

1. Encode the binary tree into an understandable input for the code. List every node out in semantic bracketing form, change the brackets to parenthesis and add "Node" before each left bracket "(". When submitting a sentence, ensure that the nouns are different. If the same noun is used, utilize a number to keep track of the noun being used to ensure that it does not get deleted in the output dictionary.

	a. As the code ignores all non-local domains, as long as the input includes the VP structure, it will ignore all non-relevant parts of the tree.

2. After the sentence is encoded, enter the input into the code and allow the code to run.

3. The code will pre-order traverse the tree and save all DPs found in the tree along with their mother nodes and daughter nodes (to keep track of the local domains and the the lexical items of the tree).

4. The code will output a dictionary of the detected DP lexical items and their mother nodes as well as a dictionary of each of the DP lexical items and their case assignments. All non-terminal DPs will be detected in the motherhood dictionary but would be ignored in the dictionary containing the case assignments.

5. Below is a sample run of the sentence "His dog likes her cat".

![Tree for "his dog likes her cat."](Big)

```python
Input:

S = Node("TP", Node(""), Node("T'", Node("T"),
Node("VP", Node("DP", Node("DP", Node(""), Node("he")),
Node("D'", Node("D", Node("'s'")),
Node("NP", Node(""), Node("dog")))),
Node("V'",Node("V", Node(""), Node("likes")),
Node("DP", Node("DP", Node(""), Node("she")),
Node("D'", Node("D", Node("'s'")),
Node("NP", Node(""), Node("cat"))))))))

noun_case_assignment(S)

Output:

 The nouns and their parent nodes are:
 {"D'": "V'", 'he': 'DP', 'dog': "D'", 'she': 'DP', 'cat': "D'"}

The case assignment of the nouns in the sentence are:
 {'he': 'genitive', 'dog': 'possessive nominative',
'she': 'genitive', 'cat': 'possessive accusative'}
```

---

# Resources

Vu, M., Shafiei, N., Graf, T. (2019). "Case assignment in TSL syntax: a case study", _Proceedings of the Society for Computation in Linguistics:_ Vol.2, Article 28.

---

# Contact

Email address: choryan.chau@stonybrook.edu
