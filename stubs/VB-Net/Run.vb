Imports System
Imports System.Net
Imports System.IO

Module Run
  Sub Main()  ' or args as String
    Dim arguments As String() = Environment.GetCommandLineArgs()
    Dim host, port as String

    if arguments.Length = 3 Then
      host = arguments(1)
      port = arguments(2)
    Elseif arguments.Length = 4 Then
      Console.WriteLine ("UNSUPPORTED") ' for now
      Environment.Exit(0)
    Else
      Console.WriteLine ("Usage: .. Run.exe <host> <port>")
      Environment.Exit(1)
    End if

    Dim url As String
    url = "https://" & host & ":" & port

    Dim request As WebRequest
    request = WebRequest.Create(url)

    Try
      request.GetResponse()
      Console.WriteLine ("ACCEPT")
    Catch ex As System.Net.WebException
      if ex.ToString.Contains("NameResolutionFailure") Then
        Throw ex
        Environment.Exit(1)
      Else
        Console.WriteLine ("REJECT")
      End if
    Catch ex As Exception
      Throw ex
      Environment.Exit(1)
    End Try
    Environment.Exit(0)
  End Sub
End Module
