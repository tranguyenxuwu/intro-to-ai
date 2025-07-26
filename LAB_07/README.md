# LAB 07 - Reinforcement Learning

## Mô tả

Lab này triển khai hai thuật toán AI cơ bản:

### 1. BFS Path Planning (Cell 1)

- **Chức năng**: Tìm đường đi ngắn nhất trong lưới 2D
- **Thuật toán**: Breadth-First Search (BFS)
- **Input**: Lưới 5x5 với chướng ngại vật, điểm start và goal
- **Output**: Đường đi tối ưu và visualization

### 2. Q-Learning (Cell 2)

- **Chức năng**: Học chính sách tối ưu thông qua thử-sai
- **Thuật toán**: Q-Learning với ε-greedy policy
- **Môi trường**: 16 states (4x4 grid), 4 actions
- **Output**: Q-table và heatmap giá trị học được
