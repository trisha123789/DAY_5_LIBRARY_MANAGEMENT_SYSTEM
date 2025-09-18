#------------------------------LIBRARY MANAGEMENT SYSTEM------------------------------------------------
from supabase import create_client, Client
from dotenv import load_dotenv
import os
 
load_dotenv()
 
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)
 

def add_member(name1,email1):
    d = sb.table("members").insert({"name" : name1,"email": email1}).execute()
    return d

def add_book(title1,author1,category1,stock1):
    dt = sb.table("books").insert({"title" : title1,"author" : author1,"category" : category1 ,"stock" : stock1}).execute()
    return dt

def listing_books():
    
    
    dat= sb.table("books").select("*").execute()
    for d in dat.data:
        print(f"{d['book_id']}   |     {d['title']}    |    {d['author']}   |   {d['category']}  |   {d['stock']}")   

def search_author(auth):
    da = sb.table("books").select("*").eq("author",auth).execute()
    for d in da.data:
        print(f"{d['book_id']}   |     {d['title']}    |    {d['author']}   |   {d['category']}  |   {d['stock']}")
def search_member(id):
    da = sb.table("members").select("*").eq("member_id",id).execute()
    for d in da.data:
        print(f"{d['member_id']}  | {d['name']} | {d['email']} | {d['join_date']}")
def update_email(id,email_add):
    ds = sb.table("members").update({"email" : email_add}).eq("member_id",id).execute()
   
def delete_book(id):
    ds = sb.table("books").delete().eq("book_id",id).execute()
    
def delete_member(id):
    ds = sb.table("members").delete().eq("member_id",id).execute()    

if __name__ == "__main__":
    welcome = "WELCOME TO LIBRARAY MANAGEMENT SYSTEM"
    print(welcome)
    menu = """
    1. REGISTER A MEMBER
    2. ADD A NEW BOOK
    3.LIST ALL AVAILABLE BOOKS
    4.SEARCH BOOKS BY AUTHOR
    5. SHOW DETAILS BOF A MEMBER AND THEIR BORROWED BOOK
    6.UPDATE USER EMAIL
    7.DELETE A BOOK
    8.DELETE A USER 
    9.EXIT
    
    
    """
    while(user_input := input(menu)) != "9":
        if user_input == "1":
            name = input("Enter the name of the member: ").strip()
            email= input("Enter the email of the user ").strip()
            created = add_member(name,email)
            print("Inserted:", created)
        elif user_input == "2":
            
            title = input("ENTER THE TITLE OF THE BOOK :")
            author = input("ENTER THE NAME OF THE AUTHOR :")
            category = input("ENTER THE CATEGORY OF THE BOOK :")
            stock = int(input("ENTER THE STOCK OF THE BOOK:"))
            created = add_book(title,author,category,stock)
            print("BOOK ADDED SUCCESSFULLY",created)
            
        elif user_input == "3":
            print("LISTING ALL THE AVAILABLE BOOKS")
            listing_books()
        elif user_input == "4":
            author = input("Enter the author name to search :")
            search_author(author)
        elif user_input == "5":
            id = int(input("ENTER THE ID TO SEARCH THEIR DETAILS :"))
            search_member(id)
        elif user_input == "6":
            id = int(input("ENTER THE ID OF THE MEMBER TO UPDATE :"))
            email_add = input("ENTER THE NEW EMAIL ID:")
            update_email(id,email_add)
        elif user_input == "7":
            id = int(input("ENTER A BOOK ID TO DELETE:"))
            delete_book(id)
        elif user_input == "8":
                id = int(input("ENTER A MEMBER  ID TO DELETE:"))
                delete_member(id)
        else:
            print("INVALID INPUT....")