# class Style():
#     class Color():
#         self.bg =
# def __init__(self):


class Theme():
    """Theme

    Attributes:
        accent (str): Description
        bg (str): Description
        dark (bool): Description
        green (str): Description
        primary (str): Description
        secondary (str): Description
        theme (TYPE): Description
    """

    def __init__(self, theme='default', dark=True):
        super(Theme, self).__init__()

        self.theme = theme
        self.dark  = dark
        self.default(dark=dark)

    def default(self, dark=True):
        """Default Material Theme

        Args
            dark (bool, optional): turn the dark version, defaults to True
        """
        self.bg        = "#263238"
        self.primary   = "#546E7A"
        self.secondary = "#80CBC4"

        self.accent    = "#80CBC4"

        self.green     = "#53DD6C"
        self.red       = "#D72638"


class Style(object):
    def __init__(self, theme='default', dark=True):
        super(Style, self).__init__()

        self.theme = Theme(theme=theme, dark=dark)

        self.style = self.getAll()

        return

    def getAll(self):
        return \
            self.getQWidget() + \
            self.getQToolTip() + \
            self.getQLabel() + \
            self.getQDialog() + \
            self.getQListView() + \
            self.getQTabWidget() + \
            self.getQTabBar() + \
            self.getQStackedWidget() + \
            self.getQGroupBox() + \
            self.getQComboBox() + \
            self.getQRadioButton() + \
            self.getQCheckBox() + \
            self.getQScrollBar() + \
            self.getQPushButton() + \
            self.getQLineEdit()
            # self.getQSpinBox() + \
            # self.getQToolBar() + \
            # self.getQTreeView() + \
            # self.getQToolButton() + \
            # self.getQStatusBar() + \
            # self.getQProgressBar() + \
            # self.getQMenuBar() + \
            # self.getQMenu() + \
            # self.getQDialogButtonBox() + \
            # self.getQAbstractScrollArea()

    def getQWidget(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QWidget = "\
            QWidget:window {                      \n \
                    border: 0px solid " + self.theme.bg + "; \n \
                    background-color: " + self.theme.bg + "; \n \
                } \n \
        "
        return self.QWidget

    def getQToolTip(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QToolTip = "\
            QToolTip { \n \
                    background-color: " + self.theme.primary + "; \n \
                    color: black; \n \
                    padding: 5px; \n \
                    border-radius: 0; \n \
                    opacity: 200; \n \
                } \n \
        "
        return self.QToolTip

    def getQLabel(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QLabel = "\
            QLabel { \n \
                    background: transparent; \n \
                    /* color: #CFD8DC; */    \n \
                    color: " + self.theme.primary + ";  \n \
                } \n \
        "
        return self.QLabel

    def getQDialog(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QDialog = "\
            QDialog { \n \
                    background-color: " + self.theme.bg + "; \n \
                    color: " + self.theme.secondary + "; \n \
                    outline: 0; \n \
                    border: 2px solid transparent; \n \
                } \n \
        "
        return self.QDialog

    def getQListView(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QListView = "\
            QListView { \n \
                    background-color: " + self.theme.bg + "; \n \
                    color: " + self.theme.primary + "; \n \
                    outline: 0; \n \
                    border: 2px solid transparent; \n \
                } \n \
            \n \
            QListView::item:hover { \n \
                    color: #AFBDC4; \n \
                    background: transparent; \n \
                } \n \
            \n \
            QListView::item:selected { \n \
                    color: #ffffff; \n \
                    background: transparent; \n \
                } \n \
        "
        return self.QListView

    def getQTabWidget(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QTabWidget = "\
            QTabWidget::pane { \n \
                    background: transparent; \n \
                } \n \
            \n \
            QTabWidget::tab-bar { \n \
                    left: 0px;  \n \
                } \n \
                 \n \
        "
        return self.QTabWidget

    def getQTabBar(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QTabBar = "\
            QTabBar { \n \
                    background: " + self.theme.bg + "; \n \
                } \n \
            \n \
            QTabBar::tab { \n \
                    background: transparent; \n \
                    border: 0px solid transparent; \n \
                    border-bottom: 2px solid transparent; \n \
                    color: " + self.theme.secondary + "; \n \
                    padding-left: 10px; \n \
                    padding-right: 10px; \n \
                    padding-top: 3px; \n \
                    padding-bottom: 3px; \n \
                } \n \
            \n \
            QTabBar::tab:hover { \n \
                    background-color: transparent; \n \
                    border: 0px solid transparent; \n \
                    border-bottom: 2px solid " + accent + "; \n \
                    color: #AFBDC4; \n \
                } \n \
            \n \
            QTabBar::tab:selected { \n \
                    background-color: transparent; \n \
                    border: 0px solid transparent; \n \
                    border-top: none; \n \
                    border-bottom: 2px solid " + accent + "; \n \
                    color: #FFFFFF; \n \
                } \n \
        "
        return self.QTabBar

    def getQStackedWidget(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QStackedWidget = "\
            QStackedWidget { \n \
                    background: " + self.theme.bg + ";     \n \
                } \n \
        "
        return self.QStackedWidget

    def getQGroupBox(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QGroupBox = "\
            QGroupBox { \n \
                    border: 1px solid transparent; \n \
                    margin-top: 1em; \n \
                } \n \
            \n \
            QGroupBox::title { \n \
                    color: " + accent + "; \n \
                    subcontrol-origin: margin; \n \
                    left: 6px; \n \
                    padding: 0 3px 0 3px; \n \
                } \n \
        "
        return self.QGroupBox

    def getQComboBox(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QComboBox = "\
            QComboBox { \n \
                    color: " + self.theme.secondary + "; \n \
                    background-color: transparent; \n \
                    selection-background-color: transparent; \n \
                    outline: 0; \n \
                } \n \
                 \n \
                QComboBox QAbstractItemView \n \
                {     \n \
                    selection-background-color: transparent; \n \
                    outline: 0; \n \
                } \n \
        "
        return self.QComboBox

    def getQRadioButton(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QRadioButton = "\
            QRadioButton { \n \
                color: #AFBDC4; \n \
            } \n \
            \n \
            QRadioButton::indicator::unchecked { \n \
                background-color: " + self.theme.bg + "; \n \
                border: 1px solid #536D79; \n \
                border-radius: 7px; \n \
            } \n \
            \n \
            QRadioButton::indicator::checked { \n \
                    background-color: #53DD6C; \n \
                    border: 1px solid #536D79; \n \
                    border-radius: 7px; \n \
                } \n \
        "
        return self.QRadioButton

    def getQCheckBox(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QCheckBox = "\
            QCheckBox { \n \
                    color: #AFBDC4; \n \
                } \n \
            \n \
            QCheckBox::indicator::unchecked  { \n \
                    background-color: " + self.theme.bg + "; \n \
                    border: 1px solid #536D79; \n \
                } \n \
            \n \
            QCheckBox::indicator::checked, QTreeView::indicator::checked { \n \
                    background-color: #53DD6C; \n \
                    border: 1px solid #536D79; \n \
                } \n \
            \n \
            QCheckBox::indicator:disabled, QRadioButton::indicator:disabled, QTreeView::indicator:disabled { \n \
                    background-color: #444444;             \n \
                } \n \
            \n \
            QCheckBox::indicator::checked:disabled, QRadioButton::indicator::checked:disabled, QTreeView::indicator::checked:disabled {   \n \
                    background-color: #444444;  \n \
                } \n \
        "
        return self.QCheckBox

    def getQScrollBar(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QScrollBar = "\
            QScrollBar:horizontal { \n \
                    background: " + self.theme.bg + ";                 \n \
                    height: 10px; \n \
                    margin: 0; \n \
                } \n \
            \n \
            QScrollBar:vertical { \n \
                    background: " + self.theme.bg + ";                 \n \
                    width: 10px; \n \
                    margin: 0; \n \
                } \n \
            \n \
            QScrollBar::handle:horizontal { \n \
                    background: #37474F;                     \n \
                    min-width: 16px; \n \
                    border-radius: 5px; \n \
                } \n \
            \n \
            QScrollBar::handle:vertical { \n \
                    background: #37474F;                     \n \
                    min-height: 16px; \n \
                    border-radius: 5px; \n \
                } \n \
                 \n \
                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, \n \
            \n \
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { \n \
                    background: none;                                                 \n \
                } \n \
                 \n \
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal, \n \
            \n \
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {     \n \
                      border: none; \n \
                      background: none; \n \
                } \n \
        "
        return self.QScrollBar

    def getQPushButton(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QPushButton = "\
            QPushButton { \n \
                    background-color: transparent; \n \
                    color: " + self.theme.primary + "; \n \
                    border: 1px solid transparent; \n \
                    padding: 4px 22px; \n \
                } \n \
            \n \
            QPushButton:hover { \n \
                    color: #AFBDC4; \n \
                } \n \
            \n \
            QPushButton:pressed { \n \
                    color: #FFFFFF; \n \
                } \n \
        "
        return self.QPushButton

    def getQLineEdit(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QLineEdit = "\
            QLineEdit { \n \
                    background: transparent; \n \
                    border: 1px solid transparent; \n \
                    border-top: none; \n \
                    border-bottom: 2px solid " + accent + "; \n \
                    color: " + self.theme.primary + "; \n \
                } \n \
        "
        return self.QLineEdit

    def getQSpinBox(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QSpinBox = "\
            QSpinBox { \n \
                    background: transparent; \n \
                    border: 1px solid transparent; \n \
                    color: " + self.theme.secondary + "; \n \
                } \n \
        "
        return self.QSpinBox

    def getQTreeView(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QTreeView = "\
            QTreeView { \n \
                    background-color: " + self.theme.bg + "; \n \
                } \n \
        "
        return self.QTreeView

    def getQMenu(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QMenu = "\
            QMenu { \n \
                    background-color: " + self.theme.bg + "; \n \
                    color: " + self.theme.secondary + "; \n \
                } \n \
            \n \
            QMenu::item:selected { \n \
                    color: #AFBDC4; \n \
                } \n \
            \n \
            QMenu::item:pressed { \n \
                    color: #FFFFFF; \n \
                } \n \
            \n \
            QMenu::separator { \n \
                    height: 1px; \n \
                    background: transparent; \n \
                    margin-left: 10px; \n \
                    margin-right: 10px; \n \
                    margin-top: 5px; \n \
                    margin-bottom: 5px; \n \
                } \n \
        "
        return self.QMenu

    def getQMenuBar(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QMenuBar = "\
            QMenuBar { \n \
                    background-color: " + self.theme.bg + "; \n \
                    color: " + self.theme.secondary + "; \n \
                } \n \
            \n \
            QMenuBar::item { \n \
                    background: transparent; \n \
                } \n \
            \n \
            QMenuBar::item:disabled { \n \
                    color: gray; \n \
                } \n \
            \n \
            QMenuBar::item:selected { \n \
                    color: #AFBDC4; \n \
                } \n \
            \n \
            QMenuBar::item:pressed { \n \
                    color: #FFFFFF; \n \
                } \n \
        "
        return self.QMenuBar

    def getQToolBar(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QToolBar = "\
            QToolBar { \n \
                    background: " + self.theme.bg + "; \n \
                    border: 1px solid transparent; \n \
                } \n \
            \n \
            QToolBar:handle { \n \
                    background: transparent; \n \
                    border-left: 2px dotted " + accent + "; \n \
                    color: transparent; \n \
                } \n \
            \n \
            QToolBar::separator { \n \
                    border: 0; \n \
                } \n \
                 \n \
        "
        return self.QToolBar

    def getQStatusBar(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QStatusBar = "\
            QStatusBar { \n \
                    background-color: " + self.theme.bg + "; \n \
                } \n \
            \n \
            QStatusBar::item { \n \
                    color: " + self.theme.secondary + "; \n \
                    background-color: " + self.theme.bg + "; \n \
                } \n \
        "
        return self.QStatusBar

    def getQToolButton(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QToolButton = "\
            QToolButton:hover, QToolButton:pressed { \n \
                    background-color: transparent; \n \
                } \n \
            \n \
            QToolButton::menu-button { \n \
                    background(\'./images/downarrowgray.png\') center center no-repeat; \n \
                    background-color: " + self.theme.bg + "; \n \
                } \n \
            \n \
            QToolButton::menu-button:hover, QToolButton::menu-button:pressed { \n \
                    background-color: " + self.theme.bg + "; \n \
                } \n \
            \n \
            QToolButton {     \n \
                    color: " + self.theme.secondary + "; \n \
                } \n \
            \n \
            QToolButton:hover, QToolButton:pressed, QToolButton:checked { \n \
                    background-color: " + self.theme.bg + "; \n \
                } \n \
            \n \
            QToolButton:hover { \n \
                    color: #AFBDC4; \n \
                 \n \
                } \n \
            \n \
            QToolButton:checked, QToolButton:pressed { \n \
                    color: #FFFFFF; \n \
                } \n \
                 \n \
            \n \
            QToolButton { \n \
                    border: 1px solid transparent; \n \
                    margin: 1px; \n \
                } \n \
            \n \
            QToolButton:hover { \n \
                    background-color: transparent;                 \n \
                    border: 1px solid transparent; \n \
                } \n \
            \n \
            QToolButton[popupMode=\"1\"] {  \n \
                    padding-right: 20px;  \n \
                } \n \
            \n \
            QToolButton::menu-button { \n \
                    border-left: 1px solid transparent; \n \
                    background: transparent; \n \
                    width: 16px; \n \
                } \n \
            \n \
            QToolButton::menu-button:hover { \n \
                    border-left: 1px solid transparent; \n \
                    background: transparent; \n \
                    width: 16px; \n \
                } \n \
        "
        return self.QToolButton

    def getQAbstractScrollArea(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QAbstractScrollArea  = "\
            QAbstractScrollArea  {     \n \
                    border: 0; \n \
                } \n \
                 \n \
                /***************************************************************************** \n \
                Play around with these settings \n \
                *****************************************************************************/ \n \
                 \n \
                 \n \
        "
        return self.QAbstractScrollArea

    def getQDialogButtonBox(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QDialogButtonBox = "\
            QDialogButtonBox { \n \
                    button-layout: 0; \n \
                } \n \
        "
        return self.QDialogButtonBox

    def getQProgressBar(self, accent=None):
        if accent is None:
            accent = self.theme.accent

        self.QProgressBar = "\
            QProgressBar {                      \n \
                    border: 1px solid transparent ; \n \
                    background-color: transparent;  \n \
                    color: #CFD8DC;                 \n \
                }                                   \n \
            \n \
            QProgressBar::chunk {              \n \
                    background-color: #53DD6C; \n \
                    width: 20px;               \n \
                }                              \n \
            "
        return self.QProgressBar
