#!/usr/bin/python3

import sys
import re
from lxml import etree 
import csv

#Archivo XML que cargar
#file = "../datos/ftppriv.cnig.es/17/xml/spaignActa_1923_05918020150591802015.xml"
#file = "../datos/ftppriv.cnig.es/01/xml/spaignActa_1927_05675720150567572015.xml"
#file = "../datos/ftppriv.cnig.es/18/xml/spaignActa_1990_1042142015071042142015.xml"
#file = "../datos/ftppriv.cnig.es/Metadatos_ActasSerie2015.xml"
file = sys.argv[1]
root = etree.parse(file)

#Ruta del archivo con las definiciones de cada ruta (etiquetas)
tags_file="./acta_tags_list.txt"

#Objeto con un diccionario con clave la ruta y valor el nombre de la etiqueta
tags ={}

#Objeto con un diccionario con clave la ruta y valor el texto del elemento
#for i in `cat /tmp/tags`; do echo "\""$i"\": None,"; done
data = {
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/": None,
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/type/MD_KeywordTypeCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/topicCategory/MD_TopicCategoryCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/title/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/date/Date/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/positionName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/individualName/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/role/CI_RoleCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/organisationName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/individualName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/presentationForm/CI_PresentationFormCode/": None,
"MD_Metadata/contact/CI_ResponsibleParty/role/CI_RoleCode/": None,
"MD_Metadata/contact/CI_ResponsibleParty/positionName/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/individualName/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/": None,
"MD_Metadata/referenceSystemInfo/MD_ReferenceSystem/referenceSystemIdentifier/RS_Identifier/code/CharacterString/": None,
"MD_Metadata/metadataStandardVersion/CharacterString/": None,
"MD_Metadata/metadataStandardName/CharacterString/": None,
"MD_Metadata/language/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/role/CI_RoleCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/positionName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/organisationName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/individualName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/specificUsage/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceConstraints/MD_LegalConstraints/useLimitation/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceConstraints/MD_LegalConstraints/useConstraints/MD_RestrictionCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/purpose/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/positionName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/facsimile/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/contactInstructions/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/language/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/graphicOverview/MD_BrowseGraphic/fileType/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/graphicOverview/MD_BrowseGraphic/fileName/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/graphicOverview/MD_BrowseGraphic/fileDescription/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/westBoundLongitude/Decimal/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/southBoundLatitude/Decimal/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/northBoundLatitude/Decimal/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/extentTypeCode/Boolean/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/eastBoundLongitude/Decimal/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/credit/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/title/CharacterString/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/date/CI_Date/date/Date/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/URL/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/characterSet/MD_CharacterSetCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/abstract/CharacterString/": None,
"MD_Metadata/hierarchyLevel/MD_ScopeCode/": None,
"MD_Metadata/fileIdentifier/CharacterString/": None,
"MD_Metadata/distributionInfo/MD_Distribution/transferOptions/MD_DigitalTransferOptions/onLine/CI_OnlineResource/linkage/URL/": None,
"MD_Metadata/distributionInfo/MD_Distribution/distributionFormat/MD_Format/version/CharacterString/": None,
"MD_Metadata/distributionInfo/MD_Distribution/distributionFormat/MD_Format/name/CharacterString/": None,
"MD_Metadata/dateStamp/Date/": None,
"MD_Metadata/dataQualityInfo/DQ_DataQuality/scope/DQ_Scope/level/MD_ScopeCode/": None,
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/statement/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/facsimile/CharacterString/": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/": None,
"MD_Metadata/characterSet/MD_CharacterSetCode/": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/topicCategory/MD_TopicCategoryCode/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/topicCategory/MD_TopicCategoryCode/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/role/CI_RoleCode/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/organisationName/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/individualName/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/type/MD_KeywordTypeCode/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/type/MD_KeywordTypeCode/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/type/MD_KeywordTypeCode/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/title/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/title/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/date/Date/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/date/Date/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/9": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/8": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/7": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/6": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/10": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/presentationForm/CI_PresentationFormCode/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/positionName/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/positionName/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/individualName/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/individualName/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/9": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/8": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/7": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/6": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/10": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/5": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/4": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/3": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/2": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/1": None,
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/4": None,
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/3": None,
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/2": None,
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/role/CI_RoleCode/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/positionName/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/individualName/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/2": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/1": None,
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/1": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/11": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/12": None,
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/13": None
}


