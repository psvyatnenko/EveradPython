from selenium.webdriver.common.by import By


class MainPageLocators(object):
    mainPageTitle = "Рекламная сеть EverAD - лучшая партнерская (CPA) сеть по продаже товаров"
    logo = By.XPATH("html/body/div[3]/header/div[1]/a/img")
    wmLink = By.XPATH("html/body/div[3]/header/div[2]/ul/li[1]/a")
    wmLinkText = "Вебмастеру"
    advLink = By.XPATH("html/body/div[3]/header/div[2]/ul/li[2]/a")
    advLinkText = "Рекламодателю"
    aboutSystemLink = By.XPATH("html/body/div[3]/header/div[2]/ul/li[3]/a")
    aboutSystemLinkText = "О системе"
    contactLink = By.XPATH("html/body/div[3]/header/div[2]/ul/li[4]/a")
    contactLinkText = "Контакты"
    enterAndRegButton = By.XPATH("html/body/div[3]/header/div[3]/a")
    enterAndRegButtonText = "Вход и регистрация"
    iAmWMButton = By.XPATH("html/body/div[3]/main/div[1]/div[1]/div[1]/a[1]")
    iAmWMButtonText = "Я веб-мастер"
    iAmWMBannerText1Locator = By.XPATH("html/body/div[3]/main/div[1]/div[1]/div[1]/p/text()[1]")
    iAmWMBannerText1 = "EverAD - это сеть партнёрских интернет-площадок и"
    iAmWMBannerText2Locator = By.XPATH("html/body/div[3]/main/div[1]/div[1]/div[1]/p/text()[2]")
    iAmWMBannerText2 = "рекламных предложений с оплатой за действие."
    iAmAdvButton = By.XPATH("html/body/div[3]/main/div[1]/div[1]/div[2]/a[1]")
    iAmAdvButtonText = "Я рекламодатель"
    iAmAdvBannerText1Locator = By.XPATH("html/body/div[3]/main/div[1]/div[1]/div[2]/p/text()[1]")
    iAmAdvBannerText1 = "Вы хотите увеличить свои продажи в интернете"
    iAmAdvBannerText2Locator = By.XPATH("html/body/div[3]/main/div[1]/div[1]/div[2]/p/text()[2]")
    iAmAdvBannerText2 = "прямо сейчас? Напишите нам!"
    regButton = By.XPATH("html/body/div[3]/main/div[1]/a")
    regButtonFooter = By.XPATH(".//*[@id='section5']/a")
    regButtonText = "Зарегистрироваться"
    forWMLabel = By.XPATH("html/body/footer/div/div[1]/p")
    forWMLabelText = "Для веб-мастеров"
    rulesLink = By.XPATH("html/body/footer/div/div[1]/ul/li[1]/a")
    rulesLinkText = "Правила"
    faqLink = By.XPATH("html/body/footer/div/div[1]/ul/li[2]/a")
    faqLinkText = "FAQ"
    forAdvLabel = By.XPATH("html/body/footer/div/div[2]/p")
    forAdvLabelText = "Рекламодателям"
    addProjectLink = By.XPATH("html/body/footer/div/div[2]/ul/li/a")
    addProjectText = "Разместить проект"
    aboutCompanyLabel = By.XPATH("html/body/footer/div/div[3]/p")
    aboutCompanyLabelText = "Компания"
    aboutUsLink = By.XPATH("html/body/footer/div/div[3]/ul/li[1]/a")
    aboutUsText = "О нас"
    contactsFooterLink = By.XPATH("html/body/footer/div/div[3]/ul/li[2]/a")
    contactsFooterText = "Контакты"
    privacyLink = By.XPATH("html/body/footer/div/div[3]/ul/li[3]/a")
    privacyText = "Политика конфиденциальности"
    postAddressLabel = By.XPATH("html/body/footer/div/div[4]/p")
    postAddressLabelText = "Почтовый адрес"
    postAddressLabel1 = By.XPATH("html/body/footer/div/div[4]/div/p[1]")
    postAddressLabelText1 = "Cariovision Trade Ltd. Geneva Place"
    postAddressLabel2 = By.XPATH("html/body/footer/div/div[4]/div/p[2]")
    postAddressLabelText2 = "Waterfront Drive, P.O. Box 3469, Road"
    postAddressLabel3 = By.XPATH("html/body/footer/div/div[4]/div/p[3]")
    postAddressLabelText3 = "Town, Tortola. BVI"
    enterAndRegPopup = By.XPATH(".//*[@id='form_popup']")
    popupHeader = By.XPATH(".//*[@id='form_popup']/div[1]")
    popupHeaderText = "Войти в аккаунт"
    popupClose = By.XPATH(".//*[@id='form_popup']/div[1]/a")
    popupEmailField = By.XPATH(".//*[@id='login-container']/div/form/div[1]/div[1]/input")
    popupPasswordField = By.XPATH(".//*[@id='login-container']/div/form/div[1]/div[2]/input")
    popupEmailFieldText = "Войти в аккаунт"
    popupRememberMeCheckBox = By.XPATH(".//*[@id='login-container']/div/form/div[2]/label")
    popupRememberMeLabelText = "Запомнить меня"
    popupForgotPasswordLink = By.XPATH(".//*[@id='login-container']/div/form/div[2]/a")
    popupForgotPasswordLinkText = "Забыли пароль?"
    popupEnterButton = By.XPATH(".//*[@id='login-container']/div/form/div[2]/div/input[1]")
    popupEnterButtonText = "Войти"
    popupEnterVKLogo = By.XPATH(".//*[@id='login-container']/div/form/div[2]/div/a[1]/i")
    popupEnterFBLogo = By.XPATH(".//*[@id='login-container']/div/form/div[2]/div/a[2]/i")
    popupCancelButton = By.XPATH(".//*[@id='login-container']/div/form/div[2]/div/input[2]")
    popupCancelButtonText = "Отмена"
    popupWrongEmailOrPasswordLabel = By.XPATH(".//*[@id='login-container']/div/form/div[1]/p")
    popupWrongEmailOrPasswordLabelText = "Неверный email или пароль"
    popupDontHaveAccountLabel = By.XPATH(".//*[@id='form_popup']/div[4]/p")
    popupDontHaveAccountLabelText = "Нет аккаунта?"
    popupRegButton = By.XPATH(".//*[@id='form_popup']/div[4]/a")
    popupRegButtonText = "Зарегистрироваться"
    popupForgotPasswordLabel = By.XPATH(".//*[@id='recover-password-container']/div/form/p")
    popupForgotPasswordLabelText = "На заданный E-mail адрес, будет выслана ссылка." \
                                   " По которой вы сможете создать новый пароль по вашей учетной записи"
    popupForgotPasswordEmailField = By.XPATH(".//*[@id='recover-password-container']/div/form/div/input")
    popupForgotPasswordRestoreButton = By.XPATH(".//*[@id='recover-password-container']/div/form/button")
    popupForgotPasswordRestoreButtonText = "Восстановить"


