using System;
using System.Net;

public class Run
{
  static public void Main (String []args)
  {
    if (args.Length == 3){
      Console.WriteLine("UNSUPPORTED");
      Environment.Exit(0);
    } else if (args.Length != 2) {
      Console.WriteLine("usage: run.exe <host> <port>");
      Environment.Exit(1);
    }

    String host, port;

    host = args[0];
    port = args[1];

    try {
      string url = "https://" + host + ":" + port;
      HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
      HttpWebResponse response = (HttpWebResponse)request.GetResponse();
      Console.WriteLine ("ACCEPT");
    } catch (System.Net.WebException e) {
      if (! e.ToString().Contains("NameResolutionFailure")){
        Console.WriteLine("REJECT");
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
