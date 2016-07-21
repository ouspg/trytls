using System;
using System.Net;

public class Run
{
  static public void Main (String []args)
  {
    if (args.Length != 2){
      Console.WriteLine("UNSUPPORTED");
      Environment.Exit(0);
    }

    String host, port;

    host = args[0];
    port = args[1];

    try {
      string url = "https://" + host + ":" + port;
      HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
      HttpWebResponse response = (HttpWebResponse)request.GetResponse();
      Console.WriteLine ("VERIFY SUCCESS");
    } catch (System.Net.WebException e) {
      if (! e.ToString().Contains("NameResolutionFailure")){
        Console.WriteLine("VERIFY FAILURE");
      } else {
        Console.WriteLine (e);
        Environment.Exit(1);
      }
    } catch (System.Exception e) {
      Console.WriteLine (e);
      Environment.Exit(1);
    }
    Environment.Exit(0);
  }
}
