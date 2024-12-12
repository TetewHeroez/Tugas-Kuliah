% MATLAB Code: Comparison of Non-linear Runge-Kutta and Linearized Solution
clc;
clear;

% Parameter dan kondisi awal
u1 = 3/4; 
u2 = 1/2;
h = 0.1; % langkah waktu
t_end = 5; % waktu akhir
t = 0:h:t_end; % vektor waktu

% Kondisi awal
x0 = 1; 
y0 = 2;

% Sistem Non-Linier: Runge-Kutta Orde 4
x_nl = zeros(size(t)); % solusi x non-linier
y_nl = zeros(size(t)); % solusi y non-linier
x_nl(1) = x0;
y_nl(1) = y0;

for i = 1:length(t)-1
    % f(x, y) = dx/dt
    f = @(x, y) (1 - u1)*y^2 - x^2;
    % g(x, y) = dy/dt
    g = @(x, y) x - u2*x*y;
    
    % Runge-Kutta 4 untuk x
    k1 = h * f(x_nl(i), y_nl(i));
    l1 = h * g(x_nl(i), y_nl(i));
    
    k2 = h * f(x_nl(i) + 0.5*k1, y_nl(i) + 0.5*l1);
    l2 = h * g(x_nl(i) + 0.5*k1, y_nl(i) + 0.5*l1);
    
    k3 = h * f(x_nl(i) + 0.5*k2, y_nl(i) + 0.5*l2);
    l3 = h * g(x_nl(i) + 0.5*k2, y_nl(i) + 0.5*l2);
    
    k4 = h * f(x_nl(i) + k3, y_nl(i) + l3);
    l4 = h * g(x_nl(i) + k3, y_nl(i) + l3);
    
    x_nl(i+1) = x_nl(i) + (1/6)*(k1 + 2*k2 + 2*k3 + k4);
    y_nl(i+1) = y_nl(i) + (1/6)*(l1 + 2*l2 + 2*l3 + l4);
end

% Sistem Linier: Solusi Analitik
A = [0, 1; -1, -u2];
eig_val = eig(A);
C1 = (y0 - x0)/2; % koefisien pertama
C2 = (y0 + x0)/2; % koefisien kedua

x_lin = C1 * exp(eig_val(1)*t) + C2 * exp(eig_val(2)*t);
y_lin = C1 * exp(eig_val(1)*t) - C2 * exp(eig_val(2)*t);

% Plot Hasil
figure;
hold on;
plot(t, x_nl, '--b', 'LineWidth', 2, 'DisplayName', '(x) Runge-Kutta');
plot(t, y_nl, '--r', 'LineWidth', 2, 'DisplayName', '(y) Runge-Kutta');
plot(t, x_lin, 'b', 'LineWidth', 2, 'DisplayName', '(x) Linier');
plot(t, y_lin, 'r', 'LineWidth', 2, 'DisplayName', '(y) Linier');
hold off;

% Tambahkan detail grafik
xlabel('Waktu (t)');
ylabel('Nilai');
title('Perbandingan Solusi Non-Linier (Runge-Kutta) dan Linier');
legend('Location', 'Best');
grid on;