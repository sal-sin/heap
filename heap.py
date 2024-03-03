"""
@author: Saloni Sinha

File: heap.py
This file implements the heap data structure with additional features. 
The APIs `percolate_up` and `percolate_down` can be used to heapify the heap 
when an element at an index `i` is changed, in O(log(n)) time.
- Heap.heapify(): Transform the list to satisfy heap invariant
- Heap.top(): Return the top (minimum) element in O(1) time
- Heap.pop(): Pop the top element in O(log(n)) time
- Heap.push(ele): Push an element `ele` by appending and percolating up in O(log(n)) time
- Heap.pos(ele): Return position of the element `ele` in the heap in O(1) time
- Heap.percolate_up(idx): Floats up an element at `idx` to the correct position in O(log(n)) time
- Heap.percolate_down(idx): Sinks an element at `idx` to the correct position in O(log(n)) time
- Heap.is_empty(): Returns a boolean indicating if heap is empty

NOTE: This can currently be used to only store distinct elements
"""

class Heap():
	def __init__(self, elements = []):
		self.__elements = elements
		self.__indices = {}
		self.heapify()
		self.__init__indices()

	def heapify(self): # O(n)
		""" Transform the list to satisfy heap invariant """
		n = len(self.__elements)
		for i in range(n//2, -1, -1):
			self.percolate_down(i)

	def top(self): # O(1)
		""" Return the top element """
		if len(self.__elements) == 0: return None
		return self.__elements[0]

	def pop(self): # O(logn)
		""" Pop the top element by swapping with 
		the last element and percolate down """
		ele = self.__elements[0]
		n = len(self.__elements)
		self.__swap(0, n - 1) # max ele comes up
		self.__elements.pop(-1) # remove popped ele
		self.__indices.pop(ele)
		self.percolate_down(0)
		return ele

	def push(self, ele): # O(logn)
		""" Push an element by appending 
		and percolating up """
		if ele in self.__indices: return
		
		n = len(self.__elements)
		self.__elements.append(ele)
		self.__indices[ele] = n
		self.percolate_up(n)

	def pos(self, ele): # O(1)
		""" Return position of the element in the heap """
		if ele in self.__indices: return self.__indices[ele]
		return -1

	def percolate_up(self, idx): # O(logn)
		""" Element at idx floats up to the correct position """
		parent_idx = self.__get_parent_idx(idx)
		while parent_idx != -1:
			if self.__elements[parent_idx] > self.__elements[idx]:
				self.__swap(parent_idx, idx)
			else: break
			idx = parent_idx
			parent_idx = self.__get_parent_idx(idx)

	def percolate_down(self, idx):
		""" Element at idx is brought down to the correct level """
		child_idx = self.__get_min_child_idx(idx)
		while child_idx != -1:
			if self.__elements[idx] > self.__elements[child_idx]:
				self.__swap(idx, child_idx)
			else: break
			idx = child_idx
			child_idx = self.__get_min_child_idx(idx)

	def is_empty(self):
		""" Returns if heap is empty """
		return len(self.__elements) == 0

	def __get_min_child_idx(self, idx):
		""" Return the smallest child of the element at idx """
		n = len(self.__elements)
		li, ri = 2*idx + 1, 2*idx + 2

		if li < n and ri < n:
			return li if self.__elements[li] < self.__elements[ri] else ri
		return li if li < n else -1

	def __get_parent_idx(self, idx):
		""" Return the position of the parent of the element at idx """
		pi = (idx - 1) >> 1
		return pi if pi >= 0 else -1

	def __swap(self, i, j):
		""" Self-explanatory """
		ele_i, ele_j = self.__elements[i], self.__elements[j]
		self.__elements[i], self.__elements[j] = ele_j, ele_i
		self.__indices[ele_i] = j
		self.__indices[ele_j] = i

	def __init__indices(self):
		""" Initialize __indices dictionary """
		n = len(self.__elements)
		for i in range(n):
			ele = self.__elements[i]
			self.__indices[ele] = i

	def __str__(self):
		s = "==============================\n"
		for ele in self.__elements:
			s += "\t{}\n".format(ele)
		s += "=============================\n"
		return s