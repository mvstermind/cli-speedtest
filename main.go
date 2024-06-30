package main

import (
	"fmt"
	"os/exec"
)

// SpeedData containts string type beacuse python part returns formatted string with Mbps ms etc.
type SpeedData struct {
	DownloadSpeed string `json:"download_speed"`
	UploadSpeed   string `json:"upload_speed"`
	Ping          string `json:"ping"`
}

func main() {
	cmd := exec.Command("python3", "speed.py")
	output, err := cmd.Output()
	if err != nil {
		fmt.Println("error: ", err)
	}

	fmt.Println(string(output))
}
