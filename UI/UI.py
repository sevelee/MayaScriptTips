# get maya 的主窗口
# ref:https://github.com/fredrikaverpil/pyvfx-boilerplate/blob/master/boilerplate.py
def _maya_main_window():
    """Return Maya's main window"""
    for obj in QtWidgets.qApp.topLevelWidgets():
        if obj.objectName() == 'MayaWindow':
            return obj
    raise RuntimeError('Could not find MayaWindow instance')