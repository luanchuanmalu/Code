#set-ExecutionPolicy RemoteSigned
echo "Test RESTful API"
python D:\Develop\workspace\Code\PYTHON\REST_API\FlaskAPI.py 2>&1 | %{ "$_" }
#python D:\Develop\workspace\Code\PYTHON\REST_API\FlaskWeb.py 2>&1 | %{ "$_" }
echo "----------------"