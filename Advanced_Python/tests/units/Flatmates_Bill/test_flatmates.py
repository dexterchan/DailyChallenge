from Flatmates_Bill.model import *

bill: Bill = Bill(
    amount=120,
    period="March 2021"
)

john: Flatmate = Flatmate(
    name="John",
    days_in_house=10
)

marry: Flatmate = Flatmate(
    name="Mary",
    days_in_house=30
)

si: Flatmate = Flatmate(
    name="si",
    days_in_house=10
)


def test_bill():
    print(bill)
    flatmates_list = [john, marry, si]
    print(john.pays(bill=bill, all_flatmates=flatmates_list))
    print(marry.pays(bill=bill, all_flatmates=flatmates_list))
