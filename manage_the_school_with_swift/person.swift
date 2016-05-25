class Person {
    var first_name: String
    var last_name: String
    var age: Int

    init (first_name: String, last_name: String, age: Int) {
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }

    func fullName() -> String {
        return self.first_name + " " + self.last_name
    }

    func isStudent() -> Bool {
        return false
    }
}

class Mentor: Person {
    override func isStudent() -> Bool {
        return false
    }
}

class Student: Person {
    override func isStudent() -> Bool {
        return true
    }
}

enum Subject: Int {
    case Math = 1
    case English, French, History
}
