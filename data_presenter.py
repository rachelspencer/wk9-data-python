cupcake_invoices = open('CupcakeInvoices.csv')

# 2. Loop through and print each row of data in Cupcake Invoices.
for row in cupcake_invoices:
    print(row)

#3.Loop and print the cupcake types in Cupcake Invoices.
for row in cupcake_invoices:
    values = row.split(',')
    print(values[2])

#5. Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).
for row in cupcake_invoices:
    values = row.split(',')
    order_total = order_total + (int(values[3]) * float([-1]))

print(order_total)
     
#6. Loop through all the data, and print out the total for all invoices combined.
total = 0

for row in cupcake_invoices:
  values = row.split(',')
  total = total + (int(values[3]) * float(values[4]))

print(total)

#7.Close your open file.
cupcake_invoices.close