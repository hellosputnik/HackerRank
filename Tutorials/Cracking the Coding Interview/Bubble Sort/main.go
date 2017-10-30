package main

import "fmt"

// Algorithm and comments was provided by the HackerRank problem
func sort(a []int) int {
	n := len(a)
	totalNumberOfSwaps := 0

	for i := 0; i < n; i++ {
		// Track number of elements swapped during a single array traversal
		numberOfSwaps := 0

		for j := 0; j < n-1; j++ {
			// Swap adjacent elements if they are in decreasing order
			if a[j] > a[j+1] {
				swap(&a[j], &a[j+1])
				numberOfSwaps++
			}
		}

		totalNumberOfSwaps += numberOfSwaps

		// If no elements were swapped during a traversal, array is sorted
		if numberOfSwaps == 0 {
			break
		}
	}

	return totalNumberOfSwaps
}

func swap(x, y *int) {
	*x ^= *y
	*y ^= *x
	*x ^= *y
}

func main() {
	var n int

	fmt.Scan(&n)

	a := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	fmt.Printf("Array is sorted in %d swaps.\n", sort(a))
	fmt.Printf("First Element: %d\n", a[0])
	fmt.Printf("Last Element: %d\n", a[n-1])
}
