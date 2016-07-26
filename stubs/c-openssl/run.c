#include <stdio.h>
#include <string.h>

#include <openssl/err.h>
#include <openssl/ssl.h>
#include <openssl/x509v3.h>

int main(int argc, char *argv[]) {

  int returncode = 0;

  if (argc == 3) {
    printf("UNSUPPORTED\n");  //for now at least
    return returncode;
  } else if (argc != 4) {
    printf("usage: %s <host> <port> <ca-bundle>\n", argv[0]);
    return (returncode + 1);
  }

  //init

  BIO *sbio;
	SSL_CTX *ssl_ctx;
	SSL *ssl;
	X509 *cert;

  char url[256]; sprintf(url, "%s:%s", argv[1], argv[2]);
  char ca_bundle[256]; strncpy(ca_bundle, argv[3], sizeof(ca_bundle));

  const char *servername = NULL;
  X509_VERIFY_PARAM *param = NULL;

  SSL_library_init();
  SSL_load_error_strings();

  ssl_ctx = SSL_CTX_new(TLS_method());
  param = SSL_CTX_get0_param(ssl_ctx);

  //set certificate verify

  X509_VERIFY_PARAM_set_hostflags(param, X509_CHECK_FLAG_NO_PARTIAL_WILDCARDS);
  X509_VERIFY_PARAM_set1_host(param, argv[1], 0);
  SSL_CTX_set_verify(ssl_ctx, SSL_VERIFY_PEER, NULL);
  if (SSL_CTX_load_verify_locations(ssl_ctx, ca_bundle, NULL) != 1) {
    printf("Couldn't load certificate trust store.\n");
    returncode=1;
    goto end;
  }

connect:

  //connect

  sbio = BIO_new_ssl_connect(ssl_ctx);
  BIO_get_ssl(sbio, &ssl);
  if (!ssl) {
    printf("Connection failed\n");
    returncode=2;
    goto connect_end;
  }

  //handshake
  SSL_set_tlsext_host_name(ssl, url);
  BIO_set_conn_hostname(sbio, url);
  if(SSL_do_handshake(ssl) <= 0) {
    printf ("REJECT\n");
  } else {
    printf ("ACCEPT\n");
  }

connect_end:

  BIO_free_all(sbio);

end:

  SSL_CTX_free(ssl_ctx);
  EVP_cleanup();
  ERR_free_strings();

	return returncode;
}
