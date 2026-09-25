clear all;
clc;

a=[2 1 5; 4 4 -4; 1 3 1];
%a=[ 1 2 -1; 2 1 -2; -3 1 1];
%a=[10 -7 0;-3 2 6;5 -1 5];
%A=a;
b=[ 3 3 -6]';
L=eye(3); % initialize L matrix
n=size(a,1);
for j=1:n-1
    [M,I]=max(abs(a(j:n,j)));
    I=I+j-1;
    if I~=j % condition for partial pivoting
        a([j, I], :) = a([I, j], :); % row swapping
    end
    for i=j+1:n
        mult=a(i,j)/a(j,j); % multiplication factor for elimination
        a(i,j)=mult;
        for k=j+1:n
            a(i,k)=a(i,k)-mult*a(j,k);
        end
    end
end

% extract the L and U matrices 
for i=1:n
    for j=1:n
        if i>j
            L(i,j)=a(i,j);
        else
            U(i,j)=a(i,j);
        end
    end
end

[l,u,p]=lu(A);

%solve for xi's
c=inv(L)*b;
x=inv(U)*c

