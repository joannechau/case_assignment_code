'''
    noun_case_assigment.py is a free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''


'''
traversal of syntax tree in order to read each node and parse
the DPs in the trees to assign correct case in respect to the
location of the tree
'''

# Make the print statements more readable
from pprint import pprint

# Define the class for each node, along with children labeling
class Node():
    def __init__(self, label, left_child = None, right_child = None):
        self.label = label
        self.left_child = left_child
        self.right_child = right_child
        self.parent = None
        if self.left_child != None:
            self.left_child.parent = self
        if self.right_child != None:
            self.right_child.parent = self

# Define a function for preorder traversal of tree
def pre_order(root):
    nodes = []
    if root == None:
        return []
    else:
        nodes.append(root)
        right_list = pre_order(root.right_child)
        left_list = pre_order(root.left_child)
        return nodes + left_list + right_list

# Find all DPs in the tree and then save the names of their children and parents
def noun_case_assignment(node):
    children_labels = []
    children = []
    parents = []
    case_assigned = {}
    nodes = pre_order(node)
    for node in nodes:
        if node.label == "DP" or node.label =="NP":
            children_labels.append(node.right_child.label)
            children.append(node.right_child)
            parents.append(node.parent.label)
            relationship = dict(zip(children_labels, parents))
    print ("The nouns and their parent nodes are:\n", relationship)

# Case assignment time!
    for child in children:
        if child.right_child == None and child.left_child == None:
            if child.parent.parent.label == "VP":
                case_assigned[child.label] = "nominative"
            if child.parent.parent.label == "V'":
                case_assigned[child.label] = "accusative"
            if child.parent.parent.parent.parent.label == "VP":
                case_assigned[child.label] = "possessive nominative"
            if child.parent.parent.label == "DP":
                case_assigned[child.label] = "genitive"
            if child.parent.parent.parent.parent.label == "V'":
                case_assigned[child.label] = "possessive accusative"
    print("The case assignment of the nouns in the sentence are:\n", case_assigned)

# Testing subjects
# Simple sentence
S1 = Node("TP", Node(""), Node("T'", Node("T"), Node("VP", Node("DP", Node(""), Node("he")),
Node("V'", Node("V", Node(""), Node("likes")), Node("DP", Node(""), Node("her"))))))

# Genitive case in subject position
S2 = Node("TP", Node(""), Node("T'", Node("T"),
Node("VP", Node("DP", Node("DP", Node(""), Node("he")), Node("D'", Node("D", Node("'s'")),
Node("NP", Node(""), Node("dog")))),
Node("V'",Node("V", Node(""), Node("likes")),
Node("DP", Node(""), Node("her"))))))

# Genitive case in object position
S3 =  Node("TP", Node(""), Node("T'", Node("T"),
Node("VP", Node("DP", Node(""), Node("he")),
Node("V'",Node("V", Node(""), Node("likes")),
Node("DP", Node("DP", Node(""), Node("she")), Node("D'", Node("D", Node("'s'")),
Node("NP", Node(""), Node("cat"))))))))

# Genitive case in both subject position and object position
S4 = Node("TP", Node(""), Node("T'", Node("T"),
Node("VP", Node("DP", Node("DP", Node(""), Node("he")), Node("D'", Node("D", Node("'s'")),
Node("NP", Node(""), Node("dog")))),
Node("V'",Node("V", Node(""), Node("likes")),
Node("DP", Node("DP", Node(""), Node("she")), Node("D'", Node("D", Node("'s'")),
Node("NP", Node(""), Node("cat"))))))))

# Sample SOV language: Korean "she loves him"
S5 = Node("TP", Node(""), Node("T'", Node("T"), Node("VP", Node("DP", Node(""),
Node("she-subj")), Node("V'", Node("DP", Node(""), Node("he-obj")),
Node("V", Node(""), Node("love"))))))

noun_case_assignment(S4)
