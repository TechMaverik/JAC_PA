from flask import request
import mapper
import random


def add_expenses():
    if request.method == "POST":

        id = random.randint(1, 999999999)
        account = request.form.get("account")
        description = request.form.get("description")
        expense_amt = request.form.get("amount")
        expense_type = request.form.get("type")
        is_consumerbill = request.form.get("bill")
        is_monthlyexpese = request.form.get("recurring")
        spend_to = request.form.get("spend_to")
        date = request.form.get("date")
        user = "Akhil"
        status = mapper.add_expense(
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
        )
        return status
    else:
        status = False
        return status


def add_account():
    if request.method == "POST":
        id = random.randint(1, 999999999)
        account = request.form.get("account")
        account_no = request.form.get("account_no")
        balance = request.form.get("balance")
        date = request.form.get("date")
        status = mapper.add_account(
            id,
            account,
            account_no,
            balance,
            date,
        )
        return status
    else:
        status = False
        return status


def delete_accounts():
    if request.method == "POST":
        id = request.form.get("ID")
        mapper.delete_accounts(id)


def delete_expenses():
    if request.method == "POST":
        id = request.form.get("ID")
        mapper.delete_expenses(id)


def cash_incoming_to_account():
    if request.method == "POST":
        account = request.form.get("account")
        id = request.form.get("ID")
        new_amount = request.form.get("amount")
        mapper.cash_incoming_to_account(account, id, new_amount)
