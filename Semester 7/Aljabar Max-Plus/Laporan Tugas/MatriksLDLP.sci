A=[1 -3 -3.5;
  -4 1 -4.5;
  -5 -6 1]
  
B=[2 -4 -4.5;
  -4 2 -5;
  -5 -8 2]
  
X= maxplusoplus(A,B)
Y= maxplusoplus(B,A)
  
disp(X)
disp(Y)
