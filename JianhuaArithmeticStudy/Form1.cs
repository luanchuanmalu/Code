using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace JianhuaArithmeticStudy
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //int aa = int.MaxValue;
            int number;
            int.TryParse(textBox1.Text,out number);
            Stopwatch sw = Stopwatch.StartNew();
            //string –‘ƒ‹≤‚ ‘
            string str = string.Empty;
            for (int i = 0; i < number; i++)
            {
                str += i.ToString();
            }
            sw.Stop();
            label3.Text = sw.ElapsedMilliseconds.ToString();
            //StringBuilder performance testing
            sw.Reset();
            sw.Start();
            StringBuilder sb = new StringBuilder(number+100);
            for (int i = 0; i < number; i++)
            {
                sb.Append(i.ToString());
            }
            sw.Stop();
            label4.Text = sw.ElapsedMilliseconds.ToString();
        }
    }
}