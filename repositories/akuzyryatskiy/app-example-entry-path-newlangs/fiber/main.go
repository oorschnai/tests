package main

import (
	"fmt"
	"os"

	"github.com/gofiber/fiber/v2"
)

func main() {
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.Type("html").SendString("<h1>TimeWeb + Fiber = ❤️</h1>")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8000"
	}

	if err := app.Listen(fmt.Sprintf(":%s", port)); err != nil {
		panic("failed to start Fiber server: " + err.Error())
	}
}
