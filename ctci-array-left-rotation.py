def array_left_rotation(a, n, k):
  x = a[k:] + a[0:k]
  return x 

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
