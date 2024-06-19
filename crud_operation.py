import mysql.connector;
import streamlit as st;

# Establish connection with MySQL

mysql_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="CRUD"
);

# Check MYSQL database connection
mycursor = mysql_db.cursor()
print("MYSQL Connection is sucessfully established 🤝");


# Create streamlit app
def title():
    st.title("Data Manipulation with MYSQL"); #title 
    option= st.sidebar.selectbox("SELECT THE OPTION",("CREATE","READ","UPDATE","DELETE")); # options

   # create operation
    if option == "CREATE":
        st.subheader("CREATE A RECORD");
        USERNAME = st.text_input("ENTER THE USER NAME");
        PASSWORD = st.text_input("ENTER THE PASSWORD", type="password");
        if st.button("CREATE"):
            sql = "INSERT INTO CRUD_OPERATION(USERNAME,PASSWORD)VALUES(%s,%s)";
            value = (USERNAME,PASSWORD);
            mycursor.execute(sql,value);
            mysql_db.commit();
            st.success("RECORDS CREATED SUCCESSFULLY😀");
    # end of create operation
    
  # Read Operation
    elif option == "READ":
        st.subheader("READ A RECORD");
        USERID = st.text_input("ENTER THE USER ID");
        if st.button("READ"):
            sql = "SELECT * FROM CRUD_OPERATION WHERE USER_ID = %s";
            value = (USERID,)
            mycursor.execute(sql, value)
            record = mycursor.fetchone()
            if record:
                st.write(record);
                st.success("READ RECORD SUCCESSFULLY 👏")
            else:
                st.warning("NO RECORD FOUND 😒")
    # Emd of read operation

    # Start update operation
    elif option == "UPDATE":
        st.subheader("UPDATE A RECORD");
        USERID = st.text_input("ENTER THE USER ID");
        USERNAME = st.text_input("ENTER THE USERNAME");
        if st.button("UPDATE"):
            sql = "UPDATE CRUD_OPERATION SET USERNAME = %s WHERE USER_ID = %s";
            value = (USERNAME,USERID);
            mycursor.execute(sql,value);
            mysql_db.commit()
            st.success("UPDATE RECORD SUCESSFULLY 🙌");
        # End of the update operation

    # Start Delete operation    
    elif option == "DELETE":
        st.subheader("DELETE A RECORD");
        USERID = st.text_input("ENTER THE USER ID");
        if st.button("DELETE"):
            sql = "DELETE FROM CRUD_OPERATION WHERE USER_ID = %s";
            value = (USERID,)
            mycursor.execute(sql,value)
            mysql_db.commit();
            st.success("DELETE RECORD SUCESSFULLY 😒");
    # End of the operation
title()
