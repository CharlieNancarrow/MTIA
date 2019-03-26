(function(){
    ('#yes').click(fucntion(){
        chrome.storage.sync.get(document.URL, fucntion(url){
            console.log
        })
    })
});
