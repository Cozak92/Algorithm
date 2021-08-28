function solution(n,a,b)
{
    let answer = 1
    if(a%2){
            a++
    }
    if(b%2){
        b++
    }
    while(a !== b){
        answer += 1
        a = parseInt(a / 2)
        b = parseInt(b / 2)
        if(a%2){
            a++
        }
        if(b%2){
            b++
        }
        
    }
        
    return answer;
}