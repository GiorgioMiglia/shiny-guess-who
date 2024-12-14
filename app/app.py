from shiny import App, render, ui, reactive
from faicons import icon_svg
import cards
import random

import random

def randomize_list(data_file):
    lines = ['JavaScript', 'Python', 'Java', 'C', 'C++', 'Ruby', 'PHP', 'C#', 'Swift', 'Kotlin', 'TypeScript', 'Go', 'Rust', 'Haskell', 'Lisp', 'Lua', 'Scala', 'Scheme', 'Brainfuck', 'Whitespace', 'Flutter', 'React', 'Vue.js', 'Angular', 'Svelte', 'Next.js', 'Nuxt.js', 'Ember.js', 'Backbone.js', 'Meteor']
    random.shuffle(lines)
    return lines

data_file = "data.txt"
values = randomize_list(data_file)

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_slider('cols', 'How many elements on each row?', min=1, max=10, value =6, step = 1),
        ui.input_action_button('load', 'Start Game '),
        ui.div(ui.input_dark_mode(mode='dark'),
               style='margin-top: auto;'),
        id = 'sidebar',
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
        ui.update_sidebar('sidebar', show = False)
        ui.update_action_button('load', label = 'Restart game')
        for val in values:
            btn_id = val.replace('.','_').replace('#', '0').replace('+', '1')
            cards.box_server('a', title=val, btn_id = btn_id)
        return ui.layout_column_wrap(*[cards.box_ui('a', title=val, btn_id = val.replace('.','_').replace('#', '0').replace('+', '1')) for val in values], width=1/input.cols())
    
    

app = App(app_ui, server)
