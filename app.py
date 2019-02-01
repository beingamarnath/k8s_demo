from flask import Flask
import numpy as np
from numba import vectorize
from timeit import default_timer as timer

@vectorize(["float32(float32,float32)"], target='cuda')
def Add(a, b):
  return a + b

def CPU_Add(a,b,c):
  for i in range(a.size):
      c[i] = a[i] + b[i]

app = Flask(__name__)


@app.route('/')
def hello():
    N = 32000000
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)
    c = np.zeros(N, dtype=np.float32)
    d = np.zeros(N, dtype=np.float32)
    start = timer()
    c = Add(A, B)
    duration = timer() - start
    cpustart = timer()
    CPU_Add(A, B, d)
    duration2 = timer() - cpustart
    print(duration)
    print("c[:5] = " + str(c[:5]))
    print("c[-5:] = " + str(c[-5:]))
    return "App Version: 1 <BR> GPU Time: " + str(duration) + "<BR> CPU Time: " +  str(duration2)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
