from shiny import render, ui, reactive, module

@module.ui
def box_ui(title, btn_id):
    return ui.div(ui.input_action_button(id=btn_id, label=title, class_= 'bg-green-600 w-full h-40 text-xl'), 
                   ui.output_ui(f"card_{btn_id}"),
                   id=f'c_{btn_id}',
                   class_= "border-none")

@module.server
def box_server(input, output, session, title, btn_id):
    
    @output(id=f"card_{btn_id}")
    @render.ui
    @reactive.event(input[f"{btn_id}"])
    def toggle_button():
        ui.remove_ui(f"#a-{btn_id}", immediate=True)
        
        return ui.input_action_button(id=btn_id+'w', label=title, class_= 'bg-red-700 h-40 w-full text-xl')