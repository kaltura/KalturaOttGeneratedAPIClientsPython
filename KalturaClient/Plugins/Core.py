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
# Copyright (C) 2006-2018  Kaltura Inc.
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
# @package Kaltura
# @subpackage Client
from __future__ import absolute_import

from ..Base import (
    getXmlNodeBool,
    getXmlNodeFloat,
    getXmlNodeInt,
    getXmlNodeText,
    KalturaClientPlugin,
    KalturaEnumsFactory,
    KalturaObjectBase,
    KalturaObjectFactory,
    KalturaParams,
    KalturaServiceBase,
)

API_VERSION = '5.1.18.41996'

########## enums ##########
# @package Kaltura
# @subpackage Client
class KalturaAggregationCountOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAnnouncementOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAnnouncementRecipientsType(object):
    ALL = "All"
    LOGGEDIN = "LoggedIn"
    GUESTS = "Guests"
    OTHER = "Other"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAnnouncementStatus(object):
    NOTSENT = "NotSent"
    SENDING = "Sending"
    SENT = "Sent"
    ABORTED = "Aborted"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetCommentOrderBy(object):
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetHistoryOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetOrderBy(object):
    RELEVANCY_DESC = "RELEVANCY_DESC"
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    VIEWS_DESC = "VIEWS_DESC"
    RATINGS_DESC = "RATINGS_DESC"
    VOTES_DESC = "VOTES_DESC"
    START_DATE_DESC = "START_DATE_DESC"
    START_DATE_ASC = "START_DATE_ASC"
    LIKES_DESC = "LIKES_DESC"
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetReminderOrderBy(object):
    RELEVANCY_DESC = "RELEVANCY_DESC"
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    VIEWS_DESC = "VIEWS_DESC"
    RATINGS_DESC = "RATINGS_DESC"
    VOTES_DESC = "VOTES_DESC"
    START_DATE_DESC = "START_DATE_DESC"
    START_DATE_ASC = "START_DATE_ASC"
    LIKES_DESC = "LIKES_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetRuleOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetStructMetaOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetStructOrderBy(object):
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    SYSTEM_NAME_ASC = "SYSTEM_NAME_ASC"
    SYSTEM_NAME_DESC = "SYSTEM_NAME_DESC"
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"
    UPDATE_DATE_ASC = "UPDATE_DATE_ASC"
    UPDATE_DATE_DESC = "UPDATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetType(object):
    MEDIA = "media"
    RECORDING = "recording"
    EPG = "epg"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaAssetUserRuleOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBatchJobStatus(object):
    PENDING = "PENDING"
    QUEUED = "QUEUED"
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    MOVEFILE = "MOVEFILE"
    FINISHED = "FINISHED"
    FAILED = "FAILED"
    ABORTED = "ABORTED"
    ALMOST_DONE = "ALMOST_DONE"
    RETRY = "RETRY"
    FATAL = "FATAL"
    DONT_PROCESS = "DONT_PROCESS"
    FINISHED_PARTIALLY = "FINISHED_PARTIALLY"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBillingAction(object):
    UNKNOWN = "unknown"
    PURCHASE = "purchase"
    RENEW_PAYMENT = "renew_payment"
    RENEW_CANCELED_SUBSCRIPTION = "renew_canceled_subscription"
    CANCEL_SUBSCRIPTION_ORDER = "cancel_subscription_order"
    SUBSCRIPTION_DATE_CHANGED = "subscription_date_changed"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBillingItemsType(object):
    UNKNOWN = "unknown"
    PPV = "ppv"
    SUBSCRIPTION = "subscription"
    PRE_PAID = "pre_paid"
    PRE_PAID_EXPIRED = "pre_paid_expired"
    COLLECTION = "collection"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBillingPriceType(object):
    FULLPERIOD = "FullPeriod"
    PARTIALPERIOD = "PartialPeriod"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBookmarkActionType(object):
    HIT = "HIT"
    PLAY = "PLAY"
    STOP = "STOP"
    PAUSE = "PAUSE"
    FIRST_PLAY = "FIRST_PLAY"
    SWOOSH = "SWOOSH"
    FULL_SCREEN = "FULL_SCREEN"
    SEND_TO_FRIEND = "SEND_TO_FRIEND"
    LOAD = "LOAD"
    FULL_SCREEN_EXIT = "FULL_SCREEN_EXIT"
    FINISH = "FINISH"
    ERROR = "ERROR"
    BITRATE_CHANGE = "BITRATE_CHANGE"
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBookmarkOrderBy(object):
    POSITION_ASC = "POSITION_ASC"
    POSITION_DESC = "POSITION_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBulkOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaBundleType(object):
    SUBSCRIPTION = "subscription"
    COLLECTION = "collection"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaChannelEnrichment(object):
    CLIENTLOCATION = "ClientLocation"
    USERID = "UserId"
    HOUSEHOLDID = "HouseholdId"
    DEVICEID = "DeviceId"
    DEVICETYPE = "DeviceType"
    UTCOFFSET = "UTCOffset"
    LANGUAGE = "Language"
    NPVRSUPPORT = "NPVRSupport"
    CATCHUP = "Catchup"
    PARENTAL = "Parental"
    DTTREGION = "DTTRegion"
    ATHOME = "AtHome"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaChannelOrderBy(object):
    ORDER_NUM = "ORDER_NUM"
    RELEVANCY_DESC = "RELEVANCY_DESC"
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    VIEWS_DESC = "VIEWS_DESC"
    RATINGS_DESC = "RATINGS_DESC"
    VOTES_DESC = "VOTES_DESC"
    START_DATE_DESC = "START_DATE_DESC"
    START_DATE_ASC = "START_DATE_ASC"
    LIKES_DESC = "LIKES_DESC"
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaChannelsOrderBy(object):
    NONE = "NONE"
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCollectionOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaConcurrencyLimitationType(object):
    SINGLE = "Single"
    GROUP = "Group"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupDeviceOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupTagOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaConfigurationsOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCountryOrderBy(object):
    NAME_ASC = "NAME_ASC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCouponGroupType(object):
    COUPON = "COUPON"
    GIFT_CARD = "GIFT_CARD"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaCurrencyOrderBy(object):
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    CODE_ASC = "CODE_ASC"
    CODE_DESC = "CODE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaDeviceStatus(object):
    PENDING = "PENDING"
    ACTIVATED = "ACTIVATED"
    NOT_ACTIVATED = "NOT_ACTIVATED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaDrmSchemeName(object):
    PLAYREADY_CENC = "PLAYREADY_CENC"
    WIDEVINE_CENC = "WIDEVINE_CENC"
    FAIRPLAY = "FAIRPLAY"
    WIDEVINE = "WIDEVINE"
    PLAYREADY = "PLAYREADY"
    CUSTOM_DRM = "CUSTOM_DRM"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEngagementOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEngagementType(object):
    CHURN = "Churn"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEntitlementOrderBy(object):
    PURCHASE_DATE_ASC = "PURCHASE_DATE_ASC"
    PURCHASE_DATE_DESC = "PURCHASE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEntityReferenceBy(object):
    USER = "user"
    HOUSEHOLD = "household"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaEvictionPolicyType(object):
    FIFO = "FIFO"
    LIFO = "LIFO"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaExportDataType(object):
    VOD = "vod"
    EPG = "epg"
    USERS = "users"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaExportTaskOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaExportType(object):
    FULL = "full"
    INCREMENTAL = "incremental"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaFavoriteOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeriesOrderBy(object):
    START_DATE_DESC = "START_DATE_DESC"
    START_DATE_ASC = "START_DATE_ASC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaGroupByField(object):
    MEDIA_TYPE_ID = "media_type_id"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdDeviceOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentGatewaySelectedBy(object):
    NONE = "none"
    ACCOUNT = "account"
    HOUSEHOLD = "household"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdSuspensionState(object):
    NOT_SUSPENDED = "NOT_SUSPENDED"
    SUSPENDED = "SUSPENDED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdUserOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaHouseholdUserStatus(object):
    OK = "OK"
    PENDING = "PENDING"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaImageObjectType(object):
    MEDIA_ASSET = "MEDIA_ASSET"
    PROGRAM_ASSET = "PROGRAM_ASSET"
    CHANNEL = "CHANNEL"
    CATEGORY = "CATEGORY"
    PARTNER = "PARTNER"
    IMAGE_TYPE = "IMAGE_TYPE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaImageOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaImageStatus(object):
    PENDING = "PENDING"
    READY = "READY"
    FAILED = "FAILED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaImageTypeOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaInboxMessageOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaInboxMessageStatus(object):
    UNREAD = "Unread"
    READ = "Read"
    DELETED = "Deleted"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaInboxMessageType(object):
    SYSTEMANNOUNCEMENT = "SystemAnnouncement"
    FOLLOWED = "Followed"
    ENGAGEMENT = "Engagement"
    INTEREST = "Interest"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaLanguageOrderBy(object):
    SYSTEM_NAME_ASC = "SYSTEM_NAME_ASC"
    SYSTEM_NAME_DESC = "SYSTEM_NAME_DESC"
    CODE_ASC = "CODE_ASC"
    CODE_DESC = "CODE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaLinearChannelType(object):
    UNKNOWN = "UNKNOWN"
    DTT = "DTT"
    OTT = "OTT"
    DTT_AND_OTT = "DTT_AND_OTT"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaMediaFileOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaMediaFileStreamerType(object):
    APPLE_HTTP = "APPLE_HTTP"
    MPEG_DASH = "MPEG_DASH"
    URL = "URL"
    SMOOTH_STREAMING = "SMOOTH_STREAMING"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaMediaFileTypeQuality(object):
    ADAPTIVE = "ADAPTIVE"
    SD = "SD"
    HD_720 = "HD_720"
    HD_1080 = "HD_1080"
    UHD_4K = "UHD_4K"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaMetaDataType(object):
    STRING = "STRING"
    MULTILINGUAL_STRING = "MULTILINGUAL_STRING"
    NUMBER = "NUMBER"
    BOOLEAN = "BOOLEAN"
    DATE = "DATE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaMetaOrderBy(object):
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    SYSTEM_NAME_ASC = "SYSTEM_NAME_ASC"
    SYSTEM_NAME_DESC = "SYSTEM_NAME_DESC"
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"
    UPDATE_DATE_ASC = "UPDATE_DATE_ASC"
    UPDATE_DATE_DESC = "UPDATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaMetaTagOrderBy(object):
    META_ASC = "META_ASC"
    META_DESC = "META_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaOTTUserOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaParentalRuleOrderBy(object):
    PARTNER_SORT_VALUE = "PARTNER_SORT_VALUE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaParentalRuleType(object):
    ALL = "ALL"
    MOVIES = "MOVIES"
    TV_SERIES = "TV_SERIES"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPartnerConfigurationOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPartnerConfigurationType(object):
    DEFAULTPAYMENTGATEWAY = "DefaultPaymentGateway"
    ENABLEPAYMENTGATEWAYSELECTION = "EnablePaymentGatewaySelection"
    OSSADAPTER = "OSSAdapter"
    CONCURRENCY = "Concurrency"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfileOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodType(object):
    UNKNOWN = "unknown"
    CREDIT_CARD = "credit_card"
    SMS = "sms"
    PAY_PAL = "pay_pal"
    DEBIT_CARD = "debit_card"
    IDEAL = "ideal"
    INCASO = "incaso"
    GIFT = "gift"
    VISA = "visa"
    MASTER_CARD = "master_card"
    IN_APP = "in_app"
    M1 = "m1"
    CHANGE_SUBSCRIPTION = "change_subscription"
    OFFLINE = "offline"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPersonalFeedOrderBy(object):
    RELEVANCY_DESC = "RELEVANCY_DESC"
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"
    VIEWS_DESC = "VIEWS_DESC"
    RATINGS_DESC = "RATINGS_DESC"
    VOTES_DESC = "VOTES_DESC"
    START_DATE_DESC = "START_DATE_DESC"
    START_DATE_ASC = "START_DATE_ASC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPersonalListOrderBy(object):
    CREATE_DATE_DESC = "CREATE_DATE_DESC"
    CREATE_DATE_ASC = "CREATE_DATE_ASC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPlatform(object):
    ANDROID = "Android"
    IOS = "iOS"
    WINDOWSPHONE = "WindowsPhone"
    BLACKBERRY = "Blackberry"
    STB = "STB"
    CTV = "CTV"
    OTHER = "Other"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPositionOwner(object):
    HOUSEHOLD = "household"
    USER = "user"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPriceDetailsOrderBy(object):
    NAME_ASC = "NAME_ASC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPricePlanOrderBy(object):
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaProductPriceOrderBy(object):
    PRODUCT_ID_ASC = "PRODUCT_ID_ASC"
    PRODUCT_ID_DESC = "PRODUCT_ID_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaPurchaseStatus(object):
    PPV_PURCHASED = "ppv_purchased"
    FREE = "free"
    FOR_PURCHASE_SUBSCRIPTION_ONLY = "for_purchase_subscription_only"
    SUBSCRIPTION_PURCHASED = "subscription_purchased"
    FOR_PURCHASE = "for_purchase"
    SUBSCRIPTION_PURCHASED_WRONG_CURRENCY = "subscription_purchased_wrong_currency"
    PRE_PAID_PURCHASED = "pre_paid_purchased"
    GEO_COMMERCE_BLOCKED = "geo_commerce_blocked"
    ENTITLED_TO_PREVIEW_MODULE = "entitled_to_preview_module"
    FIRST_DEVICE_LIMITATION = "first_device_limitation"
    COLLECTION_PURCHASED = "collection_purchased"
    USER_SUSPENDED = "user_suspended"
    NOT_FOR_PURCHASE = "not_for_purchase"
    INVALID_CURRENCY = "invalid_currency"
    CURRENCY_NOT_DEFINED_ON_PRICE_CODE = "currency_not_defined_on_price_code"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingContextOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingOrderBy(object):
    TITLE_ASC = "TITLE_ASC"
    TITLE_DESC = "TITLE_DESC"
    START_DATE_ASC = "START_DATE_ASC"
    START_DATE_DESC = "START_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingStatus(object):
    SCHEDULED = "SCHEDULED"
    RECORDING = "RECORDING"
    RECORDED = "RECORDED"
    CANCELED = "CANCELED"
    FAILED = "FAILED"
    DELETED = "DELETED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRecordingType(object):
    SINGLE = "SINGLE"
    SEASON = "SEASON"
    SERIES = "SERIES"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRegionOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaReminderType(object):
    ASSET = "ASSET"
    SERIES = "SERIES"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaReportOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRuleActionType(object):
    BLOCK = "BLOCK"
    START_DATE_OFFSET = "START_DATE_OFFSET"
    END_DATE_OFFSET = "END_DATE_OFFSET"
    USER_BLOCK = "USER_BLOCK"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRuleConditionType(object):
    ASSET = "ASSET"
    COUNTRY = "COUNTRY"
    CONCURRENCY = "CONCURRENCY"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRuleLevel(object):
    INVALID = "invalid"
    USER = "user"
    HOUSEHOLD = "household"
    ACCOUNT = "account"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaRuleType(object):
    PARENTAL = "parental"
    GEO = "geo"
    USER_TYPE = "user_type"
    DEVICE = "device"
    ASSETUSER = "assetUser"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaScheduledRecordingAssetType(object):
    SINGLE = "single"
    SERIES = "series"
    ALL = "all"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSearchHistoryOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSeriesRecordingOrderBy(object):
    START_DATE_ASC = "START_DATE_ASC"
    START_DATE_DESC = "START_DATE_DESC"
    ID_ASC = "ID_ASC"
    ID_DESC = "ID_DESC"
    SERIES_ID_ASC = "SERIES_ID_ASC"
    SERIES_ID_DESC = "SERIES_ID_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSeriesReminderOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSocialActionOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSocialActionType(object):
    LIKE = "LIKE"
    WATCH = "WATCH"
    RATE = "RATE"
    SHARE = "SHARE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSocialCommentOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSocialFriendActivityOrderBy(object):
    NONE = "NONE"
    UPDATE_DATE_DESC = "UPDATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSocialPlatform(object):
    IN_APP = "IN_APP"
    FACEBOOK = "FACEBOOK"
    TWITTER = "TWITTER"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSubscriptionDependencyType(object):
    NOTAPPLICABLE = "NOTAPPLICABLE"
    BASE = "BASE"
    ADDON = "ADDON"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSubscriptionOrderBy(object):
    START_DATE_ASC = "START_DATE_ASC"
    START_DATE_DESC = "START_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSubscriptionSetOrderBy(object):
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaSubscriptionSetType(object):
    SWITCH = "SWITCH"
    DEPENDENCY = "DEPENDENCY"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTagOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTimeShiftedTvState(object):
    INHERITED = "INHERITED"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTopicAutomaticIssueNotification(object):
    INHERIT = "Inherit"
    YES = "Yes"
    NO = "No"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTopicOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTransactionHistoryOrderBy(object):
    CREATE_DATE_ASC = "CREATE_DATE_ASC"
    CREATE_DATE_DESC = "CREATE_DATE_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaTransactionType(object):
    PPV = "ppv"
    SUBSCRIPTION = "subscription"
    COLLECTION = "collection"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUserAssetRuleOrderBy(object):
    NAME_ASC = "NAME_ASC"
    NAME_DESC = "NAME_DESC"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUserRoleOrderBy(object):
    NONE = "NONE"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaUserState(object):
    OK = "ok"
    USER_WITH_NO_HOUSEHOLD = "user_with_no_household"
    USER_CREATED_WITH_NO_ROLE = "user_created_with_no_role"
    USER_NOT_ACTIVATED = "user_not_activated"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

# @package Kaltura
# @subpackage Client
class KalturaWatchStatus(object):
    PROGRESS = "progress"
    DONE = "done"
    ALL = "all"

    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

########## classes ##########
# @package Kaltura
# @subpackage Client
class KalturaListResponse(KalturaObjectBase):
    """Base list wrapper"""

    def __init__(self,
            totalCount=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Total items
        # @var int
        self.totalCount = totalCount


    PROPERTY_LOADERS = {
        'totalCount': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaListResponse")
        kparams.addIntIfDefined("totalCount", self.totalCount)
        return kparams

    def getTotalCount(self):
        return self.totalCount

    def setTotalCount(self, newTotalCount):
        self.totalCount = newTotalCount


# @package Kaltura
# @subpackage Client
class KalturaApiExceptionArg(KalturaObjectBase):
    def __init__(self,
            name=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Argument name
        # @var string
        self.name = name

        # Argument value
        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaApiExceptionArg.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaApiExceptionArg")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaSocialComment(KalturaObjectBase):
    def __init__(self,
            header=NotImplemented,
            text=NotImplemented,
            createDate=NotImplemented,
            writer=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Comment header
        # @var string
        self.header = header

        # Comment body
        # @var string
        self.text = text

        # Comment creation date
        # @var int
        self.createDate = createDate

        # The writer of the comment
        # @var string
        self.writer = writer


    PROPERTY_LOADERS = {
        'header': getXmlNodeText, 
        'text': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
        'writer': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialComment.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSocialComment")
        kparams.addStringIfDefined("header", self.header)
        kparams.addStringIfDefined("text", self.text)
        kparams.addIntIfDefined("createDate", self.createDate)
        kparams.addStringIfDefined("writer", self.writer)
        return kparams

    def getHeader(self):
        return self.header

    def setHeader(self, newHeader):
        self.header = newHeader

    def getText(self):
        return self.text

    def setText(self, newText):
        self.text = newText

    def getCreateDate(self):
        return self.createDate

    def setCreateDate(self, newCreateDate):
        self.createDate = newCreateDate

    def getWriter(self):
        return self.writer

    def setWriter(self, newWriter):
        self.writer = newWriter


# @package Kaltura
# @subpackage Client
class KalturaSocialCommentListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Social comments list
        # @var array of KalturaSocialComment
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSocialComment'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialCommentListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSocialCommentListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSocialNetworkComment(KalturaSocialComment):
    def __init__(self,
            header=NotImplemented,
            text=NotImplemented,
            createDate=NotImplemented,
            writer=NotImplemented,
            likeCounter=NotImplemented,
            authorImageUrl=NotImplemented):
        KalturaSocialComment.__init__(self,
            header,
            text,
            createDate,
            writer)

        # Number of likes
        # @var string
        self.likeCounter = likeCounter

        # The URL of the profile picture of the author of the comment
        # @var string
        self.authorImageUrl = authorImageUrl


    PROPERTY_LOADERS = {
        'likeCounter': getXmlNodeText, 
        'authorImageUrl': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSocialComment.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialNetworkComment.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSocialComment.toParams(self)
        kparams.put("objectType", "KalturaSocialNetworkComment")
        kparams.addStringIfDefined("likeCounter", self.likeCounter)
        kparams.addStringIfDefined("authorImageUrl", self.authorImageUrl)
        return kparams

    def getLikeCounter(self):
        return self.likeCounter

    def setLikeCounter(self, newLikeCounter):
        self.likeCounter = newLikeCounter

    def getAuthorImageUrl(self):
        return self.authorImageUrl

    def setAuthorImageUrl(self, newAuthorImageUrl):
        self.authorImageUrl = newAuthorImageUrl


# @package Kaltura
# @subpackage Client
class KalturaTwitterTwit(KalturaSocialNetworkComment):
    def __init__(self,
            header=NotImplemented,
            text=NotImplemented,
            createDate=NotImplemented,
            writer=NotImplemented,
            likeCounter=NotImplemented,
            authorImageUrl=NotImplemented):
        KalturaSocialNetworkComment.__init__(self,
            header,
            text,
            createDate,
            writer,
            likeCounter,
            authorImageUrl)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSocialNetworkComment.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTwitterTwit.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSocialNetworkComment.toParams(self)
        kparams.put("objectType", "KalturaTwitterTwit")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaFacebookPost(KalturaSocialNetworkComment):
    def __init__(self,
            header=NotImplemented,
            text=NotImplemented,
            createDate=NotImplemented,
            writer=NotImplemented,
            likeCounter=NotImplemented,
            authorImageUrl=NotImplemented,
            comments=NotImplemented,
            link=NotImplemented):
        KalturaSocialNetworkComment.__init__(self,
            header,
            text,
            createDate,
            writer,
            likeCounter,
            authorImageUrl)

        # List of comments on the post
        # @var array of KalturaSocialNetworkComment
        self.comments = comments

        # A link associated to the post
        # @var string
        self.link = link


    PROPERTY_LOADERS = {
        'comments': (KalturaObjectFactory.createArray, 'KalturaSocialNetworkComment'), 
        'link': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSocialNetworkComment.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFacebookPost.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSocialNetworkComment.toParams(self)
        kparams.put("objectType", "KalturaFacebookPost")
        kparams.addArrayIfDefined("comments", self.comments)
        kparams.addStringIfDefined("link", self.link)
        return kparams

    def getComments(self):
        return self.comments

    def setComments(self, newComments):
        self.comments = newComments

    def getLink(self):
        return self.link

    def setLink(self, newLink):
        self.link = newLink


# @package Kaltura
# @subpackage Client
class KalturaAssetComment(KalturaSocialComment):
    """Asset Comment"""

    def __init__(self,
            header=NotImplemented,
            text=NotImplemented,
            createDate=NotImplemented,
            writer=NotImplemented,
            id=NotImplemented,
            assetId=NotImplemented,
            assetType=NotImplemented,
            subHeader=NotImplemented):
        KalturaSocialComment.__init__(self,
            header,
            text,
            createDate,
            writer)

        # Comment ID
        # @var int
        self.id = id

        # Asset identifier
        # @var int
        self.assetId = assetId

        # Asset Type
        # @var KalturaAssetType
        self.assetType = assetType

        # Sub Header
        # @var string
        self.subHeader = subHeader


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'assetId': getXmlNodeInt, 
        'assetType': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
        'subHeader': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSocialComment.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetComment.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSocialComment.toParams(self)
        kparams.put("objectType", "KalturaAssetComment")
        kparams.addIntIfDefined("id", self.id)
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addStringEnumIfDefined("assetType", self.assetType)
        kparams.addStringIfDefined("subHeader", self.subHeader)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getAssetType(self):
        return self.assetType

    def setAssetType(self, newAssetType):
        self.assetType = newAssetType

    def getSubHeader(self):
        return self.subHeader

    def setSubHeader(self, newSubHeader):
        self.subHeader = newSubHeader


# @package Kaltura
# @subpackage Client
class KalturaSocialAction(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            actionType=NotImplemented,
            time=NotImplemented,
            assetId=NotImplemented,
            assetType=NotImplemented,
            url=NotImplemented):
        KalturaObjectBase.__init__(self)

        # social action document id
        # @var string
        # @readonly
        self.id = id

        # Action type
        # @var KalturaSocialActionType
        self.actionType = actionType

        # EPOC based timestamp for when the action occurred
        # @var int
        self.time = time

        # ID of the asset that was acted upon
        # @var int
        self.assetId = assetId

        # Type of the asset that was acted upon, currently only VOD (media)
        # @var KalturaAssetType
        self.assetType = assetType

        # The value of the url
        # @var string
        self.url = url


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'actionType': (KalturaEnumsFactory.createString, "KalturaSocialActionType"), 
        'time': getXmlNodeInt, 
        'assetId': getXmlNodeInt, 
        'assetType': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
        'url': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSocialAction")
        kparams.addStringEnumIfDefined("actionType", self.actionType)
        kparams.addIntIfDefined("time", self.time)
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addStringEnumIfDefined("assetType", self.assetType)
        kparams.addStringIfDefined("url", self.url)
        return kparams

    def getId(self):
        return self.id

    def getActionType(self):
        return self.actionType

    def setActionType(self, newActionType):
        self.actionType = newActionType

    def getTime(self):
        return self.time

    def setTime(self, newTime):
        self.time = newTime

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getAssetType(self):
        return self.assetType

    def setAssetType(self, newAssetType):
        self.assetType = newAssetType

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl


# @package Kaltura
# @subpackage Client
class KalturaSocialFriendActivity(KalturaObjectBase):
    def __init__(self,
            userFullName=NotImplemented,
            userPictureUrl=NotImplemented,
            socialAction=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The full name of the user who did the social action
        # @var string
        self.userFullName = userFullName

        # The URL of the profile picture of the user who did the social action
        # @var string
        self.userPictureUrl = userPictureUrl

        # The social action
        # @var KalturaSocialAction
        self.socialAction = socialAction


    PROPERTY_LOADERS = {
        'userFullName': getXmlNodeText, 
        'userPictureUrl': getXmlNodeText, 
        'socialAction': (KalturaObjectFactory.create, 'KalturaSocialAction'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialFriendActivity.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSocialFriendActivity")
        kparams.addStringIfDefined("userFullName", self.userFullName)
        kparams.addStringIfDefined("userPictureUrl", self.userPictureUrl)
        kparams.addObjectIfDefined("socialAction", self.socialAction)
        return kparams

    def getUserFullName(self):
        return self.userFullName

    def setUserFullName(self, newUserFullName):
        self.userFullName = newUserFullName

    def getUserPictureUrl(self):
        return self.userPictureUrl

    def setUserPictureUrl(self, newUserPictureUrl):
        self.userPictureUrl = newUserPictureUrl

    def getSocialAction(self):
        return self.socialAction

    def setSocialAction(self, newSocialAction):
        self.socialAction = newSocialAction


# @package Kaltura
# @subpackage Client
class KalturaSocialFriendActivityListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Social friends activity
        # @var array of KalturaSocialFriendActivity
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSocialFriendActivity'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialFriendActivityListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSocialFriendActivityListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSocialActionRate(KalturaSocialAction):
    def __init__(self,
            id=NotImplemented,
            actionType=NotImplemented,
            time=NotImplemented,
            assetId=NotImplemented,
            assetType=NotImplemented,
            url=NotImplemented,
            rate=NotImplemented):
        KalturaSocialAction.__init__(self,
            id,
            actionType,
            time,
            assetId,
            assetType,
            url)

        # The value of the rating
        # @var int
        self.rate = rate


    PROPERTY_LOADERS = {
        'rate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaSocialAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialActionRate.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSocialAction.toParams(self)
        kparams.put("objectType", "KalturaSocialActionRate")
        kparams.addIntIfDefined("rate", self.rate)
        return kparams

    def getRate(self):
        return self.rate

    def setRate(self, newRate):
        self.rate = newRate


# @package Kaltura
# @subpackage Client
class KalturaSocialActionListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # The social actions
        # @var array of KalturaSocialAction
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSocialAction'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialActionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSocialActionListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentMethod(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            externalId=NotImplemented,
            paymentGatewayId=NotImplemented,
            details=NotImplemented,
            isDefault=NotImplemented,
            paymentMethodProfileId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Household payment method identifier (internal)
        # @var int
        # @readonly
        self.id = id

        # External identifier for the household payment method
        # @var string
        # @insertonly
        self.externalId = externalId

        # Payment-gateway identifier
        # @var int
        self.paymentGatewayId = paymentGatewayId

        # Description of the payment method details
        # @var string
        self.details = details

        # indicates whether the payment method is set as default for the household
        # @var bool
        # @readonly
        self.isDefault = isDefault

        # Payment method profile identifier
        # @var int
        self.paymentMethodProfileId = paymentMethodProfileId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'externalId': getXmlNodeText, 
        'paymentGatewayId': getXmlNodeInt, 
        'details': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
        'paymentMethodProfileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPaymentMethod.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPaymentMethod")
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addIntIfDefined("paymentGatewayId", self.paymentGatewayId)
        kparams.addStringIfDefined("details", self.details)
        kparams.addIntIfDefined("paymentMethodProfileId", self.paymentMethodProfileId)
        return kparams

    def getId(self):
        return self.id

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getPaymentGatewayId(self):
        return self.paymentGatewayId

    def setPaymentGatewayId(self, newPaymentGatewayId):
        self.paymentGatewayId = newPaymentGatewayId

    def getDetails(self):
        return self.details

    def setDetails(self, newDetails):
        self.details = newDetails

    def getIsDefault(self):
        return self.isDefault

    def getPaymentMethodProfileId(self):
        return self.paymentMethodProfileId

    def setPaymentMethodProfileId(self, newPaymentMethodProfileId):
        self.paymentMethodProfileId = newPaymentMethodProfileId


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentMethodListResponse(KalturaListResponse):
    """List of household payment methods."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaHouseholdPaymentMethod
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaHouseholdPaymentMethod'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPaymentMethodListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPaymentMethodListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfile(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            paymentGatewayId=NotImplemented,
            name=NotImplemented,
            allowMultiInstance=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Payment method identifier (internal)
        # @var int
        # @readonly
        self.id = id

        # Payment gateway identifier (internal)
        # @var int
        self.paymentGatewayId = paymentGatewayId

        # Payment method name
        # @var string
        self.name = name

        # Indicates whether the payment method allow multiple instances
        # @var bool
        self.allowMultiInstance = allowMultiInstance


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'paymentGatewayId': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'allowMultiInstance': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentMethodProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPaymentMethodProfile")
        kparams.addIntIfDefined("paymentGatewayId", self.paymentGatewayId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("allowMultiInstance", self.allowMultiInstance)
        return kparams

    def getId(self):
        return self.id

    def getPaymentGatewayId(self):
        return self.paymentGatewayId

    def setPaymentGatewayId(self, newPaymentGatewayId):
        self.paymentGatewayId = newPaymentGatewayId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getAllowMultiInstance(self):
        return self.allowMultiInstance

    def setAllowMultiInstance(self, newAllowMultiInstance):
        self.allowMultiInstance = newAllowMultiInstance


# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfileListResponse(KalturaListResponse):
    """List of payment method profiles."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Payment method profiles list
        # @var array of KalturaPaymentMethodProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaPaymentMethodProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentMethodProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPaymentMethodProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentGateway(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isDefault=NotImplemented,
            selectedBy=NotImplemented):
        KalturaObjectBase.__init__(self)

        # payment gateway id
        # @var int
        # @readonly
        self.id = id

        # payment gateway name
        # @var string
        self.name = name

        # Payment gateway default (true/false)
        # @var bool
        self.isDefault = isDefault

        # distinction payment gateway selected by account or household
        # @var KalturaHouseholdPaymentGatewaySelectedBy
        self.selectedBy = selectedBy


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
        'selectedBy': (KalturaEnumsFactory.createString, "KalturaHouseholdPaymentGatewaySelectedBy"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPaymentGateway.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPaymentGateway")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        kparams.addStringEnumIfDefined("selectedBy", self.selectedBy)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getSelectedBy(self):
        return self.selectedBy

    def setSelectedBy(self, newSelectedBy):
        self.selectedBy = newSelectedBy


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPaymentGatewayListResponse(KalturaListResponse):
    """List of household payment gateways."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaHouseholdPaymentGateway
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaHouseholdPaymentGateway'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPaymentGatewayListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPaymentGatewayListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPaymentGatewayBaseProfile(KalturaObjectBase):
    """Payment gateway base profile"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isDefault=NotImplemented,
            selectedBy=NotImplemented):
        KalturaObjectBase.__init__(self)

        # payment gateway id
        # @var int
        # @readonly
        self.id = id

        # payment gateway name
        # @var string
        self.name = name

        # Payment gateway default (true/false)
        # @var bool
        self.isDefault = isDefault

        # distinction payment gateway selected by account or household
        # @var KalturaHouseholdPaymentGatewaySelectedBy
        self.selectedBy = selectedBy


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
        'selectedBy': (KalturaEnumsFactory.createString, "KalturaHouseholdPaymentGatewaySelectedBy"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentGatewayBaseProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPaymentGatewayBaseProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        kparams.addStringEnumIfDefined("selectedBy", self.selectedBy)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getSelectedBy(self):
        return self.selectedBy

    def setSelectedBy(self, newSelectedBy):
        self.selectedBy = newSelectedBy


# @package Kaltura
# @subpackage Client
class KalturaValue(KalturaObjectBase):
    """A representation to return an array of values"""

    def __init__(self,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Description
        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaValue")
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaStringValue(KalturaValue):
    """A string representation to return an array of strings"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # Value
        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStringValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaStringValue")
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaPaymentGatewayProfile(KalturaPaymentGatewayBaseProfile):
    """Payment gateway profile"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isDefault=NotImplemented,
            selectedBy=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            transactUrl=NotImplemented,
            statusUrl=NotImplemented,
            renewUrl=NotImplemented,
            paymentGatewaySettings=NotImplemented,
            externalIdentifier=NotImplemented,
            pendingInterval=NotImplemented,
            pendingRetries=NotImplemented,
            sharedSecret=NotImplemented,
            renewIntervalMinutes=NotImplemented,
            renewStartMinutes=NotImplemented,
            externalVerification=NotImplemented):
        KalturaPaymentGatewayBaseProfile.__init__(self,
            id,
            name,
            isDefault,
            selectedBy)

        # Payment gateway is active status
        # @var int
        self.isActive = isActive

        # Payment gateway adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # Payment gateway transact URL
        # @var string
        self.transactUrl = transactUrl

        # Payment gateway status URL
        # @var string
        self.statusUrl = statusUrl

        # Payment gateway renew URL
        # @var string
        self.renewUrl = renewUrl

        # Payment gateway extra parameters
        # @var map
        self.paymentGatewaySettings = paymentGatewaySettings

        # Payment gateway external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Pending Interval in minutes
        # @var int
        self.pendingInterval = pendingInterval

        # Pending Retries
        # @var int
        self.pendingRetries = pendingRetries

        # Shared Secret
        # @var string
        self.sharedSecret = sharedSecret

        # Renew Interval Minutes
        # @var int
        self.renewIntervalMinutes = renewIntervalMinutes

        # Renew Start Minutes
        # @var int
        self.renewStartMinutes = renewStartMinutes

        # Payment gateway external verification
        # @var bool
        self.externalVerification = externalVerification


    PROPERTY_LOADERS = {
        'isActive': getXmlNodeInt, 
        'adapterUrl': getXmlNodeText, 
        'transactUrl': getXmlNodeText, 
        'statusUrl': getXmlNodeText, 
        'renewUrl': getXmlNodeText, 
        'paymentGatewaySettings': (KalturaObjectFactory.createMap, 'KalturaStringValue'), 
        'externalIdentifier': getXmlNodeText, 
        'pendingInterval': getXmlNodeInt, 
        'pendingRetries': getXmlNodeInt, 
        'sharedSecret': getXmlNodeText, 
        'renewIntervalMinutes': getXmlNodeInt, 
        'renewStartMinutes': getXmlNodeInt, 
        'externalVerification': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaPaymentGatewayBaseProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentGatewayProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPaymentGatewayBaseProfile.toParams(self)
        kparams.put("objectType", "KalturaPaymentGatewayProfile")
        kparams.addIntIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addStringIfDefined("transactUrl", self.transactUrl)
        kparams.addStringIfDefined("statusUrl", self.statusUrl)
        kparams.addStringIfDefined("renewUrl", self.renewUrl)
        kparams.addMapIfDefined("paymentGatewaySettings", self.paymentGatewaySettings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        kparams.addIntIfDefined("pendingInterval", self.pendingInterval)
        kparams.addIntIfDefined("pendingRetries", self.pendingRetries)
        kparams.addStringIfDefined("sharedSecret", self.sharedSecret)
        kparams.addIntIfDefined("renewIntervalMinutes", self.renewIntervalMinutes)
        kparams.addIntIfDefined("renewStartMinutes", self.renewStartMinutes)
        kparams.addBoolIfDefined("externalVerification", self.externalVerification)
        return kparams

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getTransactUrl(self):
        return self.transactUrl

    def setTransactUrl(self, newTransactUrl):
        self.transactUrl = newTransactUrl

    def getStatusUrl(self):
        return self.statusUrl

    def setStatusUrl(self, newStatusUrl):
        self.statusUrl = newStatusUrl

    def getRenewUrl(self):
        return self.renewUrl

    def setRenewUrl(self, newRenewUrl):
        self.renewUrl = newRenewUrl

    def getPaymentGatewaySettings(self):
        return self.paymentGatewaySettings

    def setPaymentGatewaySettings(self, newPaymentGatewaySettings):
        self.paymentGatewaySettings = newPaymentGatewaySettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getPendingInterval(self):
        return self.pendingInterval

    def setPendingInterval(self, newPendingInterval):
        self.pendingInterval = newPendingInterval

    def getPendingRetries(self):
        return self.pendingRetries

    def setPendingRetries(self, newPendingRetries):
        self.pendingRetries = newPendingRetries

    def getSharedSecret(self):
        return self.sharedSecret

    def setSharedSecret(self, newSharedSecret):
        self.sharedSecret = newSharedSecret

    def getRenewIntervalMinutes(self):
        return self.renewIntervalMinutes

    def setRenewIntervalMinutes(self, newRenewIntervalMinutes):
        self.renewIntervalMinutes = newRenewIntervalMinutes

    def getRenewStartMinutes(self):
        return self.renewStartMinutes

    def setRenewStartMinutes(self, newRenewStartMinutes):
        self.renewStartMinutes = newRenewStartMinutes

    def getExternalVerification(self):
        return self.externalVerification

    def setExternalVerification(self, newExternalVerification):
        self.externalVerification = newExternalVerification


# @package Kaltura
# @subpackage Client
class KalturaPaymentGatewayProfileListResponse(KalturaListResponse):
    """PaymentGatewayProfile list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of payment-gateway profiles
        # @var array of KalturaPaymentGatewayProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaPaymentGatewayProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentGatewayProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPaymentGatewayProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaTranslationToken(KalturaObjectBase):
    """Container for translation"""

    def __init__(self,
            language=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Language code
        # @var string
        self.language = language

        # Translated value
        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'language': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTranslationToken.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTranslationToken")
        kparams.addStringIfDefined("language", self.language)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaMultilingualStringValue(KalturaValue):
    """Array of translated strings"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented,
            multilingualValue=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # Value
        # @var string
        # @readonly
        self.value = value

        # Value
        # @var array of KalturaTranslationToken
        self.multilingualValue = multilingualValue


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
        'multilingualValue': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMultilingualStringValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaMultilingualStringValue")
        kparams.addArrayIfDefined("multilingualValue", self.multilingualValue)
        return kparams

    def getValue(self):
        return self.value

    def getMultilingualValue(self):
        return self.multilingualValue

    def setMultilingualValue(self, newMultilingualValue):
        self.multilingualValue = newMultilingualValue


# @package Kaltura
# @subpackage Client
class KalturaLongValue(KalturaValue):
    """A string representation to return an array of longs"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # Value
        # @var int
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLongValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaLongValue")
        kparams.addIntIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaDoubleValue(KalturaValue):
    """A string representation to return an array of doubles"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # Value
        # @var float
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDoubleValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaDoubleValue")
        kparams.addFloatIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaBooleanValue(KalturaValue):
    """A string representation to return an array of booleans"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # Value
        # @var bool
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBooleanValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaBooleanValue")
        kparams.addBoolIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaIntegerValue(KalturaValue):
    """A string representation to return an array of ints"""

    def __init__(self,
            description=NotImplemented,
            value=NotImplemented):
        KalturaValue.__init__(self,
            description)

        # Value
        # @var int
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaValue.fromXml(self, node)
        self.fromXmlImpl(node, KalturaIntegerValue.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaValue.toParams(self)
        kparams.put("objectType", "KalturaIntegerValue")
        kparams.addIntIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaPluginData(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPluginData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPluginData")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaDrmPlaybackPluginData(KalturaPluginData):
    def __init__(self,
            scheme=NotImplemented,
            licenseURL=NotImplemented):
        KalturaPluginData.__init__(self)

        # Scheme
        # @var KalturaDrmSchemeName
        self.scheme = scheme

        # License URL
        # @var string
        self.licenseURL = licenseURL


    PROPERTY_LOADERS = {
        'scheme': (KalturaEnumsFactory.createString, "KalturaDrmSchemeName"), 
        'licenseURL': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaPluginData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDrmPlaybackPluginData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPluginData.toParams(self)
        kparams.put("objectType", "KalturaDrmPlaybackPluginData")
        kparams.addStringEnumIfDefined("scheme", self.scheme)
        kparams.addStringIfDefined("licenseURL", self.licenseURL)
        return kparams

    def getScheme(self):
        return self.scheme

    def setScheme(self, newScheme):
        self.scheme = newScheme

    def getLicenseURL(self):
        return self.licenseURL

    def setLicenseURL(self, newLicenseURL):
        self.licenseURL = newLicenseURL


# @package Kaltura
# @subpackage Client
class KalturaCustomDrmPlaybackPluginData(KalturaDrmPlaybackPluginData):
    def __init__(self,
            scheme=NotImplemented,
            licenseURL=NotImplemented,
            data=NotImplemented):
        KalturaDrmPlaybackPluginData.__init__(self,
            scheme,
            licenseURL)

        # Custom DRM license data
        # @var string
        self.data = data


    PROPERTY_LOADERS = {
        'data': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDrmPlaybackPluginData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCustomDrmPlaybackPluginData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDrmPlaybackPluginData.toParams(self)
        kparams.put("objectType", "KalturaCustomDrmPlaybackPluginData")
        kparams.addStringIfDefined("data", self.data)
        return kparams

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData


# @package Kaltura
# @subpackage Client
class KalturaHouseholdDevice(KalturaObjectBase):
    """Device details"""

    def __init__(self,
            householdId=NotImplemented,
            udid=NotImplemented,
            name=NotImplemented,
            brandId=NotImplemented,
            activatedOn=NotImplemented,
            status=NotImplemented,
            deviceFamilyId=NotImplemented,
            drm=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Household identifier
        # @var int
        self.householdId = householdId

        # Device UDID
        # @var string
        # @insertonly
        self.udid = udid

        # Device name
        # @var string
        self.name = name

        # Device brand identifier
        # @var int
        self.brandId = brandId

        # Device activation date (epoch)
        # @var int
        self.activatedOn = activatedOn

        # Device state
        # @var KalturaDeviceStatus
        # @readonly
        self.status = status

        # Device family id
        # @var int
        # @readonly
        self.deviceFamilyId = deviceFamilyId

        # Device DRM data
        # @var KalturaCustomDrmPlaybackPluginData
        # @readonly
        self.drm = drm


    PROPERTY_LOADERS = {
        'householdId': getXmlNodeInt, 
        'udid': getXmlNodeText, 
        'name': getXmlNodeText, 
        'brandId': getXmlNodeInt, 
        'activatedOn': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createString, "KalturaDeviceStatus"), 
        'deviceFamilyId': getXmlNodeInt, 
        'drm': (KalturaObjectFactory.create, 'KalturaCustomDrmPlaybackPluginData'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdDevice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdDevice")
        kparams.addIntIfDefined("householdId", self.householdId)
        kparams.addStringIfDefined("udid", self.udid)
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("brandId", self.brandId)
        kparams.addIntIfDefined("activatedOn", self.activatedOn)
        return kparams

    def getHouseholdId(self):
        return self.householdId

    def setHouseholdId(self, newHouseholdId):
        self.householdId = newHouseholdId

    def getUdid(self):
        return self.udid

    def setUdid(self, newUdid):
        self.udid = newUdid

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getBrandId(self):
        return self.brandId

    def setBrandId(self, newBrandId):
        self.brandId = newBrandId

    def getActivatedOn(self):
        return self.activatedOn

    def setActivatedOn(self, newActivatedOn):
        self.activatedOn = newActivatedOn

    def getStatus(self):
        return self.status

    def getDeviceFamilyId(self):
        return self.deviceFamilyId

    def getDrm(self):
        return self.drm


# @package Kaltura
# @subpackage Client
class KalturaHouseholdDeviceListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Household devices
        # @var array of KalturaHouseholdDevice
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaHouseholdDevice'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdDeviceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHouseholdDeviceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaFairPlayPlaybackPluginData(KalturaDrmPlaybackPluginData):
    def __init__(self,
            scheme=NotImplemented,
            licenseURL=NotImplemented,
            certificate=NotImplemented):
        KalturaDrmPlaybackPluginData.__init__(self,
            scheme,
            licenseURL)

        # Custom data string
        # @var string
        self.certificate = certificate


    PROPERTY_LOADERS = {
        'certificate': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaDrmPlaybackPluginData.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFairPlayPlaybackPluginData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDrmPlaybackPluginData.toParams(self)
        kparams.put("objectType", "KalturaFairPlayPlaybackPluginData")
        kparams.addStringIfDefined("certificate", self.certificate)
        return kparams

    def getCertificate(self):
        return self.certificate

    def setCertificate(self, newCertificate):
        self.certificate = newCertificate


# @package Kaltura
# @subpackage Client
class KalturaHouseholdUser(KalturaObjectBase):
    """Household user"""

    def __init__(self,
            householdId=NotImplemented,
            userId=NotImplemented,
            isMaster=NotImplemented,
            householdMasterUsername=NotImplemented,
            status=NotImplemented,
            isDefault=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The identifier of the household
        # @var int
        self.householdId = householdId

        # The identifier of the user
        # @var string
        self.userId = userId

        # True if the user added as master use
        # @var bool
        self.isMaster = isMaster

        # The username of the household master for adding a user in status pending for the household master to approve
        # @var string
        # @insertonly
        self.householdMasterUsername = householdMasterUsername

        # The status of the user in the household
        # @var KalturaHouseholdUserStatus
        # @readonly
        self.status = status

        # True if the user is a default user
        # @var bool
        # @readonly
        self.isDefault = isDefault


    PROPERTY_LOADERS = {
        'householdId': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'isMaster': getXmlNodeBool, 
        'householdMasterUsername': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createString, "KalturaHouseholdUserStatus"), 
        'isDefault': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdUser")
        kparams.addIntIfDefined("householdId", self.householdId)
        kparams.addStringIfDefined("userId", self.userId)
        kparams.addBoolIfDefined("isMaster", self.isMaster)
        kparams.addStringIfDefined("householdMasterUsername", self.householdMasterUsername)
        return kparams

    def getHouseholdId(self):
        return self.householdId

    def setHouseholdId(self, newHouseholdId):
        self.householdId = newHouseholdId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getIsMaster(self):
        return self.isMaster

    def setIsMaster(self, newIsMaster):
        self.isMaster = newIsMaster

    def getHouseholdMasterUsername(self):
        return self.householdMasterUsername

    def setHouseholdMasterUsername(self, newHouseholdMasterUsername):
        self.householdMasterUsername = newHouseholdMasterUsername

    def getStatus(self):
        return self.status

    def getIsDefault(self):
        return self.isDefault


# @package Kaltura
# @subpackage Client
class KalturaHouseholdUserListResponse(KalturaListResponse):
    """Household users list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Household users
        # @var array of KalturaHouseholdUser
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaHouseholdUser'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdUserListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHouseholdUserListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaHomeNetwork(KalturaObjectBase):
    """Home network details"""

    def __init__(self,
            externalId=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            isActive=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Home network identifier
        # @var string
        # @insertonly
        self.externalId = externalId

        # Home network name
        # @var string
        self.name = name

        # Home network description
        # @var string
        self.description = description

        # Is home network is active
        # @var bool
        self.isActive = isActive


    PROPERTY_LOADERS = {
        'externalId': getXmlNodeText, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHomeNetwork.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaHomeNetwork")
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addBoolIfDefined("isActive", self.isActive)
        return kparams

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive


# @package Kaltura
# @subpackage Client
class KalturaHomeNetworkListResponse(KalturaListResponse):
    """Home networks"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Home networks
        # @var array of KalturaHomeNetwork
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaHomeNetwork'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHomeNetworkListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHomeNetworkListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaConfigurations(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            partnerId=NotImplemented,
            configurationGroupId=NotImplemented,
            appName=NotImplemented,
            clientVersion=NotImplemented,
            platform=NotImplemented,
            externalPushId=NotImplemented,
            isForceUpdate=NotImplemented,
            content=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Configuration id
        # @var string
        # @readonly
        self.id = id

        # Partner id
        # @var int
        # @readonly
        self.partnerId = partnerId

        # Configuration group id
        # @var string
        self.configurationGroupId = configurationGroupId

        # Application name
        # @var string
        self.appName = appName

        # Client version
        # @var string
        self.clientVersion = clientVersion

        # Platform: Android/iOS/WindowsPhone/Blackberry/STB/CTV/Other
        # @var KalturaPlatform
        self.platform = platform

        # External push id
        # @var string
        self.externalPushId = externalPushId

        # Is force update
        # @var bool
        self.isForceUpdate = isForceUpdate

        # Content
        # @var string
        self.content = content


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'configurationGroupId': getXmlNodeText, 
        'appName': getXmlNodeText, 
        'clientVersion': getXmlNodeText, 
        'platform': (KalturaEnumsFactory.createString, "KalturaPlatform"), 
        'externalPushId': getXmlNodeText, 
        'isForceUpdate': getXmlNodeBool, 
        'content': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurations.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConfigurations")
        kparams.addStringIfDefined("configurationGroupId", self.configurationGroupId)
        kparams.addStringIfDefined("appName", self.appName)
        kparams.addStringIfDefined("clientVersion", self.clientVersion)
        kparams.addStringEnumIfDefined("platform", self.platform)
        kparams.addStringIfDefined("externalPushId", self.externalPushId)
        kparams.addBoolIfDefined("isForceUpdate", self.isForceUpdate)
        kparams.addStringIfDefined("content", self.content)
        return kparams

    def getId(self):
        return self.id

    def getPartnerId(self):
        return self.partnerId

    def getConfigurationGroupId(self):
        return self.configurationGroupId

    def setConfigurationGroupId(self, newConfigurationGroupId):
        self.configurationGroupId = newConfigurationGroupId

    def getAppName(self):
        return self.appName

    def setAppName(self, newAppName):
        self.appName = newAppName

    def getClientVersion(self):
        return self.clientVersion

    def setClientVersion(self, newClientVersion):
        self.clientVersion = newClientVersion

    def getPlatform(self):
        return self.platform

    def setPlatform(self, newPlatform):
        self.platform = newPlatform

    def getExternalPushId(self):
        return self.externalPushId

    def setExternalPushId(self, newExternalPushId):
        self.externalPushId = newExternalPushId

    def getIsForceUpdate(self):
        return self.isForceUpdate

    def setIsForceUpdate(self, newIsForceUpdate):
        self.isForceUpdate = newIsForceUpdate

    def getContent(self):
        return self.content

    def setContent(self, newContent):
        self.content = newContent


# @package Kaltura
# @subpackage Client
class KalturaConfigurationsListResponse(KalturaListResponse):
    """Configurations info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Configurations
        # @var array of KalturaConfigurations
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaConfigurations'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaConfigurationsListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupDevice(KalturaObjectBase):
    def __init__(self,
            configurationGroupId=NotImplemented,
            partnerId=NotImplemented,
            udid=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Configuration group id
        # @var string
        self.configurationGroupId = configurationGroupId

        # Partner id
        # @var int
        # @readonly
        self.partnerId = partnerId

        # Device UDID
        # @var string
        self.udid = udid


    PROPERTY_LOADERS = {
        'configurationGroupId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'udid': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationGroupDevice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConfigurationGroupDevice")
        kparams.addStringIfDefined("configurationGroupId", self.configurationGroupId)
        kparams.addStringIfDefined("udid", self.udid)
        return kparams

    def getConfigurationGroupId(self):
        return self.configurationGroupId

    def setConfigurationGroupId(self, newConfigurationGroupId):
        self.configurationGroupId = newConfigurationGroupId

    def getPartnerId(self):
        return self.partnerId

    def getUdid(self):
        return self.udid

    def setUdid(self, newUdid):
        self.udid = newUdid


# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupDeviceListResponse(KalturaListResponse):
    """Configuration group devices info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Configuration group devices
        # @var array of KalturaConfigurationGroupDevice
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaConfigurationGroupDevice'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationGroupDeviceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaConfigurationGroupDeviceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupTag(KalturaObjectBase):
    def __init__(self,
            configurationGroupId=NotImplemented,
            partnerId=NotImplemented,
            tag=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Configuration group identifier
        # @var string
        self.configurationGroupId = configurationGroupId

        # Partner identifier
        # @var int
        # @readonly
        self.partnerId = partnerId

        # Tag
        # @var string
        self.tag = tag


    PROPERTY_LOADERS = {
        'configurationGroupId': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'tag': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationGroupTag.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConfigurationGroupTag")
        kparams.addStringIfDefined("configurationGroupId", self.configurationGroupId)
        kparams.addStringIfDefined("tag", self.tag)
        return kparams

    def getConfigurationGroupId(self):
        return self.configurationGroupId

    def setConfigurationGroupId(self, newConfigurationGroupId):
        self.configurationGroupId = newConfigurationGroupId

    def getPartnerId(self):
        return self.partnerId

    def getTag(self):
        return self.tag

    def setTag(self, newTag):
        self.tag = newTag


# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupTagListResponse(KalturaListResponse):
    """Configurations group tags info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Configuration group tags
        # @var array of KalturaConfigurationGroupTag
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaConfigurationGroupTag'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationGroupTagListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaConfigurationGroupTagListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaConfigurationIdentifier(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Identifier
        # @var string
        self.id = id

        # Name
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationIdentifier.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConfigurationIdentifier")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroup(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            partnerId=NotImplemented,
            isDefault=NotImplemented,
            tags=NotImplemented,
            numberOfDevices=NotImplemented,
            configurationIdentifiers=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Configuration group identifier
        # @var string
        # @readonly
        self.id = id

        # Configuration group name
        # @var string
        self.name = name

        # Partner id
        # @var int
        # @readonly
        self.partnerId = partnerId

        # Is default
        # @var bool
        # @insertonly
        self.isDefault = isDefault

        # tags
        # @var array of KalturaStringValue
        # @readonly
        self.tags = tags

        # Number of devices
        # @var int
        # @readonly
        self.numberOfDevices = numberOfDevices

        # Configuration identifiers
        # @var array of KalturaConfigurationIdentifier
        # @readonly
        self.configurationIdentifiers = configurationIdentifiers


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'partnerId': getXmlNodeInt, 
        'isDefault': getXmlNodeBool, 
        'tags': (KalturaObjectFactory.createArray, 'KalturaStringValue'), 
        'numberOfDevices': getXmlNodeInt, 
        'configurationIdentifiers': (KalturaObjectFactory.createArray, 'KalturaConfigurationIdentifier'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationGroup.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaConfigurationGroup")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPartnerId(self):
        return self.partnerId

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getTags(self):
        return self.tags

    def getNumberOfDevices(self):
        return self.numberOfDevices

    def getConfigurationIdentifiers(self):
        return self.configurationIdentifiers


# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupListResponse(KalturaListResponse):
    """Configuration groups info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Configuration groups
        # @var array of KalturaConfigurationGroup
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaConfigurationGroup'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationGroupListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaConfigurationGroupListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSSOAdapterProfile(KalturaObjectBase):
    """SSO adapter configuration"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            settings=NotImplemented,
            externalIdentifier=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaObjectBase.__init__(self)

        # SSO Adapter id
        # @var int
        # @readonly
        self.id = id

        # SSO Adapter name
        # @var string
        self.name = name

        # SSO Adapter is active status
        # @var int
        self.isActive = isActive

        # SSO Adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # SSO Adapter extra parameters
        # @var map
        self.settings = settings

        # SSO Adapter external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Shared Secret
        # @var string
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeInt, 
        'adapterUrl': getXmlNodeText, 
        'settings': (KalturaObjectFactory.createMap, 'KalturaStringValue'), 
        'externalIdentifier': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSSOAdapterProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSSOAdapterProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addMapIfDefined("settings", self.settings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        kparams.addStringIfDefined("sharedSecret", self.sharedSecret)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getSettings(self):
        return self.settings

    def setSettings(self, newSettings):
        self.settings = newSettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getSharedSecret(self):
        return self.sharedSecret

    def setSharedSecret(self, newSharedSecret):
        self.sharedSecret = newSharedSecret


# @package Kaltura
# @subpackage Client
class KalturaSSOAdapterProfileListResponse(KalturaListResponse):
    """ssoAdapterProfile list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of payment-gateway profiles
        # @var array of KalturaSSOAdapterProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSSOAdapterProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSSOAdapterProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSSOAdapterProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaUserInterestTopic(KalturaObjectBase):
    """User interest topic"""

    def __init__(self,
            metaId=NotImplemented,
            value=NotImplemented,
            parentTopic=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Meta identifier
        # @var string
        self.metaId = metaId

        # Meta Value
        # @var string
        self.value = value

        # Parent topic
        # @var KalturaUserInterestTopic
        self.parentTopic = parentTopic


    PROPERTY_LOADERS = {
        'metaId': getXmlNodeText, 
        'value': getXmlNodeText, 
        'parentTopic': (KalturaObjectFactory.create, 'KalturaObjectBase'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserInterestTopic.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserInterestTopic")
        kparams.addStringIfDefined("metaId", self.metaId)
        kparams.addStringIfDefined("value", self.value)
        kparams.addObjectIfDefined("parentTopic", self.parentTopic)
        return kparams

    def getMetaId(self):
        return self.metaId

    def setMetaId(self, newMetaId):
        self.metaId = newMetaId

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

    def getParentTopic(self):
        return self.parentTopic

    def setParentTopic(self, newParentTopic):
        self.parentTopic = newParentTopic


# @package Kaltura
# @subpackage Client
class KalturaUserInterest(KalturaObjectBase):
    """User Interest"""

    def __init__(self,
            id=NotImplemented,
            topic=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Identifier
        # @var string
        # @readonly
        self.id = id

        # Topic
        # @var KalturaUserInterestTopic
        self.topic = topic


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'topic': (KalturaObjectFactory.create, 'KalturaUserInterestTopic'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserInterest.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserInterest")
        kparams.addObjectIfDefined("topic", self.topic)
        return kparams

    def getId(self):
        return self.id

    def getTopic(self):
        return self.topic

    def setTopic(self, newTopic):
        self.topic = newTopic


# @package Kaltura
# @subpackage Client
class KalturaUserInterestListResponse(KalturaListResponse):
    """User interest list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of UserInterests
        # @var array of KalturaUserInterest
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaUserInterest'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserInterestListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaUserInterestListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaMediaImage(KalturaObjectBase):
    """Image details"""

    def __init__(self,
            ratio=NotImplemented,
            width=NotImplemented,
            height=NotImplemented,
            url=NotImplemented,
            version=NotImplemented,
            id=NotImplemented,
            isDefault=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Image aspect ratio
        # @var string
        self.ratio = ratio

        # Image width
        # @var int
        self.width = width

        # Image height
        # @var int
        self.height = height

        # Image URL
        # @var string
        self.url = url

        # Image Version
        # @var int
        self.version = version

        # Image ID
        # @var string
        # @readonly
        self.id = id

        # Determined whether image was taken from default configuration or not
        # @var bool
        self.isDefault = isDefault


    PROPERTY_LOADERS = {
        'ratio': getXmlNodeText, 
        'width': getXmlNodeInt, 
        'height': getXmlNodeInt, 
        'url': getXmlNodeText, 
        'version': getXmlNodeInt, 
        'id': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaImage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaImage")
        kparams.addStringIfDefined("ratio", self.ratio)
        kparams.addIntIfDefined("width", self.width)
        kparams.addIntIfDefined("height", self.height)
        kparams.addStringIfDefined("url", self.url)
        kparams.addIntIfDefined("version", self.version)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        return kparams

    def getRatio(self):
        return self.ratio

    def setRatio(self, newRatio):
        self.ratio = newRatio

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl

    def getVersion(self):
        return self.version

    def setVersion(self, newVersion):
        self.version = newVersion

    def getId(self):
        return self.id

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault


# @package Kaltura
# @subpackage Client
class KalturaAssetFile(KalturaObjectBase):
    """Asset file details"""

    def __init__(self,
            url=NotImplemented):
        KalturaObjectBase.__init__(self)

        # URL of the media file to be played
        # @var string
        self.url = url


    PROPERTY_LOADERS = {
        'url': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetFile")
        kparams.addStringIfDefined("url", self.url)
        return kparams

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl


# @package Kaltura
# @subpackage Client
class KalturaMediaFile(KalturaAssetFile):
    """Media file details"""

    def __init__(self,
            url=NotImplemented,
            assetId=NotImplemented,
            id=NotImplemented,
            typeId=NotImplemented,
            duration=NotImplemented,
            externalId=NotImplemented,
            altExternalId=NotImplemented,
            fileSize=NotImplemented,
            additionalData=NotImplemented,
            altStreamingCode=NotImplemented,
            alternativeCdnAdapaterProfileId=NotImplemented,
            endDate=NotImplemented,
            startDate=NotImplemented,
            externalStoreId=NotImplemented,
            isDefaultLanguage=NotImplemented,
            language=NotImplemented,
            orderNum=NotImplemented,
            outputProtecationLevel=NotImplemented,
            cdnAdapaterProfileId=NotImplemented,
            status=NotImplemented):
        KalturaAssetFile.__init__(self,
            url)

        # Unique identifier for the asset
        # @var int
        self.assetId = assetId

        # File unique identifier
        # @var int
        # @readonly
        self.id = id

        # Device types identifier as defined in the system
        # @var int
        self.typeId = typeId

        # Duration of the media file
        # @var int
        self.duration = duration

        # External identifier for the media file
        # @var string
        self.externalId = externalId

        # Alternative external identifier for the media file
        # @var string
        self.altExternalId = altExternalId

        # File size
        # @var int
        self.fileSize = fileSize

        # Additional Data
        # @var string
        self.additionalData = additionalData

        # Alternative streaming code
        # @var string
        self.altStreamingCode = altStreamingCode

        # Alternative cdn adapter profile identifier
        # @var int
        self.alternativeCdnAdapaterProfileId = alternativeCdnAdapaterProfileId

        # EndDate
        # @var int
        self.endDate = endDate

        # StartDate
        # @var int
        self.startDate = startDate

        # ExternalStoreId
        # @var string
        self.externalStoreId = externalStoreId

        # IsDefaultLanguage
        # @var bool
        self.isDefaultLanguage = isDefaultLanguage

        # Language
        # @var string
        self.language = language

        # OrderNum
        # @var int
        self.orderNum = orderNum

        # OutputProtecationLevel
        # @var string
        self.outputProtecationLevel = outputProtecationLevel

        # cdn adapter profile identifier
        # @var int
        self.cdnAdapaterProfileId = cdnAdapaterProfileId

        # The media file status
        # @var bool
        self.status = status


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
        'id': getXmlNodeInt, 
        'typeId': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'externalId': getXmlNodeText, 
        'altExternalId': getXmlNodeText, 
        'fileSize': getXmlNodeInt, 
        'additionalData': getXmlNodeText, 
        'altStreamingCode': getXmlNodeText, 
        'alternativeCdnAdapaterProfileId': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'startDate': getXmlNodeInt, 
        'externalStoreId': getXmlNodeText, 
        'isDefaultLanguage': getXmlNodeBool, 
        'language': getXmlNodeText, 
        'orderNum': getXmlNodeInt, 
        'outputProtecationLevel': getXmlNodeText, 
        'cdnAdapaterProfileId': getXmlNodeInt, 
        'status': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaAssetFile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFile.toParams(self)
        kparams.put("objectType", "KalturaMediaFile")
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addIntIfDefined("typeId", self.typeId)
        kparams.addIntIfDefined("duration", self.duration)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addStringIfDefined("altExternalId", self.altExternalId)
        kparams.addIntIfDefined("fileSize", self.fileSize)
        kparams.addStringIfDefined("additionalData", self.additionalData)
        kparams.addStringIfDefined("altStreamingCode", self.altStreamingCode)
        kparams.addIntIfDefined("alternativeCdnAdapaterProfileId", self.alternativeCdnAdapaterProfileId)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addStringIfDefined("externalStoreId", self.externalStoreId)
        kparams.addBoolIfDefined("isDefaultLanguage", self.isDefaultLanguage)
        kparams.addStringIfDefined("language", self.language)
        kparams.addIntIfDefined("orderNum", self.orderNum)
        kparams.addStringIfDefined("outputProtecationLevel", self.outputProtecationLevel)
        kparams.addIntIfDefined("cdnAdapaterProfileId", self.cdnAdapaterProfileId)
        kparams.addBoolIfDefined("status", self.status)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getId(self):
        return self.id

    def getTypeId(self):
        return self.typeId

    def setTypeId(self, newTypeId):
        self.typeId = newTypeId

    def getDuration(self):
        return self.duration

    def setDuration(self, newDuration):
        self.duration = newDuration

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getAltExternalId(self):
        return self.altExternalId

    def setAltExternalId(self, newAltExternalId):
        self.altExternalId = newAltExternalId

    def getFileSize(self):
        return self.fileSize

    def setFileSize(self, newFileSize):
        self.fileSize = newFileSize

    def getAdditionalData(self):
        return self.additionalData

    def setAdditionalData(self, newAdditionalData):
        self.additionalData = newAdditionalData

    def getAltStreamingCode(self):
        return self.altStreamingCode

    def setAltStreamingCode(self, newAltStreamingCode):
        self.altStreamingCode = newAltStreamingCode

    def getAlternativeCdnAdapaterProfileId(self):
        return self.alternativeCdnAdapaterProfileId

    def setAlternativeCdnAdapaterProfileId(self, newAlternativeCdnAdapaterProfileId):
        self.alternativeCdnAdapaterProfileId = newAlternativeCdnAdapaterProfileId

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getExternalStoreId(self):
        return self.externalStoreId

    def setExternalStoreId(self, newExternalStoreId):
        self.externalStoreId = newExternalStoreId

    def getIsDefaultLanguage(self):
        return self.isDefaultLanguage

    def setIsDefaultLanguage(self, newIsDefaultLanguage):
        self.isDefaultLanguage = newIsDefaultLanguage

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getOrderNum(self):
        return self.orderNum

    def setOrderNum(self, newOrderNum):
        self.orderNum = newOrderNum

    def getOutputProtecationLevel(self):
        return self.outputProtecationLevel

    def setOutputProtecationLevel(self, newOutputProtecationLevel):
        self.outputProtecationLevel = newOutputProtecationLevel

    def getCdnAdapaterProfileId(self):
        return self.cdnAdapaterProfileId

    def setCdnAdapaterProfileId(self, newCdnAdapaterProfileId):
        self.cdnAdapaterProfileId = newCdnAdapaterProfileId

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus


# @package Kaltura
# @subpackage Client
class KalturaBuzzScore(KalturaObjectBase):
    """Buzz score"""

    def __init__(self,
            normalizedAvgScore=NotImplemented,
            updateDate=NotImplemented,
            avgScore=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Normalized average score
        # @var float
        self.normalizedAvgScore = normalizedAvgScore

        # Update date
        # @var int
        self.updateDate = updateDate

        # Average score
        # @var float
        self.avgScore = avgScore


    PROPERTY_LOADERS = {
        'normalizedAvgScore': getXmlNodeFloat, 
        'updateDate': getXmlNodeInt, 
        'avgScore': getXmlNodeFloat, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBuzzScore.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBuzzScore")
        kparams.addFloatIfDefined("normalizedAvgScore", self.normalizedAvgScore)
        kparams.addIntIfDefined("updateDate", self.updateDate)
        kparams.addFloatIfDefined("avgScore", self.avgScore)
        return kparams

    def getNormalizedAvgScore(self):
        return self.normalizedAvgScore

    def setNormalizedAvgScore(self, newNormalizedAvgScore):
        self.normalizedAvgScore = newNormalizedAvgScore

    def getUpdateDate(self):
        return self.updateDate

    def setUpdateDate(self, newUpdateDate):
        self.updateDate = newUpdateDate

    def getAvgScore(self):
        return self.avgScore

    def setAvgScore(self, newAvgScore):
        self.avgScore = newAvgScore


# @package Kaltura
# @subpackage Client
class KalturaAssetStatistics(KalturaObjectBase):
    """Asset statistics"""

    def __init__(self,
            assetId=NotImplemented,
            likes=NotImplemented,
            views=NotImplemented,
            ratingCount=NotImplemented,
            rating=NotImplemented,
            buzzScore=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier for the asset
        # @var int
        self.assetId = assetId

        # Total number of likes for this asset
        # @var int
        self.likes = likes

        # Total number of views for this asset
        # @var int
        self.views = views

        # Number of people that rated the asset
        # @var int
        self.ratingCount = ratingCount

        # Average rating for the asset
        # @var float
        self.rating = rating

        # Buzz score
        # @var KalturaBuzzScore
        self.buzzScore = buzzScore


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
        'likes': getXmlNodeInt, 
        'views': getXmlNodeInt, 
        'ratingCount': getXmlNodeInt, 
        'rating': getXmlNodeFloat, 
        'buzzScore': (KalturaObjectFactory.create, 'KalturaBuzzScore'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStatistics.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetStatistics")
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addIntIfDefined("likes", self.likes)
        kparams.addIntIfDefined("views", self.views)
        kparams.addIntIfDefined("ratingCount", self.ratingCount)
        kparams.addFloatIfDefined("rating", self.rating)
        kparams.addObjectIfDefined("buzzScore", self.buzzScore)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getLikes(self):
        return self.likes

    def setLikes(self, newLikes):
        self.likes = newLikes

    def getViews(self):
        return self.views

    def setViews(self, newViews):
        self.views = newViews

    def getRatingCount(self):
        return self.ratingCount

    def setRatingCount(self, newRatingCount):
        self.ratingCount = newRatingCount

    def getRating(self):
        return self.rating

    def setRating(self, newRating):
        self.rating = newRating

    def getBuzzScore(self):
        return self.buzzScore

    def setBuzzScore(self, newBuzzScore):
        self.buzzScore = newBuzzScore


# @package Kaltura
# @subpackage Client
class KalturaMultilingualStringValueArray(KalturaObjectBase):
    """Array of translated strings"""

    def __init__(self,
            objects=NotImplemented):
        KalturaObjectBase.__init__(self)

        # List of string values
        # @var array of KalturaMultilingualStringValue
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaMultilingualStringValue'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMultilingualStringValueArray.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMultilingualStringValueArray")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaFavorite(KalturaObjectBase):
    """Favorite details"""

    def __init__(self,
            assetId=NotImplemented,
            extraData=NotImplemented,
            createDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # AssetInfo Model
        # @var int
        self.assetId = assetId

        # Extra Value
        # @var string
        self.extraData = extraData

        # Specifies when was the favorite created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
        'extraData': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFavorite.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFavorite")
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addStringIfDefined("extraData", self.extraData)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getExtraData(self):
        return self.extraData

    def setExtraData(self, newExtraData):
        self.extraData = newExtraData

    def getCreateDate(self):
        return self.createDate


# @package Kaltura
# @subpackage Client
class KalturaFavoriteListResponse(KalturaListResponse):
    """Favorite list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of favorites
        # @var array of KalturaFavorite
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaFavorite'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFavoriteListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaFavoriteListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPlaybackSource(KalturaMediaFile):
    def __init__(self,
            url=NotImplemented,
            assetId=NotImplemented,
            id=NotImplemented,
            typeId=NotImplemented,
            duration=NotImplemented,
            externalId=NotImplemented,
            altExternalId=NotImplemented,
            fileSize=NotImplemented,
            additionalData=NotImplemented,
            altStreamingCode=NotImplemented,
            alternativeCdnAdapaterProfileId=NotImplemented,
            endDate=NotImplemented,
            startDate=NotImplemented,
            externalStoreId=NotImplemented,
            isDefaultLanguage=NotImplemented,
            language=NotImplemented,
            orderNum=NotImplemented,
            outputProtecationLevel=NotImplemented,
            cdnAdapaterProfileId=NotImplemented,
            status=NotImplemented,
            format=NotImplemented,
            protocols=NotImplemented,
            drm=NotImplemented):
        KalturaMediaFile.__init__(self,
            url,
            assetId,
            id,
            typeId,
            duration,
            externalId,
            altExternalId,
            fileSize,
            additionalData,
            altStreamingCode,
            alternativeCdnAdapaterProfileId,
            endDate,
            startDate,
            externalStoreId,
            isDefaultLanguage,
            language,
            orderNum,
            outputProtecationLevel,
            cdnAdapaterProfileId,
            status)

        # Source format according to delivery profile streamer type (applehttp, mpegdash etc.)
        # @var string
        self.format = format

        # Comma separated string according to deliveryProfile media protocols (&#39;http,https&#39; etc.)
        # @var string
        self.protocols = protocols

        # DRM data object containing relevant license URL ,scheme name and certificate
        # @var array of KalturaDrmPlaybackPluginData
        self.drm = drm


    PROPERTY_LOADERS = {
        'format': getXmlNodeText, 
        'protocols': getXmlNodeText, 
        'drm': (KalturaObjectFactory.createArray, 'KalturaDrmPlaybackPluginData'), 
    }

    def fromXml(self, node):
        KalturaMediaFile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPlaybackSource.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaFile.toParams(self)
        kparams.put("objectType", "KalturaPlaybackSource")
        kparams.addStringIfDefined("format", self.format)
        kparams.addStringIfDefined("protocols", self.protocols)
        kparams.addArrayIfDefined("drm", self.drm)
        return kparams

    def getFormat(self):
        return self.format

    def setFormat(self, newFormat):
        self.format = newFormat

    def getProtocols(self):
        return self.protocols

    def setProtocols(self, newProtocols):
        self.protocols = newProtocols

    def getDrm(self):
        return self.drm

    def setDrm(self, newDrm):
        self.drm = newDrm


# @package Kaltura
# @subpackage Client
class KalturaBaseOTTUser(KalturaObjectBase):
    """Slim user data"""

    def __init__(self,
            id=NotImplemented,
            username=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented):
        KalturaObjectBase.__init__(self)

        # User identifier
        # @var string
        # @readonly
        self.id = id

        # Username
        # @var string
        self.username = username

        # First name
        # @var string
        self.firstName = firstName

        # Last name
        # @var string
        self.lastName = lastName


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'username': getXmlNodeText, 
        'firstName': getXmlNodeText, 
        'lastName': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseOTTUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseOTTUser")
        kparams.addStringIfDefined("username", self.username)
        kparams.addStringIfDefined("firstName", self.firstName)
        kparams.addStringIfDefined("lastName", self.lastName)
        return kparams

    def getId(self):
        return self.id

    def getUsername(self):
        return self.username

    def setUsername(self, newUsername):
        self.username = newUsername

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, newFirstName):
        self.firstName = newFirstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, newLastName):
        self.lastName = newLastName


# @package Kaltura
# @subpackage Client
class KalturaCountry(KalturaObjectBase):
    """Country details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            code=NotImplemented,
            mainLanguageCode=NotImplemented,
            languagesCode=NotImplemented,
            currency=NotImplemented,
            currencySign=NotImplemented,
            vatPercent=NotImplemented,
            timeZoneId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Country identifier
        # @var int
        # @readonly
        self.id = id

        # Country name
        # @var string
        self.name = name

        # Country code
        # @var string
        self.code = code

        # The main language code in the country
        # @var string
        self.mainLanguageCode = mainLanguageCode

        # All the languages code that are supported in the country
        # @var string
        self.languagesCode = languagesCode

        # Currency code
        # @var string
        self.currency = currency

        # Currency Sign
        # @var string
        self.currencySign = currencySign

        # Vat Percent in the country
        # @var float
        self.vatPercent = vatPercent

        # Time zone ID
        # @var string
        self.timeZoneId = timeZoneId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'code': getXmlNodeText, 
        'mainLanguageCode': getXmlNodeText, 
        'languagesCode': getXmlNodeText, 
        'currency': getXmlNodeText, 
        'currencySign': getXmlNodeText, 
        'vatPercent': getXmlNodeFloat, 
        'timeZoneId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCountry.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCountry")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("code", self.code)
        kparams.addStringIfDefined("mainLanguageCode", self.mainLanguageCode)
        kparams.addStringIfDefined("languagesCode", self.languagesCode)
        kparams.addStringIfDefined("currency", self.currency)
        kparams.addStringIfDefined("currencySign", self.currencySign)
        kparams.addFloatIfDefined("vatPercent", self.vatPercent)
        kparams.addStringIfDefined("timeZoneId", self.timeZoneId)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getCode(self):
        return self.code

    def setCode(self, newCode):
        self.code = newCode

    def getMainLanguageCode(self):
        return self.mainLanguageCode

    def setMainLanguageCode(self, newMainLanguageCode):
        self.mainLanguageCode = newMainLanguageCode

    def getLanguagesCode(self):
        return self.languagesCode

    def setLanguagesCode(self, newLanguagesCode):
        self.languagesCode = newLanguagesCode

    def getCurrency(self):
        return self.currency

    def setCurrency(self, newCurrency):
        self.currency = newCurrency

    def getCurrencySign(self):
        return self.currencySign

    def setCurrencySign(self, newCurrencySign):
        self.currencySign = newCurrencySign

    def getVatPercent(self):
        return self.vatPercent

    def setVatPercent(self, newVatPercent):
        self.vatPercent = newVatPercent

    def getTimeZoneId(self):
        return self.timeZoneId

    def setTimeZoneId(self, newTimeZoneId):
        self.timeZoneId = newTimeZoneId


# @package Kaltura
# @subpackage Client
class KalturaOTTUserType(KalturaObjectBase):
    """User type"""

    def __init__(self,
            id=NotImplemented,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # User type identifier
        # @var int
        # @readonly
        self.id = id

        # User type description
        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTUserType.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaOTTUserType")
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getId(self):
        return self.id

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaOTTUser(KalturaBaseOTTUser):
    """User"""

    def __init__(self,
            id=NotImplemented,
            username=NotImplemented,
            firstName=NotImplemented,
            lastName=NotImplemented,
            householdId=NotImplemented,
            email=NotImplemented,
            address=NotImplemented,
            city=NotImplemented,
            countryId=NotImplemented,
            zip=NotImplemented,
            phone=NotImplemented,
            affiliateCode=NotImplemented,
            externalId=NotImplemented,
            userType=NotImplemented,
            dynamicData=NotImplemented,
            isHouseholdMaster=NotImplemented,
            suspensionState=NotImplemented,
            userState=NotImplemented):
        KalturaBaseOTTUser.__init__(self,
            id,
            username,
            firstName,
            lastName)

        # Household identifier
        # @var int
        # @readonly
        self.householdId = householdId

        # Email
        # @var string
        self.email = email

        # Address
        # @var string
        self.address = address

        # City
        # @var string
        self.city = city

        # Country identifier
        # @var int
        self.countryId = countryId

        # Zip code
        # @var string
        self.zip = zip

        # Phone
        # @var string
        self.phone = phone

        # Affiliate code
        # @var string
        # @insertonly
        self.affiliateCode = affiliateCode

        # External user identifier
        # @var string
        self.externalId = externalId

        # User type
        # @var KalturaOTTUserType
        self.userType = userType

        # Dynamic data
        # @var map
        self.dynamicData = dynamicData

        # Is the user the household master
        # @var bool
        # @readonly
        self.isHouseholdMaster = isHouseholdMaster

        # Suspension state
        # @var KalturaHouseholdSuspensionState
        # @readonly
        self.suspensionState = suspensionState

        # User state
        # @var KalturaUserState
        # @readonly
        self.userState = userState


    PROPERTY_LOADERS = {
        'householdId': getXmlNodeInt, 
        'email': getXmlNodeText, 
        'address': getXmlNodeText, 
        'city': getXmlNodeText, 
        'countryId': getXmlNodeInt, 
        'zip': getXmlNodeText, 
        'phone': getXmlNodeText, 
        'affiliateCode': getXmlNodeText, 
        'externalId': getXmlNodeText, 
        'userType': (KalturaObjectFactory.create, 'KalturaOTTUserType'), 
        'dynamicData': (KalturaObjectFactory.createMap, 'KalturaStringValue'), 
        'isHouseholdMaster': getXmlNodeBool, 
        'suspensionState': (KalturaEnumsFactory.createString, "KalturaHouseholdSuspensionState"), 
        'userState': (KalturaEnumsFactory.createString, "KalturaUserState"), 
    }

    def fromXml(self, node):
        KalturaBaseOTTUser.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTUser.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseOTTUser.toParams(self)
        kparams.put("objectType", "KalturaOTTUser")
        kparams.addStringIfDefined("email", self.email)
        kparams.addStringIfDefined("address", self.address)
        kparams.addStringIfDefined("city", self.city)
        kparams.addIntIfDefined("countryId", self.countryId)
        kparams.addStringIfDefined("zip", self.zip)
        kparams.addStringIfDefined("phone", self.phone)
        kparams.addStringIfDefined("affiliateCode", self.affiliateCode)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addObjectIfDefined("userType", self.userType)
        kparams.addMapIfDefined("dynamicData", self.dynamicData)
        return kparams

    def getHouseholdId(self):
        return self.householdId

    def getEmail(self):
        return self.email

    def setEmail(self, newEmail):
        self.email = newEmail

    def getAddress(self):
        return self.address

    def setAddress(self, newAddress):
        self.address = newAddress

    def getCity(self):
        return self.city

    def setCity(self, newCity):
        self.city = newCity

    def getCountryId(self):
        return self.countryId

    def setCountryId(self, newCountryId):
        self.countryId = newCountryId

    def getZip(self):
        return self.zip

    def setZip(self, newZip):
        self.zip = newZip

    def getPhone(self):
        return self.phone

    def setPhone(self, newPhone):
        self.phone = newPhone

    def getAffiliateCode(self):
        return self.affiliateCode

    def setAffiliateCode(self, newAffiliateCode):
        self.affiliateCode = newAffiliateCode

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getUserType(self):
        return self.userType

    def setUserType(self, newUserType):
        self.userType = newUserType

    def getDynamicData(self):
        return self.dynamicData

    def setDynamicData(self, newDynamicData):
        self.dynamicData = newDynamicData

    def getIsHouseholdMaster(self):
        return self.isHouseholdMaster

    def getSuspensionState(self):
        return self.suspensionState

    def getUserState(self):
        return self.userState


# @package Kaltura
# @subpackage Client
class KalturaOTTUserListResponse(KalturaListResponse):
    """Users list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of users
        # @var array of KalturaOTTUser
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaOTTUser'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTUserListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaOTTUserListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaBaseChannel(KalturaObjectBase):
    """Slim channel"""

    def __init__(self,
            id=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier for the channel
        # @var int
        # @readonly
        self.id = id


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseChannel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseChannel")
        return kparams

    def getId(self):
        return self.id


# @package Kaltura
# @subpackage Client
class KalturaDiscountModule(KalturaObjectBase):
    """Discount module"""

    def __init__(self,
            percent=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The discount percentage
        # @var float
        self.percent = percent

        # The first date the discount is available
        # @var int
        self.startDate = startDate

        # The last date the discount is available
        # @var int
        self.endDate = endDate


    PROPERTY_LOADERS = {
        'percent': getXmlNodeFloat, 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDiscountModule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDiscountModule")
        kparams.addFloatIfDefined("percent", self.percent)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        return kparams

    def getPercent(self):
        return self.percent

    def setPercent(self, newPercent):
        self.percent = newPercent

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate


# @package Kaltura
# @subpackage Client
class KalturaUsageModule(KalturaObjectBase):
    """Pricing usage module"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            maxViewsNumber=NotImplemented,
            viewLifeCycle=NotImplemented,
            fullLifeCycle=NotImplemented,
            couponId=NotImplemented,
            waiverPeriod=NotImplemented,
            isWaiverEnabled=NotImplemented,
            isOfflinePlayback=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Usage module identifier
        # @var int
        # @readonly
        self.id = id

        # Usage module name
        # @var string
        # @readonly
        self.name = name

        # The maximum number of times an item in this usage module can be viewed
        # @var int
        # @readonly
        self.maxViewsNumber = maxViewsNumber

        # The amount time an item is available for viewing since a user started watching the item
        # @var int
        # @readonly
        self.viewLifeCycle = viewLifeCycle

        # The amount time an item is available for viewing
        # @var int
        # @readonly
        self.fullLifeCycle = fullLifeCycle

        # Identifies a specific coupon linked to this object
        # @var int
        # @readonly
        self.couponId = couponId

        # Time period during which the end user can waive his rights to cancel a purchase. When the time period is passed, the purchase can no longer be cancelled
        # @var int
        # @readonly
        self.waiverPeriod = waiverPeriod

        # Indicates whether or not the end user has the right to waive his rights to cancel a purchase
        # @var bool
        # @readonly
        self.isWaiverEnabled = isWaiverEnabled

        # Indicates that usage is targeted for offline playback
        # @var bool
        # @readonly
        self.isOfflinePlayback = isOfflinePlayback


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'maxViewsNumber': getXmlNodeInt, 
        'viewLifeCycle': getXmlNodeInt, 
        'fullLifeCycle': getXmlNodeInt, 
        'couponId': getXmlNodeInt, 
        'waiverPeriod': getXmlNodeInt, 
        'isWaiverEnabled': getXmlNodeBool, 
        'isOfflinePlayback': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUsageModule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUsageModule")
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getMaxViewsNumber(self):
        return self.maxViewsNumber

    def getViewLifeCycle(self):
        return self.viewLifeCycle

    def getFullLifeCycle(self):
        return self.fullLifeCycle

    def getCouponId(self):
        return self.couponId

    def getWaiverPeriod(self):
        return self.waiverPeriod

    def getIsWaiverEnabled(self):
        return self.isWaiverEnabled

    def getIsOfflinePlayback(self):
        return self.isOfflinePlayback


# @package Kaltura
# @subpackage Client
class KalturaCouponsGroup(KalturaObjectBase):
    """Coupons group details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            maxUsesNumber=NotImplemented,
            maxUsesNumberOnRenewableSub=NotImplemented,
            couponGroupType=NotImplemented,
            maxHouseholdUses=NotImplemented,
            discountId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Coupon group identifier
        # @var string
        # @readonly
        self.id = id

        # Coupon group name
        # @var string
        self.name = name

        # The first date the coupons in this coupons group are valid
        # @var int
        self.startDate = startDate

        # The last date the coupons in this coupons group are valid
        # @var int
        self.endDate = endDate

        # Maximum number of uses for each coupon in the group
        # @var int
        self.maxUsesNumber = maxUsesNumber

        # Maximum number of uses for each coupon in the group on a renewable subscription
        # @var int
        self.maxUsesNumberOnRenewableSub = maxUsesNumberOnRenewableSub

        # Type of the coupon group
        # @var KalturaCouponGroupType
        self.couponGroupType = couponGroupType

        # Maximum number of uses per household for each coupon in the group
        # @var int
        self.maxHouseholdUses = maxHouseholdUses

        # Discount ID
        # @var int
        self.discountId = discountId


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'maxUsesNumber': getXmlNodeInt, 
        'maxUsesNumberOnRenewableSub': getXmlNodeInt, 
        'couponGroupType': (KalturaEnumsFactory.createString, "KalturaCouponGroupType"), 
        'maxHouseholdUses': getXmlNodeInt, 
        'discountId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCouponsGroup.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCouponsGroup")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addIntIfDefined("maxUsesNumber", self.maxUsesNumber)
        kparams.addIntIfDefined("maxUsesNumberOnRenewableSub", self.maxUsesNumberOnRenewableSub)
        kparams.addStringEnumIfDefined("couponGroupType", self.couponGroupType)
        kparams.addIntIfDefined("maxHouseholdUses", self.maxHouseholdUses)
        kparams.addIntIfDefined("discountId", self.discountId)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getMaxUsesNumber(self):
        return self.maxUsesNumber

    def setMaxUsesNumber(self, newMaxUsesNumber):
        self.maxUsesNumber = newMaxUsesNumber

    def getMaxUsesNumberOnRenewableSub(self):
        return self.maxUsesNumberOnRenewableSub

    def setMaxUsesNumberOnRenewableSub(self, newMaxUsesNumberOnRenewableSub):
        self.maxUsesNumberOnRenewableSub = newMaxUsesNumberOnRenewableSub

    def getCouponGroupType(self):
        return self.couponGroupType

    def setCouponGroupType(self, newCouponGroupType):
        self.couponGroupType = newCouponGroupType

    def getMaxHouseholdUses(self):
        return self.maxHouseholdUses

    def setMaxHouseholdUses(self, newMaxHouseholdUses):
        self.maxHouseholdUses = newMaxHouseholdUses

    def getDiscountId(self):
        return self.discountId

    def setDiscountId(self, newDiscountId):
        self.discountId = newDiscountId


# @package Kaltura
# @subpackage Client
class KalturaProductCode(KalturaObjectBase):
    """Product Code"""

    def __init__(self,
            inappProvider=NotImplemented,
            code=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Provider Name
        # @var string
        self.inappProvider = inappProvider

        # Product Code
        # @var string
        self.code = code


    PROPERTY_LOADERS = {
        'inappProvider': getXmlNodeText, 
        'code': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductCode.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaProductCode")
        kparams.addStringIfDefined("inappProvider", self.inappProvider)
        kparams.addStringIfDefined("code", self.code)
        return kparams

    def getInappProvider(self):
        return self.inappProvider

    def setInappProvider(self, newInappProvider):
        self.inappProvider = newInappProvider

    def getCode(self):
        return self.code

    def setCode(self, newCode):
        self.code = newCode


# @package Kaltura
# @subpackage Client
class KalturaCollection(KalturaObjectBase):
    """Collection"""

    def __init__(self,
            id=NotImplemented,
            channels=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            discountModule=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            usageModule=NotImplemented,
            couponsGroups=NotImplemented,
            externalId=NotImplemented,
            productCodes=NotImplemented,
            priceDetailsId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Collection identifier
        # @var string
        self.id = id

        # A list of channels associated with this collection
        # @var array of KalturaBaseChannel
        self.channels = channels

        # The first date the collection is available for purchasing
        # @var int
        self.startDate = startDate

        # The last date the collection is available for purchasing
        # @var int
        self.endDate = endDate

        # The internal discount module for the subscription
        # @var KalturaDiscountModule
        self.discountModule = discountModule

        # Name of the subscription
        # @var string
        # @readonly
        self.name = name

        # Name of the subscription
        # @var array of KalturaTranslationToken
        self.multilingualName = multilingualName

        # description of the subscription
        # @var string
        # @readonly
        self.description = description

        # description of the subscription
        # @var array of KalturaTranslationToken
        self.multilingualDescription = multilingualDescription

        # Collection usage module
        # @var KalturaUsageModule
        self.usageModule = usageModule

        # List of Coupons group
        # @var array of KalturaCouponsGroup
        self.couponsGroups = couponsGroups

        # External ID
        # @var string
        self.externalId = externalId

        # List of Collection product codes
        # @var array of KalturaProductCode
        self.productCodes = productCodes

        # The ID of the price details associated with this collection
        # @var int
        self.priceDetailsId = priceDetailsId


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'channels': (KalturaObjectFactory.createArray, 'KalturaBaseChannel'), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'discountModule': (KalturaObjectFactory.create, 'KalturaDiscountModule'), 
        'name': getXmlNodeText, 
        'multilingualName': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'description': getXmlNodeText, 
        'multilingualDescription': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'usageModule': (KalturaObjectFactory.create, 'KalturaUsageModule'), 
        'couponsGroups': (KalturaObjectFactory.createArray, 'KalturaCouponsGroup'), 
        'externalId': getXmlNodeText, 
        'productCodes': (KalturaObjectFactory.createArray, 'KalturaProductCode'), 
        'priceDetailsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCollection.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCollection")
        kparams.addStringIfDefined("id", self.id)
        kparams.addArrayIfDefined("channels", self.channels)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addObjectIfDefined("discountModule", self.discountModule)
        kparams.addArrayIfDefined("multilingualName", self.multilingualName)
        kparams.addArrayIfDefined("multilingualDescription", self.multilingualDescription)
        kparams.addObjectIfDefined("usageModule", self.usageModule)
        kparams.addArrayIfDefined("couponsGroups", self.couponsGroups)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addArrayIfDefined("productCodes", self.productCodes)
        kparams.addIntIfDefined("priceDetailsId", self.priceDetailsId)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getChannels(self):
        return self.channels

    def setChannels(self, newChannels):
        self.channels = newChannels

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getDiscountModule(self):
        return self.discountModule

    def setDiscountModule(self, newDiscountModule):
        self.discountModule = newDiscountModule

    def getName(self):
        return self.name

    def getMultilingualName(self):
        return self.multilingualName

    def setMultilingualName(self, newMultilingualName):
        self.multilingualName = newMultilingualName

    def getDescription(self):
        return self.description

    def getMultilingualDescription(self):
        return self.multilingualDescription

    def setMultilingualDescription(self, newMultilingualDescription):
        self.multilingualDescription = newMultilingualDescription

    def getUsageModule(self):
        return self.usageModule

    def setUsageModule(self, newUsageModule):
        self.usageModule = newUsageModule

    def getCouponsGroups(self):
        return self.couponsGroups

    def setCouponsGroups(self, newCouponsGroups):
        self.couponsGroups = newCouponsGroups

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getProductCodes(self):
        return self.productCodes

    def setProductCodes(self, newProductCodes):
        self.productCodes = newProductCodes

    def getPriceDetailsId(self):
        return self.priceDetailsId

    def setPriceDetailsId(self, newPriceDetailsId):
        self.priceDetailsId = newPriceDetailsId


# @package Kaltura
# @subpackage Client
class KalturaCollectionListResponse(KalturaListResponse):
    """Collections list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of collections
        # @var array of KalturaCollection
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaCollection'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCollectionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCollectionListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetGroupBy(KalturaObjectBase):
    """Abstarct class - represents an asset parameter that can be used for grouping"""

    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetGroupBy.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetGroupBy")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaDynamicOrderBy(KalturaObjectBase):
    """Kaltura Asset Order"""

    def __init__(self,
            name=NotImplemented,
            orderBy=NotImplemented):
        KalturaObjectBase.__init__(self)

        # order by name
        # @var string
        self.name = name

        # order by meta asc/desc
        # @var KalturaMetaTagOrderBy
        self.orderBy = orderBy


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'orderBy': (KalturaEnumsFactory.createString, "KalturaMetaTagOrderBy"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDynamicOrderBy.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDynamicOrderBy")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringEnumIfDefined("orderBy", self.orderBy)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy


# @package Kaltura
# @subpackage Client
class KalturaChannelOrder(KalturaObjectBase):
    """Channel order details"""

    def __init__(self,
            dynamicOrderBy=NotImplemented,
            orderBy=NotImplemented,
            period=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Channel dynamic order by (meta)
        # @var KalturaDynamicOrderBy
        self.dynamicOrderBy = dynamicOrderBy

        # Channel order by
        # @var KalturaChannelOrderBy
        self.orderBy = orderBy

        # Sliding window period in minutes, used only when ordering by LIKES_DESC / VOTES_DESC / RATINGS_DESC / VIEWS_DESC
        # @var int
        self.period = period


    PROPERTY_LOADERS = {
        'dynamicOrderBy': (KalturaObjectFactory.create, 'KalturaDynamicOrderBy'), 
        'orderBy': (KalturaEnumsFactory.createString, "KalturaChannelOrderBy"), 
        'period': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelOrder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaChannelOrder")
        kparams.addObjectIfDefined("dynamicOrderBy", self.dynamicOrderBy)
        kparams.addStringEnumIfDefined("orderBy", self.orderBy)
        kparams.addIntIfDefined("period", self.period)
        return kparams

    def getDynamicOrderBy(self):
        return self.dynamicOrderBy

    def setDynamicOrderBy(self, newDynamicOrderBy):
        self.dynamicOrderBy = newDynamicOrderBy

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy

    def getPeriod(self):
        return self.period

    def setPeriod(self, newPeriod):
        self.period = newPeriod


# @package Kaltura
# @subpackage Client
class KalturaChannel(KalturaBaseChannel):
    """Channel details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            isActive=NotImplemented,
            orderBy=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented):
        KalturaBaseChannel.__init__(self,
            id)

        # Channel name
        # @var string
        # @readonly
        self.name = name

        # Channel name
        # @var array of KalturaTranslationToken
        self.multilingualName = multilingualName

        # Channel system name
        # @var string
        self.systemName = systemName

        # Cannel description
        # @var string
        # @readonly
        self.description = description

        # Cannel description
        # @var array of KalturaTranslationToken
        self.multilingualDescription = multilingualDescription

        # active status
        # @var bool
        self.isActive = isActive

        # Channel order by
        # @var KalturaChannelOrder
        self.orderBy = orderBy

        # Specifies when was the Channel was created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the Channel last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'multilingualName': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'systemName': getXmlNodeText, 
        'description': getXmlNodeText, 
        'multilingualDescription': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'isActive': getXmlNodeBool, 
        'orderBy': (KalturaObjectFactory.create, 'KalturaChannelOrder'), 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaBaseChannel.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseChannel.toParams(self)
        kparams.put("objectType", "KalturaChannel")
        kparams.addArrayIfDefined("multilingualName", self.multilingualName)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addArrayIfDefined("multilingualDescription", self.multilingualDescription)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addObjectIfDefined("orderBy", self.orderBy)
        return kparams

    def getName(self):
        return self.name

    def getMultilingualName(self):
        return self.multilingualName

    def setMultilingualName(self, newMultilingualName):
        self.multilingualName = newMultilingualName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getDescription(self):
        return self.description

    def getMultilingualDescription(self):
        return self.multilingualDescription

    def setMultilingualDescription(self, newMultilingualDescription):
        self.multilingualDescription = newMultilingualDescription

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate


# @package Kaltura
# @subpackage Client
class KalturaDynamicChannel(KalturaChannel):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            isActive=NotImplemented,
            orderBy=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            kSql=NotImplemented,
            assetTypes=NotImplemented,
            groupBy=NotImplemented):
        KalturaChannel.__init__(self,
            id,
            name,
            multilingualName,
            systemName,
            description,
            multilingualDescription,
            isActive,
            orderBy,
            createDate,
            updateDate)

        # Search assets using dynamic criteria. Provided collection of nested expressions with key, comparison operators, value, and logical conjunction.
        #             Possible keys: any Tag or Meta defined in the system and the following reserved keys: start_date, end_date. 
        #             epg_id, media_id - for specific asset IDs.
        #             geo_block - only valid value is &quot;true&quot;: When enabled, only assets that are not restriced to the user by geo-block rules will return.
        #             parental_rules - only valid value is &quot;true&quot;: When enabled, only assets that the user doesn&#39;t need to provide PIN code will return.
        #             user_interests - only valid value is &quot;true&quot;. When enabled, only assets that the user defined as his interests (by tags and metas) will return.
        #             epg_channel_id - the channel identifier of the EPG program. *****Deprecated, please use linear_media_id instead*****
        #             linear_media_id - the linear media identifier of the EPG program.
        #             entitled_assets - valid values: &quot;free&quot;, &quot;entitled&quot;, &quot;both&quot;. free - gets only free to watch assets. entitled - only those that the user is implicitly entitled to watch.
        #             Comparison operators: for numerical fields =, &gt;, &gt;=, &lt;, &lt;=, : (in). 
        #             For alpha-numerical fields =, != (not), ~ (like), !~, ^ (any word starts with), ^= (phrase starts with), + (exists), !+ (not exists).
        #             Logical conjunction: and, or. 
        #             Search values are limited to 20 characters each.
        #             (maximum length of entire filter is 2048 characters)
        # @var string
        self.kSql = kSql

        # Asset types in the channel.
        #             -26 is EPG
        # @var array of KalturaIntegerValue
        self.assetTypes = assetTypes

        # Channel group by
        # @var KalturaAssetGroupBy
        self.groupBy = groupBy


    PROPERTY_LOADERS = {
        'kSql': getXmlNodeText, 
        'assetTypes': (KalturaObjectFactory.createArray, 'KalturaIntegerValue'), 
        'groupBy': (KalturaObjectFactory.create, 'KalturaAssetGroupBy'), 
    }

    def fromXml(self, node):
        KalturaChannel.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDynamicChannel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaChannel.toParams(self)
        kparams.put("objectType", "KalturaDynamicChannel")
        kparams.addStringIfDefined("kSql", self.kSql)
        kparams.addArrayIfDefined("assetTypes", self.assetTypes)
        kparams.addObjectIfDefined("groupBy", self.groupBy)
        return kparams

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql

    def getAssetTypes(self):
        return self.assetTypes

    def setAssetTypes(self, newAssetTypes):
        self.assetTypes = newAssetTypes

    def getGroupBy(self):
        return self.groupBy

    def setGroupBy(self, newGroupBy):
        self.groupBy = newGroupBy


# @package Kaltura
# @subpackage Client
class KalturaManualChannel(KalturaChannel):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            systemName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            isActive=NotImplemented,
            orderBy=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            mediaIds=NotImplemented):
        KalturaChannel.__init__(self,
            id,
            name,
            multilingualName,
            systemName,
            description,
            multilingualDescription,
            isActive,
            orderBy,
            createDate,
            updateDate)

        # A list of comma separated media ids associated with this channel, according to the order of the medias in the channel.
        # @var string
        self.mediaIds = mediaIds


    PROPERTY_LOADERS = {
        'mediaIds': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaChannel.fromXml(self, node)
        self.fromXmlImpl(node, KalturaManualChannel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaChannel.toParams(self)
        kparams.put("objectType", "KalturaManualChannel")
        kparams.addStringIfDefined("mediaIds", self.mediaIds)
        return kparams

    def getMediaIds(self):
        return self.mediaIds

    def setMediaIds(self, newMediaIds):
        self.mediaIds = newMediaIds


# @package Kaltura
# @subpackage Client
class KalturaAssetMetaOrTagGroupBy(KalturaAssetGroupBy):
    """Group by a tag or meta - according to the name that appears in the system (similar to KSQL)"""

    def __init__(self,
            value=NotImplemented):
        KalturaAssetGroupBy.__init__(self)

        # Group by a tag or meta - according to the name that appears in the system (similar to KSQL)
        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetGroupBy.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetMetaOrTagGroupBy.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetGroupBy.toParams(self)
        kparams.put("objectType", "KalturaAssetMetaOrTagGroupBy")
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaAssetFieldGroupBy(KalturaAssetGroupBy):
    """Group by a field that is defined in enum"""

    def __init__(self,
            value=NotImplemented):
        KalturaAssetGroupBy.__init__(self)

        # Group by a specific field that is defined in enum
        # @var KalturaGroupByField
        self.value = value


    PROPERTY_LOADERS = {
        'value': (KalturaEnumsFactory.createString, "KalturaGroupByField"), 
    }

    def fromXml(self, node):
        KalturaAssetGroupBy.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetFieldGroupBy.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetGroupBy.toParams(self)
        kparams.put("objectType", "KalturaAssetFieldGroupBy")
        kparams.addStringEnumIfDefined("value", self.value)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaPricePlan(KalturaUsageModule):
    """Price plan"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            maxViewsNumber=NotImplemented,
            viewLifeCycle=NotImplemented,
            fullLifeCycle=NotImplemented,
            couponId=NotImplemented,
            waiverPeriod=NotImplemented,
            isWaiverEnabled=NotImplemented,
            isOfflinePlayback=NotImplemented,
            isRenewable=NotImplemented,
            renewalsNumber=NotImplemented,
            discountId=NotImplemented,
            priceDetailsId=NotImplemented):
        KalturaUsageModule.__init__(self,
            id,
            name,
            maxViewsNumber,
            viewLifeCycle,
            fullLifeCycle,
            couponId,
            waiverPeriod,
            isWaiverEnabled,
            isOfflinePlayback)

        # Denotes whether or not this object can be renewed
        # @var bool
        # @readonly
        self.isRenewable = isRenewable

        # Defines the number of times the module will be renewed (for the life_cycle period)
        # @var int
        # @readonly
        self.renewalsNumber = renewalsNumber

        # The discount module identifier of the price plan
        # @var int
        # @readonly
        self.discountId = discountId

        # The ID of the price details associated with this price plan
        # @var int
        self.priceDetailsId = priceDetailsId


    PROPERTY_LOADERS = {
        'isRenewable': getXmlNodeBool, 
        'renewalsNumber': getXmlNodeInt, 
        'discountId': getXmlNodeInt, 
        'priceDetailsId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaUsageModule.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPricePlan.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaUsageModule.toParams(self)
        kparams.put("objectType", "KalturaPricePlan")
        kparams.addIntIfDefined("priceDetailsId", self.priceDetailsId)
        return kparams

    def getIsRenewable(self):
        return self.isRenewable

    def getRenewalsNumber(self):
        return self.renewalsNumber

    def getDiscountId(self):
        return self.discountId

    def getPriceDetailsId(self):
        return self.priceDetailsId

    def setPriceDetailsId(self, newPriceDetailsId):
        self.priceDetailsId = newPriceDetailsId


# @package Kaltura
# @subpackage Client
class KalturaPrice(KalturaObjectBase):
    """Price"""

    def __init__(self,
            amount=NotImplemented,
            currency=NotImplemented,
            currencySign=NotImplemented,
            countryId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Price
        # @var float
        self.amount = amount

        # Currency
        # @var string
        self.currency = currency

        # Currency Sign
        # @var string
        self.currencySign = currencySign

        # Country ID
        # @var int
        self.countryId = countryId


    PROPERTY_LOADERS = {
        'amount': getXmlNodeFloat, 
        'currency': getXmlNodeText, 
        'currencySign': getXmlNodeText, 
        'countryId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPrice")
        kparams.addFloatIfDefined("amount", self.amount)
        kparams.addStringIfDefined("currency", self.currency)
        kparams.addStringIfDefined("currencySign", self.currencySign)
        kparams.addIntIfDefined("countryId", self.countryId)
        return kparams

    def getAmount(self):
        return self.amount

    def setAmount(self, newAmount):
        self.amount = newAmount

    def getCurrency(self):
        return self.currency

    def setCurrency(self, newCurrency):
        self.currency = newCurrency

    def getCurrencySign(self):
        return self.currencySign

    def setCurrencySign(self, newCurrencySign):
        self.currencySign = newCurrencySign

    def getCountryId(self):
        return self.countryId

    def setCountryId(self, newCountryId):
        self.countryId = newCountryId


# @package Kaltura
# @subpackage Client
class KalturaDiscount(KalturaPrice):
    """Discount"""

    def __init__(self,
            amount=NotImplemented,
            currency=NotImplemented,
            currencySign=NotImplemented,
            countryId=NotImplemented,
            percentage=NotImplemented):
        KalturaPrice.__init__(self,
            amount,
            currency,
            currencySign,
            countryId)

        # The discount percentage
        # @var int
        # @readonly
        self.percentage = percentage


    PROPERTY_LOADERS = {
        'percentage': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaPrice.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDiscount.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPrice.toParams(self)
        kparams.put("objectType", "KalturaDiscount")
        return kparams

    def getPercentage(self):
        return self.percentage


# @package Kaltura
# @subpackage Client
class KalturaDiscountDetails(KalturaObjectBase):
    """Discount details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            multiCurrencyDiscount=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The discount ID
        # @var int
        # @readonly
        self.id = id

        # The price code name
        # @var string
        self.name = name

        # Multi currency discounts for all countries and currencies
        # @var array of KalturaDiscount
        self.multiCurrencyDiscount = multiCurrencyDiscount

        # Start date represented as epoch
        # @var int
        self.startDate = startDate

        # End date represented as epoch
        # @var int
        self.endDate = endDate


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'multiCurrencyDiscount': (KalturaObjectFactory.createArray, 'KalturaDiscount'), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDiscountDetails.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDiscountDetails")
        kparams.addStringIfDefined("name", self.name)
        kparams.addArrayIfDefined("multiCurrencyDiscount", self.multiCurrencyDiscount)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getMultiCurrencyDiscount(self):
        return self.multiCurrencyDiscount

    def setMultiCurrencyDiscount(self, newMultiCurrencyDiscount):
        self.multiCurrencyDiscount = newMultiCurrencyDiscount

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate


# @package Kaltura
# @subpackage Client
class KalturaDiscountDetailsListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of price details
        # @var array of KalturaDiscountDetails
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaDiscountDetails'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDiscountDetailsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaDiscountDetailsListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionSet(KalturaObjectBase):
    """Subscription details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            type=NotImplemented,
            subscriptionIds=NotImplemented):
        KalturaObjectBase.__init__(self)

        # SubscriptionSet identifier
        # @var int
        # @readonly
        self.id = id

        # SubscriptionSet name
        # @var string
        self.name = name

        # Type of the Subscription Set
        # @var KalturaSubscriptionSetType
        # @readonly
        self.type = type

        # A list of comma separated subscription ids associated with this set ordered by priority ascending
        # @var string
        self.subscriptionIds = subscriptionIds


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createString, "KalturaSubscriptionSetType"), 
        'subscriptionIds': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionSet.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionSet")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("subscriptionIds", self.subscriptionIds)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getType(self):
        return self.type

    def getSubscriptionIds(self):
        return self.subscriptionIds

    def setSubscriptionIds(self, newSubscriptionIds):
        self.subscriptionIds = newSubscriptionIds


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionSetListResponse(KalturaListResponse):
    """SubscriptionSets list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of subscriptionSets
        # @var array of KalturaSubscriptionSet
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSubscriptionSet'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionSetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionSetListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionDependencySet(KalturaSubscriptionSet):
    """Subscription Dependency Set"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            type=NotImplemented,
            subscriptionIds=NotImplemented,
            baseSubscriptionId=NotImplemented):
        KalturaSubscriptionSet.__init__(self,
            id,
            name,
            type,
            subscriptionIds)

        # Base Subscription identifier
        # @var int
        self.baseSubscriptionId = baseSubscriptionId


    PROPERTY_LOADERS = {
        'baseSubscriptionId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaSubscriptionSet.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionDependencySet.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSubscriptionSet.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionDependencySet")
        kparams.addIntIfDefined("baseSubscriptionId", self.baseSubscriptionId)
        return kparams

    def getBaseSubscriptionId(self):
        return self.baseSubscriptionId

    def setBaseSubscriptionId(self, newBaseSubscriptionId):
        self.baseSubscriptionId = newBaseSubscriptionId


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionSwitchSet(KalturaSubscriptionSet):
    """Subscription details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            type=NotImplemented,
            subscriptionIds=NotImplemented):
        KalturaSubscriptionSet.__init__(self,
            id,
            name,
            type,
            subscriptionIds)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaSubscriptionSet.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionSwitchSet.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSubscriptionSet.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionSwitchSet")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaProductPrice(KalturaObjectBase):
    def __init__(self,
            productId=NotImplemented,
            productType=NotImplemented,
            price=NotImplemented,
            purchaseStatus=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Product identifier
        # @var string
        self.productId = productId

        # Product Type
        # @var KalturaTransactionType
        self.productType = productType

        # Product price
        # @var KalturaPrice
        self.price = price

        # Product purchase status
        # @var KalturaPurchaseStatus
        self.purchaseStatus = purchaseStatus


    PROPERTY_LOADERS = {
        'productId': getXmlNodeText, 
        'productType': (KalturaEnumsFactory.createString, "KalturaTransactionType"), 
        'price': (KalturaObjectFactory.create, 'KalturaPrice'), 
        'purchaseStatus': (KalturaEnumsFactory.createString, "KalturaPurchaseStatus"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaProductPrice")
        kparams.addStringIfDefined("productId", self.productId)
        kparams.addStringEnumIfDefined("productType", self.productType)
        kparams.addObjectIfDefined("price", self.price)
        kparams.addStringEnumIfDefined("purchaseStatus", self.purchaseStatus)
        return kparams

    def getProductId(self):
        return self.productId

    def setProductId(self, newProductId):
        self.productId = newProductId

    def getProductType(self):
        return self.productType

    def setProductType(self, newProductType):
        self.productType = newProductType

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getPurchaseStatus(self):
        return self.purchaseStatus

    def setPurchaseStatus(self, newPurchaseStatus):
        self.purchaseStatus = newPurchaseStatus


# @package Kaltura
# @subpackage Client
class KalturaProductPriceListResponse(KalturaListResponse):
    """Prices list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of prices
        # @var array of KalturaProductPrice
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaProductPrice'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductPriceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaProductPriceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaCollectionPrice(KalturaProductPrice):
    """Collection price details"""

    def __init__(self,
            productId=NotImplemented,
            productType=NotImplemented,
            price=NotImplemented,
            purchaseStatus=NotImplemented):
        KalturaProductPrice.__init__(self,
            productId,
            productType,
            price,
            purchaseStatus)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaProductPrice.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCollectionPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaProductPrice.toParams(self)
        kparams.put("objectType", "KalturaCollectionPrice")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPpvPrice(KalturaProductPrice):
    """PPV price details"""

    def __init__(self,
            productId=NotImplemented,
            productType=NotImplemented,
            price=NotImplemented,
            purchaseStatus=NotImplemented,
            fileId=NotImplemented,
            ppvModuleId=NotImplemented,
            isSubscriptionOnly=NotImplemented,
            fullPrice=NotImplemented,
            subscriptionId=NotImplemented,
            collectionId=NotImplemented,
            prePaidId=NotImplemented,
            ppvDescriptions=NotImplemented,
            purchaseUserId=NotImplemented,
            purchasedMediaFileId=NotImplemented,
            relatedMediaFileIds=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            discountEndDate=NotImplemented,
            firstDeviceName=NotImplemented,
            isInCancelationPeriod=NotImplemented,
            ppvProductCode=NotImplemented):
        KalturaProductPrice.__init__(self,
            productId,
            productType,
            price,
            purchaseStatus)

        # Media file identifier
        # @var int
        self.fileId = fileId

        # The associated PPV module identifier
        # @var string
        self.ppvModuleId = ppvModuleId

        # Denotes whether this object is available only as part of a subscription or can be sold separately
        # @var bool
        self.isSubscriptionOnly = isSubscriptionOnly

        # The full price of the item (with no discounts)
        # @var KalturaPrice
        self.fullPrice = fullPrice

        # The identifier of the relevant subscription
        # @var string
        self.subscriptionId = subscriptionId

        # The identifier of the relevant collection
        # @var string
        self.collectionId = collectionId

        # The identifier of the relevant pre paid
        # @var string
        self.prePaidId = prePaidId

        # A list of the descriptions of the PPV module on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.ppvDescriptions = ppvDescriptions

        # If the item already purchased - the identifier of the user (in the household) who purchased this item
        # @var string
        self.purchaseUserId = purchaseUserId

        # If the item already purchased - the identifier of the purchased file
        # @var int
        self.purchasedMediaFileId = purchasedMediaFileId

        # Related media files identifiers (different types)
        # @var array of KalturaIntegerValue
        self.relatedMediaFileIds = relatedMediaFileIds

        # If the item already purchased - since when the user can start watching the item
        # @var int
        self.startDate = startDate

        # If the item already purchased - until when the user can watch the item
        # @var int
        self.endDate = endDate

        # Discount end date
        # @var int
        self.discountEndDate = discountEndDate

        # If the item already purchased and played - the name of the device on which it was first played
        # @var string
        self.firstDeviceName = firstDeviceName

        # If waiver period is enabled - donates whether the user is still in the cancelation window
        # @var bool
        self.isInCancelationPeriod = isInCancelationPeriod

        # The PPV product code
        # @var string
        self.ppvProductCode = ppvProductCode


    PROPERTY_LOADERS = {
        'fileId': getXmlNodeInt, 
        'ppvModuleId': getXmlNodeText, 
        'isSubscriptionOnly': getXmlNodeBool, 
        'fullPrice': (KalturaObjectFactory.create, 'KalturaPrice'), 
        'subscriptionId': getXmlNodeText, 
        'collectionId': getXmlNodeText, 
        'prePaidId': getXmlNodeText, 
        'ppvDescriptions': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'purchaseUserId': getXmlNodeText, 
        'purchasedMediaFileId': getXmlNodeInt, 
        'relatedMediaFileIds': (KalturaObjectFactory.createArray, 'KalturaIntegerValue'), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'discountEndDate': getXmlNodeInt, 
        'firstDeviceName': getXmlNodeText, 
        'isInCancelationPeriod': getXmlNodeBool, 
        'ppvProductCode': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaProductPrice.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPpvPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaProductPrice.toParams(self)
        kparams.put("objectType", "KalturaPpvPrice")
        kparams.addIntIfDefined("fileId", self.fileId)
        kparams.addStringIfDefined("ppvModuleId", self.ppvModuleId)
        kparams.addBoolIfDefined("isSubscriptionOnly", self.isSubscriptionOnly)
        kparams.addObjectIfDefined("fullPrice", self.fullPrice)
        kparams.addStringIfDefined("subscriptionId", self.subscriptionId)
        kparams.addStringIfDefined("collectionId", self.collectionId)
        kparams.addStringIfDefined("prePaidId", self.prePaidId)
        kparams.addArrayIfDefined("ppvDescriptions", self.ppvDescriptions)
        kparams.addStringIfDefined("purchaseUserId", self.purchaseUserId)
        kparams.addIntIfDefined("purchasedMediaFileId", self.purchasedMediaFileId)
        kparams.addArrayIfDefined("relatedMediaFileIds", self.relatedMediaFileIds)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addIntIfDefined("discountEndDate", self.discountEndDate)
        kparams.addStringIfDefined("firstDeviceName", self.firstDeviceName)
        kparams.addBoolIfDefined("isInCancelationPeriod", self.isInCancelationPeriod)
        kparams.addStringIfDefined("ppvProductCode", self.ppvProductCode)
        return kparams

    def getFileId(self):
        return self.fileId

    def setFileId(self, newFileId):
        self.fileId = newFileId

    def getPpvModuleId(self):
        return self.ppvModuleId

    def setPpvModuleId(self, newPpvModuleId):
        self.ppvModuleId = newPpvModuleId

    def getIsSubscriptionOnly(self):
        return self.isSubscriptionOnly

    def setIsSubscriptionOnly(self, newIsSubscriptionOnly):
        self.isSubscriptionOnly = newIsSubscriptionOnly

    def getFullPrice(self):
        return self.fullPrice

    def setFullPrice(self, newFullPrice):
        self.fullPrice = newFullPrice

    def getSubscriptionId(self):
        return self.subscriptionId

    def setSubscriptionId(self, newSubscriptionId):
        self.subscriptionId = newSubscriptionId

    def getCollectionId(self):
        return self.collectionId

    def setCollectionId(self, newCollectionId):
        self.collectionId = newCollectionId

    def getPrePaidId(self):
        return self.prePaidId

    def setPrePaidId(self, newPrePaidId):
        self.prePaidId = newPrePaidId

    def getPpvDescriptions(self):
        return self.ppvDescriptions

    def setPpvDescriptions(self, newPpvDescriptions):
        self.ppvDescriptions = newPpvDescriptions

    def getPurchaseUserId(self):
        return self.purchaseUserId

    def setPurchaseUserId(self, newPurchaseUserId):
        self.purchaseUserId = newPurchaseUserId

    def getPurchasedMediaFileId(self):
        return self.purchasedMediaFileId

    def setPurchasedMediaFileId(self, newPurchasedMediaFileId):
        self.purchasedMediaFileId = newPurchasedMediaFileId

    def getRelatedMediaFileIds(self):
        return self.relatedMediaFileIds

    def setRelatedMediaFileIds(self, newRelatedMediaFileIds):
        self.relatedMediaFileIds = newRelatedMediaFileIds

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getDiscountEndDate(self):
        return self.discountEndDate

    def setDiscountEndDate(self, newDiscountEndDate):
        self.discountEndDate = newDiscountEndDate

    def getFirstDeviceName(self):
        return self.firstDeviceName

    def setFirstDeviceName(self, newFirstDeviceName):
        self.firstDeviceName = newFirstDeviceName

    def getIsInCancelationPeriod(self):
        return self.isInCancelationPeriod

    def setIsInCancelationPeriod(self, newIsInCancelationPeriod):
        self.isInCancelationPeriod = newIsInCancelationPeriod

    def getPpvProductCode(self):
        return self.ppvProductCode

    def setPpvProductCode(self, newPpvProductCode):
        self.ppvProductCode = newPpvProductCode


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionPrice(KalturaProductPrice):
    """Subscription price details"""

    def __init__(self,
            productId=NotImplemented,
            productType=NotImplemented,
            price=NotImplemented,
            purchaseStatus=NotImplemented,
            endDate=NotImplemented):
        KalturaProductPrice.__init__(self,
            productId,
            productType,
            price,
            purchaseStatus)

        # If the item related to unified billing cycle purchased - until when the this price is relevant
        # @var int
        self.endDate = endDate


    PROPERTY_LOADERS = {
        'endDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaProductPrice.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionPrice.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaProductPrice.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionPrice")
        kparams.addIntIfDefined("endDate", self.endDate)
        return kparams

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate


# @package Kaltura
# @subpackage Client
class KalturaCouponsGroupListResponse(KalturaListResponse):
    """Coupons group list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of coupons groups
        # @var array of KalturaCouponsGroup
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaCouponsGroup'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCouponsGroupListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCouponsGroupListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPriceDetails(KalturaObjectBase):
    """Price details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            price=NotImplemented,
            multiCurrencyPrice=NotImplemented,
            descriptions=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The price code identifier
        # @var int
        # @readonly
        self.id = id

        # The price code name
        # @var string
        self.name = name

        # The price
        # @var KalturaPrice
        # @readonly
        self.price = price

        # Multi currency prices for all countries and currencies
        # @var array of KalturaPrice
        self.multiCurrencyPrice = multiCurrencyPrice

        # A list of the descriptions for this price on different languages (language code and translation)
        # @var array of KalturaTranslationToken
        self.descriptions = descriptions


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'price': (KalturaObjectFactory.create, 'KalturaPrice'), 
        'multiCurrencyPrice': (KalturaObjectFactory.createArray, 'KalturaPrice'), 
        'descriptions': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPriceDetails.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPriceDetails")
        kparams.addStringIfDefined("name", self.name)
        kparams.addArrayIfDefined("multiCurrencyPrice", self.multiCurrencyPrice)
        kparams.addArrayIfDefined("descriptions", self.descriptions)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPrice(self):
        return self.price

    def getMultiCurrencyPrice(self):
        return self.multiCurrencyPrice

    def setMultiCurrencyPrice(self, newMultiCurrencyPrice):
        self.multiCurrencyPrice = newMultiCurrencyPrice

    def getDescriptions(self):
        return self.descriptions

    def setDescriptions(self, newDescriptions):
        self.descriptions = newDescriptions


# @package Kaltura
# @subpackage Client
class KalturaPriceDetailsListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of price details
        # @var array of KalturaPriceDetails
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaPriceDetails'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPriceDetailsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPriceDetailsListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPricePlanListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of price plans
        # @var array of KalturaPricePlan
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaPricePlan'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPricePlanListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPricePlanListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPreviewModule(KalturaObjectBase):
    """Preview module"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            lifeCycle=NotImplemented,
            nonRenewablePeriod=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Preview module identifier
        # @var int
        # @readonly
        self.id = id

        # Preview module name
        # @var string
        self.name = name

        # Preview module life cycle - for how long the preview module is active
        # @var int
        self.lifeCycle = lifeCycle

        # The time you can&#39;t buy the item to which the preview module is assigned to again
        # @var int
        self.nonRenewablePeriod = nonRenewablePeriod


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'lifeCycle': getXmlNodeInt, 
        'nonRenewablePeriod': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPreviewModule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPreviewModule")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("lifeCycle", self.lifeCycle)
        kparams.addIntIfDefined("nonRenewablePeriod", self.nonRenewablePeriod)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getLifeCycle(self):
        return self.lifeCycle

    def setLifeCycle(self, newLifeCycle):
        self.lifeCycle = newLifeCycle

    def getNonRenewablePeriod(self):
        return self.nonRenewablePeriod

    def setNonRenewablePeriod(self, newNonRenewablePeriod):
        self.nonRenewablePeriod = newNonRenewablePeriod


# @package Kaltura
# @subpackage Client
class KalturaPremiumService(KalturaObjectBase):
    """Premium service"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Service identifier
        # @var int
        # @readonly
        self.id = id

        # Service name / description
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPremiumService.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPremiumService")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaSubscription(KalturaObjectBase):
    """Subscription details"""

    def __init__(self,
            id=NotImplemented,
            channels=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            fileTypes=NotImplemented,
            isRenewable=NotImplemented,
            renewalsNumber=NotImplemented,
            isInfiniteRenewal=NotImplemented,
            price=NotImplemented,
            discountModule=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            mediaId=NotImplemented,
            prorityInOrder=NotImplemented,
            pricePlanIds=NotImplemented,
            previewModule=NotImplemented,
            householdLimitationsId=NotImplemented,
            gracePeriodMinutes=NotImplemented,
            premiumServices=NotImplemented,
            maxViewsNumber=NotImplemented,
            viewLifeCycle=NotImplemented,
            waiverPeriod=NotImplemented,
            isWaiverEnabled=NotImplemented,
            userTypes=NotImplemented,
            couponsGroups=NotImplemented,
            productCodes=NotImplemented,
            dependencyType=NotImplemented,
            externalId=NotImplemented,
            isCancellationBlocked=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Subscription identifier
        # @var string
        self.id = id

        # A list of channels associated with this subscription
        # @var array of KalturaBaseChannel
        self.channels = channels

        # The first date the subscription is available for purchasing
        # @var int
        self.startDate = startDate

        # The last date the subscription is available for purchasing
        # @var int
        self.endDate = endDate

        # A list of file types identifiers that are supported in this subscription
        # @var array of KalturaIntegerValue
        self.fileTypes = fileTypes

        # Denotes whether or not this subscription can be renewed
        # @var bool
        self.isRenewable = isRenewable

        # Defines the number of times this subscription will be renewed
        # @var int
        self.renewalsNumber = renewalsNumber

        # Indicates whether the subscription will renew forever
        # @var bool
        self.isInfiniteRenewal = isInfiniteRenewal

        # The price of the subscription
        # @var KalturaPriceDetails
        self.price = price

        # The internal discount module for the subscription
        # @var KalturaDiscountModule
        self.discountModule = discountModule

        # Name of the subscription
        # @var string
        # @readonly
        self.name = name

        # Name of the subscription
        # @var array of KalturaTranslationToken
        self.multilingualName = multilingualName

        # description of the subscription
        # @var string
        # @readonly
        self.description = description

        # description of the subscription
        # @var array of KalturaTranslationToken
        self.multilingualDescription = multilingualDescription

        # Identifier of the media associated with the subscription
        # @var int
        self.mediaId = mediaId

        # Subscription order (when returned in methods that retrieve subscriptions)
        # @var int
        self.prorityInOrder = prorityInOrder

        # Comma separated subscription price plan IDs
        # @var string
        self.pricePlanIds = pricePlanIds

        # Subscription preview module
        # @var KalturaPreviewModule
        self.previewModule = previewModule

        # The household limitation module identifier associated with this subscription
        # @var int
        self.householdLimitationsId = householdLimitationsId

        # The subscription grace period in minutes
        # @var int
        self.gracePeriodMinutes = gracePeriodMinutes

        # List of premium services included in the subscription
        # @var array of KalturaPremiumService
        self.premiumServices = premiumServices

        # The maximum number of times an item in this usage module can be viewed
        # @var int
        self.maxViewsNumber = maxViewsNumber

        # The amount time an item is available for viewing since a user started watching the item
        # @var int
        self.viewLifeCycle = viewLifeCycle

        # Time period during which the end user can waive his rights to cancel a purchase. When the time period is passed, the purchase can no longer be cancelled
        # @var int
        self.waiverPeriod = waiverPeriod

        # Indicates whether or not the end user has the right to waive his rights to cancel a purchase
        # @var bool
        self.isWaiverEnabled = isWaiverEnabled

        # List of permitted user types for the subscription
        # @var array of KalturaOTTUserType
        self.userTypes = userTypes

        # List of Coupons group
        # @var array of KalturaCouponsGroup
        self.couponsGroups = couponsGroups

        # List of Subscription product codes
        # @var array of KalturaProductCode
        self.productCodes = productCodes

        # Dependency Type
        # @var KalturaSubscriptionDependencyType
        self.dependencyType = dependencyType

        # External ID
        # @var string
        self.externalId = externalId

        # Is cancellation blocked for the subscription
        # @var bool
        self.isCancellationBlocked = isCancellationBlocked


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'channels': (KalturaObjectFactory.createArray, 'KalturaBaseChannel'), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'fileTypes': (KalturaObjectFactory.createArray, 'KalturaIntegerValue'), 
        'isRenewable': getXmlNodeBool, 
        'renewalsNumber': getXmlNodeInt, 
        'isInfiniteRenewal': getXmlNodeBool, 
        'price': (KalturaObjectFactory.create, 'KalturaPriceDetails'), 
        'discountModule': (KalturaObjectFactory.create, 'KalturaDiscountModule'), 
        'name': getXmlNodeText, 
        'multilingualName': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'description': getXmlNodeText, 
        'multilingualDescription': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'mediaId': getXmlNodeInt, 
        'prorityInOrder': getXmlNodeInt, 
        'pricePlanIds': getXmlNodeText, 
        'previewModule': (KalturaObjectFactory.create, 'KalturaPreviewModule'), 
        'householdLimitationsId': getXmlNodeInt, 
        'gracePeriodMinutes': getXmlNodeInt, 
        'premiumServices': (KalturaObjectFactory.createArray, 'KalturaPremiumService'), 
        'maxViewsNumber': getXmlNodeInt, 
        'viewLifeCycle': getXmlNodeInt, 
        'waiverPeriod': getXmlNodeInt, 
        'isWaiverEnabled': getXmlNodeBool, 
        'userTypes': (KalturaObjectFactory.createArray, 'KalturaOTTUserType'), 
        'couponsGroups': (KalturaObjectFactory.createArray, 'KalturaCouponsGroup'), 
        'productCodes': (KalturaObjectFactory.createArray, 'KalturaProductCode'), 
        'dependencyType': (KalturaEnumsFactory.createString, "KalturaSubscriptionDependencyType"), 
        'externalId': getXmlNodeText, 
        'isCancellationBlocked': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscription.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSubscription")
        kparams.addStringIfDefined("id", self.id)
        kparams.addArrayIfDefined("channels", self.channels)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addArrayIfDefined("fileTypes", self.fileTypes)
        kparams.addBoolIfDefined("isRenewable", self.isRenewable)
        kparams.addIntIfDefined("renewalsNumber", self.renewalsNumber)
        kparams.addBoolIfDefined("isInfiniteRenewal", self.isInfiniteRenewal)
        kparams.addObjectIfDefined("price", self.price)
        kparams.addObjectIfDefined("discountModule", self.discountModule)
        kparams.addArrayIfDefined("multilingualName", self.multilingualName)
        kparams.addArrayIfDefined("multilingualDescription", self.multilingualDescription)
        kparams.addIntIfDefined("mediaId", self.mediaId)
        kparams.addIntIfDefined("prorityInOrder", self.prorityInOrder)
        kparams.addStringIfDefined("pricePlanIds", self.pricePlanIds)
        kparams.addObjectIfDefined("previewModule", self.previewModule)
        kparams.addIntIfDefined("householdLimitationsId", self.householdLimitationsId)
        kparams.addIntIfDefined("gracePeriodMinutes", self.gracePeriodMinutes)
        kparams.addArrayIfDefined("premiumServices", self.premiumServices)
        kparams.addIntIfDefined("maxViewsNumber", self.maxViewsNumber)
        kparams.addIntIfDefined("viewLifeCycle", self.viewLifeCycle)
        kparams.addIntIfDefined("waiverPeriod", self.waiverPeriod)
        kparams.addBoolIfDefined("isWaiverEnabled", self.isWaiverEnabled)
        kparams.addArrayIfDefined("userTypes", self.userTypes)
        kparams.addArrayIfDefined("couponsGroups", self.couponsGroups)
        kparams.addArrayIfDefined("productCodes", self.productCodes)
        kparams.addStringEnumIfDefined("dependencyType", self.dependencyType)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addBoolIfDefined("isCancellationBlocked", self.isCancellationBlocked)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getChannels(self):
        return self.channels

    def setChannels(self, newChannels):
        self.channels = newChannels

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getFileTypes(self):
        return self.fileTypes

    def setFileTypes(self, newFileTypes):
        self.fileTypes = newFileTypes

    def getIsRenewable(self):
        return self.isRenewable

    def setIsRenewable(self, newIsRenewable):
        self.isRenewable = newIsRenewable

    def getRenewalsNumber(self):
        return self.renewalsNumber

    def setRenewalsNumber(self, newRenewalsNumber):
        self.renewalsNumber = newRenewalsNumber

    def getIsInfiniteRenewal(self):
        return self.isInfiniteRenewal

    def setIsInfiniteRenewal(self, newIsInfiniteRenewal):
        self.isInfiniteRenewal = newIsInfiniteRenewal

    def getPrice(self):
        return self.price

    def setPrice(self, newPrice):
        self.price = newPrice

    def getDiscountModule(self):
        return self.discountModule

    def setDiscountModule(self, newDiscountModule):
        self.discountModule = newDiscountModule

    def getName(self):
        return self.name

    def getMultilingualName(self):
        return self.multilingualName

    def setMultilingualName(self, newMultilingualName):
        self.multilingualName = newMultilingualName

    def getDescription(self):
        return self.description

    def getMultilingualDescription(self):
        return self.multilingualDescription

    def setMultilingualDescription(self, newMultilingualDescription):
        self.multilingualDescription = newMultilingualDescription

    def getMediaId(self):
        return self.mediaId

    def setMediaId(self, newMediaId):
        self.mediaId = newMediaId

    def getProrityInOrder(self):
        return self.prorityInOrder

    def setProrityInOrder(self, newProrityInOrder):
        self.prorityInOrder = newProrityInOrder

    def getPricePlanIds(self):
        return self.pricePlanIds

    def setPricePlanIds(self, newPricePlanIds):
        self.pricePlanIds = newPricePlanIds

    def getPreviewModule(self):
        return self.previewModule

    def setPreviewModule(self, newPreviewModule):
        self.previewModule = newPreviewModule

    def getHouseholdLimitationsId(self):
        return self.householdLimitationsId

    def setHouseholdLimitationsId(self, newHouseholdLimitationsId):
        self.householdLimitationsId = newHouseholdLimitationsId

    def getGracePeriodMinutes(self):
        return self.gracePeriodMinutes

    def setGracePeriodMinutes(self, newGracePeriodMinutes):
        self.gracePeriodMinutes = newGracePeriodMinutes

    def getPremiumServices(self):
        return self.premiumServices

    def setPremiumServices(self, newPremiumServices):
        self.premiumServices = newPremiumServices

    def getMaxViewsNumber(self):
        return self.maxViewsNumber

    def setMaxViewsNumber(self, newMaxViewsNumber):
        self.maxViewsNumber = newMaxViewsNumber

    def getViewLifeCycle(self):
        return self.viewLifeCycle

    def setViewLifeCycle(self, newViewLifeCycle):
        self.viewLifeCycle = newViewLifeCycle

    def getWaiverPeriod(self):
        return self.waiverPeriod

    def setWaiverPeriod(self, newWaiverPeriod):
        self.waiverPeriod = newWaiverPeriod

    def getIsWaiverEnabled(self):
        return self.isWaiverEnabled

    def setIsWaiverEnabled(self, newIsWaiverEnabled):
        self.isWaiverEnabled = newIsWaiverEnabled

    def getUserTypes(self):
        return self.userTypes

    def setUserTypes(self, newUserTypes):
        self.userTypes = newUserTypes

    def getCouponsGroups(self):
        return self.couponsGroups

    def setCouponsGroups(self, newCouponsGroups):
        self.couponsGroups = newCouponsGroups

    def getProductCodes(self):
        return self.productCodes

    def setProductCodes(self, newProductCodes):
        self.productCodes = newProductCodes

    def getDependencyType(self):
        return self.dependencyType

    def setDependencyType(self, newDependencyType):
        self.dependencyType = newDependencyType

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getIsCancellationBlocked(self):
        return self.isCancellationBlocked

    def setIsCancellationBlocked(self, newIsCancellationBlocked):
        self.isCancellationBlocked = newIsCancellationBlocked


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionListResponse(KalturaListResponse):
    """Subscriptions list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of subscriptions
        # @var array of KalturaSubscription
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSubscription'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaNpvrPremiumService(KalturaPremiumService):
    """Npvr Premium Service"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            quotaInMinutes=NotImplemented):
        KalturaPremiumService.__init__(self,
            id,
            name)

        # Quota in minutes
        # @var int
        # @readonly
        self.quotaInMinutes = quotaInMinutes


    PROPERTY_LOADERS = {
        'quotaInMinutes': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaPremiumService.fromXml(self, node)
        self.fromXmlImpl(node, KalturaNpvrPremiumService.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPremiumService.toParams(self)
        kparams.put("objectType", "KalturaNpvrPremiumService")
        return kparams

    def getQuotaInMinutes(self):
        return self.quotaInMinutes


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPremiumService(KalturaPremiumService):
    """Houshold premium service"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaPremiumService.__init__(self,
            id,
            name)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaPremiumService.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPremiumService.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPremiumService.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPremiumService")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaProductsPriceListResponse(KalturaListResponse):
    """Prices list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of prices
        # @var array of KalturaProductPrice
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaProductPrice'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductsPriceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaProductsPriceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPersonalList(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            createDate=NotImplemented,
            ksql=NotImplemented,
            partnerListType=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Id
        # @var int
        # @readonly
        self.id = id

        # Name
        # @var string
        self.name = name

        # Create Date
        # @var int
        # @readonly
        self.createDate = createDate

        # Search assets using dynamic criteria. Provided collection of nested expressions with key, comparison operators, value, and logical conjunction.
        #             Possible keys: any Tag or Meta defined in the system and the following reserved keys: start_date, end_date. 
        #             epg_id, media_id - for specific asset IDs.
        #             geo_block - only valid value is &quot;true&quot;: When enabled, only assets that are not restricted to the user by geo-block rules will return.
        #             parental_rules - only valid value is &quot;true&quot;: When enabled, only assets that the user doesn&#39;t need to provide PIN code will return.
        #             user_interests - only valid value is &quot;true&quot;. When enabled, only assets that the user defined as his interests (by tags and metas) will return.
        #             epg_channel_id - the channel identifier of the EPG program.
        #             entitled_assets - valid values: &quot;free&quot;, &quot;entitled&quot;, &quot;not_entitled&quot;, &quot;both&quot;. free - gets only free to watch assets. entitled - only those that the user is implicitly entitled to watch.
        #             asset_type - valid values: &quot;media&quot;, &quot;epg&quot;, &quot;recording&quot; or any number that represents media type in group.
        #             Comparison operators: for numerical fields =, &gt;, &gt;=, &lt;, &lt;=, : (in). 
        #             For alpha-numerical fields =, != (not), ~ (like), !~, ^ (any word starts with), ^= (phrase starts with), + (exists), !+ (not exists).
        #             Logical conjunction: and, or. 
        #             Search values are limited to 20 characters each for the next operators: ~, !~, ^, ^=
        #             (maximum length of entire filter is 2048 characters)
        # @var string
        self.ksql = ksql

        # Partner List Type (optional)
        # @var int
        self.partnerListType = partnerListType


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
        'ksql': getXmlNodeText, 
        'partnerListType': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalList.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPersonalList")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("ksql", self.ksql)
        kparams.addIntIfDefined("partnerListType", self.partnerListType)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getCreateDate(self):
        return self.createDate

    def getKsql(self):
        return self.ksql

    def setKsql(self, newKsql):
        self.ksql = newKsql

    def getPartnerListType(self):
        return self.partnerListType

    def setPartnerListType(self, newPartnerListType):
        self.partnerListType = newPartnerListType


# @package Kaltura
# @subpackage Client
class KalturaPersonalListListResponse(KalturaListResponse):
    """List of KalturaPersonalList."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaPersonalList
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaPersonalList'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalListListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPersonalListListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaEngagement(KalturaObjectBase):
    """Engagement"""

    def __init__(self,
            id=NotImplemented,
            totalNumberOfRecipients=NotImplemented,
            type=NotImplemented,
            adapterId=NotImplemented,
            adapterDynamicData=NotImplemented,
            intervalSeconds=NotImplemented,
            userList=NotImplemented,
            sendTimeInSeconds=NotImplemented,
            couponGroupId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Engagement id
        # @var int
        # @readonly
        self.id = id

        # Total number of recipients
        # @var int
        # @readonly
        self.totalNumberOfRecipients = totalNumberOfRecipients

        # Engagement type
        # @var KalturaEngagementType
        self.type = type

        # Engagement adapter id
        # @var int
        self.adapterId = adapterId

        # Engagement adapter dynamic data
        # @var string
        self.adapterDynamicData = adapterDynamicData

        # Interval (seconds)
        # @var int
        self.intervalSeconds = intervalSeconds

        # Manual User list
        # @var string
        self.userList = userList

        # Send time (seconds)
        # @var int
        self.sendTimeInSeconds = sendTimeInSeconds

        # Coupon GroupId
        # @var int
        self.couponGroupId = couponGroupId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'totalNumberOfRecipients': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaEngagementType"), 
        'adapterId': getXmlNodeInt, 
        'adapterDynamicData': getXmlNodeText, 
        'intervalSeconds': getXmlNodeInt, 
        'userList': getXmlNodeText, 
        'sendTimeInSeconds': getXmlNodeInt, 
        'couponGroupId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEngagement.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEngagement")
        kparams.addStringEnumIfDefined("type", self.type)
        kparams.addIntIfDefined("adapterId", self.adapterId)
        kparams.addStringIfDefined("adapterDynamicData", self.adapterDynamicData)
        kparams.addIntIfDefined("intervalSeconds", self.intervalSeconds)
        kparams.addStringIfDefined("userList", self.userList)
        kparams.addIntIfDefined("sendTimeInSeconds", self.sendTimeInSeconds)
        kparams.addIntIfDefined("couponGroupId", self.couponGroupId)
        return kparams

    def getId(self):
        return self.id

    def getTotalNumberOfRecipients(self):
        return self.totalNumberOfRecipients

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getAdapterId(self):
        return self.adapterId

    def setAdapterId(self, newAdapterId):
        self.adapterId = newAdapterId

    def getAdapterDynamicData(self):
        return self.adapterDynamicData

    def setAdapterDynamicData(self, newAdapterDynamicData):
        self.adapterDynamicData = newAdapterDynamicData

    def getIntervalSeconds(self):
        return self.intervalSeconds

    def setIntervalSeconds(self, newIntervalSeconds):
        self.intervalSeconds = newIntervalSeconds

    def getUserList(self):
        return self.userList

    def setUserList(self, newUserList):
        self.userList = newUserList

    def getSendTimeInSeconds(self):
        return self.sendTimeInSeconds

    def setSendTimeInSeconds(self, newSendTimeInSeconds):
        self.sendTimeInSeconds = newSendTimeInSeconds

    def getCouponGroupId(self):
        return self.couponGroupId

    def setCouponGroupId(self, newCouponGroupId):
        self.couponGroupId = newCouponGroupId


# @package Kaltura
# @subpackage Client
class KalturaEngagementListResponse(KalturaListResponse):
    """Engagement adapter list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of Engagement
        # @var array of KalturaEngagement
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaEngagement'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEngagementListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaEngagementListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaEngagementAdapterBase(KalturaObjectBase):
    """Engagement adapter basic"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Engagement adapter id
        # @var int
        # @readonly
        self.id = id

        # Engagement adapter name
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEngagementAdapterBase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEngagementAdapterBase")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaEngagementAdapter(KalturaEngagementAdapterBase):
    """Engagement Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            providerUrl=NotImplemented,
            engagementAdapterSettings=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaEngagementAdapterBase.__init__(self,
            id,
            name)

        # Engagement adapter active status
        # @var bool
        self.isActive = isActive

        # Engagement adapter adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # Engagement provider adapter URL
        # @var string
        self.providerUrl = providerUrl

        # Engagement adapter extra parameters
        # @var map
        self.engagementAdapterSettings = engagementAdapterSettings

        # Shared Secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'providerUrl': getXmlNodeText, 
        'engagementAdapterSettings': (KalturaObjectFactory.createMap, 'KalturaStringValue'), 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaEngagementAdapterBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEngagementAdapter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEngagementAdapterBase.toParams(self)
        kparams.put("objectType", "KalturaEngagementAdapter")
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addStringIfDefined("providerUrl", self.providerUrl)
        kparams.addMapIfDefined("engagementAdapterSettings", self.engagementAdapterSettings)
        return kparams

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getProviderUrl(self):
        return self.providerUrl

    def setProviderUrl(self, newProviderUrl):
        self.providerUrl = newProviderUrl

    def getEngagementAdapterSettings(self):
        return self.engagementAdapterSettings

    def setEngagementAdapterSettings(self, newEngagementAdapterSettings):
        self.engagementAdapterSettings = newEngagementAdapterSettings

    def getSharedSecret(self):
        return self.sharedSecret


# @package Kaltura
# @subpackage Client
class KalturaEngagementAdapterListResponse(KalturaListResponse):
    """Engagement adapter list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of Engagement adapter
        # @var array of KalturaEngagementAdapter
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaEngagementAdapter'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEngagementAdapterListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaEngagementAdapterListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaReminder(KalturaObjectBase):
    def __init__(self,
            name=NotImplemented,
            id=NotImplemented,
            type=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Reminder name
        # @var string
        # @readonly
        self.name = name

        # Reminder id
        # @var int
        # @readonly
        self.id = id

        # Reminder type
        # @var KalturaReminderType
        self.type = type


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'id': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaReminderType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReminder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReminder")
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaReminderListResponse(KalturaListResponse):
    """List of reminders from DB."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Reminders
        # @var array of KalturaReminder
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaReminder'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReminderListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaReminderListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSeriesReminder(KalturaReminder):
    def __init__(self,
            name=NotImplemented,
            id=NotImplemented,
            type=NotImplemented,
            seriesId=NotImplemented,
            seasonNumber=NotImplemented,
            epgChannelId=NotImplemented):
        KalturaReminder.__init__(self,
            name,
            id,
            type)

        # Series identifier
        # @var string
        self.seriesId = seriesId

        # Season number
        # @var int
        self.seasonNumber = seasonNumber

        # EPG channel identifier
        # @var int
        self.epgChannelId = epgChannelId


    PROPERTY_LOADERS = {
        'seriesId': getXmlNodeText, 
        'seasonNumber': getXmlNodeInt, 
        'epgChannelId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaReminder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeriesReminder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReminder.toParams(self)
        kparams.put("objectType", "KalturaSeriesReminder")
        kparams.addStringIfDefined("seriesId", self.seriesId)
        kparams.addIntIfDefined("seasonNumber", self.seasonNumber)
        kparams.addIntIfDefined("epgChannelId", self.epgChannelId)
        return kparams

    def getSeriesId(self):
        return self.seriesId

    def setSeriesId(self, newSeriesId):
        self.seriesId = newSeriesId

    def getSeasonNumber(self):
        return self.seasonNumber

    def setSeasonNumber(self, newSeasonNumber):
        self.seasonNumber = newSeasonNumber

    def getEpgChannelId(self):
        return self.epgChannelId

    def setEpgChannelId(self, newEpgChannelId):
        self.epgChannelId = newEpgChannelId


# @package Kaltura
# @subpackage Client
class KalturaAssetReminder(KalturaReminder):
    def __init__(self,
            name=NotImplemented,
            id=NotImplemented,
            type=NotImplemented,
            assetId=NotImplemented):
        KalturaReminder.__init__(self,
            name,
            id,
            type)

        # Asset id
        # @var int
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaReminder.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetReminder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReminder.toParams(self)
        kparams.put("objectType", "KalturaAssetReminder")
        kparams.addIntIfDefined("assetId", self.assetId)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId


# @package Kaltura
# @subpackage Client
class KalturaInboxMessage(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            message=NotImplemented,
            status=NotImplemented,
            type=NotImplemented,
            createdAt=NotImplemented,
            url=NotImplemented):
        KalturaObjectBase.__init__(self)

        # message id
        # @var string
        # @readonly
        self.id = id

        # message
        # @var string
        self.message = message

        # Status
        # @var KalturaInboxMessageStatus
        # @readonly
        self.status = status

        # Type
        # @var KalturaInboxMessageType
        self.type = type

        # Created at
        # @var int
        # @readonly
        self.createdAt = createdAt

        # url
        # @var string
        self.url = url


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'message': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createString, "KalturaInboxMessageStatus"), 
        'type': (KalturaEnumsFactory.createString, "KalturaInboxMessageType"), 
        'createdAt': getXmlNodeInt, 
        'url': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInboxMessage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaInboxMessage")
        kparams.addStringIfDefined("message", self.message)
        kparams.addStringEnumIfDefined("type", self.type)
        kparams.addStringIfDefined("url", self.url)
        return kparams

    def getId(self):
        return self.id

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage):
        self.message = newMessage

    def getStatus(self):
        return self.status

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getCreatedAt(self):
        return self.createdAt

    def getUrl(self):
        return self.url

    def setUrl(self, newUrl):
        self.url = newUrl


# @package Kaltura
# @subpackage Client
class KalturaInboxMessageListResponse(KalturaListResponse):
    """List of inbox message."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaInboxMessage
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaInboxMessage'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInboxMessageListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaInboxMessageListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaFollowDataBase(KalturaObjectBase):
    def __init__(self,
            announcementId=NotImplemented,
            status=NotImplemented,
            title=NotImplemented,
            timestamp=NotImplemented,
            followPhrase=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Announcement Id
        # @var int
        # @readonly
        self.announcementId = announcementId

        # Status
        # @var int
        # @readonly
        self.status = status

        # Title
        # @var string
        # @readonly
        self.title = title

        # Timestamp
        # @var int
        # @readonly
        self.timestamp = timestamp

        # Follow Phrase
        # @var string
        # @readonly
        self.followPhrase = followPhrase


    PROPERTY_LOADERS = {
        'announcementId': getXmlNodeInt, 
        'status': getXmlNodeInt, 
        'title': getXmlNodeText, 
        'timestamp': getXmlNodeInt, 
        'followPhrase': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFollowDataBase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFollowDataBase")
        return kparams

    def getAnnouncementId(self):
        return self.announcementId

    def getStatus(self):
        return self.status

    def getTitle(self):
        return self.title

    def getTimestamp(self):
        return self.timestamp

    def getFollowPhrase(self):
        return self.followPhrase


# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeries(KalturaFollowDataBase):
    def __init__(self,
            announcementId=NotImplemented,
            status=NotImplemented,
            title=NotImplemented,
            timestamp=NotImplemented,
            followPhrase=NotImplemented,
            assetId=NotImplemented):
        KalturaFollowDataBase.__init__(self,
            announcementId,
            status,
            title,
            timestamp,
            followPhrase)

        # Asset Id
        # @var int
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFollowDataBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFollowTvSeries.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFollowDataBase.toParams(self)
        kparams.put("objectType", "KalturaFollowTvSeries")
        kparams.addIntIfDefined("assetId", self.assetId)
        return kparams

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId


# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeriesListResponse(KalturaListResponse):
    """List of message follow data."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaFollowTvSeries
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaFollowTvSeries'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFollowTvSeriesListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaFollowTvSeriesListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAnnouncement(KalturaObjectBase):
    def __init__(self,
            name=NotImplemented,
            message=NotImplemented,
            enabled=NotImplemented,
            startTime=NotImplemented,
            timezone=NotImplemented,
            status=NotImplemented,
            recipients=NotImplemented,
            id=NotImplemented,
            imageUrl=NotImplemented,
            includeMail=NotImplemented,
            mailTemplate=NotImplemented,
            mailSubject=NotImplemented,
            includeSms=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Announcement name
        # @var string
        self.name = name

        # Announcement message
        # @var string
        self.message = message

        # Announcement enabled
        # @var bool
        self.enabled = enabled

        # Announcement start time
        # @var int
        self.startTime = startTime

        # Announcement time zone
        # @var string
        self.timezone = timezone

        # Announcement status: NotSent=0/Sending=1/Sent=2/Aborted=3
        # @var KalturaAnnouncementStatus
        # @readonly
        self.status = status

        # Announcement recipients: All=0/LoggedIn=1/Guests=2/Other=3
        # @var KalturaAnnouncementRecipientsType
        self.recipients = recipients

        # Announcement id
        # @var int
        # @readonly
        self.id = id

        # Announcement image URL, relevant for system announcements
        # @var string
        self.imageUrl = imageUrl

        # Include Mail
        # @var bool
        self.includeMail = includeMail

        # Mail Template
        # @var string
        self.mailTemplate = mailTemplate

        # Mail Subject
        # @var string
        self.mailSubject = mailSubject

        # Include SMS
        # @var bool
        self.includeSms = includeSms


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'message': getXmlNodeText, 
        'enabled': getXmlNodeBool, 
        'startTime': getXmlNodeInt, 
        'timezone': getXmlNodeText, 
        'status': (KalturaEnumsFactory.createString, "KalturaAnnouncementStatus"), 
        'recipients': (KalturaEnumsFactory.createString, "KalturaAnnouncementRecipientsType"), 
        'id': getXmlNodeInt, 
        'imageUrl': getXmlNodeText, 
        'includeMail': getXmlNodeBool, 
        'mailTemplate': getXmlNodeText, 
        'mailSubject': getXmlNodeText, 
        'includeSms': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnouncement.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAnnouncement")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("message", self.message)
        kparams.addBoolIfDefined("enabled", self.enabled)
        kparams.addIntIfDefined("startTime", self.startTime)
        kparams.addStringIfDefined("timezone", self.timezone)
        kparams.addStringEnumIfDefined("recipients", self.recipients)
        kparams.addStringIfDefined("imageUrl", self.imageUrl)
        kparams.addBoolIfDefined("includeMail", self.includeMail)
        kparams.addStringIfDefined("mailTemplate", self.mailTemplate)
        kparams.addStringIfDefined("mailSubject", self.mailSubject)
        kparams.addBoolIfDefined("includeSms", self.includeSms)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getMessage(self):
        return self.message

    def setMessage(self, newMessage):
        self.message = newMessage

    def getEnabled(self):
        return self.enabled

    def setEnabled(self, newEnabled):
        self.enabled = newEnabled

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, newStartTime):
        self.startTime = newStartTime

    def getTimezone(self):
        return self.timezone

    def setTimezone(self, newTimezone):
        self.timezone = newTimezone

    def getStatus(self):
        return self.status

    def getRecipients(self):
        return self.recipients

    def setRecipients(self, newRecipients):
        self.recipients = newRecipients

    def getId(self):
        return self.id

    def getImageUrl(self):
        return self.imageUrl

    def setImageUrl(self, newImageUrl):
        self.imageUrl = newImageUrl

    def getIncludeMail(self):
        return self.includeMail

    def setIncludeMail(self, newIncludeMail):
        self.includeMail = newIncludeMail

    def getMailTemplate(self):
        return self.mailTemplate

    def setMailTemplate(self, newMailTemplate):
        self.mailTemplate = newMailTemplate

    def getMailSubject(self):
        return self.mailSubject

    def setMailSubject(self, newMailSubject):
        self.mailSubject = newMailSubject

    def getIncludeSms(self):
        return self.includeSms

    def setIncludeSms(self, newIncludeSms):
        self.includeSms = newIncludeSms


# @package Kaltura
# @subpackage Client
class KalturaAnnouncementListResponse(KalturaListResponse):
    """List of message announcements from DB."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Announcements
        # @var array of KalturaAnnouncement
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAnnouncement'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnouncementListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAnnouncementListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaFeed(KalturaObjectBase):
    def __init__(self,
            assetId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Asset identifier
        # @var int
        # @readonly
        self.assetId = assetId


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFeed")
        return kparams

    def getAssetId(self):
        return self.assetId


# @package Kaltura
# @subpackage Client
class KalturaPersonalFeed(KalturaFeed):
    def __init__(self,
            assetId=NotImplemented):
        KalturaFeed.__init__(self,
            assetId)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFeed.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalFeed.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFeed.toParams(self)
        kparams.put("objectType", "KalturaPersonalFeed")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPersonalFeedListResponse(KalturaListResponse):
    """List of message follow data."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaPersonalFeed
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaPersonalFeed'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalFeedListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPersonalFeedListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaTopic(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            subscribersAmount=NotImplemented,
            automaticIssueNotification=NotImplemented,
            lastMessageSentDateSec=NotImplemented):
        KalturaObjectBase.__init__(self)

        # message id
        # @var string
        # @readonly
        self.id = id

        # message
        # @var string
        self.name = name

        # message
        # @var string
        self.subscribersAmount = subscribersAmount

        # automaticIssueNotification
        # @var KalturaTopicAutomaticIssueNotification
        self.automaticIssueNotification = automaticIssueNotification

        # lastMessageSentDateSec
        # @var int
        self.lastMessageSentDateSec = lastMessageSentDateSec


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'subscribersAmount': getXmlNodeText, 
        'automaticIssueNotification': (KalturaEnumsFactory.createString, "KalturaTopicAutomaticIssueNotification"), 
        'lastMessageSentDateSec': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTopic.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTopic")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("subscribersAmount", self.subscribersAmount)
        kparams.addStringEnumIfDefined("automaticIssueNotification", self.automaticIssueNotification)
        kparams.addIntIfDefined("lastMessageSentDateSec", self.lastMessageSentDateSec)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSubscribersAmount(self):
        return self.subscribersAmount

    def setSubscribersAmount(self, newSubscribersAmount):
        self.subscribersAmount = newSubscribersAmount

    def getAutomaticIssueNotification(self):
        return self.automaticIssueNotification

    def setAutomaticIssueNotification(self, newAutomaticIssueNotification):
        self.automaticIssueNotification = newAutomaticIssueNotification

    def getLastMessageSentDateSec(self):
        return self.lastMessageSentDateSec

    def setLastMessageSentDateSec(self, newLastMessageSentDateSec):
        self.lastMessageSentDateSec = newLastMessageSentDateSec


# @package Kaltura
# @subpackage Client
class KalturaTopicListResponse(KalturaListResponse):
    """List of inbox message."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Follow data list
        # @var array of KalturaTopic
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaTopic'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTopicListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaTopicListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSeriesRecording(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            epgId=NotImplemented,
            channelId=NotImplemented,
            seriesId=NotImplemented,
            seasonNumber=NotImplemented,
            type=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            excludedSeasons=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Kaltura unique ID representing the series recording identifier
        # @var int
        # @readonly
        self.id = id

        # Kaltura EpgId
        # @var int
        self.epgId = epgId

        # Kaltura ChannelId
        # @var int
        self.channelId = channelId

        # Kaltura SeriesId
        # @var string
        self.seriesId = seriesId

        # Kaltura SeasonNumber
        # @var int
        self.seasonNumber = seasonNumber

        # Recording Type: single/series/season
        # @var KalturaRecordingType
        self.type = type

        # Specifies when was the series recording created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the series recording last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate

        # List of the season numbers to exclude.
        # @var array of KalturaIntegerValue
        # @readonly
        self.excludedSeasons = excludedSeasons


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'epgId': getXmlNodeInt, 
        'channelId': getXmlNodeInt, 
        'seriesId': getXmlNodeText, 
        'seasonNumber': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaRecordingType"), 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
        'excludedSeasons': (KalturaObjectFactory.createArray, 'KalturaIntegerValue'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeriesRecording.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSeriesRecording")
        kparams.addIntIfDefined("epgId", self.epgId)
        kparams.addIntIfDefined("channelId", self.channelId)
        kparams.addStringIfDefined("seriesId", self.seriesId)
        kparams.addIntIfDefined("seasonNumber", self.seasonNumber)
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getId(self):
        return self.id

    def getEpgId(self):
        return self.epgId

    def setEpgId(self, newEpgId):
        self.epgId = newEpgId

    def getChannelId(self):
        return self.channelId

    def setChannelId(self, newChannelId):
        self.channelId = newChannelId

    def getSeriesId(self):
        return self.seriesId

    def setSeriesId(self, newSeriesId):
        self.seriesId = newSeriesId

    def getSeasonNumber(self):
        return self.seasonNumber

    def setSeasonNumber(self, newSeasonNumber):
        self.seasonNumber = newSeasonNumber

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate

    def getExcludedSeasons(self):
        return self.excludedSeasons


# @package Kaltura
# @subpackage Client
class KalturaSeriesRecordingListResponse(KalturaListResponse):
    """Series Recordings info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Series Recordings
        # @var array of KalturaSeriesRecording
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSeriesRecording'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeriesRecordingListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSeriesRecordingListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaHouseholdPremiumServiceListResponse(KalturaListResponse):
    """Premium services list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of premium services
        # @var array of KalturaHouseholdPremiumService
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaHouseholdPremiumService'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdPremiumServiceListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaHouseholdPremiumServiceListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaCDVRAdapterProfile(KalturaObjectBase):
    """C-DVR Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            settings=NotImplemented,
            externalIdentifier=NotImplemented,
            sharedSecret=NotImplemented,
            dynamicLinksSupport=NotImplemented):
        KalturaObjectBase.__init__(self)

        # C-DVR adapter identifier
        # @var int
        # @readonly
        self.id = id

        # C-DVR adapter name
        # @var string
        self.name = name

        # C-DVR adapter active status
        # @var bool
        self.isActive = isActive

        # C-DVR adapter adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # C-DVR adapter extra parameters
        # @var map
        self.settings = settings

        # C-DVR adapter external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # C-DVR shared secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret

        # Indicates whether the C-DVR adapter supports dynamic URLs
        # @var bool
        self.dynamicLinksSupport = dynamicLinksSupport


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'settings': (KalturaObjectFactory.createMap, 'KalturaStringValue'), 
        'externalIdentifier': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
        'dynamicLinksSupport': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDVRAdapterProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCDVRAdapterProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addMapIfDefined("settings", self.settings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        kparams.addBoolIfDefined("dynamicLinksSupport", self.dynamicLinksSupport)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getSettings(self):
        return self.settings

    def setSettings(self, newSettings):
        self.settings = newSettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getSharedSecret(self):
        return self.sharedSecret

    def getDynamicLinksSupport(self):
        return self.dynamicLinksSupport

    def setDynamicLinksSupport(self, newDynamicLinksSupport):
        self.dynamicLinksSupport = newDynamicLinksSupport


# @package Kaltura
# @subpackage Client
class KalturaCDVRAdapterProfileListResponse(KalturaListResponse):
    """C-DVR adapter profiles"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # C-DVR adapter profiles
        # @var array of KalturaCDVRAdapterProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaCDVRAdapterProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDVRAdapterProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCDVRAdapterProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaRecording(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            status=NotImplemented,
            assetId=NotImplemented,
            type=NotImplemented,
            viewableUntilDate=NotImplemented,
            isProtected=NotImplemented,
            externalId=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Kaltura unique ID representing the recording identifier
        # @var int
        # @readonly
        self.id = id

        # Recording state: scheduled/recording/recorded/canceled/failed/deleted
        # @var KalturaRecordingStatus
        # @readonly
        self.status = status

        # Kaltura unique ID representing the program identifier
        # @var int
        self.assetId = assetId

        # Recording Type: single/season/series
        # @var KalturaRecordingType
        # @readonly
        self.type = type

        # Specifies until when the recording is available for viewing. Date and time represented as epoch.
        # @var int
        # @readonly
        self.viewableUntilDate = viewableUntilDate

        # Specifies whether or not the recording is protected
        # @var bool
        # @readonly
        self.isProtected = isProtected

        # External identifier for the recording
        # @var string
        self.externalId = externalId

        # Specifies when was the recording created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the recording last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createString, "KalturaRecordingStatus"), 
        'assetId': getXmlNodeInt, 
        'type': (KalturaEnumsFactory.createString, "KalturaRecordingType"), 
        'viewableUntilDate': getXmlNodeInt, 
        'isProtected': getXmlNodeBool, 
        'externalId': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecording.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRecording")
        kparams.addIntIfDefined("assetId", self.assetId)
        kparams.addStringIfDefined("externalId", self.externalId)
        return kparams

    def getId(self):
        return self.id

    def getStatus(self):
        return self.status

    def getAssetId(self):
        return self.assetId

    def setAssetId(self, newAssetId):
        self.assetId = newAssetId

    def getType(self):
        return self.type

    def getViewableUntilDate(self):
        return self.viewableUntilDate

    def getIsProtected(self):
        return self.isProtected

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate


# @package Kaltura
# @subpackage Client
class KalturaRecordingListResponse(KalturaListResponse):
    """Recordings info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Recordings
        # @var array of KalturaRecording
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaRecording'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecordingListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRecordingListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaBillingTransaction(KalturaObjectBase):
    """Billing Transaction"""

    def __init__(self,
            recieptCode=NotImplemented,
            purchasedItemName=NotImplemented,
            purchasedItemCode=NotImplemented,
            itemType=NotImplemented,
            billingAction=NotImplemented,
            price=NotImplemented,
            actionDate=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            paymentMethod=NotImplemented,
            paymentMethodExtraDetails=NotImplemented,
            isRecurring=NotImplemented,
            billingProviderRef=NotImplemented,
            purchaseId=NotImplemented,
            remarks=NotImplemented,
            billingPriceType=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Reciept Code
        # @var string
        # @readonly
        self.recieptCode = recieptCode

        # Purchased Item Name
        # @var string
        # @readonly
        self.purchasedItemName = purchasedItemName

        # Purchased Item Code
        # @var string
        # @readonly
        self.purchasedItemCode = purchasedItemCode

        # Item Type
        # @var KalturaBillingItemsType
        # @readonly
        self.itemType = itemType

        # Billing Action
        # @var KalturaBillingAction
        # @readonly
        self.billingAction = billingAction

        # price
        # @var KalturaPrice
        # @readonly
        self.price = price

        # Action Date
        # @var int
        # @readonly
        self.actionDate = actionDate

        # Start Date
        # @var int
        # @readonly
        self.startDate = startDate

        # End Date
        # @var int
        # @readonly
        self.endDate = endDate

        # Payment Method
        # @var KalturaPaymentMethodType
        # @readonly
        self.paymentMethod = paymentMethod

        # Payment Method Extra Details
        # @var string
        # @readonly
        self.paymentMethodExtraDetails = paymentMethodExtraDetails

        # Is Recurring
        # @var bool
        # @readonly
        self.isRecurring = isRecurring

        # Billing Provider Ref
        # @var int
        # @readonly
        self.billingProviderRef = billingProviderRef

        # Purchase ID
        # @var int
        # @readonly
        self.purchaseId = purchaseId

        # Remarks
        # @var string
        # @readonly
        self.remarks = remarks

        # Billing Price Info
        # @var KalturaBillingPriceType
        # @readonly
        self.billingPriceType = billingPriceType


    PROPERTY_LOADERS = {
        'recieptCode': getXmlNodeText, 
        'purchasedItemName': getXmlNodeText, 
        'purchasedItemCode': getXmlNodeText, 
        'itemType': (KalturaEnumsFactory.createString, "KalturaBillingItemsType"), 
        'billingAction': (KalturaEnumsFactory.createString, "KalturaBillingAction"), 
        'price': (KalturaObjectFactory.create, 'KalturaPrice'), 
        'actionDate': getXmlNodeInt, 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'paymentMethod': (KalturaEnumsFactory.createString, "KalturaPaymentMethodType"), 
        'paymentMethodExtraDetails': getXmlNodeText, 
        'isRecurring': getXmlNodeBool, 
        'billingProviderRef': getXmlNodeInt, 
        'purchaseId': getXmlNodeInt, 
        'remarks': getXmlNodeText, 
        'billingPriceType': (KalturaEnumsFactory.createString, "KalturaBillingPriceType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBillingTransaction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBillingTransaction")
        return kparams

    def getRecieptCode(self):
        return self.recieptCode

    def getPurchasedItemName(self):
        return self.purchasedItemName

    def getPurchasedItemCode(self):
        return self.purchasedItemCode

    def getItemType(self):
        return self.itemType

    def getBillingAction(self):
        return self.billingAction

    def getPrice(self):
        return self.price

    def getActionDate(self):
        return self.actionDate

    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate

    def getPaymentMethod(self):
        return self.paymentMethod

    def getPaymentMethodExtraDetails(self):
        return self.paymentMethodExtraDetails

    def getIsRecurring(self):
        return self.isRecurring

    def getBillingProviderRef(self):
        return self.billingProviderRef

    def getPurchaseId(self):
        return self.purchaseId

    def getRemarks(self):
        return self.remarks

    def getBillingPriceType(self):
        return self.billingPriceType


# @package Kaltura
# @subpackage Client
class KalturaBillingTransactionListResponse(KalturaListResponse):
    """Billing Transactions"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Transactions
        # @var array of KalturaBillingTransaction
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaBillingTransaction'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBillingTransactionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaBillingTransactionListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaEntitlement(KalturaObjectBase):
    """Entitlement"""

    def __init__(self,
            id=NotImplemented,
            productId=NotImplemented,
            currentUses=NotImplemented,
            endDate=NotImplemented,
            currentDate=NotImplemented,
            lastViewDate=NotImplemented,
            purchaseDate=NotImplemented,
            paymentMethod=NotImplemented,
            deviceUdid=NotImplemented,
            deviceName=NotImplemented,
            isCancelationWindowEnabled=NotImplemented,
            maxUses=NotImplemented,
            userId=NotImplemented,
            householdId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Purchase identifier (for subscriptions and collections only)
        # @var int
        # @readonly
        self.id = id

        # Product identifier
        # @var string
        # @readonly
        self.productId = productId

        # The current number of uses
        # @var int
        # @readonly
        self.currentUses = currentUses

        # The end date of the entitlement
        # @var int
        # @readonly
        self.endDate = endDate

        # Current date
        # @var int
        # @readonly
        self.currentDate = currentDate

        # The last date the item was viewed
        # @var int
        # @readonly
        self.lastViewDate = lastViewDate

        # Purchase date
        # @var int
        # @readonly
        self.purchaseDate = purchaseDate

        # Payment Method
        # @var KalturaPaymentMethodType
        # @readonly
        self.paymentMethod = paymentMethod

        # The UDID of the device from which the purchase was made
        # @var string
        # @readonly
        self.deviceUdid = deviceUdid

        # The name of the device from which the purchase was made
        # @var string
        # @readonly
        self.deviceName = deviceName

        # Indicates whether a cancelation window period is enabled
        # @var bool
        # @readonly
        self.isCancelationWindowEnabled = isCancelationWindowEnabled

        # The maximum number of uses available for this item (only for subscription and PPV)
        # @var int
        # @readonly
        self.maxUses = maxUses

        # The Identifier of the purchasing user
        # @var string
        # @readonly
        self.userId = userId

        # The Identifier of the purchasing household
        # @var int
        # @readonly
        self.householdId = householdId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'productId': getXmlNodeText, 
        'currentUses': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'currentDate': getXmlNodeInt, 
        'lastViewDate': getXmlNodeInt, 
        'purchaseDate': getXmlNodeInt, 
        'paymentMethod': (KalturaEnumsFactory.createString, "KalturaPaymentMethodType"), 
        'deviceUdid': getXmlNodeText, 
        'deviceName': getXmlNodeText, 
        'isCancelationWindowEnabled': getXmlNodeBool, 
        'maxUses': getXmlNodeInt, 
        'userId': getXmlNodeText, 
        'householdId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntitlement.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaEntitlement")
        return kparams

    def getId(self):
        return self.id

    def getProductId(self):
        return self.productId

    def getCurrentUses(self):
        return self.currentUses

    def getEndDate(self):
        return self.endDate

    def getCurrentDate(self):
        return self.currentDate

    def getLastViewDate(self):
        return self.lastViewDate

    def getPurchaseDate(self):
        return self.purchaseDate

    def getPaymentMethod(self):
        return self.paymentMethod

    def getDeviceUdid(self):
        return self.deviceUdid

    def getDeviceName(self):
        return self.deviceName

    def getIsCancelationWindowEnabled(self):
        return self.isCancelationWindowEnabled

    def getMaxUses(self):
        return self.maxUses

    def getUserId(self):
        return self.userId

    def getHouseholdId(self):
        return self.householdId


# @package Kaltura
# @subpackage Client
class KalturaEntitlementListResponse(KalturaListResponse):
    """Entitlements list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of entitlements
        # @var array of KalturaEntitlement
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaEntitlement'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntitlementListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaEntitlementListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaCollectionEntitlement(KalturaEntitlement):
    def __init__(self,
            id=NotImplemented,
            productId=NotImplemented,
            currentUses=NotImplemented,
            endDate=NotImplemented,
            currentDate=NotImplemented,
            lastViewDate=NotImplemented,
            purchaseDate=NotImplemented,
            paymentMethod=NotImplemented,
            deviceUdid=NotImplemented,
            deviceName=NotImplemented,
            isCancelationWindowEnabled=NotImplemented,
            maxUses=NotImplemented,
            userId=NotImplemented,
            householdId=NotImplemented):
        KalturaEntitlement.__init__(self,
            id,
            productId,
            currentUses,
            endDate,
            currentDate,
            lastViewDate,
            purchaseDate,
            paymentMethod,
            deviceUdid,
            deviceName,
            isCancelationWindowEnabled,
            maxUses,
            userId,
            householdId)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaEntitlement.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCollectionEntitlement.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntitlement.toParams(self)
        kparams.put("objectType", "KalturaCollectionEntitlement")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPpvEntitlement(KalturaEntitlement):
    """KalturaPpvEntitlement"""

    def __init__(self,
            id=NotImplemented,
            productId=NotImplemented,
            currentUses=NotImplemented,
            endDate=NotImplemented,
            currentDate=NotImplemented,
            lastViewDate=NotImplemented,
            purchaseDate=NotImplemented,
            paymentMethod=NotImplemented,
            deviceUdid=NotImplemented,
            deviceName=NotImplemented,
            isCancelationWindowEnabled=NotImplemented,
            maxUses=NotImplemented,
            userId=NotImplemented,
            householdId=NotImplemented,
            mediaFileId=NotImplemented,
            mediaId=NotImplemented):
        KalturaEntitlement.__init__(self,
            id,
            productId,
            currentUses,
            endDate,
            currentDate,
            lastViewDate,
            purchaseDate,
            paymentMethod,
            deviceUdid,
            deviceName,
            isCancelationWindowEnabled,
            maxUses,
            userId,
            householdId)

        # Media file identifier
        # @var int
        # @readonly
        self.mediaFileId = mediaFileId

        # Media identifier
        # @var int
        # @readonly
        self.mediaId = mediaId


    PROPERTY_LOADERS = {
        'mediaFileId': getXmlNodeInt, 
        'mediaId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaEntitlement.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPpvEntitlement.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntitlement.toParams(self)
        kparams.put("objectType", "KalturaPpvEntitlement")
        return kparams

    def getMediaFileId(self):
        return self.mediaFileId

    def getMediaId(self):
        return self.mediaId


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionEntitlement(KalturaEntitlement):
    """KalturaSubscriptionEntitlement"""

    def __init__(self,
            id=NotImplemented,
            productId=NotImplemented,
            currentUses=NotImplemented,
            endDate=NotImplemented,
            currentDate=NotImplemented,
            lastViewDate=NotImplemented,
            purchaseDate=NotImplemented,
            paymentMethod=NotImplemented,
            deviceUdid=NotImplemented,
            deviceName=NotImplemented,
            isCancelationWindowEnabled=NotImplemented,
            maxUses=NotImplemented,
            userId=NotImplemented,
            householdId=NotImplemented,
            nextRenewalDate=NotImplemented,
            isRenewableForPurchase=NotImplemented,
            isRenewable=NotImplemented,
            isInGracePeriod=NotImplemented,
            paymentGatewayId=NotImplemented,
            paymentMethodId=NotImplemented,
            scheduledSubscriptionId=NotImplemented,
            unifiedPaymentId=NotImplemented,
            isSuspended=NotImplemented):
        KalturaEntitlement.__init__(self,
            id,
            productId,
            currentUses,
            endDate,
            currentDate,
            lastViewDate,
            purchaseDate,
            paymentMethod,
            deviceUdid,
            deviceName,
            isCancelationWindowEnabled,
            maxUses,
            userId,
            householdId)

        # The date of the next renewal (only for subscription)
        # @var int
        # @readonly
        self.nextRenewalDate = nextRenewalDate

        # Indicates whether the subscription is renewable in this purchase (only for subscription)
        # @var bool
        # @readonly
        self.isRenewableForPurchase = isRenewableForPurchase

        # Indicates whether a subscription is renewable (only for subscription)
        # @var bool
        # @readonly
        self.isRenewable = isRenewable

        # Indicates whether the user is currently in his grace period entitlement
        # @var bool
        # @readonly
        self.isInGracePeriod = isInGracePeriod

        # Payment Gateway identifier
        # @var int
        self.paymentGatewayId = paymentGatewayId

        # Payment Method identifier
        # @var int
        self.paymentMethodId = paymentMethodId

        # Scheduled Subscription Identifier
        # @var int
        # @readonly
        self.scheduledSubscriptionId = scheduledSubscriptionId

        # Unified payment identifier
        # @var int
        # @readonly
        self.unifiedPaymentId = unifiedPaymentId

        # Indicates if the subscription suspended
        # @var bool
        # @readonly
        self.isSuspended = isSuspended


    PROPERTY_LOADERS = {
        'nextRenewalDate': getXmlNodeInt, 
        'isRenewableForPurchase': getXmlNodeBool, 
        'isRenewable': getXmlNodeBool, 
        'isInGracePeriod': getXmlNodeBool, 
        'paymentGatewayId': getXmlNodeInt, 
        'paymentMethodId': getXmlNodeInt, 
        'scheduledSubscriptionId': getXmlNodeInt, 
        'unifiedPaymentId': getXmlNodeInt, 
        'isSuspended': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaEntitlement.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionEntitlement.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaEntitlement.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionEntitlement")
        kparams.addIntIfDefined("paymentGatewayId", self.paymentGatewayId)
        kparams.addIntIfDefined("paymentMethodId", self.paymentMethodId)
        return kparams

    def getNextRenewalDate(self):
        return self.nextRenewalDate

    def getIsRenewableForPurchase(self):
        return self.isRenewableForPurchase

    def getIsRenewable(self):
        return self.isRenewable

    def getIsInGracePeriod(self):
        return self.isInGracePeriod

    def getPaymentGatewayId(self):
        return self.paymentGatewayId

    def setPaymentGatewayId(self, newPaymentGatewayId):
        self.paymentGatewayId = newPaymentGatewayId

    def getPaymentMethodId(self):
        return self.paymentMethodId

    def setPaymentMethodId(self, newPaymentMethodId):
        self.paymentMethodId = newPaymentMethodId

    def getScheduledSubscriptionId(self):
        return self.scheduledSubscriptionId

    def getUnifiedPaymentId(self):
        return self.unifiedPaymentId

    def getIsSuspended(self):
        return self.isSuspended


# @package Kaltura
# @subpackage Client
class KalturaPartnerConfiguration(KalturaObjectBase):
    """Partner  base configuration"""

    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerConfiguration.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPartnerConfiguration")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPartnerConfigurationListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Partner Configurations
        # @var array of KalturaPartnerConfiguration
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaPartnerConfiguration'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerConfigurationListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaPartnerConfigurationListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaConcurrencyPartnerConfig(KalturaPartnerConfiguration):
    """Partner concurrency configuration"""

    def __init__(self,
            deviceFamilyIds=NotImplemented,
            evictionPolicy=NotImplemented):
        KalturaPartnerConfiguration.__init__(self)

        # Comma separated list of device Family Ids order by their priority.
        # @var string
        self.deviceFamilyIds = deviceFamilyIds

        # Policy of eviction devices
        # @var KalturaEvictionPolicyType
        self.evictionPolicy = evictionPolicy


    PROPERTY_LOADERS = {
        'deviceFamilyIds': getXmlNodeText, 
        'evictionPolicy': (KalturaEnumsFactory.createString, "KalturaEvictionPolicyType"), 
    }

    def fromXml(self, node):
        KalturaPartnerConfiguration.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConcurrencyPartnerConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPartnerConfiguration.toParams(self)
        kparams.put("objectType", "KalturaConcurrencyPartnerConfig")
        kparams.addStringIfDefined("deviceFamilyIds", self.deviceFamilyIds)
        kparams.addStringEnumIfDefined("evictionPolicy", self.evictionPolicy)
        return kparams

    def getDeviceFamilyIds(self):
        return self.deviceFamilyIds

    def setDeviceFamilyIds(self, newDeviceFamilyIds):
        self.deviceFamilyIds = newDeviceFamilyIds

    def getEvictionPolicy(self):
        return self.evictionPolicy

    def setEvictionPolicy(self, newEvictionPolicy):
        self.evictionPolicy = newEvictionPolicy


# @package Kaltura
# @subpackage Client
class KalturaBillingPartnerConfig(KalturaPartnerConfiguration):
    """Partner billing configuration"""

    def __init__(self,
            value=NotImplemented,
            type=NotImplemented):
        KalturaPartnerConfiguration.__init__(self)

        # configuration value
        # @var string
        self.value = value

        # partner configuration type
        # @var KalturaPartnerConfigurationType
        self.type = type


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createString, "KalturaPartnerConfigurationType"), 
    }

    def fromXml(self, node):
        KalturaPartnerConfiguration.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBillingPartnerConfig.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPartnerConfiguration.toParams(self)
        kparams.put("objectType", "KalturaBillingPartnerConfig")
        kparams.addStringIfDefined("value", self.value)
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaT(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaT.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaT")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaGenericListResponse(KalturaListResponse):
    """Generic response list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of objects
        # @var array of KalturaT
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaT'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaGenericListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaGenericListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaIntegerValueListResponse(KalturaListResponse):
    """Integer list wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Interger value items
        # @var array of KalturaIntegerValue
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaIntegerValue'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaIntegerValueListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaIntegerValueListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaReport(KalturaObjectBase):
    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReport.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaReport")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaReportListResponse(KalturaListResponse):
    """Reports info wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Reports
        # @var array of KalturaReport
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaReport'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaReportListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaPushParams(KalturaObjectBase):
    def __init__(self,
            token=NotImplemented,
            externalToken=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Device-Application push token
        # @var string
        self.token = token

        # External device token as received from external push provider in exchange for the device token
        # @var string
        self.externalToken = externalToken


    PROPERTY_LOADERS = {
        'token': getXmlNodeText, 
        'externalToken': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPushParams.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaPushParams")
        kparams.addStringIfDefined("token", self.token)
        kparams.addStringIfDefined("externalToken", self.externalToken)
        return kparams

    def getToken(self):
        return self.token

    def setToken(self, newToken):
        self.token = newToken

    def getExternalToken(self):
        return self.externalToken

    def setExternalToken(self, newExternalToken):
        self.externalToken = newExternalToken


# @package Kaltura
# @subpackage Client
class KalturaDeviceReport(KalturaReport):
    def __init__(self,
            partnerId=NotImplemented,
            configurationGroupId=NotImplemented,
            udid=NotImplemented,
            pushParameters=NotImplemented,
            versionNumber=NotImplemented,
            versionPlatform=NotImplemented,
            versionAppName=NotImplemented,
            lastAccessIP=NotImplemented,
            lastAccessDate=NotImplemented,
            userAgent=NotImplemented,
            operationSystem=NotImplemented):
        KalturaReport.__init__(self)

        # Partner unique identifier
        # @var int
        self.partnerId = partnerId

        # Configuration group identifier which the version configuration the device last received belongs to
        # @var string
        self.configurationGroupId = configurationGroupId

        # Device unique identifier
        # @var string
        self.udid = udid

        # Device-Application push parameters
        # @var KalturaPushParams
        self.pushParameters = pushParameters

        # Application version number
        # @var string
        self.versionNumber = versionNumber

        # Application version type
        # @var KalturaPlatform
        self.versionPlatform = versionPlatform

        # Application version name
        # @var string
        self.versionAppName = versionAppName

        # Last access IP
        # @var string
        self.lastAccessIP = lastAccessIP

        # Last device configuration request date
        # @var int
        self.lastAccessDate = lastAccessDate

        # request header property
        # @var string
        self.userAgent = userAgent

        # Request header property
        #             Incase value cannot be found - returns &quot;Unknown 0.0&quot;
        # @var string
        self.operationSystem = operationSystem


    PROPERTY_LOADERS = {
        'partnerId': getXmlNodeInt, 
        'configurationGroupId': getXmlNodeText, 
        'udid': getXmlNodeText, 
        'pushParameters': (KalturaObjectFactory.create, 'KalturaPushParams'), 
        'versionNumber': getXmlNodeText, 
        'versionPlatform': (KalturaEnumsFactory.createString, "KalturaPlatform"), 
        'versionAppName': getXmlNodeText, 
        'lastAccessIP': getXmlNodeText, 
        'lastAccessDate': getXmlNodeInt, 
        'userAgent': getXmlNodeText, 
        'operationSystem': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaReport.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeviceReport.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReport.toParams(self)
        kparams.put("objectType", "KalturaDeviceReport")
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addStringIfDefined("configurationGroupId", self.configurationGroupId)
        kparams.addStringIfDefined("udid", self.udid)
        kparams.addObjectIfDefined("pushParameters", self.pushParameters)
        kparams.addStringIfDefined("versionNumber", self.versionNumber)
        kparams.addStringEnumIfDefined("versionPlatform", self.versionPlatform)
        kparams.addStringIfDefined("versionAppName", self.versionAppName)
        kparams.addStringIfDefined("lastAccessIP", self.lastAccessIP)
        kparams.addIntIfDefined("lastAccessDate", self.lastAccessDate)
        kparams.addStringIfDefined("userAgent", self.userAgent)
        kparams.addStringIfDefined("operationSystem", self.operationSystem)
        return kparams

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getConfigurationGroupId(self):
        return self.configurationGroupId

    def setConfigurationGroupId(self, newConfigurationGroupId):
        self.configurationGroupId = newConfigurationGroupId

    def getUdid(self):
        return self.udid

    def setUdid(self, newUdid):
        self.udid = newUdid

    def getPushParameters(self):
        return self.pushParameters

    def setPushParameters(self, newPushParameters):
        self.pushParameters = newPushParameters

    def getVersionNumber(self):
        return self.versionNumber

    def setVersionNumber(self, newVersionNumber):
        self.versionNumber = newVersionNumber

    def getVersionPlatform(self):
        return self.versionPlatform

    def setVersionPlatform(self, newVersionPlatform):
        self.versionPlatform = newVersionPlatform

    def getVersionAppName(self):
        return self.versionAppName

    def setVersionAppName(self, newVersionAppName):
        self.versionAppName = newVersionAppName

    def getLastAccessIP(self):
        return self.lastAccessIP

    def setLastAccessIP(self, newLastAccessIP):
        self.lastAccessIP = newLastAccessIP

    def getLastAccessDate(self):
        return self.lastAccessDate

    def setLastAccessDate(self, newLastAccessDate):
        self.lastAccessDate = newLastAccessDate

    def getUserAgent(self):
        return self.userAgent

    def setUserAgent(self, newUserAgent):
        self.userAgent = newUserAgent

    def getOperationSystem(self):
        return self.operationSystem

    def setOperationSystem(self, newOperationSystem):
        self.operationSystem = newOperationSystem


# @package Kaltura
# @subpackage Client
class KalturaAssetStructMeta(KalturaObjectBase):
    """Asset statistics"""

    def __init__(self,
            assetStructId=NotImplemented,
            metaId=NotImplemented,
            ingestReferencePath=NotImplemented,
            protectFromIngest=NotImplemented,
            defaultIngestValue=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Asset Struct id (template_id)
        # @var int
        # @readonly
        self.assetStructId = assetStructId

        # Meta id (topic_id)
        # @var int
        # @readonly
        self.metaId = metaId

        # IngestReferencePath
        # @var string
        self.ingestReferencePath = ingestReferencePath

        # ProtectFromIngest
        # @var bool
        self.protectFromIngest = protectFromIngest

        # DefaultIngestValue
        # @var string
        self.defaultIngestValue = defaultIngestValue

        # Specifies when was the Asset Struct Meta was created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the Asset Struct Meta last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate


    PROPERTY_LOADERS = {
        'assetStructId': getXmlNodeInt, 
        'metaId': getXmlNodeInt, 
        'ingestReferencePath': getXmlNodeText, 
        'protectFromIngest': getXmlNodeBool, 
        'defaultIngestValue': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStructMeta.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetStructMeta")
        kparams.addStringIfDefined("ingestReferencePath", self.ingestReferencePath)
        kparams.addBoolIfDefined("protectFromIngest", self.protectFromIngest)
        kparams.addStringIfDefined("defaultIngestValue", self.defaultIngestValue)
        return kparams

    def getAssetStructId(self):
        return self.assetStructId

    def getMetaId(self):
        return self.metaId

    def getIngestReferencePath(self):
        return self.ingestReferencePath

    def setIngestReferencePath(self, newIngestReferencePath):
        self.ingestReferencePath = newIngestReferencePath

    def getProtectFromIngest(self):
        return self.protectFromIngest

    def setProtectFromIngest(self, newProtectFromIngest):
        self.protectFromIngest = newProtectFromIngest

    def getDefaultIngestValue(self):
        return self.defaultIngestValue

    def setDefaultIngestValue(self, newDefaultIngestValue):
        self.defaultIngestValue = newDefaultIngestValue

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate


# @package Kaltura
# @subpackage Client
class KalturaAssetStructMetaListResponse(KalturaListResponse):
    """Asset Struct Metas list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of asset struct metas
        # @var array of KalturaAssetStructMeta
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetStructMeta'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStructMetaListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetStructMetaListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaMediaFileType(KalturaObjectBase):
    """Media-file type"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            status=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            isTrailer=NotImplemented,
            streamerType=NotImplemented,
            drmProfileId=NotImplemented,
            quality=NotImplemented,
            videoCodecs=NotImplemented,
            audioCodecs=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier
        # @var int
        # @readonly
        self.id = id

        # Unique name
        # @var string
        self.name = name

        # Unique description
        # @var string
        self.description = description

        # Indicates if media-file type is active or disabled
        # @var bool
        self.status = status

        # Specifies when was the type was created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the type last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate

        # Specifies whether playback as trailer is allowed
        # @var bool
        # @insertonly
        self.isTrailer = isTrailer

        # Defines playback streamer type
        # @var KalturaMediaFileStreamerType
        # @insertonly
        self.streamerType = streamerType

        # DRM adapter-profile identifier, use -1 for uDRM, 0 for no DRM.
        # @var int
        # @insertonly
        self.drmProfileId = drmProfileId

        # Media file type quality
        # @var KalturaMediaFileTypeQuality
        self.quality = quality

        # List of comma separated video codecs
        # @var string
        self.videoCodecs = videoCodecs

        # List of comma separated audio codecs
        # @var string
        self.audioCodecs = audioCodecs


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'status': getXmlNodeBool, 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
        'isTrailer': getXmlNodeBool, 
        'streamerType': (KalturaEnumsFactory.createString, "KalturaMediaFileStreamerType"), 
        'drmProfileId': getXmlNodeInt, 
        'quality': (KalturaEnumsFactory.createString, "KalturaMediaFileTypeQuality"), 
        'videoCodecs': getXmlNodeText, 
        'audioCodecs': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFileType.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaFileType")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addBoolIfDefined("status", self.status)
        kparams.addBoolIfDefined("isTrailer", self.isTrailer)
        kparams.addStringEnumIfDefined("streamerType", self.streamerType)
        kparams.addIntIfDefined("drmProfileId", self.drmProfileId)
        kparams.addStringEnumIfDefined("quality", self.quality)
        kparams.addStringIfDefined("videoCodecs", self.videoCodecs)
        kparams.addStringIfDefined("audioCodecs", self.audioCodecs)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate

    def getIsTrailer(self):
        return self.isTrailer

    def setIsTrailer(self, newIsTrailer):
        self.isTrailer = newIsTrailer

    def getStreamerType(self):
        return self.streamerType

    def setStreamerType(self, newStreamerType):
        self.streamerType = newStreamerType

    def getDrmProfileId(self):
        return self.drmProfileId

    def setDrmProfileId(self, newDrmProfileId):
        self.drmProfileId = newDrmProfileId

    def getQuality(self):
        return self.quality

    def setQuality(self, newQuality):
        self.quality = newQuality

    def getVideoCodecs(self):
        return self.videoCodecs

    def setVideoCodecs(self, newVideoCodecs):
        self.videoCodecs = newVideoCodecs

    def getAudioCodecs(self):
        return self.audioCodecs

    def setAudioCodecs(self, newAudioCodecs):
        self.audioCodecs = newAudioCodecs


# @package Kaltura
# @subpackage Client
class KalturaMediaFileTypeListResponse(KalturaListResponse):
    """Media-file types list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of media-file types
        # @var array of KalturaMediaFileType
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaMediaFileType'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFileTypeListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaMediaFileTypeListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaChannelListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of channels
        # @var array of KalturaChannel
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaChannel'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaChannelListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaImage(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            version=NotImplemented,
            imageTypeId=NotImplemented,
            imageObjectId=NotImplemented,
            imageObjectType=NotImplemented,
            status=NotImplemented,
            url=NotImplemented,
            contentId=NotImplemented,
            isDefault=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Image ID
        # @var int
        # @readonly
        self.id = id

        # Image version
        # @var string
        # @readonly
        self.version = version

        # Image type ID
        # @var int
        self.imageTypeId = imageTypeId

        # ID of the object the image is related to
        # @var int
        self.imageObjectId = imageObjectId

        # Type of the object the image is related to
        # @var KalturaImageObjectType
        self.imageObjectType = imageObjectType

        # Image content status
        # @var KalturaImageStatus
        # @readonly
        self.status = status

        # Image URL
        # @var string
        # @readonly
        self.url = url

        # Image content ID
        # @var string
        # @readonly
        self.contentId = contentId

        # Specifies if the image is default for atleast one image type.
        # @var bool
        # @readonly
        self.isDefault = isDefault


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'version': getXmlNodeText, 
        'imageTypeId': getXmlNodeInt, 
        'imageObjectId': getXmlNodeInt, 
        'imageObjectType': (KalturaEnumsFactory.createString, "KalturaImageObjectType"), 
        'status': (KalturaEnumsFactory.createString, "KalturaImageStatus"), 
        'url': getXmlNodeText, 
        'contentId': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaImage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaImage")
        kparams.addIntIfDefined("imageTypeId", self.imageTypeId)
        kparams.addIntIfDefined("imageObjectId", self.imageObjectId)
        kparams.addStringEnumIfDefined("imageObjectType", self.imageObjectType)
        return kparams

    def getId(self):
        return self.id

    def getVersion(self):
        return self.version

    def getImageTypeId(self):
        return self.imageTypeId

    def setImageTypeId(self, newImageTypeId):
        self.imageTypeId = newImageTypeId

    def getImageObjectId(self):
        return self.imageObjectId

    def setImageObjectId(self, newImageObjectId):
        self.imageObjectId = newImageObjectId

    def getImageObjectType(self):
        return self.imageObjectType

    def setImageObjectType(self, newImageObjectType):
        self.imageObjectType = newImageObjectType

    def getStatus(self):
        return self.status

    def getUrl(self):
        return self.url

    def getContentId(self):
        return self.contentId

    def getIsDefault(self):
        return self.isDefault


# @package Kaltura
# @subpackage Client
class KalturaImageListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of images
        # @var array of KalturaImage
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaImage'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaImageListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaImageListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaRatio(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            height=NotImplemented,
            width=NotImplemented,
            precisionPrecentage=NotImplemented):
        KalturaObjectBase.__init__(self)

        # ID
        # @var int
        # @readonly
        self.id = id

        # Name
        # @var string
        # @insertonly
        self.name = name

        # Height
        # @var int
        # @insertonly
        self.height = height

        # Width
        # @var int
        # @insertonly
        self.width = width

        # Accepted error margin precentage of an image uploaded for this ratio
        #             0 - no validation, everything accepted
        # @var int
        self.precisionPrecentage = precisionPrecentage


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'height': getXmlNodeInt, 
        'width': getXmlNodeInt, 
        'precisionPrecentage': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRatio.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRatio")
        kparams.addStringIfDefined("name", self.name)
        kparams.addIntIfDefined("height", self.height)
        kparams.addIntIfDefined("width", self.width)
        kparams.addIntIfDefined("precisionPrecentage", self.precisionPrecentage)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getHeight(self):
        return self.height

    def setHeight(self, newHeight):
        self.height = newHeight

    def getWidth(self):
        return self.width

    def setWidth(self, newWidth):
        self.width = newWidth

    def getPrecisionPrecentage(self):
        return self.precisionPrecentage

    def setPrecisionPrecentage(self, newPrecisionPrecentage):
        self.precisionPrecentage = newPrecisionPrecentage


# @package Kaltura
# @subpackage Client
class KalturaRatioListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of ratios
        # @var array of KalturaRatio
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaRatio'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRatioListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRatioListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaTag(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            tag=NotImplemented,
            multilingualTag=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Tag id
        # @var int
        # @readonly
        self.id = id

        # Tag Type
        # @var int
        self.type = type

        # Tag
        # @var string
        # @readonly
        self.tag = tag

        # Tag
        # @var array of KalturaTranslationToken
        self.multilingualTag = multilingualTag


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'type': getXmlNodeInt, 
        'tag': getXmlNodeText, 
        'multilingualTag': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTag.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaTag")
        kparams.addIntIfDefined("type", self.type)
        kparams.addArrayIfDefined("multilingualTag", self.multilingualTag)
        return kparams

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getTag(self):
        return self.tag

    def getMultilingualTag(self):
        return self.multilingualTag

    def setMultilingualTag(self, newMultilingualTag):
        self.multilingualTag = newMultilingualTag


# @package Kaltura
# @subpackage Client
class KalturaTagListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of partner tags
        # @var array of KalturaTag
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaTag'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTagListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaTagListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAsset(KalturaObjectBase):
    """Asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented,
            metas=NotImplemented,
            tags=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            externalId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique identifier for the asset
        # @var int
        # @readonly
        self.id = id

        # Identifies the asset type (EPG, Recording, Movie, TV Series, etc). 
        #             Possible values: 0 - EPG linear programs, 1 - Recording; or any asset type ID according to the asset types IDs defined in the system.
        # @var int
        # @insertonly
        self.type = type

        # Asset name
        # @var string
        # @readonly
        self.name = name

        # Asset name
        # @var array of KalturaTranslationToken
        self.multilingualName = multilingualName

        # Asset description
        # @var string
        # @readonly
        self.description = description

        # Asset description
        # @var array of KalturaTranslationToken
        self.multilingualDescription = multilingualDescription

        # Collection of images details that can be used to represent this asset
        # @var array of KalturaMediaImage
        # @readonly
        self.images = images

        # Files
        # @var array of KalturaMediaFile
        # @readonly
        self.mediaFiles = mediaFiles

        # Dynamic collection of key-value pairs according to the String Meta defined in the system
        # @var map
        self.metas = metas

        # Dynamic collection of key-value pairs according to the Tag Types defined in the system
        # @var map
        self.tags = tags

        # Date and time represented as epoch. For VOD - since when the asset is available in the catalog. For EPG/Linear - when the program is aired (can be in the future).
        # @var int
        self.startDate = startDate

        # Date and time represented as epoch. For VOD - till when the asset be available in the catalog. For EPG/Linear - program end time and date
        # @var int
        self.endDate = endDate

        # Specifies when was the Asset was created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the Asset last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate

        # External identifier for the asset
        # @var string
        self.externalId = externalId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'type': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'multilingualName': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'description': getXmlNodeText, 
        'multilingualDescription': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'images': (KalturaObjectFactory.createArray, 'KalturaMediaImage'), 
        'mediaFiles': (KalturaObjectFactory.createArray, 'KalturaMediaFile'), 
        'metas': (KalturaObjectFactory.createMap, 'KalturaValue'), 
        'tags': (KalturaObjectFactory.createMap, 'KalturaMultilingualStringValueArray'), 
        'startDate': getXmlNodeInt, 
        'endDate': getXmlNodeInt, 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
        'externalId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAsset")
        kparams.addIntIfDefined("type", self.type)
        kparams.addArrayIfDefined("multilingualName", self.multilingualName)
        kparams.addArrayIfDefined("multilingualDescription", self.multilingualDescription)
        kparams.addMapIfDefined("metas", self.metas)
        kparams.addMapIfDefined("tags", self.tags)
        kparams.addIntIfDefined("startDate", self.startDate)
        kparams.addIntIfDefined("endDate", self.endDate)
        kparams.addStringIfDefined("externalId", self.externalId)
        return kparams

    def getId(self):
        return self.id

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType

    def getName(self):
        return self.name

    def getMultilingualName(self):
        return self.multilingualName

    def setMultilingualName(self, newMultilingualName):
        self.multilingualName = newMultilingualName

    def getDescription(self):
        return self.description

    def getMultilingualDescription(self):
        return self.multilingualDescription

    def setMultilingualDescription(self, newMultilingualDescription):
        self.multilingualDescription = newMultilingualDescription

    def getImages(self):
        return self.images

    def getMediaFiles(self):
        return self.mediaFiles

    def getMetas(self):
        return self.metas

    def setMetas(self, newMetas):
        self.metas = newMetas

    def getTags(self):
        return self.tags

    def setTags(self, newTags):
        self.tags = newTags

    def getStartDate(self):
        return self.startDate

    def setStartDate(self, newStartDate):
        self.startDate = newStartDate

    def getEndDate(self):
        return self.endDate

    def setEndDate(self, newEndDate):
        self.endDate = newEndDate

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId


# @package Kaltura
# @subpackage Client
class KalturaAssetListResponse(KalturaListResponse):
    """Asset wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaAsset
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAsset'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaMediaAsset(KalturaAsset):
    """Media-asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented,
            metas=NotImplemented,
            tags=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            externalId=NotImplemented,
            externalIds=NotImplemented,
            entryId=NotImplemented,
            deviceRuleId=NotImplemented,
            geoBlockRuleId=NotImplemented,
            status=NotImplemented):
        KalturaAsset.__init__(self,
            id,
            type,
            name,
            multilingualName,
            description,
            multilingualDescription,
            images,
            mediaFiles,
            metas,
            tags,
            startDate,
            endDate,
            createDate,
            updateDate,
            externalId)

        # External identifiers
        # @var string
        self.externalIds = externalIds

        # Entry Identifier
        # @var string
        self.entryId = entryId

        # Device rule identifier
        # @var int
        self.deviceRuleId = deviceRuleId

        # Geo block rule identifier
        # @var int
        self.geoBlockRuleId = geoBlockRuleId

        # The media asset status
        # @var bool
        self.status = status


    PROPERTY_LOADERS = {
        'externalIds': getXmlNodeText, 
        'entryId': getXmlNodeText, 
        'deviceRuleId': getXmlNodeInt, 
        'geoBlockRuleId': getXmlNodeInt, 
        'status': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaMediaAsset")
        kparams.addStringIfDefined("externalIds", self.externalIds)
        kparams.addStringIfDefined("entryId", self.entryId)
        kparams.addIntIfDefined("deviceRuleId", self.deviceRuleId)
        kparams.addIntIfDefined("geoBlockRuleId", self.geoBlockRuleId)
        kparams.addBoolIfDefined("status", self.status)
        return kparams

    def getExternalIds(self):
        return self.externalIds

    def setExternalIds(self, newExternalIds):
        self.externalIds = newExternalIds

    def getEntryId(self):
        return self.entryId

    def setEntryId(self, newEntryId):
        self.entryId = newEntryId

    def getDeviceRuleId(self):
        return self.deviceRuleId

    def setDeviceRuleId(self, newDeviceRuleId):
        self.deviceRuleId = newDeviceRuleId

    def getGeoBlockRuleId(self):
        return self.geoBlockRuleId

    def setGeoBlockRuleId(self, newGeoBlockRuleId):
        self.geoBlockRuleId = newGeoBlockRuleId

    def getStatus(self):
        return self.status

    def setStatus(self, newStatus):
        self.status = newStatus


# @package Kaltura
# @subpackage Client
class KalturaLinearMediaAsset(KalturaMediaAsset):
    """Linear media asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented,
            metas=NotImplemented,
            tags=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            externalId=NotImplemented,
            externalIds=NotImplemented,
            entryId=NotImplemented,
            deviceRuleId=NotImplemented,
            geoBlockRuleId=NotImplemented,
            status=NotImplemented,
            enableCdvrState=NotImplemented,
            enableCatchUpState=NotImplemented,
            enableStartOverState=NotImplemented,
            bufferCatchUp=NotImplemented,
            bufferTrickPlay=NotImplemented,
            enableRecordingPlaybackNonEntitledChannelState=NotImplemented,
            enableTrickPlayState=NotImplemented,
            externalEpgIngestId=NotImplemented,
            externalCdvrId=NotImplemented,
            cdvrEnabled=NotImplemented,
            catchUpEnabled=NotImplemented,
            startOverEnabled=NotImplemented,
            summedCatchUpBuffer=NotImplemented,
            summedTrickPlayBuffer=NotImplemented,
            recordingPlaybackNonEntitledChannelEnabled=NotImplemented,
            trickPlayEnabled=NotImplemented,
            channelType=NotImplemented):
        KalturaMediaAsset.__init__(self,
            id,
            type,
            name,
            multilingualName,
            description,
            multilingualDescription,
            images,
            mediaFiles,
            metas,
            tags,
            startDate,
            endDate,
            createDate,
            updateDate,
            externalId,
            externalIds,
            entryId,
            deviceRuleId,
            geoBlockRuleId,
            status)

        # Enable CDVR, configuration only
        # @var KalturaTimeShiftedTvState
        self.enableCdvrState = enableCdvrState

        # Enable catch-up, configuration only
        # @var KalturaTimeShiftedTvState
        self.enableCatchUpState = enableCatchUpState

        # Enable start over, configuration only
        # @var KalturaTimeShiftedTvState
        self.enableStartOverState = enableStartOverState

        # buffer Catch-up, configuration only
        # @var int
        self.bufferCatchUp = bufferCatchUp

        # buffer Trick-play, configuration only
        # @var int
        self.bufferTrickPlay = bufferTrickPlay

        # Enable Recording playback for non entitled channel, configuration only
        # @var KalturaTimeShiftedTvState
        self.enableRecordingPlaybackNonEntitledChannelState = enableRecordingPlaybackNonEntitledChannelState

        # Enable trick-play, configuration only
        # @var KalturaTimeShiftedTvState
        self.enableTrickPlayState = enableTrickPlayState

        # External identifier used when ingesting programs for this linear media asset
        # @var string
        self.externalEpgIngestId = externalEpgIngestId

        # External identifier for the CDVR
        # @var string
        self.externalCdvrId = externalCdvrId

        # Is CDVR enabled for this asset
        # @var bool
        # @readonly
        self.cdvrEnabled = cdvrEnabled

        # Is catch-up enabled for this asset
        # @var bool
        # @readonly
        self.catchUpEnabled = catchUpEnabled

        # Is start over enabled for this asset
        # @var bool
        # @readonly
        self.startOverEnabled = startOverEnabled

        # summed Catch-up buffer, the TimeShiftedTvPartnerSettings are also taken into consideration
        # @var int
        # @readonly
        self.summedCatchUpBuffer = summedCatchUpBuffer

        # summed Trick-play buffer, the TimeShiftedTvPartnerSettings are also taken into consideration
        # @var int
        # @readonly
        self.summedTrickPlayBuffer = summedTrickPlayBuffer

        # Is recording playback for non entitled channel enabled for this asset
        # @var bool
        # @readonly
        self.recordingPlaybackNonEntitledChannelEnabled = recordingPlaybackNonEntitledChannelEnabled

        # Is trick-play enabled for this asset
        # @var bool
        # @readonly
        self.trickPlayEnabled = trickPlayEnabled

        # channel type, possible values: UNKNOWN, DTT, OTT, DTT_AND_OTT
        # @var KalturaLinearChannelType
        self.channelType = channelType


    PROPERTY_LOADERS = {
        'enableCdvrState': (KalturaEnumsFactory.createString, "KalturaTimeShiftedTvState"), 
        'enableCatchUpState': (KalturaEnumsFactory.createString, "KalturaTimeShiftedTvState"), 
        'enableStartOverState': (KalturaEnumsFactory.createString, "KalturaTimeShiftedTvState"), 
        'bufferCatchUp': getXmlNodeInt, 
        'bufferTrickPlay': getXmlNodeInt, 
        'enableRecordingPlaybackNonEntitledChannelState': (KalturaEnumsFactory.createString, "KalturaTimeShiftedTvState"), 
        'enableTrickPlayState': (KalturaEnumsFactory.createString, "KalturaTimeShiftedTvState"), 
        'externalEpgIngestId': getXmlNodeText, 
        'externalCdvrId': getXmlNodeText, 
        'cdvrEnabled': getXmlNodeBool, 
        'catchUpEnabled': getXmlNodeBool, 
        'startOverEnabled': getXmlNodeBool, 
        'summedCatchUpBuffer': getXmlNodeInt, 
        'summedTrickPlayBuffer': getXmlNodeInt, 
        'recordingPlaybackNonEntitledChannelEnabled': getXmlNodeBool, 
        'trickPlayEnabled': getXmlNodeBool, 
        'channelType': (KalturaEnumsFactory.createString, "KalturaLinearChannelType"), 
    }

    def fromXml(self, node):
        KalturaMediaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLinearMediaAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaMediaAsset.toParams(self)
        kparams.put("objectType", "KalturaLinearMediaAsset")
        kparams.addStringEnumIfDefined("enableCdvrState", self.enableCdvrState)
        kparams.addStringEnumIfDefined("enableCatchUpState", self.enableCatchUpState)
        kparams.addStringEnumIfDefined("enableStartOverState", self.enableStartOverState)
        kparams.addIntIfDefined("bufferCatchUp", self.bufferCatchUp)
        kparams.addIntIfDefined("bufferTrickPlay", self.bufferTrickPlay)
        kparams.addStringEnumIfDefined("enableRecordingPlaybackNonEntitledChannelState", self.enableRecordingPlaybackNonEntitledChannelState)
        kparams.addStringEnumIfDefined("enableTrickPlayState", self.enableTrickPlayState)
        kparams.addStringIfDefined("externalEpgIngestId", self.externalEpgIngestId)
        kparams.addStringIfDefined("externalCdvrId", self.externalCdvrId)
        kparams.addStringEnumIfDefined("channelType", self.channelType)
        return kparams

    def getEnableCdvrState(self):
        return self.enableCdvrState

    def setEnableCdvrState(self, newEnableCdvrState):
        self.enableCdvrState = newEnableCdvrState

    def getEnableCatchUpState(self):
        return self.enableCatchUpState

    def setEnableCatchUpState(self, newEnableCatchUpState):
        self.enableCatchUpState = newEnableCatchUpState

    def getEnableStartOverState(self):
        return self.enableStartOverState

    def setEnableStartOverState(self, newEnableStartOverState):
        self.enableStartOverState = newEnableStartOverState

    def getBufferCatchUp(self):
        return self.bufferCatchUp

    def setBufferCatchUp(self, newBufferCatchUp):
        self.bufferCatchUp = newBufferCatchUp

    def getBufferTrickPlay(self):
        return self.bufferTrickPlay

    def setBufferTrickPlay(self, newBufferTrickPlay):
        self.bufferTrickPlay = newBufferTrickPlay

    def getEnableRecordingPlaybackNonEntitledChannelState(self):
        return self.enableRecordingPlaybackNonEntitledChannelState

    def setEnableRecordingPlaybackNonEntitledChannelState(self, newEnableRecordingPlaybackNonEntitledChannelState):
        self.enableRecordingPlaybackNonEntitledChannelState = newEnableRecordingPlaybackNonEntitledChannelState

    def getEnableTrickPlayState(self):
        return self.enableTrickPlayState

    def setEnableTrickPlayState(self, newEnableTrickPlayState):
        self.enableTrickPlayState = newEnableTrickPlayState

    def getExternalEpgIngestId(self):
        return self.externalEpgIngestId

    def setExternalEpgIngestId(self, newExternalEpgIngestId):
        self.externalEpgIngestId = newExternalEpgIngestId

    def getExternalCdvrId(self):
        return self.externalCdvrId

    def setExternalCdvrId(self, newExternalCdvrId):
        self.externalCdvrId = newExternalCdvrId

    def getCdvrEnabled(self):
        return self.cdvrEnabled

    def getCatchUpEnabled(self):
        return self.catchUpEnabled

    def getStartOverEnabled(self):
        return self.startOverEnabled

    def getSummedCatchUpBuffer(self):
        return self.summedCatchUpBuffer

    def getSummedTrickPlayBuffer(self):
        return self.summedTrickPlayBuffer

    def getRecordingPlaybackNonEntitledChannelEnabled(self):
        return self.recordingPlaybackNonEntitledChannelEnabled

    def getTrickPlayEnabled(self):
        return self.trickPlayEnabled

    def getChannelType(self):
        return self.channelType

    def setChannelType(self, newChannelType):
        self.channelType = newChannelType


# @package Kaltura
# @subpackage Client
class KalturaProgramAsset(KalturaAsset):
    """Program-asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented,
            metas=NotImplemented,
            tags=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            externalId=NotImplemented,
            epgChannelId=NotImplemented,
            epgId=NotImplemented,
            relatedMediaId=NotImplemented,
            crid=NotImplemented,
            linearAssetId=NotImplemented):
        KalturaAsset.__init__(self,
            id,
            type,
            name,
            multilingualName,
            description,
            multilingualDescription,
            images,
            mediaFiles,
            metas,
            tags,
            startDate,
            endDate,
            createDate,
            updateDate,
            externalId)

        # EPG channel identifier
        # @var int
        self.epgChannelId = epgChannelId

        # EPG identifier
        # @var string
        self.epgId = epgId

        # Ralated media identifier
        # @var int
        self.relatedMediaId = relatedMediaId

        # Unique identifier for the program
        # @var string
        self.crid = crid

        # Id of linear media asset
        # @var int
        self.linearAssetId = linearAssetId


    PROPERTY_LOADERS = {
        'epgChannelId': getXmlNodeInt, 
        'epgId': getXmlNodeText, 
        'relatedMediaId': getXmlNodeInt, 
        'crid': getXmlNodeText, 
        'linearAssetId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProgramAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAsset.toParams(self)
        kparams.put("objectType", "KalturaProgramAsset")
        kparams.addIntIfDefined("epgChannelId", self.epgChannelId)
        kparams.addStringIfDefined("epgId", self.epgId)
        kparams.addIntIfDefined("relatedMediaId", self.relatedMediaId)
        kparams.addStringIfDefined("crid", self.crid)
        kparams.addIntIfDefined("linearAssetId", self.linearAssetId)
        return kparams

    def getEpgChannelId(self):
        return self.epgChannelId

    def setEpgChannelId(self, newEpgChannelId):
        self.epgChannelId = newEpgChannelId

    def getEpgId(self):
        return self.epgId

    def setEpgId(self, newEpgId):
        self.epgId = newEpgId

    def getRelatedMediaId(self):
        return self.relatedMediaId

    def setRelatedMediaId(self, newRelatedMediaId):
        self.relatedMediaId = newRelatedMediaId

    def getCrid(self):
        return self.crid

    def setCrid(self, newCrid):
        self.crid = newCrid

    def getLinearAssetId(self):
        return self.linearAssetId

    def setLinearAssetId(self, newLinearAssetId):
        self.linearAssetId = newLinearAssetId


# @package Kaltura
# @subpackage Client
class KalturaRecordingAsset(KalturaProgramAsset):
    """Recording-asset info"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            description=NotImplemented,
            multilingualDescription=NotImplemented,
            images=NotImplemented,
            mediaFiles=NotImplemented,
            metas=NotImplemented,
            tags=NotImplemented,
            startDate=NotImplemented,
            endDate=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            externalId=NotImplemented,
            epgChannelId=NotImplemented,
            epgId=NotImplemented,
            relatedMediaId=NotImplemented,
            crid=NotImplemented,
            linearAssetId=NotImplemented,
            recordingId=NotImplemented,
            recordingType=NotImplemented):
        KalturaProgramAsset.__init__(self,
            id,
            type,
            name,
            multilingualName,
            description,
            multilingualDescription,
            images,
            mediaFiles,
            metas,
            tags,
            startDate,
            endDate,
            createDate,
            updateDate,
            externalId,
            epgChannelId,
            epgId,
            relatedMediaId,
            crid,
            linearAssetId)

        # Recording identifier
        # @var string
        self.recordingId = recordingId

        # Recording Type: single/season/series
        # @var KalturaRecordingType
        self.recordingType = recordingType


    PROPERTY_LOADERS = {
        'recordingId': getXmlNodeText, 
        'recordingType': (KalturaEnumsFactory.createString, "KalturaRecordingType"), 
    }

    def fromXml(self, node):
        KalturaProgramAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecordingAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaProgramAsset.toParams(self)
        kparams.put("objectType", "KalturaRecordingAsset")
        kparams.addStringIfDefined("recordingId", self.recordingId)
        kparams.addStringEnumIfDefined("recordingType", self.recordingType)
        return kparams

    def getRecordingId(self):
        return self.recordingId

    def setRecordingId(self, newRecordingId):
        self.recordingId = newRecordingId

    def getRecordingType(self):
        return self.recordingType

    def setRecordingType(self, newRecordingType):
        self.recordingType = newRecordingType


# @package Kaltura
# @subpackage Client
class KalturaAssetStruct(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            systemName=NotImplemented,
            isProtected=NotImplemented,
            metaIds=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented,
            features=NotImplemented,
            pluralName=NotImplemented,
            parentId=NotImplemented,
            connectingMetaId=NotImplemented,
            connectedParentMetaId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Asset Struct id
        # @var int
        # @readonly
        self.id = id

        # Asset struct name for the partner
        # @var string
        # @readonly
        self.name = name

        # Asset struct name for the partner
        # @var array of KalturaTranslationToken
        self.multilingualName = multilingualName

        # Asset Struct system name for the partner
        # @var string
        self.systemName = systemName

        # Is the Asset Struct protected by the system
        # @var bool
        self.isProtected = isProtected

        # A list of comma separated meta ids associated with this asset struct, returned according to the order.
        # @var string
        self.metaIds = metaIds

        # Specifies when was the Asset Struct was created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the Asset Struct last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate

        # List of supported features
        # @var string
        self.features = features

        # Plural Name
        # @var string
        self.pluralName = pluralName

        # AssetStruct parent Id
        # @var int
        self.parentId = parentId

        # connectingMetaId
        # @var int
        self.connectingMetaId = connectingMetaId

        # connectedParentMetaId
        # @var int
        self.connectedParentMetaId = connectedParentMetaId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'multilingualName': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'systemName': getXmlNodeText, 
        'isProtected': getXmlNodeBool, 
        'metaIds': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
        'features': getXmlNodeText, 
        'pluralName': getXmlNodeText, 
        'parentId': getXmlNodeInt, 
        'connectingMetaId': getXmlNodeInt, 
        'connectedParentMetaId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStruct.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetStruct")
        kparams.addArrayIfDefined("multilingualName", self.multilingualName)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addBoolIfDefined("isProtected", self.isProtected)
        kparams.addStringIfDefined("metaIds", self.metaIds)
        kparams.addStringIfDefined("features", self.features)
        kparams.addStringIfDefined("pluralName", self.pluralName)
        kparams.addIntIfDefined("parentId", self.parentId)
        kparams.addIntIfDefined("connectingMetaId", self.connectingMetaId)
        kparams.addIntIfDefined("connectedParentMetaId", self.connectedParentMetaId)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getMultilingualName(self):
        return self.multilingualName

    def setMultilingualName(self, newMultilingualName):
        self.multilingualName = newMultilingualName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getIsProtected(self):
        return self.isProtected

    def setIsProtected(self, newIsProtected):
        self.isProtected = newIsProtected

    def getMetaIds(self):
        return self.metaIds

    def setMetaIds(self, newMetaIds):
        self.metaIds = newMetaIds

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate

    def getFeatures(self):
        return self.features

    def setFeatures(self, newFeatures):
        self.features = newFeatures

    def getPluralName(self):
        return self.pluralName

    def setPluralName(self, newPluralName):
        self.pluralName = newPluralName

    def getParentId(self):
        return self.parentId

    def setParentId(self, newParentId):
        self.parentId = newParentId

    def getConnectingMetaId(self):
        return self.connectingMetaId

    def setConnectingMetaId(self, newConnectingMetaId):
        self.connectingMetaId = newConnectingMetaId

    def getConnectedParentMetaId(self):
        return self.connectedParentMetaId

    def setConnectedParentMetaId(self, newConnectedParentMetaId):
        self.connectedParentMetaId = newConnectedParentMetaId


# @package Kaltura
# @subpackage Client
class KalturaAssetStructListResponse(KalturaListResponse):
    """Asset Structs list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of asset structs
        # @var array of KalturaAssetStruct
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetStruct'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStructListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetStructListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaImageType(KalturaObjectBase):
    """Image type"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            systemName=NotImplemented,
            ratioId=NotImplemented,
            helpText=NotImplemented,
            defaultImageId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Image type ID
        # @var int
        # @readonly
        self.id = id

        # Name
        # @var string
        self.name = name

        # System name
        # @var string
        self.systemName = systemName

        # Ration ID
        # @var int
        self.ratioId = ratioId

        # Help text
        # @var string
        self.helpText = helpText

        # Default image ID
        # @var int
        self.defaultImageId = defaultImageId


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'ratioId': getXmlNodeInt, 
        'helpText': getXmlNodeText, 
        'defaultImageId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaImageType.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaImageType")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addIntIfDefined("ratioId", self.ratioId)
        kparams.addStringIfDefined("helpText", self.helpText)
        kparams.addIntIfDefined("defaultImageId", self.defaultImageId)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getRatioId(self):
        return self.ratioId

    def setRatioId(self, newRatioId):
        self.ratioId = newRatioId

    def getHelpText(self):
        return self.helpText

    def setHelpText(self, newHelpText):
        self.helpText = newHelpText

    def getDefaultImageId(self):
        return self.defaultImageId

    def setDefaultImageId(self, newDefaultImageId):
        self.defaultImageId = newDefaultImageId


# @package Kaltura
# @subpackage Client
class KalturaImageTypeListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of partner image types
        # @var array of KalturaImageType
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaImageType'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaImageTypeListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaImageTypeListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetCount(KalturaObjectBase):
    """Asset count - represents a specific value of the field, its count and its sub groups."""

    def __init__(self,
            value=NotImplemented,
            count=NotImplemented,
            subs=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Value
        # @var string
        self.value = value

        # Count
        # @var int
        self.count = count

        # Sub groups
        # @var array of KalturaAssetsCount
        self.subs = subs


    PROPERTY_LOADERS = {
        'value': getXmlNodeText, 
        'count': getXmlNodeInt, 
        'subs': (KalturaObjectFactory.createArray, 'KalturaAssetsCount'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetCount.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetCount")
        kparams.addStringIfDefined("value", self.value)
        kparams.addIntIfDefined("count", self.count)
        kparams.addArrayIfDefined("subs", self.subs)
        return kparams

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

    def getCount(self):
        return self.count

    def setCount(self, newCount):
        self.count = newCount

    def getSubs(self):
        return self.subs

    def setSubs(self, newSubs):
        self.subs = newSubs


# @package Kaltura
# @subpackage Client
class KalturaAssetsCount(KalturaObjectBase):
    """Single aggregation objects"""

    def __init__(self,
            field=NotImplemented,
            objects=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Field name
        # @var string
        self.field = field

        # Values, their count and sub groups
        # @var array of KalturaAssetCount
        self.objects = objects


    PROPERTY_LOADERS = {
        'field': getXmlNodeText, 
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetCount'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetsCount.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetsCount")
        kparams.addStringIfDefined("field", self.field)
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getField(self):
        return self.field

    def setField(self, newField):
        self.field = newField

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetCountListResponse(KalturaListResponse):
    """Asset counts wrapper - represents a group"""

    def __init__(self,
            totalCount=NotImplemented,
            assetsCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Count of assets that match filter result, regardless of group by result
        # @var int
        self.assetsCount = assetsCount

        # List of groupings (field name and sub-list of values and their counts)
        # @var array of KalturaAssetsCount
        self.objects = objects


    PROPERTY_LOADERS = {
        'assetsCount': getXmlNodeInt, 
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetsCount'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetCountListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetCountListResponse")
        kparams.addIntIfDefined("assetsCount", self.assetsCount)
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getAssetsCount(self):
        return self.assetsCount

    def setAssetsCount(self, newAssetsCount):
        self.assetsCount = newAssetsCount

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSlimAsset(KalturaObjectBase):
    """Slim Asset Details"""

    def __init__(self,
            id=NotImplemented,
            type=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Internal identifier of the asset
        # @var string
        # @insertonly
        self.id = id

        # The type of the asset. Possible values: media, recording, epg
        # @var KalturaAssetType
        # @insertonly
        self.type = type


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'type': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSlimAsset.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSlimAsset")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaBookmarkPlayerData(KalturaObjectBase):
    def __init__(self,
            action=NotImplemented,
            averageBitrate=NotImplemented,
            totalBitrate=NotImplemented,
            currentBitrate=NotImplemented,
            fileId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Action
        # @var KalturaBookmarkActionType
        self.action = action

        # Average Bitrate
        # @var int
        self.averageBitrate = averageBitrate

        # Total Bitrate
        # @var int
        self.totalBitrate = totalBitrate

        # Current Bitrate
        # @var int
        self.currentBitrate = currentBitrate

        # Identifier of the file
        # @var int
        self.fileId = fileId


    PROPERTY_LOADERS = {
        'action': (KalturaEnumsFactory.createString, "KalturaBookmarkActionType"), 
        'averageBitrate': getXmlNodeInt, 
        'totalBitrate': getXmlNodeInt, 
        'currentBitrate': getXmlNodeInt, 
        'fileId': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBookmarkPlayerData.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBookmarkPlayerData")
        kparams.addStringEnumIfDefined("action", self.action)
        kparams.addIntIfDefined("averageBitrate", self.averageBitrate)
        kparams.addIntIfDefined("totalBitrate", self.totalBitrate)
        kparams.addIntIfDefined("currentBitrate", self.currentBitrate)
        kparams.addIntIfDefined("fileId", self.fileId)
        return kparams

    def getAction(self):
        return self.action

    def setAction(self, newAction):
        self.action = newAction

    def getAverageBitrate(self):
        return self.averageBitrate

    def setAverageBitrate(self, newAverageBitrate):
        self.averageBitrate = newAverageBitrate

    def getTotalBitrate(self):
        return self.totalBitrate

    def setTotalBitrate(self, newTotalBitrate):
        self.totalBitrate = newTotalBitrate

    def getCurrentBitrate(self):
        return self.currentBitrate

    def setCurrentBitrate(self, newCurrentBitrate):
        self.currentBitrate = newCurrentBitrate

    def getFileId(self):
        return self.fileId

    def setFileId(self, newFileId):
        self.fileId = newFileId


# @package Kaltura
# @subpackage Client
class KalturaBookmark(KalturaSlimAsset):
    def __init__(self,
            id=NotImplemented,
            type=NotImplemented,
            userId=NotImplemented,
            position=NotImplemented,
            positionOwner=NotImplemented,
            finishedWatching=NotImplemented,
            playerData=NotImplemented,
            programId=NotImplemented,
            isReportingMode=NotImplemented):
        KalturaSlimAsset.__init__(self,
            id,
            type)

        # User identifier
        # @var string
        # @readonly
        self.userId = userId

        # The position of the user in the specific asset (in seconds)
        # @var int
        # @insertonly
        self.position = position

        # Indicates who is the owner of this position
        # @var KalturaPositionOwner
        # @readonly
        self.positionOwner = positionOwner

        # Specifies whether the user&#39;s current position exceeded 95% of the duration
        # @var bool
        # @readonly
        self.finishedWatching = finishedWatching

        # Insert only player data
        # @var KalturaBookmarkPlayerData
        self.playerData = playerData

        # Program Id
        # @var int
        self.programId = programId

        # Indicates if the current request is in reporting mode (hit)
        # @var bool
        self.isReportingMode = isReportingMode


    PROPERTY_LOADERS = {
        'userId': getXmlNodeText, 
        'position': getXmlNodeInt, 
        'positionOwner': (KalturaEnumsFactory.createString, "KalturaPositionOwner"), 
        'finishedWatching': getXmlNodeBool, 
        'playerData': (KalturaObjectFactory.create, 'KalturaBookmarkPlayerData'), 
        'programId': getXmlNodeInt, 
        'isReportingMode': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaSlimAsset.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBookmark.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSlimAsset.toParams(self)
        kparams.put("objectType", "KalturaBookmark")
        kparams.addIntIfDefined("position", self.position)
        kparams.addObjectIfDefined("playerData", self.playerData)
        kparams.addIntIfDefined("programId", self.programId)
        kparams.addBoolIfDefined("isReportingMode", self.isReportingMode)
        return kparams

    def getUserId(self):
        return self.userId

    def getPosition(self):
        return self.position

    def setPosition(self, newPosition):
        self.position = newPosition

    def getPositionOwner(self):
        return self.positionOwner

    def getFinishedWatching(self):
        return self.finishedWatching

    def getPlayerData(self):
        return self.playerData

    def setPlayerData(self, newPlayerData):
        self.playerData = newPlayerData

    def getProgramId(self):
        return self.programId

    def setProgramId(self, newProgramId):
        self.programId = newProgramId

    def getIsReportingMode(self):
        return self.isReportingMode

    def setIsReportingMode(self, newIsReportingMode):
        self.isReportingMode = newIsReportingMode


# @package Kaltura
# @subpackage Client
class KalturaBookmarkListResponse(KalturaListResponse):
    """List of assets and their bookmarks"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaBookmark
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaBookmark'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBookmarkListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaBookmarkListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetCommentListResponse(KalturaListResponse):
    """Asset Comment Response"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaAssetComment
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetComment'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetCommentListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetCommentListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetStatisticsListResponse(KalturaListResponse):
    """List of assets statistics"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Assets
        # @var array of KalturaAssetStatistics
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetStatistics'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStatisticsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetStatisticsListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaMediaFileListResponse(KalturaListResponse):
    """Media-file list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of media-file types
        # @var array of KalturaMediaFile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaMediaFile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaMediaFileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetHistory(KalturaObjectBase):
    """Watch history asset info"""

    def __init__(self,
            assetId=NotImplemented,
            assetType=NotImplemented,
            position=NotImplemented,
            duration=NotImplemented,
            watchedDate=NotImplemented,
            finishedWatching=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Asset identifier
        # @var int
        # @readonly
        self.assetId = assetId

        # Asset identifier
        # @var KalturaAssetType
        # @readonly
        self.assetType = assetType

        # Position in seconds of the relevant asset
        # @var int
        # @readonly
        self.position = position

        # Duration in seconds of the relevant asset
        # @var int
        # @readonly
        self.duration = duration

        # The date when the media was last watched
        # @var int
        # @readonly
        self.watchedDate = watchedDate

        # Boolean which specifies whether the user finished watching the movie or not
        # @var bool
        # @readonly
        self.finishedWatching = finishedWatching


    PROPERTY_LOADERS = {
        'assetId': getXmlNodeInt, 
        'assetType': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
        'position': getXmlNodeInt, 
        'duration': getXmlNodeInt, 
        'watchedDate': getXmlNodeInt, 
        'finishedWatching': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetHistory.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetHistory")
        return kparams

    def getAssetId(self):
        return self.assetId

    def getAssetType(self):
        return self.assetType

    def getPosition(self):
        return self.position

    def getDuration(self):
        return self.duration

    def getWatchedDate(self):
        return self.watchedDate

    def getFinishedWatching(self):
        return self.finishedWatching


# @package Kaltura
# @subpackage Client
class KalturaAssetHistoryListResponse(KalturaListResponse):
    """Watch history asset wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # WatchHistoryAssets Models
        # @var array of KalturaAssetHistory
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetHistory'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetHistoryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetHistoryListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaBulk(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            status=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Bulk identifier
        # @var int
        # @readonly
        self.id = id

        # Status
        # @var KalturaBatchJobStatus
        # @readonly
        self.status = status

        # Specifies when was the bulk action created. Date and time represented as epoch
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the bulk action last updated. Date and time represented as epoch
        # @var int
        # @readonly
        self.updateDate = updateDate


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'status': (KalturaEnumsFactory.createString, "KalturaBatchJobStatus"), 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulk.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBulk")
        return kparams

    def getId(self):
        return self.id

    def getStatus(self):
        return self.status

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate


# @package Kaltura
# @subpackage Client
class KalturaBulkListResponse(KalturaListResponse):
    """Asset wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # bulk items
        # @var array of KalturaBulk
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaBulk'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaBulkListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaDrmProfile(KalturaObjectBase):
    """DRM Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            settings=NotImplemented,
            systemName=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaObjectBase.__init__(self)

        # DRM adapter identifier
        # @var int
        # @readonly
        self.id = id

        # DRM adapter name
        # @var string
        self.name = name

        # DRM adapter active status
        # @var bool
        self.isActive = isActive

        # DRM adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # DRM adapter settings
        # @var string
        self.settings = settings

        # DRM adapter alias
        # @var string
        self.systemName = systemName

        # DRM shared secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'settings': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDrmProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDrmProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addStringIfDefined("settings", self.settings)
        kparams.addStringIfDefined("systemName", self.systemName)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getSettings(self):
        return self.settings

    def setSettings(self, newSettings):
        self.settings = newSettings

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getSharedSecret(self):
        return self.sharedSecret


# @package Kaltura
# @subpackage Client
class KalturaDrmProfileListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Adapters
        # @var array of KalturaDrmProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaDrmProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDrmProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaDrmProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaMediaConcurrencyRule(KalturaObjectBase):
    """Media concurrency rule"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            concurrencyLimitationType=NotImplemented,
            limitation=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Media concurrency rule  identifier
        # @var string
        self.id = id

        # Media concurrency rule  name
        # @var string
        self.name = name

        # Concurrency limitation type
        # @var KalturaConcurrencyLimitationType
        self.concurrencyLimitationType = concurrencyLimitationType

        # Limitation
        # @var int
        self.limitation = limitation


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'concurrencyLimitationType': (KalturaEnumsFactory.createString, "KalturaConcurrencyLimitationType"), 
        'limitation': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaConcurrencyRule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMediaConcurrencyRule")
        kparams.addStringIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringEnumIfDefined("concurrencyLimitationType", self.concurrencyLimitationType)
        kparams.addIntIfDefined("limitation", self.limitation)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getConcurrencyLimitationType(self):
        return self.concurrencyLimitationType

    def setConcurrencyLimitationType(self, newConcurrencyLimitationType):
        self.concurrencyLimitationType = newConcurrencyLimitationType

    def getLimitation(self):
        return self.limitation

    def setLimitation(self, newLimitation):
        self.limitation = newLimitation


# @package Kaltura
# @subpackage Client
class KalturaMediaConcurrencyRuleListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Media CONCURRENCY RULES
        # @var array of KalturaMediaConcurrencyRule
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaMediaConcurrencyRule'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaConcurrencyRuleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaMediaConcurrencyRuleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetRuleBase(KalturaObjectBase):
    """Asset rule base"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # ID
        # @var int
        # @readonly
        self.id = id

        # Name
        # @var string
        self.name = name

        # Description
        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetRuleBase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaAssetRuleBase")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaCondition(KalturaObjectBase):
    """Condition"""

    def __init__(self,
            type=NotImplemented,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The type of the condition
        # @var KalturaRuleConditionType
        # @readonly
        self.type = type

        # Description
        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createString, "KalturaRuleConditionType"), 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCondition")
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getType(self):
        return self.type

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaAssetCondition(KalturaCondition):
    """Asset Condition"""

    def __init__(self,
            type=NotImplemented,
            description=NotImplemented,
            ksql=NotImplemented):
        KalturaCondition.__init__(self,
            type,
            description)

        # KSQL
        # @var string
        self.ksql = ksql


    PROPERTY_LOADERS = {
        'ksql': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaCondition.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCondition.toParams(self)
        kparams.put("objectType", "KalturaAssetCondition")
        kparams.addStringIfDefined("ksql", self.ksql)
        return kparams

    def getKsql(self):
        return self.ksql

    def setKsql(self, newKsql):
        self.ksql = newKsql


# @package Kaltura
# @subpackage Client
class KalturaRuleAction(KalturaObjectBase):
    def __init__(self,
            type=NotImplemented,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The type of the action
        # @var KalturaRuleActionType
        # @readonly
        self.type = type

        # Description
        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createString, "KalturaRuleActionType"), 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRuleAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRuleAction")
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getType(self):
        return self.type

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaAssetUserRuleAction(KalturaRuleAction):
    def __init__(self,
            type=NotImplemented,
            description=NotImplemented):
        KalturaRuleAction.__init__(self,
            type,
            description)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRuleAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetUserRuleAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRuleAction.toParams(self)
        kparams.put("objectType", "KalturaAssetUserRuleAction")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaAssetUserRule(KalturaAssetRuleBase):
    """Asset user rule"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            conditions=NotImplemented,
            actions=NotImplemented):
        KalturaAssetRuleBase.__init__(self,
            id,
            name,
            description)

        # List of Ksql conditions for the user rule
        # @var array of KalturaAssetCondition
        self.conditions = conditions

        # List of actions for the user rule
        # @var array of KalturaAssetUserRuleAction
        self.actions = actions


    PROPERTY_LOADERS = {
        'conditions': (KalturaObjectFactory.createArray, 'KalturaAssetCondition'), 
        'actions': (KalturaObjectFactory.createArray, 'KalturaAssetUserRuleAction'), 
    }

    def fromXml(self, node):
        KalturaAssetRuleBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetUserRule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetRuleBase.toParams(self)
        kparams.put("objectType", "KalturaAssetUserRule")
        kparams.addArrayIfDefined("conditions", self.conditions)
        kparams.addArrayIfDefined("actions", self.actions)
        return kparams

    def getConditions(self):
        return self.conditions

    def setConditions(self, newConditions):
        self.conditions = newConditions

    def getActions(self):
        return self.actions

    def setActions(self, newActions):
        self.actions = newActions


# @package Kaltura
# @subpackage Client
class KalturaAssetUserRuleListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Asset user rules
        # @var array of KalturaAssetUserRule
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetUserRule'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetUserRuleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetUserRuleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetRuleAction(KalturaRuleAction):
    def __init__(self,
            type=NotImplemented,
            description=NotImplemented):
        KalturaRuleAction.__init__(self,
            type,
            description)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRuleAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetRuleAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRuleAction.toParams(self)
        kparams.put("objectType", "KalturaAssetRuleAction")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaAssetRule(KalturaAssetRuleBase):
    """Asset rule"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            conditions=NotImplemented,
            actions=NotImplemented):
        KalturaAssetRuleBase.__init__(self,
            id,
            name,
            description)

        # List of conditions for the rule
        # @var array of KalturaCondition
        self.conditions = conditions

        # List of actions for the rule
        # @var array of KalturaAssetRuleAction
        self.actions = actions


    PROPERTY_LOADERS = {
        'conditions': (KalturaObjectFactory.createArray, 'KalturaCondition'), 
        'actions': (KalturaObjectFactory.createArray, 'KalturaAssetRuleAction'), 
    }

    def fromXml(self, node):
        KalturaAssetRuleBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetRule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetRuleBase.toParams(self)
        kparams.put("objectType", "KalturaAssetRule")
        kparams.addArrayIfDefined("conditions", self.conditions)
        kparams.addArrayIfDefined("actions", self.actions)
        return kparams

    def getConditions(self):
        return self.conditions

    def setConditions(self, newConditions):
        self.conditions = newConditions

    def getActions(self):
        return self.actions

    def setActions(self, newActions):
        self.actions = newActions


# @package Kaltura
# @subpackage Client
class KalturaCountryCondition(KalturaCondition):
    """Country condition"""

    def __init__(self,
            type=NotImplemented,
            description=NotImplemented,
            not_=NotImplemented,
            countries=NotImplemented):
        KalturaCondition.__init__(self,
            type,
            description)

        # Indicates whether to apply not on the other properties in the condition
        # @var bool
        self.not_ = not_

        # Comma separated countries IDs list
        # @var string
        self.countries = countries


    PROPERTY_LOADERS = {
        'not_': getXmlNodeBool, 
        'countries': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaCondition.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCountryCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaCondition.toParams(self)
        kparams.put("objectType", "KalturaCountryCondition")
        kparams.addBoolIfDefined("not", self.not_)
        kparams.addStringIfDefined("countries", self.countries)
        return kparams

    def getNot_(self):
        return self.not_

    def setNot_(self, newNot_):
        self.not_ = newNot_

    def getCountries(self):
        return self.countries

    def setCountries(self, newCountries):
        self.countries = newCountries


# @package Kaltura
# @subpackage Client
class KalturaConcurrencyCondition(KalturaAssetCondition):
    """Asset Condition"""

    def __init__(self,
            type=NotImplemented,
            description=NotImplemented,
            ksql=NotImplemented,
            limit=NotImplemented,
            concurrencyLimitationType=NotImplemented):
        KalturaAssetCondition.__init__(self,
            type,
            description,
            ksql)

        # Concurrency limitation
        # @var int
        self.limit = limit

        # Concurrency limitation type
        # @var KalturaConcurrencyLimitationType
        self.concurrencyLimitationType = concurrencyLimitationType


    PROPERTY_LOADERS = {
        'limit': getXmlNodeInt, 
        'concurrencyLimitationType': (KalturaEnumsFactory.createString, "KalturaConcurrencyLimitationType"), 
    }

    def fromXml(self, node):
        KalturaAssetCondition.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConcurrencyCondition.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetCondition.toParams(self)
        kparams.put("objectType", "KalturaConcurrencyCondition")
        kparams.addIntIfDefined("limit", self.limit)
        kparams.addStringEnumIfDefined("concurrencyLimitationType", self.concurrencyLimitationType)
        return kparams

    def getLimit(self):
        return self.limit

    def setLimit(self, newLimit):
        self.limit = newLimit

    def getConcurrencyLimitationType(self):
        return self.concurrencyLimitationType

    def setConcurrencyLimitationType(self, newConcurrencyLimitationType):
        self.concurrencyLimitationType = newConcurrencyLimitationType


# @package Kaltura
# @subpackage Client
class KalturaAssetUserRuleBlockAction(KalturaAssetUserRuleAction):
    def __init__(self,
            type=NotImplemented,
            description=NotImplemented):
        KalturaAssetUserRuleAction.__init__(self,
            type,
            description)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetUserRuleAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetUserRuleBlockAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetUserRuleAction.toParams(self)
        kparams.put("objectType", "KalturaAssetUserRuleBlockAction")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaAccessControlBlockAction(KalturaAssetRuleAction):
    def __init__(self,
            type=NotImplemented,
            description=NotImplemented):
        KalturaAssetRuleAction.__init__(self,
            type,
            description)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaAssetRuleAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAccessControlBlockAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetRuleAction.toParams(self)
        kparams.put("objectType", "KalturaAccessControlBlockAction")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaTimeOffsetRuleAction(KalturaAssetRuleAction):
    """Time offset action"""

    def __init__(self,
            type=NotImplemented,
            description=NotImplemented,
            offset=NotImplemented,
            timeZone=NotImplemented):
        KalturaAssetRuleAction.__init__(self,
            type,
            description)

        # Offset in seconds
        # @var int
        self.offset = offset

        # Indicates whether to add time zone offset to the time
        # @var bool
        self.timeZone = timeZone


    PROPERTY_LOADERS = {
        'offset': getXmlNodeInt, 
        'timeZone': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaAssetRuleAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTimeOffsetRuleAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetRuleAction.toParams(self)
        kparams.put("objectType", "KalturaTimeOffsetRuleAction")
        kparams.addIntIfDefined("offset", self.offset)
        kparams.addBoolIfDefined("timeZone", self.timeZone)
        return kparams

    def getOffset(self):
        return self.offset

    def setOffset(self, newOffset):
        self.offset = newOffset

    def getTimeZone(self):
        return self.timeZone

    def setTimeZone(self, newTimeZone):
        self.timeZone = newTimeZone


# @package Kaltura
# @subpackage Client
class KalturaEndDateOffsetRuleAction(KalturaTimeOffsetRuleAction):
    """End date offset action"""

    def __init__(self,
            type=NotImplemented,
            description=NotImplemented,
            offset=NotImplemented,
            timeZone=NotImplemented):
        KalturaTimeOffsetRuleAction.__init__(self,
            type,
            description,
            offset,
            timeZone)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaTimeOffsetRuleAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEndDateOffsetRuleAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaTimeOffsetRuleAction.toParams(self)
        kparams.put("objectType", "KalturaEndDateOffsetRuleAction")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaStartDateOffsetRuleAction(KalturaTimeOffsetRuleAction):
    """Start date offset action"""

    def __init__(self,
            type=NotImplemented,
            description=NotImplemented,
            offset=NotImplemented,
            timeZone=NotImplemented):
        KalturaTimeOffsetRuleAction.__init__(self,
            type,
            description,
            offset,
            timeZone)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaTimeOffsetRuleAction.fromXml(self, node)
        self.fromXmlImpl(node, KalturaStartDateOffsetRuleAction.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaTimeOffsetRuleAction.toParams(self)
        kparams.put("objectType", "KalturaStartDateOffsetRuleAction")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaCurrency(KalturaObjectBase):
    """Currency details"""

    def __init__(self,
            name=NotImplemented,
            code=NotImplemented,
            sign=NotImplemented,
            isDefault=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Currency name
        # @var string
        self.name = name

        # Currency code
        # @var string
        self.code = code

        # Currency Sign
        # @var string
        self.sign = sign

        # Is the default Currency of the account
        # @var bool
        self.isDefault = isDefault


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'code': getXmlNodeText, 
        'sign': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCurrency.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCurrency")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("code", self.code)
        kparams.addStringIfDefined("sign", self.sign)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getCode(self):
        return self.code

    def setCode(self, newCode):
        self.code = newCode

    def getSign(self):
        return self.sign

    def setSign(self, newSign):
        self.sign = newSign

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault


# @package Kaltura
# @subpackage Client
class KalturaCurrencyListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Currencies
        # @var array of KalturaCurrency
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaCurrency'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCurrencyListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCurrencyListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaAssetRuleListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Asset rules
        # @var array of KalturaAssetRule
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaAssetRule'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetRuleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaAssetRuleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaLanguage(KalturaObjectBase):
    """Language details"""

    def __init__(self,
            name=NotImplemented,
            systemName=NotImplemented,
            code=NotImplemented,
            direction=NotImplemented,
            isDefault=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Language name
        # @var string
        self.name = name

        # Language system name
        # @var string
        self.systemName = systemName

        # Language code
        # @var string
        self.code = code

        # Language direction (LTR/RTL)
        # @var string
        self.direction = direction

        # Is the default language of the account
        # @var bool
        self.isDefault = isDefault


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'systemName': getXmlNodeText, 
        'code': getXmlNodeText, 
        'direction': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLanguage.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaLanguage")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringIfDefined("code", self.code)
        kparams.addStringIfDefined("direction", self.direction)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getCode(self):
        return self.code

    def setCode(self, newCode):
        self.code = newCode

    def getDirection(self):
        return self.direction

    def setDirection(self, newDirection):
        self.direction = newDirection

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault


# @package Kaltura
# @subpackage Client
class KalturaLanguageListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Languages
        # @var array of KalturaLanguage
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaLanguage'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLanguageListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaLanguageListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaMeta(KalturaObjectBase):
    """Asset meta"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            multilingualName=NotImplemented,
            systemName=NotImplemented,
            dataType=NotImplemented,
            multipleValue=NotImplemented,
            isProtected=NotImplemented,
            helpText=NotImplemented,
            features=NotImplemented,
            parentId=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Meta id
        # @var string
        # @readonly
        self.id = id

        # Meta name for the partner
        # @var string
        # @readonly
        self.name = name

        # Meta name for the partner
        # @var array of KalturaTranslationToken
        self.multilingualName = multilingualName

        # Meta system name for the partner
        # @var string
        # @insertonly
        self.systemName = systemName

        # Meta data type
        # @var KalturaMetaDataType
        # @insertonly
        self.dataType = dataType

        # Does the meta contain multiple values
        # @var bool
        self.multipleValue = multipleValue

        # Is the meta protected by the system
        # @var bool
        # @insertonly
        self.isProtected = isProtected

        # The help text of the meta to be displayed on the UI.
        # @var string
        self.helpText = helpText

        # List of supported features
        # @var string
        self.features = features

        # Parent meta id
        # @var string
        self.parentId = parentId

        # Specifies when was the meta created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the meta last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'multilingualName': (KalturaObjectFactory.createArray, 'KalturaTranslationToken'), 
        'systemName': getXmlNodeText, 
        'dataType': (KalturaEnumsFactory.createString, "KalturaMetaDataType"), 
        'multipleValue': getXmlNodeBool, 
        'isProtected': getXmlNodeBool, 
        'helpText': getXmlNodeText, 
        'features': getXmlNodeText, 
        'parentId': getXmlNodeText, 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMeta.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaMeta")
        kparams.addArrayIfDefined("multilingualName", self.multilingualName)
        kparams.addStringIfDefined("systemName", self.systemName)
        kparams.addStringEnumIfDefined("dataType", self.dataType)
        kparams.addBoolIfDefined("multipleValue", self.multipleValue)
        kparams.addBoolIfDefined("isProtected", self.isProtected)
        kparams.addStringIfDefined("helpText", self.helpText)
        kparams.addStringIfDefined("features", self.features)
        kparams.addStringIfDefined("parentId", self.parentId)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getMultilingualName(self):
        return self.multilingualName

    def setMultilingualName(self, newMultilingualName):
        self.multilingualName = newMultilingualName

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getDataType(self):
        return self.dataType

    def setDataType(self, newDataType):
        self.dataType = newDataType

    def getMultipleValue(self):
        return self.multipleValue

    def setMultipleValue(self, newMultipleValue):
        self.multipleValue = newMultipleValue

    def getIsProtected(self):
        return self.isProtected

    def setIsProtected(self, newIsProtected):
        self.isProtected = newIsProtected

    def getHelpText(self):
        return self.helpText

    def setHelpText(self, newHelpText):
        self.helpText = newHelpText

    def getFeatures(self):
        return self.features

    def setFeatures(self, newFeatures):
        self.features = newFeatures

    def getParentId(self):
        return self.parentId

    def setParentId(self, newParentId):
        self.parentId = newParentId

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate


# @package Kaltura
# @subpackage Client
class KalturaMetaListResponse(KalturaListResponse):
    """Meta list response"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list asset meta
        # @var array of KalturaMeta
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaMeta'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetaListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaMetaListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaDeviceBrand(KalturaObjectBase):
    """Device brand details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            deviceFamilyid=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Device brand identifier
        # @var int
        # @readonly
        self.id = id

        # Device brand name
        # @var string
        self.name = name

        # Device family identifier
        # @var int
        # @readonly
        self.deviceFamilyid = deviceFamilyid


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'deviceFamilyid': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeviceBrand.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDeviceBrand")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDeviceFamilyid(self):
        return self.deviceFamilyid


# @package Kaltura
# @subpackage Client
class KalturaDeviceBrandListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Device brands
        # @var array of KalturaDeviceBrand
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaDeviceBrand'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeviceBrandListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaDeviceBrandListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaCountryListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Countries
        # @var array of KalturaCountry
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaCountry'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCountryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCountryListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaOSSAdapterBaseProfile(KalturaObjectBase):
    """OSS adapter basic"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # OSS adapter id
        # @var int
        # @readonly
        self.id = id

        # OSS adapter name
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOSSAdapterBaseProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaOSSAdapterBaseProfile")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaOSSAdapterProfile(KalturaOSSAdapterBaseProfile):
    """OSS Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            ossAdapterSettings=NotImplemented,
            externalIdentifier=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaOSSAdapterBaseProfile.__init__(self,
            id,
            name)

        # OSS adapter active status
        # @var bool
        self.isActive = isActive

        # OSS adapter adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # OSS adapter extra parameters
        # @var map
        self.ossAdapterSettings = ossAdapterSettings

        # OSS adapter external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Shared Secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'ossAdapterSettings': (KalturaObjectFactory.createMap, 'KalturaStringValue'), 
        'externalIdentifier': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaOSSAdapterBaseProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOSSAdapterProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaOSSAdapterBaseProfile.toParams(self)
        kparams.put("objectType", "KalturaOSSAdapterProfile")
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addMapIfDefined("ossAdapterSettings", self.ossAdapterSettings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        return kparams

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getOssAdapterSettings(self):
        return self.ossAdapterSettings

    def setOssAdapterSettings(self, newOssAdapterSettings):
        self.ossAdapterSettings = newOssAdapterSettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getSharedSecret(self):
        return self.sharedSecret


# @package Kaltura
# @subpackage Client
class KalturaOSSAdapterProfileListResponse(KalturaListResponse):
    """OSS adapter-profiles list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of OSS adapter-profiles
        # @var array of KalturaOSSAdapterProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaOSSAdapterProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOSSAdapterProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaOSSAdapterProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaSearchHistory(KalturaObjectBase):
    """Search history info"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            filter=NotImplemented,
            language=NotImplemented,
            createdAt=NotImplemented,
            service=NotImplemented,
            action=NotImplemented,
            deviceId=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Search ID
        # @var string
        # @readonly
        self.id = id

        # Search name
        # @var string
        # @readonly
        self.name = name

        # Filter
        # @var string
        # @readonly
        self.filter = filter

        # Search language
        # @var string
        # @readonly
        self.language = language

        # When search was performed
        # @var int
        # @readonly
        self.createdAt = createdAt

        # Kaltura OTT Service
        # @var string
        # @readonly
        self.service = service

        # Kaltura OTT Service Action
        # @var string
        # @readonly
        self.action = action

        # Unique Device ID
        # @var string
        # @readonly
        self.deviceId = deviceId


    PROPERTY_LOADERS = {
        'id': getXmlNodeText, 
        'name': getXmlNodeText, 
        'filter': getXmlNodeText, 
        'language': getXmlNodeText, 
        'createdAt': getXmlNodeInt, 
        'service': getXmlNodeText, 
        'action': getXmlNodeText, 
        'deviceId': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchHistory.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaSearchHistory")
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getFilter(self):
        return self.filter

    def getLanguage(self):
        return self.language

    def getCreatedAt(self):
        return self.createdAt

    def getService(self):
        return self.service

    def getAction(self):
        return self.action

    def getDeviceId(self):
        return self.deviceId


# @package Kaltura
# @subpackage Client
class KalturaSearchHistoryListResponse(KalturaListResponse):
    """Search history wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # KalturaSearchHistory Models
        # @var array of KalturaSearchHistory
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaSearchHistory'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchHistoryListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaSearchHistoryListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaDeviceFamilyBase(KalturaObjectBase):
    """Device family details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Device family identifier
        # @var int
        # @readonly
        self.id = id

        # Device family name
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeviceFamilyBase.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaDeviceFamilyBase")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaDeviceFamily(KalturaDeviceFamilyBase):
    """Device family details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented):
        KalturaDeviceFamilyBase.__init__(self,
            id,
            name)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaDeviceFamilyBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeviceFamily.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDeviceFamilyBase.toParams(self)
        kparams.put("objectType", "KalturaDeviceFamily")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaDeviceFamilyListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Device families
        # @var array of KalturaDeviceFamily
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaDeviceFamily'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeviceFamilyListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaDeviceFamilyListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaHouseholdDeviceFamilyLimitations(KalturaDeviceFamilyBase):
    """Device family limitations details"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            frequency=NotImplemented,
            deviceLimit=NotImplemented,
            concurrentLimit=NotImplemented):
        KalturaDeviceFamilyBase.__init__(self,
            id,
            name)

        # Allowed device change frequency code
        # @var int
        self.frequency = frequency

        # Max number of devices allowed for this family
        # @var int
        self.deviceLimit = deviceLimit

        # Max number of streams allowed for this family
        # @var int
        self.concurrentLimit = concurrentLimit


    PROPERTY_LOADERS = {
        'frequency': getXmlNodeInt, 
        'deviceLimit': getXmlNodeInt, 
        'concurrentLimit': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaDeviceFamilyBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdDeviceFamilyLimitations.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaDeviceFamilyBase.toParams(self)
        kparams.put("objectType", "KalturaHouseholdDeviceFamilyLimitations")
        kparams.addIntIfDefined("frequency", self.frequency)
        kparams.addIntIfDefined("deviceLimit", self.deviceLimit)
        kparams.addIntIfDefined("concurrentLimit", self.concurrentLimit)
        return kparams

    def getFrequency(self):
        return self.frequency

    def setFrequency(self, newFrequency):
        self.frequency = newFrequency

    def getDeviceLimit(self):
        return self.deviceLimit

    def setDeviceLimit(self, newDeviceLimit):
        self.deviceLimit = newDeviceLimit

    def getConcurrentLimit(self):
        return self.concurrentLimit

    def setConcurrentLimit(self, newConcurrentLimit):
        self.concurrentLimit = newConcurrentLimit


# @package Kaltura
# @subpackage Client
class KalturaRegionalChannel(KalturaObjectBase):
    def __init__(self,
            linearChannelId=NotImplemented,
            channelNumber=NotImplemented):
        KalturaObjectBase.__init__(self)

        # The identifier of the linear media representing the channel
        # @var int
        self.linearChannelId = linearChannelId

        # The number of the channel
        # @var int
        self.channelNumber = channelNumber


    PROPERTY_LOADERS = {
        'linearChannelId': getXmlNodeInt, 
        'channelNumber': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegionalChannel.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRegionalChannel")
        kparams.addIntIfDefined("linearChannelId", self.linearChannelId)
        kparams.addIntIfDefined("channelNumber", self.channelNumber)
        return kparams

    def getLinearChannelId(self):
        return self.linearChannelId

    def setLinearChannelId(self, newLinearChannelId):
        self.linearChannelId = newLinearChannelId

    def getChannelNumber(self):
        return self.channelNumber

    def setChannelNumber(self, newChannelNumber):
        self.channelNumber = newChannelNumber


# @package Kaltura
# @subpackage Client
class KalturaRegion(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            externalId=NotImplemented,
            isDefault=NotImplemented,
            linearChannels=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Region identifier
        # @var int
        self.id = id

        # Region name
        # @var string
        self.name = name

        # Region external identifier
        # @var string
        self.externalId = externalId

        # Indicates whether this is the default region for the partner
        # @var bool
        self.isDefault = isDefault

        # List of associated linear channels
        # @var array of KalturaRegionalChannel
        self.linearChannels = linearChannels


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'externalId': getXmlNodeText, 
        'isDefault': getXmlNodeBool, 
        'linearChannels': (KalturaObjectFactory.createArray, 'KalturaRegionalChannel'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegion.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRegion")
        kparams.addIntIfDefined("id", self.id)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("externalId", self.externalId)
        kparams.addBoolIfDefined("isDefault", self.isDefault)
        kparams.addArrayIfDefined("linearChannels", self.linearChannels)
        return kparams

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getExternalId(self):
        return self.externalId

    def setExternalId(self, newExternalId):
        self.externalId = newExternalId

    def getIsDefault(self):
        return self.isDefault

    def setIsDefault(self, newIsDefault):
        self.isDefault = newIsDefault

    def getLinearChannels(self):
        return self.linearChannels

    def setLinearChannels(self, newLinearChannels):
        self.linearChannels = newLinearChannels


# @package Kaltura
# @subpackage Client
class KalturaRegionListResponse(KalturaListResponse):
    """Regions list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of regions
        # @var array of KalturaRegion
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaRegion'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegionListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRegionListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaUserAssetRule(KalturaObjectBase):
    """User asset rule - representing different type of rules on an asset(Parental, Geo, User Type, Device)"""

    def __init__(self,
            id=NotImplemented,
            ruleType=NotImplemented,
            name=NotImplemented,
            description=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique rule identifier
        # @var int
        # @readonly
        self.id = id

        # Rule type - possible values: Rule type - Parental, Geo, UserType, Device
        # @var KalturaRuleType
        self.ruleType = ruleType

        # Rule display name
        # @var string
        self.name = name

        # Additional description for the specific rule
        # @var string
        self.description = description


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'ruleType': (KalturaEnumsFactory.createString, "KalturaRuleType"), 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserAssetRule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserAssetRule")
        kparams.addStringEnumIfDefined("ruleType", self.ruleType)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        return kparams

    def getId(self):
        return self.id

    def getRuleType(self):
        return self.ruleType

    def setRuleType(self, newRuleType):
        self.ruleType = newRuleType

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription


# @package Kaltura
# @subpackage Client
class KalturaUserAssetRuleListResponse(KalturaListResponse):
    """GenericRules list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of generic rules
        # @var array of KalturaUserAssetRule
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaUserAssetRule'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserAssetRuleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaUserAssetRuleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaCDNAdapterProfile(KalturaObjectBase):
    """CDN Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            baseUrl=NotImplemented,
            settings=NotImplemented,
            systemName=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaObjectBase.__init__(self)

        # CDN adapter identifier
        # @var int
        # @readonly
        self.id = id

        # CDNR adapter name
        # @var string
        self.name = name

        # CDN adapter active status
        # @var bool
        self.isActive = isActive

        # CDN adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # CDN adapter base URL
        # @var string
        self.baseUrl = baseUrl

        # CDN adapter settings
        # @var map
        self.settings = settings

        # CDN adapter alias
        # @var string
        self.systemName = systemName

        # CDN shared secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'baseUrl': getXmlNodeText, 
        'settings': (KalturaObjectFactory.createMap, 'KalturaStringValue'), 
        'systemName': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDNAdapterProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaCDNAdapterProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addStringIfDefined("baseUrl", self.baseUrl)
        kparams.addMapIfDefined("settings", self.settings)
        kparams.addStringIfDefined("systemName", self.systemName)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getBaseUrl(self):
        return self.baseUrl

    def setBaseUrl(self, newBaseUrl):
        self.baseUrl = newBaseUrl

    def getSettings(self):
        return self.settings

    def setSettings(self, newSettings):
        self.settings = newSettings

    def getSystemName(self):
        return self.systemName

    def setSystemName(self, newSystemName):
        self.systemName = newSystemName

    def getSharedSecret(self):
        return self.sharedSecret


# @package Kaltura
# @subpackage Client
class KalturaCDNAdapterProfileListResponse(KalturaListResponse):
    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Adapters
        # @var array of KalturaCDNAdapterProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaCDNAdapterProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCDNAdapterProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaCDNAdapterProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaExportTask(KalturaObjectBase):
    """Bulk export task"""

    def __init__(self,
            id=NotImplemented,
            alias=NotImplemented,
            name=NotImplemented,
            dataType=NotImplemented,
            filter=NotImplemented,
            exportType=NotImplemented,
            frequency=NotImplemented,
            notificationUrl=NotImplemented,
            vodTypes=NotImplemented,
            isActive=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Task identifier
        # @var int
        # @readonly
        self.id = id

        # Alias for the task used to solicit an export using API
        # @var string
        self.alias = alias

        # Task display name
        # @var string
        self.name = name

        # The data type exported in this task
        # @var KalturaExportDataType
        self.dataType = dataType

        # Filter to apply on the export, utilize KSQL.
        #             Note: KSQL currently applies to media assets only. It cannot be used for USERS filtering
        # @var string
        self.filter = filter

        # Type of export batch - full or incremental
        # @var KalturaExportType
        self.exportType = exportType

        # How often the export should occur, reasonable minimum threshold should apply, configurable in minutes
        # @var int
        self.frequency = frequency

        # The URL for sending a notification when the task&#39;s export process is done
        # @var string
        self.notificationUrl = notificationUrl

        # List of media type identifiers (as configured in TVM) to export. used only in case data_type = vod
        # @var array of KalturaIntegerValue
        self.vodTypes = vodTypes

        # Indicates if the task is active or not
        # @var bool
        self.isActive = isActive


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'alias': getXmlNodeText, 
        'name': getXmlNodeText, 
        'dataType': (KalturaEnumsFactory.createString, "KalturaExportDataType"), 
        'filter': getXmlNodeText, 
        'exportType': (KalturaEnumsFactory.createString, "KalturaExportType"), 
        'frequency': getXmlNodeInt, 
        'notificationUrl': getXmlNodeText, 
        'vodTypes': (KalturaObjectFactory.createArray, 'KalturaIntegerValue'), 
        'isActive': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExportTask.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaExportTask")
        kparams.addStringIfDefined("alias", self.alias)
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringEnumIfDefined("dataType", self.dataType)
        kparams.addStringIfDefined("filter", self.filter)
        kparams.addStringEnumIfDefined("exportType", self.exportType)
        kparams.addIntIfDefined("frequency", self.frequency)
        kparams.addStringIfDefined("notificationUrl", self.notificationUrl)
        kparams.addArrayIfDefined("vodTypes", self.vodTypes)
        kparams.addBoolIfDefined("isActive", self.isActive)
        return kparams

    def getId(self):
        return self.id

    def getAlias(self):
        return self.alias

    def setAlias(self, newAlias):
        self.alias = newAlias

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDataType(self):
        return self.dataType

    def setDataType(self, newDataType):
        self.dataType = newDataType

    def getFilter(self):
        return self.filter

    def setFilter(self, newFilter):
        self.filter = newFilter

    def getExportType(self):
        return self.exportType

    def setExportType(self, newExportType):
        self.exportType = newExportType

    def getFrequency(self):
        return self.frequency

    def setFrequency(self, newFrequency):
        self.frequency = newFrequency

    def getNotificationUrl(self):
        return self.notificationUrl

    def setNotificationUrl(self, newNotificationUrl):
        self.notificationUrl = newNotificationUrl

    def getVodTypes(self):
        return self.vodTypes

    def setVodTypes(self, newVodTypes):
        self.vodTypes = newVodTypes

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive


# @package Kaltura
# @subpackage Client
class KalturaExportTaskListResponse(KalturaListResponse):
    """Export task list wrapper"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Export task items
        # @var array of KalturaExportTask
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaExportTask'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExportTaskListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaExportTaskListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaChannelEnrichmentHolder(KalturaObjectBase):
    """Holder object for channel enrichment enum"""

    def __init__(self,
            type=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Enrichment type
        # @var KalturaChannelEnrichment
        self.type = type


    PROPERTY_LOADERS = {
        'type': (KalturaEnumsFactory.createString, "KalturaChannelEnrichment"), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelEnrichmentHolder.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaChannelEnrichmentHolder")
        kparams.addStringEnumIfDefined("type", self.type)
        return kparams

    def getType(self):
        return self.type

    def setType(self, newType):
        self.type = newType


# @package Kaltura
# @subpackage Client
class KalturaExternalChannelProfile(KalturaObjectBase):
    """OSS Adapter"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            externalIdentifier=NotImplemented,
            filterExpression=NotImplemented,
            recommendationEngineId=NotImplemented,
            enrichments=NotImplemented):
        KalturaObjectBase.__init__(self)

        # External channel id
        # @var int
        # @readonly
        self.id = id

        # External channel name
        # @var string
        self.name = name

        # External channel active status
        # @var bool
        self.isActive = isActive

        # External channel external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Filter expression
        # @var string
        self.filterExpression = filterExpression

        # Recommendation engine id
        # @var int
        self.recommendationEngineId = recommendationEngineId

        # Enrichments
        # @var array of KalturaChannelEnrichmentHolder
        self.enrichments = enrichments


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'externalIdentifier': getXmlNodeText, 
        'filterExpression': getXmlNodeText, 
        'recommendationEngineId': getXmlNodeInt, 
        'enrichments': (KalturaObjectFactory.createArray, 'KalturaChannelEnrichmentHolder'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExternalChannelProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaExternalChannelProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        kparams.addStringIfDefined("filterExpression", self.filterExpression)
        kparams.addIntIfDefined("recommendationEngineId", self.recommendationEngineId)
        kparams.addArrayIfDefined("enrichments", self.enrichments)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getFilterExpression(self):
        return self.filterExpression

    def setFilterExpression(self, newFilterExpression):
        self.filterExpression = newFilterExpression

    def getRecommendationEngineId(self):
        return self.recommendationEngineId

    def setRecommendationEngineId(self, newRecommendationEngineId):
        self.recommendationEngineId = newRecommendationEngineId

    def getEnrichments(self):
        return self.enrichments

    def setEnrichments(self, newEnrichments):
        self.enrichments = newEnrichments


# @package Kaltura
# @subpackage Client
class KalturaExternalChannelProfileListResponse(KalturaListResponse):
    """External channel profiles"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # External channel profiles
        # @var array of KalturaExternalChannelProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaExternalChannelProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExternalChannelProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaExternalChannelProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaRecommendationProfile(KalturaObjectBase):
    """PaymentGW"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            isActive=NotImplemented,
            adapterUrl=NotImplemented,
            recommendationEngineSettings=NotImplemented,
            externalIdentifier=NotImplemented,
            sharedSecret=NotImplemented):
        KalturaObjectBase.__init__(self)

        # recommendation engine id
        # @var int
        # @readonly
        self.id = id

        # recommendation engine name
        # @var string
        self.name = name

        # recommendation engine is active status
        # @var bool
        self.isActive = isActive

        # recommendation engine adapter URL
        # @var string
        self.adapterUrl = adapterUrl

        # recommendation engine extra parameters
        # @var map
        self.recommendationEngineSettings = recommendationEngineSettings

        # recommendation engine external identifier
        # @var string
        self.externalIdentifier = externalIdentifier

        # Shared Secret
        # @var string
        # @readonly
        self.sharedSecret = sharedSecret


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'isActive': getXmlNodeBool, 
        'adapterUrl': getXmlNodeText, 
        'recommendationEngineSettings': (KalturaObjectFactory.createMap, 'KalturaStringValue'), 
        'externalIdentifier': getXmlNodeText, 
        'sharedSecret': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecommendationProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRecommendationProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addBoolIfDefined("isActive", self.isActive)
        kparams.addStringIfDefined("adapterUrl", self.adapterUrl)
        kparams.addMapIfDefined("recommendationEngineSettings", self.recommendationEngineSettings)
        kparams.addStringIfDefined("externalIdentifier", self.externalIdentifier)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getAdapterUrl(self):
        return self.adapterUrl

    def setAdapterUrl(self, newAdapterUrl):
        self.adapterUrl = newAdapterUrl

    def getRecommendationEngineSettings(self):
        return self.recommendationEngineSettings

    def setRecommendationEngineSettings(self, newRecommendationEngineSettings):
        self.recommendationEngineSettings = newRecommendationEngineSettings

    def getExternalIdentifier(self):
        return self.externalIdentifier

    def setExternalIdentifier(self, newExternalIdentifier):
        self.externalIdentifier = newExternalIdentifier

    def getSharedSecret(self):
        return self.sharedSecret


# @package Kaltura
# @subpackage Client
class KalturaRecommendationProfileListResponse(KalturaListResponse):
    """List of recommendation profiles."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Recommendation profiles list
        # @var array of KalturaRecommendationProfile
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaRecommendationProfile'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecommendationProfileListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRecommendationProfileListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaRegistrySettings(KalturaObjectBase):
    def __init__(self,
            key=NotImplemented,
            value=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Permission item identifier
        # @var string
        self.key = key

        # Permission item name
        # @var string
        self.value = value


    PROPERTY_LOADERS = {
        'key': getXmlNodeText, 
        'value': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegistrySettings.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRegistrySettings")
        kparams.addStringIfDefined("key", self.key)
        kparams.addStringIfDefined("value", self.value)
        return kparams

    def getKey(self):
        return self.key

    def setKey(self, newKey):
        self.key = newKey

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue


# @package Kaltura
# @subpackage Client
class KalturaRegistrySettingsListResponse(KalturaListResponse):
    """List of registry settings."""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # Registry settings list
        # @var array of KalturaRegistrySettings
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaRegistrySettings'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegistrySettingsListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaRegistrySettingsListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaParentalRule(KalturaObjectBase):
    """Parental rule"""

    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            description=NotImplemented,
            order=NotImplemented,
            mediaTag=NotImplemented,
            epgTag=NotImplemented,
            blockAnonymousAccess=NotImplemented,
            ruleType=NotImplemented,
            mediaTagValues=NotImplemented,
            epgTagValues=NotImplemented,
            isDefault=NotImplemented,
            origin=NotImplemented,
            isActive=NotImplemented,
            createDate=NotImplemented,
            updateDate=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Unique parental rule identifier
        # @var int
        # @readonly
        self.id = id

        # Rule display name
        # @var string
        self.name = name

        # Explanatory description
        # @var string
        self.description = description

        # Rule order within the full list of rules
        # @var int
        self.order = order

        # Media asset tag ID to in which to look for corresponding trigger values
        # @var int
        self.mediaTag = mediaTag

        # EPG asset tag ID to in which to look for corresponding trigger values
        # @var int
        self.epgTag = epgTag

        # Content that correspond to this rule is not available for guests
        # @var bool
        self.blockAnonymousAccess = blockAnonymousAccess

        # Rule type - Movies, TV series or both
        # @var KalturaParentalRuleType
        self.ruleType = ruleType

        # Media tag values that trigger rule
        # @var array of KalturaStringValue
        self.mediaTagValues = mediaTagValues

        # EPG tag values that trigger rule
        # @var array of KalturaStringValue
        self.epgTagValues = epgTagValues

        # Is the rule the default rule of the account
        # @var bool
        # @readonly
        self.isDefault = isDefault

        # Where was this rule defined account, household or user
        # @var KalturaRuleLevel
        # @readonly
        self.origin = origin

        # active status
        # @var bool
        self.isActive = isActive

        # Specifies when was the parental rule created. Date and time represented as epoch.
        # @var int
        # @readonly
        self.createDate = createDate

        # Specifies when was the parental rule last updated. Date and time represented as epoch.
        # @var int
        # @readonly
        self.updateDate = updateDate


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'description': getXmlNodeText, 
        'order': getXmlNodeInt, 
        'mediaTag': getXmlNodeInt, 
        'epgTag': getXmlNodeInt, 
        'blockAnonymousAccess': getXmlNodeBool, 
        'ruleType': (KalturaEnumsFactory.createString, "KalturaParentalRuleType"), 
        'mediaTagValues': (KalturaObjectFactory.createArray, 'KalturaStringValue'), 
        'epgTagValues': (KalturaObjectFactory.createArray, 'KalturaStringValue'), 
        'isDefault': getXmlNodeBool, 
        'origin': (KalturaEnumsFactory.createString, "KalturaRuleLevel"), 
        'isActive': getXmlNodeBool, 
        'createDate': getXmlNodeInt, 
        'updateDate': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaParentalRule.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaParentalRule")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("description", self.description)
        kparams.addIntIfDefined("order", self.order)
        kparams.addIntIfDefined("mediaTag", self.mediaTag)
        kparams.addIntIfDefined("epgTag", self.epgTag)
        kparams.addBoolIfDefined("blockAnonymousAccess", self.blockAnonymousAccess)
        kparams.addStringEnumIfDefined("ruleType", self.ruleType)
        kparams.addArrayIfDefined("mediaTagValues", self.mediaTagValues)
        kparams.addArrayIfDefined("epgTagValues", self.epgTagValues)
        kparams.addBoolIfDefined("isActive", self.isActive)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescription(self):
        return self.description

    def setDescription(self, newDescription):
        self.description = newDescription

    def getOrder(self):
        return self.order

    def setOrder(self, newOrder):
        self.order = newOrder

    def getMediaTag(self):
        return self.mediaTag

    def setMediaTag(self, newMediaTag):
        self.mediaTag = newMediaTag

    def getEpgTag(self):
        return self.epgTag

    def setEpgTag(self, newEpgTag):
        self.epgTag = newEpgTag

    def getBlockAnonymousAccess(self):
        return self.blockAnonymousAccess

    def setBlockAnonymousAccess(self, newBlockAnonymousAccess):
        self.blockAnonymousAccess = newBlockAnonymousAccess

    def getRuleType(self):
        return self.ruleType

    def setRuleType(self, newRuleType):
        self.ruleType = newRuleType

    def getMediaTagValues(self):
        return self.mediaTagValues

    def setMediaTagValues(self, newMediaTagValues):
        self.mediaTagValues = newMediaTagValues

    def getEpgTagValues(self):
        return self.epgTagValues

    def setEpgTagValues(self, newEpgTagValues):
        self.epgTagValues = newEpgTagValues

    def getIsDefault(self):
        return self.isDefault

    def getOrigin(self):
        return self.origin

    def getIsActive(self):
        return self.isActive

    def setIsActive(self, newIsActive):
        self.isActive = newIsActive

    def getCreateDate(self):
        return self.createDate

    def getUpdateDate(self):
        return self.updateDate


# @package Kaltura
# @subpackage Client
class KalturaParentalRuleListResponse(KalturaListResponse):
    """ParentalRules list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of parental rules
        # @var array of KalturaParentalRule
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaParentalRule'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaParentalRuleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaParentalRuleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaUserRole(KalturaObjectBase):
    def __init__(self,
            id=NotImplemented,
            name=NotImplemented,
            permissionNames=NotImplemented,
            excludedPermissionNames=NotImplemented):
        KalturaObjectBase.__init__(self)

        # User role identifier
        # @var int
        # @readonly
        self.id = id

        # User role name
        # @var string
        self.name = name

        # permissions associated with the user role
        # @var string
        self.permissionNames = permissionNames

        # permissions associated with the user role in is_exclueded = true
        # @var string
        self.excludedPermissionNames = excludedPermissionNames


    PROPERTY_LOADERS = {
        'id': getXmlNodeInt, 
        'name': getXmlNodeText, 
        'permissionNames': getXmlNodeText, 
        'excludedPermissionNames': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRole.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaUserRole")
        kparams.addStringIfDefined("name", self.name)
        kparams.addStringIfDefined("permissionNames", self.permissionNames)
        kparams.addStringIfDefined("excludedPermissionNames", self.excludedPermissionNames)
        return kparams

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getPermissionNames(self):
        return self.permissionNames

    def setPermissionNames(self, newPermissionNames):
        self.permissionNames = newPermissionNames

    def getExcludedPermissionNames(self):
        return self.excludedPermissionNames

    def setExcludedPermissionNames(self, newExcludedPermissionNames):
        self.excludedPermissionNames = newExcludedPermissionNames


# @package Kaltura
# @subpackage Client
class KalturaUserRoleListResponse(KalturaListResponse):
    """User-roles list"""

    def __init__(self,
            totalCount=NotImplemented,
            objects=NotImplemented):
        KalturaListResponse.__init__(self,
            totalCount)

        # A list of generic rules
        # @var array of KalturaUserRole
        self.objects = objects


    PROPERTY_LOADERS = {
        'objects': (KalturaObjectFactory.createArray, 'KalturaUserRole'), 
    }

    def fromXml(self, node):
        KalturaListResponse.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleListResponse.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaListResponse.toParams(self)
        kparams.put("objectType", "KalturaUserRoleListResponse")
        kparams.addArrayIfDefined("objects", self.objects)
        return kparams

    def getObjects(self):
        return self.objects

    def setObjects(self, newObjects):
        self.objects = newObjects


# @package Kaltura
# @subpackage Client
class KalturaClientConfiguration(KalturaObjectBase):
    """Define client optional configurations"""

    def __init__(self,
            clientTag=NotImplemented,
            apiVersion=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Client Tag
        # @var string
        self.clientTag = clientTag

        # API client version
        # @var string
        self.apiVersion = apiVersion


    PROPERTY_LOADERS = {
        'clientTag': getXmlNodeText, 
        'apiVersion': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaClientConfiguration.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaClientConfiguration")
        kparams.addStringIfDefined("clientTag", self.clientTag)
        kparams.addStringIfDefined("apiVersion", self.apiVersion)
        return kparams

    def getClientTag(self):
        return self.clientTag

    def setClientTag(self, newClientTag):
        self.clientTag = newClientTag

    def getApiVersion(self):
        return self.apiVersion

    def setApiVersion(self, newApiVersion):
        self.apiVersion = newApiVersion


# @package Kaltura
# @subpackage Client
class KalturaBaseResponseProfile(KalturaObjectBase):
    """Define base profile response -  optional configurations"""

    def __init__(self):
        KalturaObjectBase.__init__(self)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseResponseProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaBaseResponseProfile")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaRequestConfiguration(KalturaObjectBase):
    """Define client request optional configurations"""

    def __init__(self,
            partnerId=NotImplemented,
            userId=NotImplemented,
            language=NotImplemented,
            currency=NotImplemented,
            ks=NotImplemented,
            responseProfile=NotImplemented):
        KalturaObjectBase.__init__(self)

        # Impersonated partner id
        # @var int
        self.partnerId = partnerId

        # Impersonated user id
        # @var int
        self.userId = userId

        # Content language
        # @var string
        self.language = language

        # Currency to be used
        # @var string
        self.currency = currency

        # Kaltura API session
        # @var string
        self.ks = ks

        # Kaltura response profile object
        # @var KalturaBaseResponseProfile
        self.responseProfile = responseProfile


    PROPERTY_LOADERS = {
        'partnerId': getXmlNodeInt, 
        'userId': getXmlNodeInt, 
        'language': getXmlNodeText, 
        'currency': getXmlNodeText, 
        'ks': getXmlNodeText, 
        'responseProfile': (KalturaObjectFactory.create, 'KalturaBaseResponseProfile'), 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRequestConfiguration.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaRequestConfiguration")
        kparams.addIntIfDefined("partnerId", self.partnerId)
        kparams.addIntIfDefined("userId", self.userId)
        kparams.addStringIfDefined("language", self.language)
        kparams.addStringIfDefined("currency", self.currency)
        kparams.addStringIfDefined("ks", self.ks)
        kparams.addObjectIfDefined("responseProfile", self.responseProfile)
        return kparams

    def getPartnerId(self):
        return self.partnerId

    def setPartnerId(self, newPartnerId):
        self.partnerId = newPartnerId

    def getUserId(self):
        return self.userId

    def setUserId(self, newUserId):
        self.userId = newUserId

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getCurrency(self):
        return self.currency

    def setCurrency(self, newCurrency):
        self.currency = newCurrency

    def getKs(self):
        return self.ks

    def setKs(self, newKs):
        self.ks = newKs

    def getResponseProfile(self):
        return self.responseProfile

    def setResponseProfile(self, newResponseProfile):
        self.responseProfile = newResponseProfile


# @package Kaltura
# @subpackage Client
class KalturaFilter(KalturaObjectBase):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaObjectBase.__init__(self)

        # order by
        # @var string
        self.orderBy = orderBy


    PROPERTY_LOADERS = {
        'orderBy': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaObjectBase.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaObjectBase.toParams(self)
        kparams.put("objectType", "KalturaFilter")
        kparams.addStringIfDefined("orderBy", self.orderBy)
        return kparams

    def getOrderBy(self):
        return self.orderBy

    def setOrderBy(self, newOrderBy):
        self.orderBy = newOrderBy


# @package Kaltura
# @subpackage Client
class KalturaDetachedResponseProfile(KalturaBaseResponseProfile):
    """Define specific base profile response"""

    def __init__(self,
            name=NotImplemented,
            filter=NotImplemented,
            relatedProfiles=NotImplemented):
        KalturaBaseResponseProfile.__init__(self)

        # name
        # @var string
        self.name = name

        # filter
        # @var KalturaRelatedObjectFilter
        self.filter = filter

        # relatedProfiles
        # @var array of KalturaDetachedResponseProfile
        self.relatedProfiles = relatedProfiles


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
        'filter': (KalturaObjectFactory.create, 'KalturaRelatedObjectFilter'), 
        'relatedProfiles': (KalturaObjectFactory.createArray, 'KalturaObjectBase'), 
    }

    def fromXml(self, node):
        KalturaBaseResponseProfile.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDetachedResponseProfile.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseResponseProfile.toParams(self)
        kparams.put("objectType", "KalturaDetachedResponseProfile")
        kparams.addStringIfDefined("name", self.name)
        kparams.addObjectIfDefined("filter", self.filter)
        kparams.addArrayIfDefined("relatedProfiles", self.relatedProfiles)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getFilter(self):
        return self.filter

    def setFilter(self, newFilter):
        self.filter = newFilter

    def getRelatedProfiles(self):
        return self.relatedProfiles

    def setRelatedProfiles(self, newRelatedProfiles):
        self.relatedProfiles = newRelatedProfiles


# @package Kaltura
# @subpackage Client
class KalturaRelatedObjectFilter(KalturaFilter):
    """Define KalturaRelatedObjectFilter"""

    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRelatedObjectFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaRelatedObjectFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaSocialCommentFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            assetIdEqual=NotImplemented,
            assetTypeEqual=NotImplemented,
            socialPlatformEqual=NotImplemented,
            createDateGreaterThan=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Asset ID to filter by
        # @var int
        self.assetIdEqual = assetIdEqual

        # Asset type to filter by, currently only VOD (media)
        # @var KalturaAssetType
        self.assetTypeEqual = assetTypeEqual

        # Comma separated list of social actions to filter by
        # @var KalturaSocialPlatform
        self.socialPlatformEqual = socialPlatformEqual

        # The create date from which to get the comments
        # @var int
        self.createDateGreaterThan = createDateGreaterThan


    PROPERTY_LOADERS = {
        'assetIdEqual': getXmlNodeInt, 
        'assetTypeEqual': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
        'socialPlatformEqual': (KalturaEnumsFactory.createString, "KalturaSocialPlatform"), 
        'createDateGreaterThan': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialCommentFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSocialCommentFilter")
        kparams.addIntIfDefined("assetIdEqual", self.assetIdEqual)
        kparams.addStringEnumIfDefined("assetTypeEqual", self.assetTypeEqual)
        kparams.addStringEnumIfDefined("socialPlatformEqual", self.socialPlatformEqual)
        kparams.addIntIfDefined("createDateGreaterThan", self.createDateGreaterThan)
        return kparams

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual

    def getSocialPlatformEqual(self):
        return self.socialPlatformEqual

    def setSocialPlatformEqual(self, newSocialPlatformEqual):
        self.socialPlatformEqual = newSocialPlatformEqual

    def getCreateDateGreaterThan(self):
        return self.createDateGreaterThan

    def setCreateDateGreaterThan(self, newCreateDateGreaterThan):
        self.createDateGreaterThan = newCreateDateGreaterThan


# @package Kaltura
# @subpackage Client
class KalturaSocialFriendActivityFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            assetIdEqual=NotImplemented,
            assetTypeEqual=NotImplemented,
            actionTypeIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Asset ID to filter by
        # @var int
        self.assetIdEqual = assetIdEqual

        # Asset type to filter by, currently only VOD (media)
        # @var KalturaAssetType
        self.assetTypeEqual = assetTypeEqual

        # Comma separated list of social actions to filter by
        # @var string
        self.actionTypeIn = actionTypeIn


    PROPERTY_LOADERS = {
        'assetIdEqual': getXmlNodeInt, 
        'assetTypeEqual': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
        'actionTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialFriendActivityFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSocialFriendActivityFilter")
        kparams.addIntIfDefined("assetIdEqual", self.assetIdEqual)
        kparams.addStringEnumIfDefined("assetTypeEqual", self.assetTypeEqual)
        kparams.addStringIfDefined("actionTypeIn", self.actionTypeIn)
        return kparams

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual

    def getActionTypeIn(self):
        return self.actionTypeIn

    def setActionTypeIn(self, newActionTypeIn):
        self.actionTypeIn = newActionTypeIn


# @package Kaltura
# @subpackage Client
class KalturaSocialActionFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            assetIdIn=NotImplemented,
            assetTypeEqual=NotImplemented,
            actionTypeIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated list of asset identifiers.
        # @var string
        self.assetIdIn = assetIdIn

        # Asset Type
        # @var KalturaAssetType
        self.assetTypeEqual = assetTypeEqual

        # Comma separated list of social actions to filter by
        # @var string
        self.actionTypeIn = actionTypeIn


    PROPERTY_LOADERS = {
        'assetIdIn': getXmlNodeText, 
        'assetTypeEqual': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
        'actionTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSocialActionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSocialActionFilter")
        kparams.addStringIfDefined("assetIdIn", self.assetIdIn)
        kparams.addStringEnumIfDefined("assetTypeEqual", self.assetTypeEqual)
        kparams.addStringIfDefined("actionTypeIn", self.actionTypeIn)
        return kparams

    def getAssetIdIn(self):
        return self.assetIdIn

    def setAssetIdIn(self, newAssetIdIn):
        self.assetIdIn = newAssetIdIn

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual

    def getActionTypeIn(self):
        return self.actionTypeIn

    def setActionTypeIn(self, newActionTypeIn):
        self.actionTypeIn = newActionTypeIn


# @package Kaltura
# @subpackage Client
class KalturaPaymentMethodProfileFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            paymentGatewayIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Payment gateway identifier to list the payment methods for
        # @var int
        self.paymentGatewayIdEqual = paymentGatewayIdEqual


    PROPERTY_LOADERS = {
        'paymentGatewayIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPaymentMethodProfileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPaymentMethodProfileFilter")
        kparams.addIntIfDefined("paymentGatewayIdEqual", self.paymentGatewayIdEqual)
        return kparams

    def getPaymentGatewayIdEqual(self):
        return self.paymentGatewayIdEqual

    def setPaymentGatewayIdEqual(self, newPaymentGatewayIdEqual):
        self.paymentGatewayIdEqual = newPaymentGatewayIdEqual


# @package Kaltura
# @subpackage Client
class KalturaHouseholdDeviceFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            householdIdEqual=NotImplemented,
            deviceFamilyIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # The identifier of the household
        # @var int
        self.householdIdEqual = householdIdEqual

        # Device family Ids
        # @var string
        self.deviceFamilyIdIn = deviceFamilyIdIn


    PROPERTY_LOADERS = {
        'householdIdEqual': getXmlNodeInt, 
        'deviceFamilyIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdDeviceFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaHouseholdDeviceFilter")
        kparams.addIntIfDefined("householdIdEqual", self.householdIdEqual)
        kparams.addStringIfDefined("deviceFamilyIdIn", self.deviceFamilyIdIn)
        return kparams

    def getHouseholdIdEqual(self):
        return self.householdIdEqual

    def setHouseholdIdEqual(self, newHouseholdIdEqual):
        self.householdIdEqual = newHouseholdIdEqual

    def getDeviceFamilyIdIn(self):
        return self.deviceFamilyIdIn

    def setDeviceFamilyIdIn(self, newDeviceFamilyIdIn):
        self.deviceFamilyIdIn = newDeviceFamilyIdIn


# @package Kaltura
# @subpackage Client
class KalturaHouseholdUserFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            householdIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # The identifier of the household
        # @var int
        self.householdIdEqual = householdIdEqual


    PROPERTY_LOADERS = {
        'householdIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaHouseholdUserFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaHouseholdUserFilter")
        kparams.addIntIfDefined("householdIdEqual", self.householdIdEqual)
        return kparams

    def getHouseholdIdEqual(self):
        return self.householdIdEqual

    def setHouseholdIdEqual(self, newHouseholdIdEqual):
        self.householdIdEqual = newHouseholdIdEqual


# @package Kaltura
# @subpackage Client
class KalturaConfigurationsFilter(KalturaFilter):
    """Configuration filter"""

    def __init__(self,
            orderBy=NotImplemented,
            configurationGroupIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # the ID of the configuration group for which to return related configurations
        # @var string
        self.configurationGroupIdEqual = configurationGroupIdEqual


    PROPERTY_LOADERS = {
        'configurationGroupIdEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaConfigurationsFilter")
        kparams.addStringIfDefined("configurationGroupIdEqual", self.configurationGroupIdEqual)
        return kparams

    def getConfigurationGroupIdEqual(self):
        return self.configurationGroupIdEqual

    def setConfigurationGroupIdEqual(self, newConfigurationGroupIdEqual):
        self.configurationGroupIdEqual = newConfigurationGroupIdEqual


# @package Kaltura
# @subpackage Client
class KalturaReportFilter(KalturaFilter):
    """Report filter"""

    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReportFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaReportFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaDeviceReportFilter(KalturaReportFilter):
    """Report filter"""

    def __init__(self,
            orderBy=NotImplemented,
            lastAccessDateGreaterThanOrEqual=NotImplemented):
        KalturaReportFilter.__init__(self,
            orderBy)

        # Filter device configuration later than specific date
        # @var int
        self.lastAccessDateGreaterThanOrEqual = lastAccessDateGreaterThanOrEqual


    PROPERTY_LOADERS = {
        'lastAccessDateGreaterThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaReportFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDeviceReportFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReportFilter.toParams(self)
        kparams.put("objectType", "KalturaDeviceReportFilter")
        kparams.addIntIfDefined("lastAccessDateGreaterThanOrEqual", self.lastAccessDateGreaterThanOrEqual)
        return kparams

    def getLastAccessDateGreaterThanOrEqual(self):
        return self.lastAccessDateGreaterThanOrEqual

    def setLastAccessDateGreaterThanOrEqual(self, newLastAccessDateGreaterThanOrEqual):
        self.lastAccessDateGreaterThanOrEqual = newLastAccessDateGreaterThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupTagFilter(KalturaFilter):
    """Configuration group tag filter"""

    def __init__(self,
            orderBy=NotImplemented,
            configurationGroupIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # the ID of the configuration group for which to return related configurations group tags
        # @var string
        self.configurationGroupIdEqual = configurationGroupIdEqual


    PROPERTY_LOADERS = {
        'configurationGroupIdEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationGroupTagFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaConfigurationGroupTagFilter")
        kparams.addStringIfDefined("configurationGroupIdEqual", self.configurationGroupIdEqual)
        return kparams

    def getConfigurationGroupIdEqual(self):
        return self.configurationGroupIdEqual

    def setConfigurationGroupIdEqual(self, newConfigurationGroupIdEqual):
        self.configurationGroupIdEqual = newConfigurationGroupIdEqual


# @package Kaltura
# @subpackage Client
class KalturaConfigurationGroupDeviceFilter(KalturaFilter):
    """Configuration group device filter"""

    def __init__(self,
            orderBy=NotImplemented,
            configurationGroupIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # the ID of the configuration group for which to return related configurations group devices
        # @var string
        self.configurationGroupIdEqual = configurationGroupIdEqual


    PROPERTY_LOADERS = {
        'configurationGroupIdEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaConfigurationGroupDeviceFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaConfigurationGroupDeviceFilter")
        kparams.addStringIfDefined("configurationGroupIdEqual", self.configurationGroupIdEqual)
        return kparams

    def getConfigurationGroupIdEqual(self):
        return self.configurationGroupIdEqual

    def setConfigurationGroupIdEqual(self, newConfigurationGroupIdEqual):
        self.configurationGroupIdEqual = newConfigurationGroupIdEqual


# @package Kaltura
# @subpackage Client
class KalturaFavoriteFilter(KalturaFilter):
    """Favorite request filter"""

    def __init__(self,
            orderBy=NotImplemented,
            mediaTypeEqual=NotImplemented,
            mediaIdIn=NotImplemented,
            udidEqualCurrent=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Media type to filter by the favorite assets
        # @var int
        self.mediaTypeEqual = mediaTypeEqual

        # Media identifiers from which to filter the favorite assets
        # @var string
        self.mediaIdIn = mediaIdIn

        # Indicates whether the results should be filtered by origin UDID using the current
        # @var bool
        self.udidEqualCurrent = udidEqualCurrent


    PROPERTY_LOADERS = {
        'mediaTypeEqual': getXmlNodeInt, 
        'mediaIdIn': getXmlNodeText, 
        'udidEqualCurrent': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFavoriteFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaFavoriteFilter")
        kparams.addIntIfDefined("mediaTypeEqual", self.mediaTypeEqual)
        kparams.addStringIfDefined("mediaIdIn", self.mediaIdIn)
        kparams.addBoolIfDefined("udidEqualCurrent", self.udidEqualCurrent)
        return kparams

    def getMediaTypeEqual(self):
        return self.mediaTypeEqual

    def setMediaTypeEqual(self, newMediaTypeEqual):
        self.mediaTypeEqual = newMediaTypeEqual

    def getMediaIdIn(self):
        return self.mediaIdIn

    def setMediaIdIn(self, newMediaIdIn):
        self.mediaIdIn = newMediaIdIn

    def getUdidEqualCurrent(self):
        return self.udidEqualCurrent

    def setUdidEqualCurrent(self, newUdidEqualCurrent):
        self.udidEqualCurrent = newUdidEqualCurrent


# @package Kaltura
# @subpackage Client
class KalturaOTTUserFilter(KalturaFilter):
    """OTT User filter"""

    def __init__(self,
            orderBy=NotImplemented,
            usernameEqual=NotImplemented,
            externalIdEqual=NotImplemented,
            idIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Username
        # @var string
        self.usernameEqual = usernameEqual

        # User external identifier
        # @var string
        self.externalIdEqual = externalIdEqual

        # List of user identifiers separated by &#39;,&#39;
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'usernameEqual': getXmlNodeText, 
        'externalIdEqual': getXmlNodeText, 
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaOTTUserFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaOTTUserFilter")
        kparams.addStringIfDefined("usernameEqual", self.usernameEqual)
        kparams.addStringIfDefined("externalIdEqual", self.externalIdEqual)
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getUsernameEqual(self):
        return self.usernameEqual

    def setUsernameEqual(self, newUsernameEqual):
        self.usernameEqual = newUsernameEqual

    def getExternalIdEqual(self):
        return self.externalIdEqual

    def setExternalIdEqual(self, newExternalIdEqual):
        self.externalIdEqual = newExternalIdEqual

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaCollectionFilter(KalturaFilter):
    """Collection Filter"""

    def __init__(self,
            orderBy=NotImplemented,
            collectionIdIn=NotImplemented,
            mediaFileIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated collection IDs
        # @var string
        self.collectionIdIn = collectionIdIn

        # Media-file ID to get the subscriptions by
        # @var int
        self.mediaFileIdEqual = mediaFileIdEqual


    PROPERTY_LOADERS = {
        'collectionIdIn': getXmlNodeText, 
        'mediaFileIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCollectionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaCollectionFilter")
        kparams.addStringIfDefined("collectionIdIn", self.collectionIdIn)
        kparams.addIntIfDefined("mediaFileIdEqual", self.mediaFileIdEqual)
        return kparams

    def getCollectionIdIn(self):
        return self.collectionIdIn

    def setCollectionIdIn(self, newCollectionIdIn):
        self.collectionIdIn = newCollectionIdIn

    def getMediaFileIdEqual(self):
        return self.mediaFileIdEqual

    def setMediaFileIdEqual(self, newMediaFileIdEqual):
        self.mediaFileIdEqual = newMediaFileIdEqual


# @package Kaltura
# @subpackage Client
class KalturaDiscountDetailsFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated discount codes
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaDiscountDetailsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaDiscountDetailsFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaPricePlanFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated price plans identifiers
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPricePlanFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPricePlanFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaPriceDetailsFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated price identifiers
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPriceDetailsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPriceDetailsFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionSetFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented,
            subscriptionIdContains=NotImplemented,
            typeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated identifiers
        # @var string
        self.idIn = idIn

        # Comma separated subscription identifiers
        # @var string
        self.subscriptionIdContains = subscriptionIdContains

        # Subscription Type
        # @var KalturaSubscriptionSetType
        self.typeEqual = typeEqual


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
        'subscriptionIdContains': getXmlNodeText, 
        'typeEqual': (KalturaEnumsFactory.createString, "KalturaSubscriptionSetType"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionSetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionSetFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("subscriptionIdContains", self.subscriptionIdContains)
        kparams.addStringEnumIfDefined("typeEqual", self.typeEqual)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getSubscriptionIdContains(self):
        return self.subscriptionIdContains

    def setSubscriptionIdContains(self, newSubscriptionIdContains):
        self.subscriptionIdContains = newSubscriptionIdContains

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionDependencySetFilter(KalturaSubscriptionSetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented,
            subscriptionIdContains=NotImplemented,
            typeEqual=NotImplemented,
            baseSubscriptionIdIn=NotImplemented):
        KalturaSubscriptionSetFilter.__init__(self,
            orderBy,
            idIn,
            subscriptionIdContains,
            typeEqual)

        # Comma separated identifiers
        # @var string
        self.baseSubscriptionIdIn = baseSubscriptionIdIn


    PROPERTY_LOADERS = {
        'baseSubscriptionIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaSubscriptionSetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionDependencySetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSubscriptionSetFilter.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionDependencySetFilter")
        kparams.addStringIfDefined("baseSubscriptionIdIn", self.baseSubscriptionIdIn)
        return kparams

    def getBaseSubscriptionIdIn(self):
        return self.baseSubscriptionIdIn

    def setBaseSubscriptionIdIn(self, newBaseSubscriptionIdIn):
        self.baseSubscriptionIdIn = newBaseSubscriptionIdIn


# @package Kaltura
# @subpackage Client
class KalturaSubscriptionFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            subscriptionIdIn=NotImplemented,
            mediaFileIdEqual=NotImplemented,
            externalIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated subscription IDs to get the subscriptions by
        # @var string
        self.subscriptionIdIn = subscriptionIdIn

        # Media-file ID to get the subscriptions by
        # @var int
        self.mediaFileIdEqual = mediaFileIdEqual

        # Comma separated subscription external IDs to get the subscriptions by
        # @var string
        self.externalIdIn = externalIdIn


    PROPERTY_LOADERS = {
        'subscriptionIdIn': getXmlNodeText, 
        'mediaFileIdEqual': getXmlNodeInt, 
        'externalIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSubscriptionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSubscriptionFilter")
        kparams.addStringIfDefined("subscriptionIdIn", self.subscriptionIdIn)
        kparams.addIntIfDefined("mediaFileIdEqual", self.mediaFileIdEqual)
        kparams.addStringIfDefined("externalIdIn", self.externalIdIn)
        return kparams

    def getSubscriptionIdIn(self):
        return self.subscriptionIdIn

    def setSubscriptionIdIn(self, newSubscriptionIdIn):
        self.subscriptionIdIn = newSubscriptionIdIn

    def getMediaFileIdEqual(self):
        return self.mediaFileIdEqual

    def setMediaFileIdEqual(self, newMediaFileIdEqual):
        self.mediaFileIdEqual = newMediaFileIdEqual

    def getExternalIdIn(self):
        return self.externalIdIn

    def setExternalIdIn(self, newExternalIdIn):
        self.externalIdIn = newExternalIdIn


# @package Kaltura
# @subpackage Client
class KalturaPersonalListFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            partnerListTypeIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated list of partner list types to search within. 
        #             If omitted - all types should be included.
        # @var string
        self.partnerListTypeIn = partnerListTypeIn


    PROPERTY_LOADERS = {
        'partnerListTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalListFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPersonalListFilter")
        kparams.addStringIfDefined("partnerListTypeIn", self.partnerListTypeIn)
        return kparams

    def getPartnerListTypeIn(self):
        return self.partnerListTypeIn

    def setPartnerListTypeIn(self, newPartnerListTypeIn):
        self.partnerListTypeIn = newPartnerListTypeIn


# @package Kaltura
# @subpackage Client
class KalturaEngagementFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            typeIn=NotImplemented,
            sendTimeGreaterThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # List of inbox message types to search within.
        # @var string
        self.typeIn = typeIn

        # SendTime GreaterThanOrEqual
        # @var int
        self.sendTimeGreaterThanOrEqual = sendTimeGreaterThanOrEqual


    PROPERTY_LOADERS = {
        'typeIn': getXmlNodeText, 
        'sendTimeGreaterThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEngagementFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaEngagementFilter")
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntIfDefined("sendTimeGreaterThanOrEqual", self.sendTimeGreaterThanOrEqual)
        return kparams

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getSendTimeGreaterThanOrEqual(self):
        return self.sendTimeGreaterThanOrEqual

    def setSendTimeGreaterThanOrEqual(self, newSendTimeGreaterThanOrEqual):
        self.sendTimeGreaterThanOrEqual = newSendTimeGreaterThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaReminderFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaReminderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaReminderFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaAssetReminderFilter(KalturaReminderFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaReminderFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaReminderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetReminderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReminderFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetReminderFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaSeriesReminderFilter(KalturaReminderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            seriesIdIn=NotImplemented,
            epgChannelIdEqual=NotImplemented):
        KalturaReminderFilter.__init__(self,
            orderBy)

        # Comma separated series IDs
        # @var string
        self.seriesIdIn = seriesIdIn

        # EPG channel ID
        # @var int
        self.epgChannelIdEqual = epgChannelIdEqual


    PROPERTY_LOADERS = {
        'seriesIdIn': getXmlNodeText, 
        'epgChannelIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaReminderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeriesReminderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReminderFilter.toParams(self)
        kparams.put("objectType", "KalturaSeriesReminderFilter")
        kparams.addStringIfDefined("seriesIdIn", self.seriesIdIn)
        kparams.addIntIfDefined("epgChannelIdEqual", self.epgChannelIdEqual)
        return kparams

    def getSeriesIdIn(self):
        return self.seriesIdIn

    def setSeriesIdIn(self, newSeriesIdIn):
        self.seriesIdIn = newSeriesIdIn

    def getEpgChannelIdEqual(self):
        return self.epgChannelIdEqual

    def setEpgChannelIdEqual(self, newEpgChannelIdEqual):
        self.epgChannelIdEqual = newEpgChannelIdEqual


# @package Kaltura
# @subpackage Client
class KalturaSeasonsReminderFilter(KalturaReminderFilter):
    def __init__(self,
            orderBy=NotImplemented,
            seriesIdEqual=NotImplemented,
            seasonNumberIn=NotImplemented,
            epgChannelIdEqual=NotImplemented):
        KalturaReminderFilter.__init__(self,
            orderBy)

        # Series ID
        # @var string
        self.seriesIdEqual = seriesIdEqual

        # Comma separated season numbers
        # @var string
        self.seasonNumberIn = seasonNumberIn

        # EPG channel ID
        # @var int
        self.epgChannelIdEqual = epgChannelIdEqual


    PROPERTY_LOADERS = {
        'seriesIdEqual': getXmlNodeText, 
        'seasonNumberIn': getXmlNodeText, 
        'epgChannelIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaReminderFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeasonsReminderFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaReminderFilter.toParams(self)
        kparams.put("objectType", "KalturaSeasonsReminderFilter")
        kparams.addStringIfDefined("seriesIdEqual", self.seriesIdEqual)
        kparams.addStringIfDefined("seasonNumberIn", self.seasonNumberIn)
        kparams.addIntIfDefined("epgChannelIdEqual", self.epgChannelIdEqual)
        return kparams

    def getSeriesIdEqual(self):
        return self.seriesIdEqual

    def setSeriesIdEqual(self, newSeriesIdEqual):
        self.seriesIdEqual = newSeriesIdEqual

    def getSeasonNumberIn(self):
        return self.seasonNumberIn

    def setSeasonNumberIn(self, newSeasonNumberIn):
        self.seasonNumberIn = newSeasonNumberIn

    def getEpgChannelIdEqual(self):
        return self.epgChannelIdEqual

    def setEpgChannelIdEqual(self, newEpgChannelIdEqual):
        self.epgChannelIdEqual = newEpgChannelIdEqual


# @package Kaltura
# @subpackage Client
class KalturaFollowTvSeriesFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaFollowTvSeriesFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaFollowTvSeriesFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaInboxMessageFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            typeIn=NotImplemented,
            createdAtGreaterThanOrEqual=NotImplemented,
            createdAtLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # List of inbox message types to search within.
        # @var string
        self.typeIn = typeIn

        # createdAtGreaterThanOrEqual
        # @var int
        self.createdAtGreaterThanOrEqual = createdAtGreaterThanOrEqual

        # createdAtLessThanOrEqual
        # @var int
        self.createdAtLessThanOrEqual = createdAtLessThanOrEqual


    PROPERTY_LOADERS = {
        'typeIn': getXmlNodeText, 
        'createdAtGreaterThanOrEqual': getXmlNodeInt, 
        'createdAtLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaInboxMessageFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaInboxMessageFilter")
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntIfDefined("createdAtGreaterThanOrEqual", self.createdAtGreaterThanOrEqual)
        kparams.addIntIfDefined("createdAtLessThanOrEqual", self.createdAtLessThanOrEqual)
        return kparams

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getCreatedAtGreaterThanOrEqual(self):
        return self.createdAtGreaterThanOrEqual

    def setCreatedAtGreaterThanOrEqual(self, newCreatedAtGreaterThanOrEqual):
        self.createdAtGreaterThanOrEqual = newCreatedAtGreaterThanOrEqual

    def getCreatedAtLessThanOrEqual(self):
        return self.createdAtLessThanOrEqual

    def setCreatedAtLessThanOrEqual(self, newCreatedAtLessThanOrEqual):
        self.createdAtLessThanOrEqual = newCreatedAtLessThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaAnnouncementFilter(KalturaFilter):
    """order announcements"""

    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAnnouncementFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAnnouncementFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPersonalFeedFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalFeedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPersonalFeedFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaTopicFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTopicFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaTopicFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaSeriesRecordingFilter(KalturaFilter):
    """Filtering recordings"""

    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSeriesRecordingFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSeriesRecordingFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaProductPriceFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            subscriptionIdIn=NotImplemented,
            fileIdIn=NotImplemented,
            collectionIdIn=NotImplemented,
            isLowest=NotImplemented,
            couponCodeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated subscriptions identifiers
        # @var string
        self.subscriptionIdIn = subscriptionIdIn

        # Comma separated media files identifiers
        # @var string
        self.fileIdIn = fileIdIn

        # Comma separated collections identifiers
        # @var string
        self.collectionIdIn = collectionIdIn

        # A flag that indicates if only the lowest price of an item should return
        # @var bool
        self.isLowest = isLowest

        # Discount coupon code
        # @var string
        self.couponCodeEqual = couponCodeEqual


    PROPERTY_LOADERS = {
        'subscriptionIdIn': getXmlNodeText, 
        'fileIdIn': getXmlNodeText, 
        'collectionIdIn': getXmlNodeText, 
        'isLowest': getXmlNodeBool, 
        'couponCodeEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaProductPriceFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaProductPriceFilter")
        kparams.addStringIfDefined("subscriptionIdIn", self.subscriptionIdIn)
        kparams.addStringIfDefined("fileIdIn", self.fileIdIn)
        kparams.addStringIfDefined("collectionIdIn", self.collectionIdIn)
        kparams.addBoolIfDefined("isLowest", self.isLowest)
        kparams.addStringIfDefined("couponCodeEqual", self.couponCodeEqual)
        return kparams

    def getSubscriptionIdIn(self):
        return self.subscriptionIdIn

    def setSubscriptionIdIn(self, newSubscriptionIdIn):
        self.subscriptionIdIn = newSubscriptionIdIn

    def getFileIdIn(self):
        return self.fileIdIn

    def setFileIdIn(self, newFileIdIn):
        self.fileIdIn = newFileIdIn

    def getCollectionIdIn(self):
        return self.collectionIdIn

    def setCollectionIdIn(self, newCollectionIdIn):
        self.collectionIdIn = newCollectionIdIn

    def getIsLowest(self):
        return self.isLowest

    def setIsLowest(self, newIsLowest):
        self.isLowest = newIsLowest

    def getCouponCodeEqual(self):
        return self.couponCodeEqual

    def setCouponCodeEqual(self, newCouponCodeEqual):
        self.couponCodeEqual = newCouponCodeEqual


# @package Kaltura
# @subpackage Client
class KalturaEntitlementFilter(KalturaFilter):
    """Entitlements filter"""

    def __init__(self,
            orderBy=NotImplemented,
            productTypeEqual=NotImplemented,
            entityReferenceEqual=NotImplemented,
            isExpiredEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # The type of the entitlements to return
        # @var KalturaTransactionType
        self.productTypeEqual = productTypeEqual

        # Reference type to filter by
        # @var KalturaEntityReferenceBy
        self.entityReferenceEqual = entityReferenceEqual

        # Is expired
        # @var bool
        self.isExpiredEqual = isExpiredEqual


    PROPERTY_LOADERS = {
        'productTypeEqual': (KalturaEnumsFactory.createString, "KalturaTransactionType"), 
        'entityReferenceEqual': (KalturaEnumsFactory.createString, "KalturaEntityReferenceBy"), 
        'isExpiredEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaEntitlementFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaEntitlementFilter")
        kparams.addStringEnumIfDefined("productTypeEqual", self.productTypeEqual)
        kparams.addStringEnumIfDefined("entityReferenceEqual", self.entityReferenceEqual)
        kparams.addBoolIfDefined("isExpiredEqual", self.isExpiredEqual)
        return kparams

    def getProductTypeEqual(self):
        return self.productTypeEqual

    def setProductTypeEqual(self, newProductTypeEqual):
        self.productTypeEqual = newProductTypeEqual

    def getEntityReferenceEqual(self):
        return self.entityReferenceEqual

    def setEntityReferenceEqual(self, newEntityReferenceEqual):
        self.entityReferenceEqual = newEntityReferenceEqual

    def getIsExpiredEqual(self):
        return self.isExpiredEqual

    def setIsExpiredEqual(self, newIsExpiredEqual):
        self.isExpiredEqual = newIsExpiredEqual


# @package Kaltura
# @subpackage Client
class KalturaTransactionHistoryFilter(KalturaFilter):
    """Transactions filter"""

    def __init__(self,
            orderBy=NotImplemented,
            entityReferenceEqual=NotImplemented,
            startDateGreaterThanOrEqual=NotImplemented,
            endDateLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Reference type to filter by
        # @var KalturaEntityReferenceBy
        self.entityReferenceEqual = entityReferenceEqual

        # Filter transactions later than specific date
        # @var int
        self.startDateGreaterThanOrEqual = startDateGreaterThanOrEqual

        # Filter transactions earlier than specific date
        # @var int
        self.endDateLessThanOrEqual = endDateLessThanOrEqual


    PROPERTY_LOADERS = {
        'entityReferenceEqual': (KalturaEnumsFactory.createString, "KalturaEntityReferenceBy"), 
        'startDateGreaterThanOrEqual': getXmlNodeInt, 
        'endDateLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTransactionHistoryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaTransactionHistoryFilter")
        kparams.addStringEnumIfDefined("entityReferenceEqual", self.entityReferenceEqual)
        kparams.addIntIfDefined("startDateGreaterThanOrEqual", self.startDateGreaterThanOrEqual)
        kparams.addIntIfDefined("endDateLessThanOrEqual", self.endDateLessThanOrEqual)
        return kparams

    def getEntityReferenceEqual(self):
        return self.entityReferenceEqual

    def setEntityReferenceEqual(self, newEntityReferenceEqual):
        self.entityReferenceEqual = newEntityReferenceEqual

    def getStartDateGreaterThanOrEqual(self):
        return self.startDateGreaterThanOrEqual

    def setStartDateGreaterThanOrEqual(self, newStartDateGreaterThanOrEqual):
        self.startDateGreaterThanOrEqual = newStartDateGreaterThanOrEqual

    def getEndDateLessThanOrEqual(self):
        return self.endDateLessThanOrEqual

    def setEndDateLessThanOrEqual(self, newEndDateLessThanOrEqual):
        self.endDateLessThanOrEqual = newEndDateLessThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaRecordingContextFilter(KalturaFilter):
    """Filtering assets"""

    def __init__(self,
            orderBy=NotImplemented,
            assetIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated asset ids
        # @var string
        self.assetIdIn = assetIdIn


    PROPERTY_LOADERS = {
        'assetIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecordingContextFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaRecordingContextFilter")
        kparams.addStringIfDefined("assetIdIn", self.assetIdIn)
        return kparams

    def getAssetIdIn(self):
        return self.assetIdIn

    def setAssetIdIn(self, newAssetIdIn):
        self.assetIdIn = newAssetIdIn


# @package Kaltura
# @subpackage Client
class KalturaRecordingFilter(KalturaFilter):
    """Filtering recordings"""

    def __init__(self,
            orderBy=NotImplemented,
            statusIn=NotImplemented,
            kSql=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Recording Statuses
        # @var string
        self.statusIn = statusIn

        # KSQL expression
        # @var string
        self.kSql = kSql


    PROPERTY_LOADERS = {
        'statusIn': getXmlNodeText, 
        'kSql': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRecordingFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaRecordingFilter")
        kparams.addStringIfDefined("statusIn", self.statusIn)
        kparams.addStringIfDefined("kSql", self.kSql)
        return kparams

    def getStatusIn(self):
        return self.statusIn

    def setStatusIn(self, newStatusIn):
        self.statusIn = newStatusIn

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql


# @package Kaltura
# @subpackage Client
class KalturaPartnerConfigurationFilter(KalturaFilter):
    """Partner configuration filter"""

    def __init__(self,
            orderBy=NotImplemented,
            partnerConfigurationTypeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Indicates which partner configuration list to return
        # @var KalturaPartnerConfigurationType
        self.partnerConfigurationTypeEqual = partnerConfigurationTypeEqual


    PROPERTY_LOADERS = {
        'partnerConfigurationTypeEqual': (KalturaEnumsFactory.createString, "KalturaPartnerConfigurationType"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPartnerConfigurationFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPartnerConfigurationFilter")
        kparams.addStringEnumIfDefined("partnerConfigurationTypeEqual", self.partnerConfigurationTypeEqual)
        return kparams

    def getPartnerConfigurationTypeEqual(self):
        return self.partnerConfigurationTypeEqual

    def setPartnerConfigurationTypeEqual(self, newPartnerConfigurationTypeEqual):
        self.partnerConfigurationTypeEqual = newPartnerConfigurationTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaAggregationCountFilter(KalturaRelatedObjectFilter):
    """Kaltura Aggregation CountFilter"""

    def __init__(self,
            orderBy=NotImplemented):
        KalturaRelatedObjectFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaRelatedObjectFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAggregationCountFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaRelatedObjectFilter.toParams(self)
        kparams.put("objectType", "KalturaAggregationCountFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaPersistedFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Name for the presisted filter. If empty, no action will be done. If has value, the filter will be saved and persisted in user&#39;s search history.
        # @var string
        self.name = name


    PROPERTY_LOADERS = {
        'name': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersistedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaPersistedFilter")
        kparams.addStringIfDefined("name", self.name)
        return kparams

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName


# @package Kaltura
# @subpackage Client
class KalturaAssetFilter(KalturaPersistedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented):
        KalturaPersistedFilter.__init__(self,
            orderBy,
            name)

        # dynamicOrderBy - order by Meta
        # @var KalturaDynamicOrderBy
        self.dynamicOrderBy = dynamicOrderBy


    PROPERTY_LOADERS = {
        'dynamicOrderBy': (KalturaObjectFactory.create, 'KalturaDynamicOrderBy'), 
    }

    def fromXml(self, node):
        KalturaPersistedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPersistedFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetFilter")
        kparams.addObjectIfDefined("dynamicOrderBy", self.dynamicOrderBy)
        return kparams

    def getDynamicOrderBy(self):
        return self.dynamicOrderBy

    def setDynamicOrderBy(self, newDynamicOrderBy):
        self.dynamicOrderBy = newDynamicOrderBy


# @package Kaltura
# @subpackage Client
class KalturaBaseSearchAssetFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            kSql=NotImplemented,
            groupBy=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy)

        # Search assets using dynamic criteria. Provided collection of nested expressions with key, comparison operators, value, and logical conjunction.
        #             Possible keys: any Tag or Meta defined in the system and the following reserved keys: start_date, end_date. 
        #             epg_id, media_id - for specific asset IDs.
        #             geo_block - only valid value is &quot;true&quot;: When enabled, only assets that are not restricted to the user by geo-block rules will return.
        #             parental_rules - only valid value is &quot;true&quot;: When enabled, only assets that the user doesn&#39;t need to provide PIN code will return.
        #             user_interests - only valid value is &quot;true&quot;. When enabled, only assets that the user defined as his interests (by tags and metas) will return.
        #             epg_channel_id - the channel identifier of the EPG program.
        #             entitled_assets - valid values: &quot;free&quot;, &quot;entitled&quot;, &quot;not_entitled&quot;, &quot;both&quot;. free - gets only free to watch assets. entitled - only those that the user is implicitly entitled to watch.
        #             asset_type - valid values: &quot;media&quot;, &quot;epg&quot;, &quot;recording&quot; or any number that represents media type in group.
        #             Comparison operators: for numerical fields =, &gt;, &gt;=, &lt;, &lt;=, : (in). 
        #             For alpha-numerical fields =, != (not), ~ (like), !~, ^ (any word starts with), ^= (phrase starts with), + (exists), !+ (not exists).
        #             Logical conjunction: and, or. 
        #             Search values are limited to 20 characters each for the next operators: ~, !~, ^, ^=
        #             (maximum length of entire filter is 2048 characters)
        # @var string
        self.kSql = kSql

        # groupBy
        # @var array of KalturaAssetGroupBy
        self.groupBy = groupBy


    PROPERTY_LOADERS = {
        'kSql': getXmlNodeText, 
        'groupBy': (KalturaObjectFactory.createArray, 'KalturaAssetGroupBy'), 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBaseSearchAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaBaseSearchAssetFilter")
        kparams.addStringIfDefined("kSql", self.kSql)
        kparams.addArrayIfDefined("groupBy", self.groupBy)
        return kparams

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql

    def getGroupBy(self):
        return self.groupBy

    def setGroupBy(self, newGroupBy):
        self.groupBy = newGroupBy


# @package Kaltura
# @subpackage Client
class KalturaPersonalListSearchFilter(KalturaBaseSearchAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            kSql=NotImplemented,
            groupBy=NotImplemented,
            partnerListTypeIn=NotImplemented):
        KalturaBaseSearchAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy,
            kSql,
            groupBy)

        # Comma separated list of partner list types to search within. 
        #             If omitted - all types should be included.
        # @var string
        self.partnerListTypeIn = partnerListTypeIn


    PROPERTY_LOADERS = {
        'partnerListTypeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseSearchAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaPersonalListSearchFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSearchAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaPersonalListSearchFilter")
        kparams.addStringIfDefined("partnerListTypeIn", self.partnerListTypeIn)
        return kparams

    def getPartnerListTypeIn(self):
        return self.partnerListTypeIn

    def setPartnerListTypeIn(self, newPartnerListTypeIn):
        self.partnerListTypeIn = newPartnerListTypeIn


# @package Kaltura
# @subpackage Client
class KalturaSearchAssetFilter(KalturaBaseSearchAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            kSql=NotImplemented,
            groupBy=NotImplemented,
            kSql=NotImplemented,
            typeIn=NotImplemented,
            idIn=NotImplemented):
        KalturaBaseSearchAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy,
            kSql,
            groupBy)

        # Search assets using dynamic criteria. Provided collection of nested expressions with key, comparison operators, value, and logical conjunction.
        #             Possible keys: any Tag or Meta defined in the system and the following reserved keys: start_date, end_date. 
        #             epg_id, media_id - for specific asset IDs.
        #             geo_block - only valid value is &quot;true&quot;: When enabled, only assets that are not restriced to the user by geo-block rules will return.
        #             parental_rules - only valid value is &quot;true&quot;: When enabled, only assets that the user doesn&#39;t need to provide PIN code will return.
        #             user_interests - only valid value is &quot;true&quot;. When enabled, only assets that the user defined as his interests (by tags and metas) will return.
        #             epg_channel_id - the channel identifier of the EPG program. *****Deprecated, please use linear_media_id instead*****
        #             linear_media_id - the linear media identifier of the EPG program.
        #             entitled_assets - valid values: &quot;free&quot;, &quot;entitled&quot;, &quot;both&quot;. free - gets only free to watch assets. entitled - only those that the user is implicitly entitled to watch.
        #             asset_type - valid values: &quot;media&quot;, &quot;epg&quot;, &quot;recording&quot; or any number that represents media type in group.
        #             Comparison operators: for numerical fields =, &gt;, &gt;=, &lt;, &lt;=, : (in). 
        #             For alpha-numerical fields =, != (not), ~ (like), !~, ^ (any word starts with), ^= (phrase starts with), + (exists), !+ (not exists).
        #             Logical conjunction: and, or. 
        #             Search values are limited to 20 characters each.
        #             (maximum length of entire filter is 2048 characters)
        # @var string
        self.kSql = kSql

        # (Deprecated - use KalturaBaseSearchAssetFilter.kSql)
        #             Comma separated list of asset types to search within. 
        #             Possible values: 0 - EPG linear programs entries; 1 - Recordings; Any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted - all types should be included.
        # @var string
        self.typeIn = typeIn

        # Comma separated list of EPG channel ids to search within. *****Deprecated, please use linear_media_id inside kSql instead*****
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'kSql': getXmlNodeText, 
        'typeIn': getXmlNodeText, 
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaBaseSearchAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchAssetFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSearchAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaSearchAssetFilter")
        kparams.addStringIfDefined("kSql", self.kSql)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaSearchAssetListFilter(KalturaSearchAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            kSql=NotImplemented,
            groupBy=NotImplemented,
            kSql=NotImplemented,
            typeIn=NotImplemented,
            idIn=NotImplemented,
            excludeWatched=NotImplemented):
        KalturaSearchAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy,
            kSql,
            groupBy,
            kSql,
            typeIn,
            idIn)

        # Exclude watched asset.
        # @var bool
        self.excludeWatched = excludeWatched


    PROPERTY_LOADERS = {
        'excludeWatched': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaSearchAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchAssetListFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaSearchAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaSearchAssetListFilter")
        kparams.addBoolIfDefined("excludeWatched", self.excludeWatched)
        return kparams

    def getExcludeWatched(self):
        return self.excludeWatched

    def setExcludeWatched(self, newExcludeWatched):
        self.excludeWatched = newExcludeWatched


# @package Kaltura
# @subpackage Client
class KalturaScheduledRecordingProgramFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            recordingTypeEqual=NotImplemented,
            channelsIn=NotImplemented,
            startDateGreaterThanOrNull=NotImplemented,
            endDateLessThanOrNull=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy)

        # The type of recordings to return
        # @var KalturaScheduledRecordingAssetType
        self.recordingTypeEqual = recordingTypeEqual

        # Channels to filter by
        # @var string
        self.channelsIn = channelsIn

        # start date
        # @var int
        self.startDateGreaterThanOrNull = startDateGreaterThanOrNull

        # end date
        # @var int
        self.endDateLessThanOrNull = endDateLessThanOrNull


    PROPERTY_LOADERS = {
        'recordingTypeEqual': (KalturaEnumsFactory.createString, "KalturaScheduledRecordingAssetType"), 
        'channelsIn': getXmlNodeText, 
        'startDateGreaterThanOrNull': getXmlNodeInt, 
        'endDateLessThanOrNull': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaScheduledRecordingProgramFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaScheduledRecordingProgramFilter")
        kparams.addStringEnumIfDefined("recordingTypeEqual", self.recordingTypeEqual)
        kparams.addStringIfDefined("channelsIn", self.channelsIn)
        kparams.addIntIfDefined("startDateGreaterThanOrNull", self.startDateGreaterThanOrNull)
        kparams.addIntIfDefined("endDateLessThanOrNull", self.endDateLessThanOrNull)
        return kparams

    def getRecordingTypeEqual(self):
        return self.recordingTypeEqual

    def setRecordingTypeEqual(self, newRecordingTypeEqual):
        self.recordingTypeEqual = newRecordingTypeEqual

    def getChannelsIn(self):
        return self.channelsIn

    def setChannelsIn(self, newChannelsIn):
        self.channelsIn = newChannelsIn

    def getStartDateGreaterThanOrNull(self):
        return self.startDateGreaterThanOrNull

    def setStartDateGreaterThanOrNull(self, newStartDateGreaterThanOrNull):
        self.startDateGreaterThanOrNull = newStartDateGreaterThanOrNull

    def getEndDateLessThanOrNull(self):
        return self.endDateLessThanOrNull

    def setEndDateLessThanOrNull(self, newEndDateLessThanOrNull):
        self.endDateLessThanOrNull = newEndDateLessThanOrNull


# @package Kaltura
# @subpackage Client
class KalturaBundleFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            idEqual=NotImplemented,
            typeIn=NotImplemented,
            bundleTypeEqual=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy)

        # Bundle Id.
        # @var int
        self.idEqual = idEqual

        # Comma separated list of asset types to search within. 
        #             Possible values: 0 - EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted - all types should be included.
        # @var string
        self.typeIn = typeIn

        # bundleType - possible values: Subscription or Collection
        # @var KalturaBundleType
        self.bundleTypeEqual = bundleTypeEqual


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'typeIn': getXmlNodeText, 
        'bundleTypeEqual': (KalturaEnumsFactory.createString, "KalturaBundleType"), 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBundleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaBundleFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addStringEnumIfDefined("bundleTypeEqual", self.bundleTypeEqual)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getBundleTypeEqual(self):
        return self.bundleTypeEqual

    def setBundleTypeEqual(self, newBundleTypeEqual):
        self.bundleTypeEqual = newBundleTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaChannelExternalFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            idEqual=NotImplemented,
            utcOffsetEqual=NotImplemented,
            freeText=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy)

        # External Channel Id.
        # @var int
        self.idEqual = idEqual

        # UtcOffsetEqual
        # @var float
        self.utcOffsetEqual = utcOffsetEqual

        # FreeTextEqual
        # @var string
        self.freeText = freeText


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'utcOffsetEqual': getXmlNodeFloat, 
        'freeText': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelExternalFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaChannelExternalFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addFloatIfDefined("utcOffsetEqual", self.utcOffsetEqual)
        kparams.addStringIfDefined("freeText", self.freeText)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getUtcOffsetEqual(self):
        return self.utcOffsetEqual

    def setUtcOffsetEqual(self, newUtcOffsetEqual):
        self.utcOffsetEqual = newUtcOffsetEqual

    def getFreeText(self):
        return self.freeText

    def setFreeText(self, newFreeText):
        self.freeText = newFreeText


# @package Kaltura
# @subpackage Client
class KalturaChannelFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            idEqual=NotImplemented,
            kSql=NotImplemented,
            excludeWatched=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy)

        # Channel Id
        # @var int
        self.idEqual = idEqual

        # /// 
        #             Search assets using dynamic criteria. Provided collection of nested expressions with key, comparison operators, value, and logical conjunction.
        #             Possible keys: any Tag or Meta defined in the system and the following reserved keys: start_date, end_date. 
        #             epg_id, media_id - for specific asset IDs.
        #             geo_block - only valid value is &quot;true&quot;: When enabled, only assets that are not restricted to the user by geo-block rules will return.
        #             parental_rules - only valid value is &quot;true&quot;: When enabled, only assets that the user doesn&#39;t need to provide PIN code will return.
        #             user_interests - only valid value is &quot;true&quot;. When enabled, only assets that the user defined as his interests (by tags and metas) will return.
        #             epg_channel_id - the channel identifier of the EPG program. *****Deprecated, please use linear_media_id instead*****
        #             linear_media_id - the linear media identifier of the EPG program.
        #             entitled_assets - valid values: &quot;free&quot;, &quot;entitled&quot;, &quot;not_entitled&quot;, &quot;both&quot;. free - gets only free to watch assets. entitled - only those that the user is implicitly entitled to watch.
        #             asset_type - valid values: &quot;media&quot;, &quot;epg&quot;, &quot;recording&quot; or any number that represents media type in group.
        #             Comparison operators: for numerical fields =, &gt;, &gt;=, &lt;, &lt;=, : (in). 
        #             For alpha-numerical fields =, != (not), ~ (like), !~, ^ (any word starts with), ^= (phrase starts with), + (exists), !+ (not exists).
        #             Logical conjunction: and, or. 
        #             Search values are limited to 20 characters each for the next operators: ~, !~, ^, ^=
        #             (maximum length of entire filter is 2048 characters)
        # @var string
        self.kSql = kSql

        # Exclude watched asset.
        # @var bool
        self.excludeWatched = excludeWatched


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'kSql': getXmlNodeText, 
        'excludeWatched': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaChannelFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("kSql", self.kSql)
        kparams.addBoolIfDefined("excludeWatched", self.excludeWatched)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql

    def getExcludeWatched(self):
        return self.excludeWatched

    def setExcludeWatched(self, newExcludeWatched):
        self.excludeWatched = newExcludeWatched


# @package Kaltura
# @subpackage Client
class KalturaRelatedFilter(KalturaBaseSearchAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            kSql=NotImplemented,
            groupBy=NotImplemented,
            kSql=NotImplemented,
            idEqual=NotImplemented,
            typeIn=NotImplemented,
            excludeWatched=NotImplemented):
        KalturaBaseSearchAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy,
            kSql,
            groupBy)

        # Search assets using dynamic criteria. Provided collection of nested expressions with key, comparison operators, value, and logical conjunction.
        #             Possible keys: any Tag or Meta defined in the system and the following reserved keys: start_date, end_date. 
        #             epg_id, media_id - for specific asset IDs.
        #             geo_block - only valid value is &quot;true&quot;: When enabled, only assets that are not restriced to the user by geo-block rules will return.
        #             parental_rules - only valid value is &quot;true&quot;: When enabled, only assets that the user doesn&#39;t need to provide PIN code will return.
        #             user_interests - only valid value is &quot;true&quot;. When enabled, only assets that the user defined as his interests (by tags and metas) will return.
        #             epg_channel_id - the channel identifier of the EPG program. *****Deprecated, please use linear_media_id instead*****
        #             linear_media_id - the linear media identifier of the EPG program.
        #             entitled_assets - valid values: &quot;free&quot;, &quot;entitled&quot;, &quot;both&quot;. free - gets only free to watch assets. entitled - only those that the user is implicitly entitled to watch.
        #             Comparison operators: for numerical fields =, &gt;, &gt;=, &lt;, &lt;=, : (in). 
        #             For alpha-numerical fields =, != (not), ~ (like), !~, ^ (any word starts with), ^= (phrase starts with), + (exists), !+ (not exists).
        #             Logical conjunction: and, or. 
        #             Search values are limited to 20 characters each.
        #             (maximum length of entire filter is 2048 characters)
        # @var string
        self.kSql = kSql

        # the ID of the asset for which to return related assets
        # @var int
        self.idEqual = idEqual

        # (Deprecated - use KalturaBaseSearchAssetFilter.kSql)
        #             Comma separated list of asset types to search within. 
        #             Possible values: any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted -   same type as the provided asset.
        # @var string
        self.typeIn = typeIn

        # Exclude watched asset.
        # @var bool
        self.excludeWatched = excludeWatched


    PROPERTY_LOADERS = {
        'kSql': getXmlNodeText, 
        'idEqual': getXmlNodeInt, 
        'typeIn': getXmlNodeText, 
        'excludeWatched': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaBaseSearchAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRelatedFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaBaseSearchAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaRelatedFilter")
        kparams.addStringIfDefined("kSql", self.kSql)
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addBoolIfDefined("excludeWatched", self.excludeWatched)
        return kparams

    def getKSql(self):
        return self.kSql

    def setKSql(self, newKSql):
        self.kSql = newKSql

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getExcludeWatched(self):
        return self.excludeWatched

    def setExcludeWatched(self, newExcludeWatched):
        self.excludeWatched = newExcludeWatched


# @package Kaltura
# @subpackage Client
class KalturaRelatedExternalFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            idEqual=NotImplemented,
            typeIn=NotImplemented,
            utcOffsetEqual=NotImplemented,
            freeText=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy)

        # the External ID of the asset for which to return related assets
        # @var int
        self.idEqual = idEqual

        # Comma separated list of asset types to search within. 
        #             Possible values: 0 - EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted - all types should be included.
        # @var string
        self.typeIn = typeIn

        # UtcOffsetEqual
        # @var int
        self.utcOffsetEqual = utcOffsetEqual

        # FreeText
        # @var string
        self.freeText = freeText


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'typeIn': getXmlNodeText, 
        'utcOffsetEqual': getXmlNodeInt, 
        'freeText': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRelatedExternalFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaRelatedExternalFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addIntIfDefined("utcOffsetEqual", self.utcOffsetEqual)
        kparams.addStringIfDefined("freeText", self.freeText)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getUtcOffsetEqual(self):
        return self.utcOffsetEqual

    def setUtcOffsetEqual(self, newUtcOffsetEqual):
        self.utcOffsetEqual = newUtcOffsetEqual

    def getFreeText(self):
        return self.freeText

    def setFreeText(self, newFreeText):
        self.freeText = newFreeText


# @package Kaltura
# @subpackage Client
class KalturaSearchExternalFilter(KalturaAssetFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            dynamicOrderBy=NotImplemented,
            query=NotImplemented,
            utcOffsetEqual=NotImplemented,
            typeIn=NotImplemented):
        KalturaAssetFilter.__init__(self,
            orderBy,
            name,
            dynamicOrderBy)

        # Query
        # @var string
        self.query = query

        # UtcOffsetEqual
        # @var int
        self.utcOffsetEqual = utcOffsetEqual

        # Comma separated list of asset types to search within. 
        #             Possible values: 0 - EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted - all types should be included.
        # @var string
        self.typeIn = typeIn


    PROPERTY_LOADERS = {
        'query': getXmlNodeText, 
        'utcOffsetEqual': getXmlNodeInt, 
        'typeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaAssetFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchExternalFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaAssetFilter.toParams(self)
        kparams.put("objectType", "KalturaSearchExternalFilter")
        kparams.addStringIfDefined("query", self.query)
        kparams.addIntIfDefined("utcOffsetEqual", self.utcOffsetEqual)
        kparams.addStringIfDefined("typeIn", self.typeIn)
        return kparams

    def getQuery(self):
        return self.query

    def setQuery(self, newQuery):
        self.query = newQuery

    def getUtcOffsetEqual(self):
        return self.utcOffsetEqual

    def setUtcOffsetEqual(self, newUtcOffsetEqual):
        self.utcOffsetEqual = newUtcOffsetEqual

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn


# @package Kaltura
# @subpackage Client
class KalturaBulkFilter(KalturaPersistedFilter):
    def __init__(self,
            orderBy=NotImplemented,
            name=NotImplemented,
            statusEqual=NotImplemented):
        KalturaPersistedFilter.__init__(self,
            orderBy,
            name)

        # dynamicOrderBy - order by Meta
        # @var KalturaBatchJobStatus
        self.statusEqual = statusEqual


    PROPERTY_LOADERS = {
        'statusEqual': (KalturaEnumsFactory.createString, "KalturaBatchJobStatus"), 
    }

    def fromXml(self, node):
        KalturaPersistedFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBulkFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaPersistedFilter.toParams(self)
        kparams.put("objectType", "KalturaBulkFilter")
        kparams.addStringEnumIfDefined("statusEqual", self.statusEqual)
        return kparams

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual


# @package Kaltura
# @subpackage Client
class KalturaAssetStructMetaFilter(KalturaFilter):
    """Filtering Asset Struct Metas"""

    def __init__(self,
            orderBy=NotImplemented,
            assetStructIdEqual=NotImplemented,
            metaIdEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Filter Asset Struct metas that contain a specific asset struct id
        # @var int
        self.assetStructIdEqual = assetStructIdEqual

        # Filter Asset Struct metas that contain a specific meta id
        # @var int
        self.metaIdEqual = metaIdEqual


    PROPERTY_LOADERS = {
        'assetStructIdEqual': getXmlNodeInt, 
        'metaIdEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStructMetaFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetStructMetaFilter")
        kparams.addIntIfDefined("assetStructIdEqual", self.assetStructIdEqual)
        kparams.addIntIfDefined("metaIdEqual", self.metaIdEqual)
        return kparams

    def getAssetStructIdEqual(self):
        return self.assetStructIdEqual

    def setAssetStructIdEqual(self, newAssetStructIdEqual):
        self.assetStructIdEqual = newAssetStructIdEqual

    def getMetaIdEqual(self):
        return self.metaIdEqual

    def setMetaIdEqual(self, newMetaIdEqual):
        self.metaIdEqual = newMetaIdEqual


# @package Kaltura
# @subpackage Client
class KalturaChannelsFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idEqual=NotImplemented,
            mediaIdEqual=NotImplemented,
            nameEqual=NotImplemented,
            nameStartsWith=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # channel identifier to filter by
        # @var int
        self.idEqual = idEqual

        # media identifier to filter by
        # @var int
        self.mediaIdEqual = mediaIdEqual

        # Exact channel name to filter by
        # @var string
        self.nameEqual = nameEqual

        # Channel name starts with (auto-complete)
        # @var string
        self.nameStartsWith = nameStartsWith


    PROPERTY_LOADERS = {
        'idEqual': getXmlNodeInt, 
        'mediaIdEqual': getXmlNodeInt, 
        'nameEqual': getXmlNodeText, 
        'nameStartsWith': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaChannelsFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaChannelsFilter")
        kparams.addIntIfDefined("idEqual", self.idEqual)
        kparams.addIntIfDefined("mediaIdEqual", self.mediaIdEqual)
        kparams.addStringIfDefined("nameEqual", self.nameEqual)
        kparams.addStringIfDefined("nameStartsWith", self.nameStartsWith)
        return kparams

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual

    def getMediaIdEqual(self):
        return self.mediaIdEqual

    def setMediaIdEqual(self, newMediaIdEqual):
        self.mediaIdEqual = newMediaIdEqual

    def getNameEqual(self):
        return self.nameEqual

    def setNameEqual(self, newNameEqual):
        self.nameEqual = newNameEqual

    def getNameStartsWith(self):
        return self.nameStartsWith

    def setNameStartsWith(self, newNameStartsWith):
        self.nameStartsWith = newNameStartsWith


# @package Kaltura
# @subpackage Client
class KalturaMediaFileFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            assetIdEqual=NotImplemented,
            idEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Asset identifier to filter by
        # @var int
        self.assetIdEqual = assetIdEqual

        # Asset file identifier to filter by
        # @var int
        self.idEqual = idEqual


    PROPERTY_LOADERS = {
        'assetIdEqual': getXmlNodeInt, 
        'idEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMediaFileFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaMediaFileFilter")
        kparams.addIntIfDefined("assetIdEqual", self.assetIdEqual)
        kparams.addIntIfDefined("idEqual", self.idEqual)
        return kparams

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getIdEqual(self):
        return self.idEqual

    def setIdEqual(self, newIdEqual):
        self.idEqual = newIdEqual


# @package Kaltura
# @subpackage Client
class KalturaImageFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented,
            imageObjectIdEqual=NotImplemented,
            imageObjectTypeEqual=NotImplemented,
            isDefaultEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # IDs to filter by
        # @var string
        self.idIn = idIn

        # ID of the object the is related to, to filter by
        # @var int
        self.imageObjectIdEqual = imageObjectIdEqual

        # Type of the object the image is related to, to filter by
        # @var KalturaImageObjectType
        self.imageObjectTypeEqual = imageObjectTypeEqual

        # Filter images that are default on atleast on image type or not default at any
        # @var bool
        self.isDefaultEqual = isDefaultEqual


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
        'imageObjectIdEqual': getXmlNodeInt, 
        'imageObjectTypeEqual': (KalturaEnumsFactory.createString, "KalturaImageObjectType"), 
        'isDefaultEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaImageFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaImageFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("imageObjectIdEqual", self.imageObjectIdEqual)
        kparams.addStringEnumIfDefined("imageObjectTypeEqual", self.imageObjectTypeEqual)
        kparams.addBoolIfDefined("isDefaultEqual", self.isDefaultEqual)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getImageObjectIdEqual(self):
        return self.imageObjectIdEqual

    def setImageObjectIdEqual(self, newImageObjectIdEqual):
        self.imageObjectIdEqual = newImageObjectIdEqual

    def getImageObjectTypeEqual(self):
        return self.imageObjectTypeEqual

    def setImageObjectTypeEqual(self, newImageObjectTypeEqual):
        self.imageObjectTypeEqual = newImageObjectTypeEqual

    def getIsDefaultEqual(self):
        return self.isDefaultEqual

    def setIsDefaultEqual(self, newIsDefaultEqual):
        self.isDefaultEqual = newIsDefaultEqual


# @package Kaltura
# @subpackage Client
class KalturaImageTypeFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented,
            ratioIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # IDs to filter by
        # @var string
        self.idIn = idIn

        # Ratio IDs to filter by
        # @var string
        self.ratioIdIn = ratioIdIn


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
        'ratioIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaImageTypeFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaImageTypeFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("ratioIdIn", self.ratioIdIn)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getRatioIdIn(self):
        return self.ratioIdIn

    def setRatioIdIn(self, newRatioIdIn):
        self.ratioIdIn = newRatioIdIn


# @package Kaltura
# @subpackage Client
class KalturaTagFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            tagEqual=NotImplemented,
            tagStartsWith=NotImplemented,
            typeEqual=NotImplemented,
            languageEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Tag to filter by
        # @var string
        self.tagEqual = tagEqual

        # Tag to filter by
        # @var string
        self.tagStartsWith = tagStartsWith

        # Type identifier
        # @var int
        self.typeEqual = typeEqual

        # Language to filter by
        # @var string
        self.languageEqual = languageEqual


    PROPERTY_LOADERS = {
        'tagEqual': getXmlNodeText, 
        'tagStartsWith': getXmlNodeText, 
        'typeEqual': getXmlNodeInt, 
        'languageEqual': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaTagFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaTagFilter")
        kparams.addStringIfDefined("tagEqual", self.tagEqual)
        kparams.addStringIfDefined("tagStartsWith", self.tagStartsWith)
        kparams.addIntIfDefined("typeEqual", self.typeEqual)
        kparams.addStringIfDefined("languageEqual", self.languageEqual)
        return kparams

    def getTagEqual(self):
        return self.tagEqual

    def setTagEqual(self, newTagEqual):
        self.tagEqual = newTagEqual

    def getTagStartsWith(self):
        return self.tagStartsWith

    def setTagStartsWith(self, newTagStartsWith):
        self.tagStartsWith = newTagStartsWith

    def getTypeEqual(self):
        return self.typeEqual

    def setTypeEqual(self, newTypeEqual):
        self.typeEqual = newTypeEqual

    def getLanguageEqual(self):
        return self.languageEqual

    def setLanguageEqual(self, newLanguageEqual):
        self.languageEqual = newLanguageEqual


# @package Kaltura
# @subpackage Client
class KalturaAssetStructFilter(KalturaFilter):
    """Filtering Asset Structs"""

    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented,
            metaIdEqual=NotImplemented,
            isProtectedEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated identifiers
        # @var string
        self.idIn = idIn

        # Filter Asset Structs that contain a specific meta id
        # @var int
        self.metaIdEqual = metaIdEqual

        # Filter Asset Structs by isProtectedEqual value
        # @var bool
        self.isProtectedEqual = isProtectedEqual


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
        'metaIdEqual': getXmlNodeInt, 
        'isProtectedEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetStructFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetStructFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("metaIdEqual", self.metaIdEqual)
        kparams.addBoolIfDefined("isProtectedEqual", self.isProtectedEqual)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getMetaIdEqual(self):
        return self.metaIdEqual

    def setMetaIdEqual(self, newMetaIdEqual):
        self.metaIdEqual = newMetaIdEqual

    def getIsProtectedEqual(self):
        return self.isProtectedEqual

    def setIsProtectedEqual(self, newIsProtectedEqual):
        self.isProtectedEqual = newIsProtectedEqual


# @package Kaltura
# @subpackage Client
class KalturaAssetCommentFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            assetIdEqual=NotImplemented,
            assetTypeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Asset Id
        # @var int
        self.assetIdEqual = assetIdEqual

        # Asset Type
        # @var KalturaAssetType
        self.assetTypeEqual = assetTypeEqual


    PROPERTY_LOADERS = {
        'assetIdEqual': getXmlNodeInt, 
        'assetTypeEqual': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetCommentFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetCommentFilter")
        kparams.addIntIfDefined("assetIdEqual", self.assetIdEqual)
        kparams.addStringEnumIfDefined("assetTypeEqual", self.assetTypeEqual)
        return kparams

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaBookmarkFilter(KalturaFilter):
    """Filtering Assets requests"""

    def __init__(self,
            orderBy=NotImplemented,
            assetIdIn=NotImplemented,
            assetTypeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated list of assets identifiers
        # @var string
        self.assetIdIn = assetIdIn

        # Asset type
        # @var KalturaAssetType
        self.assetTypeEqual = assetTypeEqual


    PROPERTY_LOADERS = {
        'assetIdIn': getXmlNodeText, 
        'assetTypeEqual': (KalturaEnumsFactory.createString, "KalturaAssetType"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaBookmarkFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaBookmarkFilter")
        kparams.addStringIfDefined("assetIdIn", self.assetIdIn)
        kparams.addStringEnumIfDefined("assetTypeEqual", self.assetTypeEqual)
        return kparams

    def getAssetIdIn(self):
        return self.assetIdIn

    def setAssetIdIn(self, newAssetIdIn):
        self.assetIdIn = newAssetIdIn

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaAssetHistoryFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            typeIn=NotImplemented,
            assetIdIn=NotImplemented,
            statusEqual=NotImplemented,
            daysLessThanOrEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated list of asset types to search within.
        #             Possible values: 0 - EPG linear programs entries, any media type ID (according to media type IDs defined dynamically in the system).
        #             If omitted - all types should be included.
        # @var string
        self.typeIn = typeIn

        # Comma separated list of asset identifiers.
        # @var string
        self.assetIdIn = assetIdIn

        # Which type of recently watched media to include in the result - those that finished watching, those that are in progress or both.
        #             If omitted or specified filter = all - return all types.
        #             Allowed values: progress - return medias that are in-progress, done - return medias that finished watching.
        # @var KalturaWatchStatus
        self.statusEqual = statusEqual

        # How many days back to return the watched media. If omitted, default to 7 days
        # @var int
        self.daysLessThanOrEqual = daysLessThanOrEqual


    PROPERTY_LOADERS = {
        'typeIn': getXmlNodeText, 
        'assetIdIn': getXmlNodeText, 
        'statusEqual': (KalturaEnumsFactory.createString, "KalturaWatchStatus"), 
        'daysLessThanOrEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetHistoryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetHistoryFilter")
        kparams.addStringIfDefined("typeIn", self.typeIn)
        kparams.addStringIfDefined("assetIdIn", self.assetIdIn)
        kparams.addStringEnumIfDefined("statusEqual", self.statusEqual)
        kparams.addIntIfDefined("daysLessThanOrEqual", self.daysLessThanOrEqual)
        return kparams

    def getTypeIn(self):
        return self.typeIn

    def setTypeIn(self, newTypeIn):
        self.typeIn = newTypeIn

    def getAssetIdIn(self):
        return self.assetIdIn

    def setAssetIdIn(self, newAssetIdIn):
        self.assetIdIn = newAssetIdIn

    def getStatusEqual(self):
        return self.statusEqual

    def setStatusEqual(self, newStatusEqual):
        self.statusEqual = newStatusEqual

    def getDaysLessThanOrEqual(self):
        return self.daysLessThanOrEqual

    def setDaysLessThanOrEqual(self, newDaysLessThanOrEqual):
        self.daysLessThanOrEqual = newDaysLessThanOrEqual


# @package Kaltura
# @subpackage Client
class KalturaAssetRuleFilter(KalturaFilter):
    """Asset rule filter"""

    def __init__(self,
            orderBy=NotImplemented,
            conditionsContainType=NotImplemented,
            assetApplied=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Indicates which asset rule list to return by it KalturaRuleConditionType.
        #             Default value: KalturaRuleConditionType.COUNTRY
        # @var KalturaRuleConditionType
        self.conditionsContainType = conditionsContainType

        # Indicates if to return an asset rule list that related to specific asset
        # @var KalturaSlimAsset
        self.assetApplied = assetApplied


    PROPERTY_LOADERS = {
        'conditionsContainType': (KalturaEnumsFactory.createString, "KalturaRuleConditionType"), 
        'assetApplied': (KalturaObjectFactory.create, 'KalturaSlimAsset'), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetRuleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetRuleFilter")
        kparams.addStringEnumIfDefined("conditionsContainType", self.conditionsContainType)
        kparams.addObjectIfDefined("assetApplied", self.assetApplied)
        return kparams

    def getConditionsContainType(self):
        return self.conditionsContainType

    def setConditionsContainType(self, newConditionsContainType):
        self.conditionsContainType = newConditionsContainType

    def getAssetApplied(self):
        return self.assetApplied

    def setAssetApplied(self, newAssetApplied):
        self.assetApplied = newAssetApplied


# @package Kaltura
# @subpackage Client
class KalturaAssetUserRuleFilter(KalturaFilter):
    """Asset user rule filter"""

    def __init__(self,
            orderBy=NotImplemented,
            attachedUserIdEqualCurrent=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Indicates if to get the asset user rule list for the attached user or for the entire group
        # @var bool
        self.attachedUserIdEqualCurrent = attachedUserIdEqualCurrent


    PROPERTY_LOADERS = {
        'attachedUserIdEqualCurrent': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaAssetUserRuleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaAssetUserRuleFilter")
        kparams.addBoolIfDefined("attachedUserIdEqualCurrent", self.attachedUserIdEqualCurrent)
        return kparams

    def getAttachedUserIdEqualCurrent(self):
        return self.attachedUserIdEqualCurrent

    def setAttachedUserIdEqualCurrent(self, newAttachedUserIdEqualCurrent):
        self.attachedUserIdEqualCurrent = newAttachedUserIdEqualCurrent


# @package Kaltura
# @subpackage Client
class KalturaCurrencyFilter(KalturaFilter):
    """Currency filter"""

    def __init__(self,
            orderBy=NotImplemented,
            codeIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Currency codes
        # @var string
        self.codeIn = codeIn


    PROPERTY_LOADERS = {
        'codeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCurrencyFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaCurrencyFilter")
        kparams.addStringIfDefined("codeIn", self.codeIn)
        return kparams

    def getCodeIn(self):
        return self.codeIn

    def setCodeIn(self, newCodeIn):
        self.codeIn = newCodeIn


# @package Kaltura
# @subpackage Client
class KalturaLanguageFilter(KalturaFilter):
    """Language filter"""

    def __init__(self,
            orderBy=NotImplemented,
            codeIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Language codes
        # @var string
        self.codeIn = codeIn


    PROPERTY_LOADERS = {
        'codeIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaLanguageFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaLanguageFilter")
        kparams.addStringIfDefined("codeIn", self.codeIn)
        return kparams

    def getCodeIn(self):
        return self.codeIn

    def setCodeIn(self, newCodeIn):
        self.codeIn = newCodeIn


# @package Kaltura
# @subpackage Client
class KalturaMetaFilter(KalturaFilter):
    """Meta filter"""

    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented,
            assetStructIdEqual=NotImplemented,
            dataTypeEqual=NotImplemented,
            multipleValueEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated identifiers
        # @var string
        self.idIn = idIn

        # Filter Metas that are contained in a specific asset struct
        # @var int
        self.assetStructIdEqual = assetStructIdEqual

        # Meta data type to filter by
        # @var KalturaMetaDataType
        self.dataTypeEqual = dataTypeEqual

        # Filter metas by multipleValueEqual value
        # @var bool
        self.multipleValueEqual = multipleValueEqual


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
        'assetStructIdEqual': getXmlNodeInt, 
        'dataTypeEqual': (KalturaEnumsFactory.createString, "KalturaMetaDataType"), 
        'multipleValueEqual': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaMetaFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaMetaFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addIntIfDefined("assetStructIdEqual", self.assetStructIdEqual)
        kparams.addStringEnumIfDefined("dataTypeEqual", self.dataTypeEqual)
        kparams.addBoolIfDefined("multipleValueEqual", self.multipleValueEqual)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getAssetStructIdEqual(self):
        return self.assetStructIdEqual

    def setAssetStructIdEqual(self, newAssetStructIdEqual):
        self.assetStructIdEqual = newAssetStructIdEqual

    def getDataTypeEqual(self):
        return self.dataTypeEqual

    def setDataTypeEqual(self, newDataTypeEqual):
        self.dataTypeEqual = newDataTypeEqual

    def getMultipleValueEqual(self):
        return self.multipleValueEqual

    def setMultipleValueEqual(self, newMultipleValueEqual):
        self.multipleValueEqual = newMultipleValueEqual


# @package Kaltura
# @subpackage Client
class KalturaCountryFilter(KalturaFilter):
    """Country filter"""

    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented,
            ipEqual=NotImplemented,
            ipEqualCurrent=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Country identifiers
        # @var string
        self.idIn = idIn

        # Ip to identify the country
        # @var string
        self.ipEqual = ipEqual

        # Indicates if to get the IP from the request
        # @var bool
        self.ipEqualCurrent = ipEqualCurrent


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
        'ipEqual': getXmlNodeText, 
        'ipEqualCurrent': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaCountryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaCountryFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addStringIfDefined("ipEqual", self.ipEqual)
        kparams.addBoolIfDefined("ipEqualCurrent", self.ipEqualCurrent)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getIpEqual(self):
        return self.ipEqual

    def setIpEqual(self, newIpEqual):
        self.ipEqual = newIpEqual

    def getIpEqualCurrent(self):
        return self.ipEqualCurrent

    def setIpEqualCurrent(self, newIpEqualCurrent):
        self.ipEqualCurrent = newIpEqualCurrent


# @package Kaltura
# @subpackage Client
class KalturaSearchHistoryFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)


    PROPERTY_LOADERS = {
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaSearchHistoryFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaSearchHistoryFilter")
        return kparams


# @package Kaltura
# @subpackage Client
class KalturaRegionFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            externalIdIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # List of comma separated regions external identifiers
        # @var string
        self.externalIdIn = externalIdIn


    PROPERTY_LOADERS = {
        'externalIdIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaRegionFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaRegionFilter")
        kparams.addStringIfDefined("externalIdIn", self.externalIdIn)
        return kparams

    def getExternalIdIn(self):
        return self.externalIdIn

    def setExternalIdIn(self, newExternalIdIn):
        self.externalIdIn = newExternalIdIn


# @package Kaltura
# @subpackage Client
class KalturaUserAssetRuleFilter(KalturaFilter):
    """User asset rule filter"""

    def __init__(self,
            orderBy=NotImplemented,
            assetIdEqual=NotImplemented,
            assetTypeEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Asset identifier to filter by
        # @var int
        self.assetIdEqual = assetIdEqual

        # Asset type to filter by - 0 = EPG, 1 = media
        # @var int
        self.assetTypeEqual = assetTypeEqual


    PROPERTY_LOADERS = {
        'assetIdEqual': getXmlNodeInt, 
        'assetTypeEqual': getXmlNodeInt, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserAssetRuleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserAssetRuleFilter")
        kparams.addIntIfDefined("assetIdEqual", self.assetIdEqual)
        kparams.addIntIfDefined("assetTypeEqual", self.assetTypeEqual)
        return kparams

    def getAssetIdEqual(self):
        return self.assetIdEqual

    def setAssetIdEqual(self, newAssetIdEqual):
        self.assetIdEqual = newAssetIdEqual

    def getAssetTypeEqual(self):
        return self.assetTypeEqual

    def setAssetTypeEqual(self, newAssetTypeEqual):
        self.assetTypeEqual = newAssetTypeEqual


# @package Kaltura
# @subpackage Client
class KalturaParentalRuleFilter(KalturaFilter):
    def __init__(self,
            orderBy=NotImplemented,
            entityReferenceEqual=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Reference type to filter by
        # @var KalturaEntityReferenceBy
        self.entityReferenceEqual = entityReferenceEqual


    PROPERTY_LOADERS = {
        'entityReferenceEqual': (KalturaEnumsFactory.createString, "KalturaEntityReferenceBy"), 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaParentalRuleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaParentalRuleFilter")
        kparams.addStringEnumIfDefined("entityReferenceEqual", self.entityReferenceEqual)
        return kparams

    def getEntityReferenceEqual(self):
        return self.entityReferenceEqual

    def setEntityReferenceEqual(self, newEntityReferenceEqual):
        self.entityReferenceEqual = newEntityReferenceEqual


# @package Kaltura
# @subpackage Client
class KalturaExportTaskFilter(KalturaFilter):
    """Bulk export tasks filter"""

    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated tasks identifiers
        # @var string
        self.idIn = idIn


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaExportTaskFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaExportTaskFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn


# @package Kaltura
# @subpackage Client
class KalturaUserRoleFilter(KalturaFilter):
    """User roles filter"""

    def __init__(self,
            orderBy=NotImplemented,
            idIn=NotImplemented,
            currentUserRoleIdsContains=NotImplemented):
        KalturaFilter.__init__(self,
            orderBy)

        # Comma separated roles identifiers
        # @var string
        self.idIn = idIn

        # Indicates whether the results should be filtered by userId using the current
        # @var bool
        self.currentUserRoleIdsContains = currentUserRoleIdsContains


    PROPERTY_LOADERS = {
        'idIn': getXmlNodeText, 
        'currentUserRoleIdsContains': getXmlNodeBool, 
    }

    def fromXml(self, node):
        KalturaFilter.fromXml(self, node)
        self.fromXmlImpl(node, KalturaUserRoleFilter.PROPERTY_LOADERS)

    def toParams(self):
        kparams = KalturaFilter.toParams(self)
        kparams.put("objectType", "KalturaUserRoleFilter")
        kparams.addStringIfDefined("idIn", self.idIn)
        kparams.addBoolIfDefined("currentUserRoleIdsContains", self.currentUserRoleIdsContains)
        return kparams

    def getIdIn(self):
        return self.idIn

    def setIdIn(self, newIdIn):
        self.idIn = newIdIn

    def getCurrentUserRoleIdsContains(self):
        return self.currentUserRoleIdsContains

    def setCurrentUserRoleIdsContains(self, newCurrentUserRoleIdsContains):
        self.currentUserRoleIdsContains = newCurrentUserRoleIdsContains


########## services ##########
########## main ##########
class KalturaCoreClient(KalturaClientPlugin):
    # KalturaCoreClient
    instance = None

    # @return KalturaCoreClient
    @staticmethod
    def get():
        if KalturaCoreClient.instance == None:
            KalturaCoreClient.instance = KalturaCoreClient()
        return KalturaCoreClient.instance

    # @return array<KalturaServiceBase>
    def getServices(self):
        return {
        }

    def getEnums(self):
        return {
            'KalturaAggregationCountOrderBy': KalturaAggregationCountOrderBy,
            'KalturaAnnouncementOrderBy': KalturaAnnouncementOrderBy,
            'KalturaAnnouncementRecipientsType': KalturaAnnouncementRecipientsType,
            'KalturaAnnouncementStatus': KalturaAnnouncementStatus,
            'KalturaAssetCommentOrderBy': KalturaAssetCommentOrderBy,
            'KalturaAssetHistoryOrderBy': KalturaAssetHistoryOrderBy,
            'KalturaAssetOrderBy': KalturaAssetOrderBy,
            'KalturaAssetReminderOrderBy': KalturaAssetReminderOrderBy,
            'KalturaAssetRuleOrderBy': KalturaAssetRuleOrderBy,
            'KalturaAssetStructMetaOrderBy': KalturaAssetStructMetaOrderBy,
            'KalturaAssetStructOrderBy': KalturaAssetStructOrderBy,
            'KalturaAssetType': KalturaAssetType,
            'KalturaAssetUserRuleOrderBy': KalturaAssetUserRuleOrderBy,
            'KalturaBatchJobStatus': KalturaBatchJobStatus,
            'KalturaBillingAction': KalturaBillingAction,
            'KalturaBillingItemsType': KalturaBillingItemsType,
            'KalturaBillingPriceType': KalturaBillingPriceType,
            'KalturaBookmarkActionType': KalturaBookmarkActionType,
            'KalturaBookmarkOrderBy': KalturaBookmarkOrderBy,
            'KalturaBulkOrderBy': KalturaBulkOrderBy,
            'KalturaBundleType': KalturaBundleType,
            'KalturaChannelEnrichment': KalturaChannelEnrichment,
            'KalturaChannelOrderBy': KalturaChannelOrderBy,
            'KalturaChannelsOrderBy': KalturaChannelsOrderBy,
            'KalturaCollectionOrderBy': KalturaCollectionOrderBy,
            'KalturaConcurrencyLimitationType': KalturaConcurrencyLimitationType,
            'KalturaConfigurationGroupDeviceOrderBy': KalturaConfigurationGroupDeviceOrderBy,
            'KalturaConfigurationGroupTagOrderBy': KalturaConfigurationGroupTagOrderBy,
            'KalturaConfigurationsOrderBy': KalturaConfigurationsOrderBy,
            'KalturaCountryOrderBy': KalturaCountryOrderBy,
            'KalturaCouponGroupType': KalturaCouponGroupType,
            'KalturaCurrencyOrderBy': KalturaCurrencyOrderBy,
            'KalturaDeviceStatus': KalturaDeviceStatus,
            'KalturaDrmSchemeName': KalturaDrmSchemeName,
            'KalturaEngagementOrderBy': KalturaEngagementOrderBy,
            'KalturaEngagementType': KalturaEngagementType,
            'KalturaEntitlementOrderBy': KalturaEntitlementOrderBy,
            'KalturaEntityReferenceBy': KalturaEntityReferenceBy,
            'KalturaEvictionPolicyType': KalturaEvictionPolicyType,
            'KalturaExportDataType': KalturaExportDataType,
            'KalturaExportTaskOrderBy': KalturaExportTaskOrderBy,
            'KalturaExportType': KalturaExportType,
            'KalturaFavoriteOrderBy': KalturaFavoriteOrderBy,
            'KalturaFollowTvSeriesOrderBy': KalturaFollowTvSeriesOrderBy,
            'KalturaGroupByField': KalturaGroupByField,
            'KalturaHouseholdDeviceOrderBy': KalturaHouseholdDeviceOrderBy,
            'KalturaHouseholdPaymentGatewaySelectedBy': KalturaHouseholdPaymentGatewaySelectedBy,
            'KalturaHouseholdSuspensionState': KalturaHouseholdSuspensionState,
            'KalturaHouseholdUserOrderBy': KalturaHouseholdUserOrderBy,
            'KalturaHouseholdUserStatus': KalturaHouseholdUserStatus,
            'KalturaImageObjectType': KalturaImageObjectType,
            'KalturaImageOrderBy': KalturaImageOrderBy,
            'KalturaImageStatus': KalturaImageStatus,
            'KalturaImageTypeOrderBy': KalturaImageTypeOrderBy,
            'KalturaInboxMessageOrderBy': KalturaInboxMessageOrderBy,
            'KalturaInboxMessageStatus': KalturaInboxMessageStatus,
            'KalturaInboxMessageType': KalturaInboxMessageType,
            'KalturaLanguageOrderBy': KalturaLanguageOrderBy,
            'KalturaLinearChannelType': KalturaLinearChannelType,
            'KalturaMediaFileOrderBy': KalturaMediaFileOrderBy,
            'KalturaMediaFileStreamerType': KalturaMediaFileStreamerType,
            'KalturaMediaFileTypeQuality': KalturaMediaFileTypeQuality,
            'KalturaMetaDataType': KalturaMetaDataType,
            'KalturaMetaOrderBy': KalturaMetaOrderBy,
            'KalturaMetaTagOrderBy': KalturaMetaTagOrderBy,
            'KalturaOTTUserOrderBy': KalturaOTTUserOrderBy,
            'KalturaParentalRuleOrderBy': KalturaParentalRuleOrderBy,
            'KalturaParentalRuleType': KalturaParentalRuleType,
            'KalturaPartnerConfigurationOrderBy': KalturaPartnerConfigurationOrderBy,
            'KalturaPartnerConfigurationType': KalturaPartnerConfigurationType,
            'KalturaPaymentMethodProfileOrderBy': KalturaPaymentMethodProfileOrderBy,
            'KalturaPaymentMethodType': KalturaPaymentMethodType,
            'KalturaPersonalFeedOrderBy': KalturaPersonalFeedOrderBy,
            'KalturaPersonalListOrderBy': KalturaPersonalListOrderBy,
            'KalturaPlatform': KalturaPlatform,
            'KalturaPositionOwner': KalturaPositionOwner,
            'KalturaPriceDetailsOrderBy': KalturaPriceDetailsOrderBy,
            'KalturaPricePlanOrderBy': KalturaPricePlanOrderBy,
            'KalturaProductPriceOrderBy': KalturaProductPriceOrderBy,
            'KalturaPurchaseStatus': KalturaPurchaseStatus,
            'KalturaRecordingContextOrderBy': KalturaRecordingContextOrderBy,
            'KalturaRecordingOrderBy': KalturaRecordingOrderBy,
            'KalturaRecordingStatus': KalturaRecordingStatus,
            'KalturaRecordingType': KalturaRecordingType,
            'KalturaRegionOrderBy': KalturaRegionOrderBy,
            'KalturaReminderType': KalturaReminderType,
            'KalturaReportOrderBy': KalturaReportOrderBy,
            'KalturaRuleActionType': KalturaRuleActionType,
            'KalturaRuleConditionType': KalturaRuleConditionType,
            'KalturaRuleLevel': KalturaRuleLevel,
            'KalturaRuleType': KalturaRuleType,
            'KalturaScheduledRecordingAssetType': KalturaScheduledRecordingAssetType,
            'KalturaSearchHistoryOrderBy': KalturaSearchHistoryOrderBy,
            'KalturaSeriesRecordingOrderBy': KalturaSeriesRecordingOrderBy,
            'KalturaSeriesReminderOrderBy': KalturaSeriesReminderOrderBy,
            'KalturaSocialActionOrderBy': KalturaSocialActionOrderBy,
            'KalturaSocialActionType': KalturaSocialActionType,
            'KalturaSocialCommentOrderBy': KalturaSocialCommentOrderBy,
            'KalturaSocialFriendActivityOrderBy': KalturaSocialFriendActivityOrderBy,
            'KalturaSocialPlatform': KalturaSocialPlatform,
            'KalturaSubscriptionDependencyType': KalturaSubscriptionDependencyType,
            'KalturaSubscriptionOrderBy': KalturaSubscriptionOrderBy,
            'KalturaSubscriptionSetOrderBy': KalturaSubscriptionSetOrderBy,
            'KalturaSubscriptionSetType': KalturaSubscriptionSetType,
            'KalturaTagOrderBy': KalturaTagOrderBy,
            'KalturaTimeShiftedTvState': KalturaTimeShiftedTvState,
            'KalturaTopicAutomaticIssueNotification': KalturaTopicAutomaticIssueNotification,
            'KalturaTopicOrderBy': KalturaTopicOrderBy,
            'KalturaTransactionHistoryOrderBy': KalturaTransactionHistoryOrderBy,
            'KalturaTransactionType': KalturaTransactionType,
            'KalturaUserAssetRuleOrderBy': KalturaUserAssetRuleOrderBy,
            'KalturaUserRoleOrderBy': KalturaUserRoleOrderBy,
            'KalturaUserState': KalturaUserState,
            'KalturaWatchStatus': KalturaWatchStatus,
        }

    def getTypes(self):
        return {
            'KalturaListResponse': KalturaListResponse,
            'KalturaApiExceptionArg': KalturaApiExceptionArg,
            'KalturaSocialComment': KalturaSocialComment,
            'KalturaSocialCommentListResponse': KalturaSocialCommentListResponse,
            'KalturaSocialNetworkComment': KalturaSocialNetworkComment,
            'KalturaTwitterTwit': KalturaTwitterTwit,
            'KalturaFacebookPost': KalturaFacebookPost,
            'KalturaAssetComment': KalturaAssetComment,
            'KalturaSocialAction': KalturaSocialAction,
            'KalturaSocialFriendActivity': KalturaSocialFriendActivity,
            'KalturaSocialFriendActivityListResponse': KalturaSocialFriendActivityListResponse,
            'KalturaSocialActionRate': KalturaSocialActionRate,
            'KalturaSocialActionListResponse': KalturaSocialActionListResponse,
            'KalturaHouseholdPaymentMethod': KalturaHouseholdPaymentMethod,
            'KalturaHouseholdPaymentMethodListResponse': KalturaHouseholdPaymentMethodListResponse,
            'KalturaPaymentMethodProfile': KalturaPaymentMethodProfile,
            'KalturaPaymentMethodProfileListResponse': KalturaPaymentMethodProfileListResponse,
            'KalturaHouseholdPaymentGateway': KalturaHouseholdPaymentGateway,
            'KalturaHouseholdPaymentGatewayListResponse': KalturaHouseholdPaymentGatewayListResponse,
            'KalturaPaymentGatewayBaseProfile': KalturaPaymentGatewayBaseProfile,
            'KalturaValue': KalturaValue,
            'KalturaStringValue': KalturaStringValue,
            'KalturaPaymentGatewayProfile': KalturaPaymentGatewayProfile,
            'KalturaPaymentGatewayProfileListResponse': KalturaPaymentGatewayProfileListResponse,
            'KalturaTranslationToken': KalturaTranslationToken,
            'KalturaMultilingualStringValue': KalturaMultilingualStringValue,
            'KalturaLongValue': KalturaLongValue,
            'KalturaDoubleValue': KalturaDoubleValue,
            'KalturaBooleanValue': KalturaBooleanValue,
            'KalturaIntegerValue': KalturaIntegerValue,
            'KalturaPluginData': KalturaPluginData,
            'KalturaDrmPlaybackPluginData': KalturaDrmPlaybackPluginData,
            'KalturaCustomDrmPlaybackPluginData': KalturaCustomDrmPlaybackPluginData,
            'KalturaHouseholdDevice': KalturaHouseholdDevice,
            'KalturaHouseholdDeviceListResponse': KalturaHouseholdDeviceListResponse,
            'KalturaFairPlayPlaybackPluginData': KalturaFairPlayPlaybackPluginData,
            'KalturaHouseholdUser': KalturaHouseholdUser,
            'KalturaHouseholdUserListResponse': KalturaHouseholdUserListResponse,
            'KalturaHomeNetwork': KalturaHomeNetwork,
            'KalturaHomeNetworkListResponse': KalturaHomeNetworkListResponse,
            'KalturaConfigurations': KalturaConfigurations,
            'KalturaConfigurationsListResponse': KalturaConfigurationsListResponse,
            'KalturaConfigurationGroupDevice': KalturaConfigurationGroupDevice,
            'KalturaConfigurationGroupDeviceListResponse': KalturaConfigurationGroupDeviceListResponse,
            'KalturaConfigurationGroupTag': KalturaConfigurationGroupTag,
            'KalturaConfigurationGroupTagListResponse': KalturaConfigurationGroupTagListResponse,
            'KalturaConfigurationIdentifier': KalturaConfigurationIdentifier,
            'KalturaConfigurationGroup': KalturaConfigurationGroup,
            'KalturaConfigurationGroupListResponse': KalturaConfigurationGroupListResponse,
            'KalturaSSOAdapterProfile': KalturaSSOAdapterProfile,
            'KalturaSSOAdapterProfileListResponse': KalturaSSOAdapterProfileListResponse,
            'KalturaUserInterestTopic': KalturaUserInterestTopic,
            'KalturaUserInterest': KalturaUserInterest,
            'KalturaUserInterestListResponse': KalturaUserInterestListResponse,
            'KalturaMediaImage': KalturaMediaImage,
            'KalturaAssetFile': KalturaAssetFile,
            'KalturaMediaFile': KalturaMediaFile,
            'KalturaBuzzScore': KalturaBuzzScore,
            'KalturaAssetStatistics': KalturaAssetStatistics,
            'KalturaMultilingualStringValueArray': KalturaMultilingualStringValueArray,
            'KalturaFavorite': KalturaFavorite,
            'KalturaFavoriteListResponse': KalturaFavoriteListResponse,
            'KalturaPlaybackSource': KalturaPlaybackSource,
            'KalturaBaseOTTUser': KalturaBaseOTTUser,
            'KalturaCountry': KalturaCountry,
            'KalturaOTTUserType': KalturaOTTUserType,
            'KalturaOTTUser': KalturaOTTUser,
            'KalturaOTTUserListResponse': KalturaOTTUserListResponse,
            'KalturaBaseChannel': KalturaBaseChannel,
            'KalturaDiscountModule': KalturaDiscountModule,
            'KalturaUsageModule': KalturaUsageModule,
            'KalturaCouponsGroup': KalturaCouponsGroup,
            'KalturaProductCode': KalturaProductCode,
            'KalturaCollection': KalturaCollection,
            'KalturaCollectionListResponse': KalturaCollectionListResponse,
            'KalturaAssetGroupBy': KalturaAssetGroupBy,
            'KalturaDynamicOrderBy': KalturaDynamicOrderBy,
            'KalturaChannelOrder': KalturaChannelOrder,
            'KalturaChannel': KalturaChannel,
            'KalturaDynamicChannel': KalturaDynamicChannel,
            'KalturaManualChannel': KalturaManualChannel,
            'KalturaAssetMetaOrTagGroupBy': KalturaAssetMetaOrTagGroupBy,
            'KalturaAssetFieldGroupBy': KalturaAssetFieldGroupBy,
            'KalturaPricePlan': KalturaPricePlan,
            'KalturaPrice': KalturaPrice,
            'KalturaDiscount': KalturaDiscount,
            'KalturaDiscountDetails': KalturaDiscountDetails,
            'KalturaDiscountDetailsListResponse': KalturaDiscountDetailsListResponse,
            'KalturaSubscriptionSet': KalturaSubscriptionSet,
            'KalturaSubscriptionSetListResponse': KalturaSubscriptionSetListResponse,
            'KalturaSubscriptionDependencySet': KalturaSubscriptionDependencySet,
            'KalturaSubscriptionSwitchSet': KalturaSubscriptionSwitchSet,
            'KalturaProductPrice': KalturaProductPrice,
            'KalturaProductPriceListResponse': KalturaProductPriceListResponse,
            'KalturaCollectionPrice': KalturaCollectionPrice,
            'KalturaPpvPrice': KalturaPpvPrice,
            'KalturaSubscriptionPrice': KalturaSubscriptionPrice,
            'KalturaCouponsGroupListResponse': KalturaCouponsGroupListResponse,
            'KalturaPriceDetails': KalturaPriceDetails,
            'KalturaPriceDetailsListResponse': KalturaPriceDetailsListResponse,
            'KalturaPricePlanListResponse': KalturaPricePlanListResponse,
            'KalturaPreviewModule': KalturaPreviewModule,
            'KalturaPremiumService': KalturaPremiumService,
            'KalturaSubscription': KalturaSubscription,
            'KalturaSubscriptionListResponse': KalturaSubscriptionListResponse,
            'KalturaNpvrPremiumService': KalturaNpvrPremiumService,
            'KalturaHouseholdPremiumService': KalturaHouseholdPremiumService,
            'KalturaProductsPriceListResponse': KalturaProductsPriceListResponse,
            'KalturaPersonalList': KalturaPersonalList,
            'KalturaPersonalListListResponse': KalturaPersonalListListResponse,
            'KalturaEngagement': KalturaEngagement,
            'KalturaEngagementListResponse': KalturaEngagementListResponse,
            'KalturaEngagementAdapterBase': KalturaEngagementAdapterBase,
            'KalturaEngagementAdapter': KalturaEngagementAdapter,
            'KalturaEngagementAdapterListResponse': KalturaEngagementAdapterListResponse,
            'KalturaReminder': KalturaReminder,
            'KalturaReminderListResponse': KalturaReminderListResponse,
            'KalturaSeriesReminder': KalturaSeriesReminder,
            'KalturaAssetReminder': KalturaAssetReminder,
            'KalturaInboxMessage': KalturaInboxMessage,
            'KalturaInboxMessageListResponse': KalturaInboxMessageListResponse,
            'KalturaFollowDataBase': KalturaFollowDataBase,
            'KalturaFollowTvSeries': KalturaFollowTvSeries,
            'KalturaFollowTvSeriesListResponse': KalturaFollowTvSeriesListResponse,
            'KalturaAnnouncement': KalturaAnnouncement,
            'KalturaAnnouncementListResponse': KalturaAnnouncementListResponse,
            'KalturaFeed': KalturaFeed,
            'KalturaPersonalFeed': KalturaPersonalFeed,
            'KalturaPersonalFeedListResponse': KalturaPersonalFeedListResponse,
            'KalturaTopic': KalturaTopic,
            'KalturaTopicListResponse': KalturaTopicListResponse,
            'KalturaSeriesRecording': KalturaSeriesRecording,
            'KalturaSeriesRecordingListResponse': KalturaSeriesRecordingListResponse,
            'KalturaHouseholdPremiumServiceListResponse': KalturaHouseholdPremiumServiceListResponse,
            'KalturaCDVRAdapterProfile': KalturaCDVRAdapterProfile,
            'KalturaCDVRAdapterProfileListResponse': KalturaCDVRAdapterProfileListResponse,
            'KalturaRecording': KalturaRecording,
            'KalturaRecordingListResponse': KalturaRecordingListResponse,
            'KalturaBillingTransaction': KalturaBillingTransaction,
            'KalturaBillingTransactionListResponse': KalturaBillingTransactionListResponse,
            'KalturaEntitlement': KalturaEntitlement,
            'KalturaEntitlementListResponse': KalturaEntitlementListResponse,
            'KalturaCollectionEntitlement': KalturaCollectionEntitlement,
            'KalturaPpvEntitlement': KalturaPpvEntitlement,
            'KalturaSubscriptionEntitlement': KalturaSubscriptionEntitlement,
            'KalturaPartnerConfiguration': KalturaPartnerConfiguration,
            'KalturaPartnerConfigurationListResponse': KalturaPartnerConfigurationListResponse,
            'KalturaConcurrencyPartnerConfig': KalturaConcurrencyPartnerConfig,
            'KalturaBillingPartnerConfig': KalturaBillingPartnerConfig,
            'KalturaT': KalturaT,
            'KalturaGenericListResponse': KalturaGenericListResponse,
            'KalturaIntegerValueListResponse': KalturaIntegerValueListResponse,
            'KalturaReport': KalturaReport,
            'KalturaReportListResponse': KalturaReportListResponse,
            'KalturaPushParams': KalturaPushParams,
            'KalturaDeviceReport': KalturaDeviceReport,
            'KalturaAssetStructMeta': KalturaAssetStructMeta,
            'KalturaAssetStructMetaListResponse': KalturaAssetStructMetaListResponse,
            'KalturaMediaFileType': KalturaMediaFileType,
            'KalturaMediaFileTypeListResponse': KalturaMediaFileTypeListResponse,
            'KalturaChannelListResponse': KalturaChannelListResponse,
            'KalturaImage': KalturaImage,
            'KalturaImageListResponse': KalturaImageListResponse,
            'KalturaRatio': KalturaRatio,
            'KalturaRatioListResponse': KalturaRatioListResponse,
            'KalturaTag': KalturaTag,
            'KalturaTagListResponse': KalturaTagListResponse,
            'KalturaAsset': KalturaAsset,
            'KalturaAssetListResponse': KalturaAssetListResponse,
            'KalturaMediaAsset': KalturaMediaAsset,
            'KalturaLinearMediaAsset': KalturaLinearMediaAsset,
            'KalturaProgramAsset': KalturaProgramAsset,
            'KalturaRecordingAsset': KalturaRecordingAsset,
            'KalturaAssetStruct': KalturaAssetStruct,
            'KalturaAssetStructListResponse': KalturaAssetStructListResponse,
            'KalturaImageType': KalturaImageType,
            'KalturaImageTypeListResponse': KalturaImageTypeListResponse,
            'KalturaAssetCount': KalturaAssetCount,
            'KalturaAssetsCount': KalturaAssetsCount,
            'KalturaAssetCountListResponse': KalturaAssetCountListResponse,
            'KalturaSlimAsset': KalturaSlimAsset,
            'KalturaBookmarkPlayerData': KalturaBookmarkPlayerData,
            'KalturaBookmark': KalturaBookmark,
            'KalturaBookmarkListResponse': KalturaBookmarkListResponse,
            'KalturaAssetCommentListResponse': KalturaAssetCommentListResponse,
            'KalturaAssetStatisticsListResponse': KalturaAssetStatisticsListResponse,
            'KalturaMediaFileListResponse': KalturaMediaFileListResponse,
            'KalturaAssetHistory': KalturaAssetHistory,
            'KalturaAssetHistoryListResponse': KalturaAssetHistoryListResponse,
            'KalturaBulk': KalturaBulk,
            'KalturaBulkListResponse': KalturaBulkListResponse,
            'KalturaDrmProfile': KalturaDrmProfile,
            'KalturaDrmProfileListResponse': KalturaDrmProfileListResponse,
            'KalturaMediaConcurrencyRule': KalturaMediaConcurrencyRule,
            'KalturaMediaConcurrencyRuleListResponse': KalturaMediaConcurrencyRuleListResponse,
            'KalturaAssetRuleBase': KalturaAssetRuleBase,
            'KalturaCondition': KalturaCondition,
            'KalturaAssetCondition': KalturaAssetCondition,
            'KalturaRuleAction': KalturaRuleAction,
            'KalturaAssetUserRuleAction': KalturaAssetUserRuleAction,
            'KalturaAssetUserRule': KalturaAssetUserRule,
            'KalturaAssetUserRuleListResponse': KalturaAssetUserRuleListResponse,
            'KalturaAssetRuleAction': KalturaAssetRuleAction,
            'KalturaAssetRule': KalturaAssetRule,
            'KalturaCountryCondition': KalturaCountryCondition,
            'KalturaConcurrencyCondition': KalturaConcurrencyCondition,
            'KalturaAssetUserRuleBlockAction': KalturaAssetUserRuleBlockAction,
            'KalturaAccessControlBlockAction': KalturaAccessControlBlockAction,
            'KalturaTimeOffsetRuleAction': KalturaTimeOffsetRuleAction,
            'KalturaEndDateOffsetRuleAction': KalturaEndDateOffsetRuleAction,
            'KalturaStartDateOffsetRuleAction': KalturaStartDateOffsetRuleAction,
            'KalturaCurrency': KalturaCurrency,
            'KalturaCurrencyListResponse': KalturaCurrencyListResponse,
            'KalturaAssetRuleListResponse': KalturaAssetRuleListResponse,
            'KalturaLanguage': KalturaLanguage,
            'KalturaLanguageListResponse': KalturaLanguageListResponse,
            'KalturaMeta': KalturaMeta,
            'KalturaMetaListResponse': KalturaMetaListResponse,
            'KalturaDeviceBrand': KalturaDeviceBrand,
            'KalturaDeviceBrandListResponse': KalturaDeviceBrandListResponse,
            'KalturaCountryListResponse': KalturaCountryListResponse,
            'KalturaOSSAdapterBaseProfile': KalturaOSSAdapterBaseProfile,
            'KalturaOSSAdapterProfile': KalturaOSSAdapterProfile,
            'KalturaOSSAdapterProfileListResponse': KalturaOSSAdapterProfileListResponse,
            'KalturaSearchHistory': KalturaSearchHistory,
            'KalturaSearchHistoryListResponse': KalturaSearchHistoryListResponse,
            'KalturaDeviceFamilyBase': KalturaDeviceFamilyBase,
            'KalturaDeviceFamily': KalturaDeviceFamily,
            'KalturaDeviceFamilyListResponse': KalturaDeviceFamilyListResponse,
            'KalturaHouseholdDeviceFamilyLimitations': KalturaHouseholdDeviceFamilyLimitations,
            'KalturaRegionalChannel': KalturaRegionalChannel,
            'KalturaRegion': KalturaRegion,
            'KalturaRegionListResponse': KalturaRegionListResponse,
            'KalturaUserAssetRule': KalturaUserAssetRule,
            'KalturaUserAssetRuleListResponse': KalturaUserAssetRuleListResponse,
            'KalturaCDNAdapterProfile': KalturaCDNAdapterProfile,
            'KalturaCDNAdapterProfileListResponse': KalturaCDNAdapterProfileListResponse,
            'KalturaExportTask': KalturaExportTask,
            'KalturaExportTaskListResponse': KalturaExportTaskListResponse,
            'KalturaChannelEnrichmentHolder': KalturaChannelEnrichmentHolder,
            'KalturaExternalChannelProfile': KalturaExternalChannelProfile,
            'KalturaExternalChannelProfileListResponse': KalturaExternalChannelProfileListResponse,
            'KalturaRecommendationProfile': KalturaRecommendationProfile,
            'KalturaRecommendationProfileListResponse': KalturaRecommendationProfileListResponse,
            'KalturaRegistrySettings': KalturaRegistrySettings,
            'KalturaRegistrySettingsListResponse': KalturaRegistrySettingsListResponse,
            'KalturaParentalRule': KalturaParentalRule,
            'KalturaParentalRuleListResponse': KalturaParentalRuleListResponse,
            'KalturaUserRole': KalturaUserRole,
            'KalturaUserRoleListResponse': KalturaUserRoleListResponse,
            'KalturaClientConfiguration': KalturaClientConfiguration,
            'KalturaBaseResponseProfile': KalturaBaseResponseProfile,
            'KalturaRequestConfiguration': KalturaRequestConfiguration,
            'KalturaFilter': KalturaFilter,
            'KalturaDetachedResponseProfile': KalturaDetachedResponseProfile,
            'KalturaRelatedObjectFilter': KalturaRelatedObjectFilter,
            'KalturaSocialCommentFilter': KalturaSocialCommentFilter,
            'KalturaSocialFriendActivityFilter': KalturaSocialFriendActivityFilter,
            'KalturaSocialActionFilter': KalturaSocialActionFilter,
            'KalturaPaymentMethodProfileFilter': KalturaPaymentMethodProfileFilter,
            'KalturaHouseholdDeviceFilter': KalturaHouseholdDeviceFilter,
            'KalturaHouseholdUserFilter': KalturaHouseholdUserFilter,
            'KalturaConfigurationsFilter': KalturaConfigurationsFilter,
            'KalturaReportFilter': KalturaReportFilter,
            'KalturaDeviceReportFilter': KalturaDeviceReportFilter,
            'KalturaConfigurationGroupTagFilter': KalturaConfigurationGroupTagFilter,
            'KalturaConfigurationGroupDeviceFilter': KalturaConfigurationGroupDeviceFilter,
            'KalturaFavoriteFilter': KalturaFavoriteFilter,
            'KalturaOTTUserFilter': KalturaOTTUserFilter,
            'KalturaCollectionFilter': KalturaCollectionFilter,
            'KalturaDiscountDetailsFilter': KalturaDiscountDetailsFilter,
            'KalturaPricePlanFilter': KalturaPricePlanFilter,
            'KalturaPriceDetailsFilter': KalturaPriceDetailsFilter,
            'KalturaSubscriptionSetFilter': KalturaSubscriptionSetFilter,
            'KalturaSubscriptionDependencySetFilter': KalturaSubscriptionDependencySetFilter,
            'KalturaSubscriptionFilter': KalturaSubscriptionFilter,
            'KalturaPersonalListFilter': KalturaPersonalListFilter,
            'KalturaEngagementFilter': KalturaEngagementFilter,
            'KalturaReminderFilter': KalturaReminderFilter,
            'KalturaAssetReminderFilter': KalturaAssetReminderFilter,
            'KalturaSeriesReminderFilter': KalturaSeriesReminderFilter,
            'KalturaSeasonsReminderFilter': KalturaSeasonsReminderFilter,
            'KalturaFollowTvSeriesFilter': KalturaFollowTvSeriesFilter,
            'KalturaInboxMessageFilter': KalturaInboxMessageFilter,
            'KalturaAnnouncementFilter': KalturaAnnouncementFilter,
            'KalturaPersonalFeedFilter': KalturaPersonalFeedFilter,
            'KalturaTopicFilter': KalturaTopicFilter,
            'KalturaSeriesRecordingFilter': KalturaSeriesRecordingFilter,
            'KalturaProductPriceFilter': KalturaProductPriceFilter,
            'KalturaEntitlementFilter': KalturaEntitlementFilter,
            'KalturaTransactionHistoryFilter': KalturaTransactionHistoryFilter,
            'KalturaRecordingContextFilter': KalturaRecordingContextFilter,
            'KalturaRecordingFilter': KalturaRecordingFilter,
            'KalturaPartnerConfigurationFilter': KalturaPartnerConfigurationFilter,
            'KalturaAggregationCountFilter': KalturaAggregationCountFilter,
            'KalturaPersistedFilter': KalturaPersistedFilter,
            'KalturaAssetFilter': KalturaAssetFilter,
            'KalturaBaseSearchAssetFilter': KalturaBaseSearchAssetFilter,
            'KalturaPersonalListSearchFilter': KalturaPersonalListSearchFilter,
            'KalturaSearchAssetFilter': KalturaSearchAssetFilter,
            'KalturaSearchAssetListFilter': KalturaSearchAssetListFilter,
            'KalturaScheduledRecordingProgramFilter': KalturaScheduledRecordingProgramFilter,
            'KalturaBundleFilter': KalturaBundleFilter,
            'KalturaChannelExternalFilter': KalturaChannelExternalFilter,
            'KalturaChannelFilter': KalturaChannelFilter,
            'KalturaRelatedFilter': KalturaRelatedFilter,
            'KalturaRelatedExternalFilter': KalturaRelatedExternalFilter,
            'KalturaSearchExternalFilter': KalturaSearchExternalFilter,
            'KalturaBulkFilter': KalturaBulkFilter,
            'KalturaAssetStructMetaFilter': KalturaAssetStructMetaFilter,
            'KalturaChannelsFilter': KalturaChannelsFilter,
            'KalturaMediaFileFilter': KalturaMediaFileFilter,
            'KalturaImageFilter': KalturaImageFilter,
            'KalturaImageTypeFilter': KalturaImageTypeFilter,
            'KalturaTagFilter': KalturaTagFilter,
            'KalturaAssetStructFilter': KalturaAssetStructFilter,
            'KalturaAssetCommentFilter': KalturaAssetCommentFilter,
            'KalturaBookmarkFilter': KalturaBookmarkFilter,
            'KalturaAssetHistoryFilter': KalturaAssetHistoryFilter,
            'KalturaAssetRuleFilter': KalturaAssetRuleFilter,
            'KalturaAssetUserRuleFilter': KalturaAssetUserRuleFilter,
            'KalturaCurrencyFilter': KalturaCurrencyFilter,
            'KalturaLanguageFilter': KalturaLanguageFilter,
            'KalturaMetaFilter': KalturaMetaFilter,
            'KalturaCountryFilter': KalturaCountryFilter,
            'KalturaSearchHistoryFilter': KalturaSearchHistoryFilter,
            'KalturaRegionFilter': KalturaRegionFilter,
            'KalturaUserAssetRuleFilter': KalturaUserAssetRuleFilter,
            'KalturaParentalRuleFilter': KalturaParentalRuleFilter,
            'KalturaExportTaskFilter': KalturaExportTaskFilter,
            'KalturaUserRoleFilter': KalturaUserRoleFilter,
        }

    # @return string
    def getName(self):
        return ''

