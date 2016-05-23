
var numbers = [4, 7, 1, 9, 6, 5, 6, 9]
/*
let max: () -> (Int) = {
  numbers.sortInPlace(>)
  return numbers[0]
}
*/
let max = { () -> Int in
  numbers.sortInPlace(>)
  return numbers[0]
}

print(max())

print(max)