def load_tags(tags_file,tags):
    with open (tags_file) as f:
        for line in f:
            both_tags = line.split(':')
            tags[both_tags[0].replace(" ", "")]=both_tags[1]
    #print (tags.keys())


#Obtiene la ruta completa a cada elemento    
def get_parents(element):
    text = ""
    while element != None:
        text = sanitize_tag(element)+"/"+text
        #print (element.tag)
        element = element.getparent()
    return text


#Sanitiza el texto de salida eliminando la cadena de los namespaces del XML. 
def sanitize_tag(element):
   text = element.tag
   sanitized2 = text.replace("{http://www.isotc211.org/2005/gmd}","") 
   sanitized = sanitized2.replace("{http://www.isotc211.org/2005/gco}","") 
   return sanitized



#Carga de las etiquetas
load_tags(tags_file,tags)

#Diccionario para la gestión de etiquetas duplicadas
dup_tags = {}


#Gestiona las etiquetas duplicadas añadiendo un número al final de la etiqueta en caso de coincidencia
def update_key(dicct,kkey):
    if kkey in dup_tags:
        dup_tags[str(kkey)] = dup_tags[str(kkey)]+1
    else:
        dup_tags[str(kkey)] = 1
    return str(kkey)+str(dup_tags[str(kkey)])




#Bucle principal que recorre todo el XML imprimiendo la ruta y el contenido de cada elemento 
for element in root.iter():
    if element.text and not element.text.isspace():
#Imprimir etiqueta y contenido del XML
#        print("%s - %s" % (get_parents(element), element.text))
#Imprimir etiqueta del XML
#        print("%s" % (get_parents(element)))
        (key, val) = (get_parents(element), element.text)
        if key in data:
            data[str(update_key(data,key))] = val
        else: 
#Desde que data ha sido inicializado con todas las claves, nunca se llegará aquí
#            data[str(key)] = val
            sys.exit()            



#Nombre del archivo de salida
outputname = file + ".csv"

#Orden de las tags
#TODO: Establecer el orden final de las tags. Se hará tal y como indican los metadatos Metadatos_ActasSerie2015.xml
#Sin terminar.
#tags_order = ["MD_Metadata/fileIdentifier/CharacterString/", "MD_Metadata/identificationInfo/MD_DataIdentification/language/CharacterString/", "MD_Metadata/characterSet/MD_CharacterSetCode/","MD_Metadata/hierarchyLevel/MD_ScopeCode/","MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/","MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/1","MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/","MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/1","MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/","MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/1","MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/","MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/1","MD_Metadata/contact/CI_ResponsibleParty/role/CI_RoleCode/","MD_Metadata/contact/CI_ResponsibleParty/role/CI_RoleCode/1","MD_Metadata/dateStamp/Date/","MD_Metadata/metadataStandardName/CharacterString/","MD_Metadata/metadataStandardVersion/CharacterString/","MD_Metadata/spatialRepresentationInfo/MD_GridSpatialRepresentation/numberOfDimensions/Integer/","MD_Metadata/spatialRepresentationInfo/MD_GridSpatialRepresentation/cellGeometry/MD_CellGeometryCode/","MD_Metadata/spatialRepresentationInfo/MD_GridSpatialRepresentation/transformationParameterAvailability/Boolean/","MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/title/CharacterString/","MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/alternateTitle/CharacterString/","MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/date/CI_Date/date/Date/","MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/","","","","","","",  "TODO" ]

