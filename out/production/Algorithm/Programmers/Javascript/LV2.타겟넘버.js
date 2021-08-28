function solution(numbers, target) {
    var answer = 0;
    const n = numbers.length

    function dfs(index,k){
        if ( k < 0){
            return 0
        }
        if (index === n){
            if (k === target){
                answer++
                return 0
            }
            else{
                return 0
            }
        }
            dfs(index + 1,k + numbers[i])
            dfs(index + 1,k - numbers[i])

    }
    dfs(0,0)
    return answer;
}