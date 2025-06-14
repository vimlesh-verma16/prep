# important programs for DSA
"""Sorting"""

"""Insertion Sort"""
# by ravindra babu take example of deck of cards and start picking card and travesing back in array till 0 position and finding its right place and do swaps

# nums = [2, -3, 4, 6, 55, 7, -2]
# for i in range(len(nums)):
#     j = i
#     while j > 0 and nums[j - 1] > nums[j]:
#         nums[j - 1], nums[j] = nums[j], nums[j - 1]
#         j -= 1

#     print(nums)

# --------------------------------------------------------------
# "Selection sort"
# putinng the smallest element at the front of array

# a=[-4,81,9,2,-3,6,1,2,3]
# for i in range(len(a)):
#     index=i
#     for j in range(i+1,len(a)):
#         if a[j]<a[index]:
#             index=j

#     if index!=i:
#         a[i],a[index]=a[index],a[i]
#         print(a)

# print(a)

# ------------------------------------------------------------------

# This algorithm is fastest on an extremely small or nearly sorted set of data.
# sends biggest element in the end
"""Bubble Sort"""

# num = [11, 1, -3, 4, 9, 0, -2]
# for i in range(len(num)):
#     for j in range(len(num) - 1 - i): # subtract i as last element will be sorted
#         if num[j] > num[j + 1]:
#             num[j], num[j + 1] = num[j + 1], num[j]

#     print(num)

# print("final answeer", num)

# ---------------------------------------------------------
"""Counting Sort"""
# Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K.

# num=[9,2,0,4,1,2,3,4,5]
# m=max(num)
# arr=[0]*(m+1)
# ans=[0]*len(num)
# for i in range(len(num)):
#     arr[num[i]]+=1

# for i in range(1,len(arr)):
#     s=arr[i]+arr[i-1]
#     arr[i]=s

# for i in range(len(num)):
#     arr[num[i]]=arr[num[i]]-1
#     ans[arr[num[i]]]=num[i]
# print(ans)
# ---------------------------------------------------------

"""Merge Sort"""

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])

#     return merge(left, right)


# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# # Example usage
# arr = [-1, 3, 6, 8, -10, 22, 18, 2, -3, 0]
# print("before:", arr)
# sorted_arr = merge_sort(arr)
# print("after:", sorted_arr)

# --------------------------------------------------------------------------------------------

"""Quick Sort"""
# 1.Quick sort is fastest, but it is not always O(N*log N), as there are worst cases where it becomes O(N2).
# 2.Quicksort is probably more effective for datasets that fit in memory. For larger data sets it proves to be inefficient so algorithms like merge sort are preferred in that case.
# 3.Quick Sort in is an in-place sort (i.e. it doesn’t require any extra storage) so it is appropriate to use it for arrays.
# 🔁 Quicksort Overview

# Quicksort is a divide-and-conquer sorting algorithm:
#     Pick a pivot.
#     Partition the array: put all elements smaller than the pivot to the left, and all greater to the right.
#     Recursively sort the left and right parts.


# def swap(nums, i, j):
#     # Swap elements at index i and j
#     nums[i], nums[j] = nums[j], nums[i]


# def partition(nums, low, high):
#     # Choose the middle element as pivot
#     pivot_index = (low + high) // 2
#     pivot_value = nums[pivot_index]

#     # Move pivot to the end temporarily
#     swap(nums, pivot_index, high)

#     store_index = low  # Position to store next smaller element

#     # Rearranging the elements
#     for i in range(low, high):
#         if nums[i] < pivot_value:
#             swap(nums, i, store_index)
#             store_index += 1

#     # Move pivot to its final position
#     swap(nums, store_index, high)

#     return store_index  # Return the index where pivot ended up


# def quicksort(nums, low, high):
#     # Base case: if the segment is of length 0 or 1, it's sorted
#     if low >= high:
#         return

#     # Partition the list and get pivot index
#     pivot = partition(nums, low, high)

#     # Recursively sort elements before and after partition
#     quicksort(nums, low, pivot - 1)
#     quicksort(nums, pivot + 1, high)


