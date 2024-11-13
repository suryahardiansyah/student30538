from shiny import App, render, ui, reactive
import matplotlib.pyplot as plt
import numpy as np

app_ui = ui.page_fluid(
    ui.panel_title("Histogram of 200 Draws from Normal with mean mu"),
    ui.input_slider("mu", "mean mu", 0, 100, 20), 
    ui.output_plot("my_hist"),
    ui.output_text_verbatim("my_sumstats")
)

def server(input, output, session):
    @reactive.calc
    def sample():
        return(np.random.normal(input.n(), 20, 100))

    @render.plot
    def my_hist():
        fig, ax = plt.subplots()
        ax.hist(sample(), bins=30, color='blue', alpha=0.7)
        return fig
    
    @render.text
    def my_sumstats():
        min_out = np.min(sample())
        max_out = np.max(sample())
        median_out = np.median(sample())
        return "Min:" + str(min_out) + ", Median: " + str(median_out), ", Max: " + str(max_out)

app = App(app_ui, server)
