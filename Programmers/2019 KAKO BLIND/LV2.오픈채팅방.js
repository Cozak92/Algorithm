 // 다른 사람풀이

// function solution(record) {
//     const userInfo = {};
//     const action = [];
//     const stateMapping = {
//         'Enter': '님이 들어왔습니다.',
//         'Leave': '님이 나갔습니다.'
//     }

//     record.forEach((v) => {
//         const [state, id, nick] = v.split(' ');

//         if(state !== "Change") {
//             action.push([state, id]);
//         }

//         if(nick) {
//             userInfo[id] = nick;
//         }
//     })

//     return action.map(([state, uid]) => {
//         return `${userInfo[uid]}${stateMapping[state]}`;    
//     })
// }

function solution(record) {
    //console.log(record)
    var answer = [];
    var order = [];
    let id = new Map();
    for (var i = 0; i < record.length; i++){
        var temp = record[i].split(" ")
        if ( temp.length > 2){
            id[temp[1]] = temp[2]
            
        }
        order.push([temp[0],temp[1]])
    }
    
    //console.log(id)
    for (var [o,name] of order){
        if (o === "Enter"){
            answer.push(id[name]+"님이 들어왔습니다.")
            
        }
        else if (o === "Leave"){
             answer.push(id[name]+"님이 나갔습니다.")
            
        }
    }
    return answer;
}