class Attack(object):
  def __init__(self, link, form_parameter, button, cookie, type):
    """A session_hijacking_attack object."""
    self.link = link
    self.form_parameter = form_parameter
    self.button = button
    self.cookie = cookie
    self.type = type

  def perform(self):
    raise NotImplementedError("Please Implement this method")

  def show_details(self):
    """Show information of the attack """
    print ("link %s; forma_paramster %s; button_name %s; cookie %s" %(self.link, self.form_parameter, self.button_name, self.cookie))
