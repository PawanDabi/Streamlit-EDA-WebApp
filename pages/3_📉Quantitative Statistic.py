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
    st.header(":green[Quantitative Statistics]")
    st.subheader("Visualization for **:green[Numerical Data]**")
    numeric_columns = df.select_dtypes(['float64', 'float32', 'int32', 'int64']).columns
    select_columns = st.selectbox("**:green[Select a Column]**", numeric_columns)
    left_col, right_col, center_col, count_col = st.columns((2,2,2,2))
    with left_col:
        st.write("Column Name")
        st.write(df[[select_columns]])
    with right_col:
        st.write("No. of Missing Values are")
        st.write(df[[select_columns]].isna().sum())
    with center_col:
        st.write("Percentage of Missing Value are")
        st.write(df[[select_columns]].isna().sum() / len(df) * 100)
    with count_col:
        st.write("No of Non-Empty Values")
        st.write(df[[select_columns]].count())
    if select_columns:
        options = st.tabs(['Dist Plot', 'Line Plot', 'Histogram Plot', 'Scatter Plot', 'Box Plot', 'kde Plot'])
        with options[0]:
            dist_slider = st.slider(label="Number of distplot Bins", min_value=5, max_value=100, value=15)
            histo_size, ax = plt.subplots(figsize=(width, height))
            sns.distplot(df[select_columns], bins=dist_slider)
            plt.title("Numerical Data Distance Plot")
            buf = BytesIO()
            histo_size.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(histo_size)
            if st.button('Download Plot', key=31):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="Numeric_distance_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with options[1]:
            line_size, ax = plt.subplots(figsize=(width, height))
            sns.lineplot(df[select_columns])
            plt.title("Numerical Data Distance Plot")
            plt.grid()
            buf = BytesIO()
            line_size.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(line_size)
            if st.button('Download Plot', key=32):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="Numeric_line_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with options[2]:
            hist_slider = st.slider(label="Number of histogram Bins", min_value=5, max_value=100, value=15)
            hist_size, ax = plt.subplots(figsize=(width, height))
            sns.histplot(df[select_columns], bins=hist_slider, kde=True)
            plt.title("Numerical Data histogram Plot")
            plt.grid()
            buf = BytesIO()
            hist_size.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(hist_size)
            if st.button('Download Plot', key=33):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="Numeric_hist_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with options[3]:
            scatter_size, ax = plt.subplots(figsize=(width, height))
            sns.scatterplot(df[select_columns])
            plt.title("Numerical Data Scatter Plot")
            # plt.grid()
            buf = BytesIO()
            scatter_size.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(scatter_size)
            if st.button('Download Plot', key=34):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="Numeric_scatter_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with options[4]:
            boxplot_size, ax = plt.subplots(figsize=(width, height))
            sns.boxplot(df[select_columns])
            plt.title("Numerical Data Box Plot")
            buf = BytesIO()
            boxplot_size.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(boxplot_size)
            if st.button('Download Plot', key=35):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="Numeric_box_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
        with options[5]:
            heat_size, ax = plt.subplots(figsize=(width, height))
            sns.kdeplot(df[select_columns], common_grid=True)
            plt.title("Numerical Data KDE Plot")
            buf = BytesIO()
            heat_size.savefig(buf, format='png', bbox_inches='tight')
            buf.seek(0)
            plot_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot(heat_size)
            if st.button('Download Plot', key=36):
                st.markdown(
                    f'<a href="data:image/png;base64,{plot_base64}" download="Numeric_kde_plot.png">Download Plot as Image</a>',
                    unsafe_allow_html=True
                )
