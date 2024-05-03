import sqlite3
import database


def create_database():
    try:
        database.create_account_balance_table()
        database.create_expenses_table()
        return True
    except:
        return False


def view_expenses():

    with sqlite3.connect("jac_pa.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Expenses")
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    conn.close()
    return rows


def add_expense(
    id,
    account,
    description,
    expense_amt,
    expense_type,
    is_consumerbill,
    is_monthlyexpese,
    spend_to,
    date,
    user,
):
    """Add Expense"""

    with sqlite3.connect("jac_pa.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT into Expenses(Id ,account ,description ,expense_amt ,expense_type ,is_consumerbill ,is_monthlyexpese ,spend_to ,date, user ) Values (?,?,?,?,?,?,?,?,?,?)",
            (
                id,
                account,
                description,
                expense_amt,
                expense_type,
                is_consumerbill,
                is_monthlyexpese,
                spend_to,
                date,
                user,
            ),
        )
        conn.commit()
    conn.close()
    return True


def view_account():
    with sqlite3.connect("jac_pa.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * from Accounts")
        rows = cursor.fetchall()
        conn.commit()
    conn.close()
    for i in rows:
        print(i)
    return rows


def add_account(id, account, account_no, balance, date):
    with sqlite3.connect("jac_pa.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT into Accounts(Id , account , account_no, balance, date )values(?,?,?,?,?)",
            (
                id,
                account,
                account_no,
                balance,
                date,
            ),
        )
        conn.commit()
    conn.close()
    return True


def delete_accounts(Id):
    with sqlite3.connect("jac_pa.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE from Accounts where Id=?", (Id,))
        conn.commit()
    conn.close()
    return True


def delete_expenses(Id):
    with sqlite3.connect("jac_pa.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE from Expenses where Id=?", (Id,))
        conn.commit()
    conn.close()
    return True
