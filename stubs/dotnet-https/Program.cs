using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
	static void Main(string[] args)
	{
		if (args.Length == 3) {
			Console.WriteLine("UNSUPPORTED");
			System.Environment.Exit(0);
		} else if (args.Length != 2) {
			Console.WriteLine("Usage: dotnettest <HOST> <PORT>");
			System.Environment.Exit(1);
		}
		try {
			string url = "https://"+args[0]+":"+args[1];
			GetURL(url).Wait();
			Console.WriteLine("ACCEPT");
		} catch (AggregateException ae) {
			ae.Handle((x) =>
			{
			if (x is HttpRequestException)
			{
				Console.WriteLine("REJECT");
				return true;
			}
			else {
				return false;
			}
			});
		} catch (Exception e) {
			Console.WriteLine("Unhandled exception: {0} {1}",e.Message,e);
			System.Environment.Exit(1);
		}
	}

	static async Task GetURL(string url)
	{
		using (HttpClient client = new HttpClient())
		using (HttpResponseMessage response = await client.GetAsync(url))
		using (HttpContent content = response.Content)
		{
		// ... Read the string.
			string result = await content.ReadAsStringAsync();

		}
	}
}
