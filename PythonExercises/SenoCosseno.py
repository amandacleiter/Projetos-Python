import math

an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tang = math.tan(math.radians(an))

print('O seno de {} é {:.2f}, \n o cosseno é {:.2f} \ne o tangente é {:.2f}'.format(an,seno,cos,tang))