var fruitDict:[String:String] = ["red":"apple","yellow":"banana","green":"mango"]
fruitDict["red"]
fruitDict["yellow"]
fruitDict["green"] = "watermelon"
fruitDict.updateValue("kiwi", forKey: "green")
fruitDict["green"]

fruitDict["orange"] = "orange"
fruitDict.updateValue("peach", forKey: "pink")
fruitDict

fruitDict["red"] = nil
fruitDict

fruitDict.removeValue(forKey: "yellow")
var score = ["English": 90, "chinese": 95, "sport" : 80]
score["chinese"]

score["English"] = 70
score
