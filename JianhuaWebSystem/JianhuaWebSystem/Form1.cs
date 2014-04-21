using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Net;

namespace JianhuaWebSystem
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            setLoginImg();
        }

        /// <summary>
        /// 获取登录验证码
        /// </summary>
        private void setLoginImg()
        {
            HttpWebRequest request = WebRequest.Create(LinkAddress.LOGINIMG_ADDRESS) as HttpWebRequest;
            request.ProtocolVersion = HttpVersion.Version10;
            request.UserAgent = LinkAddress.DefaultUserAgent;
            request.KeepAlive = true;
            request.Headers.Add("DNT", "1");
            request.Method = "GET";

            //get reponse
            if (request.RequestUri.Scheme == "https")
                ServicePointManager.ServerCertificateValidationCallback = validateServerCertificate;

            CookieContainer cookies = new CookieContainer();
            request.CookieContainer = cookies;

            request.ContentType = "application/x-www-form-urlencoded";

            try
            {
                HttpWebResponse response = request.GetResponse() as HttpWebResponse;
                DateTime serverDateTime = response.LastModified;
                if (response.StatusCode != HttpStatusCode.OK)
                    throw new Exception("Server error!");
                Image img = new Bitmap(response.GetResponseStream());
                this.pictureBox1.Image = img;
            }
            catch (Exception)
            {
                MessageBox.Show("网络连接错误");
            }



            //HttpHelper helper = new HttpHelper(LinkAddress.LOGINIMG_ADDRESS);



            //helper.Request.Method = "GET";
            //try
            //{
            //    this.pictureBox1.Image = helper.GetResponseIMG();
            //}
            //catch (Exception)
            //{
            //    MessageBox.Show("网络连接错误");
            //    this.Close();
            //}

            //if (helper.ServerDateTime.Hour >= 23 || helper.ServerDateTime.Hour <= 7)
            //{
            //    isAllowLogin = false;
            //    this.button1.Enabled = false;
            //    this.label1.Text = "每天23点到次日7点铁道部都在维护系统";
            //    setLabelLocation();
            //}
        }
        private bool validateServerCertificate(object sender, System.Security.Cryptography.X509Certificates.X509Certificate certificate, System.Security.Cryptography.X509Certificates.X509Chain chain, System.Net.Security.SslPolicyErrors sslPolicyErrors)
        {
            return true;
        }

        private void picturebox1_Click(object sender, EventArgs e)
        {
            setLoginImg();

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            setLoginImg();
        }
    }
}