import unittest

import mock

from module import get_status, input_conf, read_config, url_type, write_config


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