# # Example usage
# nums = [2, 5, 33, 4, 1, 0, -5, 10]
# print("Before sorting:", nums)
# quicksort(nums, 0, len(nums) - 1)
# print("After sorting:", nums)


# ---------------------------------------------------------------
# ravindra babu ravula

# def quicksort(nums,low,high):
#     if low>=high:
#         return

#     pivot_index=partition(nums,low,high)
#     quicksort(nums,low,pivot_index-1)
#     quicksort(nums,pivot_index+1,high)

# def partition(nums,low,high):
#     pivot=nums[high]
#     i=low-1
#     for j in range(low,high):
#         if nums[j]<=pivot:
#             i+=1
#             swap(nums,i,j)

#     swap(nums,i+1,high)
#     return i+1

# def swap(nums,i,j):
#     temp=nums[i]
#     nums[i]=nums[j]
#     nums[j]=temp

# nums=[2,5,33,4,1,0,-5,10]
# print(nums)
# quicksort(nums,0,len(nums)-1)
# print(nums)
# -------------------------------------------------------------------
"""Binary search """

# def binary(a,n):
#     low=0
#     high=len(a)-1


#     while low <= high:
#         mid=(low+high)//2

#         if a[mid]<n:
#             low=mid+1
#         elif a[mid]>n:
#             high=mid-1
#         elif a[mid]==n:
#             return mid
#     return -1

# arr=[1,22,55,66,33,-1,-2,244,54,22,33,4,5]
# arr.sort()
# print(arr)
# num=1
# r=binary(arr,num)
# print(r )

"""REcursive approach for binary search"""

# nums=[12,3,3,4212,32,67,787,8,98,45,34,32]


# -------------------------------------------------------------------------------
"""Kadane Algorithm """
# a=[-2,-5,-8]
# maxsum=0
# cursum=0
# for i in range(len(a)):
#     cursum+=a[i]
#     if cursum>maxsum:
#         maxsum=cursum
#     if cursum<0 :
#         cursum=0

# print(maxsum)

"""Kadane algo for both positive and negative """
# a=[1,2,3,-2,5]
#     # meh=Max ending here
#     # msf=Max so far
# meh=0
# msf=float('-inf')
# for i in range(len(a)):
#     meh=meh+a[i]
#     if meh<a[i]:
#         meh=a[i]
#     if (msf<meh):
#         msf=meh

# print(msf)


# ---------------------------------------------------------
""" linked list implimentation """

# class Node():
#     def __init__(self,data):
#         self.data=data
#         self.nextNode=None

# class Linkedlist():
#     def __init__(self):
#         self.head=None
#         self.size=0

#     def insertStart(self,data):
#         self.size+=1
#         newNode=Node(data)

#         if not self.head:
#             self.head=newNode
#         else:
#             newNode.nextNode=self.head
#             self.head=newNode

#     def remove(self,data):
#         if self.head is None:
#             return
#         self.size=self.size-1
#         currentNode=self.head
#         prevNode=None

#         while currentNode.data !=data:
#             prevNode=currentNode
#             currentNode=currentNode.nextNode

#         if prevNode is None:
#             self.head=currentNode.nextNode
#         else:
#             prevNode.nextNode=currentNode.nextNode


#     def size1(self):
#         return self.size

#     def insertEnd(self,data):
#         self.size +=1
#         newNode=Node(data)
#         actualNode=self.head

#         while actualNode.nextNode is not None:
#             actualNode=actualNode.nextNode

#         actualNode.nextNode=newNode

#     def traverselist(self):
#         actualNode=self.head

#         while actualNode is not None:
#             print(actualNode.data)
#             actualNode=actualNode.nextNode

# llist=Linkedlist()
# llist.insertStart(25)
# llist.insertStart(2)
# llist.insertStart(10)
# llist.insertEnd(22)

# llist.traverselist()
# print(llist.size)


# --------------------------------------------------------------
"""Binary search Tree"""

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.leftchild=None
#         self.rightchild=None

