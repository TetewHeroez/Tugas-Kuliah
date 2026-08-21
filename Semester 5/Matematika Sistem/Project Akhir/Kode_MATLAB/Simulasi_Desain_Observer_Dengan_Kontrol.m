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
