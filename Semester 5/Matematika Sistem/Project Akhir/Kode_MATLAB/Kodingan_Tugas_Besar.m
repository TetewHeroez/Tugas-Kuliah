clear
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

%simulasi PUPD
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

% Desain Kontrol
B = [0 ; 1];

%mencari nilai k
desired_poles = [-1 + 1j, -1 - 1j]; 
K_kontrol = place(A, B, desired_poles);
disp("nilai Kc:")
disp(K_kontrol);

% Matriks sistem dengan kontrol (closed-loop)
A_kontrol = A - B * K_kontrol;

% Waktu simulasi dan kondisi awal
t_span = [0 10];    % Simulasi 10 detik
x0 = [1; 0];      % Kondisi awal (deviasi sudut kecil dan kecepatan nol)

% Simulasi sistem tanpa kontrol
[t_tidak_kontrol, x_tidak_kontrol] = ode45(@(t, x) A * x, t_span, x0);

% Simulasi sistem dengan kontrol
[t_kontrol, x_kontrol] = ode45(@(t, x) A_kontrol * x, t_span, x0);

% Plot hasil simulasi
figure;

% Plot x1 (deviasi sudut) sebelum dan sesudah kontrol
subplot(2, 1, 1); % Grafik pertama
plot(t_tidak_kontrol, x_tidak_kontrol(:, 1), 'r', 'LineWidth', 1.5); hold on;
plot(t_kontrol, x_kontrol(:, 1), 'b', 'LineWidth', 1.5);
title('Deviasi Sudut(x1) Sebelum dan Sesudah Kontrol');
xlabel('Waktu (s)');
ylabel('x1 (Deviasi Sudut)');
legend('Tanpa Kontrol', 'Dengan Kontrol');
grid on;

% Plot x2 (kecepatan sudut) sebelum dan sesudah kontrol
subplot(2, 1, 2); % Grafik kedua
plot(t_tidak_kontrol, x_tidak_kontrol(:, 2), 'r', 'LineWidth', 1.5); hold on;
plot(t_kontrol, x_kontrol(:, 2), 'b', 'LineWidth', 1.5);
title('Kecepatan Sudut(x2) Sebelum dan Sesudah Kontrol');
xlabel('Waktu (s)');
ylabel('x2 (Kecepatan Sudut)');
legend('Tanpa Kontrol', 'Dengan Kontrol');
grid on;

