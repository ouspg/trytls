using System;
using System.Net;
using System.Security.Cryptography.X509Certificates;

//tested with Mono and cannot recommend using

public class Run
{
  static public void Main (String []args)
  {
    if (args.Length > 3 || args.Length < 2){
      Console.WriteLine("UNSUPPORTED");
      Environment.Exit(0);
    }

    String host, port, crt;

    host = args[0];
    port = args[1];

    try {
      string url = "https://" + host + ":" + port;
      //Console.WriteLine (url);
      //request
      HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
      //certificate if required
      if (args.Length > 2) {
        crt = args[2];
        //DER decoded certificates only. fails with PEM decoded certificates
        request.ClientCertificates.Add(X509Certificate.CreateFromCertFile(crt));
      }
      //get response(connection + file)
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
