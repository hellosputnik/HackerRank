package main

import "fmt"

func getInput() string {
	var buffer string

	fmt.Scanf("%s\n", &buffer)

	return buffer
}

func f(X string) int {
	y := 0

	array := []byte(X)
	for i := 0; i < len(array); i += 3 {
		if array[i + 0] != 'S' {
			y++
		}
		if array[i + 1] != 'O' {
			y++
		}
		if array[i + 2] != 'S' {
			y++
		}
	}

	return y
}

func main() {
	S := getInput()

	fmt.Println(f(S))
}
