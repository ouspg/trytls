# Dependencies:

.NET Core 1.0

# How to build:
dotnet restore && dotnet build

# How to run:
dotnet exec ./bin/Debug/netcoreapp1.0/prj.dll <URL> <PORT

Or:

docker build -t trytls:dotnet-https .
docker run trytls:dotnet-https <URL> <PORT>