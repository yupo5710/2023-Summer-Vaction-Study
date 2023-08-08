n = input()
answer = ''
for i in range(len(n)):
    if 64 < ord(n[i]) < 91:
        answer += n[i]
        