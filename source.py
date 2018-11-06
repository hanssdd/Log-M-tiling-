import numpy as np

B=matrix([[2,-1,-3],[-1,2,-1],[-1,-1,2]])
L1=(B.inverse())[0]
L2=(B.inverse())[1]
L3=(B.inverse())[2]

R1=matrix.identity(3)-matrix(3,3,[(B.transpose())[0],[0,0,0],[0,0,0]])
R2=matrix.identity(3)-matrix(3,3,[[0,0,0],(B.transpose())[1],[0,0,0]])
R3=matrix.identity(3)-matrix(3,3,[[0,0,0],[0,0,0],(B.transpose())[2]])

def P(v):
    p=vector([v[0]/v[2],v[1]/v[2]])
    return p

def tiling(matrices):
    draw=sum(line([P(A*L1),P(A*L2),P(A*L3),P(A*L1)]) for A in matrices)
    return draw

def colored_tiling(matrices):
    draw=sum(polygon([P(A*L1),P(A*L2),P(A*L3)],color="blue") for A in matrices)
    return draw

draw_these_lines=[matrix.identity(3),R1*R2,R1*R2*R1*R2,R1,R1*R2*R1,R1*R2*R1*R2*R1,R3]
draw_these_polygons=[matrix.identity(3),R1*R2,R1*R2*R1*R2]
draw_these3=[(R1*R2*R3)^i for i in [-4..4]]

(
    tiling(draw_these3)+
    tiling(draw_these_lines)+
     colored_tiling(draw_these_polygons)
).show(axes=false,aspect_ratio=1)
