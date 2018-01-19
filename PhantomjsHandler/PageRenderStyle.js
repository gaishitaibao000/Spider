//  2 var page = require('webpage').create();
//  3 page.open("http://www.baidu.com", function(status) {
//  4    if ( status === "success" ) {
//  5       console.log(page.title);
//  6       page.paperSize = { format: 'A4',
//  7             orientation: 'portrait',
//  8             border: '1cm' };
//  9       page.render("front-Thinking.pdf");
// 10    } else {
// 11       console.log("Page failed to load.");
// 12    }
// 13    phantom.exit(0);
// 14 });
var page = require('webpage').create();
page.open('http://www.baidu.com',function (status) {
    if (status === 'success') {
        console.log(page.title);
        page.paperSize = {
            format:'A4',
            orientation: 'portrait',
            border: '5cm'};
        page.render('baidu.png')
    }
    phantom.exit()
});

