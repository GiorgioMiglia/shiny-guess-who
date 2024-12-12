from shiny import App, render, ui, reactive
from faicons import icon_svg
import cards
import random

import random

def randomize_list(data_file):
    with open(data_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    random.shuffle(lines)
    return lines

data_file = "data.txt"
values = randomize_list(data_file)

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_action_button('load', 'Start Game '),
        ui.div(ui.input_dark_mode(mode='dark'),
               style='margin-top: auto;'),
        class_ = 'bg-indigo-100',
    ),
    ui.tags.link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css"),
    ui.output_ui("page"),
)

def server(input, output, session):

    @output(id='page')
    @render.ui
    @reactive.event(input.load)
    def load_cards():
        print(input.load())
        for val in values:
            btn_id = val.replace('.','_').replace('#', '0').replace('+', '1')
            cards.box_server('a', title=val, btn_id = btn_id)
        return ui.layout_column_wrap(*[cards.box_ui('a', title=val, btn_id = val.replace('.','_').replace('#', '0').replace('+', '1')) for val in values], width=1/10)
    
    

app = App(app_ui, server)
