func is_palindrome(s: String) -> Bool {
     if s == String(s.characters.reverse()) {
     	return true
	}

	return false
}