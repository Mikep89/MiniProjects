package main

import (
	"fmt"
)

func strings() {
	book := "The colour of magic"
	fmt.Println(book)

	fmt.Println(len(book))

	fmt.Printf("book[0] = %v (type %T)\n", book[0], book[0])

	// strings in go are immutable
	// book[0] = 116

	fmt.Println(book[4:11])

	fmt.Println(book[4:])
	fmt.Println(book[:4])
	fmt.Println("t" + book[1:])

	poem := `
	The road goes ever on
	Down from the door where it began
	...
	`

	fmt.Println(poem)
}
