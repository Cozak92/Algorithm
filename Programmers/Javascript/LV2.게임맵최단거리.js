dx = [0,0,1,-1]
dy = [1,-1,0,0]
const bfs = function(n,m,maps){
    let nx,ny;
    let q = []
    let isVisited = Array.from(Array(n), () => Array(m).fill(false))
    q.push([0,0,1])
    isVisited[0][0] = true
    let ans = Number.MAX_VALUE

    while(q.length){
        temp = q.shift()
        x = temp[0]
        y = temp[1]
        
        dist = temp[2]
        if(x === n - 1 && y === m -1){

            ans = Math.min(ans,dist)
        }

        for(let i = 0; i < 4; i++){
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(0 <= nx && nx < n && 0 <= ny && ny < m){
                if(isVisited[nx][ny] === false && maps[nx][ny] === 1){
                    isVisited[nx][ny] = true
                    console.log(nx,ny)
                    q.push([nx,ny,dist+1])


                }
            }
        }
        
    }
    return ans
}

function solution(maps) {
    let n = maps.length
    let m = maps[0].length
    var answer = 0;

    answer = bfs(n,m,maps)
    if(answer === Number.MAX_VALUE){
        return -1
    }
    return answer
}

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])