import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.gridspec as gridspec

# 读取数据
df = pd.read_csv('log.txt', sep='\s+', header=None,
                 names=['timestamp', 'x', 'y', 'z', 'roll', 'yaw'])

# 转换时间戳
start_time = df['timestamp'].iloc[0]
df['time_elapsed'] = (df['timestamp'] - start_time) / 1000.0

# 创建画布和子图
fig = plt.figure(figsize=(18, 12))
gs = gridspec.GridSpec(3, 3, height_ratios=[2, 1, 1], width_ratios=[1, 1, 1])

ax1 = fig.add_subplot(gs[0:2, 0:2], projection='3d')  # 3D轨迹图
ax2 = fig.add_subplot(gs[0, 2])                        # Roll角度图
ax3 = fig.add_subplot(gs[1, 2])                        # Yaw角度图
ax4 = fig.add_subplot(gs[2, 0])                        # X-T图
ax5 = fig.add_subplot(gs[2, 1])                        # Y-T图
ax6 = fig.add_subplot(gs[2, 2])                        # Z-T图

# 初始化图形
def init():
    # 3D轨迹图设置
    ax1.set_xlim((df['x'].min() - 0.5)*1000, (df['x'].max() + 0.5)*1000)
    ax1.set_ylim((df['y'].min() - 0.5)*1000, (df['y'].max() + 0.5)*1000)
    ax1.set_zlim((df['z'].min() - 0.5)*1000, (df['z'].max() + 0.5)*1000)
    ax1.set_xlabel('X (mm)')
    ax1.set_ylabel('Y (mm)')
    ax1.set_zlabel('Z (mm)')
    ax1.set_title('3D Trajectory')

    # Roll角度图设置
    ax2.set_xlim(0, df['time_elapsed'].max())
    ax2.set_ylim(df['roll'].min() - 0.5, df['roll'].max() + 0.5)
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Roll (rad)')
    ax2.set_title('Roll Angle')

    # Yaw角度图设置
    ax3.set_xlim(0, df['time_elapsed'].max())
    ax3.set_ylim(df['yaw'].min() - 0.5, df['yaw'].max() + 0.5)
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Yaw (rad)')
    ax3.set_title('Yaw Angle')

    # X-T图设置
    ax4.set_xlim(0, df['time_elapsed'].max())
    ax4.set_ylim((df['x'].min() - 0.5)*1000, (df['x'].max() + 0.5)*1000)
    ax4.set_xlabel('Time (s)')
    ax4.set_ylabel('X (mm)')
    ax4.set_title('X vs Time')

    # Y-T图设置
    ax5.set_xlim(0, df['time_elapsed'].max())
    ax5.set_ylim((df['y'].min() - 0.5)*1000, (df['y'].max() + 0.5)*1000)
    ax5.set_xlabel('Time (s)')
    ax5.set_ylabel('Y (mm)')
    ax5.set_title('Y vs Time')

    # Z-T图设置
    ax6.set_xlim(0, df['time_elapsed'].max())
    ax6.set_ylim((df['z'].min() - 0.5)*1000, (df['z'].max() + 0.5)*1000)
    ax6.set_xlabel('Time (s)')
    ax6.set_ylabel('Z (mm)')
    ax6.set_title('Z vs Time')

    return []

# 动态更新函数
def update(frame):
    # 清空所有子图
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    ax5.cla()
    ax6.cla()

    # 重新设置属性并绘制数据
    # 3D轨迹图
    ax1.set_xlim((df['x'].min() - 0.5)*1000, (df['x'].max() + 0.5)*1000)
    ax1.set_ylim((df['y'].min() - 0.5)*1000, (df['y'].max() + 0.5)*1000)
    ax1.set_zlim((df['z'].min() - 0.5)*1000, (df['z'].max() + 0.5)*1000)
    ax1.set_xlabel('X (mm)')
    ax1.set_ylabel('Y (mm)')
    ax1.set_zlabel('Z (mm)')
    ax1.set_title('3D Trajectory')
    ax1.scatter(df['x'][:frame+1]*1000, df['y'][:frame+1]*1000, df['z'][:frame+1]*1000,
                c=df['time_elapsed'][:frame+1], cmap='viridis', s=30)
    ax1.scatter(df['x'][frame]*1000, df['y'][frame]*1000, df['z'][frame]*1000, c='red', s=100)

    # Roll角度图
    ax2.set_xlim(0, df['time_elapsed'].max())
    ax2.set_ylim(df['roll'].min() - 0.5, df['roll'].max() + 0.5)
    ax2.set_xlabel('Time (s)')
    ax2.set_ylabel('Roll (rad)')
    ax2.set_title('Roll Angle')
    ax2.plot(df['time_elapsed'][:frame+1], df['roll'][:frame+1], 'b')

    # Yaw角度图
    ax3.set_xlim(0, df['time_elapsed'].max())
    ax3.set_ylim(df['yaw'].min() - 0.5, df['yaw'].max() + 0.5)
    ax3.set_xlabel('Time (s)')
    ax3.set_ylabel('Yaw (rad)')
    ax3.set_title('Yaw Angle')
    ax3.plot(df['time_elapsed'][:frame+1], df['yaw'][:frame+1], 'g')

    # X-T图
    ax4.set_xlim(0, df['time_elapsed'].max())
    ax4.set_ylim((df['x'].min() - 0.5)*1000, (df['x'].max() + 0.5)*1000)
    ax4.set_xlabel('Time (s)')
    ax4.set_ylabel('X (mm)')
    ax4.set_title('X vs Time')
    ax4.plot(df['time_elapsed'][:frame+1], df['x'][:frame+1]*1000, 'r')

    # Y-T图
    ax5.set_xlim(0, df['time_elapsed'].max())
    ax5.set_ylim((df['y'].min() - 0.5)*1000, (df['y'].max() + 0.5)*1000)
    ax5.set_xlabel('Time (s)')
    ax5.set_ylabel('Y (mm)')
    ax5.set_title('Y vs Time')
    ax5.plot(df['time_elapsed'][:frame+1], df['y'][:frame+1]*1000, 'g')

    # Z-T图
    ax6.set_xlim(0, df['time_elapsed'].max())
    ax6.set_ylim((df['z'].min() - 0.5)*1000, (df['z'].max() + 0.5)*1000)
    ax6.set_xlabel('Time (s)')
    ax6.set_ylabel('Z (mm)')
    ax6.set_title('Z vs Time')
    ax6.plot(df['time_elapsed'][:frame+1], df['z'][:frame+1]*1000, 'b')

    return []

# 创建动画
ani = FuncAnimation(fig, update, frames=len(df), init_func=init, blit=True, interval=50)

plt.tight_layout()
plt.show()