# class binarySearchTree:
#     def __init__(self):
#         self.root=None

#     def insert(self,data):
#         if not self.root:
#             self.root=Node(data)
#         else:
#             self.insertNode(data,self.root)

#     def insertNode(self,data,node):
#         if data<node.data:
#             if node.leftchild:
#                 self.insertNode(data,node.leftchild)
#             else:
#                 node.leftchild=Node(data)
#         else:
#             if node.rightchild:
#                 self.insertNode(data,node.rightchild)
#             else:
#                 node.rightchild=Node(data)
#     def removeNode(self,data,node):
#         if not node :
#             return node

#         if data<node.data:
#             node.leftchild=self.removeNode(data,node.leftchild)

#         elif data>node.data:
#             node.rightchild=self.removeNode(data,node.rightchild)

#         else:
#             if not node.leftchild and node.rightchild:
#                 print('removing a leaf node')
#                 del node
#                 return None

#             if not node.leftchild:
#                 print("removing node with single rightchild ")
#                 tempnode=node.rightchild
#                 del node
#                 return tempnode

#             elif not node.rightchild:
#                 print("removing node with single left child")
#                 tempnode=node.leftchild
#                 del node
#                 return tempnode

#             print('removing node with both childs')
#             tempnode=self.getpredecessor(node.leftchild)
#             node.data=tempnode.data
#             node.leftchild=self.removeNode(tempnode.data,node.leftchild)

#         return node

#     def getpredecessor(self,node):
#         if node.rightchild:
#             return self.getpredecessor(node.rightchild)
#         return node

#     def remove(self,data):
#         if self.root:
#             self.root=self.removeNode(data,self.root)

#     def getMinValue(self,node):
#         if self.root:
#             return self.getMin(self.root)

#     def getMin(self,node):
#         if node.leftchild:
#             return self.getMin(node.leftchild)

#         return node.data

#     def getMaxValue(self,node):
#         if self.root:
#             return self.getMax(self.root)

#     def getMax(self,node):
#         if node.rightchild:
#             return self.getMax(node.rightchild)

#         return node.data

#     def Traverse(self):
#         if self.root:
#             self.traverseinorder(self.root)
#     def traverseinorder(self,node):
#         if node.leftchild:
#             self.traverseinorder(node.leftchild)

#         print(node.data)

#         if node.rightchild:
#             self.traverseinorder(node.rightchild)

# bst=binarySearchTree()

# bst.insert(10)
# bst.insert(1)
# bst.insert(5)
# bst.insert(11)
# bst.insert(0)
# bst.Traverse()
# bst.remove(1)

# bst.Traverse()
# ----------------------------------------------------------------------

"""AVL Tree"""

# class Node(object):

# 	def __init__(self, data):
# 		self.data = data
# 		self.height = 0
# 		self.leftChild = None
# 		self.rightChild = None

# class AVL(object):

# 	def __init__(self):
# 		self.root = None

# 	def remove(self, data):
# 		if self.root:
# 			self.root = self.removeNode(data, self.root)

# 	def insert(self, data):
# 		self.root = self.insertNode(data, self.root)

# 	def insertNode(self, data, node):

# 		if not node:
# 			return Node(data)

# 		if data < node.data:
# 			node.leftChild = self.insertNode(data, node.leftChild)
# 		else:
# 			node.rightChild = self.insertNode(data, node.rightChild)

# 		node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1

# 		return self.settleViolation(data, node)

# 	def removeNode(self,data, node):

# 		if not node:
# 			return node

# 		if data < node.data:
# 			node.leftChild = self.removeNode(data, node.leftChild)
# 		elif data > node.data:
# 			node.rightChild = self.removeNode(data, node.rightChild)
# 		else:

# 			if not node.leftChild and not node.rightChild:
# 				print("Removing a leaf node...")
# 				del node
# 				return None

# 			if not node.leftChild:
# 				print("Removing a node with a right child...")
# 				tempNode = node.rightChild
# 				del node
# 				return tempNode
# 			elif not node.rightChild:
# 				print("Removing a node with a left child...")
# 				tempNode = node.leftChild
# 				del node
# 				return tempNode

