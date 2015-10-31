import unittest

import mock

from module import get_status, input_conf, read_config, url_type, write_config, \
    set_config, configure_to_tuple


class TestModule(unittest.TestCase):

    def test_status(self):
        self.assertEqual(200, get_status("http://jellyms.kr"))

    """Change code to comments to commint"""
#    def test_send_email(self):
#        send_email(str(get_status("http://jellyms.kr")),
#                    "chm073@gmail.com","","")

    def test_url_type(self):
        self.assertEqual("http://jellyms.kr", url_type("jellyms.kr"))
        self.assertEqual("http://jellyms.kr", url_type("http://jellyms.kr"))

    def test_read_config(self):
        self.assertEquals("smtp.gmail.com:587", read_config()["smtpServer"])

    def test_write_config(self):
        conf = {
            "url": "jellyms.kr",
            "smtpServer": "smtp.gmail.com:587",
            "smtpUser": "jelly",
            "toEmail": "chm073@naver.com"
        }
        write_config(conf)
        self.assertEquals(conf, read_config())

    def test_input_conf(self):
        conf = {
            "url": "jellyms.kr",
            "smtpServer": "smtp.gmail.com:587",
            "smtpUser": "jelly",
            "toEmail": "chm073@naver.com"
        }

        write_config(conf)

        with mock.patch("__builtin__.raw_input", return_value=""):
            self.assertEquals(conf["url"], input_conf(
                "Please just enter", conf["url"]))
        with mock.patch("__builtin__.raw_input", return_value="test"):
            self.assertEquals("test", input_conf(
                "Please write 'test'", conf["url"]))

    def test_set_config(self):
        expected_conf = {
            "url": "http://abc",
            "smtpServer": "abc",
            "smtpUser": "abc",
            "toEmail": "abc",
            "smtpPw": "Password",
        }

        with mock.patch("__builtin__.raw_input", return_value="abc"):
            with mock.patch("getpass.getpass", return_value="Password"):
                self.assertEquals(expected_conf["url"], set_config()["url"])
                self.assertEquals(
                    expected_conf["smtpServer"], set_config()["smtpServer"])
                self.assertEquals(
                    expected_conf["smtpUser"], set_config()["smtpUser"])
                self.assertEquals(
                    expected_conf["toEmail"], set_config()["toEmail"])
                self.assertEquals(
                    expected_conf["smtpPw"], set_config()["smtpPw"])

    def test_configure_to_tuple(self):
        expected_conf = {
            "url": "http://abc",
            "smtpServer": "smtpServernnabcde",
            "smtpUser": "smtpUserarst",
            "toEmail": "toEmailabc",
        }

        exp_url = expected_conf["url"]
        exp_smtp_server = expected_conf["smtpServer"]
        exp_smtp_user = expected_conf["smtpUser"]
        exp_to_email = expected_conf["toEmail"]

        with mock.patch("module.read_config", return_value=expected_conf):
            act_url, act_smtp_server, act_smtp_user, act_smtp_email \
                = configure_to_tuple()
            self.assertEquals(exp_url, act_url)
            self.assertEquals(exp_smtp_server, act_smtp_server)
            self.assertEquals(exp_smtp_user, act_smtp_user)
            self.assertEquals(exp_to_email, act_smtp_email)
        
