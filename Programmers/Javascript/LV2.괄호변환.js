const isCorret = function (braket){
    let stack = []
    for(let b of braket){
        if(b === "("){
            stack.push(b)
        }
        else{
            if(stack.length){
                stack.pop()
            }
            else{
                return false
            }
        }
    }
    return true

}

const makeBalanced = function(braket,n){
    let tu = ""
    let tv = ""
    let index = 0
    let leftBraket = 0
    let rightBraket = 0

    for (let c of braket){
        index++
        if(c ==="("){
            leftBraket++
        }
        else{
            rightBraket++
        }
        if(leftBraket === rightBraket){
            break
        }
    }

    tu = braket.slice(0,index)
    tv = braket.slice(index,n)

    return [tu,tv]

}

const makeBraket = function (braket){
    //console.log(braket)
    if(braket === ""){ return braket}
    let n = braket.length
    let temp = makeBalanced(braket,n)
    let u = temp[0]
    let v = temp[1]
 
    if(isCorret(u)){
        return u + makeBraket(v)
    }
    else{
        let temp = "(" + makeBraket(v) + ")"
        u = u.slice(1,(u.length)-1)

        for (let char of u) {
            if (char === "("){
                temp += ")"
            }    
            else{
                temp += "(";
            }    
        }
        return temp;
    }
}


function solution(p) {
    if(isCorret(p)){return p}
    return makeBraket(p)
}

console.log(solution("()))((()"))