from typing import List, Tuple
from database.ministatement import Ministatement

# Mini statement function for Flask
def ministatement(account:int) -> List[Tuple]:
    try:
        ministatement_obj = Ministatement()
        transactions = ministatement_obj.get_ministatement(account_no=account)
        if isinstance(transactions, list):
            return transactions
        return []
    except Exception as e:
        print(f"Error in ministatement function: {e}")
        return []

# Logout function for Flask
from flask import session, redirect

def logout_flask():
    session.clear()  # clear all session data
    return redirect("/login")
