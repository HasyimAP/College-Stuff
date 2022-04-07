x = [1 1 1 1 1 1]
n = [-2 -1 0 1 2 3]

stem(n,x)
axis([-5 6 -1 2])
title("x[n]=u[n+2]-u[n-4]")
xlabel("n")
ylabel("x[n]")
grid on