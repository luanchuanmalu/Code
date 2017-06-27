package ServletDemo;

import java.io.IOException;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletOutputStream;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class demo2
 */
public class demo2 extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public demo2() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//response.getOutputStream().write("servletDemo2".getBytes());
		outputChineseByOutputStream(response);//ʹ��OutputStream���������
		//ServletContext context = this.getServletContext();
		//��ȡ����webվ��ĳ�ʼ������
		//String contextInitParam = context.getInitParameter("url");
		//response.getWriter().print(contextInitParam);
		//response.getWriter().print("\nservletDemo2");
		
		
		

		
	}
	
	/**
     * ʹ��OutputStream���������
     * @param request
     * @param response
     * @throws IOException 
     */
    public void outputChineseByOutputStream(HttpServletResponse response) throws IOException{
        /**ʹ��OutputStream�������ע�����⣺
         * �ڷ������ˣ����������ĸ��������ģ���ô��Ҫ���ƿͻ������������Ӧ�����򿪣�
         * ���磺outputStream.write("�й�".getBytes("UTF-8"));//ʹ��OutputStream����ͻ��������������ģ���UTF-8�ı���������
         * ��ʱ��Ҫ���ƿͻ����������UTF-8�ı���򿪣�������ʾ��ʱ��ͻ�����������룬��ô�ڷ���������ο��ƿͻ������������UTF-8�ı�����ʾ�����أ�
         * ����ͨ��������Ӧͷ�������������Ϊ�����磺
         * response.setHeader("content-type", "text/html;charset=UTF-8");//ͨ��������Ӧͷ�����������UTF-8�ı�����ʾ����
         */
        String data = "�й�";
        ServletOutputStream outputStream = response.getOutputStream();//��ȡOutputStream�����
        response.setHeader("content-type", "text/html;charset=UTF-8");//ͨ��������Ӧͷ�����������UTF-8�ı�����ʾ���ݣ����������仰����ô�������ʾ�Ľ�������
        /**
         * data.getBytes()��һ�����ַ�ת�����ֽ�����Ĺ��̣����������һ����ȥ�����
         * ��������ĵĲ���ϵͳ������Ĭ�Ͼ��ǲ��Ҳ�GB2312�����
         * ���ַ�ת�����ֽ�����Ĺ��̾��ǽ������ַ�ת����GB2312������϶�Ӧ������
         * ���磺 "��"��GB2312������϶�Ӧ��������98
         *         "��"��GB2312������϶�Ӧ��������99
         */
        /**
         * getBytes()�������������������ô�ͻ���ݲ���ϵͳ�����Ի�����ѡ��ת�������������Ĳ���ϵͳ����ô��ʹ��GB2312�����
         */
        byte[] dataByteArr = data.getBytes("UTF-8");//���ַ�ת�����ֽ����飬ָ����UTF-8�������ת��
        outputStream.write(dataByteArr);//ʹ��OutputStream����ͻ�������ֽ�����
    }

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
