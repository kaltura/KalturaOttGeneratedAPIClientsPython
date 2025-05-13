# ===================================================================================================
#                           _  __     _ _
#                          | |/ /__ _| | |_ _  _ _ _ __ _
#                          | ' </ _` | |  _| || | '_/ _` |
#                          |_|\_\__,_|_|\__|\_,_|_| \__,_|
#
# This file is part of the Kaltura Collaborative Media Suite which allows users
# to do with audio, video, and animation what Wiki platforms allow them to do with
# text.
#
# Copyright (C) 2006-2023  Kaltura Inc.
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
from typing import List
from KalturaClient import KalturaConfiguration
from KalturaClient.Plugins.Core import KalturaObject
from KalturaClient.Plugins.Core import KalturaAiMetadataGeneratorService
from KalturaClient.Plugins.Core import KalturaAnnouncementService
from KalturaClient.Plugins.Core import KalturaAppTokenService
from KalturaClient.Plugins.Core import KalturaAssetCommentService
from KalturaClient.Plugins.Core import KalturaAssetService
from KalturaClient.Plugins.Core import KalturaAssetFileService
from KalturaClient.Plugins.Core import KalturaAssetFilePpvService
from KalturaClient.Plugins.Core import KalturaAssetHistoryService
from KalturaClient.Plugins.Core import KalturaAssetPersonalMarkupService
from KalturaClient.Plugins.Core import KalturaAssetPersonalSelectionService
from KalturaClient.Plugins.Core import KalturaAssetRuleService
from KalturaClient.Plugins.Core import KalturaAssetStatisticsService
from KalturaClient.Plugins.Core import KalturaAssetStructService
from KalturaClient.Plugins.Core import KalturaAssetStructMetaService
from KalturaClient.Plugins.Core import KalturaAssetUserRuleService
from KalturaClient.Plugins.Core import KalturaBookmarkService
from KalturaClient.Plugins.Core import KalturaBulkUploadService
from KalturaClient.Plugins.Core import KalturaBulkUploadStatisticsService
from KalturaClient.Plugins.Core import KalturaBusinessModuleRuleService
from KalturaClient.Plugins.Core import KalturaCampaignService
from KalturaClient.Plugins.Core import KalturaCategoryItemService
from KalturaClient.Plugins.Core import KalturaCategoryTreeService
from KalturaClient.Plugins.Core import KalturaCategoryVersionService
from KalturaClient.Plugins.Core import KalturaCdnAdapterProfileService
from KalturaClient.Plugins.Core import KalturaCdnPartnerSettingsService
from KalturaClient.Plugins.Core import KalturaCDVRAdapterProfileService
from KalturaClient.Plugins.Core import KalturaChannelService
from KalturaClient.Plugins.Core import KalturaCollectionService
from KalturaClient.Plugins.Core import KalturaCompensationService
from KalturaClient.Plugins.Core import KalturaConfigurationGroupService
from KalturaClient.Plugins.Core import KalturaConfigurationGroupDeviceService
from KalturaClient.Plugins.Core import KalturaConfigurationGroupTagService
from KalturaClient.Plugins.Core import KalturaConfigurationsService
from KalturaClient.Plugins.Core import KalturaCountryService
from KalturaClient.Plugins.Core import KalturaCouponService
from KalturaClient.Plugins.Core import KalturaCouponsGroupService
from KalturaClient.Plugins.Core import KalturaCurrencyService
from KalturaClient.Plugins.Core import KalturaDeviceBrandService
from KalturaClient.Plugins.Core import KalturaDeviceFamilyService
from KalturaClient.Plugins.Core import KalturaDeviceReferenceDataService
from KalturaClient.Plugins.Core import KalturaDiscountDetailsService
from KalturaClient.Plugins.Core import KalturaDrmProfileService
from KalturaClient.Plugins.Core import KalturaDurationService
from KalturaClient.Plugins.Core import KalturaDynamicListService
from KalturaClient.Plugins.Core import KalturaEmailService
from KalturaClient.Plugins.Core import KalturaEngagementAdapterService
from KalturaClient.Plugins.Core import KalturaEngagementService
from KalturaClient.Plugins.Core import KalturaEntitlementService
from KalturaClient.Plugins.Core import KalturaEpgService
from KalturaClient.Plugins.Core import KalturaEpgServicePartnerConfigurationService
from KalturaClient.Plugins.Core import KalturaEventNotificationActionService
from KalturaClient.Plugins.Core import KalturaEventNotificationService
from KalturaClient.Plugins.Core import KalturaExportTaskService
from KalturaClient.Plugins.Core import KalturaExternalChannelProfileService
from KalturaClient.Plugins.Core import KalturaFavoriteService
from KalturaClient.Plugins.Core import KalturaFollowTvSeriesService
from KalturaClient.Plugins.Core import KalturaGeoBlockRuleService
from KalturaClient.Plugins.Core import KalturaHomeNetworkService
from KalturaClient.Plugins.Core import KalturaHouseholdService
from KalturaClient.Plugins.Core import KalturaHouseholdCouponService
from KalturaClient.Plugins.Core import KalturaHouseholdDeviceService
from KalturaClient.Plugins.Core import KalturaHouseholdLimitationsService
from KalturaClient.Plugins.Core import KalturaHouseholdPaymentGatewayService
from KalturaClient.Plugins.Core import KalturaHouseholdPaymentMethodService
from KalturaClient.Plugins.Core import KalturaHouseholdPremiumServiceService
from KalturaClient.Plugins.Core import KalturaHouseholdQuotaService
from KalturaClient.Plugins.Core import KalturaHouseholdSegmentService
from KalturaClient.Plugins.Core import KalturaHouseholdUserService
from KalturaClient.Plugins.Core import KalturaImageService
from KalturaClient.Plugins.Core import KalturaImageTypeService
from KalturaClient.Plugins.Core import KalturaInboxMessageService
from KalturaClient.Plugins.Core import KalturaIngestProfileService
from KalturaClient.Plugins.Core import KalturaIngestStatusService
from KalturaClient.Plugins.Core import KalturaIotService
from KalturaClient.Plugins.Core import KalturaIotProfileService
from KalturaClient.Plugins.Core import KalturaLabelService
from KalturaClient.Plugins.Core import KalturaLanguageService
from KalturaClient.Plugins.Core import KalturaLicensedUrlService
from KalturaClient.Plugins.Core import KalturaLineupService
from KalturaClient.Plugins.Core import KalturaLiveToVodService
from KalturaClient.Plugins.Core import KalturaMediaConcurrencyRuleService
from KalturaClient.Plugins.Core import KalturaMediaFileService
from KalturaClient.Plugins.Core import KalturaMediaFileDynamicDataService
from KalturaClient.Plugins.Core import KalturaMediaFileTypeService
from KalturaClient.Plugins.Core import KalturaMessageTemplateService
from KalturaClient.Plugins.Core import KalturaMetaService
from KalturaClient.Plugins.Core import KalturaMfaPartnerConfigurationService
from KalturaClient.Plugins.Core import KalturaNotificationService
from KalturaClient.Plugins.Core import KalturaNotificationsPartnerSettingsService
from KalturaClient.Plugins.Core import KalturaNotificationsSettingsService
from KalturaClient.Plugins.Core import KalturaOssAdapterProfileService
from KalturaClient.Plugins.Core import KalturaOttCategoryService
from KalturaClient.Plugins.Core import KalturaOttUserService
from KalturaClient.Plugins.Core import KalturaParentalRuleService
from KalturaClient.Plugins.Core import KalturaPartnerConfigurationService
from KalturaClient.Plugins.Core import KalturaPartnerService
from KalturaClient.Plugins.Core import KalturaPartnerPremiumServicesService
from KalturaClient.Plugins.Core import KalturaPasswordPolicyService
from KalturaClient.Plugins.Core import KalturaPaymentGatewayProfileService
from KalturaClient.Plugins.Core import KalturaPaymentMethodProfileService
from KalturaClient.Plugins.Core import KalturaPermissionService
from KalturaClient.Plugins.Core import KalturaPermissionItemService
from KalturaClient.Plugins.Core import KalturaPersonalActivityCleanupService
from KalturaClient.Plugins.Core import KalturaPersonalFeedService
from KalturaClient.Plugins.Core import KalturaPersonalListService
from KalturaClient.Plugins.Core import KalturaPinService
from KalturaClient.Plugins.Core import KalturaPlaybackProfileService
from KalturaClient.Plugins.Core import KalturaPpvService
from KalturaClient.Plugins.Core import KalturaPreviewModuleService
from KalturaClient.Plugins.Core import KalturaPriceDetailsService
from KalturaClient.Plugins.Core import KalturaPricePlanService
from KalturaClient.Plugins.Core import KalturaProductPriceService
from KalturaClient.Plugins.Core import KalturaProgramAssetGroupOfferService
from KalturaClient.Plugins.Core import KalturaPurchaseSettingsService
from KalturaClient.Plugins.Core import KalturaRatioService
from KalturaClient.Plugins.Core import KalturaRecommendationProfileService
from KalturaClient.Plugins.Core import KalturaRecordingService
from KalturaClient.Plugins.Core import KalturaRegionService
from KalturaClient.Plugins.Core import KalturaRegistrySettingsService
from KalturaClient.Plugins.Core import KalturaReminderService
from KalturaClient.Plugins.Core import KalturaReportService
from KalturaClient.Plugins.Core import KalturaSearchHistoryService
from KalturaClient.Plugins.Core import KalturaSearchPriorityGroupService
from KalturaClient.Plugins.Core import KalturaSearchPriorityGroupOrderedIdsSetService
from KalturaClient.Plugins.Core import KalturaSegmentationTypeService
from KalturaClient.Plugins.Core import KalturaSemanticAssetSearchPartnerConfigService
from KalturaClient.Plugins.Core import KalturaSeriesRecordingService
from KalturaClient.Plugins.Core import KalturaSessionService
from KalturaClient.Plugins.Core import KalturaSmsAdapterProfileService
from KalturaClient.Plugins.Core import KalturaSocialActionService
from KalturaClient.Plugins.Core import KalturaSocialCommentService
from KalturaClient.Plugins.Core import KalturaSocialService
from KalturaClient.Plugins.Core import KalturaSocialFriendActivityService
from KalturaClient.Plugins.Core import KalturaSsoAdapterProfileService
from KalturaClient.Plugins.Core import KalturaStreamingDeviceService
from KalturaClient.Plugins.Core import KalturaSubscriptionService
from KalturaClient.Plugins.Core import KalturaSubscriptionSetService
from KalturaClient.Plugins.Core import KalturaSubtitlesService
from KalturaClient.Plugins.Core import KalturaSystemService
from KalturaClient.Plugins.Core import KalturaTagService
from KalturaClient.Plugins.Core import KalturaTimeShiftedTvPartnerSettingsService
from KalturaClient.Plugins.Core import KalturaTopicService
from KalturaClient.Plugins.Core import KalturaTopicNotificationService
from KalturaClient.Plugins.Core import KalturaTopicNotificationMessageService
from KalturaClient.Plugins.Core import KalturaTransactionService
from KalturaClient.Plugins.Core import KalturaTransactionHistoryService
from KalturaClient.Plugins.Core import KalturaTvmRuleService
from KalturaClient.Plugins.Core import KalturaUnifiedPaymentService
from KalturaClient.Plugins.Core import KalturaUploadTokenService
from KalturaClient.Plugins.Core import KalturaUsageModuleService
from KalturaClient.Plugins.Core import KalturaUserAssetRuleService
from KalturaClient.Plugins.Core import KalturaUserAssetsListItemService
from KalturaClient.Plugins.Core import KalturaUserInterestService
from KalturaClient.Plugins.Core import KalturaUserLogService
from KalturaClient.Plugins.Core import KalturaUserLoginPinService
from KalturaClient.Plugins.Core import KalturaUserRoleService
from KalturaClient.Plugins.Core import KalturaUserSegmentService
from KalturaClient.Plugins.Core import KalturaUserSessionProfileService
from KalturaClient.Plugins.Core import KalturaWatchBasedRecommendationsAdminConfigurationService
from KalturaClient.Plugins.Core import KalturaWatchBasedRecommendationsProfileService

