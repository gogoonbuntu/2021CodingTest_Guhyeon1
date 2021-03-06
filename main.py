# N 은 맵 크기 NxN
# D 는 움직임 방향. LRUD 중 하나.
# 크기 밖으로 나가면 무시

def main ():
	N = int(input())
	print("N = ", N)
	D = list(input().split())
	print("D = ", D)
	dx = [0, 0, -1, 1]
	dy = [-1, 1, 0, 0]
	dir = ['L', 'R', 'U', 'D']
	x, y = 1, 1
	for move in D:
		print(move)
		nx = dx[dir.index(move)]
		ny = dy[dir.index(move)]
		if(x + nx >= 1 and y + ny >= 1):
			x += nx
			y += ny
		print("(%d, %d)", x, y) 

main()

# 방향에 주의할 것.