import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
st.sidebar.header("Information About Graph.")
graph_option = ["", "Bar Chart", "Barh(Horizontal Bar) Chart", "Histogram Chart",
                "Line Chart", "Box Chart", "Pie Chart", "Heat Map", "Dist Plot", "Line Plot", "Histogram Plot",
                "Scatter Plot", "Box Plot", "Kde Plot"]
op_column_name = st.sidebar.selectbox("**:green[Brief Description About Graph's]**", graph_option)
if op_column_name == 'Bar Plot':
    st.sidebar.write("**:green[{name}]**: A :red[bar chart] or bar graph is a chart or graph that presents categorical data with rectangular "
                     "bars with heights or lengths proportional to the values that they represent. "
                     "The bars plotted in :red[vertically].".format(name='Bar Plot'))
elif op_column_name == 'Barh(Horizontal Bar) Chart':
    st.sidebar.write("**:green[{name}]**: The :red[barh chart] is a chart of graph that presents categorical data with rectangular "
                     "bars with heights or lengths proportional to the values that they represent. "
                     "The bars plotted in :red[horizontally]".format(name='Barh(Horizontal Bar) Chart'))
elif op_column_name == 'Histogram Chart':
    st.sidebar.write("**:green[{name}]**: A :red[histogram] is a graph showing frequency distributions. "
                     "It is a graph showing the number of observations within each given interval.".format(name='Histogram Chart'))
elif op_column_name == 'Line Chart':
    st.sidebar.write("**:green[{name}]**: The :red[Line charts] work out of the box with matplotlib. "
                     "You can have multiple lines in a line chart, change color, "
                     "change type of line and much more. Matplotlib is a Python module for plotting. "
                     "Line charts are one of the many chart types it can create.".format(name='Line Chart'))
elif op_column_name == 'Box Chart':
    st.sidebar.write("**:green[{name}]**: A :red[Box Plot] is also known as Whisker plot is created to display "
                     "the summary of the set of data values having properties like minimum, first quartile, "
                     "median, third quartile and maximum".format(name='Box Chart'))
elif op_column_name == 'Pie Chart':
    st.sidebar.write("**:green[{name}]**: The :red[Pie charts] show the size of items (called wedge) in one data series, "
                     "proportional to the sum of the items. The data points in a pie chart are shown as a "
                     "percentage of the whole pie. Matplotlib API has a :red[pie()] function that generates "
                     "a pie diagram representing data in an array.".format(name='Pie Chart'))
elif op_column_name == 'Heat Map':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[Heat Map] is often desirable to show data which depends on two independent "
                     "variables as a color coded image plot. This is often referred to as a heatmap. "
                     "If the data is categorical, this would be called a categorical heatmap. "
                     "Matplotlib's imshow function makes production of such plots particularly easy.".format(name='Heat Map'))
elif op_column_name == 'Dist Plot':
    st.sidebar.write("**:green[{name}]**:  The seaborn :red[Distplot] or distribution plot, depicts the variation in the data distribution. "
                     "Seaborn Distplot represents the overall distribution of continuous data variables. "
                     "The Seaborn module along with the Matplotlib module is used to depict "
                     "the distplot with different variations in it.".format(name='Dist Plot'))
elif op_column_name == 'Line Plot':
    st.sidebar.write("**:green[{name}]**: The Seaborn :red[Line Plots] depict the relationship between continuous "
                     "as well as categorical values in a continuous data point format.".format(name='Line Plot'))
elif op_column_name == 'Histogram Plot':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[histogram Plot] is a classic visualization tool that represents the "
                     "distribution of one or more variables by counting the number of "
                     "observations that fall within discrete bins.". format(name='Histogram Plot'))
elif op_column_name == 'Scatter Plot':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[scatter plot] displays data between two continuous data. "
                     "It shows how one data variable affects the other variable. "
                     "A scatter plot can display data in different types of plots, both 2D and 3D.". format(name='Scatter Plot'))
elif op_column_name == 'Box Plot':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[box plot] is a very basic plot Boxplots are used to visualize distributions. "
                     "That is very useful when you want to compare data between two groups. "
                     "Sometimes a boxplot is named a box-and-whisker plot. "
                     "Any box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution.".format(name='Box Plot'))
elif op_column_name == 'Kde Plot':
    st.sidebar.write("**:green[{name}]**: The seaborn :red[Kde plot] is a Kernel Distribution Estimation Plot which depicts "
                     "the probability density function of the continuous or non-parametric data variables"
                     " i.e. we can plot for the univariate or multiple variables altogether". format(name='Kde Plot'))
