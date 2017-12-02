/**
 * Created by imlv  on 27-11-2017.
 */
// Calls intelliq server for question generation 
var request = require('request');
exports.getQuestion = function (text,callback){
    var options = {
        //uri: 'http://127.0.0.1:8000/generate_qa',
		uri: 'https://glacial-castle-64742.herokuapp.com/?format=json',
        method: 'POST',
        json: {
            "mytopic": text
        }
    };
    request(options, function (error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body)
            callback(body);
        }
    })
}