%Desain Observer
desired_poles = [-1 + 1j, -1 - 1j]; 
C = [1 0];
K_observer = place(A, C', desired_poles)';
disp("nilai Ko:")
disp(K_observer);

%Simulasi Obersever
% Kondisi awal untuk observer
x_hat0 = [1; 0]; % Kondisi awal estimasi (diasumsikan tidak tahu state awal)
x_hat = x_hat0; % Inisialisasi estimasi
x_actual = x0;  % Kondisi awal sistem aktual

% Waktu simulasi
dt = 0.01; % Time step
t = 0:dt:10; % Waktu simulasi 10 detik

% Penyimpanan hasil
x_actual_history = [];
x_hat_history = [];
error_history = [];

% Simulasi observer
for i = 1:length(t)
    % Sistem aktual (tanpa kontrol untuk simulasi observer)
    x_dot_actual = A * x_actual;
    x_actual = x_actual + x_dot_actual * dt; % Euler Integration

    % Output aktual
    y = C * x_actual;

    % Sistem observer
    x_dot_hat = (A - K_observer * C) * x_hat + K_observer * y;
    x_hat = x_hat + x_dot_hat * dt; % Euler Integration

    % Simpan hasil
    x_actual_history = [x_actual_history, x_actual];
    x_hat_history = [x_hat_history, x_hat];
    error_history = [error_history, x_actual - x_hat];
end

% Plot hasil simulasi observer
figure;

% Plot x1 (state aktual vs estimasi)
subplot(3, 1, 1);
plot(t, x_actual_history(1, :), 'b', 'LineWidth', 1.5); hold on;
plot(t, x_hat_history(1, :), 'r--', 'LineWidth', 1.5);
title('State x_1 (Deviasi Sudut)');
xlabel('Waktu (s)');
ylabel('x_1');
legend('State Aktual', 'Estimasi Observer');
grid on;

% Plot x2 (state aktual vs estimasi)
subplot(3, 1, 2);
plot(t, x_actual_history(2, :), 'b', 'LineWidth', 1.5); hold on;
plot(t, x_hat_history(2, :), 'r--', 'LineWidth', 1.5);
title('State x_2 (Kecepatan Sudut)');
xlabel('Waktu (s)');
ylabel('x_2');
legend('State Aktual', 'Estimasi Observer');
grid on;

% Plot error estimasi
subplot(3, 1, 3);
plot(t, error_history(1, :), 'g', 'LineWidth', 1.5); hold on;
plot(t, error_history(2, :), 'm', 'LineWidth', 1.5);
title('Error Estimasi (x - x\_hat)');
xlabel('Waktu (s)');
ylabel('Error');
legend('Error x_1', 'Error x_2');
grid on;

% Hitung RMSE untuk masing-masing state
error_x1 = error_history(1, :);
error_x2 = error_history(2, :);

RMSE_x1 = sqrt(mean(error_x1.^2));
RMSE_x2 = sqrt(mean(error_x2.^2));

disp('RMSE untuk state x1 (Deviasi Sudut):');
disp(RMSE_x1);
disp('RMSE untuk state x2 (Kecepatan Sudut):');
disp(RMSE_x2);

% Kondisi awal untuk sistem aktual dan observer
x_actual = x0;      % Kondisi awal sistem aktual
x_hat = x_hat0;     % Kondisi awal observer

% Penyimpanan hasil
x_actual_history = [];
x_hat_history = [];
u_history = [];
error_history = [];

% Simulasi sistem dengan kontrol dan observer
for i = 1:length(t)
    % Masukan kontrol (feedback dari state aktual)
    u = -K_kontrol * x_hat; % Gunakan estimasi state untuk kontrol
    u_history = [u_history, u];

    % Sistem aktual
    x_dot_actual = A * x_actual + B * u;
    x_actual = x_actual + x_dot_actual * dt; % Euler Integration

    % Output aktual
    y = C * x_actual;

    % Sistem observer
    x_dot_hat = (A - K_observer * C) * x_hat + B * u + K_observer * y;
    x_hat = x_hat + x_dot_hat * dt; % Euler Integration

    % Simpan hasil
    x_actual_history = [x_actual_history, x_actual];
    x_hat_history = [x_hat_history, x_hat];
    error_history = [error_history, x_actual - x_hat];
end

% Plot hasil simulasi
figure;

% Plot x1 (state aktual vs estimasi)
subplot(4, 1, 1);
plot(t, x_actual_history(1, :), 'b', 'LineWidth', 1.5); hold on;
plot(t, x_hat_history(1, :), 'r--', 'LineWidth', 1.5);
title('State x_1 (Deviasi Sudut)');
xlabel('Waktu (s)');
ylabel('x_1');
legend('State Aktual', 'Estimasi Observer');
grid on;

% Plot x2 (state aktual vs estimasi)
subplot(4, 1, 2);
plot(t, x_actual_history(2, :), 'b', 'LineWidth', 1.5); hold on;
plot(t, x_hat_history(2, :), 'r--', 'LineWidth', 1.5);
title('State x_2 (Kecepatan Sudut)');
xlabel('Waktu (s)');
ylabel('x_2');
legend('State Aktual', 'Estimasi Observer');
grid on;

% Plot error estimasi
subplot(4, 1, 3);
plot(t, error_history(1, :), 'g', 'LineWidth', 1.5); hold on;
plot(t, error_history(2, :), 'm', 'LineWidth', 1.5);
title('Error Estimasi (x - x\_hat)');
xlabel('Waktu (s)');
ylabel('Error');
legend('Error x_1', 'Error x_2');
grid on;

% Plot kontrol u(t)
subplot(4, 1, 4);
plot(t, u_history, 'k', 'LineWidth', 1.5);
title('Input Kontrol u(t)');
xlabel('Waktu (s)');
ylabel('u(t)');
grid on;

% Hitung RMSE untuk masing-masing state
error_x1 = error_history(1, :);
error_x2 = error_history(2, :);

RMSE_x1 = sqrt(mean(error_x1.^2));
RMSE_x2 = sqrt(mean(error_x2.^2));

disp('RMSE untuk state x1 (Deviasi Sudut):');
disp(RMSE_x1);
disp('RMSE untuk state x2 (Kecepatan Sudut):');
disp(RMSE_x2);

