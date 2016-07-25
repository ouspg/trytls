import java.net.URL;
import java.io.*;
import javax.net.ssl.HttpsURLConnection;

public class Run{

	public static void main(String[] args)
	{

		if (args.length != 2) {
			System.out.println("UNSUPPORTED");
			System.exit(0);
		}

		String host = args[0];
		String port = args[1];

		URL url;
		String https_url = String.format("https://%s:%s", host, port);
		try {
			url = new URL(https_url);
			HttpsURLConnection con = (HttpsURLConnection)url.openConnection();
			con.getResponseCode();
			System.out.println("VERIFY SUCCESS");
		} catch (javax.net.ssl.SSLHandshakeException|javax.net.ssl.SSLKeyException|javax.net.ssl.SSLProtocolException e) {
			System.out.println("VERIFY FAILURE");
		} catch (Exception e) {
			System.out.println(e);
			System.exit(3);
		}

		System.exit(0);
	}

}
