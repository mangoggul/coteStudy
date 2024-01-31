# 코테 스터디 1주차

## 요제푸스 순열 
원순열 개념 -> popleft 한거 바로 append

## two pointer 알고리즘 
첫번째를 start 마지막을 last <br/>
sum 과 찾는 것이 같다면 last -= 1 cnt += 1 <br/>
sum 이 찾는 것보다 작다면 start += 1 <br/>
sum 이 찾는 것보다 크다면 last -= 1

## 회전하는 큐 문제 
dq.index(num) <= len(dq)//2: 이런 방식 자주 사용될것 같다. 왼쪽, 오른쪽 비교할떄 len(dq)//2 랑 비교

## rotate 함수 
rotate(양수) : 안에 들어있는 수 만큼 오른쪽에 있는 걸 왼쪽으로 <br/>
1 2 3 -> 3 1 2 <br/>
rotate(음수) : 안에 들어있는 수 만큼 왼쪽에 있는 걸 오른쪽으로 

## DFS/BFS
![image](https://github.com/mangoggul/coteStudy/assets/102888719/f2c3cc41-82f3-4f67-a92c-0dea0a3a8f51)

![image](https://github.com/mangoggul/coteStudy/assets/102888719/a50eda03-2191-437d-a100-40e1e4e17c2d)

출처 : https://devuna.tistory.com/32

## 인접리스트 인접행렬
![image](https://github.com/mangoggul/coteStudy/assets/102888719/ee9e37cd-d197-4231-a2ed-f335822a18e4)
