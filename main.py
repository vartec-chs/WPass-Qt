import sys

from PySide6.QtCore import QSize
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidget,QTableWidgetItem, QMessageBox
from PySide6.QtGui import QIcon

from main_ui import Ui_MainWindow
from add_pass import AddPass
from search import Search_Dialog

from db import DB
import search



class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.db: DB | None = None
		
		self.ui.setupUi(self)
		self.page = 1

		self.ui.statusBar.showMessage("Пожалуйста, откройте базу данных")
		self.ui.add_button.setEnabled(False)
		self.ui.edit_button.setEnabled(False)
		self.ui.delete_button.setEnabled(False)

		self.ui.next_button.setEnabled(False)
		self.ui.prev_button.setEnabled(False)

		self.ui.search_button.setEnabled(False)

		self.ui.open_db_button.clicked.connect(self.open_db)
		self.ui.add_button.clicked.connect(self.open_add_pass_modal)
		self.ui.edit_button.clicked.connect(self.edit_password)
		self.ui.delete_button.clicked.connect(self.delete_password)
		self.ui.next_button.clicked.connect(self.next_page)
		self.ui.prev_button.clicked.connect(self.prev_page)

		self.ui.search_button.clicked.connect(self.search)

		


	def open_db(self):
		file_dialog = QFileDialog()
		file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
		file_dialog.setNameFilter("DB Files (*.db)")
		file_dialog.setViewMode(QFileDialog.ViewMode.Detail)
		if file_dialog.exec():
			file_path = file_dialog.selectedFiles()[0]
			self.db = DB(file_path)
			self.table_set_columns()
			self.table_render()
			self.ui.page_counter_label.setText(f"{self.page}/{self.db.page_count()}")
			self.ui.statusBar.showMessage(f"База данных открыта {file_path}")

			self.ui.add_button.setEnabled(True)
			self.ui.edit_button.setEnabled(True)
			self.ui.delete_button.setEnabled(True)
			self.ui.search_button.setEnabled(True)

			self.ui.next_button.setEnabled(True)
			self.ui.prev_button.setEnabled(True)

	
	def delete_password(self):
		row = self.ui.pass_table.currentRow()

		if row == -1:
			QMessageBox.warning(self, "Ошибка", "Выберите пароль для удаления")
			return
		
		answer = QMessageBox.question(self, "Подтверждение", "Вы уверены, что хотите удалить пароль?")

		if answer != QMessageBox.StandardButton.Yes:
			return

		id = self.ui.pass_table.item(row, 0).text()
		self.db.delete_password(id)
		page_count = self.db.pass_count()

		if page_count == 0:
			self.ui.pass_table.setRowCount(0)

		self.ui.page_counter_label.setText(f"{self.page}/{page_count}")
		self.table_render()
		QMessageBox.information(self, "Успешно", "Пароль успешно удален")


	def edit_password(self):
		row = self.ui.pass_table.currentRow()

		if row == -1:
			QMessageBox.warning(self, "Ошибка", "Выберите пароль для редактирования")
			return

		id = self.ui.pass_table.item(row, 0).text()
		self.open_edit_pass_modal()
		
		self.add_pass_window_ui.name_field.setText(self.ui.pass_table.item(row, 1).text())
		self.add_pass_window_ui.login_field.setText(self.ui.pass_table.item(row, 2).text())
		self.add_pass_window_ui.pass_field.setText(self.ui.pass_table.item(row, 3).text())
		self.add_pass_window_ui.url_field.setText(self.ui.pass_table.item(row, 4).text())
		self.add_pass_window_ui.notes_field.setPlainText(self.ui.pass_table.item(row, 5).text())

		self.add_pass_window_ui.submit_button.clicked.connect(lambda: self.edit_password_submit(id))


	def edit_password_submit(self, id):
		name = self.add_pass_window_ui.name_field.text()
		login = self.add_pass_window_ui.login_field.text()
		password = self.add_pass_window_ui.pass_field.text()
		url = self.add_pass_window_ui.url_field.text()
		notes = self.add_pass_window_ui.notes_field.toPlainText()

		if name == "" or login == "" or password == "":
			QMessageBox.warning(self, "Error", "Please fill all fields")
			self.add_pass_window_ui.name_field.setFocus()
			return

		self.db.update_password(id, name, login, password, url, notes)
		self.add_pass_window.close()
		self.table_render()


	def search(self):
		self.search_window = QtWidgets.QDialog()
		self.search_window_ui = Search_Dialog()
		self.search_window_ui.setupUi(self.search_window)
		self.search_window.show()

		self.search_window_ui.seacrh_button.clicked.connect(self.search_submit)
		self.search_window_ui.throw_off_button.clicked.connect(self.throw_off_search)


	def throw_off_search(self):
		self.search_window.close()
		self.table_render()


	def search_submit(self):
		search_text = self.search_window_ui.search_field.text()

		if search_text == "":
			QMessageBox.warning(self, "Ошибка", "Поле поиска пустое")
			self.search_window_ui.search_field.setFocus()
			return

		self.search_window_ui.radio_button_name.setChecked(True)
		
		if self.search_window_ui.radio_button_name.isChecked():
			data = self.db.search_by_name(search_text)
			self.table_search(data)
		elif self.search_window_ui.radio_button_login.isChecked():
			data = self.db.search_by_login(search_text)
			self.table_search(data)
		elif self.search_window_ui.radio_button_url.isChecked():
			data = self.db.search_by_url(search_text)
			self.table_search(data)
			
		


	def table_search(self, data):

		for i in range(len(data)):
			self.ui.pass_table.insertRow(i)
			self.ui.pass_table.setItem(i, 0, QTableWidgetItem(data[i][0]))
			self.ui.pass_table.setItem(i, 1, QTableWidgetItem(data[i][1]))
			self.ui.pass_table.setItem(i, 2, QTableWidgetItem(data[i][2]))
			self.ui.pass_table.setItem(i, 3, QTableWidgetItem(data[i][3]))
			self.ui.pass_table.setItem(i, 4, QTableWidgetItem(data[i][4]))
			self.ui.pass_table.setItem(i, 5, QTableWidgetItem(data[i][5]))
		
		self.ui.pass_table.setRowCount(len(data))



		
		
	def open_edit_pass_modal(self):
		self.add_pass_window = QtWidgets.QDialog()
		self.add_pass_window_ui = AddPass()
		self.add_pass_window_ui.setupUi(self.add_pass_window)

		self.add_pass_window_ui.submit_button.setText("Изменить")
		icon1 = QIcon()
		icon1.addFile(u":/icons/icons/edit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
		self.add_pass_window_ui.submit_button.setIcon(icon1)
		self.add_pass_window.setWindowTitle("Редактирование пароля")

		self.add_pass_window.show()


	def open_add_pass_modal(self):
		self.add_pass_window = QtWidgets.QDialog()
		self.add_pass_window_ui = AddPass()
		self.add_pass_window_ui.setupUi(self.add_pass_window)
		self.add_pass_window.show()



		self.add_pass_window_ui.submit_button.clicked.connect(self.add_password)


	def add_password(self):
		name = self.add_pass_window_ui.name_field.text()
		login = self.add_pass_window_ui.login_field.text()
		password = self.add_pass_window_ui.pass_field.text()
		url = self.add_pass_window_ui.url_field.text()
		notes = self.add_pass_window_ui.notes_field.toPlainText()

		if name == "" or login == "" or password == "":
			QMessageBox.warning(self, "Error", "Пожалуйста, заполните все поля")
			self.add_pass_window_ui.name_field.setFocus()
			return

		self.db.add_password(name, login, password, url, notes)
		self.add_pass_window.close()
		self.table_render()

	
	
	def next_page(self):
		page_count = self.db.page_count()

		if self.page == page_count or page_count == 0:
			return

		self.page += 1
		self.ui.page_counter_label.setText(f"{self.page}/{page_count}")
		self.table_render()
	
	def prev_page(self):
		page_count = self.db.page_count()

		if self.page == 1:
			return

		self.page -= 1
		self.ui.page_counter_label.setText(f"{self.page}/{page_count}")
		self.table_render()
	

	def table_set_columns(self):
		self.ui.pass_table.setColumnCount(6)
		self.ui.pass_table.setHorizontalHeaderLabels(["ID", "Name", "Login", "Password", "URL", "Notes"])
		
		for i in range(6):
			self.ui.pass_table.setColumnWidth(i, 126)


	def table_render(self):
		count = self.db.pass_count()

		if count == 0:
			self.ui.pass_table.setRowCount(0)
			return

		data = self.db.paginate(self.page)

		self.ui.pass_table.setRowCount(len(data))
		for i, password in enumerate(data):
			self.ui.pass_table.setItem(i, 0, QTableWidgetItem(str(password[0])))
			self.ui.pass_table.setItem(i, 1, QTableWidgetItem(password[1]))
			self.ui.pass_table.setItem(i, 2, QTableWidgetItem(password[2]))
			self.ui.pass_table.setItem(i, 3, QTableWidgetItem(password[3]))
			self.ui.pass_table.setItem(i, 4, QTableWidgetItem(password[4]))
			self.ui.pass_table.setItem(i, 5, QTableWidgetItem(password[5]))



	def closeEvent(self, event):
		self.db.close()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	app.setStyle("Universal")
	window = MainWindow()
	window.show()
	sys.exit(app.exec())