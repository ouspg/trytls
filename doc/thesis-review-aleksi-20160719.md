These are persistent notes of the [OUSPG open](https://github.com/ouspg/ouspg-open) review of the draft of [Aleksi Klasila's trytls](https://github.com/ouspg/trytls/tree/Klasila_Aleksi_Bach_Thesis/doc/Klasila_Aleksi_Bach_Thesis) B.Sc. thesis on  [etherpad](http://muistio.tieke.fi/p/trytls) [7 reviewers]

# Generic notes

 * Overall impression: this is going to be a good, solid and significant contribition
 * There are some typos that would be caught by a basic spell checker (please consider installing/enabling a spell check plugin to your editor)
  * Word actually does the job well, and university library has access to MOT proof (see MOT sanakirja on library.oulu.fi front page)
   * editor spell checker does nice runtime linting of spelling and periodically you can paste the markdown to word to double check,
e.g  Atom would have caught most of these by default
  * You are losing now a lot of review bandwidth to people wasting time on trivial typos/misspellings

> eNcryption

 * formatting -> Encryption

# Abstract

 * Abstract (ja Tiivistelmä) now start with apolegetic term explanaton, whereas this sort of good work deserves to start with a bang
  * Maybe consider starting with "Encyption is a fundamental building block in protecting our privacy and safety of our society, unfortunately
  we may fail to use it properly. Transport Layer Security (TLS) SSL has an important part in encrypting the trafficing on the internet today."
   * and then leave out the SSL to some part of the body text introduction

> In this bachelor's thesis the term SSL is used as TLS(Transport Layer Security)/SSL(Secure Socket Layer). They are technically the same.

   * Use term TLS instead of SSL. TLS 1.0 has been released January 1999 (17 years ago) and SSLv3 is deprecated (in June 2015)
   * Maybe be more specific? In my mind they are definately not the same.
   * Maybe it is time to get rid of the SSL

> In this bachelor's thesis the term SSL is used as TLS(Transport Layer Security)/SSL(Secure Socket Layer). They are technically the same. TLS is only the newer version of SSL.

 * Maybe it is time to start using TLS as default :) (and mention that SSL is just an older and dangerous version of the same)

 This also leads to a test for "If connection is with SSLv2 or v3, we should FAIL"

>  HTTPS(Hypertext Trasfer Protocol Secure)

 * Please consider using space between the term introduction and the abbreviation, systematically

> FTPS(File Transfer Protocol with support for SSL)

 * Unless you really want, maybe use e.g. IMAPS instead of FTPS  as an example ... FTPS never took off but IMAPS actually became popular

Typo in Abstract section trasfer -> transfer
coputers -> computers

> "The backend can be used in testing how different programming languages and libraries"

 * Drop the "programming languages". It's TLS implementation (usually done as a library) which is tested. Programming language is used to implement the TLS.

>  In this thesis a software/backed

 * typo and formatting ->  "In this thesis a software backend"?

>  is a secure(ish) one or not.

 * shorten to -> "is secure" or "is safe"

> internet connnection

 * typo -> internet connection

# Tiivistelmä

 * Tiivistelmä: SSL käyttäviä protokollia --> SSL:ää käyttäviä protokollia
 * kandidaattityössä -> kandidaatintyössä?

## 1.1. Related research

There are already many ways developed to be used to test for the weakness of used protocols, --> weaknesses (??)


## 2.8. Problems with the current testing approaches

... tools are not for checking whether if the client checks the certificates correctly or not ... : whether if --> only whether
 (can you move this down a bit -->)

General:
Maybe you could add references after chapters instead in the middle of them

> All the protocols that use SSL have also got many different kind of implementations in different programming languages and libraries.

   * There are a number of TLS-implementations

> In this thesis a software/backed

   * Typo "backed"?


> "The backend can be used in testing how different programming languages and libraries used support SSL protocol and if the way of supporting is a secure(ish) one or not. "

 * Typo "used" -> "use"
 * Why should we be satisfied with "secureish"? How about "secure or not".

> The backend can also be used in testing if libraries check certificates correctly or not.

 * "also" - isn't this the main purpose?

 > I will also research other implementations already developed.

  * Active tone - good!
  * :+1 excellent!

> own coputers

 * typo -> computers

>  This thesis provides a way to test if client libraries do SSL correctly and as expected even without internet connnection.

 * Localhost testing may limit the test coverage? I wonder if localhost testing should be highlighted/advertised as a feature. :/

