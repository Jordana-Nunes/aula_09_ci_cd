import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

    def test_soma():
        a = 3
        b = 5

        output = methods.test_soma(a,b)

        assert output == 8

    def test_sub():
        a = 3
        b = 5

        output = methods.test_sub()

        assert output == 2

    def test_multi():
        a = 3
        b = 5

        output = methods.test_multi()

        assert output == 15

    def test_div():
        a = 10
        b = 5

        output = methods.test_div()

        assert output == 2