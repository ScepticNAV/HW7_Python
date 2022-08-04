import ui
import base

def button_click():
    end = False
    while not end:
        choice = ui.choice_operation()
        if choice == '1':
            is_end = False
            while not is_end:
                base.write_base(ui.input_PC())
                if ui.repeat_input() == 'Нет':
                    is_end = True
        elif choice == '2':
            base.view_base()
        elif choice == '3':
            end = True