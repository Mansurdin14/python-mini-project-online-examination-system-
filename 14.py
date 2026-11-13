
print("ONLINE EXAMINATION SYSTEM")
naame=input("Enter your name:")
questions=[("capital of india?",["A.mumbai", "B.delhi","C.chennai", "D.kolkata"],"B"),
          ("which is a programming language?", ["A.python", "B.HTML", "C.css","D.all"],"D"),
          ("which is used for output in python?",["A. input()", "B.print()", "C.scan()", "D.read()"], "B"),
           ("which is national bird of india?", ["A.pigeon", "B.eagle", "C.peacock", "D.parrot"],"c"),
           ("which is the king of forest?", ["A.tiger", "B.lion", "C.fox", "D.rabbit"], "B") ]
score = 0
for q, options, ans in questions:
    print(q)
    for option in options:
        print(option)

    answer = input("Enter A/B/C/D: ").upper()
    while answer not in["A", "B","C", "D"]:
              answer = input("Invalid! Enter A/B/C/D:").upper()
    if answer == ans:
       score+=1
total= len(questions)
           
percentage = (score / total)*100
print("EXAM RESULT")
print("Total marks:", total)
print("obtained marks:", score)
print("Percentage:",percentage, "%")
                  
if percentage>= 60:
  print("Result: PASS")
else:
  print("Result: FAIL")
                          
              
