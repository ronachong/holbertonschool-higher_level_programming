//
//  EntitiesHelper.swift
//  TechCompanies
//
//  Created by Rona Chong on 5/27/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation


// EntitiesHelper is a helper class to populate the list of schools and list of tech companies.
class EntitiesHelper {
    
    // make two lists, one for schools, one for tech co.'s
    static var listOfSchool: [Entity]! = []
    static var listOfTechCompany: [Entity]! = []
    
    static func getSchools() -> [Entity]! {
        // if list of schools is empty, add Holberton
        if listOfSchool.count == 0 {
            listOfSchool.append(Entity(name: "Holberton", town: "San Francisco", imageName: "holberton", type: .School))
        }
        // return list
        return listOfSchool
    }
    
    static func getTechCompanies() -> [Entity]! {
        // if list of tech companies is empty, add the following companies
        if listOfTechCompany.count == 0 {
            listOfTechCompany.append(Entity(name: "Linkedin", town: "San Francisco", imageName: "linkedin", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Docker", town: "San Francisco", imageName: "docker", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Google", town: "Mountain View", imageName: "google", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Yahoo", town: "Sunnyvale", imageName: "yahoo", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Apple", town: "Cupertino", imageName: "apple", type: .TechCompany))
            listOfTechCompany.append(Entity(name: "Twitter", town: "San Francisco", imageName: "twitter", type: .TechCompany))
        }
        // return list
        return listOfTechCompany
    }
}