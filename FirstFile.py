# noinspection PyUnresolvedReferences
from _ast import Assert
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys
# noinspection PyUnresolvedReferences
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
# noinspection PyUnresolvedReferences
import unittest
# noinspection PyUnresolvedReferences
import time



class All_case(unittest.TestCase):

    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()

    def setUp(self):
        pass

    def test_a_first(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        elem = driver.find_element_by_class_name("login")
        elem.click()
        addrem = driver.find_element_by_id("email")
        addrem.send_keys("szymon.burko@vp.pl")
        passwrd= driver.find_element_by_id("passwd")
        passwrd.send_keys("qwerty")
        signin = driver.find_element_by_id("SubmitLogin")
        signin.click()
        time.sleep(5)
        self.assertIn("logout", driver.page_source)
       # driver.quit()

    def test_my_orders(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        order = driver.find_element_by_xpath('//*[@title="My orders"]')
        order.click()
        time.sleep(3)
        orhist = driver.find_element_by_xpath('//div[@id="block-history"]')
        if orhist.is_displayed():
            pass
        else:
            self.fail("Error in diplaying order history")

    def test_best_sellers(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        best = driver.find_element_by_xpath('//*[@title="Best sellers"]')
        best.click()
        time.sleep(2)
        bestsel = driver.find_element_by_xpath('//h1[@class="page-heading product-listing"]')
        self.assertEqual(bestsel.text, "BEST SELLERS")

    def test_contac_us(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        con = driver.find_element_by_id("contact-link")
        con.click()
        time.sleep(5)
        addrem = driver.find_element_by_id("email")
        addrem.clear()
        addrem.send_keys("szymon.burko@vp.pl")
        idconselect = driver.find_element_by_id("id_contact")
        idconselect.click()
        for option in idconselect.find_elements_by_tag_name('option'):
            if option.text == 'Customer service':
                option.click()
                break
        idorder = driver.find_element_by_xpath('//*[@name="id_order"]')
        idorder.click()
        for option in idorder.find_elements_by_tag_name('option'):
            if option.text == 'FYLDVQWDB - 08/09/2017':
                option.click()
                break
        time.sleep(5)
        prodid = driver.find_element_by_id("17949_order_products")
        prodid.click()
        for option in  prodid.find_elements_by_tag_name('option'):
            if option.text == 'Printed Dress - Color : Beige, Size : L':
                option.click()
                break
        msg = driver.find_element_by_id("message")
        msg.send_keys("Wrong product")
        send = driver.find_element_by_id("submitMessage")
        send.click()
        time.sleep(5)

    def test_In_stock(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        prod = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/2/12-home_default.jpg"]')
        prod.click()
        color = driver.find_element_by_id("color_13")
        color.click()
        time.sleep(2)
        stock = driver.find_element_by_id("availability_statut")
        if stock.is_displayed():
            pass
        else:
            self.fail()

    def test_wishlist(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        prod = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/6/16-home_default.jpg"]')
        prod.click()
        wish = driver.find_element_by_id("wishlist_button")
        wish.click()
        time.sleep(1)
        msgbox = driver.find_element_by_class_name("fancybox-error")
        if msgbox.is_displayed():
            print "Added to wishlist"
        else:
            print "Adding to wishlist failed"
            self.fail()

    def test_zsign_out(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        out = driver.find_element_by_class_name("logout")
        out.click()
        self.assertIn("login", driver.page_source)

    def test_view_list(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        lst = driver.find_element_by_class_name("icon-th-list")
        lst.click()
        if lst.is_displayed():
            print "Product listed"
        else:
            self.fail("List doesn't work")

    def test_delivery_info(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        delivery = driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?id_cms=1&controller=cms"]')
        delivery.click()
        self.assertIn("Delivery", driver.title)

    def test_Tshirt(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        search = driver.find_element_by_id("search_query_top")
        search.send_keys("T-shirts")
        search.submit()
        prodname = driver.find_element_by_xpath('//img[@title="Faded Short Sleeve T-shirts"]')
        if prodname.is_displayed():
            self.defaultTestResult()
        else:
            self.fail("Search doesn't work correct")

    def test_d_product_to_cart(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        prod = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/6/16-home_default.jpg"]')
        prod.click()
        adding = driver.find_element_by_id("add_to_cart")
        adding.click()
        time.sleep(3)
        laycart = driver.find_element_by_xpath('//a[@title="Proceed to checkout"]')
        if laycart.is_displayed():
            self.defaultTestResult()
        else:
            self.fail("Error in adding product to cart")

    def test_search_dress(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(3)
        search = driver.find_element_by_id("search_query_top")
        search.send_keys("Dress")
        search.submit()
        prodname = driver.find_element_by_xpath('//img[@title="Faded Short Sleeve T-shirts"]')
        if prodname.is_displayed():
            self.fail("Wrong search results")
        else:
            self.defaultTestResult()

    def test_discount_price(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(3)
        special = driver.find_element_by_xpath('//a[@title="Specials"]')
        special.click()
        prod1 = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/2/0/20-home_default.jpg"]')
        prod2 = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/2/12-home_default.jpg"]')
        if prod1.is_displayed():
            self.defaultTestResult()
        elif prod2.is_displayed():
            self.defaultTestResult()
        else:
            self.fail("Wrong products with discount")

    def test_new_products(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(3)
        nprod = driver.find_element_by_xpath('//a[@title="New products"]')
        nprod.click()
        conf = driver.find_element_by_link_text("New products")
        if conf.is_displayed():
            self.defaultTestResult()
        else:
            self.fail("Wrong site displayed")

    def test_map_with_stores(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(3)
        stores = driver.find_element_by_link_text("Our stores")
        stores.click()
        location = driver.find_element_by_id("addressInput")
        location.send_keys("Miami")
        radius = driver.find_element_by_id("radiusSelect")
        for option in radius.find_elements_by_tag_name('option'):
            if option.text == '100':
                option.click()
                break
        searchb = driver.find_element_by_xpath('//button[@name="search_locations"]')
        searchb.click()
        storetable = driver.find_element_by_id("stores-table")
        if storetable.is_displayed():
            self.defaultTestResult()
        elif location.send_keys("Hollywood") and storetable.is_displayed():
            self.defaultTestResult()
        else:
            self.fail("Error displaying stores")

    def test_zz_create_new_account(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        signin = driver.find_element_by_class_name("login")
        signin.click()
        emcreate = driver.find_element_by_id("email_create")
        emcreate.send_keys("heyehey@gmail.com")
        sub = driver.find_element_by_id("SubmitCreate")
        sub.click()
        time.sleep(1)
        gender = driver.find_element_by_xpath('//label[@for="id_gender1"]')
        gender.click()
        time.sleep(1)
        fname = driver.find_element_by_id("customer_firstname")
        fname.send_keys("Michael")
        time.sleep(1)
        lname = driver.find_element_by_id("customer_lastname")
        lname.send_keys("Jackson")
        time.sleep(1)
        pswdr = driver.find_element_by_id("passwd")
        pswdr.send_keys("qwerty")
        time.sleep(2)
        days = driver.find_element_by_id("days")
        for option in days.find_elements_by_tag_name('option'):
            if option.text == '29':
                option.click()
                break
        time.sleep(1)
        months = driver.find_element_by_id("months")
        for option in months.find_elements_by_tag_name('option'):
            if option.text == 'August':
                time.sleep(2)
                option.click()
                break
        yearz = driver.find_element_by_id("years")
        time.sleep(1)
        for option in yearz.find_elements_by_tag_name('option'):
            if option.text == '1958':
                time.sleep(2)
                option.click()
                break
        time.sleep(1)
        addrname = driver.find_element_by_id("firstname")
        addrname.send_keys("Michael")
        time.sleep(1)
        addrlname = driver.find_element_by_id("lastname")
        addrlname.send_keys("Jackson")
        time.sleep(1)
        addr1 = driver.find_element_by_id("address1")
        addr1.send_keys("Second Street")
        time.sleep(1)
        addr2 = driver.find_element_by_id("address2")
        addr2.send_keys("22")
        time.sleep(1)
        city = driver.find_element_by_id("city")
        city.send_keys("New York")
        time.sleep(1)
        state = driver.find_element_by_id("id_state")
        for option in state.find_elements_by_tag_name('option'):
            if option.text == 'New York':
                time.sleep(2)
                option.click()
                break
        time.sleep(1)
        postcode = driver.find_element_by_id("postcode")
        postcode.send_keys("22222")
        time.sleep(1)
        mobile = driver.find_element_by_id("phone_mobile")
        mobile.send_keys("22272728")
        time.sleep(1)
        alias = driver.find_element_by_id("alias")
        alias.send_keys("HAHA")
        time.sleep(4)
        reg = driver.find_element_by_id("submitAccount")
        reg.click()

    def test_zy_retrive_password(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        signin = driver.find_element_by_class_name("login")
        signin.click()
        email = driver.find_element_by_id("email")
        email.send_keys("szymon.burko@vp.pl")
        email.submit()
        forgot = driver.find_element_by_xpath('//a[@title="Recover your forgotten password"]')
        forgot.click()
        email = driver.find_element_by_id("email")
        email.send_keys("szymon.burko@vp.pl")
        email.submit()
        time.sleep(1)
        # submitret = driver.find_element_by_tag_name("BUTTON")
        # driver.current_url
        # con = driver.find_element_by_link_text("A confirmation email has been sent to your address: szymon.burko@vp.pl")
    def test_newsletter(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        nletter = driver.find_element_by_id("newsletter-input")
        nletter.send_keys("abcdefgh@gmail.pl")
        nletter.submit()
        # msg =driver.find_element_by_class_name("alert alert-success")
    def test_terms_of_use(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        elem = driver.find_element_by_link_text("Terms and conditions of use")
        elem.click()
        head = driver.find_element_by_link_text("Terms and conditions of use")
        if head.is_displayed():
            self.defaultTestResult()
        else:
            self.fail("Cannot display terms and conditions of use")

    def test_deleting_from_cart(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(5)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        prod = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/6/16-home_default.jpg"]')
        prod.click()
        adding = driver.find_element_by_id("add_to_cart")
        adding.click()
        time.sleep(1)
        proceedb = driver.find_element_by_xpath('//a[@title="Proceed to checkout"]')
        # if proceedb.is_displayed():
        proceedb.click()
        trash = driver.find_element_by_class_name("cart_quantity_delete")
        trash.click()
        # driver.save_screenshot('screens.png')

    def test_change_addr(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        prod = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/6/16-home_default.jpg"]')
        prod.click()
        adding = driver.find_element_by_xpath('//button[@class="exclusive"]')
        adding.click()
        laycart = driver.find_element_by_xpath('//*[@href="http://automationpractice.com/index.php?controller=order"]')
        if laycart.is_displayed():
            laycart.click()
        time.sleep(1)
        but = driver.find_element_by_xpath('//*[@href="http://automationpractice.com/index.php?controller=order&step=1"]')
        but.click()
        sel = driver.find_element_by_id("id_address_delivery")
        for option in sel.find_elements_by_tag_name('option'):
            if option.text == 'My address':
                option.click()
                self.defaultTestResult()
                break

    def test_order_confcheck(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        prod = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/6/16-home_default.jpg"]')
        prod.click()
        adding = driver.find_element_by_xpath('//button[@class="exclusive"]')
        adding.click()
        laycart = driver.find_element_by_xpath('//*[@href="http://automationpractice.com/index.php?controller=order"]')
        if laycart.is_displayed():
            laycart.click()
        time.sleep(1)
        but = driver.find_element_by_xpath('//*[@href="http://automationpractice.com/index.php?controller=order&step=1"]')
        but.click()
        time.sleep(1)
        prcd = driver.find_element_by_xpath('//button[@name="processAddress"]')
        prcd.click()
        time.sleep(1)
        inpt = driver.find_element_by_xpath('//div[@id="uniform-cgv"]')
        inpt.click()
        check = driver.find_element_by_xpath('//button[@name="processCarrier"]')
        check.click()
        time.sleep(1)
        payment = driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?fc=module&module=cheque&controller=payment"]')
        payment.click()
        time.sleep(1)
        confirmation = driver.find_element_by_tag_name("BUTTON")
        confirmation.click()

    def test_order_confbank(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        prod = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/6/16-home_default.jpg"]')
        prod.click()
        adding = driver.find_element_by_xpath('//button[@class="exclusive"]')
        adding.click()
        laycart = driver.find_element_by_xpath('//*[@href="http://automationpractice.com/index.php?controller=order"]')
        if laycart.is_displayed():
            laycart.click()
        time.sleep(1)
        but = driver.find_element_by_xpath(
            '//*[@href="http://automationpractice.com/index.php?controller=order&step=1"]')
        but.click()
        time.sleep(1)
        prcd = driver.find_element_by_xpath('//button[@name="processAddress"]')
        prcd.click()
        time.sleep(1)
        inpt = driver.find_element_by_xpath('//div[@id="uniform-cgv"]')
        inpt.click()
        check = driver.find_element_by_xpath('//button[@name="processCarrier"]')
        check.click()
        time.sleep(1)
        payment = driver.find_element_by_xpath('//a[@href="http://automationpractice.com/index.php?fc=module&module=bankwire&controller=payment"]')
        payment.click()
        time.sleep(1)
        confirmation = driver.find_element_by_tag_name("BUTTON")
        confirmation.click()

    def test_sort_by_price_lowest(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        sortp = driver.find_element_by_id("selectProductSort")
        for option in sortp.find_elements_by_tag_name('option'):
            if option.text == 'Price: Lowest first':
                time.sleep(2)
                option.click()
                break
        time.sleep(2)
        tab = driver.find_element_by_xpath('//ul[@class="product_list grid row"]')
        time.sleep(1)
        elem = tab.find_elements_by_xpath('//span[@class="price product-price"]')
        prod = []
        for item in elem:
            prod = item.text
            print prod
        self.assertEqual(elem[1].text, "$16.40" )
        time.sleep(2)

    def test_sort_by_price_highest(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        sortp = driver.find_element_by_id("selectProductSort")
        for option in sortp.find_elements_by_tag_name('option'):
            if option.text == 'Price: Highest first':
                time.sleep(2)
                option.click()
                break
        time.sleep(2)
        tab = driver.find_element_by_xpath('//ul[@class="product_list grid row"]')
        time.sleep(1)
        elem = tab.find_elements_by_xpath('//span[@class="price product-price"]')
        prod = []
        for item in elem:
            prod = item.text
            print prod
        self.assertEqual(elem[1].text, "$50.99" )
        time.sleep(2)

    def test_sort_by_name_atoz(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        sortp = driver.find_element_by_id("selectProductSort")
        for option in sortp.find_elements_by_tag_name('option'):
            if option.text == 'Product Name: A to Z':
                time.sleep(2)
                option.click()
                break
        time.sleep(2)
        tab = driver.find_element_by_xpath('//ul[@class="product_list grid row"]')
        time.sleep(1)
        elem = tab.find_elements_by_xpath('//h5[@itemprop="name"]')
        prod = []
        for item in elem:
            prod = item.text
            print prod
        self.assertEqual(elem[0].text, "Blouse" )
        time.sleep(2)

    def test_sort_by_name_ztoa(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        sortp = driver.find_element_by_id("selectProductSort")
        for option in sortp.find_elements_by_tag_name('option'):
            if option.text == 'Product Name: A to Z':
                time.sleep(2)
                option.click()
                break
        time.sleep(2)
        tab = driver.find_element_by_xpath('//ul[@class="product_list grid row"]')
        time.sleep(1)
        elem = tab.find_elements_by_xpath('//h5[@itemprop="name"]')
        prod = []
        for item in elem:
            prod = item.text
            print prod
        self.assertEqual(elem[0].text, "Printed Summer Dress")
        time.sleep(2)

    def test_sort_dresses_by_price_lowest(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        time.sleep(1)
        dr = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/c/8-medium_default.jpg"]')
        dr.click()
        time.sleep(1)
        sortp = driver.find_element_by_id("selectProductSort")
        for option in sortp.find_elements_by_tag_name('option'):
            if option.text == 'Price: Lowest first':
                time.sleep(2)
                option.click()
                break
        time.sleep(2)
        tab = driver.find_element_by_xpath('//ul[@class="product_list grid row"]')
        time.sleep(1)
        elem = tab.find_elements_by_xpath('//span[@class="price product-price"]')
        prod = []
        for item in elem:
            prod = item.text
            print prod
        self.assertEqual(elem[1].text, "$16.40")
        time.sleep(2)

    def test_sort_dresses_by_price_highest(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        time.sleep(1)
        dr = driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/c/8-medium_default.jpg"]')
        dr.click()
        time.sleep(1)
        sortp = driver.find_element_by_id("selectProductSort")
        for option in sortp.find_elements_by_tag_name('option'):
            if option.text == 'Price: Highest first':
                time.sleep(2)
                option.click()
                break
        time.sleep(2)
        tab = driver.find_element_by_xpath('//ul[@class="product_list grid row"]')
        time.sleep(1)
        elem = tab.find_elements_by_xpath('//span[@class="price product-price"]')
        prod = []
        for item in elem:
            prod = item.text
            print prod
        self.assertEqual(elem[1].text, "$50.99")
        time.sleep(2)

    def test_price_range(self):
        driver = self.driver
        driver.get("http://automationpractice.com")
        time.sleep(2)
        wom = driver.find_element_by_class_name("sf-with-ul")
        wom.click()
        time.sleep(1)
        slider = driver.find_element_by_xpath('//a[@class="ui-slider-handle ui-state-default ui-corner-all"]')
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 750)")
        time.sleep(1)
        move = ActionChains(driver)
        move.click_and_hold(slider).move_by_offset(120, 0).release().perform()
        time.sleep(5)
        prod= driver.find_element_by_xpath('//img[@src="http://automationpractice.com/img/p/1/0/10-home_default.jpg"]')
        if prod.is_displayed():
            self.shortDescription()
        else:
            self.fail("Product is not suitable to price range ")


    def tearDown(self):
         pass
        # self.driver.close()

if __name__ == "__main__":
    unittest.main()
