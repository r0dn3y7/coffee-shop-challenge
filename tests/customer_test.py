from customer import Customer

def test_customer_name_validation():
    c = Customer("Alex")
    assert c.name == "Alex"
    
    try:
        Customer("ThisNameIsWayTooLongToBeValid")
    except ValueError:
        assert True
    else:
        assert False
