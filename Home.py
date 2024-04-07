import streamlit as st
import functions
todos=functions.get_todos()
def add_todo():
    todo=st.session_state['new_todo']+'\n'
    todos.append(todo)
    functions.write_todos(todos)
#st.set_page_config(layout='wide')
st.title('This is a to Do-App')
st.subheader('We use this web-app to manage our daily todos')
st.write("Let's try <b>it:</b>")

st.text_input(label='Enter to do below:',placeholder='Write a To_Do.....'
              , on_change=add_todo,key='new_todo')

for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



