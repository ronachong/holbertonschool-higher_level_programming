
var numbers = [4, 7, 1, 9, 6, 5, 6, 9]

let max = numbers.reduce(numbers[0], combine: { (x, y) -> Int in
  if x > y {
    return x
  }
  return y
})

print(max)
