open System.Net
open System

[<EntryPoint>]
let main(args) =      //host, port, no support for ca-bundle at the moment
  match args with
  | [|host; port|] ->
    let url = String.Format("https://{0}:{1}", host, port)
    try
      let req = HttpWebRequest.Create(url)
      let resp = req.GetResponse()
      printfn "VERIFY SUCCESS"
      exit 0
    with
      | :? System.Net.WebException as ex ->
        let error = ex.Message
        if error.Contains("NameResolutionFailure") then
          printfn "%s" error;
          exit 1
        else
          printfn "%s" "VERIFY FAILURE";
          exit 0
      | _ as ex->
        printfn "%A" ex.Message;
        exit 1
  | _ ->
    printfn "UNSUPPORTED"
    exit 0
