import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class TestSurvApp {
    public static void main(String[] args) throws InterruptedException {

        // System Property for Chrome Driver
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\VenkyG\\ChromeDriver\\chromedriver.exe");

//        ChromeOptions options = new ChromeOptions();
//        options.addArguments("enable-precise-memory-info");

        // Instantiate a ChromeDriver class.
        WebDriver driver = new ChromeDriver();

        // Launch Website
        //driver.navigate().to("http://www.javatpoint.com/");
        driver.get("http://www.javatpoint.com/");

        //Maximize the browser
        driver.manage().window().maximize();

        WebElement splunk = driver.findElement(By.className("homecontent"));
        splunk.click();
        System.out.println("Waiting");
        Thread.sleep(5000);

        driver.quit();
        System.out.println("Hello World!");
//        Thread.sleep(5000);
    }
}
