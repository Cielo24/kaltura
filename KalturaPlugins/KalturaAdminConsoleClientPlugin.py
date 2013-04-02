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
class KalturaTrackEntryEventType:
    UPLOADED_FILE = 1
    WEBCAM_COMPLETED = 2
    IMPORT_STARTED = 3
    ADD_ENTRY = 4
    UPDATE_ENTRY = 5
    DELETED_ENTRY = 6

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package External
# @subpackage Kaltura
class KalturaUiConfAdminOrderBy:
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
class KalturaTrackEntry(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            trackEventType=NotImplemented,
            psVersion=NotImplemented,
            context=NotImplemented,
            partnerId=NotImplemented,
            entryId=NotImplemented,
            hostName=NotImplemented,
            userId=NotImplemented,
            changedProperties=NotImplemented,
            paramStr1=NotImplemented,
            paramStr2=NotImplemented,
            paramStr3=NotImplemented,
            ks=NotImplemented,
            description=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            userIp=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        self.id = id

        # @var KalturaTrackEntryEventType
        self.trackEventType = trackEventType

        # @var string
        self.psVersion = psVersion

        # @var string
        self.context = context

        # @var int
        self.partnerId = partnerId

        # @var string
        self.entryId = entryId

        # @var string
        self.hostName = hostName

        # @var string
        self.userId = userId

        # @var string
        self.changedProperties = changedProperties

        # @var string
        self.paramStr1 = paramStr1

        # @var string
        self.paramStr2 = paramStr2

        # @var string
        self.paramStr3 = paramStr3

        # @var string
        self.ks = ks

        # @var string
        self.description = description

        # @var int
        self.createdAt = createdAt

        # @var int
        self.updatedAt = updatedAt

        # @var string
        self.userIp = userIp


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'trackEventType': (KalturaEnumsFactory.createInt, "KalturaTrackEntryEventType"), 
        'psVersion': getXmlNodeText, 
        'context': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'entryId': getXmlNodeText, 
        'hostName': getXmlNodeText, 
        'userId': getXmlNodeText, 
        'changedProperties': getXmlNodeText, 
        'paramStr1': getXmlNodeText, 
        'paramStr2': getXmlNodeText, 
        'paramStr3': getXmlNodeText, 
        'ks': getXmlNodeText, 
        'description': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'updatedAt': getXmlNodeInt, 
        'userIp': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTrackEntry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTrackEntry")
        kparams.addIntIfDefined("id", self.id)
        kparams.addIntEnumIfDefined("trackEventType", self.trackEventType)
        kparams.addStringIfDefined("psVersion", self.psVersion)
        kparams.addStringIfDefined("context", self.context)
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addStringIfDefined("hostName", self.hostName)
        kparams.addStringIfDefined("userId", self.userId)
        kparams.addStringIfDefined("changedProperties", self.changedProperties)
        kparams.addStringIfDefined("paramStr1", self.paramStr1)
        kparams.addStringIfDefined("paramStr2", self.paramStr2)
        kparams.addStringIfDefined("paramStr3", self.paramStr3)
        kparams.addStringIfDefined("ks", self.ks)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntIfDefined("createdAt", self.createdAt)
        kparams.addIntIfDefined("updatedAt", self.updatedAt)
        kparams.addStringIfDefined("userIp", self.userIp)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getTrackEventType(self):
        return self.trackEventType

    def setTrackEventType(self, newTrackEventType):
        self.trackEventType = newTrackEventType

    def getPsVersion(self):
        return self.psVersion

    def setPsVersion(self, newPsVersion):
        self.psVersion = newPsVersion

    def getContext(self):
        return self.context

    def setContext(self, newContext):
        self.context = newContext

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getHostName(self):
        return self.hostName

    def setHostName(self, newHostName):
        self.hostName = newHostName

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getChangedProperties(self):
        return self.changedProperties

    def setChangedProperties(self, newChangedProperties):
        self.changedProperties = newChangedProperties

    def getParamStr1(self):
        return self.paramStr1

    def setParamStr1(self, newParamStr1):
        self.paramStr1 = newParamStr1

    def getParamStr2(self):
        return self.paramStr2

    def setParamStr2(self, newParamStr2):
        self.paramStr2 = newParamStr2

    def getParamStr3(self):
        return self.paramStr3

    def setParamStr3(self, newParamStr3):
        self.paramStr3 = newParamStr3

    def getKs(self):
        return self.ks

    def setKs(self, newKs):
        self.ks = newKs

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getCreatedAt(self):
        return self.createdAt

    def setCreatedAt(self, newCreatedAt):
        self.createdAt = newCreatedAt

    def getUpdatedAt(self):
        return self.updatedAt

    def setUpdatedAt(self, newUpdatedAt):
        self.updatedAt = newUpdatedAt

    def getUserIp(self):
        return self.userIp

    def setUserIp(self, newUserIp):
        self.userIp = newUserIp


# @package External
# @subpackage Kaltura
class KalturaTrackEntryListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaTrackEntry
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaTrackEntry), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTrackEntryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTrackEntryListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


