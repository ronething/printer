var mysql=require('mysql');
var http = require('http');
var server=http.createServer(function(res,res){

	res.writeHead(200,{"Content-Type":"text/plain","Access-Control-Allow-Origin":"http://192.168.164.130"});

	var connection=mysql.createConnection({
	host:'localhost',
	user:'user',
	password:'password',
	database:'linux'
	})
	connection.connect();
	connection.query('SELECT name,id from demo',function(error,results,field){
	if(error) throw error;
    res.write(JSON.stringify(results));
    	res.end();
	});

});
server.listen('8888','192.168.164.130',function(){
console.log("开始监听");
})
