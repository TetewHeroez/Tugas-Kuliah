% Input nilai a dan b
a = 1; 
b = 2; 
t = linspace(0, 10, 2000); 

% Eigenvalue
lambda1 = (a + b*1i); % Lamda 1
lambda2 = (a - b*1i); % Lamda 2

% Fungsi Eksponensial Kompleks untuk Lamda 1
x1 = exp(real(lambda1) * t) .* cos(imag(lambda1) * t); 
y1 = exp(real(lambda1) * t) .* sin(imag(lambda1) * t); 

% Fungsi Eksponensial Kompleks untuk Lamda 2
x2 = exp(real(lambda2) * t) .* cos(imag(lambda2) * t); 
y2 = exp(real(lambda2) * t) .* sin(imag(lambda2) * t); 

% Plot
figure;
plot(x1, y1, 'b-', 'DisplayName', sprintf('\\lambda_1 = (%.1f + %.1fi) / 2', a, b)); % Plot untuk Lamda 1
hold on;
plot(x2, y2, 'r--', 'DisplayName', sprintf('\\lambda_2 = (%.1f - %.1fi) / 2', a, b)); % Plot untuk Lamda 2
xlabel('Re');
ylabel('Im');
legend show;
grid on;
axis equal;