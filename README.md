# IC_DSI_Project
Team [Data Hunter!!]'s Repository

## 使用手册（展示人员、验收人员必看）：
### ① web文件夹
#### 结构：

1. map.html
包含与地区有关的可视化部分

2. js文件夹
包含嵌入到html的JavaScript脚本

3. css文件夹
包含外联到html的css

### web文件夹使用方法
#### 1. 克隆项目
将仓库克隆（clone）到本地文件夹

#### 2. 搭建本地服务器
在项目的web文件夹下建立本地服务器

具体操作：打开终端，输入
```
cd web文件夹的位置
python -m http.server
```
终端记得不要关掉
#### 3. 开始调试html
如本地装有VSCode可以直接用VSCode打开项目文件夹，装上Chrome拓展后即可直接在调试->open map.html（调试已经配置好）

如果没有VSCode，在浏览器（最好是Chrome）中输入
```
localhost:8000
```
这时候会显示这个目录下的文件，点击map.html即可
### ② process文件夹
#### 结构：

1. main.ipynb
包含岗位平均薪资和使用的编程语言间的关系

2. main2.ipynb
包含岗位平均薪资和岗位描述中提到的要求关键词间的关系

3. main3.ipynb
包含岗位平均薪资和企业年龄的关系

4. generate.py
包含生成json的代码

### process文件夹使用方法：
123均可直接在github中查看，或者尝试百度jupyter notebook...不过没必要，有什么需要可以直接提，无论是需要图片或者是要求修改、增加内容

4不用看（内含丑陋代码）

### ③ data文件夹
#### 结构：
1. data_cleaned_2021.csv主要数据

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
