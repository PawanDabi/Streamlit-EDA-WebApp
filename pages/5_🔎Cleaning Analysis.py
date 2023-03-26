import pandas as pd
import streamlit as st
st.title(":green[Cleaning Analysis of DataSet]")
file_upload_1 = st.file_uploader(" ", type=['CSV'])
if file_upload_1 is not None:
    df = pd.read_csv(file_upload_1)
    st.subheader("**:red[{}]** dataSet are . . . ".format(file_upload_1.name))
    st.write(df)
    st.write("The Shape of file is : ",df.shape)
    st.header("New DataSet with **:green[Missing Values]** Removed / :green[Cleaned DataSet]")
    df.dropna(axis=0, inplace=True)
    df.to_csv(file_upload_1.name, index=False)
    st.write(df)
    st.write("The Shape of file is: ",df.shape)
    st.download_button("Download CSV File", df.to_csv(), file_name='Column csv file.csv', mime='text/csv')
    st.stop()