# @package External
# @subpackage Kaltura
class KalturaUiConfAdmin(KalturaUiConf):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            partnerId=NotImplemented,
            objType=NotImplemented,
            objTypeAsString=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            htmlParams=NotImplemented,
            swfUrl=NotImplemented,
            confFilePath=NotImplemented,
            confFile=NotImplemented,
            confFileFeatures=NotImplemented,
            confVars=NotImplemented,
            useCdn=NotImplemented,
            tags=NotImplemented,
            swfUrlVersion=NotImplemented,
            createdAt=NotImplemented,
            updatedAt=NotImplemented,
            creationMode=NotImplemented,
            html5Url=NotImplemented,
            isPublic=NotImplemented):
        KalturaUiConf.__init__(self,
            id,
            name,
            description,
            partnerId,
            objType,
            objTypeAsString,
            width,
            height,
            htmlParams,
            swfUrl,
            confFilePath,
            confFile,
            confFileFeatures,
            confVars,
            useCdn,
            tags,
            swfUrlVersion,
            createdAt,
            updatedAt,
            creationMode,
            html5Url)

        # @var bool
        self.isPublic = isPublic


    PROPERTY_LOADERS = {
        'isPublic': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaUiConf.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfAdmin.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUiConf.toParams(self)
        kparams.put("objectType", "KalturaUiConfAdmin")
        kparams.addBoolIfDefined("isPublic", self.isPublic)
        return kparams

    def getIsPublic(self):
        return self.isPublic

    def setIsPublic(self, newIsPublic):
        self.isPublic = newIsPublic


# @package External
# @subpackage Kaltura
class KalturaUiConfAdminListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaUiConfAdmin
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaUiConfAdmin), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfAdminListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUiConfAdminListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


# @package External
# @subpackage Kaltura
class KalturaUiConfAdminBaseFilter(KalturaUiConfFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            nameLike=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            objTypeEqual=NotImplemented,
            objTypeIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            creationModeEqual=NotImplemented,
            creationModeIn=NotImplemented):
        KalturaUiConfFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            nameLike,
            partnerIdEqual,
            partnerIdIn,
            objTypeEqual,
            objTypeIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            creationModeEqual,
            creationModeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUiConfFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfAdminBaseFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUiConfFilter.toParams(self)
        kparams.put("objectType", "KalturaUiConfAdminBaseFilter")
        return kparams


# @package External
# @subpackage Kaltura
class KalturaUiConfAdminFilter(KalturaUiConfAdminBaseFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            idEqual=NotImplemented,
            idIn=NotImplemented,
            nameLike=NotImplemented,
            partnerIdEqual=NotImplemented,
            partnerIdIn=NotImplemented,
            objTypeEqual=NotImplemented,
            objTypeIn=NotImplemented,
            tagsMultiLikeOr=NotImplemented,
            tagsMultiLikeAnd=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented,
            updatedAtGreaterThanOrEqual=NotImplemented,
            updatedAtLessThanOrEqual=NotImplemented,
            creationModeEqual=NotImplemented,
            creationModeIn=NotImplemented):
        KalturaUiConfAdminBaseFilter.__init__(self,
            orderBy,
            advancedSearch,
            idEqual,
            idIn,
            nameLike,
            partnerIdEqual,
            partnerIdIn,
            objTypeEqual,
            objTypeIn,
            tagsMultiLikeOr,
            tagsMultiLikeAnd,
            createdAtGreaterThanOrEqual,
            createdAtLessThanOrEqual,
            updatedAtGreaterThanOrEqual,
            updatedAtLessThanOrEqual,
            creationModeEqual,
            creationModeIn)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaUiConfAdminBaseFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUiConfAdminFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUiConfAdminBaseFilter.toParams(self)
        kparams.put("objectType", "KalturaUiConfAdminFilter")
        return kparams


########## services ##########

