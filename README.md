#Simple Project use Flask
这个article app 实现了一个简单的文章管理系统功能，具体如下：
1. 文章展示
   ·列表展示：在首页（/articles 路由对应的视图函数 index），从数据库中获取所有文章信息，通过 render_template 渲染 index.html 模板展示文章列表。列表中每个文章包含标题和创建时间，标题以超链接形式呈现，点击可跳转到对应文章详情页。
   ·详情展示：/articles/<int:article_id> 路由对应的 article 视图函数，根据传入的文章 id 从数据库中查询文章详情，再渲染 article.html 模板展示文章的标题、创建时间和内容，并提供返回文章列表、删除和修改文章的操作链接或按钮。
   
2. 文章添加：/submit 路由对应的 submit 视图函数处理文章添加功能。当用户在前端页面填写文章标题和内容并提交表单（method="post"）时，该函数从表单中获取数据，创建新的文章对象并添加到数据库，然后重定向到文章列表页面。

3. 文章删除：/delete/<int:article_id> 路由对应的 delete 视图函数接收文章 id，从数据库中获取对应的文章对象并删除，之后重定向回文章列表页面，实现删除指定文章的功能。

4.文章修改
   ·编辑页面展示：/edit/<int:article_id> 路由对应的 edit 视图函数在接收到 GET 请求时，根据文章 id 从数据库获取文章信息，渲染 edit.html 模板，展示包含文章当前标题和内容的编辑页面。
   ·修改提交处理：当 edit 视图函数接收到 POST 请求时，从表单中获取修改后的标题和内容，更新数据库中对应文章的信息，成功后重定向到修改后的文章详情页面。若更新过程出现异常，会打印错误信息并回滚数据库事务 。


最后的页面结果如下：
![app](https://github.com/Daisy1259/Simple-Project-use-Flask/blob/main/Flask Project.jpg)

   
