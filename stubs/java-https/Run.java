import java.net.URL;
import java.io.*;
import javax.net.ssl.HttpsURLConnection;

public class Run{

	public static void main(String[] args)
	{

		if (args.length == 3) {
			System.out.println("UNSUPPORTED");
			System.exit(0);
		} else if (args.length != 2) {
			System.out.println("usage: java Run <host> <port>");
			System.exit(1);
		}

		String host = args[0];
		String port = args[1];

		URL url;
		String https_url = String.format("https://%s:%s", host, port);
		try {
			url = new URL(https_url);
			HttpsURLConnection con = (HttpsURLConnection)url.openConnection();
			con.getContent();
			System.out.println("ACCEPT");
		} catch (javax.net.ssl.SSLException e) {
			System.out.println(e);
			System.out.println("REJECT");
		} catch (Exception e) {
			System.out.println(e);
			System.exit(3);
		}

		System.exit(0);
	}
}
