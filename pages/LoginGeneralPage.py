from base.baseFile import BasePage
import utilities.CustomLogger as cl


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # overiding the self Init method of base class
        self.driver = driver

    # Locators for the Login form
    _letsShopButton = "com.androidsample.generalstore:id/btnLetsShop"  # id
    _enterName = "com.androidsample.generalstore:id/nameField"  # id
    _selectGenderFemale = "com.androidsample.generalstore:id/radioFemale" # id
    _selectGenderMale = "com.androidsample.generalstore:id/radioMale" # id
    _countryDropdown = "com.androidsample.generalstore:id/spinnerCountry" #id
    _selectCountryAntartica = "Antarctica" #text
    _addToCartButton = "//android.widget.TextView[@text='ADD TO CART'][1]" #xpath

    def letsShop(self):
        self.clickElement(self._letsShopButton, "id")
        cl.allureLogs("Click on Login button")

    def enterName(self):
        self.sendText("Checked", self._enterName, "id")
        cl.allureLogs("Enter the Name")

    def selectGenderFemale(self):
        self.clickElement(self._selectGenderFemale, "id")
        cl.allureLogs("Gender is selected as Female")

    def selectGenderMale(self):
        self.clickElement(self._selectGenderMale, "id")
        cl.allureLogs("Gender is selected as Male")

    def selectCountry(self):
        self.clickElement(self._countryDropdown, "id")
        cl.allureLogs("Country is selected as Antartica")

    def addtoCart(self):
        self.clickElement(self._addToCartButton, "xpath")
        cl.allureLogs("Product is added to the Cart")
