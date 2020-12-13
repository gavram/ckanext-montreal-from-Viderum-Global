import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.montreal import helpers


class MontrealPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IRoutes)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'montreal')

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'montreal_get_groups': helpers.get_groups,
            'get_recently_updated_datasets':
                helpers.get_recently_updated_datasets,

        }
    
    def download(self, package_id, resource_id, file_name):
        # Use Response with content_disposition as attachement.
        if response.content_type == 'Application/json':
            response.content_disposition = 'attachment'
            response.content_type = 'Application/octet-stream'
            response.cache_control = 'no-cache';
        #Use ckan internal resource_download method
        return self.resource_download(package_id,resource_id,file_name)
    
    def preview(self, package_id, resource_id, file_name):
        response.content_disposition = 'inline'
        return self.resource_download(package_id,resource_id,file_name)

    # IRoutes

    def before_map(self, map):
        static_ctrl = 'ckanext.montreal.controller:StaticController'
        map.connect('newsletter', '/abonnement',
                    controller=static_ctrl, action='newsletter')
        contact_ctrl = 'ckanext.montreal.controller:ContactController'
        map.connect('contact', '/nous-joindre',
                    controller=contact_ctrl, action='contact_form')
        return map

    def after_map(self, map):
        return map
