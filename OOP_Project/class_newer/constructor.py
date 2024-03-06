stock = Stock()
daily = DailyStock(datetime(2024, 2, 15, 16, 30))


def create_cabana_and_locker():
    w01 = Cabana("W01", "S", "Wave Pool")  # Wave Pool Zone
    w02 = Cabana("W02", "S", "Wave Pool")
    w03 = Cabana("W03", "M", "Wave Pool")
    w04 = Cabana("W04", "M", "Wave Pool")
    w05 = Cabana("W05", "M", "Wave Pool")
    w06 = Cabana("W06", "M", "Wave Pool")
    w07 = Cabana("W07", "M", "Wave Pool")
    w08 = Cabana("W08", "M", "Wave Pool")
    w09 = Cabana("W09", "M", "Wave Pool")
    w10 = Cabana("W10", "S", "Wave Pool")
    w11 = Cabana("W11", "S", "Wave Pool")
    w12 = Cabana("W12", "S", "Wave Pool")
    w13 = Cabana("W13", "L", "Wave Pool")
    w14 = Cabana("W14", "S", "Wave Pool")
    w15 = Cabana("W15", "M", "Wave Pool")
    w16 = Cabana("W16", "M", "Wave Pool")
    w17 = Cabana("W14", "S", "Wave Pool")
    w18 = Cabana("W14", "S", "Wave Pool")
    w19 = Cabana("W14", "S", "Wave Pool")
    p05 = Cabana("P05", "S", "Wave Pool")
    p06 = Cabana("P06", "S", "Wave Pool")

    p01 = Cabana("P01", "S", "Activity and Relax")  # Activity and Relax Zone
    p02 = Cabana("P02", "S", "Activity and Relax")
    p03 = Cabana("P03", "M", "Activity and Relax")
    p04 = Cabana("P04", "M", "Activity and Relax")

    h01 = Cabana("H01", "S", "Activity and Relax")  # Hill Zone
    h02 = Cabana("H02", "S", "Activity and Relax")
    h03 = Cabana("H03", "S", "Activity and Relax")
    h04 = Cabana("H04", "M", "Activity and Relax")
    h05 = Cabana("H05", "M", "Activity and Relax")

    f01 = Cabana("F01", "M", "Family")  # Family Zone
    f02 = Cabana("F02", "S", "Family")
    f03 = Cabana("F03", "L", "Family")
    f04 = Cabana("F04", "S", "Family")
    f05 = Cabana("F05", "M", "Family")
    f06 = Cabana("F06", "M", "Family")
    k05 = Cabana("K05", "M", "Family")
    k06 = Cabana("K06", "M", "Family")
    k07 = Cabana("K07", "S", "Family")

    locker_m = Locker("M")  # Locker
    locker_l = Locker("L")


def create_ticket():
    full_day_ticket = Ticket("Full Day", 1, 699)
    senior_with_slides = Ticket("Senior", 1, 599)  # >= 60 y.o. and want to play slides
    free_child_ticket = Ticket("Child", 1)
    senior_pools_only = Ticket("SPD", 1)  # including pregnant and disabled
    group_for_4 = Ticket("Group", 4, 2599)
    group_for_6 = Ticket("Group", 6, 3779)
    group_for_8 = Ticket("Group", 8, 4879)
    group_for_10 = Ticket("Group", 10, 5999)


def create_customer_and_member():
    # Member
    # prae = Member('Prae', 'sirima26@gmail.com', '0912345678', date(2005, 3, 26), 'Thai')
    # louis = Member('Louis', 'manatsavin@gmail.com', '0923456789', date(2005, 4, 23), 'Thai')
    # beam = Member('Beam', 'ananthachai@gmail.com', '0934567890', date(2004, 9, 20), 'Thai')
    # som = Member('Som', 'ariya28@gmail.com', '0945678901', date(2004, 10, 28), 'Thai')

    # Customer
    james = Customer("James", "james123@gmail.com", "0812345678")
    yuji = Customer("Yuji", "yuji1234@gmail.com", "0823456789")
    irene = Customer("Irene", "irene123@gmail.com", "0834567890")
    charlotte = Customer("Charlotte", "charlotte@gmail.com", "0845678901")
    sharon = Customer("Sharon", "sharon12@gmail.com", "0856789012")
    rose = Customer("Rose", "rose1234@gmail.com", "0867890123")
    lucian = Customer("Lucian", "lucian123@gmail.com", "0878901234")
    zeno = Customer("Zeno", "zeno1234@gmail.com", "0889012345")
    apollo = Customer("Apollo", "apollo12@gmail.com", "0890123456")
    lucian = Customer("Lucian", "lucian123@gmail.com", "0801234567")
    dion = Customer("Dion", "dion1234@gmail.com", "0898765432")


w01 = Cabana("W01", "S", "Wave Pool")

create_cabana_and_locker()
create_ticket()
create_customer_and_member()
print(w01.price)
# print(daily.show_cabana())