# 			print("Removing node with two children...")
# 			tempNode = self.getPredecessor(node.leftChild)
# 			node.data = tempNode.data
# 			node.leftChild = self.removeNode(tempNode.data, node.leftChild)

# 		if not node:
# 			return node; # if the tree had just a single node

# 		node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1

# 		balance = self.calcBalance(node)

# 		# doubly left heavy situation
# 		if balance > 1 and self.calcBalance(node.leftChild) >= 0:
# 			return self.rotateRight(node)

# 		# left right case
# 		if balance > 1 and self.calcBalance(node.leftChild) < 0:
# 			node.leftChild = self.rotateLeft(node.leftChild)
# 			return self.rotateRight(node)

# 		# right right case
# 		if balance < -1 and self.calcBalance(node.rightChild) <= 0:
# 			return self.rotateLeft(node)

# 		# right left case
# 		if balance < -1 and self.calcBalance(node.rightChild) > 0:
# 			node.rightChild = self.rotateRight(node.rightChild)
# 			return self.rotateLeft(node)

# 		return node

# 	def getPredecessor(self, node):

# 		if node.rightChild:
# 			return self.getPredecessor(node.rightChild)

# 		return node

# 	def settleViolation(self, data, node):

# 		balance = self.calcBalance(node)

# 		# this is the Case I !!!! left-left heavy situation
# 		if balance > 1 and data < node.leftChild.data:
# 			print("Left left heavy tree...")
# 			return self.rotateRight(node)

# 		# this is the Case II right-right !!!!
# 		if balance < -1 and data > node.rightChild.data:
# 			print("Right right heavy tree...")
# 			return self.rotateLeft(node)

# 		# left-right situation
# 		if balance > 1 and data > node.leftChild.data:
# 			print("Tree is left right heavy...")
# 			node.leftChild = self.rotateLeft(node.leftChild)
# 			return self.rotateRight(node)

# 		# right-left situation
# 		if balance < -1 and data < node.rightChild.data:
# 			node.rightChild = self.rotateRight(node.rightChild)
# 			return self.rotateLeft(node)

# 		return node


# 	def calcHeight(self, node):

# 		if not node:
# 			return -1

# 		return node.height

# 	# if it returns value > 1  it means it is a left heavy tree --> right rotation
# 	#   < -1   right heavy tree -> left rotation
# 	def calcBalance(self, node):

# 		if not node:
# 			return 0

# 		return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild);

# 	def traverse(self):
# 		if self.root:
# 			self.traverseInorder(self.root)

# 	def traverseInorder(self, node):

# 		if node.leftChild:
# 			self.traverseInorder(node.leftChild)

# 		print("%s " % node.data)

# 		if node.rightChild:
# 			self.traverseInorder(node.rightChild)

# 	def rotateRight(self, node):

# 		print("Rotating to the right on node " , node.data)

# 		tempLeftChild = node.leftChild
# 		t = tempLeftChild.rightChild

# 		tempLeftChild.rightChild = node
# 		node.leftChild = t

# 		node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1
# 		tempLeftChild.height = max( self.calcHeight(tempLeftChild.leftChild) , self.calcHeight(tempLeftChild.rightChild) ) + 1

# 		return tempLeftChild

# 	def rotateLeft(self, node):

# 		print("Rotating to the left on node " , node.data)

# 		tempRightChild = node.rightChild
# 		t = tempRightChild.leftChild

# 		tempRightChild.leftChild = node
# 		node.rightChild = t

# 		node.height = max( self.calcHeight(node.leftChild) , self.calcHeight(node.rightChild) ) + 1
# 		tempRightChild.height = max( self.calcHeight(tempRightChild.leftChild) , self.calcHeight(tempRightChild.rightChild) ) + 1

# 		return tempRightChild


# avl = AVL()
# avl.insert(5)
# avl.insert(3)
# avl.insert(4)


# avl.traverse()

