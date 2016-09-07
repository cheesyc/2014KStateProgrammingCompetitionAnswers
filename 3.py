from __future__ import division

x = 1
while x == 1:
    usd = int(input("How much in USD?"))
    fee = int(input("What is the fee percentage? (without the percentage sign)"))

    def convertion (usd, fee):
        trueFee = fee / 100
        w = trueFee * usd
        trueUSD = usd - w
        convert = trueUSD * 0.784
        return convert

    y = convertion(usd,fee)

    print "Your convertion rate is %s" %y

    inp = raw_input("Do you have another convertion that you want to make? (y/n)")

    if inp == "n":
        raise SystemExit
