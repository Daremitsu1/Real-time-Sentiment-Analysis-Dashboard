package main

import (
	"fmt"
	"net/http"
	"log"
	"encoding/json"
)

func receiveDataHandler(w http.ResponseWriter, r *http.Request) {
	// Handle incoming data
}

func sendAnalyzedDataHandler(w http.ResponseWriter, r *http.Request) {
	// Sample data
	data := map[string]interface{}{
		"time":           "2024-02-17 12:00:00",
		"sentimentScore": 0.75,
	}

	// Convert data to JSON
	response, err := json.Marshal(data)
	if err != nil {
		log.Println("Error:", err)
		http.Error(w, "Internal server error", http.StatusInternalServerError)
		return
	}

	// Set response header
	w.Header().Set("Content-Type", "application/json")

	// Send JSON response
	w.Write(response)
}

func main() {
	// Define endpoints
	http.HandleFunc("/receive-data", receiveDataHandler)
	http.HandleFunc("/send-analyzed-data", sendAnalyzedDataHandler)

	// Start server
	fmt.Println("Server running on :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