# ------------------------------------------------------------------------------
""" Heaps """
# from heapq import heappush,heappop,heapify

# heap=[]

# nums=[4,8,2,7,3,-1,22]
# for i in nums:
# 	heappush(heap,i)

# while(heap):
# 	print(heappop(heap))

# heapify(nums)
# print(nums)
# ---------------------------------------------------------------
"""Graphs  TRaversals """

"""BFS"""
# class Node(object):
# 	def __init__(self, name):
# 		self.name = name
# 		self.adjacencyList = []
# 		self.visited = False
# 		self.predecessor = None

# class BreadthFirstSearch(object):
# 	def bfs(self, startNode):
# 		queue = []
# 		queue.append(startNode)
# 		startNode.visited = True
# 		# BFS -> queue      DFS --> stack BUT usually we implement it with recursion !!!
# 		while queue:
# 			actualNode = queue.pop(0)
# 			print(actualNode.name)

# 			for n in actualNode.adjacencyList:
# 				if not n.visited:
# 					n.visited = True
# 					queue.append(n)

# node1 = Node("A")
# node2 = Node("B")
# node3 = Node("C")
# node4 = Node("D")
# node5 = Node("E")

# node1.adjacencyList.append(node2)
# node1.adjacencyList.append(node3)
# node2.adjacencyList.append(node4)
# node4.adjacencyList.append(node5)

# bfs = BreadthFirstSearch()
# bfs.bfs(node1)
# ---------------------------------------------------------------------------
""" DFS """

# class Node(object):

# 	def __init__(self, name):
# 		self.name = name
# 		self.adjacenciesList = []
# 		self.visited = False
# 		self.predecessor = None

# class DepthFirstSearch(object): # BFS -> queue + layer by layer algorithm   DFS -> stack + goes as deep aspossible into the tree !!!

# 	def dfs(self, node):
# 		node.visited = True
# 		print(node.name)

# 		for n in node.adjacenciesList:
# 			if not n.visited:
# 				self.dfs(n)


# node1 = Node("A")
# node2 = Node("B")
# node3 = Node("C")
# node4 = Node("D")
# node5 = Node("E")

# node1.adjacenciesList.append(node2)
# node1.adjacenciesList.append(node3)
# node2.adjacenciesList.append(node4)
# node4.adjacenciesList.append(node5)

# dfs=DepthFirstSearch()
# dfs.dfs(node1)

# -------------------------------------------------------------------------------------------

"""Garphs shortest path finding algorithms"""

"""Dijkstra algorithm"""
# import heapq
# import sys

# class Edge(object):

# 	def __init__(self, weight, startVertex, targetVertex):
# 		self.weight = weight
# 		self.startVertex = startVertex
# 		self.targetVertex = targetVertex

# class Node(object):

# 	def __init__(self, name):
# 		self.name = name
# 		self.visited = False
# 		self.predecessor = None
# 		self.adjacenciesList = []
# 		self.minDistance = sys.maxsize

# 	def __cmp__(self, otherVertex):
# 		return self.cmp(self.minDistance, otherVertex.minDistance)

# 	def __lt__(self, other):
# 		selfPriority = self.minDistance
# 		otherPriority = other.minDistance
# 		return selfPriority < otherPriority

# class Algorithm(object):

# 	def calculateShortestPath(self, vertexList, startVertex):

# 		q = []
# 		startVertex.minDistance = 0
# 		heapq.heappush(q, startVertex)

# 		while q:
# 			actualVertex = heapq.heappop(q)

# 			for edge in actualVertex.adjacenciesList:
# 				u = edge.startVertex
# 				v = edge.targetVertex
# 				newDistance = u.minDistance + edge.weight

# 				if newDistance < v.minDistance:
# 					v.predecessor = u
# 					v.minDistance = newDistance
# 					heapq.heappush(q, v)

# 	def getShortestPathTo(self, targetVertex):
# 		print("Shortest path to vertex is: ", targetVertex.minDistance)

# 		node = targetVertex

# 		while node is not None:
# 			print("%s " % node.name)
# 			node = node.predecessor

