import java.net.URL;
import java.io.*;
import javax.net.ssl.HttpsURLConnection;

public class Main{
	
	public static void main(String[] args)
	{
		try (BufferedReader br = new BufferedReader(new FileReader("tmp/messages"))) {
			String line;
			String splitted[]; // = port & message & crt & hostname
			URL url;
			int port = 0, message = 1, hostname = 3;
			while ((line = br.readLine()) != null) {
				splitted = line.split(" & ", 4);
				String https_url = String.format("https://%s:%s", splitted[hostname], splitted[port]);
				try {
					url = new URL(https_url);
					HttpsURLConnection con = (HttpsURLConnection)url.openConnection();
					if (con.getResponseCode() == 200){
						System.out.println("    True: " + splitted[message]);
					} else {
						System.out.println("not True: " + splitted[message]);
					}
				} catch (Exception e) {
					System.out.println("not True: " + splitted[message]);
				}
			}
		} catch (Exception e) {
			return ;
		}
	}
	
}

