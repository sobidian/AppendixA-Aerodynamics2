import math

def isentropic_properties(M):
    gamma = 1.4
    P0_P = (1+(gamma-1)/2*M**2)**(gamma/(gamma-1))
    T0_T = P0_P**((gamma-1)/gamma)
    rho0_rho = P0_P**(1/gamma)
    A_Astar = ((gamma+1)/2)**(-(gamma+1)/(2*(gamma-1)))*(1/M)*((1+(gamma-1)/2*M**2)**((gamma+1)/(2*(gamma-1))))

    return P0_P,T0_T,rho0_rho,A_Astar

print("{:^60}".format("ISENTROPIC FLOW PROPERTIES"))
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format("M","P0/P","T0/T","rho0/rho","A/A*"))
print("-"*70)

for M in [x/1000 for x in range(20,50001,20)]:
    P0_P,T0_T,rho0_rho,A_Astar = isentropic_properties(M)
    print("{:<15.2f}{:<15.2f}{:<15.2f}{:<15.2f}{:<15.2f}".format(M,P0_P,T0_T,rho0_rho,A_Astar))