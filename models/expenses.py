from pydantic import BaseModel


class expenses(BaseModel):
    id: int
    account: str
    description: str
    expense_amt: str
    expense_type: str
    is_consumerbill: str
    is_monthlyexpense: str
    spend_to: str
    date: str
    user: str
