import re

_input = ["{}", "[{()}]", "{{[]}}[]", "{}}([])","{{{{{{{{{{{","}{{{}","{[]}"]

def sub_s(gh):
    try:
        r = []
        for i in list(gh):
            if i == "[" or i == "{" or i == "(":
                if len(r) == 0 or i == "(":
                    r.append(i)
                else:
                    r.append(i)
            else:
                r.pop()
        if r:
            return 0        

                

    except:
        return 0
    return 1



def solution(_input):
    answer = []
    for gh in _input:
        answer.append(sub_s(gh))

    return answer
    

print(solution(_input))


'''function solution(pars) {
    let answer = [];

    for(let par of pars) {
        let stack = [];
        let isRight = true;
        
        for(let str of par) {
            if('[' === str || '{' === str || '(' === str) {
                 if(('(' === str) || 0 === stack.length) {
                    stack.push(str);
                }else{
                    let stackLastChar = stack[stack.length - 1];
                    let condition = ('[' === str)? ('[' === stackLastChar) : ('[' === stackLastChar || '{' === stackLastChar);

                    if(condition) {
                        stack.push(str);
                    }else {
                        isRight = false;
                    }
                }
            }else {
                let standardChar = (']' === str)? '[' : ('}' === str)? '{' : '(';

                if(standardChar !== stack.pop())    
                    isRight = false;
            }

            if(!isRight)
                break;
        }

        answer.push(  
            (0 < stack.length)? 0 : (isRight)? 1 : 0
        );
    }

    return answer;
}'''