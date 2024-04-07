import streamlit as st
import json
from datetime import datetime
from connection import save_entry, list_entries, user_input


def app():
    st.title("To-do list app")

    with st.form(key="todo_form", clear_on_submit=True):
        title = st.text_input("Title ", max_chars=64)
        description = st.text_area("Description", max_chars=528)
        due_date = st.date_input("Due Date")
        submit_button = st.form_submit_button("Submit")

        if submit_button:  # means its true
            taskdict = {
                "title": title,
                "description": description,
                "date_created": datetime.today().strftime("%Y-$n-%d"),
                "due_date": due_date.strftime("%Y-$n-%d"),
            }
            save_entry(taskdict)
            st.success("Task added sucessfully! ")
    view_button = st.button("List pending tasks")
    if view_button:
        tasks = list_entries()
        if tasks:  # if len(tasks) != 0
            for task in tasks:
                # loop
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.markdown(f"**Title** {task['title']}")
                with col2:
                    st.markdown(f"**Description** {task['description']}")
                with col3:
                    st.markdown(f"**Date Created** {task['date_created']}")
                with col4:
                    st.markdown(f"**Due Date** {task['due_date']}")


if __name__ == "__main__":
    app()
