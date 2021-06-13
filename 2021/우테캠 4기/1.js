function solution(weights,head2head){

    let Player = function(index,winRate,beats,weights) {
        this.index = index
        this.winRate = winRate
        this.beats = beats
        this.weights = weights
    }
    winRate = []
    beat = []
    players = []
    n = weights.length

    for(let match of head2head){
        let wins = 0
        for(let m of match){
            if(m === "W"){
                wins++
            }
        }
        winRate.push(wins/n)
    }

    for(let i = 0; i < n; i++){
        let b = 0
        for(let j = 0; j < n; j++){
            if(head2head[i][j] === "W"){
                if(weights[i] < weights[j]){
                    b++
                }
                
            }
        }
        beat.push(b)
    }

    for(let i=0; i < n; i++){
        players.push(new Player(i,winRate[i],beat[i],weights[i]) )
    }


    players.sort(function(a,b){
        if(a.winRate === b.winRate){
            if(a.beats === b.beats){
                if(a.weights === b.weights){
                    return a.index - b.index
                }
                else{
                    return a.weights - b.weights
                }
            }
            else{
                return b.beats - a.beats
            }
        }
        else{
            return b.winRate - a.winRate
        }
        
    })

    return players




}

solution([50,82,75,120],["NLWL","WNLL","LWNW","WWLN"])