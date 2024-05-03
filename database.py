import sqlite3
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="jac_pa.log", encoding="utf-8", level=logging.DEBUG)


def create_expenses_table():
    """Create expenses table"""
    con = sqlite3.connect("jac_pa.db")
    con.execute(
        "Create table Expenses(Id VARCHAR,account VARCHAR,description VARCHAR,expense_amt VARCHAR,expense_type VARCHAR,is_consumerbill VARCHAR,is_monthlyexpese VARCHAR,spend_to VARCHAR,date VARCHAR,user VARCHAR)"
    )
    con.close()
    logging.info(msg="Expenses Table Created")


def create_account_balance_table():
    """Create account balance table"""
    con = sqlite3.connect("jac_pa.db")
    con.execute(
        "Create table Accounts(Id VARCHAR, account VARCHAR,account_no VARCHAR, balance VARCHAR, date VARCHAR)"
    )
    con.close()
    logging.info(msg="Account Balance Table Created")


# create_account_balance_table()
# create_expenses_table()
