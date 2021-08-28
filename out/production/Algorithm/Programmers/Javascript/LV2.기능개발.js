function solution(progresses, speeds) {
    var answer = [];
    while (progresses.length){
        if (progresses[0] >= 100){
            var  cnt = 0
            for (var progresse of progresses ){
                if (progresse >= 100){
                    cnt += 1
                }
                else{                  
                    break
                }           
            }
            answer.push(cnt)

            for (var i = 0; i < cnt; i++){
                progresses.shift()
                speeds.shift()
            }
        }
        for (var i = 0; i < progresses.length; i++){
            progresses[i] += speeds[i]
        }
            
        
        
    }
    return answer;
}

console.log(solution([93, 30, 55],[1, 30, 5]))