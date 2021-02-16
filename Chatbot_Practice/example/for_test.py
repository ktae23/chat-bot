import sys

print(sys.argv) # 시스템 인자로 들어온 리스트 내용 출력
msg = sys.argv[1] # 'hello'
cnt = int(sys.argv[2]) # 10

for i in range(cnt):    # cnt 범위 만큼 반복
    print(i, msg)