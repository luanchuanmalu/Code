#set-ExecutionPolicy RemoteSigned
echo "Test RESTful API"
python D:\Develop\workspace\Code\PYTHON\REST_API\FlaskWeb.py 2>&1 | %{ "$_" }
echo "----------------"