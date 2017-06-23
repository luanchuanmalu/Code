
proxy_pass

语法: proxy_pass URL

默认值: no

上下文: location, if in location

This directive sets the port or socket, on which listens to the proxied server, and the URI, to which will be reflected location.

Port can be indicated in the form of the name of hostname or address and port, for example,

proxy_pass http://localhost:8000/uri /;

and socket -- in the form of unix of socket:

proxy_pass http://unix:/tmp/backend.socket:/uri /;
Path is indicated after the word
unix
and is concluded between two colons.

With the transfer of request to server part URI, which corresponds to location, is substituted to URI, indicated in directive proxy_pass.

But there are two exceptions to this rule, when it is not possible to determine that replaced location:

if the location is assigned by regular expression;
if inside proxied location with the help of directive rewrite changes URI and with this configuration will be precisely processed request (break):
location  /name/ {
: rewrite      /name/([^/] +)  /users?name=$1  break;
: proxy_pass   http://127.0.0.1;
}
For these cases of URI it is transferred without the mapping.

Furthermore, it is possible to indicate so that URI demand it would be transferred in the same form, as it sent client, but not v in the processed form.

During the working:

two or by more slashes are converted into one slash: "//" -- "/";
references to the current directory are removed: "/./" -- "/";
references to the previous catalog are removed: "/dir /../" -- "/".
If on server it is necessary to transmit URI in the unprocessed form, then for this in directive proxy_pass it is necessary to indicate URL server without URI:

location  /some/path/ {
: proxy_pass   http://127.0.0.1;
}
proxy_pass_header

语法: proxy_pass_header the_name

上下文: http, server, location

This directive allows transferring header-lines forbidden for response.

For example:

location / {
: proxy_pass_header Server;
: proxy_pass_header X-MyHeader;
}
proxy_pass_request_body

语法: proxy_pass_request_body [ on | off ] ;

默认值: proxy_pass_request_body on;

上下文: http, server, location

Available since: 0.1.29
TODO: Description.

proxy_pass_request_headers

语法: proxy_pass_request_headers [ on | off ] ;

默认值: proxy_pass_request_headers on;

上下文: http, server, location

Available since: 0.1.29
TODO: Description.

proxy_redirect

语法: proxy_redirect [ default|off|redirect replacement ]

默认值: proxy_redirect default

上下文: http, server, location

This directive sets the text, which must be changed in response-header "Location" and "Refresh" in the response of the proxied server.

Let us suppose the proxied server returned line
Location: http://localhost:8000/two/some/uri/
.

The directive


proxy_redirect   http://localhost:8000/two/   http://frontend/one/;
will rewrite this line in the form
Location: http://frontend/one/some/uri/
.

In the replaceable line it is possible not to indicate the name of the server:


proxy_redirect http://localhost:8000/two/ /;
then the basic name of server and port is set, if it is different from 80.

The change by default, given by the parameter "default", uses the parameters of directives location and proxy_pass.

Therefore two following configurations are equivalent:

location /one/ {
: proxy_pass       http://upstream:port/two/;
: proxy_redirect   default;
}

location /one/ {
: proxy_pass       http://upstream:port/two/;
: proxy_redirect   http://upstream:port/two/   /one/;
}
In the replace line, it is possible to use some variables:

proxy_redirect   http://localhost:8000/    http://$host:$server_port/;
This directive repeated some times:


: proxy_redirect   default;
: proxy_redirect   http://localhost:8000/    /;
: proxy_redirect   http://www.example.com/   /;
The parameter
off
forbids all
proxy_redirect
directives at this level:

: proxy_redirect   off;
: proxy_redirect   default;
: proxy_redirect   http://localhost:8000/    /;
: proxy_redirect   http://www.example.com/   /;
With the help of this directive it is possible to add the name of host for relative redirect, issued by the proxied server:

proxy_redirect   /   /;
