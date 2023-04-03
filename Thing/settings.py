import math


res = WIDTH, HEIGHT = 1600,900
FPS = 1200



playerPos = 1.5, 5
playerAngle = 0
playerSpeed = 0.004
playerRotSpeed = 0.002


FOV = math.pi / 3
halfFOV = FOV/2
numrays = WIDTH // 2
halfNumrays = numrays//2
deltaAngle = FOV/numrays
maxDepth = 20