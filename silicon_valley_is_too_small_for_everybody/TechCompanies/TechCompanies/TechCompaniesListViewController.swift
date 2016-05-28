//
//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Rona Chong on 5/27/16.
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class TechCompaniesListViewController: UITableViewController {

    // set class attributes (list of schools, and list of tech companies)
    var schoolList: [Entity]!
    var techCompanyList: [Entity]!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        techCompanyList = EntitiesHelper.getTechCompanies()
        schoolList = EntitiesHelper.getSchools()
        
        // Uncomment the following line to preserve selection between presentations
        // self.clearsSelectionOnViewWillAppear = false

        // Uncomment the following line to display an Edit button in the navigation bar for this view controller.
        // self.navigationItem.rightBarButtonItem = self.editButtonItem()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    // MARK: - Table view data source

    override func numberOfSectionsInTableView(tableView: UITableView) -> Int {
        // return the number of sections
        return 2
    }

    override func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        // return the number of rows
        
        // for tech companies (arbitrarily sxn 0)
        if section == 0 {
            // return # of companies as # of rows
            print(techCompanyList.count)
            return techCompanyList.count
        }
        
        // # for schools sxn (arbitrarily sxn 1)
        else {
            // return # of schools as # of rows
            return schoolList.count
        }
    }

    override func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {
        // return title for section
        if section == 0 {
            return "Tech Companies"
        }
        
        else {
            return "Schools"
        }
    }
    
    override func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCellWithIdentifier("techCell", forIndexPath: indexPath)
        print(String(indexPath))
        // Configure the cell...
        // for companies sxn
        if indexPath.section == 0 {
            cell.textLabel?.text = techCompanyList[indexPath.row].name
            cell.detailTextLabel?.text = "I love working"
            
        }
        
        // for schools sxn
        else if indexPath.section == 1 {
            cell.textLabel?.text = schoolList[indexPath.row].name
            cell.detailTextLabel?.text = "I love studying"
        }
        
        return cell
    }

    /*
    // Override to support conditional editing of the table view.
    override func tableView(tableView: UITableView, canEditRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the specified item to be editable.
        return true
    }
    */

    /*
    // Override to support editing the table view.
    override func tableView(tableView: UITableView, commitEditingStyle editingStyle: UITableViewCellEditingStyle, forRowAtIndexPath indexPath: NSIndexPath) {
        if editingStyle == .Delete {
            // Delete the row from the data source
            tableView.deleteRowsAtIndexPaths([indexPath], withRowAnimation: .Fade)
        } else if editingStyle == .Insert {
            // Create a new instance of the appropriate class, insert it into the array, and add a new row to the table view
        }    
    }
    */

    /*
    // Override to support rearranging the table view.
    override func tableView(tableView: UITableView, moveRowAtIndexPath fromIndexPath: NSIndexPath, toIndexPath: NSIndexPath) {

    }
    */

    /*
    // Override to support conditional rearranging of the table view.
    override func tableView(tableView: UITableView, canMoveRowAtIndexPath indexPath: NSIndexPath) -> Bool {
        // Return false if you do not want the item to be re-orderable.
        return true
    }
    */

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
