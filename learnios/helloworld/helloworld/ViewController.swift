//
//  ViewController.swift
//  helloworld
//
//  Created by Tze on 2018/10/5.
//  Copyright © 2018年 Tze. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    
    @IBOutlet weak var mylabel: UILabel!
    
    @IBAction func buttonpressed(_ sender: UIButton) {
        mylabel.text = "hello world"
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
       
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

