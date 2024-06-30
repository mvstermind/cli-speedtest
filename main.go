package main

import (
	"github.com/mvstermind/cli-speedtest/tui"
)

// TODO: find a way to make this shit more performant
func main() {
	// speedData := py2go.UnmarshalJson()
	// fmt.Println("download speed: ", speedData.Ping)
	// fmt.Println("download speed: ", speedData.DownloadSpeed)
	tui.Run()
}
