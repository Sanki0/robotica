import numpy as np
A= [ 2, 2, -1 ]
B= [7, 0, 24 ]

#find the angle between the vectors
A = np.array(A)
B = np.array(B)
print(A)
print(B)
print(np.dot(A,B))
print(np.linalg.norm(A))
print(np.linalg.norm(B))
print(np.linalg.norm(A)*np.linalg.norm(B))
print(np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B)))
print(np.arccos(np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B))))
print(np.degrees(np.arccos(np.dot(A,B)/(np.linalg.norm(A)*np.linalg.norm(B)))))
