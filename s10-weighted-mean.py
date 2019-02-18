no = input()
arr = map(int, raw_input().split())
weight = map(int, raw_input().split())
sm, wt_sm = 0, sum(weight)
for i in range(no):
    sm = sm + arr[i] * weight[i]
print '%.1f' % (sm / wt_sm )