> It also provides a backend that anyone can run on their own coputers both either to be used in private or to be published/shared with the rest of us.

 * typo: coputers

> Keywords: Tools, TLS/SSL, Security

 * Tools is too generic, maybe -> Keywords: Security testing, Vulnerability research, Assurance tools, TLS, SSL, Security, Encryption

 > TIIVISTELMÄ

  * Skipped

> tunnetuimille ssl:ää käyttäville

 * formattting: tunnetuimille SSL:ää käyttäville
  * or ever better with TLS:ää

 > FOREWORD
  * Skipped

> It was a part of my job during the summer 2016 to create a backend of a kind for testing SSL behavior of different programming languages and their libraries. The backend is a group of servers to which the potential client can try to connect. The backend was to be used mostly on our server to which everyone could try their codes against. This backend I created can be set up very easily to either private use or to be shared with the public. And all that with very little change in the way of setting the backend up.

 * Maybe align this a bit with common goal of the TryTLS ... -> "It was my job to work in the TryTLS core team to develope and popularize the TryTLS approach in order to help library and programming language developers to secure their use of the TLS encryption. We worked as a team on the whole TryTLS product and the TryTLS social enterprise and my specific area of responsibility was the selection, documentation and integration of the test backends. Role of the backends is to provide the tests that the users of the TryTLS can test their implementations against."


# INTRODUCTION

Could also have:
 * Background and motivation
 * Research scope, thesis statement and research objectives
 * Research methodology
 * Structure of thesis

> “The TLS(SSL) protocol provides communications security over the internet

 * Internet with capital I ? - Hmm, this is direct quote? Original uses I
 On the same quote: eyesdropping -> eavesdropping

>  t is not recommended by any means to use libraries that allow the client to be vulnerable to at least any of the known attacks excluding of course testings.

 * "excluding of course testings" - a bit redundant? short = good -> remove?

 > This thesis is about expanding the tool set used to test the testing behavior of SSL libraries and why not even programs that use those libraries.

 * Sharp focus would be one reason for "why not"?


## 1.1. RELATED RESEARCH

> There are not so many tools that by using them the client can check whether if it does the checking correctly or not.

   * Add "however" to the beginnign to emphasize "vastakkainasettelu"?

> There are also not so many tools that tell what ciphers and protocol versions exactly does the client support at least not locally usable ones.

   * Add "furthermore"?

>   Even if the connection is established ‘securely’

 * Even if encrypted connection is established?

> it does not necessarily mean that the connection is necessarily secure

    * Reduntant use of "necessarily"?

    >
In section "1.3. Description of the TryTLS backend approach" -> Backend

  * Quite a lot of repeation of word backend.


> "optional authentication which is usually done using SSL certificates"

 * -> Correct term here is "X.509 certificate". SSL nor TLS doesn't have any certificates by itself

> " You also know that the server is really who it says it is just by having a look at the certificates available."

 * -> Not really true. :)

> No need for internet connection means also that it is relatively safe to test new libraries in action without having to worry about anyone eavesdropping the newborn library or protocol support taking it’s first steps in the world of wonders – surrounded only by the beauty of pure logic.

 * gotta love the emotional content in this sentence
  * However - I wonder if eavesdropping is a real concern here? What is the information to be protected when developing a new library?


# TLS/SSL IN ACTION

> The SSL protocol provides relatively good support for safe connections if used correctly.

 * In sentences like these, it becomes vital to use TLS instead of SSL

 > FTP(S)

  * IMAPS here as well (search & replace)


> The protocol versions currently used and the ones that have been and are still used in some cases are today(06.2016) SSLv2, SSLv3, TLSv1.0, TLSv1.1 and TLSv1.2.

 * Maybe worth separating the useless versions with the modern recommended ones? IF SSLv2 is still used somewhere, that is very unfortunate and outright dangerous


##  2.2 MOTIVATION OF..

 > You also know that the server is really who it says it is just by having a look at the certificates available

 * This is not that black and white? "You can estimate the risk of being intercepted by looking at the certificate chain.."?

> sing SSL is more costly for the servers (and clients) than just using plain text b

 * is prosessing power cost an issue nowadays (in average case)? I'm under impression that the cost is neglible?

> If a server does not support SSL it can use many services available to offer i.a. certificates for http servers using https connection between the client and the security provider.

 * hard-to-understand sentence?
