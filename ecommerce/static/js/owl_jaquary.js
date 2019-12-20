$(document).ready(function() {
 
    $("#owl-demo").owlCarousel({

        // setting responsive
        
        responsive:{
            0:{
                items:2
            },
            680:{
                    items:2
            },  
            998:{
                items:3
            },
            1080:{
                items:4
            },
          
        },

          // end of responsive

        autoplay: 3000, //Set AutoPlay to 3 seconds
        margin:10,
        loop:true,
        // nav:true,
       
        paginationNumbers:false,
        // items : 3,
        // itemsDesktop : [1199,4],
        // itemsDesktopSmall : [979,2],
        // itemsDesktop : [1199,4],
        // itemsDesktopSmall : [980,3],
        // itemsTablet: [768,2],
        // itemsTabletSmall: false,
        // itemsMobile : [479,2],
        // singleItem : false,
   
    });
   
  });