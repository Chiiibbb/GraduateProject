import xadmin
from django.core.cache import cache
from xadmin import views
from .models import *


class GlobalSettings(object):
    site_title = '零食外卖系统后台管理'  # 修改页眉
    site_footer = "Rich Studio"  # 修改页脚
    menu_style = 'accordion'  # 修改菜单栏 改成收缩样式


class BaseSetting(object):
    enable_themes = True  # 开启主题使用
    use_bootswatch = True  # 开启主题选择  (不过我并没有发现主题列表)


class BaseModelAdmin(object):
    def save_models(self):
        obj = self.new_obj

        # 发出任务，让celery worker重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()
        # 清除首页的缓存数据
        cache.delete('index_page_data')
        # 保存该对象
        obj.save()

    def delete_models(self):
        obj = self.new_obj

        # 发出任务，让celery worker重新生成首页静态页
        from celery_tasks.tasks import generate_static_index_html
        generate_static_index_html.delay()
        # 清除首页的缓存数据
        cache.delete('index_page_data')
        # 保存该对象
        obj.save()


class GoodsTypeAdmin(BaseModelAdmin):
    pass


class IndexGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    pass


class IndexPromotionBannerAdmin(BaseModelAdmin):
    pass


xadmin.site.register(GoodsSKU)
xadmin.site.register(Goods)
xadmin.site.register(GoodsImage)
xadmin.site.register(GoodsType, GoodsTypeAdmin)
xadmin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
xadmin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
xadmin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
