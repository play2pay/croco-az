package main

import (
	"io/ioutil"
	"math/rand"
	"os"
	"strconv"
	"testing"
	"time"
)

func TestLoadEnv(t *testing.T) {
	envTestFile := ".env.test"

	envKey := getNotExistedEnvironment()
	envValue := "some value from env"

	envKeyValuePair := envKey + "=" + envValue
	err := ioutil.WriteFile(envTestFile, []byte(envKeyValuePair), 0644)
	if err != nil {
		t.Error(err)
	}
	defer func() { _ = os.Remove(envTestFile) }()

	loadEnv(envTestFile)

	if os.Getenv(envKey) != envValue {
		t.Error("invalid")
	}
}

func getNotExistedEnvironment() string {
	var key string
	for key = getRandomEnvKey(); os.Getenv(key) != ""; {
		key = getRandomEnvKey()
	}
	return key
}

func getRandomEnvKey() string {
	rand.Seed(time.Now().Unix())
	return "TESTED_ENV_KEY" + strconv.FormatInt(time.Now().Unix(), 10) + strconv.Itoa(rand.Intn(1<<31))
}
