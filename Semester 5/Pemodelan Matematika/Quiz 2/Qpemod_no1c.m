% Parameter waktu
t = linspace(0, 2, 100);  % Rentang waktu dari 0 hingga 2, dengan 100 titik data

% Solusi linier yang diperoleh dari pelinearan di titik (-1,1)
x_t = 5 * exp(2 * t) - 4 * exp(t);
y_t = 2 * exp(t);

% Membuat grafik
figure;
plot(t, x_t, 'r', 'LineWidth', 1.5);  % Grafik x(t) dalam warna merah
hold on;
plot(t, y_t, 'b', 'LineWidth', 1.5);  % Grafik y(t) dalam warna biru
hold off;

% Memberikan label dan judul
xlabel('Waktu, t');
ylabel('Nilai x(t) dan y(t)');
title('Grafik Solusi Linier dari Sistem Pelinearan di Titik (-1,1)');
legend('x(t) = 5e^{2t} - 4e^{t}', 'y(t) = 2e^{t}');
grid on;
