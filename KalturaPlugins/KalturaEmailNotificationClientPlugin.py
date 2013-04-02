# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platfroms allow them to do with
# text.
#
# Copyright (C) 2006-2011  Kaltura Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http:#www.gnu.org/licenses/>.
#
# @ignore
# ===================================================================================================
# @package External
# @subpackage Kaltura
import os.path
import sys

clientRoot = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))
if not clientRoot in sys.path:
    sys.path.append(clientRoot)

from KalturaCoreClient import *
from KalturaEventNotificationClientPlugin import *
from KalturaClientBase import *

########## enums ##########
# @package External
# @subpackage Kaltura
class KalturaEmailNotificationTemplatePriority:
    HIGH = 1
    NORMAL = 3
    LOW = 5

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaEmailNotificationTemplateOrderBy:
    ID_ASC = "+id"
    ID_DESC = "-id"
    CREATED_AT_ASC = "+createdAt"
    CREATED_AT_DESC = "-createdAt"
    UPDATED_AT_ASC = "+updatedAt"
    UPDATED_AT_DESC = "-updatedAt"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package External
# @subpackage Kaltura
class KalturaEmailNotificationDispatchJobData(KalturaEventNotificationDispatchJobData):
    def __init__(self,
            templateId=NotImplemented,
            fromEmail=NotImplemented,
            fromName=NotImplemented,
            to=NotImplemented,
            cc=NotImplemented,
            bcc=NotImplemented,
            replyTo=NotImplemented,
            priority=NotImplemented,
            confirmReadingTo=NotImplemented,
            hostname=NotImplemented,
            messageID=NotImplemented,
            customHeaders=NotImplemented,
            contentParameters=NotImplemented):
        KalturaEventNotificationDispatchJobData.__init__(self,
            templateId)

        # Define the email sender email
        # @var string
        self.fromEmail = fromEmail

        # Define the email sender name
        # @var string
        self.fromName = fromName

        # Email recipient emails and names, key is mail address and value is the name
        # @var array of KalturaKeyValue
        self.to = to

        # Email cc emails and names, key is mail address and value is the name
        # @var array of KalturaKeyValue
        self.cc = cc

        # Email bcc emails and names, key is mail address and value is the name
        # @var array of KalturaKeyValue
        self.bcc = bcc

        # Email addresses that a replies should be sent to, key is mail address and value is the name
        # @var array of KalturaKeyValue
        self.replyTo = replyTo

        # Define the email priority
        # @var KalturaEmailNotificationTemplatePriority
        self.priority = priority

        # Email address that a reading confirmation will be sent to
        # @var string
        self.confirmReadingTo = confirmReadingTo

        # Hostname to use in Message-Id and Received headers and as default HELO string. 
        # 	 If empty, the value returned by SERVER_NAME is used or 'localhost.localdomain'.
        # @var string
        self.hostname = hostname

        # Sets the message ID to be used in the Message-Id header.
        # 	 If empty, a unique id will be generated.
        # @var string
        self.messageID = messageID

        # Adds a e-mail custom header
        # @var array of KalturaKeyValue
        self.customHeaders = customHeaders

        # Define the content dynamic parameters
        # @var array of KalturaKeyValue
        self.contentParameters = contentParameters


    PROPERTY_LOADERS = {
        'fromEmail': getXmlNodeText, 
        'fromName': getXmlNodeText, 
        'to': (KalturaObjectFactory.createArray, KalturaKeyValue), 
        'cc': (KalturaObjectFactory.createArray, KalturaKeyValue), 
        'bcc': (KalturaObjectFactory.createArray, KalturaKeyValue), 
        'replyTo': (KalturaObjectFactory.createArray, KalturaKeyValue), 
        'priority': (KalturaEnumsFactory.createInt, "KalturaEmailNotificationTemplatePriority"), 
        'confirmReadingTo': getXmlNodeText, 
        'hostname': getXmlNodeText, 
        'messageID': getXmlNodeText, 
        'customHeaders': (KalturaObjectFactory.createArray, KalturaKeyValue), 
        'contentParameters': (KalturaObjectFactory.createArray, KalturaKeyValue), 
    }

    def fromXml(self, node):
        KalturaEventNotificationDispatchJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEmailNotificationDispatchJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationDispatchJobData.toParams(self)
        kparams.put("objectType", "KalturaEmailNotificationDispatchJobData")
        kparams.addStringIfDefined("fromEmail", self.fromEmail)
        kparams.addStringIfDefined("fromName", self.fromName)
        kparams.addArrayIfDefined("to", self.to)
        kparams.addArrayIfDefined("cc", self.cc)
        kparams.addArrayIfDefined("bcc", self.bcc)
        kparams.addArrayIfDefined("replyTo", self.replyTo)
        kparams.addIntEnumIfDefined("priority", self.priority)
        kparams.addStringIfDefined("confirmReadingTo", self.confirmReadingTo)
        kparams.addStringIfDefined("hostname", self.hostname)
        kparams.addStringIfDefined("messageID", self.messageID)
        kparams.addArrayIfDefined("customHeaders", self.customHeaders)
        kparams.addArrayIfDefined("contentParameters", self.contentParameters)
        return kparams

    def getFromEmail(self):
        return self.fromEmail

    def setFromEmail(self, newFromEmail):
        self.fromEmail = newFromEmail

    def getFromName(self):
        return self.fromName

    def setFromName(self, newFromName):
        self.fromName = newFromName

    def getTo(self):
        return self.to

    def setTo(self, newTo):
        self.to = newTo

    def getCc(self):
        return self.cc

    def setCc(self, newCc):
        self.cc = newCc

    def getBcc(self):
        return self.bcc

    def setBcc(self, newBcc):
        self.bcc = newBcc

    def getReplyTo(self):
        return self.replyTo

    def setReplyTo(self, newReplyTo):
        self.replyTo = newReplyTo

    def getPriority(self):
        return self.priority

    def setPriority(self, newPriority):
        self.priority = newPriority

    def getConfirmReadingTo(self):
        return self.confirmReadingTo

    def setConfirmReadingTo(self, newConfirmReadingTo):
        self.confirmReadingTo = newConfirmReadingTo

    def getHostname(self):
        return self.hostname

    def setHostname(self, newHostname):
        self.hostname = newHostname

    def getMessageID(self):
        return self.messageID

    def setMessageID(self, newMessageID):
        self.messageID = newMessageID

    def getCustomHeaders(self):
        return self.customHeaders

    def setCustomHeaders(self, newCustomHeaders):
        self.customHeaders = newCustomHeaders

    def getContentParameters(self):
        return self.contentParameters

    def setContentParameters(self, newContentParameters):
        self.contentParameters = newContentParameters


