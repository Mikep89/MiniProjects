package fizzbuzz

import (
	"fmt"
)

func fizzbuzz() {

	for a := 1; a <= 20; a++ {
		if a%5 == 0 && a%3 == 0 {
			fmt.Println("fizzbuzz")
		} else if a%3 == 0 {
			fmt.Println("fizz")
		} else if a%5 == 0 {
			fmt.Println("buzz")
		}
	}
}
