package main

import (
	"bufio"
	"encoding/hex"
	"fmt"
	"os"
	"strings"

	"github.com/fatih/color"
)

/*
import (
	"bufio"
	"encoding/hex"
	"fmt"
	"os"
	"strings"
)*/

func FUN_03104() {
	FUN_06358 := []string{"79", "6f", "75", "2d", "0a", "73", "74", "61", "79", "2d", "0a", "69", "6e", "2d", "0a", "57", "6f", "6e", "64", "65", "72", "6c", "61", "6e", "64", "2d", "0a", "61", "6e", "64", "2d", "0a", "49", "2d", "0a", "73", "68", "6f", "77", "2d", "0a", "79", "6f", "75", "2d", "0a", "68", "6f", "77", "2d", "0a", "64", "65", "65", "70", "2d", "0a", "74", "68", "65", "2d", "0a", "72", "61", "62", "62", "69", "74", "2d", "0a", "68", "6f", "6c", "65", "2d", "0a", "67", "6f", "65", "73"}
	//fmt.Println(FUN_06358)
	for _, __init__ := range FUN_06358 {
		bs, err := hex.DecodeString(__init__)
		if err != nil {
			panic(err)
		}
		fmt.Println(string(bs))
	}
}

func FUN_00123() {
	FUN_0666 := []string{"54", "47", "32", "32", "7b", "63", "34", "6e", "5f", "79", "30", "75", "5f", "70", "34", "73", "73", "5f", "6d", "33", "5f", "74", "68", "33", "5f", "73", "34", "6c", "74", "7d"}
	//fmt.Println(FUN_0666)
	for _, __init__ := range FUN_0666 {
		bs, err := hex.DecodeString(__init__)
		if err != nil {
			panic(err)
		}
		fmt.Println(string(bs))
	}
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	color.Magenta("What is the secret Phrase?")
	fmt.Println("-->")
	FUN_06660, _ := reader.ReadString('\n')
	FUN_06660 = strings.Replace(FUN_06660, "\n", "", -1)

	if strings.Compare("you-stay-in-Wonderland-and-I-show-you-how-deep-the-rabbit-hole-goes", FUN_06660) == 0 {
		FUN_40214()
	} else {
		color.Red("You will be reported, \nGaia will not be happy...")
	}
}

func FUN_40214() {
	FUN_00123()
}
