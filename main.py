import langchain_helper as lch
import streamlit as st

st.title("Generate Test Cases")

user_story = st.sidebar.text_area("User Story", height=200)
acceptance_criteria = st.sidebar.text_area("Acceptance Criteria", height=200)

if acceptance_criteria:
    response=lch.generate_test_cases(user_story, acceptance_criteria)
    st.markdown("\n\n\n "+response['test_cases'])
    #with st.expander("Click to expand", expanded=True): 
    #    st.markdown(response['test_cases'])