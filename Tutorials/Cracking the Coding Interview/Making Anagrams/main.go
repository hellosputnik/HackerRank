package main

import (
	"bytes"
	"fmt"
	"math"
)

func getInput() string {
	var buffer string

	fmt.Scanf("%s\n", &buffer)

	return buffer
}

func Count(s string) map[rune]int {
	table := make(map[rune]int)

	for _, char := range s {
		table[char]++
	}

	return table
}

func Unique(s string) []byte {
	var buffer []byte

	for _, char := range s {
		if !bytes.ContainsAny(buffer, string(char)) {
			buffer = append(buffer, byte(char))
		}
	}

	return buffer
}

func main() {
	a := getInput()
	b := getInput()

	A := Count(a)
	B := Count(b)

	sum := 0.0

	for _, element := range Unique(a + b) {
		key := rune(element)
		sum += math.Abs(float64(A[key] - B[key]))
	}

	fmt.Println(sum)
}
