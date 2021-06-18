import csv
def main():
    #calls the read_products and process_request functions
    products = read_products()
    for i in products:
        print(f'{i}  {products[i]}')
    requests = process_request()
    
  
   
def read_products():
    # Empty dictionary 
    products_dict = {}

    # Open products.csv file for reading and store its infomation
    # in the products dictionary.
    with open('products.csv', "rt") as products_file:
        

        # use the csv moduele to create a reader
        reader = csv.reader(products_file)
        
        #skip the first line (headings) in products.csv
        next(reader)

        #reads one row at a time
        for row in reader:

            # grabs the product number, name and price
            product_id = row[0]
            name = row[1]
            price = float(row[2])


            # store data in the products dictionary.
            products_dict[product_id] = [name, price]
            
    # print(products_dict)
    return products_dict
            


def process_request():
    # Open request.csv file for reading and store its infomation
    # in the products dictionary.
    with open('request.csv', "rt") as request_file:

        # use the csv moduele to create a reader
        reader = csv.reader(request_file)
        
        #skip the first line (headings) in products.csv
        next(reader)

        #reads one row at a time
        for row in reader:
            product_id = row[0]
            quantity = row[1]
            
            call = read_products()
            item_name = call[product_id][0]
            price = call[product_id][1]
            print(f'{item_name}, {quantity}, {price}')

    return 
            
            
if __name__ == "__main__":
    main()       

