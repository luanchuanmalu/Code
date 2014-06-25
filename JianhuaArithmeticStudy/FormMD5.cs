using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Security.Cryptography;

namespace JianhuaArithmeticStudy
{
    public partial class FormMD5 : Form
    {
        public FormMD5()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //Դ�ַ���
            string sourcestring = textBox1.Text;
            //����Ŀ���ַ���
            StringBuilder sBuilder = new StringBuilder();

            MD5 md5 = MD5.Create();
            byte[] source = md5.ComputeHash(Encoding.UTF8.GetBytes(sourcestring));
            for (int i = 0; i < source.Length; i++)
            {
                sBuilder.Append(source[i].ToString("x2"));
            }
            textBox2.Text = sBuilder.ToString();
        }


    }
}