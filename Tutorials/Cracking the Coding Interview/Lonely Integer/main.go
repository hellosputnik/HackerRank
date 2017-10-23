package main

import "fmt"

func getInput() (n int) {
	fmt.Scanf("%d", &n)
	return
}

func main() {
	n := getInput()

	result := 0

	for i := 0; i < n; i++ {
		result ^= getInput()
	}

	fmt.Println(result)
}
