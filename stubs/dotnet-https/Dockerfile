FROM microsoft/dotnet

RUN useradd -c "dotnet" -m dotnet
#USER dotnet

ENV HOME /home/dotnet
WORKDIR ${HOME}/prj
RUN ["dotnet","new"]
COPY . ${HOME}/prj
RUN dotnet restore && dotnet build

ENTRYPOINT ["/usr/share/dotnet/dotnet","exec","--additionalprobingpath","/home/dotnet/.nuget/packages","/home/dotnet/prj/bin/Debug/netcoreapp1.0/prj.dll"]

