from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QTextEdit
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个文本编辑器
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # 添加“打开文件”菜单项并绑定槽函数
        openAction = self.menuBar().addAction('打开文件')
        openAction.triggered.connect(self.openFile)

    def openFile(self):
        # 打开文件对话框，选择要打开的文件
        fileName, _ = QFileDialog.getOpenFileName(self, '打开文件', '', 'Text Files (*.txt)')

        if fileName != '':
            # 打开选中的文件并读取其内容
            with open(fileName, 'r') as file:
                text = file.read()

            # 在文本编辑器中显示文件内容
            self.textEdit.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
