import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QTabWidget , QTextEdit , QFileDialog , QVBoxLayout , QWidget , \
    QPushButton , QTableWidget , QTableWidgetItem , QLineEdit , QLabel , QGridLayout , QAction , QToolBar , \
    QGraphicsView , QGraphicsScene , QGraphicsLineItem , QColorDialog
from PyQt5.QtCore import Qt , QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPainter , QColor , QPen , QIcon , QTextCharFormat
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class OraclearOffice ( QMainWindow ) :
    def __init__(self) :
        super ( ).__init__ ( )
        self.setWindowTitle ( "Oraclear Office 1.0" )
        self.setGeometry ( 100 , 100 , 1200 , 800 )

        self.tabs = QTabWidget ( self )
        self.setCentralWidget ( self.tabs )

        # Add all required apps
        self.add_word_processor ( )
        self.add_spreadsheet ( )
        self.add_presentation_maker ( )
        self.add_mail_client ( )
        self.add_paint_app ( )
        self.add_web_browser ( )

    def add_word_processor(self) :
        word_tab = QWidget ( )
        self.tabs.addTab ( word_tab , "Word Processor" )

        self.word_text_edit = QTextEdit ( )
        self.word_text_edit.setFontPointSize ( 12 )

        # Toolbar for formatting options
        toolbar = QToolBar ( self )
        self.addToolBar ( toolbar )

        bold_action = QAction ( 'Bold' , self )
        bold_action.setIcon ( QIcon.fromTheme ( 'format-text-bold' ) )
        bold_action.triggered.connect ( self.toggle_bold )
        toolbar.addAction ( bold_action )

        save_action = QAction ( 'Save' , self )
        save_action.triggered.connect ( self.save_word_file )
        toolbar.addAction ( save_action )

        open_action = QAction ( 'Open' , self )
        open_action.triggered.connect ( self.open_word_file )
        toolbar.addAction ( open_action )

        layout = QVBoxLayout ( )
        layout.addWidget ( self.word_text_edit )
        word_tab.setLayout ( layout )

    def toggle_bold(self) :
        cursor = self.word_text_edit.textCursor ( )
        if cursor.charFormat ( ).fontWeight ( ) == Qt.Normal :
            cursor.mergeCharFormat ( QTextCharFormat ( Qt.Bold ) )
        else :
            cursor.mergeCharFormat ( QTextCharFormat ( Qt.Normal ) )

    def save_word_file(self) :
        filename , _ = QFileDialog.getSaveFileName (
            self , "Save Document" , "" , "Text Files (*.txt);;Word Files (*.docx)"
            )
        if filename :
            with open ( filename , 'w' ) as file :
                file.write ( self.word_text_edit.toPlainText ( ) )

    def open_word_file(self) :
        filename , _ = QFileDialog.getOpenFileName (
            self , "Open Document" , "" , "Text Files (*.txt);;Word Files (*.docx)"
            )
        if filename :
            with open ( filename , 'r' ) as file :
                self.word_text_edit.setPlainText ( file.read ( ) )

    def add_spreadsheet(self) :
        sheet_tab = QWidget ( )
        self.tabs.addTab ( sheet_tab , "Spreadsheet" )

        self.table = QTableWidget ( 10 , 5 )
        self.table.setHorizontalHeaderLabels ( [ 'A' , 'B' , 'C' , 'D' , 'E' ] )

        layout = QVBoxLayout ( )
        layout.addWidget ( self.table )
        sheet_tab.setLayout ( layout )

    def add_presentation_maker(self) :
        ppt_tab = QWidget ( )
        self.tabs.addTab ( ppt_tab , "Presentation Maker" )

        self.slide_text_edit = QTextEdit ( )
        self.add_image_button = QPushButton ( 'Add Image' , self )
        self.add_image_button.clicked.connect ( self.add_image )

        layout = QVBoxLayout ( )
        layout.addWidget ( self.slide_text_edit )
        layout.addWidget ( self.add_image_button )
        ppt_tab.setLayout ( layout )

    def add_image(self) :
        filename , _ = QFileDialog.getOpenFileName ( self , "Open Image" , "" , "Image Files (*.png *.jpg *.bmp)" )
        if filename :
            self.slide_text_edit.append ( f"Image: {filename}" )

    def add_mail_client(self) :
        mail_tab = QWidget ( )
        self.tabs.addTab ( mail_tab , "Mail Client" )

        self.recipient_label = QLabel ( "Recipient:" )
        self.recipient_input = QLineEdit ( )
        self.subject_label = QLabel ( "Subject:" )
        self.subject_input = QLineEdit ( )
        self.body_label = QLabel ( "Message:" )
        self.body_input = QTextEdit ( )

        self.send_button = QPushButton ( 'Send Email' , self )
        self.send_button.clicked.connect ( self.send_email )

        layout = QGridLayout ( )
        layout.addWidget ( self.recipient_label , 0 , 0 )
        layout.addWidget ( self.recipient_input , 0 , 1 )
        layout.addWidget ( self.subject_label , 1 , 0 )
        layout.addWidget ( self.subject_input , 1 , 1 )
        layout.addWidget ( self.body_label , 2 , 0 )
        layout.addWidget ( self.body_input , 2 , 1 )
        layout.addWidget ( self.send_button , 3 , 1 )

        mail_tab.setLayout ( layout )

    def send_email(self) :
        recipient = self.recipient_input.text ( )
        subject = self.subject_input.text ( )
        body = self.body_input.toPlainText ( )

        if not recipient or not subject or not body :
            return

        msg = MIMEMultipart ( )
        msg[ 'From' ] = 'your_email@example.com'  # Use your email here
        msg[ 'To' ] = recipient
        msg[ 'Subject' ] = subject

        msg.attach ( MIMEText ( body , 'plain' ) )

        server = smtplib.SMTP ( 'smtp.example.com' , 587 )  # Update SMTP server
        server.starttls ( )
        server.login ( 'your_email@example.com' , 'your_password' )  # Update login
        server.sendmail ( msg[ 'From' ] , msg[ 'To' ] , msg.as_string ( ) )
        server.quit ( )

        self.recipient_input.clear ( )
        self.subject_input.clear ( )
        self.body_input.clear ( )

        print ( "Email sent successfully!" )

    def add_paint_app(self) :
        paint_tab = QWidget ( )
        self.tabs.addTab ( paint_tab , "Paint" )

        self.canvas = QGraphicsView ( )
        self.scene = QGraphicsScene ( )
        self.canvas.setScene ( self.scene )

        self.last_x = None
        self.last_y = None
        self.drawing = False
        self.color = QColor ( 0 , 0 , 0 )  # Default color: black

        paint_layout = QVBoxLayout ( )

        self.canvas.setRenderHint ( QPainter.Antialiasing )
        paint_layout.addWidget ( self.canvas )

        color_button = QPushButton ( "Pick Color" )
        color_button.clicked.connect ( self.pick_color )
        paint_layout.addWidget ( color_button )

        paint_tab.setLayout ( paint_layout )

    def pick_color(self) :
        color = QColorDialog.getColor ( )
        if color.isValid ( ) :
            self.color = color

    def mousePressEvent(self , event) :
        if event.button ( ) == Qt.LeftButton :
            self.drawing = True
            self.last_x = event.x ( )
            self.last_y = event.y ( )

    def mouseMoveEvent(self , event) :
        if self.drawing :
            x = event.x ( )
            y = event.y ( )
            self.draw_line ( self.last_x , self.last_y , x , y )
            self.last_x = x
            self.last_y = y

    def mouseReleaseEvent(self , event) :
        if event.button ( ) == Qt.LeftButton :
            self.drawing = False

    def draw_line(self , x1 , y1 , x2 , y2) :
        line = QGraphicsLineItem ( x1 , y1 , x2 , y2 )
        line.setPen ( QPen ( self.color , 2 ) )
        self.scene.addItem ( line )

    def add_web_browser(self) :
        browser_tab = QWidget ( )
        self.tabs.addTab ( browser_tab , "WebWorld" )

        self.browser = QWebEngineView ( )
        self.browser.setUrl ( QUrl ( "http://www.google.com" ) )
        browser_layout = QVBoxLayout ( )
        browser_layout.addWidget ( self.browser )

        self.setWindowTitle ( "WebWorld 0.1" )
        self.setGeometry ( 100 , 100 , 1200 , 800 )

        self.browser.urlChanged.connect ( self.update_url )

        nav_bar = QToolBar ( )
        self.addToolBar ( nav_bar )

        back_button = QAction ( "Back" , self )
        back_button.triggered.connect ( self.browser.back )
        nav_bar.addAction ( back_button )

        forward_button = QAction ( "Forward" , self )
        forward_button.triggered.connect ( self.browser.forward )
        nav_bar.addAction ( forward_button )

        reload_button = QAction ( "Reload" , self )
        reload_button.triggered.connect ( self.browser.reload )
        nav_bar.addAction ( reload_button )

        self.url_bar = QLineEdit ( )
        self.url_bar.returnPressed.connect ( self.load_url )
        nav_bar.addWidget ( self.url_bar )

        browser_tab.setLayout ( browser_layout )

    def update_url(self , q) :
        self.url_bar.setText ( q.toString ( ) )

    def load_url(self) :
        url = self.url_bar.text ( )
        if not url.startswith ( "http" ) :
            url = "http://" + url
        self.browser.setUrl ( QUrl ( url ) )


if __name__ == "__main__" :
    app = QApplication ( sys.argv )
    window = OraclearOffice ( )
    window.show ( )
    sys.exit ( app.exec_ ( ) )

