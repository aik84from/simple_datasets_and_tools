package main

import (
    "log"
    "github.com/gammazero/workerpool"
)

func Worker(item string) {
    log.Println(item)
}

func SimpleWorkerPool(items []string, limit int) {
    wp := workerpool.New(limit)
    for _, item := range items {
        item := item
        wp.Submit(func() {
            Worker(item)
        })
    }
    wp.StopWait()
}
