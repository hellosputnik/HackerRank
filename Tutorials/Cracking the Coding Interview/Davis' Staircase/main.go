package main

import "fmt"

/*
func calculate(n int) int {
	if n < 0 {
		return 0
	}

	if n == 0 {
		return 1
	}

	return calculate(n-1) + calculate(n-2) + calculate(n-3)
}
*/

func main() {
	var s int

	fmt.Scan(&s)

	var table [36]int

	table[0] = 1
	table[1] = 2
	table[2] = 4

	// table[n] = table[n-1] + table[n-2] + table[n-3]
	for i := 3; i < 36; i++ {
		table[i] = table[i-1] + table[i-2] + table[i-3]
	}

	for i := 0; i < s; i++ {
		var n int

		fmt.Scan(&n)

		fmt.Println(table[n-1])
	}
}