# node1 = Node("A")
# node2 = Node("B")
# node3 = Node("C")
# node4 = Node("D")
# node5 = Node("E")
# node6 = Node("F")
# node7 = Node("G")
# node8 = Node("H")

# edge1 = Edge(5,node1,node2)
# edge2 = Edge(8,node1,node8)
# edge3 = Edge(9,node1,node5)
# edge4 = Edge(15,node2,node4)
# edge5 = Edge(12,node2,node3)
# edge6 = Edge(4,node2,node8)
# edge7 = Edge(7,node8,node3)
# edge8 = Edge(6,node8,node6)
# edge9 = Edge(5,node5,node8)
# edge10 = Edge(4,node5,node6)
# edge11 = Edge(20,node5,node7)
# edge12 = Edge(1,node6,node3)
# edge13 = Edge(13,node6,node7)
# edge14 = Edge(3,node3,node4)
# edge15 = Edge(11,node3,node7)
# edge16 = Edge(9,node4,node7)

# node1.adjacenciesList.append(edge1)
# node1.adjacenciesList.append(edge2)
# node1.adjacenciesList.append(edge3)
# node2.adjacenciesList.append(edge4)
# node2.adjacenciesList.append(edge5)
# node2.adjacenciesList.append(edge6)
# node8.adjacenciesList.append(edge7)
# node8.adjacenciesList.append(edge8)
# node5.adjacenciesList.append(edge9)
# node5.adjacenciesList.append(edge10)
# node5.adjacenciesList.append(edge11)
# node6.adjacenciesList.append(edge12)
# node6.adjacenciesList.append(edge13)
# node3.adjacenciesList.append(edge14)
# node3.adjacenciesList.append(edge15)
# node4.adjacenciesList.append(edge16)


# vertexList = (node1,node2,node3, node4, node5, node6, node7, node8);

# algorithm = Algorithm();
# algorithm.calculateShortestPath(vertexList, node1);
# algorithm.getShortestPathTo(node4);

# ----------------------------------------------------------------------------------
"""Bellman ford algorithm """

# import sys

# class Node(object):

# 	def __init__(self, name):
# 		self.name = name
# 		self.visited = False
# 		self.predecessor = None
# 		self.adjacenciesList = []
# 		self.minDistance = sys.maxsize

# class Edge(object):

# 	def __init__(self, weight, startVertex, targetVertex):
# 		self.weight = weight
# 		self.startVertex = startVertex
# 		self.targetVertex = targetVertex

# class BellmanFord(object):

# 	HAS_CYCLE = False

# 	def calculateShortestPath(self, vertexList, edgeList, startVertex):

# 		startVertex.minDistance = 0

# 		for i in range(0,len(vertexList)-1):
# 			for edge in edgeList:

# 				u = edge.startVertex
# 				v = edge.targetVertex

# 				newDistance = u.minDistance + edge.weight

# 				if newDistance < v.minDistance:
# 					v.minDistance = newDistance
# 					v.predecessor = u

# 		for edge in edgeList:
# 			if self.hasCycle(edge):
# 				print("Negative cycle detected...")
# 				BellmanFord.HAS_CYCLE = True
# 				return

# 	def hasCycle(self, edge):
# 		if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
# 			return True
# 		else:
# 			return False

# 	def getShortestPathTo(self, targetVertex):

# 		if not BellmanFord.HAS_CYCLE:
# 			print("Shortest path exists with value: ", targetVertex.minDistance);

# 			node = targetVertex

# 			while node is not None:
# 				print(node.name)
# 				node = node.predecessor
# 		else:
# 			print("Negative cycle detected...")


# node1 = Node("A");
# node2 = Node("B");
# node3 = Node("C");
# node4 = Node("D");
# node5 = Node("E");
# node6 = Node("F");
# node7 = Node("G");
# node8 = Node("H");

