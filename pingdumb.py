import sys

from smtp_module import smtp_login_test
from main_module import checker
from conf import set_config, write_config


if __name__ == "__main__":

    if len(sys.argv) == 1:
        conf = set_config()
        s_pw = conf["smtpPw"]
        write_config(conf)
    else:
        """if exist argv, set password and execute with default configure"""
        s_pw = sys.argv[1]

    smtp_login_test(conf)
    conf["smtpPW"] = s_pw
    
    checker(conf)
