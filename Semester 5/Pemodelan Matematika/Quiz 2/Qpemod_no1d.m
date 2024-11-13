% Inisialisasi parameter awal
x0 = 1;
y0 = 2;
tspan = [0 10];

% Sistem persamaan diferensial
dydt = @(t, Y) [Y(2)^2 - Y(1)^2; Y(1) - Y(1) * Y(2)];

% Runge-Kutta 4 untuk menyelesaikan sistem nonlinier
[t, Y] = ode45(dydt, tspan, [x0, y0]);

% Menampilkan grafik
figure;
plot(t, Y(:,1), 'r', 'DisplayName', 'x(t) Nonlinier');
hold on;
plot(t, Y(:,2), 'b', 'DisplayName', 'y(t) Nonlinier');
xlabel('Waktu t');
ylabel('Nilai x dan y');
title('Grafik Penyelesaian Sistem Nonlinier dengan Runge-Kutta');
legend;
grid on;
hold off;