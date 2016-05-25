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

}

protocol Classify {
    func isStudent() -> Bool
}

class Mentor: Person, Classify {
    let subject: Subject?

    init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
        self.subject = subject
        super.init(first_name: first_name, last_name: last_name, age: age)
    }

    func isStudent() -> Bool {
        return false
    }

    func stringSubject() -> String {
        // returns a printable string of the subject
        return String("\(self.subject!)")
    }

}

class Student: Person, Classify {
    func isStudent() -> Bool {
        return true
    }
}

class School {
    var name: String
    var list_persons: [Person]

    init(name: String) {
        self.name = name
        self.list_persons = []
    }

    func addStudent(p: Person) -> Bool {
    // adds p to list_persons if p is a Student
        if p is Student {
            self.list_persons.append(p)
            return true
        }
        // else
        return false
    }

    func addMentor(p: Person) -> Bool {
    // adds p to list_persons if p is a Mentor
        if p is Mentor {
            self.list_persons.append(p)
            return true
        }
        // else
        return false
    }
}

enum Subject: Int {
    case Math = 1
    case English, French, History
}
