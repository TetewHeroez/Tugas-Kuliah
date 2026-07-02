import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os

os.makedirs('foto', exist_ok=True)

# 1. Newton Polygon
def generate_newton_polygon():
    fig, ax = plt.subplots(figsize=(6, 6))
    points = np.array([[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [0, 2]])
    hull = np.array([[0, 0], [2, 0], [0, 2], [0, 0]])
    
    ax.scatter(points[:, 0], points[:, 1], color='red', zorder=5, s=100, label='Monomial Exponents')
    ax.plot(hull[:, 0], hull[:, 1], color='blue', linewidth=2, label='Newton Polygon Boundary')
    ax.fill(hull[:, 0], hull[:, 1], color='blue', alpha=0.2)
    
    ax.plot([1, 1], [0, 1], color='black', linestyle='--')
    ax.plot([0, 1], [1, 1], color='black', linestyle='--')
    ax.plot([1, 0], [0, 1], color='black', linestyle='--')
    ax.plot([2, 0], [0, 1], color='black', linestyle='--')
    ax.plot([1, 1], [0, 2], color='black', linestyle='--')
    
    ax.set_xticks(np.arange(-1, 4, 1))
    ax.set_yticks(np.arange(-1, 4, 1))
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.set_title('Poligon Newton dan Triangulasi Tropikal')
    ax.set_xlabel('Pangkat $x_1$')
    ax.set_ylabel('Pangkat $x_2$')
    ax.legend()
    
    plt.savefig('foto/newton_polygon.png', dpi=300, bbox_inches='tight')
    plt.close()

# 2. Tropical Neural Network (Piecewise Affine ReLU)
def generate_tropical_nn():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    Z1 = np.maximum(0, X + Y)
    Z2 = np.maximum(0, X - Y)
    Z = np.maximum(Z1, Z2)
    
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.8)
    
    ax.plot(x, x, np.maximum(0, 2*x), color='red', linewidth=3, label='Tropical Hypersurface')
    ax.plot(x, -x, np.maximum(0, 0*x), color='red', linewidth=3)
    
    ax.set_title('Topologi Tropikal Jaringan Saraf Tiruan (ReLU)')
    ax.set_xlabel('$x_1$')
    ax.set_ylabel('$x_2$')
    ax.set_zlabel('Aktivasi $f(\mathbf{x})$')
    
    plt.savefig('foto/tropical_neural_network.png', dpi=300, bbox_inches='tight')
    plt.close()

# 3. Euler Angle / Kinematics
def generate_kinematics():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', label='$X_0$')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', label='$Y_0$')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', label='$Z_0$ (Sumbu Engsel)')
    
    theta = np.pi / 4
    Rz = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
    
    x1 = Rz @ np.array([1, 0, 0])
    y1 = Rz @ np.array([0, 1, 0])
    
    ax.quiver(0, 0, 0, x1[0], x1[1], x1[2], color='r', linestyle='--', label='$X_1$')
    ax.quiver(0, 0, 0, y1[0], y1[1], y1[2], color='g', linestyle='--', label='$Y_1$')
    
    t = np.linspace(0, theta, 50)
    ax.plot(0.5 * np.cos(t), 0.5 * np.sin(t), 0, color='k', linewidth=2)
    ax.text(0.55, 0.2, 0, r'$\theta$', fontsize=14)
    
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    ax.set_title('Transformasi Rotasi $SO(3)$ pada Engsel Origami')
    ax.legend()
    ax.set_axis_off()
    
    plt.savefig('foto/kinematics.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    generate_newton_polygon()
    generate_tropical_nn()
    generate_kinematics()
