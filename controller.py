import modelFloat
import view

def button_push():
    modelFloat.init(view.getvalue(), view.getOperation(), view.getvalue())

    view.view_data(modelFloat.chooseOp())