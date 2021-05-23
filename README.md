# 目录结构
## page
- base_page.py: driver驱动与原生API的二次封装；  
- pre_page对象: 初始化driver对象，并隔离driver驱动，将driver以对象的方式传递；
- page对象: 继承 pre_page 后，完成对各页面的封装；  
## testcase
文件夹内统一存放所有的测试用例，调用 page 对象实现业务并断言；  
## common
文件夹内存放对其他功能封装，改进原生框架不足；  
## data
文件夹数据构造与测试用例的数据封装；  