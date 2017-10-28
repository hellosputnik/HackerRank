package main

import (
	"fmt"
)

func Counter(strings []string) map[string]int {
	counter := make(map[string]int)

	for _, s := range strings {
		counter[s]++
	}

	return counter
}

func main() {
	var m, n int

	fmt.Scan(&m, &n)

	magazine := make([]string, m)
	note := make([]string, n)

	for i := 0; i < m; i++ {
		fmt.Scan(&magazine[i])
	}

	for i := 0; i < n; i++ {
		fmt.Scan(&note[i])
	}

	M := Counter(magazine)
	N := Counter(note)
	for _, word := range note {
		if M[word]-N[word] < 0 {
			fmt.Println("No")
			return
		}
	}

	fmt.Println("Yes")
}