# edge1 = Edge(5,node1,node2);
# edge2 = Edge(8,node1,node8);
# edge3 = Edge(9,node1,node5);
# edge4 = Edge(15,node2,node4);
# edge5 = Edge(12,node2,node3);
# edge6 = Edge(4,node2,node8);
# edge7 = Edge(7,node8,node3);
# edge8 = Edge(6,node8,node6);
# edge9 = Edge(5,node5,node8);
# edge10 = Edge(4,node5,node6);
# edge11 = Edge(20,node5,node7);
# edge12 = Edge(1,node6,node3);
# edge13 = Edge(13,node6,node7);
# edge14 = Edge(3,node3,node4);
# edge15 = Edge(11,node3,node7);
# edge16 = Edge(9,node4,node7);

# edge17 = Edge(1,node1,node2);
# edge18 = Edge(1,node2,node3);
# edge19 = Edge(-3,node3,node1);

# node1.adjacenciesList.append(edge1);
# node1.adjacenciesList.append(edge2);
# node1.adjacenciesList.append(edge3);
# node2.adjacenciesList.append(edge4);
# node2.adjacenciesList.append(edge5);
# node2.adjacenciesList.append(edge6);
# node8.adjacenciesList.append(edge7);
# node8.adjacenciesList.append(edge8);
# node5.adjacenciesList.append(edge9);
# node5.adjacenciesList.append(edge10);
# node5.adjacenciesList.append(edge11);
# node6.adjacenciesList.append(edge12);
# node6.adjacenciesList.append(edge13);
# node3.adjacenciesList.append(edge14);
# node3.adjacenciesList.append(edge15);
# node4.adjacenciesList.append(edge16);


# vertexList = (node1,node2,node3, node4, node5, node6, node7, node8);
# edgeList = (edge1,edge2,edge3,edge4,edge5,edge6,edge7,edge8,edge9,edge10,edge11,edge12,edge13,edge14,edge15,edge16);
# # edgeList = (edge17, edge18, edge19);

# algorithm = BellmanFord();
# algorithm.calculateShortestPath(vertexList, edgeList, node1);
# algorithm.getShortestPathTo(node7);

# -------------------------------------------------------------------

"""dijisktra leetcode 743"""
# class Solution:
#     def networkDelayTime(self, times, N, K):
#         q, t, adj = [(0, K)], {}, collections.defaultdict(list)
#         for u, v, w in times:
#             adj[u].append((v, w))
#         while q:
#             time, node = heapq.heappop(q)
#             if node not in t:
#                 t[node] = time
#                 for v, w in adj[node]:
#                     heapq.heappush(q, (time + w, v))
#         return max(t.values()) if len(t) == N else -1


# -----------------------------------------------------------------------
"""Shortest path algo  leetcode 743"""
# class Solution:
#     def networkDelayTime(self, times, N, K):
#         t, graph, q = [0] + [float("inf")] * N, collections.defaultdict(list), collections.deque([(0, K)])
#         for u, v, w in times:
#             graph[u].append((v, w))
#         while q:
#             time, node = q.popleft()
#             if time < t[node]:
#                 t[node] = time
#                 for v, w in graph[node]:
#                     q.append((time + w, v))
#         mx = max(t)
#         return mx if mx < float("inf") else -1
# ------------------------------------------------------------------
"""taking variable length parameters for functions"""
# *args is used to give variable number of arguments in parameter
# **kwargs is used to give variable numbe of argument with keywords in params

# def func(**kwargs):
#     for i in kwargs:
#         print(i)
# func(name='vimlesh',age='22')

# -----------------------------------------------------------------

"""TAKING Multiple inputs and printing the string in lexographic order"""
# from itertools import permutations
# word,k = input().split()

# y=int(k)
# s=word.upper()
# x=list(permutations(s,y))
# x.sort()
# for i in x:
#     r = ''.join(i)
#     print(r)

"""Taking multiple input at the same time """
# word,k = input().split()

# x, y, z, n = (int(input()) for _ in range(4))
# print(x,y,z,n)

# n=int(input())
# record=[[input(),float(input())] for i in range(n)]
# print(record)

""" list compreshension with nested list"""
# if __name__ == '__main__':
#   n=int(input())
#   re=[[input(),float(input())] for i in range(n)]

