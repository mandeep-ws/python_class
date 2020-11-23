(function() {
    var hostname = window.location.hostname.toLowerCase();
    var env = 'local';
    if (hostname.indexOf('dev') > -1) {
        env = 'dev';
    } else if (hostname.indexOf('test') > -1) {
        env = 'test';
    } else if (hostname.indexOf('pre') > -1) {
        env = 'pre';
    } else if (hostname.indexOf('bms.web.boeing.com') > -1) {
        env = 'prod';
    } else {
        env = 'local';
    }

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200 && this.responseText) {
            var time = new Date().getTime();
            window['adrum-start-time'] = time;
            var text = this.responseText.toString();
            var textJSON = JSON.parse(text);
            console.log('Response Text: ' + JSON.stringify(textJSON));
            (function(config) {
                var userInfo = {};
                if (env === 'dev') {
                    userInfo = {
                        userData: {},
                        userDataDate: {currentTime: time},
                    };
                } else {
                    userInfo = {
                        userData: {},
                        userPageName: document.title,
                        userDataDate: {currentTime: time},
                    };
                }
                Object.keys(textJSON).forEach(function(key) {
                    userInfo.userData[key] = textJSON[key].toString();
                });
                config.userEventInfo = {
                    PageView: userInfo,
                    Ajax: userInfo,
                    VPageView: userInfo,
                };
                config.adrumExtUrlHttp = window.location.origin + '/adrum';
                config.adrumExtUrlHttps = window.location.origin + '/adrum';
                config.xd = {enable: false};
                config.spa = {spa2: true};
                config.beaconUrlHttp = 'http://appd-itms-ew06.ca.boeing.com:7001';
                config.beaconUrlHttps = 'https://appd-itms-ew06.ca.boeing.com:7002';
                switch (env) {
                    case 'dev':
                        config.appKey = 'EUM-AAB-AZC';
                        break;
                    case 'test':
                        config.appKey = 'EUM-AAB-AZD';
                        break;
                    case 'pre':
                        config.appKey = 'EUM-AAB-AUA';
                        break;
                    case 'prod':
                        config.appKey = 'EUM-AAB-AUB';
                        config.beaconUrlHttp = 'http://appd-itms-ew04.ca.boeing.com:7001';
                        config.beaconUrlHttps = 'https://appd-itms-ew04.ca.boeing.com:7002';
                        break;
                    default:
                        config = {};
                        break;
                }
                //Todo remove log once validated and in prod.
                console.log('EUM Configuration: ' + JSON.stringify(config));
            })(window['adrum-config'] || (window['adrum-config'] = {}));
            var adrumLatest = document.createElement('SCRIPT');
            adrumLatest.type = 'text/javascript';
            adrumLatest.src = window.location.origin + '/adrum/adrum-latest.preprod.js';
            document.head.appendChild(adrumLatest);
        }
    };
    var charmUrl =
        env.indexOf('local') > -1 ? 'http://localhost:9090/api/v1/user' : window.location.origin + '/api/v1/user';
    xhttp.open('GET', charmUrl, true);
    xhttp.send();
})();
