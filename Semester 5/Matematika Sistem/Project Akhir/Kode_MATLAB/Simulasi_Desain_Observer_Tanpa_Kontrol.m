% Desain Observer
desired_poles = [-1 + 1j, -1 - 1j]; 
C = [1 0];
K_observer = place(A, C', desired_poles)';
disp("nilai Ko:")
disp(K_observer);

% Simulasi Observer
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

% Hitung RMSE untuk masing-masing state
error_x1 = error_history(1, :);
error_x2 = error_history(2, :);

RMSE_x1 = sqrt(mean(error_x1.^2));
RMSE_x2 = sqrt(mean(error_x2.^2));

disp('RMSE untuk state x1 (Deviasi Sudut):');
disp(RMSE_x1);
disp('RMSE untuk state x2 (Kecepatan Sudut):');
disp(RMSE_x2);