# li=[]
# for i in range(len(re)):
#     li.append(re[i][1])

# se=sorted(list(set(li)))
# se.remove(min(se))
# print(min(se))
# print("\n".join([a for a,b in sorted(re) if b==min(se)]))

"""getting queery sum and rounding off"""
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     # query_name = input("avg of stu")

# k=list(student_marks.keys())
# v=list(student_marks.values())
# newdict={name:sum(avg)/3 for name,avg in zip(k,v)}
# print('{:.2f}'.format(newdict[input()]))

"""getting digit till  2 decimal places """

# float = 2.154327
# format_float = "{:.2f}".format(float)
# print(format_float)

""" eval function """
# if __name__ == '__main__':
#     l=[]
#     N = int(input())
#     for i in range(N):
#         s=input().split()
#         cmd=s[0]
#         args=s[1:]
#         if cmd != "print":
#             cmd += "("+",".join(args)+")"
#             eval("l."+cmd)
#         else:
#            print(l)


""" OOPS For Details of Company Employee"""
# class Programmer():
#     company = 'microsoft'

#     def __init__(self, name, salary, sex, position):
#         self.name = name
#         self.salary = salary
#         self.sex = sex
#         self.position = position

#     def getDetails(self):
#         print(
#             f'name of employee is {self.name} ,salary is {self.salary} ,gender is {self.sex},his position is {self.position}')

# harry = Programmer('harry', 1000, 'male', "developer")
# berry = Programmer('berry', 10, 'male', 'ml')
# kabir = Programmer('kabir', 400, 'male', 'frontend')
# kivy = Programmer('kivy', 101, 'male', 'backend')
# harry.getDetails()

"""oops for squareroot"""
# import math
# class Calculator:
#     def calculate(self,num,operation):
#               if operation=='square':
#                   print(num**2)
#               elif operation=='sqrt':
#                   print("{:.2f}".format(math.sqrt(num)))
#               elif operation=='cube':
#                   print(num**3)

# number=Calculator()
# number.calculate(10,'square')
# number.calculate(11,'sqrt')

# ----------------------------------------------------------------
"""Rabin karp"""
# def hashcode(g,glen):
#     c=0
#     for i in range(glen+1):
#         c=c+(((ord(g[i])*(26**glen))))
#         glen-=1
#         return c

# def Rabinkarp(g,f):
#     glen=len(f)-1
#     if len(g)<len(f):
#         return False
#     code=hashcode(f,glen)
#     ans=hashcode(g,glen)

#     j=0
#     for i in range(1,len(g)):
#         print(code,ans)
#         if code==ans:
#             x=j
#             for i in f:
#                 print(i,g[x])
#                 if g[x]!=i:
#                     break
#                 x+=1
#             else:
#                 return True

#         ans=((ans-((ord(g[j]))*(26**glen)))*10)+ord(g[j+1])
#         print(ans)
#         j+=1

#     return False

# given="aaabc"
# find= "abc"
# c=Rabinkarp(given,find)
# print(c)

# ------------------------------------------------------------------
"""' Union Find"""

# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         parent = [i for i in range(len(edges) + 1)]  # Parent array to track disjoint sets
#         rank = [1] * (len(edges) + 1)  # Rank array for union by rank optimization

#         # Find function with path compression
#         def find(n):
#             while n != parent[n]:
#                 parent[n] = parent[parent[n]]  # Path compression
#                 n = parent[n]
#             return n

#         # Union function with union by rank
#         def union(n1, n2):
#             par1, par2 = find(n1), find(n2)
#             if par1 == par2:  # If they already share the same parent, this edge is redundant
#                 return False
#             # Union by rank
#             if rank[par1] > rank[par2]:
#                 parent[par2] = par1
#                 rank[par1] += rank[par2]
#             else:
#                 parent[par1] = par2
#                 rank[par2] += rank[par1]
#             return True

#         # Process each edge
#         for i, j in edges:
#             if not union(i, j):  # If union fails, the edge is redundant
#                 return [i, j]
