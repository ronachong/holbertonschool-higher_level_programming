import Foundation

func longest_word(text: String) -> (String) {
  // split text str into array of words
  var spl_str = text.componentsSeparatedByString(" ")
  // use find_max as logic for sorting spl_str array
  spl_str.sortInPlace(find_max)
  // return longest word
  return spl_str[0]
}

func find_max(word1: String, _ word2: String) -> Bool {
  // returns True if word1 is longer than word2
  return word1.characters.count > word2.characters.count
}
