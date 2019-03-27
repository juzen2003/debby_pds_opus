var o_menu = {

    /**
     *
     *  the menu on the *search page*
     *
     **/

     menuBehaviors: function() {
         // search menu behaviors

         // click cat header in menu toggles arrow style
        // $('#sidebar').on("click", 'a', function() {
        //    $(this).find('b.arrow').toggleClass('fa-angle-right').toggleClass('fa-angle-down');

         //});
         $('#sidebar').on("click", '.searchMenu li .dropdown-toggle', function() {
             let adjustSearchSideBarHeight = _.debounce(o_search.adjustSearchSideBarHeight, 500);
             adjustSearchSideBarHeight();
         })

         // click param in menu get new widget
         $('#sidebar').on("click", '.submenu li a', function() {

             let slug = $(this).data('slug');
             if (!slug) { return; }
             if ($.inArray(slug, opus.widgets_drawn)>-1){
                 // widget is already showing do not fetch another
                 try {
                    // scroll to widget and highlight it
                    o_widgets.scrollToWidget('widget__'+slug);

                } catch(e) {
                    return false;
                }
                return false;

             } else {
                  o_menu.markMenuItem(this);
                  o_widgets.getWidget(slug,'#search_widgets');
             }

             o_hash.updateHash();
             return false;
         });


        // menu state - keep track of what menu items are open
        $("#sidebar").on("click", ".dropdown-toggle", function(e) {
            // for opus: keeping track of menu state, since menu is constantly refreshed
            // menu cats
            let category = $(this).data( "cat" );
            let groupElem = $(`#sidebar #submenu-${category}`);
            if ($(groupElem).hasClass("show")) {
                opus.menu_state.cats.splice(opus.menu_state.cats.indexOf(category), 1);
            } else {
                if ($.inArray(category, opus.menu_state.cats) >= 0 ) {
                    console.log(`submenu ${category } state already in array`);
                } else {
                    opus.menu_state.cats.push(category);
                }
            }
        });

        $(".searchMenu").on("shown.bs.collapse", function(e) {
            o_search.adjustSearchHeight();
        });
     },

     getMenu: function() {
        $('.menu_spinner').fadeIn("fast").css("display", "inline-block");
        var hash = o_hash.getHash();

        $( "#sidebar").load( "/opus/__menu.html?" + hash, function() {
            // open menu items that were open before
            $.each(opus.menu_state.cats, function(key, category) {
                if ($(`#submenu-${category}`).length != 0) {
                    $(`#submenu-${category}`).collapse('show');
                } else {
                    // this is if the surface geometry target is no longer applicable so it's not
                    // on the menu, remove from the menu_state
                    opus.menu_state.cats.splice(opus.menu_state.cats.indexOf(category), 1);
                }
            });
            $('.menu_spinner').fadeOut("fast");
            o_menu.markCurrentMenuItem();
            // when a new category is open after an input is clicked, we update the scrollbar
            let adjustSearchSideBarHeight = _.debounce(o_search.adjustSearchSideBarHeight, 500);
            adjustSearchSideBarHeight();
        });
     },
     markDefaultMenuItem: function() {
         o_menu.markMenuItem(".submenu li a", "unselect");
         $.each(opus.default_widgets, function(index, slug) {
             o_menu.markMenuItem(`li > [data-slug="${slug}"]`);
         });
     },

     markMenuItem: function(selector, selected) {
        if (selected == undefined || selected == "select") {
            $(selector).css("background", "gainsboro");
            $(selector).find("i.fa-check").fadeIn().css('display', 'inline-block');
        } else {
            $(selector).css("background", "initial");
            $(selector).find("i.fa-check").hide();
      }
     },

     markCurrentMenuItem: function() {
         $.each(opus.widgets_drawn, function(index, slug) {
             o_menu.markMenuItem(`li > [data-slug="${slug}"]`);
         });
     },

     // type = cat/group
     getCatGroupFromSlug: function(slug) {
         var cat = '';
         var group = '';
         $('ul.menu_list>li a', '#search').each(function() {
             if (slug == $(this).data('slug')) {
                 cat = $(this).data('cat');
                 group = $(this).data('group');
                 return false; // this is how you break in an each!
             }
         });
         return {"cat":cat, "group":group};
     },
};
