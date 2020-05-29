def func(actions, letters):
    undo, redo = [], []
    ans = []
    for i in range(len(actions)):
        if actions[i] == "insert":
            ans.append(letters[i])
            undo.append(["delete", letters[i]])
            
        if actions[i] == "delete":
            if len(ans) == 0:
                print("First operation cannot be delete")
            else:
                ans.pop()
                undo.append(["insert", ans[-1]])
             
        if actions[i] == "undo":
            if len(undo) == 0:
                print("First operation can not be undo")
            else:
                act = undo[-1][0]
                let = undo[-1][1]
                if act == "delete":
                    ans.pop()
                    undo.pop()
                    redo.append(["insert", let ])
                else:
                    ans.append(let)
                    undo.pop()
                    redo.append(["delete", let])
        if actions[i] == "redo":
            if len(redo) == 0:
                print("first do undo to redo")
            act = redo[-1][0]
            let = redo[-1][1]
            if act == "delete":
                ans.pop()
                redo.pop()
                undo.append(["insert", let])
            else:
                ans.append(let)
                redo.pop()
                undo.append(["delete", let])    

    print("".join(ans))
                


actions = ["insert", "insert", "insert", "insert", "undo", "insert"]
letters = ["a", "b", "c", "d", "", "e"]
#abce

func(actions, letters)