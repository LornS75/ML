import heapq

class  AStarPathFinding:
    def __init__(self, maze, start_pos, target_pos):
        self.maze = maze
        self.start_pos = start_pos
        self.target_pos = target_pos
        self.open_list = []         # the nodes we want to use  (待探索)
        self.closed_list = set()    # the nodes we already visited(已探索)
        self.came_from = {} # 回溯路径时专用

    # 曼哈顿距离当作启发函数
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def get_neighbors(self, pos):
        neighbors = []
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for d in directions:
            neighbor = ( pos[0] + d[0], pos[1] + d[1])
            if self.is_valid(neighbor):
                neighbors.append(neighbor)
        return neighbors
    
    def is_valid(self, pos):
        row, col = pos
        # 检查是否在边界内且该位置为1(有效路径)
        return 0 <= row < len(self.maze) and 0 <= col <len(self.maze[0]) and self.maze[row][col] == 1


    def find_path(self):

        # 初始化open_list(代价，position)
        heapq.heappush(self.open_list,(0, self.start_pos))

        # (x,y)到起点的实际代价
        g_score = {self.start_pos : 0}

        # f = 实际代价g + 估计代价h
        # 起点的f值即为启发函数值，因为g=0 --> f=0+h
        f_score = {self.start_pos : self.heuristic(self.start_pos, self.target_pos)}

        #(代价，节点)
        while self.open_list:
            # 获取open_list中f值最小的节点
            _, current = heapq.heappop(self.open_list)

            # 到达目标节点，回溯路径
            if current == self.target_pos:
                return self.reconstruct_path(current)
            
            # 加入已访问队列
            self.closed_list.add(current)

            # 遍历当前节点的邻居(没被访问过的)
            for neighbor in self.get_neighbors(current):
                if neighbor in self.closed_list:
                    continue
                
                # 计算从起点经过current到达neighbor的实际代价
                tentative_g_score = g_score[current] +1

                # 当前neighbor从未被探索  or
                # 此次neighbor的代价(从当前current+1得到的) < 该neighbor之前记录在案的代价
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # 更新came_from (neighbor:current)中插入记录
                    self.came_from[neighbor] = current
                    # 更新路径代价g
                    g_score[neighbor] = tentative_g_score
                    # 更新总代价f(g+h)
                    f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, self.target_pos)

                    # neighbor添加至待探索队列  open_list(代价，position)
                    heapq.heappush(self.open_list, (f_score[neighbor], neighbor))
                    
        return None

    # 回溯路径
    def reconstruct_path(self, current):

        # {    当前节点: 前序节点
        #     (0,1): (0,0),  # (0,1) 的前序节点是 (0,0)
        #     (1,1): (0,1),  # (1,1) 的前序节点是 (0,1)
        #     (1,2): (1,1)   # (1,2) 的前序节点是 (1,1)
        # }

        path = [current]    # 此步current即为target
        # 此时[(1,2)]

        while current in self.came_from: #检查是否有该键
            current = self.came_from[current]
            path.append(current)  
        # 此时[(1,2) (1,1) (0,1) (0,0)]

        path.reverse()
        # 此时[(0,0) (0,1) (1,1) (1,2)]
                
        return path


if __name__ == "__main__":

    maze = [
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1]
    ]

    start = (0,0)
    target = (7,7)

    A_star = AStarPathFinding(maze, start, target)
    path = A_star.find_path()

    if path:
        print("Path: ", path)
    else:
        print("No Path")








# class D2NetDetector(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.backbone = VGG16_conv4_3()
        
#     def forward(self, x):
#         # 1. 获取基础特征图
#         F = self.backbone(x)  # [B,512,H,W]
        
#         # 2. 计算α
#         exp_F = torch.exp(F)
#         sum_exp = F.avg_pool2d(exp_F, kernel_size=3, padding=1) * 9
#         alpha = exp_F / (sum_exp + 1e-6)
        
#         # 3. 计算β
#         beta = F / F.max(dim=1, keepdim=True)[0]
        
#         # 4. 计算γ
#         gamma = (alpha * beta).max(dim=1)[0]
        
#         # 5. 归一化得分
#         s = gamma / gamma.sum(dim=[1,2], keepdim=True)
        
#         return s  # 关键点得分图 [B,H,W]
