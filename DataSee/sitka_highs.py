import csv
import matplotlib.pyplot as plt

filename = r'D:\1Data\python\world_fires_1_day.csv'

# 初始化列表来存储经度、纬度和火灾强度
longitudes = []
latitudes = []
brightness = []

with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

        # 遍历CSV文件的每一行
        for row in reader:
            if len(row) > 2:  # 确保行中有足够的数据
                longitude = float(row[0])  # 假设经度在第1列（索引0）
                latitude = float(row[1])   # 假设纬度在第2列（索引1）
                brightness_value = float(row[2])  # 假设火灾强度在第3列（索引2）
                longitudes.append(longitude)
                latitudes.append(latitude)
                brightness.append(brightness_value)

# 设置matplotlib样式
plt.style.use('seaborn-v0_8-deep')  # 使用seaborn样式

# 绘制散点图，使用经度和纬度作为坐标，火灾强度作为点的大小
fig, ax = plt.subplots()
sc = ax.scatter(longitudes, latitudes, c=brightness, cmap='inferno', alpha=0.6)

# 添加颜色条
plt.colorbar(sc, label='Fire Brightness')

ax.set_title("Global Fire Locations and Intensities", fontsize=24)
ax.set_xlabel("Longitude", fontsize=16)
ax.set_ylabel("Latitude", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

# 显示图形
plt.show()