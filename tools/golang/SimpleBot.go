package main

import (
    "github.com/go-resty/resty/v2"
)

type SimpleBot struct {
    UserAgent string
}

func (simpleBot SimpleBot) fetch(url string) (error, int, string) {
    resp, err := resty.New().R().SetHeader("User-Agent", simpleBot.UserAgent).Get(url)
    if err != nil {
        return err, 500, ""
    }
    return nil, resp.StatusCode(), resp.String()
}
