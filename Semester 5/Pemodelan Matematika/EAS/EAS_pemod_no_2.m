% Parameter awal
tspan = [0 10];         % Interval waktu
x0 = 1;                 % Nilai awal x
y0 = 1;                 % Nilai awal y
lambda10 = 0;           % Nilai awal lambda_1
lambda20 = 0;           % Nilai awal lambda_2
init = [x0, y0, lambda10, lambda20]; 

% Sistem persamaan diferensial
[t, sol] = ode45(@(t, z) odefun(t, z), tspan, init);

% Ekstraksi hasil
x = sol(:, 1);
y = sol(:, 2);
lambda1 = sol(:, 3);
lambda2 = sol(:, 4);

% Hitung kontrol optimal
u1 = max(0, min(1, lambda1 .* y.^2));
u2 = max(0, min(1, lambda2 .* x .* y));

% Grafik pertama: x(t) dan y(t)
figure;
plot(t, x, 'b-', 'LineWidth', 1.5, 'DisplayName', 'x(t)');
hold on;
plot(t, y, 'r--', 'LineWidth', 1.5, 'DisplayName', 'y(t)');
hold off;
xlabel('Time');
ylabel('Value');
title('Variabel state x(t) dan y(t)');
legend('show', 'Location', 'best');
grid on;

% Tambahkan margin pada interval vertikal
ylim_min = min([x; y]);
ylim_max = max([x; y]);
margin = 0.2 * (ylim_max - ylim_min); % 10% margin
ylim([ylim_min - margin, ylim_max + margin]);

% Grafik kedua: u1(t) dan u2(t)
figure;
plot(t, u1, 'g-.', 'LineWidth', 1.5, 'DisplayName', 'u_1(t)');
hold on;
plot(t, u2, 'm:', 'LineWidth', 1.5, 'DisplayName', 'u_2(t)');
hold off;
xlabel('Time');
ylabel('Value');
title('Variabel kontrol u_1(t) dan u_2(t)');
legend('show', 'Location', 'best');
grid on;

% Tambahkan margin pada interval vertikal
ylim_min = min([u1; u2]);
ylim_max = max([u1; u2]);
margin = 0.1 * (ylim_max - ylim_min); % 10% margin
ylim([ylim_min - margin, ylim_max + margin]);

% Fungsi sistem persamaan diferensial
function dzdt = odefun(~, z)
    % Variabel
    x = z(1);
    y = z(2);
    lambda1 = z(3);
    lambda2 = z(4);

    % Kontrol optimal
    u1 = max(0, min(1, lambda1 * y^2));
    u2 = max(0, min(1, lambda2 * x * y));

    % Sistem persamaan diferensial
    dxdt = (1-u1)*y^2 - x^2;
    dydt = x - u2*x*y;
    dlambda1dt = -1 + 2*lambda1*x - lambda2*(1 - u2*y);
    dlambda2dt = -1 - 2*lambda1*(1 - u1)*y + lambda2*u2*x;

    % Output
    dzdt = [dxdt; dydt; dlambda1dt; dlambda2dt];
end
