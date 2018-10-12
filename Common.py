# 常用import
import maya.cmds as cmds
from pymel.core import *

# 带ui的import
QtVersion = cmds.about(qtVersion=True)

if QtVersion.startswith("4") or type(QtVersion) not in [str, unicode]:
    from PySide import QtGui
    from PySide import QtCore
    from PySide import QtWidgets
    from PySide import QtUiTools

else:
    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets
    from PySide2 import QtUiTools

# 更科学一点的方式
try:
    from PySide2 import QtGui
    from PySide2 import QtCore
    from PySide2 import QtWidgets
    from PySide2 import QtUiTools
    from shiboken2 import wrapInstance
except ImportError:
    from PySide import QtGui
    from PySide import QtCore
    from PySide import QtWidgets
    from PySide import QtUiTools
    from shiboken import wrapInstance