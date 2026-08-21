g = 9.81;
L = 1;

A = [0 1; -(g/L) 0];
eig_A = eig(A);
disp("Nilai Eigen Vektor A yaitu:");
disp(eig_A)
[V, D] = eig(A);
disp("Vektor Eigen:");
disp(V)
disp("Matriks Diagonal:");
disp(D)

% Membentuk solusi umum
syms t c1 c2
x_general = c1 * exp(D(1,1) * t) * V(:,1) + c2 * exp(D(2,2) * t) * V(:,2);

disp('Penyelesaian umum x(t):');
disp(x_general);

% Kondisi awal (x1(0) = 1, x2(0) = 0)
x1_0 = 1;   % Nilai awal untuk x1
x2_0 = 0;   % Nilai awal untuk x2

% Matriks eigenvektor
v1 = V(:,1);
v2 = V(:,2);

% Sistem persamaan untuk mencari c1 dan c2
syms c1 c2
eqns = [c1 * v1(1) + c2 * v2(1) == x1_0, ...
        c1 * v1(2) + c2 * v2(2) == x2_0];
sol = solve(eqns, [c1, c2]);
c1 = double(sol.c1);
c2 = double(sol.c2);

disp('Nilai c1 dan c2:');
disp(['c1 = ', num2str(c1)]);
disp(['c2 = ', num2str(c2)]);

% Rentang waktu
t = linspace(0, 10, 100);

% Eigenvalue
lambda1 = D(1,1);
lambda2 = D(2,2);

% Solusi x1(t) dan x2(t)
x1 = c1 * exp(lambda1 * t) * v1(1) + c2 * exp(lambda2 * t) * v2(1);
x2 = c1 * exp(lambda1 * t) * v1(2) + c2 * exp(lambda2 * t) * v2(2);

% Plot hasil
figure;
plot(t, x1, 'b', 'LineWidth', 2); hold on; 
plot(t, x2, 'r', 'LineWidth', 2); 
title('Grafik x_1(t) dan x_2(t)'); 
xlabel('Waktu (t)'); 
ylabel('x_1(t), x_2(t)'); 
legend('x_1(t)', 'x_2(t)'); 
grid on; 
hold off; 
