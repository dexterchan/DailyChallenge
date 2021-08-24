from __future__ import annotations
from pydantic import BaseModel
from typing import List
from functools import reduce
from fpdf import FPDF


class Bill(BaseModel):
    """
        Object contains data about a bill such as 
        total amount and period of the bill
    """
    amount: int
    period: str


class Flatmate(BaseModel):
    """
        Flatemate person who lives in the flat and share the bill
    """
    name: str
    days_in_house: int

    def pays(self, bill: Bill, all_flatmates: List[Flatmate]) -> float:

        total_days = reduce(lambda x, y: x + y,
                            list(map(lambda x: x.days_in_house, all_flatmates)))
        weight = self.days_in_house / total_days

        return bill.amount * weight
        pass


class Report(BaseModel):
    """
        Create a pdf report contains data about flatmates
        such as names, their due amount and the period of the bill
    """
    filename: str

    def generate(self, flatmates: List[Flatmate], bill: Bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add text
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=250, h=80, txt="Flatmates Bill", border=1, align='C', ln=2)
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=150, h=40, txt="March 2021", border=1)
        pdf.output(self.filename)
