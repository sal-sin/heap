# heap.py

This file implements the heap data structure with additional features. 
The APIs `percolate_up` and `percolate_down` can be used to heapify the heap 
when an element at an index `i` is changed, in O(log(n)) time.
```
- Heap.heapify(): Transform the list to satisfy heap invariant
- Heap.top(): Return the top (minimum) element in O(1) time
- Heap.pop(): Pop the top element in O(log(n)) time
- Heap.push(ele): Push an element `ele` by appending and percolating up in O(log(n)) time
- Heap.pos(ele): Return position of the element `ele` in the heap in O(1) time
- Heap.percolate_up(idx): Floats up an element at `idx` to the correct position in O(log(n)) time
- Heap.percolate_down(idx): Sinks an element at `idx` to the correct position in O(log(n)) time
- Heap.is_empty(): Returns a boolean indicating if heap is empty
```

NOTE: This can currently be used to only store distinct elements