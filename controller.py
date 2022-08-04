import ui
import base
import export_base
import import_base

def button_click():
    end = False
    while not end:
        choice = ui.choice_operation()
        if choice == '1':
            is_end = False
            while not is_end:
                base.write_base(ui.input_user())
                if ui.repeat_input() == 'Нет':
                    is_end = True
        elif choice == '2':
            base.view_base()
        elif choice == '3':
            import_base.import_csv_format('import.csv')
        elif choice == '4':
            export_base.export_csv_format()
        elif choice == '5':
            end = True