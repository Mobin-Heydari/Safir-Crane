/**
 * Themeparsi Plugin - Products Compare
 *
 * @version 1.2.0
 */
'use strict';
window.Themeparsi || (window.Themeparsi = {});
(function ($) {
    Themeparsi.productCompare = function () {
        function addToCompare(e) {
            e.preventDefault();
            if ($(this).find('.d-loading').length) {
                return;
            }
            var $button = $(this),
                data = {
                    action: 'Themeparsi_add_to_compare',
                    id: $button.data('product_id'),
                    minicompare: $('.header .compare-dropdown').length ? $('.header .compare-dropdown').data('minicompare-type') : '',
                };
            Themeparsi.doLoading($button, 'small');
        }
        function removeFromCompare(e) {
            e.preventDefault();
            if ($(this).find('.d-loading').length) {
                return;
            }
            var $this = $(this),
                data = {
                    action: 'Themeparsi_remove_from_compare',
                    id: $this.data('product_id'),
                };
            if ($this.closest('.mini-item').length) { // mini compare item
                Themeparsi.doLoading($this.closest('.mini-item'), 'small');
            } else {
                Themeparsi.doLoading($this, 'small');
            }
        }
        function addedToCompareList(e, prod_id) {
            $('.compare[data-product_id="' + prod_id + '"]').addClass('remove_from_compare');
            if ($('.header .compare-open').length) {
                var $count = $('.header .compare-open').find('.compare-count'),
                    $dropdown = $('.header .compare-dropdown'),
                    $html = '';
                if ($count.length) {
                    var qty = $count.html();
                    qty = qty.replace(/[^0-9]/, '');
                    qty = parseInt(qty) + 1;
                    $count.html(qty);
                }
                if ($dropdown.find('.empty-msg').length) {
                    $dropdown.find('.widget_compare_content').html($('script.Themeparsi-minicompare-list-html').html());
                }
                $dropdown.find('.compare-list').append();
            }
        }
        function removedFromCompareList(e, prod_id) {
            $('.compare[data-product_id="' + prod_id + '"]').removeClass('remove_from_compare');
            if ($('.header .compare-open').length) {
                var $count = $('.header .compare-open').find('.compare-count'),
                    $dropdown = $('.header .compare-dropdown');
                if ($count.length) {
                    var qty = $count.html();
                    qty = qty.replace(/[^0-9]/, '');
                    qty = parseInt(qty) - 1;
                    $count.html(qty);
                }
                if ($dropdown.find('.mini-item').length > 1) {
                    $dropdown.find('.remove_from_compare[data-product_id="' + prod_id + '"]').closest('.mini-item').remove();
                } else {
                    $dropdown.find('.widget_compare_content').html($('script.Themeparsi-minicompare-no-item-html').html());
                }
            }
        }
        function changeCompareItemPos(e) {
            e.preventDefault();
            var $basicInfo = $(this).closest('.compare-basic-info');
            if ($basicInfo.find('.d-loading').length) {
                return;
            }
            var $button = $(this),
                idx = $button.closest('.compare-value').index() - 1;
            $(this).closest('.compare-table').find('.compare-row').each(
                function () {
                    var $orgItem = $(this).children('.compare-value').eq(idx),
                        $dstItem = $button.hasClass('to-right') ? $orgItem.prev() : $orgItem.next(),
                        orgMove = ($button.hasClass('to-right') ? '-' : '') + '20%',
                        dstMove = ($button.hasClass('to-right') ? '' : '-') + '20%';
                    $orgItem.animate(
                        {
                            right: orgMove
                        },
                        200,
                        function () {
                            $orgItem.css('right', '');
                            if ($button.hasClass('to-right')) {
                                $orgItem.after($dstItem);
                            } else {
                                $orgItem.before($dstItem);
                            }
                        }
                    );
                    $dstItem.animate(
                        {
                            right: dstMove
                        },
                        200,
                        function () {
                            $dstItem.css('right', '');
                        }
                    );
                }
            );
        }
        $(document)
            .on('click', '.product a.compare:not(.remove_from_compare)', addToCompare)
            .on('click', '.remove_from_compare', removeFromCompare)
            .on('added_to_compare', addedToCompareList)
            .on('removed_from_compare', removedFromCompareList)
            .on('click', '.compare-table .to-right, .compare-table .to-left', changeCompareItemPos)
            .on('click', '.compare-offcanvas .compare-open', function (e) {
                $(this).closest('.compare-dropdown').toggleClass('opened');
                e.preventDefault();
            })
            .on('click', '.compare-offcanvas .btn-close', function (e) {
                e.preventDefault();
                $(this).closest('.compare-dropdown').removeClass('opened');
            })
            .on('click', '.compare-offcanvas .compare-overlay', function (e) {
                $(this).closest('.compare-dropdown').removeClass('opened');
            })
            .on('Themeparsi_minicart_popup_product', function (args) {
                if ('undefined' == typeof args && 'undefined' == typeof args[1]) {
                    return {};
                }
                if (args[1].closest('.minipopup-box').length) { // inside compare popup
                    var $product = args[1].closest('.minipopup-box').find('.product');
                    return {
                        link: $product.find('.product-media > a').attr('href'),
                        image: $product.find('.product-media img').attr('src'),
                        title: $product.find('.product-title').text(),
                        price: $product.find('.price').html()
                    };
                } else if (args[1].closest('.compare-table').length) { // inside compare page
                    var $product = args[1].closest('.compare-basic-info');
                    return {
                        link: $product.find('.product-title').attr('href'),
                        image: $product.find('.product-media img').attr('src'),
                        title: $product.closest('.compare-table').find('.compare-title .compare-value').eq(args[1].closest('.compare-value').index() - 1).find('.product-title').html(),
                        price: $product.closest('.compare-table').find('.compare-price .compare-value').eq(args[1].closest('.compare-value').index() - 1).html()
                    };
                }
                return {};
            });
    }
    $(window).on('Themeparsi_complete', Themeparsi.productCompare);
})(jQuery);
