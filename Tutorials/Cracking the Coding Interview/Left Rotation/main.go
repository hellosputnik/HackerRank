package main

import "fmt"

func getInput() (int, int) {
	var n, d int

	fmt.Scanf("%d %d\n", &n, &d)

	return n, d
}

func main() {
	n, d := getInput()

	array := make([]int, n)

	for i := 0; i < n; i++ {
		fmt.Scanf("%d", &array[i])
	}

	left := array[d%n:]
	right := array[:d%n]

	// Define a function to cleanly print the array.
	print := func(array []int) {
		for _, element := range array {
			fmt.Printf("%d ", element)
		}
	}

	print(append(left, right...))
	fmt.Println()
}
