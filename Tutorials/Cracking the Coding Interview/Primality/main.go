package main

import (
	"fmt"
	"math"
)

func IsPrime(integer int) string {
	if integer <= 1 {
		return "Not prime"
	}

	if integer == 2 || integer == 3 {
		return "Prime"
	}

	if integer%2 == 0 {
		return "Not prime"
	}

	root := int(math.Sqrt(float64(integer)))
	for i := 3; i <= root; i += 2 {
		if integer%i == 0 {
			return "Not prime"
		}
	}

	return "Prime"
}

func main() {
	var p int

	fmt.Scan(&p)

	for i := 0; i < p; i++ {
		var n int

		fmt.Scan(&n)

		fmt.Println(IsPrime(n))
	}
}
