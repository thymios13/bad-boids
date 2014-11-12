from numpy import power

def tmp_velocity(x_positions,y_positions,i,j):
    return power((x_positions[j]-x_positions[i]),2) + power((y_positions[j]-y_positions[i]),2)
