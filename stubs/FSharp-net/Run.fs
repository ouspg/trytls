open System.Net
open System

[<EntryPoint>]
let main(args) =      //host, port, no support for ca-bundle at the moment
  let returnval =
    match args with
    | [|host; port|] ->
      let url = String.Format("https://{0}:{1}", host, port)
      try
        let req = HttpWebRequest.Create(url).GetResponse()
        printfn "VERIFY SUCCESS"; 0
      with
        | :? System.Net.WebException as ex ->
          if ex.Message.Contains("NameResolutionFailure") then
            printfn "%s" ex.Message; 1
          else
            printfn "VERIFY FAILURE"; 0
        | _ as ex->
          printfn "%s" ex.Message; 1
    | [|_; _; _|] ->
      printfn "UNSUPPORTED"; 0
    | _ ->
      printfn "usage: .. Run.exe <host> <port>"; 1
  exit returnval
