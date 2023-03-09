
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

def get_fruitvice(thisfruit):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+thisfruit)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select fruit for information")
  else:
    streamlit.dataframe(get_fruitvice(fruit_choice))

except URLError as e:
  streamlit.error()



def get_fruit_load():
  with my_cnx.cursor() as my_cur:
    mycur.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()
  
if streamlit.button('Get fruit load list'): 
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load()
  streamlit.dataframe(my_data_rows)
  
  
streamlit.stop()  


add_myfruit=streamlit.text_input("What fruit would you like to add:", "jackfr");
streamlit.write('Thanks for adding', add_myfruit)


