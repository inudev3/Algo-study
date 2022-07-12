function solution(board) {
    const dx = [-1,1,0,0]
    const dy = [0,0,-1,1]
    let answer=10000000000;
    const cost = new Array(board.length).fill(0).map(()=>new Array(board[0].length).fill(answer))
    const queue = []
    queue.push([0,0, 0, -1]) //x,y,cost,dir
    while(queue.length){
        const [x,y,pay,dir] = queue.shift();
        if(x==board.length-1 &&y==board.length-1){
            answer = Math.min(answer,cost[x][y]);
            continue;
        }
        for(let i=0; i<4; i++){
            let nx= x+dx[i];
            let ny = y+dy[i];
            if(nx<0 || nx>=board.length || ny<0 || ny>=board.length)continue;
            if(board[nx][ny]==1)continue;
            let newPay;
            if(dir==-1 || dir==i)newPay = pay+100; //이전 방향이 다음 방향과 같거나 시작점(-1)이라면
            else newPay = pay+600; //방향이 다르다면
            if(cost[nx][ny]>newPay){
                cost[nx][ny] = newPay
                queue.push([nx,ny,newPay,i])
                console.log(queue)
            }

        }

    }
    return answer
}
console.log(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))