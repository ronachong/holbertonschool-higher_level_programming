//
//  TechCompaniesHelper.swift
//  SiliconValleyCompanies
//
//  Created by Rona Chong on 5/26/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import Foundation

class TechCompaniesHelper {
    static var companies: [String] = ["Holberton", "LinkedIn", "Docker", "Google", "Yahoo", "Apple"]
    
    init() {
     // since companies is static var, it doesn't need to be initiated here?
    }
    
    static func getTechCompanies() -> [String] {
        return self.companies
    }
}
