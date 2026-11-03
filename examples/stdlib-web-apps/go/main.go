package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != "/" {
			http.NotFound(w, r)
			return
		}
		w.Header().Set("Content-Type", "text/html; charset=utf-8")
		fmt.Fprint(w, "<!doctype html><html lang='en'><title>Go</title><h1>Hello from Go!</h1></html>")
	})

	log.Printf("Listening on 0.0.0.0:%s", port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}
