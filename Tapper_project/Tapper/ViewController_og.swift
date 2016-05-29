//
//  ViewController.swift
//  Tapper
//
//  Created by Rona Chong on 5/25/16.
//  Copyright © 2016 Rona Chong. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var tapsToDo: Int? = 0
    var tapsDone: Int = 0
    
    // bkg
    @IBOutlet weak var imgBkg: UIImageView!
    
    // first screen elements
    @IBOutlet weak var imgTapper: UIImageView!
    @IBOutlet weak var btnPlay: UIButton!
    @IBOutlet weak var tfHowMany: UITextField!
    
    // second screen elements
    @IBOutlet weak var btnCoin: UIButton!
    @IBOutlet weak var lblTaps: UILabel!
    
    
    // ---- instance methods ----
    @IBAction func clickPlay(sender: AnyObject) {
        // when Play button is clicked, do the following:
        
        // check input in textfield
        if self.tfHowMany != nil && self.tfHowMany.text != "" {
            self.tapsToDo = Int(self.tfHowMany.text!)
            
            if self.tapsToDo != nil {
                // input was valid, proceed to next screen
                self.imgTapper.hidden = true
                self.btnPlay.hidden = true
                self.tfHowMany.hidden = true
                self.btnCoin.hidden = false
                self.lblTaps.hidden = false
            }
        }
    }
    
    @IBAction func clickCoin(sender: AnyObject) {
        // when Coin button is clicked, do the following:
        self.tapsDone += 1 // update tapsDone
        self.tapsToDo! -= 1 // update tapsToDo
        
        self.updateTapsLabel() // update taps done label
        
        if self.tapsToDo == 0 {
            self.goToPlayScrn()
        }
    }
    
        
    func updateTapsLabel() {
        self.lblTaps.text = String(tapsDone) + " Taps!"
    }
    
    
    func goToPlayScrn() {
        // ---- Initialize tap vars ----
        self.tapsToDo = nil
        self.tapsDone = 0
        
        // ---- Initialize attributes of view elements ----
        // make bkg visible
        self.imgBkg.hidden = false
        
        // make first screen visible
        self.imgTapper.hidden = false
        self.btnPlay.hidden = false
        self.tfHowMany.hidden = false
        
        self.tfHowMany.text = ""
        
        // make second screen invisible
        self.btnCoin.hidden = true
        self.lblTaps.hidden = true
        
        self.updateTapsLabel()
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        self.goToPlayScrn()
    }
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

