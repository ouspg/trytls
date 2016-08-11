import java.net.URL;
import java.io.*;

public class Run {
  public static void main(String [] args) {

    if (args.length == 3) {
      System.out.println("UNSUPPORTED");
      System.exit(0);
    } else if (args.length != 2) {
      System.out.println("usage: java Run <host> <port>");
      System.exit(1);
    }

    String host = args[0];
    String port = args[1];

    String https_url = String.format("https://%s:%s", host, port);

    try {
      new java.net.URL(https_url).getResponseCode();
      System.out.println("ACCEPT");
    } catch (javax.net.ssl.SSLException e){
      System.out.println("REJECT");
    } catch (Exception e) {
      System.out.println(e);
      System.exit(3);
    }
    System.exit(0);
  }
}
