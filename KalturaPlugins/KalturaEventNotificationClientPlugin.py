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
from KalturaClientBase import *

########## enums ##########
# @package External
# @subpackage Kaltura
class KalturaEventNotificationTemplateStatus:
    DISABLED = 1
    ACTIVE = 2
    DELETED = 3

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaEventNotificationTemplateOrderBy:
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

# @package External
# @subpackage Kaltura
class KalturaEventNotificationTemplateType:
    EMAIL = "emailNotification.Email"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package External
# @subpackage Kaltura
class KalturaEventNotificationDispatchJobData(KalturaJobData):
    def __init__(self,
            templateId=NotImplemented):
        KalturaJobData.__init__(self)

        # @var int
        self.templateId = templateId


    PROPERTY_LOADERS = {
        'templateId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaJobData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEventNotificationDispatchJobData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaJobData.toParams(self)
        kparams.put("objectType", "KalturaEventNotificationDispatchJobData")
        kparams.addIntIfDefined("templateId", self.templateId)
        return kparams

    def getTemplateId(self):
        return self.templateId

    def setTemplateId(self, newTemplateId):
        self.templateId = newTemplateId


# @package External
# @subpackage Kaltura
class KalturaEventNotificationTemplateBaseFilter(KalturaFilter):
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
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var int
        self.idEqual = idEqual

        # @var string
        self.idIn = idIn

        # @var int
        self.partnerIdEqual = partnerIdEqual

        # @var string
        self.partnerIdIn = partnerIdIn

        # @var KalturaEventNotificationTemplateType
        self.typeEqual = typeEqual

        # @var string
        self.typeIn = typeIn

        # @var KalturaEventNotificationTemplateStatus
        self.statusEqual = statusEqual

        # @var string
        self.statusIn = statusIn

        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual

        # @var int
        self.updatedAtGreaterThanOrEqual = updatedAtGreaterThanOrEqual

        # @var int
        self.updatedAtLessThanOrEqual = updatedAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'idIn': getXmlNodeText, 
        'partnerIdEqual': getXmlNodeInt, 
        'partnerIdIn': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createString, "KalturaEventNotificationTemplateType"), 
        'typeIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createInt, "KalturaEventNotificationTemplateStatus"), 
        'statusIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
        'updatedAtGreaterThanOrEqual': getXmlNodeInt, 
        'updatedAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEventNotificationTemplateBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaEventNotificationTemplateBaseFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("partnerIdEqual", self.partnerIdEqual)
        kparams.addStringIfDefined("partnerIdIn", self.partnerIdIn)
        kparams.addStringEnumIfDefined("typeEqual", self.typeEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        kparams.addIntIfDefined("updatedAtGreaterThanOrEqual", self.updatedAtGreaterThanOrEqual)
        kparams.addIntIfDefined("updatedAtLessThanOrEqual", self.updatedAtLessThanOrEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getPartnerIdEqual(self):
        return self.partnerIdEqual

    def setPartnerIdEqual(self, newPartnerIdEqual):
        self.partnerIdEqual = newPartnerIdEqual

    def getPartnerIdIn(self):
        return self.partnerIdIn

    def setPartnerIdIn(self, newPartnerIdIn):
        self.partnerIdIn = newPartnerIdIn

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual

    def getUpdatedAtGreaterThanOrEqual(self):
        return self.updatedAtGreaterThanOrEqual

    def setUpdatedAtGreaterThanOrEqual(self, newUpdatedAtGreaterThanOrEqual):
        self.updatedAtGreaterThanOrEqual = newUpdatedAtGreaterThanOrEqual

    def getUpdatedAtLessThanOrEqual(self):
        return self.updatedAtLessThanOrEqual

    def setUpdatedAtLessThanOrEqual(self, newUpdatedAtLessThanOrEqual):
        self.updatedAtLessThanOrEqual = newUpdatedAtLessThanOrEqual


# @package External
# @subpackage Kaltura
class KalturaEventNotificationTemplateFilter(KalturaEventNotificationTemplateBaseFilter):
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
        KalturaEventNotificationTemplateBaseFilter.__init__(self,
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
        KalturaEventNotificationTemplateBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEventNotificationTemplateFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEventNotificationTemplateBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaEventNotificationTemplateFilter")
        return kparams


########## services ##########
########## main ##########
class KalturaEventNotificationClientPlugin(KalturaClientPlugin):
    # KalturaEventNotificationClientPlugin
    instance = None

    # @return KalturaEventNotificationClientPlugin
    @staticmethod
    def get():
        if KalturaEventNotificationClientPlugin.instance == None:
            KalturaEventNotificationClientPlugin.instance = KalturaEventNotificationClientPlugin()
        return KalturaEventNotificationClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaEventNotificationTemplateStatus': KalturaEventNotificationTemplateStatus,
            'KalturaEventNotificationTemplateOrderBy': KalturaEventNotificationTemplateOrderBy,
            'KalturaEventNotificationTemplateType': KalturaEventNotificationTemplateType,
        }

    def getTypes(self):
        return {
            'KalturaEventNotificationDispatchJobData': KalturaEventNotificationDispatchJobData,
            'KalturaEventNotificationTemplateBaseFilter': KalturaEventNotificationTemplateBaseFilter,
            'KalturaEventNotificationTemplateFilter': KalturaEventNotificationTemplateFilter,
        }

    # @return string
    def getName(self):
        return 'eventNotification'

