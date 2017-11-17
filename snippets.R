#Euler
f <- function(x) exp((0+1i)*x)
x <- seq(0, 2*pi, pi/20)
plot(f(x))

f.2 <- function(x) exp(x)
z <- complex(real=1, imaginary=x)
plot(f.2(z))


#read data and plot histogram
ce = read.table("data")
we = ce[,1]
we <- as.numeric(we)
hist(we)