class MultiRequestSubResult(object):
    def __init__(self, value): ...
    def __getattr__(self, name) -> MultiRequestSubResult: ...
    def __getitem__(self, key) -> MultiRequestSubResult: ...

class KalturaClient:
    def __init__(self, config: KalturaConfiguration, remove_data_content: bool = False): ...
    def getKs(self) -> str: ...
    def setKs(self, ks: str): ...
    def getLanguage(self) -> str: ...
    def setLanguage(self, language: str): ...
    def getPartnerId(self) -> int: ...
    def setPartnerId(self, partner_id: int): ...
    def getClientTag(self) -> str: ...
    def setClientTag(self, client_tag: str): ...
    def getApiVersion(self) -> str: ...
    def setApiVersion(self, api_version: str): ...
    def getConfig(self) -> KalturaConfiguration: ...
    def setConfig(self, config: KalturaConfiguration): ...
    def startMultiRequest(self): ...
    def doMultiRequest(self) -> List[KalturaObject]: ...

    aiMetadataGenerator: KalturaAiMetadataGeneratorService
    announcement: KalturaAnnouncementService
    appToken: KalturaAppTokenService
    assetComment: KalturaAssetCommentService
    asset: KalturaAssetService
    assetFile: KalturaAssetFileService
    assetFilePpv: KalturaAssetFilePpvService
    assetHistory: KalturaAssetHistoryService
    assetPersonalMarkup: KalturaAssetPersonalMarkupService
    assetPersonalSelection: KalturaAssetPersonalSelectionService
    assetRule: KalturaAssetRuleService
    assetStatistics: KalturaAssetStatisticsService
    assetStruct: KalturaAssetStructService
    assetStructMeta: KalturaAssetStructMetaService
    assetUserRule: KalturaAssetUserRuleService
    bookmark: KalturaBookmarkService
    bulkUpload: KalturaBulkUploadService
    bulkUploadStatistics: KalturaBulkUploadStatisticsService
    businessModuleRule: KalturaBusinessModuleRuleService
    campaign: KalturaCampaignService
    categoryItem: KalturaCategoryItemService
    categoryTree: KalturaCategoryTreeService
    categoryVersion: KalturaCategoryVersionService
    cdnAdapterProfile: KalturaCdnAdapterProfileService
    cdnPartnerSettings: KalturaCdnPartnerSettingsService
    cDVRAdapterProfile: KalturaCDVRAdapterProfileService
    channel: KalturaChannelService
    collection: KalturaCollectionService
    compensation: KalturaCompensationService
    configurationGroup: KalturaConfigurationGroupService
    configurationGroupDevice: KalturaConfigurationGroupDeviceService
    configurationGroupTag: KalturaConfigurationGroupTagService
    configurations: KalturaConfigurationsService
    country: KalturaCountryService
    coupon: KalturaCouponService
    couponsGroup: KalturaCouponsGroupService
    currency: KalturaCurrencyService
    deviceBrand: KalturaDeviceBrandService
    deviceFamily: KalturaDeviceFamilyService
    deviceReferenceData: KalturaDeviceReferenceDataService
    discountDetails: KalturaDiscountDetailsService
    drmProfile: KalturaDrmProfileService
    duration: KalturaDurationService
    dynamicList: KalturaDynamicListService
    email: KalturaEmailService
    engagementAdapter: KalturaEngagementAdapterService
    engagement: KalturaEngagementService
    entitlement: KalturaEntitlementService
    epg: KalturaEpgService
    epgServicePartnerConfiguration: KalturaEpgServicePartnerConfigurationService
    eventNotificationAction: KalturaEventNotificationActionService
    eventNotification: KalturaEventNotificationService
    exportTask: KalturaExportTaskService
    externalChannelProfile: KalturaExternalChannelProfileService
    favorite: KalturaFavoriteService
    followTvSeries: KalturaFollowTvSeriesService
    geoBlockRule: KalturaGeoBlockRuleService
    homeNetwork: KalturaHomeNetworkService
    household: KalturaHouseholdService
    householdCoupon: KalturaHouseholdCouponService
    householdDevice: KalturaHouseholdDeviceService
    householdLimitations: KalturaHouseholdLimitationsService
    householdPaymentGateway: KalturaHouseholdPaymentGatewayService
    householdPaymentMethod: KalturaHouseholdPaymentMethodService
    householdPremiumService: KalturaHouseholdPremiumServiceService
    householdQuota: KalturaHouseholdQuotaService
    householdSegment: KalturaHouseholdSegmentService
    householdUser: KalturaHouseholdUserService
    image: KalturaImageService
    imageType: KalturaImageTypeService
    inboxMessage: KalturaInboxMessageService
    IngestProfile: KalturaIngestProfileService
    ingestStatus: KalturaIngestStatusService
    iot: KalturaIotService
    iotProfile: KalturaIotProfileService
    label: KalturaLabelService
    language: KalturaLanguageService
    licensedUrl: KalturaLicensedUrlService
    lineup: KalturaLineupService
    liveToVod: KalturaLiveToVodService
    mediaConcurrencyRule: KalturaMediaConcurrencyRuleService
    mediaFile: KalturaMediaFileService
    mediaFileDynamicData: KalturaMediaFileDynamicDataService
    mediaFileType: KalturaMediaFileTypeService
    messageTemplate: KalturaMessageTemplateService
    meta: KalturaMetaService
    mfaPartnerConfiguration: KalturaMfaPartnerConfigurationService
    notification: KalturaNotificationService
    notificationsPartnerSettings: KalturaNotificationsPartnerSettingsService
    notificationsSettings: KalturaNotificationsSettingsService
    ossAdapterProfile: KalturaOssAdapterProfileService
    ottCategory: KalturaOttCategoryService
    ottUser: KalturaOttUserService
    parentalRule: KalturaParentalRuleService
    partnerConfiguration: KalturaPartnerConfigurationService
    partner: KalturaPartnerService
    partnerPremiumServices: KalturaPartnerPremiumServicesService
    passwordPolicy: KalturaPasswordPolicyService
    paymentGatewayProfile: KalturaPaymentGatewayProfileService
    paymentMethodProfile: KalturaPaymentMethodProfileService
    permission: KalturaPermissionService
    permissionItem: KalturaPermissionItemService
    personalActivityCleanup: KalturaPersonalActivityCleanupService
    personalFeed: KalturaPersonalFeedService
    personalList: KalturaPersonalListService
    pin: KalturaPinService
    playbackProfile: KalturaPlaybackProfileService
    ppv: KalturaPpvService
    previewModule: KalturaPreviewModuleService
    priceDetails: KalturaPriceDetailsService
    pricePlan: KalturaPricePlanService
    productPrice: KalturaProductPriceService
    programAssetGroupOffer: KalturaProgramAssetGroupOfferService
    purchaseSettings: KalturaPurchaseSettingsService
    ratio: KalturaRatioService
    recommendationProfile: KalturaRecommendationProfileService
    recording: KalturaRecordingService
    region: KalturaRegionService
    registrySettings: KalturaRegistrySettingsService
    reminder: KalturaReminderService
    report: KalturaReportService
    searchHistory: KalturaSearchHistoryService
    searchPriorityGroup: KalturaSearchPriorityGroupService
    searchPriorityGroupOrderedIdsSet: KalturaSearchPriorityGroupOrderedIdsSetService
    segmentationType: KalturaSegmentationTypeService
    semanticAssetSearchPartnerConfig: KalturaSemanticAssetSearchPartnerConfigService
    seriesRecording: KalturaSeriesRecordingService
    session: KalturaSessionService
    smsAdapterProfile: KalturaSmsAdapterProfileService
    socialAction: KalturaSocialActionService
    socialComment: KalturaSocialCommentService
    social: KalturaSocialService
    socialFriendActivity: KalturaSocialFriendActivityService
    ssoAdapterProfile: KalturaSsoAdapterProfileService
    streamingDevice: KalturaStreamingDeviceService
    subscription: KalturaSubscriptionService
    subscriptionSet: KalturaSubscriptionSetService
    subtitles: KalturaSubtitlesService
    system: KalturaSystemService
    tag: KalturaTagService
    timeShiftedTvPartnerSettings: KalturaTimeShiftedTvPartnerSettingsService
    topic: KalturaTopicService
    topicNotification: KalturaTopicNotificationService
    topicNotificationMessage: KalturaTopicNotificationMessageService
    transaction: KalturaTransactionService
    transactionHistory: KalturaTransactionHistoryService
    tvmRule: KalturaTvmRuleService
    unifiedPayment: KalturaUnifiedPaymentService
    uploadToken: KalturaUploadTokenService
    usageModule: KalturaUsageModuleService
    userAssetRule: KalturaUserAssetRuleService
    userAssetsListItem: KalturaUserAssetsListItemService
    userInterest: KalturaUserInterestService
    userLog: KalturaUserLogService
    userLoginPin: KalturaUserLoginPinService
    userRole: KalturaUserRoleService
    userSegment: KalturaUserSegmentService
    userSessionProfile: KalturaUserSessionProfileService
    watchBasedRecommendationsAdminConfiguration: KalturaWatchBasedRecommendationsAdminConfigurationService
    watchBasedRecommendationsProfile: KalturaWatchBasedRecommendationsProfileService