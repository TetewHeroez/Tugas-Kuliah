% Desain Kontrol
B = [0 ; 1];

% Mencari nilai k
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
