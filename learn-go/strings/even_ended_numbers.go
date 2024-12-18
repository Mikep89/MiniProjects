package main

import (
	"fmt"
)

func main() {
	even_count := 0

	for i := 1000; i <= 9999; i++ {
		for b := i; b <= 9999; b++ {
			n := i * b
			number_str := fmt.Sprintf("%d", n)

			if number_str[0] == number_str[len(number_str)-1] {
				even_count++
			}
		}

	}
	fmt.Printf("there were %d even ended numbers\n", even_count)
}