tags_order=["MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/",
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/type/MD_KeywordTypeCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/topicCategory/MD_TopicCategoryCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/title/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/date/Date/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/positionName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/individualName/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/role/CI_RoleCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/organisationName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/individualName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/presentationForm/CI_PresentationFormCode/",
"MD_Metadata/contact/CI_ResponsibleParty/role/CI_RoleCode/",
"MD_Metadata/contact/CI_ResponsibleParty/positionName/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/individualName/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/",
"MD_Metadata/referenceSystemInfo/MD_ReferenceSystem/referenceSystemIdentifier/RS_Identifier/code/CharacterString/",
"MD_Metadata/metadataStandardVersion/CharacterString/",
"MD_Metadata/metadataStandardName/CharacterString/",
"MD_Metadata/language/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/role/CI_RoleCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/positionName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/organisationName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/individualName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/userContactInfo/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceSpecificUsage/MD_Usage/specificUsage/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceConstraints/MD_LegalConstraints/useLimitation/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/resourceConstraints/MD_LegalConstraints/useConstraints/MD_RestrictionCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/purpose/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/positionName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/facsimile/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/contactInstructions/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/language/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/graphicOverview/MD_BrowseGraphic/fileType/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/graphicOverview/MD_BrowseGraphic/fileName/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/graphicOverview/MD_BrowseGraphic/fileDescription/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/westBoundLongitude/Decimal/",
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/southBoundLatitude/Decimal/",
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/northBoundLatitude/Decimal/",
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/extentTypeCode/Boolean/",
"MD_Metadata/identificationInfo/MD_DataIdentification/extent/EX_Extent/geographicElement/EX_GeographicBoundingBox/eastBoundLongitude/Decimal/",
"MD_Metadata/identificationInfo/MD_DataIdentification/credit/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/title/CharacterString/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/date/CI_Date/date/Date/",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/URL/",
"MD_Metadata/identificationInfo/MD_DataIdentification/characterSet/MD_CharacterSetCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/abstract/CharacterString/",
"MD_Metadata/hierarchyLevel/MD_ScopeCode/",
"MD_Metadata/fileIdentifier/CharacterString/",
"MD_Metadata/distributionInfo/MD_Distribution/transferOptions/MD_DigitalTransferOptions/onLine/CI_OnlineResource/linkage/URL/",
"MD_Metadata/distributionInfo/MD_Distribution/distributionFormat/MD_Format/version/CharacterString/",
"MD_Metadata/distributionInfo/MD_Distribution/distributionFormat/MD_Format/name/CharacterString/",
"MD_Metadata/dateStamp/Date/",
"MD_Metadata/dataQualityInfo/DQ_DataQuality/scope/DQ_Scope/level/MD_ScopeCode/",
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/statement/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/facsimile/CharacterString/",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/",
"MD_Metadata/characterSet/MD_CharacterSetCode/",
"MD_Metadata/identificationInfo/MD_DataIdentification/topicCategory/MD_TopicCategoryCode/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/topicCategory/MD_TopicCategoryCode/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/role/CI_RoleCode/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/organisationName/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/individualName/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/pointOfContact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/type/MD_KeywordTypeCode/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/type/MD_KeywordTypeCode/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/type/MD_KeywordTypeCode/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/title/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/title/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/dateType/CI_DateTypeCode/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/date/Date/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/thesaurusName/CI_Citation/date/CI_Date/date/Date/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/9",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/8",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/7",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/6",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/10",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/presentationForm/CI_PresentationFormCode/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/role/CI_RoleCode/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/positionName/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/positionName/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/organisationName/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/individualName/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/individualName/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/9",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/8",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/7",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/6",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/10",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/onlineResource/CI_OnlineResource/linkage/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/5",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/4",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/3",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/2",
"MD_Metadata/identificationInfo/MD_DataIdentification/citation/CI_Citation/citedResponsibleParty/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/1",
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/4",
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/3",
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/2",
"MD_Metadata/dataQualityInfo/DQ_DataQuality/lineage/LI_Lineage/processStep/LI_ProcessStep/description/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/role/CI_RoleCode/1",
"MD_Metadata/contact/CI_ResponsibleParty/positionName/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/organisationName/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/individualName/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/2",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/phone/CI_Telephone/voice/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/hoursOfService/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/postalCode/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/electronicMailAddress/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/deliveryPoint/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/country/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/city/CharacterString/1",
"MD_Metadata/contact/CI_ResponsibleParty/contactInfo/CI_Contact/address/CI_Address/administrativeArea/CharacterString/1",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/11",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/12",
"MD_Metadata/identificationInfo/MD_DataIdentification/descriptiveKeywords/MD_Keywords/keyword/CharacterString/13"]


with open("db.csv",'a') as f:
#    w = csv.DictWriter(f, data.keys(),'raise')
#    w = csv.DictWriter(f, tags_order, extrasaction='ignore')
#    listado = list(data.keys())
    listado = []
    for key in data.keys():
        listado.append(key)
    listado.sort()
    #w = csv.DictWriter(f, listado, extrasaction='ignore')
    w = csv.DictWriter(f, listado, extrasaction='raise')
#    w.writeheader()
    w.writerow(data)
#    print (data)



