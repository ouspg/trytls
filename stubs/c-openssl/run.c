#include <stdio.h>
#include <string.h>
#include <err.h>

#include <openssl/ssl.h>
#include <openssl/x509v3.h>
#include <openssl/err.h>

#define MAX_LENGTH 1024
#define FATAL_ERROR 537423874

int main(int argc, char *argv[]) {

  unsigned int bundleLength=0, urlLength=0;

  if (argc == 3) {
    printf("UNSUPPORTED\n");  //for now at least
    return EXIT_SUCCESS;
  } else if (argc != 4) {
    printf("usage: %s <host> <port> <ca-bundle>\n", argv[0]);
    return EXIT_FAILURE;
  } else if ((urlLength = strlen(argv[1]) + strlen(argv[2]) + 2) > MAX_LENGTH) {
    printf("Too long URL: %d characters, max: %d\n", urlLength, MAX_LENGTH);
    return EXIT_FAILURE;
  } else if ((bundleLength = strlen(argv[3]) + 1) > MAX_LENGTH) {
    printf("Too long ca-bundle filepath: %d characters, max: %d\n", bundleLength, MAX_LENGTH);
    return EXIT_FAILURE;
  }

  char url[1024];       snprintf(url, sizeof(url), "%s:%s", argv[1], argv[2]);
  char ca_bundle[1024]; memcpy(ca_bundle, argv[3], bundleLength);
  int exitvalue = 0;

  BIO *sbio;
  SSL_CTX *ssl_ctx;
  SSL *ssl;
  X509 *cert;

  const char *servername = NULL;
  X509_VERIFY_PARAM *param = NULL;

  SSL_load_error_strings();
  SSL_library_init();

  ssl_ctx = SSL_CTX_new(TLS_method());
  param = SSL_CTX_get0_param(ssl_ctx);

  //set certificate verify
  //https://wiki.openssl.org/index.php/Hostname_validation
  X509_VERIFY_PARAM_set_hostflags(param, X509_CHECK_FLAG_NO_PARTIAL_WILDCARDS);
  X509_VERIFY_PARAM_set1_host(param, argv[1], 0);
  SSL_CTX_set_verify(ssl_ctx, SSL_VERIFY_PEER, NULL);
  if (SSL_CTX_load_verify_locations(ssl_ctx, ca_bundle, NULL) != 1) {
    printf("Couldn't load certificate trust store\n");
    printf("%s\n", ERR_reason_error_string(ERR_get_error()));
    exitvalue=EXIT_FAILURE;
    goto end;
  }

  sbio = BIO_new_ssl_connect(ssl_ctx);
  BIO_get_ssl(sbio, &ssl);
  if (!ssl) {
    printf("Connection failed\n");
    printf("%s\n", ERR_reason_error_string(ERR_get_error()));
    exitvalue=EXIT_FAILURE;
    goto connect_end;
  }

  //handshake
  SSL_set_tlsext_host_name(ssl, url);
  BIO_set_conn_hostname(sbio, url);
  if(SSL_do_handshake(ssl) <= 0) {
    unsigned long int error = ERR_get_error();
    if (error == FATAL_ERROR) {
      printf("Fatal Error: %s\n", ERR_reason_error_string(error));  //maybe better context printing in the future
    } else {
      printf("%s\n", ERR_reason_error_string(error));
      printf("REJECT\n");
    }
  } else {
    printf ("ACCEPT\n");
  }

connect_end:

  BIO_free_all(sbio);

end:

  SSL_CTX_free(ssl_ctx);
  EVP_cleanup();
  ERR_free_strings();

  return exitvalue;
}