class RegPageLocators(object):
    regPageIamWMButton = By.XPATH("html/body/div[3]/main/div/ul/li[1]/a")
    regPageIamWMButtonText = "Вебмастер"
    regPageIamAdvButton = By.XPATH("html/body/div[3]/main/div/ul/li[2]/a")
    regPageIamAdvButtonText = "Рекламодатель"
    errorFieldText = "Обязательноe поле"
    errorEmailText = "Неверный формат email адреса"
    emailLabelText = "Электронная почта:"
    skypeLabelText = "Skype:"
    skypeField = By.XPATH(".//*[@id='skype']")


class RegWMPageLocators(object):
    regWMLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/h4")
    regWMLabelText = "Регистрация вебмастера"
    nameOrNicknameLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[1]/label")
    nameOrNicknameLabelText = "Имя или никнейм:"
    regWMPageLoginField = By.XPATH(".//*[@id='name']")
    errorNameLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[1]/em")
    regWmEmailLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[2]/label")
    regWmEmailField = By.XPATH(".//*[@id='email']")
    regWmErrorEmailLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[2]/em")
    passwordLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[3]/label")
    passwordLabelText = "Пароль:"
    passwordField = By.XPATH(".//*[@id='password']")
    errorPasswordLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[3]/em")
    repeatPasswordLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[4]/label")
    repeatPasswordLabelText = "Пароль еще раз:"
    repeatPasswordField = By.XPATH(".//*[@id='repeat_password']")
    errorRepeatPasswordField = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[4]/em")
    regWMSkypeLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[5]/label")
    wmrLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[6]/label")
    wmrLabelText = "WMR:"
    wmrField = By.XPATH(".//*[@id='wmr']")
    errorWmrLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[6]/em")
    errorWmrLabelText = "Неверный формат WMR кошелька"
    iAgreeWithRules = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[7]/span")
    iAgreeWithRulesLink = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[7]/a")
    iAgreeWithRulesLinkText = "Согласен с правилами сети EverAD"
    wmRegButton = By.XPATH("html/body/div[3]/main/div/div[1]/div[1]/div[2]/form/div[8]/input")
    wmRegButtonText = "Зарегистрироваться"


