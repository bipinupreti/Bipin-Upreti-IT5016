aus=int(input("enter the amount"));
nz=aus*0.95;
print("$",nz)

amount_to_convert=500
nz_to_aus_rate=0.95
nz_dollars=amount_to_convert

aus_dollars=nz_dollars*nz_to_aus_rate
print(" nz$ ",nz_dollars," au$ ",aus_dollars,sep="")
aus_dollars=amount_to_convert
nz_dollars=aus_dollars/nz_to_aus_rate
print(nz_dollars)