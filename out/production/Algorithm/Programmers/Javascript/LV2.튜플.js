function solution(s) {
    let set = new Set();
    let answer = []
    temp = s.substring(1,s.length-2)
    console.log(temp)
    temp = temp.split("},")
            .map(str=>str.substring(1).split(","))
    console.log(temp)
    

    

    temp.sort((x,y)=>x.length-y.length)
    
    for(let num of temp){
        
        for(let x of num){
            set.add(x)
        }
        
    }

    for(let e of set){
        answer.push(parseInt(e))
    }
    return answer
}


console.log(solution("{{20,111},{111}}"))


// function solution(s) {
//     const subsets = s.substring(1, s.length-2).split('},')
//     	.map(str=>str.substring(1).split(',')
//         .map(v=>Number(v)));
 
//     subsets.sort((a, b) => a.length - b.length);
 
//     const ans = subsets.reduce((acc, subset) => {
//         const value = subset.filter(v => !acc.includes(v))[0];
//         acc.push(value);
//         return acc;
//     }, []);
    
//     return ans;
// }