st.sidebar.markdown("---")
st.sidebar.header("Visualization Width and Height.")
st.sidebar.write("**:green[Set Width and Height of Given Graph]**")
width = st.sidebar.slider("Plot Width", 1, 25, 9)
height = st.sidebar.slider("Plot Height", 1, 25, 4)

st.cache(persist=True)
if "df" in st.session_state:
    df = st.session_state.df
    missing_value_dataset = df.isna().sum()
    missing_value_ascen_dataset = df.isna().sum().sort_values()
    df_missing_percentage = df.isna().sum() / len(df) * 100
    df_missing_percentage_Ascending = df.isna().sum().sort_values() / len(df) * 100
    df_missing_percentage_Descending = df.isna().sum().sort_values(ascending=False) / len(df) * 100
    missing_value_descen_dataset = df.isna().sum().sort_values(ascending=False)
    empty_value = df.count()
    df_missing_non_empty_ascending = df.count().sort_values()
    df_missing_non_empty_descending = df.count().sort_values(ascending=False)
    st.header(":green[Qualitative Statistics or Quantitative Statistics]")
    st.subheader("Visualization for **:green[Categorical]** and **:green[Numerical Data]** of Given **:green[CSV]** ")
    visual_tabs = st.tabs(['Missing Value(Column) Plot', 'Missing Value Percentage Plot', 'Count Plot'])
    with visual_tabs[0]:
        inner_tabs = st.tabs(['Bar Plot', 'Barh Plot', 'Histogram Plot', 'Line Plot', 'Box Plot', 'Pie Plot', 'Heat Map'])
        with inner_tabs[0]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            fig, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Value Bar Graph per column")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='bar')
            # download plot
            buf = BytesIO()
            fig.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(fig)
            if st.button('Download Plot'):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="bar_graph.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
            tab = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with tab[0]:
                sort_ascen = missing_value_ascen_dataset[missing_value_ascen_dataset != 0]
                figure, ax = plt.subplots(figsize=(width, height))
                plt.title("Missing Value Bar Graph for per column")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='bar', width=0.4)
                # button_id = str(uuid.uuid4())
                buf = BytesIO()
                figure.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(figure)
                if st.button('Download Plot', key=1):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="ascending_bar_plot.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
            with tab[1]:
                sort_ascen = missing_value_descen_dataset[missing_value_descen_dataset != 0]
                fig_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Missing Value Bar Graph for per column")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='bar', width=0.4)
                buf = BytesIO()
                fig_1.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(fig_1)
                if st.button('Download Plot', key=2):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="descending_bar_plot.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
        with inner_tabs[1]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            fig_2, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Value Horizontal Bar Graph for per column")
            plt.ylabel("Column Names")
            plt.xlabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='barh')
            buf = BytesIO()
            fig_2.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(fig_2)
            if st.button('Download Plot', key=3):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="barh.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
            tab = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with tab[0]:
                sort_ascen = missing_value_ascen_dataset[missing_value_ascen_dataset != 0]
                fig_3, ax = plt.subplots(figsize=(width, height))
                plt.title("Missing Value Horizontal Bar Graph for per column")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='barh', width=0.4)
                buf = BytesIO()
                fig_3.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(fig_3)
                if st.button('Download Plot', key=4):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="ascen_barh.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
            with tab[1]:
                sort_ascen = missing_value_descen_dataset[missing_value_descen_dataset != 0]
                fig_4, ax = plt.subplots(figsize=(width, height))
                plt.title("Missing Value Horizontal Bar Graph for per column")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = sort_ascen.plot(kind='barh', width=0.4)
                buf = BytesIO()
                fig_4.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(fig_4)
                if st.button('Download Plot', key=5):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="descen_barh.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
        with inner_tabs[2]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_3, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Value Histogram Graph")
            dist = st.slider(label="Number of plot Bins", min_value=5, max_value=100, value=8)
            graph = missing_val.plot(kind='hist', bins=dist)
            buf = BytesIO()
            missing_val_3.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_val_3)
            if st.button('Download Plot', key=6):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="histogram_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )

        with inner_tabs[3]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_4, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Value Line Graph")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='line')
            plt.grid()
            buf = BytesIO()
            missing_val_4.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_val_4)
            if st.button('Download Plot', key=7):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="line_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[4]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_5, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Value Line Graph")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_val.plot(kind='box')
            buf = BytesIO()
            missing_val_5.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_val_5)
            if st.button('Download Plot', key=8):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="box_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[5]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_6, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Value Pie Chart")
            graph = missing_val.plot(kind='pie', autopct='%1.1f%%')
            buf = BytesIO()
            missing_val_6.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_val_6)
            if st.button('Download Plot', key=9):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="pie_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[6]:
            missing_val = missing_value_dataset[missing_value_dataset != 0]
            st.write(":green[Summary of Missing Value]")
            st.write(missing_val.describe())
            missing_val_7, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Value Line Graph")
            missing_value_dataset = sns.heatmap(df.corr(), linewidth=0.5, cmap='coolwarm')
            buf = BytesIO()
            missing_val_7.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_val_7)
            if st.button('Download Plot', key=10):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="heat_map.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
    with visual_tabs[1]:
        inner_tabs = st.tabs(['Bar Plot', 'Barh Plot', 'Histogram Plot', 'Line Plot', 'Box Plot', 'Pie Plot'])
        with inner_tabs[0]:
            missing_percent = df_missing_percentage[df_missing_percentage != 0]
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Percentage value of each column: Bar Graph")
            plt.xlabel("Column Names")
            plt.ylabel("Missing Values per Column in Numerical Data")
            graph = missing_percent.plot(kind='bar')
            buf = BytesIO()
            missing_plot.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_plot)
            if st.button('Download Plot', key=11):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="bar_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
            inner_tab_percent = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_percent[0]:
                set_sort = df_missing_percentage_Ascending[df_missing_percentage_Ascending != 0]
                set_ascend, ax = plt.subplots(figsize=(width, height))
                plt.title("Missing Percentage value of each column: Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='bar', width=0.4)
                buf = BytesIO()
                set_ascend.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(set_ascend)
                if st.button('Download Plot', key=12):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="ascen_bar.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
            with inner_tab_percent[1]:
                set_sort = df_missing_percentage_Descending[df_missing_percentage_Descending != 0]
                set_descend, ax = plt.subplots(figsize=(width, height))
                plt.title("Missing Percentage value of each column: Bar Graph")
                plt.xlabel("Column Names")
                plt.ylabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='bar', width=0.4)
                buf = BytesIO()
                set_descend.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(set_descend)
                if st.button('Download Plot', key=13):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="descen_bar.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
        with inner_tabs[1]:
            missing_percent = df_missing_percentage[df_missing_percentage != 0]
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_1, ax = plt.subplots(figsize=(width, height))
            plt.title("Missing Percentage value of each column: Bar Graph")
            plt.ylabel("Column Names")
            plt.xlabel("Missing Values per Column in Numerical Data")
            graph = missing_percent.plot(kind='barh')
            buf = BytesIO()
            missing_plot_1.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_plot_1)
            if st.button('Download Plot', key=14):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="barh_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
            inner_tab_percent = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_percent[0]:
                set_sort = df_missing_percentage_Ascending[df_missing_percentage_Ascending != 0]
                set_ascend_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Missing Percentage value of each column: Bar Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='barh', width=0.4)
                buf = BytesIO()
                set_ascend_1.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(set_ascend_1)
                if st.button('Download plot', key=15):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="ascen_barh.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
            with inner_tab_percent[1]:
                set_sort = df_missing_percentage_Descending[df_missing_percentage_Descending != 0]
                set_descend_1, ax = plt.subplots(figsize=(width, height))
                plt.title("Missing Percentage value of each column: Bar Graph")
                plt.ylabel("Column Names")
                plt.xlabel("Missing Values per Column in Numerical Data")
                graph_ascen = set_sort.plot(kind='barh', width=0.4)
                buf = BytesIO()
                set_descend_1.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(set_descend_1)
                if st.button('Download Plot', key=16):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="descen_barh.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
        with inner_tabs[2]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_2, ax = plt.subplots(figsize=(width, height))
            his = st.slider(label="Number of  Bins", min_value=5, max_value=100, value=8)
            graph = df_missing_percentage.plot(kind='hist', bins=his)
            plt.title("Missing Value Percentage of Histogram")
            buf = BytesIO()
            missing_plot_2.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_plot_2)
            if st.button('Download Plot', key=17):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="histogram.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[3]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_3, ax = plt.subplots(figsize=(width, height))
            graph = df_missing_percentage.plot(kind='line')
            plt.title("Missing Value Percentage of Line")
            plt.xlabel("Column Name")
            plt.grid()
            buf = BytesIO()
            missing_plot_3.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_plot_3)
            if st.button('Download Plot', key=18):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="line_chart.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[4]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_4, ax = plt.subplots(figsize=(width, height))
            graph = df_missing_percentage.plot(kind='box')
            buf = BytesIO()
            missing_plot_4.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_plot_4)
            if st.button('Download Plot', key=19):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="box_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[5]:
            st.write(":green[Summary of Missing Value Percentage]")
            st.write(missing_percent.describe())
            missing_plot_5, ax = plt.subplots(figsize=(width, height))
            graph = df_missing_percentage.plot(kind='pie', autopct='%1.1f%%')
            buf = BytesIO()
            missing_plot_5.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(missing_plot_5)
            if st.button('Download Plot', key=20):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="Pie_chart.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
    with visual_tabs[2]:
        inner_tabs = st.tabs(['Bar Plot', 'Barh Plot', 'Histogram Plot', 'Line Plot', 'Box Plot', 'Pie Chart'])
        with inner_tabs[0]:
            empty_missing, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='bar')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buf = BytesIO()
            empty_missing.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(empty_missing)
            if st.button('Download Plot', key=21):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="count_bar_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
            inner_tab_count = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_count[0]:
                empty_missing_count, ax = plt.subplots(figsize=(width, height))
                graph = df_missing_non_empty_ascending.plot(kind='bar')
                buf = BytesIO()
                empty_missing_count.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(empty_missing_count)
                if st.button('Download Plot', key=22):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="count_ascen_bar.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
            with inner_tab_count[1]:
                empty_missing_count_2, ax = plt.subplots(figsize=(width, height))
                graph = df_missing_non_empty_descending.plot(kind='bar')
                buf = BytesIO()
                empty_missing_count_2.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(empty_missing_count_2)
                if st.button('Download Plot', key=23):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="count_descen_bar.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
        with inner_tabs[1]:
            empty_missing_1, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='barh')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buf = BytesIO()
            empty_missing_1.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(empty_missing_1)
            if st.button('Download Plot', key=24):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="count_barh_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
            inner_tab_count = st.tabs(['Sorted in Ascending Order', 'Sorted in Descending Order'])
            with inner_tab_count[0]:
                empty_missing_barh, ax = plt.subplots(figsize=(width, height))
                graph = df_missing_non_empty_ascending.plot(kind='barh')
                buf = BytesIO()
                empty_missing_barh.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(empty_missing_barh)
                if st.button('Download Plot', key=25):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="count_ascen_barh.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
            with inner_tab_count[1]:
                empty_missing_barh_2, ax = plt.subplots(figsize=(width, height))
                graph = df_missing_non_empty_descending.plot(kind='barh')
                buf = BytesIO()
                empty_missing_barh_2.savefig(buf, format='png', bbox_inches='tight')
                buf.seek(0)
                plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
                st.set_option('deprecation.showPyplotGlobalUse', False)
                st.pyplot(empty_missing_barh_2)
                if st.button('Download Plot', key=26):
                    st.markdown(
                        f'<a href="data:image/png;base64,{plot_base64}" download="count_descen_barh.png">Download Plot as Image</a>',
                        unsafe_allow_html=True
                    )
        with inner_tabs[2]:
            empty_missing_2, ax = plt.subplots(figsize=(width, height))
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            slider = st.slider(label="Number of plot  Bins", min_value=5, max_value=100, value=15)
            graph = empty_value.plot(kind='hist', bins=slider)
            buf = BytesIO()
            empty_missing_2.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(empty_missing_2)
            if st.button('Download Plot', key=27):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="count_histogram_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[3]:
            empty_missing_3, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='line')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            plt.grid()
            buf = BytesIO()
            empty_missing_3.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(empty_missing_3)
            if st.button('Download Plot', key=28):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="count_line_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[4]:
            empty_missing_4, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='box')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buf = BytesIO()
            empty_missing_4.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(empty_missing_4)
            if st.button('Download Plot', key=29):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="count_box_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with inner_tabs[5]:
            empty_missing_5, ax = plt.subplots(figsize=(width, height))
            graph = empty_value.plot(kind='pie', autopct='%1.1f%%')
            st.write(":green[Summary of Count]")
            st.write(empty_value.describe())
            buf = BytesIO()
            empty_missing_5.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(empty_missing_5)
            if st.button('Download Plot', key=30):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="count_pie_chart.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
