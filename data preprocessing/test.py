import unittest
import os
import shutil
import tempfile
from PyQt5 import QtWidgets
from final_demo import Ui_MainWindow

class TestCode(unittest.TestCase):

    def setUp(self):
        self.test_directory = tempfile.mkdtemp()
   
        self.mock_main_window = Ui_MainWindow()

    def tearDown(self):
        shutil.rmtree(self.test_directory)

    def test_open_file_dialog(self):
        mock_main_window = self.mock_main_window
        mock_main_window.listWidget_file_list = QtWidgets.QListWidget()
        mock_main_window.textBrowser_showdata = QtWidgets.QTextBrowser()

        mock_main_window.open_file_dialog()

        self.assertEqual(mock_main_window.listWidget_file_list.count(), 1)
        self.assertTrue(os.path.exists(os.path.join(self.test_directory, 'test.tx0')))
        self.assertTrue(mock_main_window.textBrowser_showdata.toPlainText() != '')

    def test_data_transfer(self):
        mock_main_window = self.mock_main_window

        with open(os.path.join(self.test_directory, 'test.tx0'), 'w') as f:
            f.write("48# Number of electrodes\n# x z\n0     0\n1     0\n909# Number of data")

        mock_main_window.data_transfer()

        self.assertTrue(os.path.exists(os.path.join(self.test_directory, 'test.txt')))

    def test_data_show(self):
        mock_main_window = self.mock_main_window
        mock_main_window.textBrowser_showdata = QtWidgets.QTextBrowser()

        with open(os.path.join(self.test_directory, 'test.txt'), 'w') as f:
            f.write("Test data")

        mock_main_window.data_show()

        self.assertEqual(mock_main_window.textBrowser_showdata.toPlainText(), "Test data")

if __name__ == '__main__':
    unittest.main()
