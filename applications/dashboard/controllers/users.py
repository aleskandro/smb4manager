# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

from util.smb4_util import SMB4UTIL
from util.ldap_util import LDAPUTIL


@auth.requires_login()
def index():
    util = LDAPUTIL(get_config())
    users = util.getUser(attributes=['sAMAccountName','name'])
    logger.debug(str(users))
    return dict(users=users)


@auth.requires_login()
def delete():
    if (request.args): 
         smbtool = SMB4UTIL(get_config());
         logger.debug('Deleted username: %s' % request.args[0])
         smbtool.deleteUser(request.args[0])
         response.flash = "User %s DELETEDE" %(request.args[0])
         redirect(URL('users', 'index'))
         #return "User %s DELETEDE" %(request.args[0])
    return "Set User for Exclude"



@auth.requires_login()
def add():
    if request.post_vars:
       #print request.post_vars
       #print request.post_vars.mail
       smbtool = SMB4UTIL(get_config());
       res_add = smbtool.addUser(request.post_vars.sAMAccountName, request.post_vars.userPassword, 
                                request.post_vars.mail, request.post_vars.givenName, request.post_vars.surname)
       #print res_add
       #if (res_add[0] == 'SUCCESS'): redirect(URL('users', 'index'))
       return res_add[1]
    return dict()



@auth.requires_login()
def edit():
    #return "Set User for Exclude"
    return dict()