# @package External
# @subpackage Kaltura
class KalturaEmailNotificationTemplateBaseFilter(KalturaEventNotificationTemplateFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaEventNotificationTemplateFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaEventNotificationTemplateFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEmailNotificationTemplateBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationTemplateFilter.toParams(self)
        kparams.put("objectType", "KalturaEmailNotificationTemplateBaseFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaEmailNotificationTemplateFilter(KalturaEmailNotificationTemplateBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            typeEqual=NotImplemented,
            typeIn=NotImplemented,
            statusEqual=NotImplemented,
            statusIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented):
        KalturaEmailNotificationTemplateBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            partnerIdEqual,
            partnerIdIn,
            typeEqual,
            typeIn,
            statusEqual,
            statusIn,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaEmailNotificationTemplateBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEmailNotificationTemplateFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEmailNotificationTemplateBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaEmailNotificationTemplateFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaEmailNotificationClientPlugin(KalturaClientPlugin):
    # KalturaEmailNotificationClientPlugin
    instance = None

    # @return KalturaEmailNotificationClientPlugin
    @staticmethod
    def get():
        if KalturaEmailNotificationClientPlugin.instance == None:
            KalturaEmailNotificationClientPlugin.instance = KalturaEmailNotificationClientPlugin()
        return KalturaEmailNotificationClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaEmailNotificationTemplatePriority': KalturaEmailNotificationTemplatePriority,
            'KalturaEmailNotificationTemplateOrderBy': KalturaEmailNotificationTemplateOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaEmailNotificationDispatchJobData': KalturaEmailNotificationDispatchJobData,
            'KalturaEmailNotificationTemplateBaseFilter': KalturaEmailNotificationTemplateBaseFilter,
            'KalturaEmailNotificationTemplateFilter': KalturaEmailNotificationTemplateFilter,
        }

    # @return string
    def getName(self):
        return 'emailNotification'

