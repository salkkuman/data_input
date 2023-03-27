import streamlit as st
import pandas as pd
import altair as alt


def main():
    st.title("Time Series Input App")
    
    # Load existing data from file
    try:
        df = pd.read_csv("user_data.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Name", "Date", "Value"])
    
    # Get user inputs
    name = st.text_input("Time Series Name:")
    date = st.date_input("Date:")
    value = st.number_input("Value:", step=0.1)
    
    # Add data to dataframe
    if st.button("Add Time Series"):
        new_row = {"Name": name, "Date": date, "Value": value}
        df = df.append(new_row, ignore_index=True)
        df.to_csv("user_data.csv", index=False)
        st.success(f"Time series '{name}' added!")
    
    # Plot data as a line chart
    if not df.empty:
        unique_names = df["Name"].unique()
        for name in unique_names:
            chart_data = df[df["Name"] == name]
            chart = (
                alt.Chart(chart_data)
                .mark_line()
                .encode(
                    x="Date:T",
                    y="Value:Q",
                )
                .properties(title=name)
            )
            st.altair_chart(chart, use_container_width=True)
    
    # Show existing data
    if not df.empty:
        st.subheader("Existing Time Series")
        st.write(df)


if __name__ == "__main__":
    main()
