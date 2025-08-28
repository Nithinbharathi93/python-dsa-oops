inheritance - a class can inherite attributes and method from another class 
helps in reusability and maintainbility 

multiple inheritance - inherite attr from more than one immediate parents
                        C(A, B)

multi-level inheritance - inherite from parents and grandparents
                        A(B) <- B(C) <- C

when we are trying to add multiple parents, the first parent has the most impact over the child 
If both Pred and Prey has action class, 
Fish(Predetor, Prey) => Fish.action => comes from Predetor
Fish(Prey, Predetor) => Fish.action => comes from Prey