
import snowflake.connector
import requests
import streamlit
import pandas

from urllib.error import URLError

streamlit.title("hello, how are you?")

streamlit.header("header test")

streamlit.text("text test")

streamlit.header('🍌🥭  Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Display the table on the page.

my_fruit_list = my_fruit_list.set_index('Fruit')
                                        
# Let's put a pick list here so they can pick the fruit they want to include 
selected_list=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(selected_list)


streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response.json())


# donvert to pandas readable format 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# create dataframe
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("Fruit load list contains")
streamlit.dataframe(my_data_rows)



add_myfruit=streamlit.text_input("What fruit would you like to add:", "jackfr");
streamlit.write('Thanks for adding', add_myfruit)


