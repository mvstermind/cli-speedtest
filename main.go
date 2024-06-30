package main

import (
	"encoding/json"
	"fmt"
	"os/exec"
)

// SpeedData containts string type beacuse python part returns formatted string with Mbps ms etc.
type SpeedData struct {
	DownloadSpeed string `json:"download_speed"`
	UploadSpeed   string `json:"upload_speed"`
	Ping          string `json:"ping"`
}

var Data SpeedData

func main() {
	// Run python file to get information from function doing speed test stuff.
	cmd := exec.Command("python3", "speed.py")
	output, err := cmd.Output()
	if err != nil {
		fmt.Println("error: ", err)
	}

	err = json.Unmarshal(output, &Data)
	if err != nil {
		fmt.Println("error: ", err)
	}
}
