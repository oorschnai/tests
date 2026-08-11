package main

import (
	"fmt"
	"net/http"
	"os"

	"github.com/labstack/echo/v4"
)

func main() {
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.HTML(http.StatusOK, "<h1>TimeWeb + Echo = ❤️</h1>")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8000"
	}

	if err := e.Start(fmt.Sprintf(":%s", port)); err != nil {
		e.Logger.Fatal(err)
	}
}
