import pandas as pd
import streamlit as st
st.set_page_config(page_title="Exploratory Data Analysis WebApp Using Streamlit",
    page_icon="https://cdn-icons-png.flaticon.com/512/3090/3090011.png",
    layout="wide",
    initial_sidebar_state="auto"
    )
st.cache(persist=True)
st.sidebar.header("Operations on Given DataSet.")
option_name = ["", "Head", "Tail", "Summery", "Info", "Column Name", "Row No", "Column No",
               "Numeric Data", "Missing Values", "Missing Values per Column", "Missing Value(Column %)", "Count"]

op_column_name = st.sidebar.selectbox("**:green[Information About Operations on Given DataSet]**", option_name)
if op_column_name == 'Head':
    st.sidebar.write("**:green[{name}]**:  The :red[head()] method returns the first 5 rows if a number is not specified. "
                     .format(name='Head'))
elif op_column_name == 'Tail':
    st.sidebar.write("**:green[{name}]**: The :red[tail()] method returns the last 5 rows if a number is not specified. "
                     .format(name='Tail'))
elif op_column_name == 'Summery':
    st.sidebar.write("**:green[{name}]**:  The :red[describe()] method returns description of the data in the DataFrame. "
                     "If the DataFrame contains numerical data " .format(name='Summery'))
elif op_column_name == 'Info':
    st.sidebar.write("**:green[{name}]**: The :red[info()] method prints information about the DataFrame. "
                     "The information contains the number of columns, column labels, column data types, "
                     "memory usage, range index, and the number of cells in each column (non-null values).".format(name='Info'))
elif op_column_name == 'Column Name':
    st.sidebar.write("**:green[{name}]**:  It can be thought of as a dict-like container for Series objects. "
                     "This is the primary data structure of the Pandas. :red[DataFrame.columns] columns attribute return the column "
                     "labels of the given Dataframe.".format(name='Column Name'))
elif op_column_name == 'Row No':
    st.sidebar.write("**:green[{name}]**: The :red[DataFrame.shape[0]] shows the number of rows in DataSet.".format(name='Row No'))
elif op_column_name == 'Column No':
    st.sidebar.write("**:green[{name}]**: The :red[DataFrame.shape[1]] shows the number of columns in dataset".format(name='Column No'))
elif op_column_name == 'Numeric Data':
    st.sidebar.write("**:green[{name}]**: The :red[select_dtypes()] method returns a new DataFrame that includes/excludes columns of "
                     " The specified dtype(s)." "Note: You must specify at least one of the parameters include and/or exclude, "
                     "or else you will get an error.".format(name='Numeric Data'))
elif op_column_name == 'Missing Values':
    st.sidebar.write("**:green[{name}]**: The :red[isna()] method returns a DataFrame object where all the values "
                     "are replaced with a Boolean value True for NA (not-a-number) values, and otherwise False.".format(name='Missing Values'))
elif op_column_name == 'Missing Values per Column':
    st.sidebar.write("**:green[{name}]**: The :red[isna().sum()] returns the number of missing values in each column."
                     " The :red[isna().sum().sort_values()], shows the missing value in ascending order and "
                     " The :red[isna().sum().sort_values(ascending=False)], shows the missing value in descending order."
                     .format(name='Missing Values per Column'))
elif op_column_name == 'Missing Value(Column %)':
    st.sidebar.write("**:green[{name}]**: The :red[isna().sum()/ len(data) * 100] will shows the percentage of missing value of each column. "
                     " The :red[isna().sum().sort_values() / len(data) * 100], shows the percentage of missing value of each column in ascending order and "
                     " The :red[isna().sum().sort_values(ascending=False) / len(data) * 100], shows the percentage of missing value of each column in descending order"
                     .format(name='Missing Value(Column %)'))
elif op_column_name == 'Count':
    st.sidebar.write("**:green[{name}]**: The :red[count()] method counts the number of not empty values for each row, or column".format(name='Count'))


