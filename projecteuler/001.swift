#!/usr/bin/env swift

import Foundation

var sum = 0

for num in 1..<1000 {
    if num % 3 == 0 {
        sum += num
    } else if num % 5 == 0 {
        sum += num
    }
}

print(sum)
