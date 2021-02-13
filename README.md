# 胡亦 - 编程课程在线练习

项目名称: 编程课程在线练习

项目概述: 参照网站网站https://codingbat.com/java制作一个前后端分离单应用.

甲方项目要求:

1. 可以在线进行编程练习，自动检测是否正确
2. 可以用于编程课程在线练习、考试
3. 目前先支持Python就行, **暂时**不考虑其他语言实现.

项目实现:



项目技术方案:

1. 项目后端: 全使用Python语言实现

   1. Web后端: Flask框架实现

   2. Python代码解释及运行

      1. 通过接受的字符串判断是否包含非法代码

      2. 在经过检查的字符串中插入相关验证代码

         1. 例子

            1. 题目: 实现一个函数`inverse`, 该函数接受一个类型` bool`名为`inputData`的参数, 该函数总是返回与之相反的结果.

               1. 正确例子1
                  1. 输入`True`
                  2. 返回`False`
               2. 正确例子2
                  1. 输入`False`
                  2. 返回`True`
               3. 错误例子1
                  1. 输入`True`
                  2. 返回`True`
               4. 错误例子2
                  1. 输入`True`
                  2. 返回`0`

            2. 在服务端处理过程

               1. 通过`sys.executable`或者`exec`运行代码

               2. ```python
                  //用户输入
                  def inverse(inputData): 
                      return NOT inputData
                  
                  //接收到用户字符串
                  "def inverse(inputData): \n\treturn NOT inputData"
                  
                  //服务端处理字符串
                  def strCheck(str):
                      // 这是一个简单地判断, 正式的判断应该包含该用户是否调用非法函数, 用户是否使用非法手段返回结果等等...
                      if str != None:
                          return str
                      else:
                          return False
                      
                  
                  //服务端插入关键判断函数
                  //这里的函数接受的是用户输入的函数的字符串, 返回的应该是经过插入关键判断函数的字符串
                  //返回的类似这个东东
                  """
                  def coreCheckFunction(str):
                      //用户实现
                      def inverse(inputData): 
                      	return NOT inputData
                      //工程师实现
                      def standardIverse(inputData):
                          return NOT inputData
                      def check:
                          if inverse(str) == standardIverse(str):
                              return true
                          else:
                              return false"
                  """
                  
                  //将相关字符串写入文件
                  
                  
                  //将成功写入字符串的文件执行
                  subprocess.check_output([EXEC, fpath]
                  //如果返回true, 就代表验证成功, 否则验证失败, 并且告知原因
                  //错误原因1: 逻辑出错
                  //错误原因2: 代码语法错误(并且原文返回错误信息)
                  
                  //web框架返回信息
                      
                  ```

      3. 后端返回格式`Json`

2. 项目前端: 使用Vue.js构建

   1. 项目UI: 项目初期以仿照原网站为主