# @package External
# @subpackage Kaltura
class KalturaEntryAdminService(KalturaServiceBase):
    """Entry Admin service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def get(self, entryId, version = -1):
        """Get base entry by ID with no filters."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("adminconsole_entryadmin", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def getByFlavorId(self, flavorId, version = -1):
        """Get base entry by flavor ID with no filters."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("flavorId", flavorId)
        kparams.addIntIfDefined("version", version);
        self.client.queueServiceActionCall("adminconsole_entryadmin", "getByFlavorId", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaBaseEntry)

    def getTracks(self, entryId):
        """Get base entry by ID with no filters."""

        kparams = KalturaParams()
        kparams.addStringIfDefined("entryId", entryId)
        self.client.queueServiceActionCall("adminconsole_entryadmin", "getTracks", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaTrackEntryListResponse)


# @package External
# @subpackage Kaltura
class KalturaUiConfAdminService(KalturaServiceBase):
    """UiConf Admin service"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, uiConf):
        """Adds new UIConf with no partner limitation"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("uiConf", uiConf)
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfAdmin)

    def update(self, id, uiConf):
        """Update an existing UIConf with no partner limitation"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("uiConf", uiConf)
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfAdmin)

    def get(self, id):
        """Retrieve a UIConf by id with no partner limitation"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfAdmin)

    def delete(self, id):
        """Delete an existing UIConf with no partner limitation"""

        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def list(self, filter = NotImplemented, pager = NotImplemented):
        """Retrieve a list of available UIConfs  with no partner limitation"""

        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("adminconsole_uiconfadmin", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaUiConfAdminListResponse)


# @package External
# @subpackage Kaltura
class KalturaReportAdminService(KalturaServiceBase):
    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def add(self, report):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("report", report)
        self.client.queueServiceActionCall("adminconsole_reportadmin", "add", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReport)

    def get(self, id):
        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("adminconsole_reportadmin", "get", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReport)

    def list(self, filter = NotImplemented, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("filter", filter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("adminconsole_reportadmin", "list", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReportListResponse)

    def update(self, id, report):
        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addObjectIfDefined("report", report)
        self.client.queueServiceActionCall("adminconsole_reportadmin", "update", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReport)

    def delete(self, id):
        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("adminconsole_reportadmin", "delete", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()

    def executeDebug(self, id, params = NotImplemented):
        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addArrayIfDefined("params", params)
        self.client.queueServiceActionCall("adminconsole_reportadmin", "executeDebug", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaReportResponse)

    def getParameters(self, id):
        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        self.client.queueServiceActionCall("adminconsole_reportadmin", "getParameters", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.createArray(resultNode, KalturaString)

    def getCsvUrl(self, id, reportPartnerId):
        kparams = KalturaParams()
        kparams.addIntIfDefined("id", id);
        kparams.addIntIfDefined("reportPartnerId", reportPartnerId);
        self.client.queueServiceActionCall("adminconsole_reportadmin", "getCsvUrl", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return getXmlNodeText(resultNode)

########## main ##########
class KalturaAdminConsoleClientPlugin(KalturaClientPlugin):
    # KalturaAdminConsoleClientPlugin
    instance = None

    # @return KalturaAdminConsoleClientPlugin
    @staticmethod
    def get():
        if KalturaAdminConsoleClientPlugin.instance == None:
            KalturaAdminConsoleClientPlugin.instance = KalturaAdminConsoleClientPlugin()
        return KalturaAdminConsoleClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'entryAdmin': KalturaEntryAdminService,
            'uiConfAdmin': KalturaUiConfAdminService,
            'reportAdmin': KalturaReportAdminService,
        }

    def getEnums(self):
        return {
            'KalturaTrackEntryEventType': KalturaTrackEntryEventType,
            'KalturaUiConfAdminOrderBy': KalturaUiConfAdminOrderBy,
        }

    def getTypes(self):
        return {
            'KalturaTrackEntry': KalturaTrackEntry,
            'KalturaTrackEntryListResponse': KalturaTrackEntryListResponse,
            'KalturaUiConfAdmin': KalturaUiConfAdmin,
            'KalturaUiConfAdminListResponse': KalturaUiConfAdminListResponse,
            'KalturaUiConfAdminBaseFilter': KalturaUiConfAdminBaseFilter,
            'KalturaUiConfAdminFilter': KalturaUiConfAdminFilter,
        }

    # @return string
    def getName(self):
        return 'adminConsole'

