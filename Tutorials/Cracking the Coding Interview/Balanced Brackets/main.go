package main

import "fmt"

// ==== Stack ==================================================================

type Stack struct {
	data []rune
	size int
}

func (s *Stack) push(char rune) {
	s.data = append(s.data, char)
	s.size++
}

func (s *Stack) pop() rune {
	popped := s.data[len(s.data)-1]
	s.data = s.data[0 : len(s.data)-1]
	s.size--

	return popped
}

// =============================================================================

func isBalanced(str string) string {
	stack := Stack{}

	for _, char := range str {
		switch char {
		case '(', '{', '[':
			stack.push(char)
		case ')':
			if stack.size == 0 || stack.pop() != '(' {
				return "NO"
			}
		case '}':
			if stack.size == 0 || stack.pop() != '{' {
				return "NO"
			}
		case ']':
			if stack.size == 0 || stack.pop() != '[' {
				return "NO"
			}
		}
	}

	if stack.size != 0 {
		return "NO"
	} else {
		return "YES"
	}
}

func main() {
	var n int

	fmt.Scan(&n)

	for i := 0; i < n; i++ {
		var str string

		fmt.Scan(&str)

		fmt.Println(isBalanced(str))
	}
}
