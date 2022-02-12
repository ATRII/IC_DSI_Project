# IC_DSI_Project
Team [Data Hunter!!]'s Repository

## 使用手册（展示人员、验收人员必看）：

### 1. 克隆项目
将仓库克隆（clone）到本地文件夹

### 2. 搭建本地服务器
在项目的web文件夹下建立本地服务器

具体操作：打开终端，输入
```
cd web文件夹的位置
python -m http.server
```
终端记得不要关掉
### 3. 开始调试html
如本地装有VSCode可以直接用VSCode打开项目文件夹，装上Chrome拓展后即可直接在调试->open map.html（调试已经配置好）

如果没有VSCode，在浏览器（最好是Chrome）中输入
```
localhost:8000
```
这时候会显示这个目录下的文件，点击map.html即可
### 4. 如果想要调试ipynb
ipynb需要安装jupyter内核，相对麻烦，项目会每次将运行完的ipynb上传，想要调试又不想安装可以试试在线jupyter notebook
## Dataset: 
data scientist salary(.csv under Project_salary/data/, about 3MB)

## Objective: 
?

## Language:

### -Python (primary, in Jupyter Notebook)

#### python packages needed:

pandas; sklearn; pycaret; seaborn; matplotlib;

### -HTML/CSS/Javascript(for visualiazation)

#### third-party js lib used:

leftlet.js(under Project_salary/web/js/; Project_salary/web/css/)
