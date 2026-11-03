package main

import (
	"log"

	"github.com/labstack/echo/v4"
)

func main() {
	app := echo.New()
	app.GET("/", func(c echo.Context) error {
		return c.String(200, "echo bootstrap ok\n")
	})

	log.Fatal(app.Start(":8080"))
}
