package main

import (
	"fmt"
	"log"
	"os"
)

func check(e error) {
	if e != nil {
		log.Fatal(e)
	}
}

func main() {

	fmt.Println("Advent of Code Day 1")

	dat, err := os.ReadFile("test_case.txt")
	check(err)

	fmt.Println(string(dat))

}
