#!/usr/bin/env Rscript
args <- commandArgs()
path <- tail(args, 1)
output <- readLines(path)
write(output, "")
