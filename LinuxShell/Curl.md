#Using curl to automate HTTP jobs  https://curl.haxx.se/docs/httpscripting.html

# GET
curl -u username https://api.github.com/user?access_token=XXXXXXXXXX

# POST
curl -u username --data "param1=value1&param2=value" https://api.github.com

# 也可以指定一个文件，将该文件中的内容当作数据传递给服务器端
curl --data @filename https://github.api.com/authorizations

curl -I -X DELETE https://api.github.cim

==============================================================================
#通过-o/-O选项保存下载的文件到指定的文件中：
#-o：将文件保存为命令行中指定的文件名的文件中
#-O：使用URL中默认的文件名保存文件到本地
curl -o mygettext.html http://www.gnu.org/software/gettext/manual/gettext.html
curl -O http://www.gnu.org/software/gettext/manual/gettext.html
#同时获取多个文件 curl -O URL1 -O URL2
#同样可以使用转向字符">"对输出进行转向输出

# 让curl使用地址重定向，此时会查询google.com.hk站点
curl -L http://www.google.com

# 当文件在下载完成之前结束该进程
$ curl -O http://www.gnu.org/software/gettext/manual/gettext.html
##############             20.1%

#断点续传 通过添加-C选项继续对该文件进行下载，已经下载过的文件不会被重新下载
curl -C - -O http://www.gnu.org/software/gettext/manual/gettext.html
###############            21.1%

#对CURL使用网络限速 下载速度最大不会超过1000B/second
curl --limit-rate 1000B -O http://www.gnu.org/software/gettext/manual/gettext.html

# 若yy.html文件在2011/12/21之后有过更新才会进行下载
curl -z 21-Dec-11 http://www.example.com/yy.html

#CURL授权 curl -u username:password URL
# 通常的做法是在命令行只输入用户名，之后会提示输入密码，这样可以保证在查看历史记录时不会将密码泄露
curl -u username URL

#从FTP服务器下载文件
# 列出public_html下的所有文件夹和文件
curl -u ftpuser:ftppass -O ftp://ftp_server/public_html/
# 下载xss.php文件
curl -u ftpuser:ftppass -O ftp://ftp_server/public_html/xss.php

#上传文件到FTP服务器
#将myfile.txt文件上传到服务器
curl -u ftpuser:ftppass -T myfile.txt ftp://ftp.testserver.com
# 同时上传多个文件
curl -u ftpuser:ftppass -T "{file1,file2}" ftp://ftp.testserver.com
# 从标准输入获取内容保存到服务器指定的文件中
curl -u ftpuser:ftppass -T - ftp://ftp.testserver.com/myfile_1.txt


#为CURL设置代理
#-x 选项可以为CURL添加代理功能
# 指定代理主机和端口
curl -x proxysever.test.com:3128 http://google.co.in
