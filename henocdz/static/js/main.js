$(dz);

function dz(){
	

	resize_content();
	var _s = new Sliderama();

	$(window).resize(resize_content);

	var h = (location.hash).replace('#','');
	if(h === 'about')
		_s.show_sc(0)
	else if(h == 'projects')
		_s.show_sc(1)
	else if(h == 'tutorials')
		_s.show_sc(2)
	else if(h == 'contact')
		_s.show_sc(3)
	else
		_s.show_sc(0)

	$('.sc-title').on('click',function (){ _s.show_sc( $(this).parents('.sc').index()); })
	$(' #da-thumbs > li ').each( function() { $(this).hoverdir(); } );
	$('#menu-show').on('click',function(){
		var n = $('#menu');
		if( n.css('display') == 'block')
			n.slideUp();
		else
			n.slideDown();
	})
}

function resize_content(){
	var c = $('#content'),	w = $(window), h = $('header');
	var active_w = 101.2 - ( ( 60 * 100 / $(window).width() * 3)  ) + '%';

	c.css('height', (100 -  (h.height() * 100 / $(window).height())) + '%' );
	$('.sc-active').css('width',active_w);

	if(w.width() > 960)
		$('#menu').slideUp(10,function(){c.css('height', (100 -  (h.height() * 100 / $(window).height())) + '%' );});
}

function Sliderama(){
	var parent = this;
	this.pre = -1,
	this.now = 0,
	this.title=$('#stitle'), 
	this.apiscroll, 
	this.w = $('window'),
	this.main = $('#content');
	
	this.show_sc = function(index){
		var self = $('.sc').eq(index);

		parent.now = index;
		if(parent.now === parent.pre || $(window).width() < 960)
			return;

		var aux = parent.pre;

		$('.sc').eq(parent.pre).children('.sc-content').slideUp('fast',function(){
							
			$('.sc').eq(aux).children('.sc-title').css({
					width:60,
					display:'block'
			});

			self.prevAll().animate({width:60})
			self.nextAll().animate({width:60})

			parent.title.text(" - "+self.children('.sc-title').text());

			self.children('.sc-title').animate({
				width:0,
			},function (){
				self.children('.sc-title').css('display','none');
				self.children('.sc-content').fadeIn();
			});

			self.addClass('sc-active');
			 $('.sc').eq(parent.pre).removeClass('sc-active');

			self.animate({
				width:  101.2 - ( ( 60 * 100 / $(window).width() * 3)  ) + '%'
			},function (){
				parent.main.css('background',$('.sc:last').css('background'))
				parent.pre = parent.now;
			});

			
		});
	}
}

