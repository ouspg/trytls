#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <tls.h>
#include <err.h>

int main(int argc, char **argv) {
  struct tls_config *config;
  struct tls *context;
  char *host;
  char *port;
  char *ca_file = NULL;
  int exit_value = EXIT_SUCCESS;

  char write_buf[1024];
  char read_buf[1024];

  write_buf[0] = '\0';
  read_buf[0] = '\0';

  if (argc < 3 || argc > 4) {
    printf("%s <host> <port> [ca-bundle]\n", argv[0]);
    return EXIT_FAILURE;
  }

  host = argv[1];
  port = argv[2];

  if (argc == 4)
    ca_file = argv[3];

  if (tls_init() == -1)
    err(1, "tls_init");

  config = tls_config_new();
  if (config == NULL)
    err(1, "tls_config_new");

  if (ca_file) {
    if (tls_config_set_ca_file(config, ca_file) == -1)
      err(1, "tls_config_set_ca_file");
    printf("Using CA bundle from %s\n", ca_file);
  }

  context = tls_client();
  if (context == NULL)
    err(1, "tls_client");

  if (tls_connect(context, host, port) == -1)
    err(1, "tls_connect");

  if (tls_handshake(context) == -1) {
    printf("%s\n", tls_error(context));
    printf("REJECT\n");
    exit_value = EXIT_SUCCESS;
    goto cleanup;
  }

  /* Send HTTP GET request */
  snprintf(write_buf, sizeof(write_buf),
	   "%s\r\n%s: %s\r\n\r\n",
	   "GET / HTTP/1.0",
	   "Host", host);
  if (tls_write(context, write_buf, strlen(write_buf)) == -1)
    err(1, "tls_write");

  /* Read HTTP GET response */
  if (tls_read(context, read_buf, sizeof(read_buf)) == -1)
    err(1, "tls_read");

  /* We only care about the first line from HTTP GET response */
  for (int i=0; i < strlen(read_buf); i++) {
    if (read_buf[i] == '\n') {
      read_buf[i] = '\0';
      break;
    }
  }

  printf("%s\n", read_buf);
  printf("ACCEPT\n");
  exit_value = EXIT_SUCCESS;

 cleanup:
  tls_close(context);
  tls_free(context);
  tls_config_free(config);

  return exit_value;
}
