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
########## classes ##########
# @package External
# @subpackage Kaltura
class KalturaTag(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            tag=NotImplemented,
            taggedObjectType=NotImplemented,
            partnerId=NotImplemented,
            instanceCount=NotImplemented,
            createdAt=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var int
        # @readonly
        self.id = id

        # @var string
        # @readonly
        self.tag = tag

        # @var KalturaTaggedObjectType
        # @readonly
        self.taggedObjectType = taggedObjectType

        # @var int
        # @readonly
        self.partnerId = partnerId

        # @var int
        # @readonly
        self.instanceCount = instanceCount

        # @var int
        # @readonly
        self.createdAt = createdAt


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'tag': getXmlNodeText, 
        'taggedObjectType': (KalturaEnumsFactory.createString, "KalturaTaggedObjectType"), 
        'partnerId': getXmlNodeInt, 
        'instanceCount': getXmlNodeInt, 
        'createdAt': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTag.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTag")
        return kparams

    def getId(self):
        return self.id

    def getTag(self):
        return self.tag

    def getTaggedObjectType(self):
        return self.taggedObjectType

    def getPartnerId(self):
        return self.partnerId

    def getInstanceCount(self):
        return self.instanceCount

    def getCreatedAt(self):
        return self.createdAt


# @package External
# @subpackage Kaltura
class KalturaTagListResponse(KalturaObjectBase):
    def __init__(self,
            objects=NotImplemented,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # @var array of KalturaTag
        # @readonly
        self.objects = objects

        # @var int
        # @readonly
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, KalturaTag), 
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTagListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTagListResponse")
        return kparams

    def getObjects(self):
        return self.objects

    def getTotalCount(self):
        return self.totalCount


# @package External
# @subpackage Kaltura
class KalturaTagFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            advancedSearch=NotImplemented,
            objectTypeEqual=NotImplemented,
            tagEqual=NotImplemented,
            tagStartsWith=NotImplemented,
            instanceCountEqual=NotImplemented,
            instanceCountIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy,
            advancedSearch)

        # @var KalturaTaggedObjectType
        self.objectTypeEqual = objectTypeEqual

        # @var string
        self.tagEqual = tagEqual

        # @var string
        self.tagStartsWith = tagStartsWith

        # @var int
        self.instanceCountEqual = instanceCountEqual

        # @var int
        self.instanceCountIn = instanceCountIn


    PROPERTY_LOADERS = {
        'objectTypeEqual': (KalturaEnumsFactory.createString, "KalturaTaggedObjectType"), 
        'tagEqual': getXmlNodeText, 
        'tagStartsWith': getXmlNodeText, 
        'instanceCountEqual': getXmlNodeInt, 
        'instanceCountIn': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTagFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaTagFilter")
        kparams.addStringEnumIfDefined("objectTypeEqual", self.objectTypeEqual)
        kparams.addStringIfDefined("tagEqual", self.tagEqual)
        kparams.addStringIfDefined("tagStartsWith", self.tagStartsWith)
        kparams.addIntIfDefined("instanceCountEqual", self.instanceCountEqual)
        kparams.addIntIfDefined("instanceCountIn", self.instanceCountIn)
        return kparams

    def getObjectTypeEqual(self):
        return self.objectTypeEqual

    def setObjectTypeEqual(self, newObjectTypeEqual):
        self.objectTypeEqual = newObjectTypeEqual

    def getTagEqual(self):
        return self.tagEqual

    def setTagEqual(self, newTagEqual):
        self.tagEqual = newTagEqual

    def getTagStartsWith(self):
        return self.tagStartsWith

    def setTagStartsWith(self, newTagStartsWith):
        self.tagStartsWith = newTagStartsWith

    def getInstanceCountEqual(self):
        return self.instanceCountEqual

    def setInstanceCountEqual(self, newInstanceCountEqual):
        self.instanceCountEqual = newInstanceCountEqual

    def getInstanceCountIn(self):
        return self.instanceCountIn

    def setInstanceCountIn(self, newInstanceCountIn):
        self.instanceCountIn = newInstanceCountIn


########## services ##########

# @package External
# @subpackage Kaltura
class KalturaTagService(KalturaServiceBase):
    """Search object tags"""

    def __init__(self, client = None):
        KalturaServiceBase.__init__(self, client)

    def search(self, tagFilter, pager = NotImplemented):
        kparams = KalturaParams()
        kparams.addObjectIfDefined("tagFilter", tagFilter)
        kparams.addObjectIfDefined("pager", pager)
        self.client.queueServiceActionCall("tagsearch_tag", "search", kparams)
        if self.client.isMultiRequest():
            return self.client.getMultiRequestResult()
        resultNode = self.client.doQueue()
        return KalturaObjectFactory.create(resultNode, KalturaTagListResponse)

########## main ##########
class KalturaTagSearchClientPlugin(KalturaClientPlugin):
    # KalturaTagSearchClientPlugin
    instance = None

    # @return KalturaTagSearchClientPlugin
    @staticmethod
    def get():
        if KalturaTagSearchClientPlugin.instance == None:
            KalturaTagSearchClientPlugin.instance = KalturaTagSearchClientPlugin()
        return KalturaTagSearchClientPlugin.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
            'tag': KalturaTagService,
        }

    def getEnums(self):
        return {
        }

    def getTypes(self):
        return {
            'KalturaTag': KalturaTag,
            'KalturaTagListResponse': KalturaTagListResponse,
            'KalturaTagFilter': KalturaTagFilter,
        }

    # @return string
    def getName(self):
        return 'tagSearch'

