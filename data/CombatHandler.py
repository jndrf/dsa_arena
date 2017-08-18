from Die import d6, d20

def main(player_blue, player_red):
    """
moep
    """

    #determine order
    order_of_battle = [player_blue, player_red]
    order_of_battle.sort(key = lambda x: x.getInitiative())
    assert(len(order_of_battle) == 2) #currently only two characters.
    first, second = order_of_battle

    no_deads = True

    while no_deads:
        if first.attackMelee() <= d20.roll() and not second.getDodge() < d20.roll():
            dmg = first.makeDamage()
            second.modifyLife(-dmg)
            print("A hit B for {} damage".format(dmg))

        if second.attackMelee() <= d20.roll() and not first.getDodge() < d20.roll():
            dmg = second.makeDamage()
            first.modifyLife(-dmg)
            print("B hit A for {} damage".format(dmg))

        no_deads = first.isAlive() and second.isAlive()

    print("yeah, its over")


if __name__ == "__main__":
    from BasePlayer import BasePlayer

    main(BasePlayer(), BasePlayer())
