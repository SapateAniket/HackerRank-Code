def solveMissing(n, m):
    n_cnt = [0] * 10
    m_cnt = [0] * 10
    offset = min(m)
     
    for ele in m:
        m_cnt[ele-offset] += 
     
    for ele in n:
        n_cnt[ele-offset] += 
     
    for idx in xrange(101):
        if m_cnt[idx] != n_cnt[idx]:
            print idx + offset,
     
     

    n = int(raw_input())
    arr = map(int, raw_input().split())
    m = int(raw_input())
    arr2 = map(int, raw_input().split())
    solveMissing(arr, arr2)