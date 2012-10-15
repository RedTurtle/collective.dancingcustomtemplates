# -*- coding: utf-8 -*-
from collective.dancing.browser.subscribe import Confirm


class CustomConfirm(Confirm):
    """
    Custom confirm view
    """
#    contents = ViewPageTemplateFile('templates/status.pt')

    @property
    def contents(self):
        """
        """
        custom_status_template = self.context.restrictedTraverse('confirm_newsletter_status', None)
        if not custom_status_template:
            return super(CustomConfirm, self).contents()
        return custom_status_template(status=self.status)

#    label = _(u"Confirming your subscription")
