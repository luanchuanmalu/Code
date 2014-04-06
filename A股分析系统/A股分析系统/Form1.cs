using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace A股分析系统
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        /// <summary>
        /// 华荣：会的，为了证明不是孔穴来风，先透露一点信息，这只股票的代码6个数字之和为16，4月上旬可能不涨。
        /// </summary>
        /// <param name="StockNumber"></param>
        /// <returns></returns>
        public string IsSum16Stock(int StockNumber)
        {
            int i = StockNumber;
            int count1 = i % 10;
            i = i / 10;
            int count2 = i % 10;
            i = i / 10;
            int count3 = i % 10;
            i = i / 10;
            int count4 = i % 10;
            i = i / 10;
            int count5 = i % 10;
            i = i / 10;
            int count6 = i % 10;
            int count = count1 + count2 + count3 + count4 + count5 + count6;
            string code = count6.ToString() + count5.ToString() + count4.ToString() + count3.ToString() + count2.ToString() + count1.ToString();
            if (count == 16)
            {
                return code;
            }
            return string.Empty;
        }
        /// <summary>
        /// 
        /// </summary>
        /// <param name="path"></param>
        /// <returns></returns>
        private List<string> GetAllStockCodeByTextFile(string path)
        {
            List<string> allStockCode = new List<string>();

            //FileStream fs = new FileStream(path, FileMode.Open);
            StreamReader filereader = new StreamReader(path);
            string stockCode = filereader.ReadLine();
            while (stockCode != null)
            {
                if (stockCode != string.Empty)
                {
                    allStockCode.Add(stockCode);
                }
                stockCode = filereader.ReadLine();
            }

            return allStockCode;

        }
        private void button1_Click(object sender, EventArgs e)
        {
            //Get all the stock code
            List<string> AllStockCode=GetAllStockCodeByTextFile("Resource\\A股列表.txt");

            

            int count = 0;
            foreach (string stockCode in AllStockCode)
            {
                int codenum = int.Parse(stockCode);
                string code = IsSum16Stock(codenum);
                if (code!=string.Empty)
                {
                    this.textBox1.Text = this.textBox1.Text + code + "-";
                    count++;
                    using (StreamWriter sw = new StreamWriter("Resource\\符合要求的股票.txt", true))
                    {
                        sw.WriteLine(stockCode);
                    }
                }
            }
            this.textBox1.Text = this.textBox1.Text + "\r\n";
            this.textBox1.Text = this.textBox1.Text + count.ToString()+ "只符合要求的股票";
            
        }
    }
}