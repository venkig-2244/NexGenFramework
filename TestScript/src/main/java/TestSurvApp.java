import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class TestSurvApp {
    public static void main(String[] args) throws InterruptedException {

        // System Property for Chrome Driver
        System.setProperty("webdriver.chrome.driver", "C:\\ChromeDriver\\chromedriver.exe");

        // Instantiate a ChromeDriver class.
        WebDriver driver = new ChromeDriver();

        // Launch Website
        driver.navigate().to("http://www.javatpoint.com/");

        //Maximize the browser
        driver.manage().window().maximize();

        WebElement splunk = driver.findElement(By.className("homecontent"));
        splunk.click();
        System.out.println("Waiting");
        Thread.sleep(5000);

        driver.quit();
    }
}