st.cache(persist=True)
st.title(":green[Streamlit EDA] : A :red[WebApp] for Efficient :green[Data Analysis] ")
st.cache(persist=True)
file_upload = st.file_uploader("", type=['CSV'])
if file_upload is not None:
    df = pd.read_csv(file_upload)
    st.session_state.df = df
    st.session_state.file_upload=file_upload
    st.subheader("**:red[{}]** dataSet are . . . ".format(file_upload.name))
    st.write(df)
    st.markdown("---")
    st.header("Basic Operation on Given **:green[CSV]** DataSet File . . . . ")
    tabs = st.tabs(["Head DataSet", "Tail DataSet", "Summary", "Columns", "Row/Column No.", "Numeric Data Column",
    "Missing Values", "Missing Values per Column", "Missing Value(%)", "Count"])
    with tabs[0]:
        number_head = st.number_input(":green[Enter the No. of Head Rows] ", step=0, format='%d')
        head_dataset = df.head(number_head)
        st.write(head_dataset)
        st.download_button("Download CSV File", head_dataset.to_csv(), file_name='head_dataset.csv', mime='text/csv')
    with tabs[1]:
        number_tail = st.number_input(":green[Enter the No. of Tail Rows]  ", step=0, format='%d')
        tail_dataset = df.tail(number_tail)
        st.write(tail_dataset)
        st.download_button("Download CSV File", tail_dataset.to_csv(), file_name='tail_dataset.csv', mime='text/csv')
    with tabs[2]:
        num = ['float64', 'int64']
        numeric_summary = df.describe(include=num)
        st.write(":green[Summary for Numeric Columns]")
        st.write(numeric_summary)
        st.download_button("Download CSV File", numeric_summary.to_csv(), file_name='numeric_dataset.csv', mime='text/csv')
        cat = 'object'
        cat_summary = df.describe(include=cat)
        st.write(":green[Summary for Categorical Column]")
        st.write(cat_summary)
        st.download_button("Download CSV File", cat_summary.to_csv(), file_name='catgorical_dataset.csv', mime='text/csv')
    with tabs[3]:
        st.write(":green[Name of Columns] in DataSet: ")
        st.write(df.columns)
    with tabs[4]:
        st.write("No. of :green[Row] in DataSet: ")
        st.write(df.shape[0])
        st.write("No. of :green[Columns] in DataSet: ")
        st.write(df.shape[1])
    with tabs[5]:
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        no_of_numeric = df.select_dtypes(include=numerics)
        st.write("No of :green[Numeric Data] in DataSet: ")
        st.write(len(no_of_numeric.columns))
        st.write(no_of_numeric)
        st.download_button("Download CSV File", no_of_numeric.to_csv(), file_name='numeric_dataset.csv', mime='text/csv')
    with tabs[6]:
        st.write(":green[Column Name Contains Missing Value]")
        miss_col = df.columns[df.isnull().any()]
        st.write(miss_col)
        empty_dataset = df.isnull()
        st.write(empty_dataset)
        st.download_button("Download CSV File", empty_dataset.to_csv(), file_name='missing_dataset.csv', mime='text/csv')
    with tabs[7]:
        st.write("Shows the :green[Missing Values Per Columns] in DataSet: ")
        missing_value_dataset = df.isna().sum()
        st.write(missing_value_dataset)
        st.download_button("Download CSV File", missing_value_dataset.to_csv(), file_name='missing_column_dataset.csv', mime='text/csv')
        sort_data = st.tabs(["Sort in Ascending Order", "Sort in Descending Order"])
        with sort_data[0]:
            st.write("Sorted in :green[Ascending Order] from DataSet ")
            missing_value_ascen_dataset = df.isna().sum().sort_values()
            st.write(missing_value_ascen_dataset)
            st.download_button("Download CSV File", missing_value_ascen_dataset.to_csv(), file_name='missing_column_ascen_dataset.csv',
                               mime='text/csv')
        with sort_data[1]:
            st.write("Sorted in :green[Descending Order] from DataSet ")
            missing_value_descen_dataset = df.isna().sum().sort_values(ascending=False)
            st.write(missing_value_descen_dataset)
            st.download_button("Download CSV File", missing_value_descen_dataset.to_csv(), file_name='missing_column_descen_dataset.csv',
                               mime='text/csv')
    with tabs[8]:
        st.write("Show the :green[Percentage] of Missing Values of Each Column: ")
        df_missing_percentage = df.isna().sum() / len(df) * 100
        st.write(df_missing_percentage)
        st.download_button("Download CSV File", df_missing_percentage.to_csv(), file_name='percentage_column_dataset.csv',
                           mime='text/csv')
        missing_value_sorted = st.tabs(["Sort in Ascending Order", "Sort in Descending Order"])
        with missing_value_sorted[0]:
            df_missing_percentage_Ascending = df.isna().sum().sort_values() / len(df) * 100
            st.write("Shows the Sorted :green[Percentage Missing Value] in :green[Ascending Order]:")
            st.write(df_missing_percentage_Ascending)
            st.download_button("Download CSV File", df_missing_percentage_Ascending.to_csv(),
                               file_name='percentage_column_ascending_dataset.csv',
                               mime='text/csv')
        with missing_value_sorted[1]:
            df_missing_percentage_Descending = df.isna().sum().sort_values(ascending=False) / len(df) * 100
            st.write("Shows the Sorted :green[Percentage Missing Value] in :green[Descending Order]: ")
            st.write(df_missing_percentage_Descending)
            st.download_button("Download CSV File", df_missing_percentage_Descending.to_csv(),
                               file_name='percentage_column_descending_dataset.csv',
                               mime='text/csv')

    with tabs[9]:
        st.write("Shows the :green[Non Empty Values] of Each Column and Row in DataSet:")
        empty_value = df.count()
        st.write(empty_value)
        st.download_button("Download CSV File", empty_value.to_csv(),
                           file_name='empty_value.csv',
                           mime='text/csv')
        missing_value_sort = st.tabs(['Sort in Ascending Order', 'Sort in Descending Order'])
        with missing_value_sort[0]:
            df_missing_non_empty_ascending = df.count().sort_values()
            st.write("Shows the Sorted :green[Non Empty Value] in :green[Ascending Order]: ")
            st.write(df_missing_non_empty_ascending)
            st.download_button("Download CSV File", df_missing_non_empty_ascending.to_csv(),
                               file_name='df_missing_non_empty_ascending.csv',
                               mime='text/csv')
        with missing_value_sort[1]:
            df_missing_non_empty_descending = df.count().sort_values(ascending=False)
            st.write("Shows teh Sorted :green[Non Empty Value] in :green[Descending Order]: ")
            st.write(df_missing_non_empty_descending)
            st.download_button("Download CSV File", df_missing_non_empty_descending.to_csv(),
                               file_name='df_missing_non_empty_descending.csv',
                               mime='text/csv')
else:
    st.write(" ")
