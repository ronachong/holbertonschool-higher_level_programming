//
//  Entity.swift
//  TechCompanies
//
//  Created by Rona Chong on 5/27/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

// EntityType is an enum which enumerates different types for Entity instances.
enum EntityType: String {
    case None
    case School
    case TechCompany
}

// Entity is a class representing institutional entities to portray in a table view.
class Entity {
    private var name: String
    private var town: String
    private var imageName: String
    private var type: EntityType
    
    init (name: String, town: String, imageName: String, type: EntityType = .None) {
        self.name = name
        self.town = town
        self.imageName = imageName
        self.type = type
    }
}