package main

import (
	"github.com/joho/godotenv"
	"os"
)

func loadEnv(envFileName string) {
	_, err := os.Stat(envFileName)
	if !os.IsNotExist(err) {
		err = godotenv.Load(envFileName)
		if err != nil {
			log.Info("Unable to load .env")
		}
	}
}
