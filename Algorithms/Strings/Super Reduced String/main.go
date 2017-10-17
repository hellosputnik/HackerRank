package main

import (
	"bytes"
	"fmt"
)

func getInput() string {
	var cin string

	fmt.Scanf("%s\n", &cin)

	return cin
}

func superReduce(input string) string {
	// Create a buffer to hold the super reduced string.
	var buffer bytes.Buffer

	// Create an array of bytes from the string.
	aob := []byte(input)

	length := len(aob)
	for i := 0; i <= length - 1; i++ {
		if i != (length - 1) && aob[i] == aob[i + 1] {
			i++
		} else {
			buffer.WriteString(string(aob[i]))
		}
	}

	result := buffer.String()

	if result == input {
		return result
	} else {
		return superReduce(result)
	}
}

func main() {
	s := getInput()

	result := superReduce(s)

	if result != "" {
		fmt.Println(result)
	} else {
		fmt.Println("Empty String")
	}
}

