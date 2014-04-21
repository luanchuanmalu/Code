using System;
using System.Collections.Generic;
using System.Text;

namespace JianhuaWebSystem
{
    internal struct LinkAddress
    {
        public const string DefaultUserAgent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; BOIE9;ZHCN)";

        private const string webroot = "https://kyfw.12306.cn";
        /// <summary>
        /// 登录验证码地址
        /// </summary>
        public const string LOGINIMG_ADDRESS = "https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew.do?module=login&rand=sjrand";
        /// <summary>
        /// 登录前验证并获取登录随机码地址
        /// /otn/passcodeNew/getPassCodeNew.do?module=login&rand=sjrand&0.2790136893745512
        /// </summary>
        public const string LOGINSUGGEST = webroot + "otsweb/loginAction.do?method=loginAysnSuggest";
        /// <summary>
        /// 系统登录地址
        /// https://kyfw.12306.cn/otn/index/init
        /// </summary>
        public const string LOGIN_ADDRESS = "https://kyfw.12306.cn/otn/login/init";

    }
}
