# import streamlit as st
# from scrape import (scraper, extract_text, 
#                     clean_body_content, split_dom_content)
# from parse import parse_with_gemini
# st.title("AI Web Scraper")
# url = st.text_input("Enter the URL to scrape:")

# if st.button("Scrape Site"):
#     st.write(f"Scraping {url}...")
#     scraper_result = scraper(url)
#     body_content = extract_text(scraper_result)
#     cleaned_content = clean_body_content(body_content)
    
#     st.session_state.dom_content = cleaned_content
#     with st.expander("View DOM Content"): #this is like a dropdown that will expand show u the dom content
#         st.text_area("DOM Content", cleaned_content, height=300)

# if 'dom_content' in st.session_state:
#     parse_description = st.text_area("What would you like to parse?")
#     if st.button("Parse Content"):
#         if parse_description:
#             st.write("Parsing content...")
#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             parsed_result = parse_with_gemini(dom_chunks, parse_description)
#             st.write(parsed_result)

import streamlit as st
from scrape import (scraper, extract_text,
                    clean_body_content, split_dom_content)
from parse import parse_with_gemini
import pandas as pd # Import pandas for CSV handling

st.set_page_config(layout="wide") # Optional: Use wide layout for better display

st.title("AI Web Scraper")

# Section for URL input and scraping
with st.container():
    url = st.text_input("Enter the URL to scrape:")
    if st.button("Scrape Site"):
        st.info(f"Scraping {url}...")
        try:
            scraper_result = scraper(url)
            body_content = extract_text(scraper_result)
            cleaned_content = clean_body_content(body_content)

            st.session_state.dom_content = cleaned_content
            st.success("Scraping complete!")
            with st.expander("View DOM Content"):
                st.text_area("DOM Content", cleaned_content, height=300)
        except Exception as e:
            st.error(f"Error during scraping: {e}")
            if 'dom_content' in st.session_state:
                del st.session_state.dom_content # Clear previous content on error
            if 'parsed_data' in st.session_state:
                del st.session_state.parsed_data # Clear parsed data on error


# Section for parsing and download
if 'dom_content' in st.session_state and st.session_state.dom_content:
    st.markdown("---") # Separator
    st.header("Parse Content")

    with st.form(key="parse_form"):
        parse_description = st.text_area("What information would you like to extract from the DOM content?",
                                          help="e.g., 'All product names and their prices', 'The main article text', 'A list of all links on the page'.")
        parse_submit_button = st.form_submit_button("Parse Content")

        if parse_submit_button:
            if parse_description:
                st.info("Parsing content with Gemini...")
                dom_chunks = split_dom_content(st.session_state.dom_content)
                try:
                    parsed_result = parse_with_gemini(dom_chunks, parse_description)
                    st.success("Parsing complete!")
                    st.write("### Parsed Result:")
                    st.write(parsed_result) # Display the parsed result

                    # Store parsed_result in session_state to make it available for download
                    st.session_state.parsed_data = parsed_result

                except Exception as e:
                    st.error(f"Error during parsing: {e}")
                    if 'parsed_data' in st.session_state:
                        del st.session_state.parsed_data # Clear parsed data on error
            else:
                st.warning("Please enter a description for parsing.")

    # Add download button if parsed_data exists in session_state
    if 'parsed_data' in st.session_state and st.session_state.parsed_data:
        st.markdown("---") # Separator
        st.header("Download Parsed Data")
        try:
            # Convert the parsed_result to a pandas DataFrame
            # *** IMPORTANT: Adjust this part based on the actual structure of your parsed_result ***
            if isinstance(st.session_state.parsed_data, dict):
                df = pd.DataFrame([st.session_state.parsed_data])
            elif isinstance(st.session_state.parsed_data, list):
                # Ensure all elements in the list are dictionaries for DataFrame creation
                if all(isinstance(item, dict) for item in st.session_state.parsed_data):
                    df = pd.DataFrame(st.session_state.parsed_data)
                else:
                    # If not all items are dicts, convert to string for display/download
                    df = pd.DataFrame({"Parsed Content": [str(st.session_state.parsed_data)]})
            else:
                # If it's a string or other simple type, put it in one column
                df = pd.DataFrame({"Parsed Content": [st.session_state.parsed_data]})

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Parsed Data as CSV",
                data=csv,
                file_name="parsed_data.csv",
                mime="text/csv",
                key="download_csv_button" # Unique key for the button
            )
        except Exception as e:
            st.error(f"Could not convert data to CSV for download: {e}")