class RegAdvPageLocators(object):
    regAdvLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/h4")
    regAdvLabelText = "Регистрация рекламодателя"
    fioLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[1]/label")
    fioLabelText = "Фамилия, Имя, Отчество:"
    fioField = By.XPATH(".//*[@id='name2']")
    errorFioField = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[1]/em")
    regAdvEmailLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[2]/label")
    regAdvEmailField = By.XPATH(".//*[@id='email2']")
    regAdvErrorEmailLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[2]/em")
    regAdvPhoneLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[3]/label")
    regAdvPhoneLabelText = "Телефон для связи:"
    regAdvPhoneField = By.XPATH(".//*[@id='phone']")
    regAdvErrorPhoneLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[3]/em")
    regAdvErrorPhoneLabelText = "Неверный формат телефона"
    regAdvSkypeLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[4]/label")
    regAdvErrorSkypeLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[4]/em")
    regAdvErrorSkypeLabelText = "Неверный формат Skype логина"
    companyNameLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[5]/label")
    companyNameLabelText = "Название компании:"
    companyNameField = By.XPATH(".//*[@id='company']")
    errorCompanyNameLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[5]/em")
    productLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[6]/label")
    productLabelText = "Рекламируемый продукт (услуга):"
    productField = By.XPATH(".//*[@id='product']")
    errorProductLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[6]/em")
    webSiteAddressLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[7]/label")
    webSiteAddressField = By.XPATH(".//*[@id='website']")
    errorWebSiteAddressLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[7]/em")
    targetActionLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[8]/label")
    targetActionDropDown = By.XPATH(".//*[@id='target-button']/span[2]")
    targetActionDropDownPaidOrder = By.XPATH(".//*[@id='ui-id-1']")
    targetActionDropDownFillingForm = By.XPATH(".//*[@id='ui-id-2']")
    targetActionDropDownViewingVideo = By.XPATH(".//*[@id='ui-id-3']")
    remunerationLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[9]/label")
    remunerationLabelText = "Желаемый размер вознаграждения (р):"
    remunerationField = By.XPATH(".//*[@id='payout']l")
    audienceLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[10]/label")
    audienceLabelText = "Предпочитаемая аудитория"
    desiredAmountLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[11]/label")
    desiredAmountLabelText = "Желаемый объём действий в месяц"
    platformsLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[12]/label")
    platformsLabelText = "В каких СРА-сетях уже идёт размещения?"
    geographyLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[13]/label")
    geographyLabelText = "Требуемая география?"
    whereIsAdvertisedLabel1 = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/label/text()[1]")
    whereIsAdvertisedLabel1Text = "Где сейчас проходит размещение рекламы"
    whereIsAdvertisedLabel2 = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/label/text()[2]")
    whereIsAdvertisedLabel2Text = "для проекта (если проводится):"
    whereIsAdvertisedContextCheckBox = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[1]/span")
    whereIsAdvertisedContextLabel = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[1]/label")
    whereIsAdvertisedMediaCheckBox = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[2]/span")
    whereIsAdvertisedMediaLabel = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[2]/label")
    whereIsAdvertisedMediaLabelText = "Медийная реклама (баннеры на площадках)"
    whereIsAdvertisedTeasersCheckBox = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[3]/span")
    whereIsAdvertisedTeasersLabel = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[3]/label")
    whereIsAdvertisedVKCheckBox = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[4]/span")
    whereIsAdvertisedVKLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[4]/label")
    whereIsAdvertisedMailRuCheckBox = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[5]/span")
    whereIsAdvertisedMailRuLabel = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[5]/label")
    whereIsAdvertisedEmailCheckBox = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[6]/span")
    whereIsAdvertisedEmailLabel = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[6]/label")
    whereIsAdvertisedAnotherCheckBox = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[7]/span")
    whereIsAdvertisedAnotherLabel = By.XPATH(
        "html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[14]/div/div[7]/label")
    postClickLabel = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[15]/label")
    postClickLabelText = "Post-click (количество дней)"
    postClickField = By.XPATH(".//*[@id='postclick']")
    whatSourceByQualityLabel1 = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[16]/label/text()[1]")
    whatSourceText = "Какие источники дали наибольшую отдачу"
    whatSourceByQualityLabel2 = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[16]/label/text()[2]")
    whatSourceByQualityLabel2Text = "по качеству (если есть)?"
    whatSourceByQualityField = By.XPATH(".//*[@id='quality_sources']")
    whatSourceByTrafficLabel1 = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[17]/label/text()[1]")
    whatSourceByTrafficLabel2 = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[17]/label/text()[2]")
    whatSourceByTrafficLabel2Text = "по объему трафика (если есть)?"
    whatSourceByTrafficField = By.XPATH(".//*[@id='traffic_sources']")
    sendButton = By.XPATH("html/body/div[3]/main/div/div[1]/div[2]/div[2]/form/div[18]/input")
    sendButtonText = "Отправить"


class RegAdvSuccessPageLocators(object):
    regAdvSuccessLabel1 = By.XPATH("html/body/div[3]/main/div/text()[2]")
    regAdvLabelText1 = "Анкета успешно отправлена!"
    regAdvSuccessLabel2 = By.XPATH("html/body/div[3]/main/div/text()[3]")
    regAdvLabelText2 = "Ваше предложение рассмотрит наш менеджер. Мы свяжемся с вами тем контактам, которые вы указали."
    regAdvSuccessLabel3 = By.XPATH("html/body/div[3]/main/div/text()[4]")
    regAdvLabelText3 = "Если у вас остались вопросы, напишите нам в Skype:"
    regAdvSuccessSkypeLink = By.XPATH("html/body/div[3]/main/div/a")
    regAdvSkypeLinkText3 = "everad_adv"
