// 최단 경로로 이동했을 때 (1->3 : 1, 1->4: 2.. 간선의 개수가 가장 많은 노드들)
// BFS로 모든 노드를 돌고, dist 저장

function solution(n, edge) {
  let answer = 0;
  const graph = Array.from(Array(n), () => []);

  edge.forEach((info) => {
    graph[info[0] - 1].push(info[1] - 1);
    graph[info[1] - 1].push(info[0] - 1);
  });

  let dist = Array(n).fill(0);
  let visited = Array(n).fill(false);

  let queue = [0];
  visited[0] = true;

  while (queue.length) {
    let node = queue.shift();

    for (adj of graph[node]) {
      if (!visited[adj]) {
        queue.push(adj);
        visited[adj] = true;
        dist[adj] = dist[node] + 1;
      }
    }
  }

  let max_num = Math.max(...dist);

  answer = dist.reduce((acc, cur) => {
    return acc + (cur === max_num);
  }, 0);

  return answer;
}
