use strict;
use warnings;

use LWP::UserAgent;

if (scalar @ARGV < 2 or scalar @ARGV > 3) {
    print STDERR "Usage: $0 <host> <port> [cafile]\n";
    exit 1;
}
my ($host, $port, $cafile) = @ARGV;
my $ua = LWP::UserAgent->new;
if (defined $cafile) {
    eval {
        $ua->ssl_opts(SSL_ca_file => $cafile);
    };
    if ($@) {
        print "UNSUPPORTED\n";
        exit 0;
    }
}
my $response = $ua->get("https://$host:$port");
my $client_warning = $response->header('Client-Warning') || '';
if ($client_warning eq 'Internal response') {
    if ($response->code == 500 and $response->content =~ m/hostname verification failed|SSL connect/) {
        print "REJECT\n";
    } else {
        print STDERR $response->as_string;
        exit 1;
    }
} else {
    print "ACCEPT\n"
}
