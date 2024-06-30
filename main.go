package main

import (
	"fmt"

	"github.com/mvstermind/cli-speedtest/py2go"
)

func main() {
	speedData := py2go.UnmarshalJson()
	fmt.Println("download speed: ", speedData.DownloadSpeed)
	fmt.Println("upload speed: ", speedData.UploadSpeed)
}
