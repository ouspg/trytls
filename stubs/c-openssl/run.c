#include <stdio.h>
#include <openssl/ssl.h>
#include <openssl/err.h>

#include <string.h>
#include <openssl/conf.h>
#include <openssl/x509v3.h>

/*

./run badssl.com 443 /etc/ssl/certs/ca-certificates.crt

*/

int verify_cert_hostname(X509 *cert, char *hostname);

int main(int argc, char *argv[]) {

  if (argc < 4) {
    printf("UNSUPPORTED");  //for now at least
    return 3;
  }

  BIO *sbio;
	SSL_CTX *ssl_ctx;
	SSL *ssl;
	X509 *cert;

  int returncode = 0;

  char url[256]; sprintf(url, "%s:%s", argv[1], argv[2]);
  char ca_bundle[256]; strcpy(ca_bundle, argv[3]);

//init:

  SSL_library_init();
  SSL_load_error_strings();

  ssl_ctx = SSL_CTX_new(TLSv1_client_method());
  SSL_CTX_set_verify(ssl_ctx, SSL_VERIFY_PEER, NULL);
  if (SSL_CTX_load_verify_locations(ssl_ctx, ca_bundle, NULL) != 1) {
    printf("Couldn't load certificate trust store.");
    returncode=1;
    goto end;
  } else {
    goto connect;
  }

connect:

  sbio = BIO_new_ssl_connect(ssl_ctx);
  BIO_get_ssl(sbio, &ssl);
  if (!ssl) {
    printf("Connection failed");
    returncode=2;
    goto connect_end;
  }

  SSL_set_tlsext_host_name(ssl, url);
  BIO_set_conn_hostname(sbio, url);

  if(SSL_do_handshake(ssl) <= 0 || !verify_cert_hostname(SSL_get_peer_certificate(ssl), argv[1])) {
    printf ("VERIFY FAILURE");
  } else {
    printf ("VERIFY SUCCESS");
  }

  X509_free(cert);
	BIO_ssl_shutdown(sbio);

connect_end:

  BIO_free_all(sbio);

end:

  SSL_CTX_free(ssl_ctx);
  EVP_cleanup();
  ERR_free_strings();

	return returncode;
}

int verify_cert_hostname(X509 *cert, char *hostname) {
  int                   extcount, i, j, ok = 0;
  char                  name[256];
  X509_NAME             *subj;
  const char            *extstr;
  unsigned char         *data;
  X509_EXTENSION        *ext;
  X509V3_EXT_METHOD     *meth;

  int l = strlen(hostname);
  char hostname_end[256];
  strncpy(hostname_end, hostname, sizeof(hostname_end));
  hostname_end[l+1]=hostname[l];
  hostname_end[l]='.';

  //update me [WIP] - feel free to edit
  if ((extcount = X509_get_ext_count(cert)) > 0) {
    for (i = 0;  !ok && i < extcount;  i++) {
      ext = X509_get_ext(cert, i);
      extstr = OBJ_nid2sn(OBJ_obj2nid(X509_EXTENSION_get_object(ext)));
      if (!strcasecmp(extstr, "subjectAltName")) {
        if (!(meth = X509V3_EXT_get(ext))) break;
        data = ext->value->data;
        int i;
        if (/*i = */strstr(data, hostname) != NULL){
          //printf("dada: %d\n", i);
          if (strstr(data, hostname_end) == NULL) {
            ok = 1;
            break;
          }
        }
      }
    }
  }

  if (!ok && (subj = X509_get_subject_name(cert)) &&
      X509_NAME_get_text_by_NID(subj, NID_commonName, name, sizeof(name)) > 0) {
    name[sizeof(name) - 1] = '\0';
    if (!strcasecmp(name, hostname)) {
      ok = 1;
    }
  }

  return ok;
}
