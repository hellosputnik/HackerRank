package main

import "fmt"

// ==== Stack ==================================================================

type Stack struct {
	data []int
	size int
}

func (s *Stack) push(integer int) {
	s.data = append(s.data, integer)
	s.size++
}

func (s *Stack) pop() int {
	popped := s.data[s.size-1]
	s.data = s.data[0 : s.size-1]
	s.size--

	return popped
}

func (s *Stack) peek() int {
	return s.data[s.size-1]
}

// =============================================================================

// ==== Queue ==================================================================

type Queue struct {
	a    *Stack
	b    *Stack
	i    int
	size int
}

func (q *Queue) enqueue(integer int) {
	q.a.push(integer)

	if q.size == 0 {
		q.i = integer
	}

	q.size++
}

func (q *Queue) dequeue() int {
	for i := 0; i < q.size; i++ {
		q.b.push(q.a.pop())
	}

	dequeued := q.b.pop()
	q.size--

	if q.size > 0 {
		q.i = q.b.peek()
	} else {
		q.i = 0
	}

	for i := 0; i < q.size; i++ {
		q.a.push(q.b.pop())
	}

	return dequeued
}

// =============================================================================

// ==== main ===================================================================

func main() {
	var q, queryType, x int

	fmt.Scan(&q)

	// Create a queue using 2 stacks.
	queue := Queue{a: &Stack{}, b: &Stack{}}

	for i := 0; i < q; i++ {
		// Read the type of queue operation.
		fmt.Scan(&queryType)

		switch queryType {
		// Enqueue element x into the end of the queue.
		case 1:
			fmt.Scan(&x)
			queue.enqueue(x)

		// Dequeue the element at the front of the queue.
		case 2:
			queue.dequeue()

		// Print the element at the front of the queue (i.e., peek).
		case 3:
			fmt.Println(queue.i)
		}
	}
}

// =============================================================================
