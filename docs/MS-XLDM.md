**\[MS-XLDM\]:**

**Spreadsheet Data Model File Format**

Intellectual Property Rights Notice for Open Specifications Documentation

- **Technical Documentation.** Microsoft publishes Open Specifications documentation ("this documentation") for protocols, file formats, data portability, computer languages, and standards support. Additionally, overview documents cover inter-protocol relationships and interactions.
- **Copyrights**. This documentation is covered by Microsoft copyrights. Regardless of any other terms that are contained in the terms of use for the Microsoft website that hosts this documentation, you can make copies of it in order to develop implementations of the technologies that are described in this documentation and can distribute portions of it in your implementations that use these technologies or in your documentation as necessary to properly document the implementation. You can also distribute in your implementation, with or without modification, any schemas, IDLs, or code samples that are included in the documentation. This permission also applies to any documents that are referenced in the Open Specifications documentation.
- **No Trade Secrets**. Microsoft does not claim any trade secret rights in this documentation.
- **Patents**. Microsoft has patents that might cover your implementations of the technologies described in the Open Specifications documentation. Neither this notice nor Microsoft's delivery of this documentation grants any licenses under those patents or any other Microsoft patents. However, a given Open Specifications document might be covered by the Microsoft [Open Specifications Promise](https://go.microsoft.com/fwlink/?LinkId=214445) or the [Microsoft Community Promise](https://go.microsoft.com/fwlink/?LinkId=214448). If you would prefer a written license, or if the technologies described in this documentation are not covered by the Open Specifications Promise or Community Promise, as applicable, patent licenses are available by contacting [iplg@microsoft.com](mailto:iplg@microsoft.com).
- **License Programs**. To see all of the protocols in scope under a specific license program and the associated patents, visit the [Patent Map](https://aka.ms/AA9ufj8).
- **Trademarks**. The names of companies and products contained in this documentation might be covered by trademarks or similar intellectual property rights. This notice does not grant any licenses under those rights. For a list of Microsoft trademarks, visit [www.microsoft.com/trademarks](https://www.microsoft.com/trademarks).
- **Fictitious Names**. The example companies, organizations, products, domain names, email addresses, logos, people, places, and events that are depicted in this documentation are fictitious. No association with any real company, organization, product, domain name, email address, logo, person, place, or event is intended or should be inferred.

**Reservation of Rights**. All other rights are reserved, and this notice does not grant any rights other than as specifically described above, whether by implication, estoppel, or otherwise.

**Tools**. The Open Specifications documentation does not require the use of Microsoft programming tools or programming environments in order for you to develop an implementation. If you have access to Microsoft programming tools and environments, you are free to take advantage of them. Certain Open Specifications documents are intended for use in conjunction with publicly available standards specifications and network programming art and, as such, assume that the reader either is familiar with the aforementioned material or has immediate access to it.

**Support.** For questions and support, please contact [dochelp@microsoft.com](mailto:dochelp@microsoft.com).

**Revision Summary**

| Date       | Revision History | Revision Class | Comments                                                                     |
| ---------- | ---------------- | -------------- | ---------------------------------------------------------------------------- |
| 1/20/2012  | 0.1              | New            | Released new document.                                                       |
| 4/11/2012  | 0.1              | None           | No changes to the meaning, language, or formatting of the technical content. |
| 7/16/2012  | 0.1              | None           | No changes to the meaning, language, or formatting of the technical content. |
| 10/8/2012  | 1.0              | Major          | Significantly changed the technical content.                                 |
| 2/11/2013  | 2.0              | Major          | Significantly changed the technical content.                                 |
| 7/30/2013  | 2.1              | Minor          | Clarified the meaning of the technical content.                              |
| 11/18/2013 | 2.1              | None           | No changes to the meaning, language, or formatting of the technical content. |
| 2/10/2014  | 2.1              | None           | No changes to the meaning, language, or formatting of the technical content. |
| 4/30/2014  | 2.2              | Minor          | Clarified the meaning of the technical content.                              |
| 7/31/2014  | 2.3              | Minor          | Clarified the meaning of the technical content.                              |
| 10/30/2014 | 2.4              | Minor          | Clarified the meaning of the technical content.                              |
| 3/16/2015  | 3.0              | Major          | Significantly changed the technical content.                                 |
| 9/4/2015   | 4.0              | Major          | Significantly changed the technical content.                                 |
| 7/15/2016  | 4.0              | None           | No changes to the meaning, language, or formatting of the technical content. |
| 9/14/2016  | 4.0              | None           | No changes to the meaning, language, or formatting of the technical content. |
| 9/29/2016  | 4.0              | None           | No changes to the meaning, language, or formatting of the technical content. |
| 4/27/2018  | 5.0              | Major          | Significantly changed the technical content.                                 |
| 8/28/2018  | 6.0              | Major          | Significantly changed the technical content.                                 |
| 4/22/2021  | 7.0              | Major          | Significantly changed the technical content.                                 |
| 8/17/2021  | 8.0              | Major          | Significantly changed the technical content.                                 |
| 11/16/2021 | 8.1              | Minor          | Clarified the meaning of the technical content.                              |
| 11/15/2022 | 8.2              | Minor          | Clarified the meaning of the technical content.                              |
| 8/19/2025  | 8.3              | Minor          | Clarified the meaning of the technical content.                              |

Table of Contents

[1 Introduction 10](#_Toc206123721)

[1.1 Glossary 10](#_Toc206123722)

[1.2 References 12](#_Toc206123723)

[1.2.1 Normative References 12](#_Toc206123724)

[1.2.2 Informative References 13](#_Toc206123725)

[1.3 Overview 13](#_Toc206123726)

[1.4 Relationship to Protocols and Other Structures 13](#_Toc206123727)

[1.5 Applicability Statement 14](#_Toc206123728)

[1.6 Versioning and Localization 14](#_Toc206123729)

[1.7 Vendor-Extensible Fields 14](#_Toc206123730)

[2 Structures 15](#_Toc206123731)

[2.1 Storage Format of the Stream 15](#_Toc206123732)

[2.1.1 Spreadsheet Data Model Header 15](#_Toc206123733)

[2.1.1.1 Byte Order Mark 16](#_Toc206123734)

[2.1.1.2 Stream Storage Signature 16](#_Toc206123735)

[2.1.1.3 BackupLogHeaderType 16](#_Toc206123736)

[2.1.2 Files Section 17](#_Toc206123737)

[2.1.2.1 Partitions 17](#_Toc206123738)

[2.1.2.1.1 SdfPartitionType 18](#_Toc206123739)

[2.1.2.2 File Stream Format 18](#_Toc206123740)

[2.1.2.2.1 File End Markers 19](#_Toc206123741)

[2.1.2.2.1.1 CRC Marker 19](#_Toc206123742)

[2.1.2.3 Log File 19](#_Toc206123743)

[2.1.2.3.1 SdfBackupLogType 19](#_Toc206123744)

[2.1.2.3.1.1 SdfBackupLogCollationsType 20](#_Toc206123745)

[2.1.2.3.1.2 SdfBackupLogLanguagesType 21](#_Toc206123746)

[2.1.2.3.1.3 SdfFileGroupsType 21](#_Toc206123747)

[2.1.2.3.1.3.1 SdfFileGroupType 21](#_Toc206123748)

[2.1.2.3.1.3.1.1 SdfFileGroupClassEnum 22](#_Toc206123749)

[2.1.2.3.1.3.1.2 SdfFileListType 23](#_Toc206123750)

[2.1.2.3.1.3.1.3 SdfFileListBackupFileType 23](#_Toc206123751)

[2.1.2.3.1.4 WriteEnum 23](#_Toc206123752)

[2.1.2.4 CryptKey.bin File 24](#_Toc206123753)

[2.1.2.4.1 CryptKey.bin File Format 24](#_Toc206123754)

[2.1.2.4.1.1 CryptKey.bin Structures 24](#_Toc206123755)

[2.1.2.4.1.1.1 CryptKeyHeader 24](#_Toc206123756)

[2.1.2.4.1.1.2 Key BLOB 26](#_Toc206123757)

[2.1.2.4.1.1.2.1 PUBLICKEYSTRUC 26](#_Toc206123758)

[2.1.2.4.1.1.3 CryptKeyTrailer 27](#_Toc206123759)

[2.1.2.4.2 Creating an Exponent-of-One Private Key 27](#_Toc206123760)

[2.1.3 Virtual Directory 29](#_Toc206123761)

[2.1.3.1 VirtualDirectoryType 30](#_Toc206123762)

[2.1.3.2 VirtualDirectoryBackupFileType 30](#_Toc206123763)

[2.2 File Name Generation 30](#_Toc206123764)

[2.2.1 Top-Level Files 31](#_Toc206123765)

[2.2.2 Database Folder 31](#_Toc206123766)

[2.2.3 Database Folder Contents 31](#_Toc206123767)

[2.2.3.1 Data Source View Definition File 31](#_Toc206123768)

[2.2.3.2 Cube Definition File 32](#_Toc206123769)

[2.2.3.3 Cube Folder 32](#_Toc206123770)

[2.2.3.3.1 Cube Folder Folders 32](#_Toc206123771)

[2.2.3.3.1.1 Measure Group Folder 32](#_Toc206123772)

[2.2.3.3.1.1.1 Measure Group Folder Folders 32](#_Toc206123773)

[2.2.3.3.1.1.1.1 Partition Folder Files 33](#_Toc206123774)

[2.2.3.3.1.1.2 Measure Group Folder Files 33](#_Toc206123775)

[2.2.3.3.2 Cube Folder Files 33](#_Toc206123776)

[2.2.3.3.2.1 Cube Information File 33](#_Toc206123777)

[2.2.3.3.2.2 MDX Script Metadata File 33](#_Toc206123778)

[2.2.3.3.2.3 Measure Group Metadata File 34](#_Toc206123779)

[2.2.3.4 Data Source Definition File 34](#_Toc206123780)

[2.2.3.5 Data Source Folder 34](#_Toc206123781)

[2.2.3.6 Dimension Definition File 34](#_Toc206123782)

[2.2.3.7 Dimension Folder 35](#_Toc206123783)

[2.2.3.7.1 Metadata Files 35](#_Toc206123784)

[2.2.3.7.1.1 Table Metadata Files 35](#_Toc206123785)

[2.2.3.7.1.2 Table Information File 35](#_Toc206123786)

[2.2.3.7.1.3 Table Relationship File 35](#_Toc206123787)

[2.2.3.7.1.4 Column Hierarchy Files 36](#_Toc206123788)

[2.2.3.7.1.5 User Hierarchy Metadata File 36](#_Toc206123789)

[2.2.3.7.2 Data Files 36](#_Toc206123790)

[2.2.3.7.2.1 Column Data Files 36](#_Toc206123791)

[2.2.3.7.2.2 Table Relationship Index File 36](#_Toc206123792)

[2.2.3.7.2.3 Column Hierarchy Position-to-Identifier File 37](#_Toc206123793)

[2.2.3.7.2.4 Column Hierarchy Identifier-to-Position File 37](#_Toc206123794)

[2.2.3.7.2.5 Column Hierarchy Hash Table 37](#_Toc206123795)

[2.2.3.7.2.6 Column Hierarchy Dictionary 37](#_Toc206123796)

[2.2.3.7.2.7 User Hierarchy Files 38](#_Toc206123797)

[2.2.3.7.2.7.1 Child Count File 38](#_Toc206123798)

[2.2.3.7.2.7.2 First Child Position File 38](#_Toc206123799)

[2.2.3.7.2.7.3 Parent Position File 38](#_Toc206123800)

[2.2.3.7.2.7.4 Multilevel Identifier File 39](#_Toc206123801)

[2.3 Storage of Data Values 39](#_Toc206123802)

[2.3.1 Column Data Storage 39](#_Toc206123803)

[2.3.1.1 File Layout for Column Data Storage Files 40](#_Toc206123804)

[2.3.1.1.1 General Layout of an .idf File 41](#_Toc206123805)

[2.3.1.1.2 General Layout of an .idf File That Uses Hybrid Compression 42](#_Toc206123806)

[2.3.1.1.3 Segment Size Limitations for .idf Files 43](#_Toc206123807)

[2.3.2 Column Data Dictionary 43](#_Toc206123808)

[2.3.2.1 File Layout for a Column Data Dictionary 44](#_Toc206123809)

[2.3.2.1.1 XM_TYPE_LONG and XM_TYPE_REAL Data Dictionary Files 45](#_Toc206123810)

[2.3.2.1.1.1 Required Hash Elements 45](#_Toc206123811)

[2.3.2.1.1.2 Vector of Values 46](#_Toc206123812)

[2.3.2.1.2 XM_TYPE_STRING Data Dictionary Files 46](#_Toc206123813)

[2.3.2.1.2.1 BLOBs and Base64 Encoding 47](#_Toc206123814)

[2.3.2.1.2.2 Required Hash Elements 48](#_Toc206123815)

[2.3.2.1.2.3 Dictionary Page Layout 48](#_Toc206123816)

[2.3.2.1.2.4 Dictionary String Store (Per Page) Information 49](#_Toc206123817)

[2.3.2.1.2.4.1 Uncompressed Page Case 51](#_Toc206123818)

[2.3.2.1.2.4.2 Compressed Page Case 52](#_Toc206123819)

[2.3.2.1.2.4.3 Second Mark (End of Page Marker) 54](#_Toc206123820)

[2.3.2.1.2.5 Dictionary Record Handles Vector 54](#_Toc206123821)

[2.3.2.1.3 Dictionary Structures, Enumerations, and Constants 55](#_Toc206123822)

[2.3.2.1.3.1 XM_TYPE Enumeration 55](#_Toc206123823)

[2.3.2.1.3.2 Page Size Limitations for an XM_TYPE_STRING Hash Data Dictionary 56](#_Toc206123824)

[2.3.2.1.3.3 Page Mask for an XM_TYPE_STRING Hash Data Dictionary 56](#_Toc206123825)

[2.3.2.1.3.4 Huffman Character Set Mode 56](#_Toc206123826)

[2.3.2.1.3.5 Record Handle Structures for an XM_TYPE_STRING Hash Data Dictionary 56](#_Toc206123827)

[2.3.3 Column Data Hierarchy Hash Index 57](#_Toc206123828)

[2.3.3.1 File Layout for Hash Index Files 57](#_Toc206123829)

[2.3.3.1.1 Required Elements for All Files That Use Hashing 58](#_Toc206123830)

[2.3.3.1.2 Required Elements for Hash Index Files 59](#_Toc206123831)

[2.3.3.1.2.1 Records and Hash Statistics 59](#_Toc206123832)

[2.3.3.1.2.2 Hash Bin Entries 62](#_Toc206123833)

[2.3.3.1.2.3 Overflow Hash Entries 63](#_Toc206123834)

[2.3.3.1.3 Hashing Algorithms 64](#_Toc206123835)

[2.3.3.1.4 Hash Structures, Enumerations and Constants 64](#_Toc206123836)

[2.3.3.1.4.1 XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT 64](#_Toc206123837)

[2.3.3.1.4.2 Hash Algorithm Enumeration and Constant 64](#_Toc206123838)

[2.3.3.1.4.3 Hash Bin Bucket Size Minimums 65](#_Toc206123839)

[2.3.3.1.4.4 HashBin Structure 65](#_Toc206123840)

[2.3.3.1.4.5 HashEntry Structure 66](#_Toc206123841)

[2.3.3.1.4.6 XM_HASH_ENTRY_COUNT_PER_BIN 69](#_Toc206123842)

[2.3.4 RowNumber Column 69](#_Toc206123843)

[2.3.4.1 File Layout for the RowNumber Column 70](#_Toc206123844)

[2.4 System-Generated Data Files 70](#_Toc206123845)

[2.4.1 Column Data Position-to-Identifier Mapping 70](#_Toc206123846)

[2.4.1.1 File Layout for Column Data Position-to-Identifier Mapping File 71](#_Toc206123847)

[2.4.2 Column Data Identifier-to-Position Mapping 71](#_Toc206123848)

[2.4.2.1 File Layout for Column Data Identifier-to-Position Mapping File 71](#_Toc206123849)

[2.4.3 Relationship Index 72](#_Toc206123850)

[2.4.3.1 File Layout for Relationship Index File 72](#_Toc206123851)

[2.4.4 User Hierarchy System-Generated Files 72](#_Toc206123852)

[2.4.4.1 User Hierarchy Child Count 73](#_Toc206123853)

[2.4.4.1.1 File Layout for User Hierarchy Child Count 74](#_Toc206123854)

[2.4.4.2 User Hierarchy First Child Position 74](#_Toc206123855)

[2.4.4.2.1 File Layout for User Hierarchy First Child Position 74](#_Toc206123856)

[2.4.4.3 User Hierarchy Multilevel Identifier 75](#_Toc206123857)

[2.4.4.3.1 File Layout for User Hierarchy Multilevel Identifier 75](#_Toc206123858)

[2.4.4.4 User Hierarchy Parent Position 75](#_Toc206123859)

[2.4.4.4.1 File Layout for User Hierarchy Parent Position 76](#_Toc206123860)

[2.5 Metadata Files 76](#_Toc206123861)

[2.5.1 XMObject Document Node Element 76](#_Toc206123862)

[2.5.1.1 XMObjectPropertiesType 77](#_Toc206123863)

[2.5.1.2 XMObjectMembersType 77](#_Toc206123864)

[2.5.1.3 XMObjectCollectionsType 78](#_Toc206123865)

[2.5.1.4 XMObjectDataObjectsType 78](#_Toc206123866)

[2.5.1.5 XMObjectMemberType 79](#_Toc206123867)

[2.5.1.6 XMObjectCollectionType 79](#_Toc206123868)

[2.5.1.7 XMObjectDataObjectType 80](#_Toc206123869)

[2.5.1.8 XMObjectMemberNameEnum 80](#_Toc206123870)

[2.5.1.9 XMObjectCollectionNameEnum 81](#_Toc206123871)

[2.5.1.10 XMObjectClassNameEnum 81](#_Toc206123872)

[2.5.2 XMObject Definitions by class Attribute 86](#_Toc206123873)

[2.5.2.1 XMObject class="XMSimpleTable" 87](#_Toc206123874)

[2.5.2.1.1 XMSimpleTablePropertiesType 87](#_Toc206123875)

[2.5.2.1.2 XMSimpleTableMembersType 88](#_Toc206123876)

[2.5.2.1.2.1 XMSimpleTableMemberType 88](#_Toc206123877)

[2.5.2.1.2.2 XMSimpleTableMemberNameEnum 89](#_Toc206123878)

[2.5.2.1.2.3 XMSimpleTableXMObjectMemberClassNameEnum 89](#_Toc206123879)

[2.5.2.1.3 XMSimpleTableCollectionsType 90](#_Toc206123880)

[2.5.2.1.3.1 XMSimpleTableCollectionType 90](#_Toc206123881)

[2.5.2.1.3.2 XMSimpleTableCollectionNameEnum 91](#_Toc206123882)

[2.5.2.1.3.3 XMSimpleTableXMObjectCollectionClassNameEnum 92](#_Toc206123883)

[2.5.2.2 XMObject class="XMTableStats" 92](#_Toc206123884)

[2.5.2.2.1 XMTableStatsPropertiesType 93](#_Toc206123885)

[2.5.2.3 XMObject class="XMRawColumn" 93](#_Toc206123886)

[2.5.2.3.1 XMRawColumnPropertiesType 94](#_Toc206123887)

[2.5.2.3.2 XMRawColumnMembersType 95](#_Toc206123888)

[2.5.2.3.2.1 XMRawColumnMemberType 96](#_Toc206123889)

[2.5.2.3.2.2 XMRawColumnMemberNameEnum 97](#_Toc206123890)

[2.5.2.3.2.3 XMRawColumnXMObjectMemberClassNameEnum 97](#_Toc206123891)

[2.5.2.3.3 XMRawColumnCollectionsType 97](#_Toc206123892)

[2.5.2.3.3.1 XMRawColumnCollectionType 98](#_Toc206123893)

[2.5.2.3.4 XMRawColumnDataObjectsType 98](#_Toc206123894)

[2.5.2.3.4.1 XMRawColumnDataObjectType 98](#_Toc206123895)

[2.5.2.3.4.2 XMRawColumnXMObjectDataObjectClassNameEnum 99](#_Toc206123896)

[2.5.2.4 XMObject class="XMRelationship" 100](#_Toc206123897)

[2.5.2.4.1 XMRelationshipPropertiesType 100](#_Toc206123898)

[2.5.2.4.2 XMRelationshipDataObjectsType 100](#_Toc206123899)

[2.5.2.4.3 XMRelationshipDataObjectType 101](#_Toc206123900)

[2.5.2.4.4 XMRelationshipXMDataObjectXMObjectClassNameEnum 101](#_Toc206123901)

[2.5.2.5 XMObject class="XMRelationshipIndexSparseDIDs" 102](#_Toc206123902)

[2.5.2.5.1 XMRelationshipIndexSparseDIDsPropertiesType 102](#_Toc206123903)

[2.5.2.6 XMObject class="XMRelationshipIndexDenseDIDs" 102](#_Toc206123904)

[2.5.2.6.1 XMRelationshipIndexDenseDIDsPropertiesType 103](#_Toc206123905)

[2.5.2.7 XMObject class="XMRelationshipIndex123DIDs" 103](#_Toc206123906)

[2.5.2.8 XMObject class="XMColumnStats" 103](#_Toc206123907)

[2.5.2.8.1 XMColumnStatsPropertiesType 104](#_Toc206123908)

[2.5.2.9 XMObject class="XMHierarchy" 107](#_Toc206123909)

[2.5.2.9.1 XMHierarchyPropertiesType 107](#_Toc206123910)

[2.5.2.10 XMObject class="XMUserHierarchy" 108](#_Toc206123911)

[2.5.2.10.1 XMUserHierarchyPropertiesType 109](#_Toc206123912)

[2.5.2.11 XMObject class="XMHierarchyDataID2PositionHashIndex" 109](#_Toc206123913)

[2.5.2.12 XMObject class="XMColumnSegment" 110](#_Toc206123914)

[2.5.2.12.1 XMColumnSegmentPropertiesType 110](#_Toc206123915)

[2.5.2.12.2 XMColumnSegmentMembersType 111](#_Toc206123916)

[2.5.2.12.2.1 XMColumnSegmentMemberType 111](#_Toc206123917)

[2.5.2.12.2.2 XMColumnSegmentMemberNameEnum 112](#_Toc206123918)

[2.5.2.12.2.3 XMColumnSegmentXMObjectMemberClassNameEnum 112](#_Toc206123919)

[2.5.2.13 XMObject class="XMPartition" 114](#_Toc206123920)

[2.5.2.13.1 XMPartitionPropertiesType 114](#_Toc206123921)

[2.5.2.14 XMObject class="XMMultiPartSegmentMap" 115](#_Toc206123922)

[2.5.2.14.1 XMMultiPartSegmentMapPropertiesType 115](#_Toc206123923)

[2.5.2.14.2 XMMultiPartSegmentMapCollectionsType 115](#_Toc206123924)

[2.5.2.14.3 XMMultiPartSegmentMapCollectionType 116](#_Toc206123925)

[2.5.2.14.3.1 XMMultiPartSegmentMapXMObjectCollectionClassNameEnum 116](#_Toc206123926)

[2.5.2.15 XMObject class="XMSegment1Map" 117](#_Toc206123927)

[2.5.2.15.1 XMSegment1MapPropertiesType 117](#_Toc206123928)

[2.5.2.16 XMObject class="XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;" 117](#_Toc206123929)

[2.5.2.16.1 XMSegmentEqualMapEx_PropertiesType 118](#_Toc206123930)

[2.5.2.17 XMObject class="XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;" 118](#_Toc206123931)

[2.5.2.18 XMObject class="XMValueDataDictionary&lt;XM_Long&gt;" 119](#_Toc206123932)

[2.5.2.18.1 PropertiesValueDictionaryType 119](#_Toc206123933)

[2.5.2.19 XMObject class="XMValueDataDictionary&lt;XM_Real&gt;" 120](#_Toc206123934)

[2.5.2.20 XMObject class="XMHashDataDictionary&lt;XM_Real&gt;" 120](#_Toc206123935)

[2.5.2.20.1 HashDictionaryAttributeGroup 120](#_Toc206123936)

[2.5.2.20.2 PropertiesHashDictionaryRealType 121](#_Toc206123937)

[2.5.2.21 XMObject class="XMHashDataDictionary&lt;XM_Long&gt;" 121](#_Toc206123938)

[2.5.2.21.1 PropertiesHashDictionaryLongType 121](#_Toc206123939)

[2.5.2.22 XMObject class="XMHashDataDictionary&lt;XM_String&gt;" 122](#_Toc206123940)

[2.5.2.22.1 PropertiesHashDictionaryStringType 122](#_Toc206123941)

[2.5.2.23 XMObject class="XMRENoSplitCompressionInfo&lt;1&gt;" 123](#_Toc206123942)

[2.5.2.23.1 XMRENoSplitCompressionInfoPropertiesType 123](#_Toc206123943)

[2.5.2.24 XMObject class="XMRENoSplitCompressionInfo&lt;2&gt;" 124](#_Toc206123944)

[2.5.2.25 XMObject class="XMRENoSplitCompressionInfo&lt;3&gt; 124](#_Toc206123945)

[2.5.2.26 XMObject class="XMRENoSplitCompressionInfo&lt;4&gt; 124](#_Toc206123946)

[2.5.2.27 XMObject class="XMRENoSplitCompressionInfo&lt;5&gt; 125](#_Toc206123947)

[2.5.2.28 XMObject class="XMRENoSplitCompressionInfo&lt;6&gt; 125](#_Toc206123948)

[2.5.2.29 XMObject class="XMRENoSplitCompressionInfo&lt;7&gt; 126](#_Toc206123949)

[2.5.2.30 XMObject class="XMRENoSplitCompressionInfo&lt;8&gt; 126](#_Toc206123950)

[2.5.2.31 XMObject class="XMRENoSplitCompressionInfo&lt;9&gt; 126](#_Toc206123951)

[2.5.2.32 XMObject class="XMRENoSplitCompressionInfo&lt;10&gt; 127](#_Toc206123952)

[2.5.2.33 XMObject class="XMRENoSplitCompressionInfo&lt;12&gt; 127](#_Toc206123953)

[2.5.2.34 XMObject class="XMRENoSplitCompressionInfo&lt;16&gt; 128](#_Toc206123954)

[2.5.2.35 XMObject class="XMRENoSplitCompressionInfo&lt;21&gt; 128](#_Toc206123955)

[2.5.2.36 XMObject class="XMRENoSplitCompressionInfo&lt;32&gt;" 128](#_Toc206123956)

[2.5.2.37 XMObject class="XM123CompressionInfo" 129](#_Toc206123957)

[2.5.2.38 XMRLECompressionInfo 129](#_Toc206123958)

[2.5.2.38.1 XMRLECompressionInfoPropertiesType 130](#_Toc206123959)

[2.5.2.39 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>" 130](#_Toc206123960)

[2.5.2.39.1 XMHybridRLECompressionInfoMembersType 130](#_Toc206123961)

[2.5.2.39.2 XMHybridRLECompressionInfoMemberType 131](#_Toc206123962)

[2.5.2.39.3 XMHybridRLECompressionInfoMemberNameEnum 132](#_Toc206123963)

[2.5.2.39.4 XMHybridRLECompressionInfoXMObjectMemberClassNameEnum 132](#_Toc206123964)

[2.5.2.40 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>" 133](#_Toc206123965)

[2.5.2.41 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>" 134](#_Toc206123966)

[2.5.2.42 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>" 134](#_Toc206123967)

[2.5.2.43 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>" 135](#_Toc206123968)

[2.5.2.44 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>" 135](#_Toc206123969)

[2.5.2.45 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>" 136](#_Toc206123970)

[2.5.2.46 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>" 136](#_Toc206123971)

[2.5.2.47 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>" 137](#_Toc206123972)

[2.5.2.48 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>" 137](#_Toc206123973)

[2.5.2.49 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>" 138](#_Toc206123974)

[2.5.2.50 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>" 138](#_Toc206123975)

[2.5.2.51 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>" 139](#_Toc206123976)

[2.5.2.52 XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>" 139](#_Toc206123977)

[2.5.2.53 XMObject class="XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;" 140](#_Toc206123978)

[2.5.2.54 XMObject class="XMColumnSegmentStats" 140](#_Toc206123979)

[2.5.2.54.1 XMColumnSegmentStatsPropertiesType 140](#_Toc206123980)

[2.5.2.55 XMObject class="XMRawColumnPartitionDataObject" 141](#_Toc206123981)

[2.5.2.55.1 XMRawColumnPartitionDataObjectPropertiesType 141](#_Toc206123982)

[2.5.3 Contents of the .tbl.xml Files 142](#_Toc206123983)

[2.6 Model OLAP Files 142](#_Toc206123984)

[2.6.1 Load Element Document Node 142](#_Toc206123985)

[2.6.1.1 MajorObjectTabularModel 143](#_Toc206123986)

[2.6.1.2 ObjectReferenceTabularModel 144](#_Toc206123987)

[2.6.1.3 TabularModelElementsGroup Group 144](#_Toc206123988)

[2.6.2 DataSourceTabularModel 144](#_Toc206123989)

[2.6.3 DataSourceViewTabularModel 145](#_Toc206123990)

[2.6.4 DatabaseTabularModel 145](#_Toc206123991)

[2.6.5 CubeTabularModel 146](#_Toc206123992)

[2.6.6 DimensionTabularModel 147](#_Toc206123993)

[2.6.7 MeasureGroupTabularModel 147](#_Toc206123994)

[2.6.8 PartitionTabularModel 148](#_Toc206123995)

[2.6.9 MdxScriptTabularModel 149](#_Toc206123996)

[2.6.10 OLAP Information Files 149](#_Toc206123997)

[2.6.10.1 Partition Information File 149](#_Toc206123998)

[2.6.10.1.1 PartitionInformationType 150](#_Toc206123999)

[2.6.10.2 Dimension Information File 150](#_Toc206124000)

[2.6.10.2.1 DimensionInformationType 150](#_Toc206124001)

[2.6.10.2.1.1 DimensionInformationPropertiesType 151](#_Toc206124002)

[2.6.10.2.1.1.1 DimensionInformationPropertyType 151](#_Toc206124003)

[2.6.10.2.1.1.2 DimensionInformationMapDataSetType 151](#_Toc206124004)

[2.6.10.3 Cube Information File 152](#_Toc206124005)

[2.6.10.3.1 CubeInformationType 152](#_Toc206124006)

[2.7 Compression 153](#_Toc206124007)

[2.7.1 XMRENoSplit Compression Algorithms 153](#_Toc206124008)

[2.7.1.1 XMRENoSplitCompressionInfo&lt;1&gt; 153](#_Toc206124009)

[2.7.1.2 XMRENoSplitCompressionInfo&lt;2&gt; 154](#_Toc206124010)

[2.7.1.3 XMRENoSplitCompressionInfo&lt;3&gt; 156](#_Toc206124011)

[2.7.1.4 XMRENoSplitCompressionInfo&lt;4&gt; 157](#_Toc206124012)

[2.7.1.5 XMRENoSplitCompressionInfo&lt;5&gt; 159](#_Toc206124013)

[2.7.1.6 XMRENoSplitCompressionInfo&lt;6&gt; 160](#_Toc206124014)

[2.7.1.7 XMRENoSplitCompressionInfo&lt;7&gt; 162](#_Toc206124015)

[2.7.1.8 XMRENoSplitCompressionInfo&lt;8&gt; 164](#_Toc206124016)

[2.7.1.9 XMRENoSplitCompressionInfo&lt;9&gt; 165](#_Toc206124017)

[2.7.1.10 XMRENoSplitCompressionInfo&lt;10&gt; 166](#_Toc206124018)

[2.7.1.11 XMRENoSplitCompressionInfo&lt;12&gt; 168](#_Toc206124019)

[2.7.1.12 XMRENoSplitCompressionInfo&lt;16&gt; 169](#_Toc206124020)

[2.7.1.13 XMRENoSplitCompressionInfo&lt;21&gt; 170](#_Toc206124021)

[2.7.1.14 XMRENoSplitCompressionInfo&lt;32&gt; 172](#_Toc206124022)

[2.7.2 XM123 Compression Algorithm 173](#_Toc206124023)

[2.7.2.1 XM123CompressionInfo 173](#_Toc206124024)

[2.7.3 XMHybridRLE Compression Algorithms 173](#_Toc206124025)

[2.7.3.1 Conceptual Overview of RLE Entries and Bit-Packing Entries 174](#_Toc206124026)

[2.7.3.2 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;> 177](#_Toc206124027)

[2.7.3.3 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;> 178](#_Toc206124028)

[2.7.3.4 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;> 179](#_Toc206124029)

[2.7.3.5 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;> 180](#_Toc206124030)

[2.7.3.6 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;> 181](#_Toc206124031)

[2.7.3.7 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;> 183](#_Toc206124032)

[2.7.3.8 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;> 184](#_Toc206124033)

[2.7.3.9 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;> 185](#_Toc206124034)

[2.7.3.10 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;> 185](#_Toc206124035)

[2.7.3.11 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;> 186](#_Toc206124036)

[2.7.3.12 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;> 188](#_Toc206124037)

[2.7.3.13 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;> 189](#_Toc206124038)

[2.7.3.14 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;> 189](#_Toc206124039)

[2.7.3.15 XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;> 190](#_Toc206124040)

[2.7.3.16 XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt; 190](#_Toc206124041)

[2.7.4 Huffman Compression 191](#_Toc206124042)

[2.7.4.1 Huffman Implementation Constraints 192](#_Toc206124043)

[2.7.4.1.1 Classical Unbalanced Huffman Tree 192](#_Toc206124044)

[2.7.4.1.2 Minimum and Maximum Codeword Sizes 192](#_Toc206124045)

[2.7.4.1.3 Huffman Alphabet Size 192](#_Toc206124046)

[2.7.4.1.4 Single and Multiple Character Set Modes 193](#_Toc206124047)

[2.7.4.1.5 Huffman Information Provided in an XM_TYPE_STRING Dictionary 194](#_Toc206124048)

[2.7.4.2 Conceptual Overview of a Huffman Tree 195](#_Toc206124049)

[2.7.5 Xpress Compression 196](#_Toc206124050)

[3 Structure Examples 197](#_Toc206124051)

[3.1 tbl.xml Metadata File 197](#_Toc206124052)

[3.2 Multiple-Segment Column Data .idf File 209](#_Toc206124053)

[3.3 Dictionary File 211](#_Toc206124054)

[4 Security 214](#_Toc206124055)

[4.1 Security Considerations for Implementers 214](#_Toc206124056)

[4.2 Index of Security Fields 214](#_Toc206124057)

[5 Appendix A: Compression Mask for XMRENoSplit Compression Algorithms 216](#_Toc206124058)

[6 Appendix B: Product Behavior 232](#_Toc206124059)

[7 Change Tracking 234](#_Toc206124060)

[8 Index 235](#_Toc206124061)

# Introduction

The Spreadsheet Data Model File Format defines a binary file format that is used to store a portion of a tabular data model, which represents tables, data, and relationships, within a containing spreadsheet file format.

Sections 1.7 and 2 of this specification are normative. All other sections and examples in this specification are informative.

## Glossary

This document uses the following terms:

**ASCII**: The American Standard Code for Information Interchange (ASCII) is an 8-bit character-encoding scheme based on the English alphabet. ASCII codes represent text in computers, communications equipment, and other devices that work with text. ASCII refers to a single 8-bit ASCII character or an array of 8-bit ASCII characters with the high bit of each character set to zero.

**assembly**: A collection of one or more files that is versioned and deployed as a unit. An assembly is the primary building block of a .NET Framework application. All managed types and resources are contained within an assembly and are marked either as accessible only within the assembly or as accessible from code in other assemblies. Assemblies also play a key role in security. The code access security system uses information about an assembly to determine the set of permissions that is granted to code in the assembly.

**Augmented Backus-Naur Form (ABNF)**: A modified version of Backus-Naur Form (BNF), commonly used by Internet specifications. ABNF notation balances compactness and simplicity with reasonable representational power. ABNF differs from standard BNF in its definitions and uses of naming rules, repetition, alternatives, order-independence, and value ranges. For more information, see [\[RFC5234\]](https://go.microsoft.com/fwlink/?LinkId=123096).

**base64 encoding**: A binary-to-text encoding scheme whereby an arbitrary sequence of bytes is converted to a sequence of printable [**ASCII**](#gt_79fa85ca-ac61-467c-b819-e97dc1a7a599) characters, as described in [\[RFC4648\]](https://go.microsoft.com/fwlink/?LinkId=90487).

**binary large object (BLOB)**: A discrete packet of data that is stored in a database and is treated as a sequence of uninterpreted bytes.

**calculated column**: A column in a table that contains a formula that is copied automatically to each record in the column.

**character set**: A mapping between the characters of a written language and the values that are used to represent those characters to a computer.

**cube**: A set of data that is organized and summarized into a multidimensional structure that is defined by a set of dimensions and measures.

**cyclic redundancy check (CRC)**: An algorithm used to produce a checksum (a small, fixed number of bits) against a block of data, such as a packet of network traffic or a block of a computer file. The CRC is a broad class of functions used to detect errors after transmission or storage. A CRC is designed to catch random errors, as opposed to intentional errors. If errors might be introduced by a motivated and intelligent adversary, a cryptographic hash function has to be used instead.

**data source**: A database, web service, disk, file, or other collection of information from which data is queried or submitted. Supported data sources vary based on application and data provider.

**globally unique identifier (GUID)**: A term used interchangeably with [**universally unique identifier (UUID)**](#gt_c4813fc3-b2e5-4aa3-bde7-421d950d68d3) in Microsoft protocol technical documents (TDs). Interchanging the usage of these terms does not imply or require a specific algorithm or mechanism to generate the value. Specifically, the use of this term does not imply or require that the algorithms described in [\[RFC4122\]](https://go.microsoft.com/fwlink/?LinkId=90460) or [\[C706\]](https://go.microsoft.com/fwlink/?LinkId=89824) have to be used for generating the GUID. See also universally unique identifier (UUID).

**hash**: A fixed-size result that is obtained by applying a one-way mathematical function, which is sometimes referred to as a hash algorithm, to an arbitrary amount of data. If the input data changes, the hash also changes. The hash can be used in many operations, including authentication and digital signing.

**hierarchy**: A logical tree structure that organizes the members of a dimension such that each member has one parent member and zero or more child members.

**hybrid compression**: A type of data compression that uses a combination of run length encoding and bit-wise compression.

**intrinsic hierarchy**: A hierarchical data structure that is automatically formed from every single column of data in a spreadsheet and contains one node for every unique data value within each column.

**language code identifier (LCID)**: A 32-bit number that identifies the user interface human language dialect or variation that is supported by an application or a client computer.

**little-endian**: Multiple-byte values that are byte-ordered with the least significant byte stored in the memory location with the lowest address.

**measure group**: A collection of related measures in a [**cube**](#gt_a0c8d97b-322c-4117-8525-37e5f26751e7) that derive from a single fact table, typically in a data source view.

**Multidimensional Expressions (MDX)**: A syntax that is used for defining multidimensional objects, and for querying and manipulating multidimensional data.

**OLAP cube**: A data structure that aggregates [**Online Analytical Processing (OLAP)**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) measures by OLAP levels and OLAP hierarchies. An OLAP cube combines several OLAP hierarchies, such as time, geography, and product lines, with OLAP measures, such as sales or inventory figures.

**OLE DB**: A set of interfaces that are based on the Component Object Model (COM) programming model and expose data from a variety of sources. These interfaces support the amount of Database Management System (DBMS) functionality that is appropriate for a data store and they enable a data store to share data.

**Online Analytical Processing (OLAP)**: A technology that uses multidimensional structures to provide access to data for analysis. The source data for OLAP is stored in data warehouses in a relational database. See also [**cube**](#gt_a0c8d97b-322c-4117-8525-37e5f26751e7).

**partition**: An area within a shared services database, such as an area that isolates different tenants within a service, or the process of creating such an area in a shared services database.

**segment map**: A data structure that specifies which particular segment contains each individual range of data in a spreadsheet.

**table**: A list that is defined in a workbook.

**tabular data model**: A representation of tables, data, and relationships. It has to contain at least one table, and can contain definitions for relationships between the table's columns, hierarchical relationships between columns, or calculated columns. It can also contain data values, or connection information to retrieve data values from external locations.

**Unicode**: A character encoding standard developed by the Unicode Consortium that represents almost all of the written languages of the world. The [**Unicode**](#gt_c305d0ab-8b94-461a-bd76-13b40cb8c4d8) standard [\[UNICODE5.0.0/2007\]](https://go.microsoft.com/fwlink/?LinkId=154659) provides three forms (UTF-8, UTF-16, and UTF-32) and seven schemes (UTF-8, UTF-16, UTF-16 BE, UTF-16 LE, UTF-32, UTF-32 LE, and UTF-32 BE).

**universally unique identifier (UUID)**: A 128-bit value. UUIDs can be used for multiple purposes, from tagging objects with an extremely short lifetime, to reliably identifying very persistent objects in cross-process communication such as client and server interfaces, manager entry-point vectors, and RPC objects. UUIDs are highly likely to be unique. UUIDs are also known as [**globally unique identifiers (GUIDs)**](#gt_f49694cc-c350-462d-ab8e-816f0103c6c1) and these terms are used interchangeably in the Microsoft protocol technical documents (TDs). Interchanging the usage of these terms does not imply or require a specific algorithm or mechanism to generate the UUID. Specifically, the use of this term does not imply or require that the algorithms described in \[RFC4122\] or \[C706\] has to be used for generating the UUID.

**value encoding**: A method of converting data into decimal numbers greater than zero by assigning each data item a unique numeric identifier. The identifier is then used in place of the data item in the data stream or storage medium.

**XML document**: A document object that is well formed, as described in [\[XML10/5\]](https://go.microsoft.com/fwlink/?LinkId=221669), and might be valid. An XML document has a logical structure that is composed of declarations, elements, comments, character references, and processing instructions. It also has a physical structure that is composed of entities, starting with the root, or document, entity.

**XML element**: An XML structure that typically consists of a start tag, an end tag, and the information between those tags. Elements can have attributes and can contain other elements.

**XML schema definition (XSD)**: The World Wide Web Consortium (W3C) standard language that is used in defining XML schemas. Schemas are useful for enforcing structure and constraining the types of data that can be used validly within other XML documents. XML schema definition refers to the fully specified and currently recommended standard for use in authoring XML schemas.

**MAY, SHOULD, MUST, SHOULD NOT, MUST NOT:** These terms (in all caps) are used as defined in [\[RFC2119\]](https://go.microsoft.com/fwlink/?LinkId=90317). All statements of optional behavior use either MAY, SHOULD, or SHOULD NOT.

## References

Links to a document in the Microsoft Open Specifications library point to the correct section in the most recently published version of the referenced document. However, because individual documents in the library are not updated at the same time, the section numbers in the documents may not match. You can confirm the correct section numbering by checking the [Errata](https://go.microsoft.com/fwlink/?linkid=850906).

### Normative References

We conduct frequent surveys of the normative references to assure their continued availability. If you have any issue with finding a normative reference, please contact [dochelp@microsoft.com](mailto:dochelp@microsoft.com). We will assist you in finding the relevant information.

\[MS-SSAS\] Microsoft Corporation, "[SQL Server Analysis Services Protocol](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9)".

\[MS-WUSP\] Microsoft Corporation, "[Windows Update Services: Client-Server Protocol](%5bMS-WUSP%5d.pdf#Section_b8a2ad1d11c44b64a2cc12771fcb079b)".

\[RFC2119\] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997, [https://www.rfc-editor.org/info/rfc2119](https://go.microsoft.com/fwlink/?LinkId=90317)

\[RFC5234\] Crocker, D., Ed., and Overell, P., "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008, [https://www.rfc-editor.org/info/rfc5234](https://go.microsoft.com/fwlink/?LinkId=123096)

\[XMLSCHEMA1\] Thompson, H., Beech, D., Maloney, M., and Mendelsohn, N., Eds., "XML Schema Part 1: Structures", W3C Recommendation, May 2001, [https://www.w3.org/TR/2001/REC-xmlschema-1-20010502/](https://go.microsoft.com/fwlink/?LinkId=90608)

\[XMLSCHEMA2\] Biron, P.V., Ed. and Malhotra, A., Ed., "XML Schema Part 2: Datatypes", W3C Recommendation, May 2001, [https://www.w3.org/TR/2001/REC-xmlschema-2-20010502/](https://go.microsoft.com/fwlink/?LinkId=90610)

### Informative References

\[MS-OFFMACRO2\] Microsoft Corporation, "[Office Macro-Enabled File Format Version 2](%5bMS-OFFMACRO2%5d.pdf#Section_802a7c98c80241c68a13987457098d8f)".

\[MS-OFFMACRO\] Microsoft Corporation, "[Office Macro-Enabled File Format](%5bMS-OFFMACRO%5d.pdf#Section_86fa5ba869cf41648559c5af66d2990e)".

\[MS-SPO\] Microsoft Corporation, "[SharePoint Protocols Overview](%5bMS-SPO%5d.pdf#Section_a9173bd4232741ac8ecbdc20e0ab7d92)".

\[MS-XLSB\] Microsoft Corporation, "[Excel (.xlsb) Binary File Format](%5bMS-XLSB%5d.pdf#Section_acc8aa921f02416799f584f9f676b95a)".

\[MS-XLSX\] Microsoft Corporation, "[Excel (.xlsx) Extensions to the Office Open XML SpreadsheetML File Format](%5bMS-XLSX%5d.pdf#Section_2c5dee00eff24b2292b60738acd4475e)".

\[MSDN-AnalysisServices\] Microsoft Corporation, "Managing Backing Up and Restoring (Analysis Services)", [http://msdn.microsoft.com/en-us/library/ms174874.aspx](https://go.microsoft.com/fwlink/?LinkId=231042)

\[MSDN-CRYPTO\] Microsoft Corporation, "Cryptography Reference", [http://msdn.microsoft.com/en-us/library/aa380256.aspx](https://go.microsoft.com/fwlink/?LinkId=89984)

\[MSDOCS-PrivKeyBlobs\] Microsoft, "Private Key BLOBs", [https://learn.microsoft.com/en-us/windows/win32/seccrypto/base-provider-key-blobs#private-key-blobs](https://aka.ms/AAhrknm)

\[XML10\] World Wide Web Consortium, "Extensible Markup Language (XML) 1.0 (Third Edition)", February 2004, [http://www.w3.org/TR/2004/REC-xml-20040204/](https://go.microsoft.com/fwlink/?LinkId=90600)

## Overview

This file format, which is used to store a [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) file within a spreadsheet file, can contain one or more of the following types of metadata:

- A definition of a [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) for data that is stored in a [**table**](#gt_d3a7da8d-a597-4838-9756-25e30b640ba7). The data source can be a range of cells in a spreadsheet, one or more tables in a relational database, or a [**cube**](#gt_a0c8d97b-322c-4117-8525-37e5f26751e7) that is stored in an [**Online Analytical Processing (OLAP)**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) database.
- The relationships between the included tables, if any.
- A user-defined, hierarchical relationship among the columns of a table.
- Any [**calculated columns**](#gt_ec25719c-0814-4978-a7e7-f18111a9598d) that are created as a function of other, existing columns.

This file format can also include connection strings and passwords for accessing external data sources. Any data that is entered directly into the tabular data model-for example, data that is entered manually or by means of a cut-and-paste operation-can also be stored by this file format.

## Relationship to Protocols and Other Structures

This file format is hosted within the structures that are defined in the following references:

- [\[MS-XLSX\]](%5bMS-XLSX%5d.pdf#Section_2c5dee00eff24b2292b60738acd4475e) describes a spreadsheet file format.
- [\[MS-XLSB\]](%5bMS-XLSB%5d.pdf#Section_acc8aa921f02416799f584f9f676b95a) describes a spreadsheet file format.
- [\[MS-OFFMACRO\]](%5bMS-OFFMACRO%5d.pdf#Section_86fa5ba869cf41648559c5af66d2990e) describes a spreadsheet file format.
- [\[MS-OFFMACRO2\]](%5bMS-OFFMACRO2%5d.pdf#Section_802a7c98c80241c68a13987457098d8f) describes a spreadsheet file format.

This file format is related to the protocols that are defined in the following references:

- [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) describes the protocol for the [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) server on which the OLAP aspects of the metadata are derived. (The metadata that describes the data contained by this file format is based on both a [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) and OLAP.)
- [\[MSDN-AnalysisServices\]](https://go.microsoft.com/fwlink/?LinkId=231042) describes backup and restore operations that produce a file with the .abf extension. This structure is an .abf file.

Portions of this structure are stored as XML, as described in [\[XML10\]](https://go.microsoft.com/fwlink/?LinkId=90600).

## Applicability Statement

This structure is used to persist a file within a containing file, as described in [\[MS-XLSX\]](%5bMS-XLSX%5d.pdf#Section_2c5dee00eff24b2292b60738acd4475e), [\[MS-XLSB\]](%5bMS-XLSB%5d.pdf#Section_acc8aa921f02416799f584f9f676b95a), [\[MS-OFFMACRO\]](%5bMS-OFFMACRO%5d.pdf#Section_86fa5ba869cf41648559c5af66d2990e), or [\[MS-OFFMACRO2\]](%5bMS-OFFMACRO2%5d.pdf#Section_802a7c98c80241c68a13987457098d8f). This structure applies to the case where a user creates a [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) within a session by using spreadsheet software that produces such a containing file.

## Versioning and Localization

This document covers versioning issues in the following areas:

- **Structure Versions:** This document covers the following information:
  - The version of this structure is stored within the file. For more information, see section [2.1.2.3.1](#Section_35cdb4315b4149c8a2b9cc30083d1e4e)
  - Many of the [**XML elements**](#gt_a364f92c-0374-4568-b7f8-40bd74437dd5) are stamped with the provider version of the server that created an instance of this structure. For more information, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).
- **Localization:** This document covers the following information:
  - All the string values that are stored in the structure are [**Unicode**](#gt_c305d0ab-8b94-461a-bd76-13b40cb8c4d8) and hence support any language's Unicode characters.
  - [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) metadata objects support the user specification of a language and a collation. For more information, see section [2.6](#Section_6bd8ed6126234bcdbe1d8b6993c880f9).
  - This structure includes a collection of languages and a collection of collations. For more information, see section 2.1.2.3.1.

## Vendor-Extensible Fields

The [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) metadata objects have an **Annotations** collection, in which vendors can store vendor-specific information. For more details, see section [2.6](#Section_6bd8ed6126234bcdbe1d8b6993c880f9) and [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9).

# Structures

In the following XML schema definitions, the namespace prefix "xs" is defined as "<http://www.w3.org/2001/XMLSchema>".

## Storage Format of the Stream

All of the files that are generated by an instance of the Spreadsheet Data Model are formed into a stream and stored within a spreadsheet file. The format of the storage container is also referred to as the Spreadsheet Data Model File Format and is described in the remainder of this section.

The Spreadsheet Data Model file consists of a header that is followed by a partition marker that is then followed by all the files in the directory, with each file separated by a marker. These files are then followed by a backup log and a virtual directory that contains the file list and related information. The three major sections-Spreadsheet Data Model header; stream of files, including the Spreadsheet Data Model backup log file at the end and the partition information at the beginning; and Spreadsheet Data Model virtual directory-are all Spreadsheet Data Model page aligned and MUST be padded with zeros (if necessary) to meet page alignment requirements.

A Spreadsheet Data Model file page MUST be 4096 bytes. This definition of the page size applies only to the Spreadsheet Data Model File Format, not to the formats of the files that are contained inside the Spreadsheet Data Model. File formats within the Spreadsheet Data Model might use a different definition of page size for their formats.

Most of the Spreadsheet Data Model file is saved by using XML metadata (Spreadsheet Data Model header, Spreadsheet Data Model backup log file, and Spreadsheet Data Model virtual directory), with the files themselves being streamed into the Spreadsheet Data Model file directly in their native format (binary or XML). However, some elements within the Spreadsheet Data Model header are binary or calculated values. Likewise, the [**cyclic redundancy check (CRC)**](#gt_9cb45a36-92bb-4c14-b2fd-2ad7e2979bfd) file end marker involves the use of a CRC algorithm.

### Spreadsheet Data Model Header

The Spreadsheet Data Model header is page aligned but never compressed-even if the Spreadsheet Data Model file as whole has been compressed. Therefore, the header is always one page (4096 bytes) in size and padded with zeros between the last header element and the end of the page.

The Spreadsheet Data Model header consists of several elements. These elements MUST be in the following order and conform exactly as defined.

The first element is the byte order mark (section [2.1.1.1](#Section_0932c259227c4426b816abf7abc57d35)), which MUST be 2 bytes. The byte order mark is also used prior to the beginning of the stream of files (section [2.1.2](#Section_72e81524c51d43dd9f8f9edecbe73a41))-preceding the partition information)-as well as prior to the writing of the Spreadsheet Data Model backup log (section [2.1.2.3](#Section_5440b19d51e04b80928257e7388e3862)), which is the last file in the streamed files section. The byte order mark is not used before the virtual directory section (section [2.1.1.3](#Section_d3e98d193e55456ebc69d9caf7b6ab28)).

The second element in the header is the stream storage signature (section [2.1.1.2](#Section_9ac4d0fc21ee4ae4ba7cb1f782ad1a45)). These first two elements (byte order mark and stream storage signature) are binary, not XML.

After these first two binary elements, the subsequent elements in the header are XML tags. These elements MUST be in the order that is specified for the **BackupLogHeaderType** complex type (section 2.1.1.3). These XML tags are followed by any padding with zeros that is necessary to fill the page to the page boundary at 4096 bytes.

There are no breaks or padding between any of the elements.

#### Byte Order Mark

The byte order mark indicates to the system the byte order of the file. It is the first element of both the header and, by extension, the entire Spreadsheet Data Model file. There MUST NOT be any breaks before or after this element. The byte order mark consists of 2 bytes. The first byte MUST be set to 0xFF. The second byte MUST be set to 0xFE.

The byte order mark MUST also be used to begin the files section and therefore precedes the partition marker that leads the files section. The byte order mark MUST also be used before the backup log, which is the last file in the files section. For more details about the files section, see section [2.1.2](#Section_72e81524c51d43dd9f8f9edecbe73a41). For more details about the backup log file, see section [2.1.2.3](#Section_5440b19d51e04b80928257e7388e3862).

#### Stream Storage Signature

The stream storage signature indicates to the system that the file is a valid Spreadsheet Data Model file. The stream storage signature is a byte stream. The stream storage signature MUST come directly after the byte order mark and directly before the rest of the header without any breaks.

The stream storage signature MUST be set to the following [**ASCII**](#gt_79fa85ca-ac61-467c-b819-e97dc1a7a599) string:

- STREAM*STORAGE_SIGNATURE*)!@#\$%^&\*(

The stream storage signature MUST be encoded in [**Unicode**](#gt_c305d0ab-8b94-461a-bd76-13b40cb8c4d8).

#### BackupLogHeaderType

The **BackupLogHeaderType** complex type is the type of the **BackupLog** element, which is the [**XML element**](#gt_a364f92c-0374-4568-b7f8-40bd74437dd5) that contains the XML content of the backup log header (section [2.1.1](#Section_b5189435d6c5498c896f53a079be0c79)).

The backup log header format begins with the byte order mark (section [2.1.1.1](#Section_0932c259227c4426b816abf7abc57d35)) and the stream storage signature (section [2.1.1.2](#Section_9ac4d0fc21ee4ae4ba7cb1f782ad1a45)) and is page aligned (see section [2.1](#Section_49ca8d5609274cb2ad97bf73f0d91536) and section 2.1.1). The backup log is an [**XML document**](#gt_8fa90ece-7a01-4c00-af85-adbf0ed01882). Its document node is the **BackupLog** element.

- &lt;xs:complexType name="BackupLogHeaderType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="BackupRestoreSyncVersion" type="xs:int"/&gt;
- &lt;xs:element name="Fault" type="xs:boolean"/&gt;
- &lt;xs:element name="faultcode" type="xs:unsignedInt"/&gt;
- &lt;xs:element name="ErrorCode" type="xs:boolean"/&gt;
- &lt;xs:element name="EncryptionFlag" type="xs:boolean"/&gt;
- &lt;xs:element name="EncryptionKey" type="xs:int"/&gt;
- &lt;xs:element name="ApplyCompression" type="xs:boolean"/&gt;
- &lt;xs:element name="m_cbOffsetHeader" type="xs:unsignedLong"/&gt;
- &lt;xs:element name="DataSize" type="xs:unsignedLong"/&gt;
- &lt;xs:element name="Files" type="xs:unsignedInt"/&gt;
- &lt;xs:element name="ObjectID"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:string"&gt;
- <xs:pattern value=
- "\[0-9A-F\]{8}-\[0-9A-F\]{4}-\[0-9A-F\]{4}-\[0-9A-F\]{4}-\[0-9A-F\]{12}" />
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="m_cbOffsetData" type="xs:unsignedLong"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**BackupRestoreSyncVersion:** The internal version number of the software that has created this file. This value MUST be set to 140.

**Fault:** A Boolean value specifying that a CRC signature is not being used as an end-of-file marker (section [2.1.2.2.1](#Section_b379742e0aab47d3ae3f6d63c23139a1)). This value MUST be set to **false**. The CRC signature MUST be used. The CRC signature is a calculated value (section [2.1.2.2.1.1](#Section_2baccaf96a3846c6baedc982c595d478)).

**Faultcode:** A value that is unused. The value MUST be an unsigned integer to avoid load errors, but the value itself does not matter.

**ErrorCode:** A Boolean value specifying that a CRC signature is being used as an end-of-file marker (section 2.1.2.2.1). This value MUST be set to **true**. The CRC signature MUST be used. The CRC signature is a calculated value (section 2.1.2.2.1.1).

**EncryptionFlag:** A Boolean value that specifies whether the Spreadsheet Data Model file is encrypted. The header MUST NOT be encrypted (section 2.1.1). This value MUST be set to **false**.

**EncryptionKey:** The version of encryption that is being used. This value MUST contain an integer to avoid load errors, but the value itself does not matter.

**ApplyCompression:** A Boolean value that specifies whether compression has been applied to the file. This value MUST be set to **true**. The header is the exception; it is never compressed. Individual files within the Spreadsheet Data Model file can also be compressed, regardless of whether the Spreadsheet Data Model file itself is compressed. The Spreadsheet Data Model file is compressed by using Xpress compression (section [2.7.5](#Section_3e3dac063f4548a593d4abacd4b34000)).

**m_cbOffsetHeader:** The byte offset of the beginning of the file list-that is, the byte offset of the virtual directory structure that contains the list of files in the directory. The offset value is calculated from the beginning of the Spreadsheet Data Model file. For example, if the offset is 28,672, the file list (the virtual directory) begins at byte 28,672 (hexadecimal 0x7000) in the file. The offset is Spreadsheet Data Model page aligned and therefore MUST be a multiple of the Spreadsheet Data Model file page size (section 2.1). For more information about the virtual directory that contains the file list, see section 2.1.1.3.

**DataSize:** The size, in bytes, of the file list (the virtual directory) in the Spreadsheet Data Model file. For example, if the file size is set to 3748, the entire virtual directory is 3748 bytes in size (section 2.1.1.3).

**Files:** The number of file entries in the file list (the virtual directory). For example, if this value is set to 5, five files exist in the virtual directory and five files are serially stored in the Spreadsheet Data Model file.

**ObjectID:** A value that is unused and MUST be ignored. This value MUST be a valid [**universally unique identifier (UUID)**](#gt_c4813fc3-b2e5-4aa3-bde7-421d950d68d3); otherwise, the file might not load.

**m_cbOffsetData:** A value that indicates the beginning of the stored files section and the end of the header section. The value is in bytes. For example, if the value is 4096, the beginning of the stored files section begins at byte 4096 (hexadecimal 0x1000). For more information about the header and the header size, see section 2.1.1.

### Files Section

This section specifies the files in the file stream.

#### Partitions

A partitions marker exists between the Spreadsheet Data File header (including its padding) and the beginning of the actual files in the directory. The partitions marker is preceded by the byte order mark (section [2.1.1.1](#Section_0932c259227c4426b816abf7abc57d35)). The partitions marker is also treated like any other file in the files section and is terminated by a CRC marker (section [2.1.2.2.1.1](#Section_2baccaf96a3846c6baedc982c595d478)).

The Partitions section is an [**XML document**](#gt_8fa90ece-7a01-4c00-af85-adbf0ed01882) with a **Partitions** element as its document node. The **Partitions** element is of type **SdfPartitionsType**.

- &lt;xs:complexType name="SdfPartitionsType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Partition" type="SdfPartitionType"
- maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Partition:** A complex type element that specifies the properties of a partition.

##### SdfPartitionType

The **SdfPartitionType** complex type specifies the properties of a partition.

- &lt;xs:complexType name="SdfPartitionType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="ObjectPath" type="xs:string"/&gt;
- &lt;xs:element name="Name" type="xs:string"/&gt;
- &lt;xs:element name="DataSize" type="xs:long"/&gt;
- &lt;xs:element name="Location" type="xs:string"/&gt;
- &lt;xs:element name="DataSourceID" type="xs:string"/&gt;
- &lt;xs:element name="ConnectionString" type="xs:string"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**ObjectPath:** A value that is unused and MUST be ignored.

**Name:** A value that is unused and MUST be ignored.

**DataSize:** A value that is unused and MUST be ignored.

**Location:** A value that is unused and MUST be ignored.

**DataSourceID:** A value that is unused and MUST be ignored.

**ConnectionString:** A value that is unused and MUST be ignored.

#### File Stream Format

All files in the Spreadsheet Data Model file are stored in their native format, whether XML or binary. A [**CRC**](#gt_9cb45a36-92bb-4c14-b2fd-2ad7e2979bfd) marker (section [2.1.2.2.1.1](#Section_2baccaf96a3846c6baedc982c595d478)) delineates the end of one file and the beginning of the next file (if present).

The byte order mark (section [2.1.1.1](#Section_0932c259227c4426b816abf7abc57d35)) begins this files section, which is followed by the partitions marker (section [2.1.2.1](#Section_2ecd827be16b41bcaec7916b0afbf0f3)), which is then all the files except for the backup log. At this point, there is another byte order mark that is followed by the backup log (section [2.1.2.3](#Section_5440b19d51e04b80928257e7388e3862)), which is the last file.

A CRC marker exists between the partitions marker (section 2.1.2.1) and the first file. As stated earlier in this section, all the files in this stream of files are terminated by a CRC marker. Finally, a CRC marker follows the last file, which is the backup log (section 2.1.2.3).

The entire files section MUST be Spreadsheet Data Model file page aligned (section [2.1](#Section_49ca8d5609274cb2ad97bf73f0d91536)). Many pages of files could exist, and all the files are streamed in without breaks, except for their CRC markers. However, following the last file in the stream (the backup log), padding with zeros MUST exist from the log's CRC marker to the end of the page boundary.

The virtual directory (section [2.1.1.3](#Section_d3e98d193e55456ebc69d9caf7b6ab28)) begins at the start of the next page.

##### File End Markers

All the files in the Spreadsheet Data Model file are terminated by an end-of-file marker. A [**CRC**](#gt_9cb45a36-92bb-4c14-b2fd-2ad7e2979bfd) marker is used to indicate the end of a file and, therefore, also the beginning of the next file (if present).

The CRC marker is a calculated value (section [2.1.2.2.1.1](#Section_2baccaf96a3846c6baedc982c595d478)).

###### CRC Marker

The [**CRC**](#gt_9cb45a36-92bb-4c14-b2fd-2ad7e2979bfd) marker provides a calculated signature value that indicates the end of one file and the beginning of the next file (if present). If the CRC marker is being used, the **ErrorCode** element of the header metadata (section [2.1.1.3](#Section_d3e98d193e55456ebc69d9caf7b6ab28)) will be set to **true**.

CRC signatures are typically used to detect the alteration of data during transmission in communication systems, but can also be used to detect the alteration of backup files, such as those in the Spreadsheet Data Model file.

The CRC is calculated according to the following pseudocode:

- SET constant value CRC32_POLY to 0x04C11DB7
- CREATE unsigned 32 bit integer array of 256 elements and name it crc32TableArray
- CREATE unsigned 32 bit integer value, name it crcValue and SET it to 0xFFFFFFFF
- CALL InitializationOfCRC32TableArray Function (as follows)
- FOR each element iValue in crc32TableArray
- FOR (cValue = ( iValue LEFT_BITSHIFT 24), jValue = 8), continue loop while jValue>0
- SET cValue to result of (cValue BITWISE_AND 0x80000000)
- IF cValue evaluates to TRUE (nonzero) THEN
- SET cValue to result of ( (cValue LEFT_BITSHIFT 1) BITWISE_EXCLUSIVEOR CRC32_POLY)
- If cValue evaluates to FALSE (zero) THEN
- SET cValue to result of (cValue LEFT_BITSHIFT 1)
- SET crc32TableArray at index position ( iValue ) to cValue
- DECREMENT jValue by 1
- END FOR
- END FOR
- CALL Calculation of crc32Value (after InitializationOfCRC32TableArray)(as follows)
- INPUT to function is an array of BYTES, called pBuffer, and also the buffer's length, cLength
- FOR each byte in pBuffer up to its length
- SET tempIndex to result of ( (crcValue RIGHT_BITSHIFT 24) BITWISE_EXCLUSIVEOR (value contained by the currently indexed byte in pBuffer))
- SET crcValue to result of ( (crcValue LEFT_BITSHIFT 8) BITWISE_EXCLUSIVEOR (crc32TableArray at index position (tempIndex) ) )
- END FOR

#### Log File

The log contains a list of all the files that are included in the instance of the Spreadsheet Data Model, except for the log itself, the virtual directory, and the partitions section. The log is the last file in the files section (see section [2.1.2.2](#Section_e10e8481e4234b4ba12f23f7c2228dca)). The log is an [**XML document**](#gt_8fa90ece-7a01-4c00-af85-adbf0ed01882). The document node is the **BackupLog** element.

##### SdfBackupLogType

The **SdfBackupLogType** is the type of the **BackupLog** document node element in the file list section of the Spreadsheet Data Model file. It contains a logging of the files that are included in the Spreadsheet Data Model instance.

- &lt;xs:complexType name="SdfBackupLogType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="BackupRestoreSyncVersion" type="xs:int"/&gt;
- &lt;xs:element name="ServerRoot" type="xs:string"/&gt;
- &lt;xs:element name="SvrEncryptPwdFlag" type="xs:boolean"/&gt;
- &lt;xs:element name="ServerEnableBinaryXML" type="xs:boolean"/&gt;
- &lt;xs:element name="ServerEnableCompression" type="xs:boolean"/&gt;
- &lt;xs:element name="CompressionFlag" type="xs:boolean"/&gt;
- &lt;xs:element name="EncryptionFlag" type="xs:boolean"/&gt;
- &lt;xs:element name="ObjectName" type="xs:string"/&gt;
- &lt;xs:element name="ObjectId" type="xs:string"/&gt;
- &lt;xs:element name="Write" type="WriteEnum"/&gt;
- &lt;xs:element name="OlapInfo" type="xs:boolean"/&gt;
- &lt;xs:element name="Collations" type="SdfBackupLogCollationsType"/&gt;
- &lt;xs:element name="Languages" type="SdfBackupLogLanguagesType"/&gt;
- &lt;xs:element name="FileGroups" type="SdfFileGroupsType"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**BackupRestoreSyncVersion:** A value that MUST be set to 1153.

**ServerRoot:** The root folder in the originating file system from which the files in the Spreadsheet Data Model were copied.

**SvrEncryptPwdFlag:** A Boolean value that specifies whether the originating source application supports password encryption. The value MUST be set to **true**.

**ServerEnableBinaryXML:** A Boolean value that specifies whether the originating source application supports XML metadata in the Spreadsheet Data Model file in binary XML. The value MUST be set to **false**.

**ServerEnableCompression:** A value that MUST be set to **false**.

**CompressionFlag:** A value that MUST be set to **false**.

**EncryptionFlag:** A value that MUST be set to **false**.

**ObjectName:** The database name.

**ObjectId:** The [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) database identifier value.

**Write:** An enumeration value that specifies the type of access allowed.

**OlapInfo:** A Boolean value that specifies whether the files came from a data model that is based on OLAP. The value MUST be one of the values that are described in the following table.

| Value     | Meaning                                                                                                                                                                                                                             |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **true**  | The data files came from a data model that is based on OLAP.                                                                                                                                                                        |
| **false** | The data files came from either a [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) or a model that is stored on a server as described in [\[MS-SPO\]](%5bMS-SPO%5d.pdf#Section_a9173bd4232741ac8ecbdc20e0ab7d92). |

**Collations:** The name of the collation. The value MAY[&lt;1&gt;](#Appendix_A_1) be restricted to a string that is recognized as valid by the system.

**Languages:** The language.

**FileGroups:** The file groups that are contained in the Spreadsheet Data Model file.

###### SdfBackupLogCollationsType

The **SdfBackupLogCollationsType** complex type specifies a collection of collations that are used by the files included in this structure.

- &lt;xs:complexType name="SdfBackupLogCollationsType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Collation" type="xs:string" maxOccurs="unbounded"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Collation:** The name of the collation. The value MAY[&lt;2&gt;](#Appendix_A_2) be restricted to a string that is recognized as valid by the system.

###### SdfBackupLogLanguagesType

The **SdfBackupLogLanguagesType** complex type specifies a collection of languages that are used by the files included in the Spreadsheet Data Model structure.

- &lt;xs:complexType name="SdfBackupLogLanguagesType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Language" type="xs:int" maxOccurs="unbounded"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Language:** The [**language code identifier (LCID)**](#gt_c7f99c66-592f-4053-b62a-878c189653b6) for the backup log.

###### SdfFileGroupsType

The **SdfFileGroupsType** complex type specifies the list of files, first as a group and then individually.

- &lt;xs:complexType name="SdfFileGroupsType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="FileGroup" type="SdfFileGroupType"
- maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**FileGroup:** A group of files with common, specified properties, followed by the list of files in the group and their individual properties.

SdfFileGroupType

The **SdfFileGroupType** complex type specifies the properties of a group of files, as well as the files and the properties for the member files in that group.

- &lt;xs:complexType name="SdfFileGroupType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Class" type="xs:int"/&gt;
- &lt;xs:element name="ID" type="xs:string"/&gt;
- &lt;xs:element name="Name" type="xs:string"/&gt;
- &lt;xs:element name="ObjectVersion" type="xs:int"/&gt;
- &lt;xs:element name="PersistLocation" type="xs:int"/&gt;
- &lt;xs:element name="PersistLocationPath" type="xs:string"/&gt;
- &lt;xs:element name="StorageLocationPath" type="xs:string"/&gt;
- &lt;xs:element name="ObjectID"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:string"&gt;
- <xs:pattern value=
- "\[0-9A-F\]{8}-\[0-9A-F\]{4}-\[0-9A-F\]{4}-\[0-9A-F\]{4}-\[0-9A-F\]{12}" />
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="FileList" type="SdfFileListType"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Class:** The OLAP object that the group of files belongs to. The value of this element MUST equal one of the values specified in **SdfFileGroupClassEnum** (section [2.1.2.3.1.3.1.1](#Section_e2236f6eca4444a5bda50bfc4cf79022)).

**ID:** The identifier of the OLAP object.

**Name:** The name of the object.

**ObjectVersion:** An internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model. The value will appear within the file name. For example, if the value is "10" for a dimension object, the file name will end in "10.dim.xml". This value MUST match that of the **ObjectVersion** element of the OLAP dimension object, which is of type **DatabaseTabularModel** (section [2.6.4](#Section_220cbde1c685486ba1df07ff4be6965d)).

**PersistLocation:** The version number that will appear within the folder name. For example, if the value is "10" for a database object, the folder name will end in "10.db". This value MUST match that of the **PersistLocation** element of the OLAP database object, which is of type **DatabaseTabularModel** (section 2.6.4).

**PersistLocationPath:** The folder in which the files of this file group are stored. This value MUST match that of the **DbStorageLocation** element of the OLAP database object, which is of type **DatabaseTabularModel** (section 2.6.4).

**StorageLocationPath:** A value that is unused, and MUST be ignored.

**ObjectID:** The identifier of this object. This value matches that of the **ObjectID** property of the OLAP object.

**FileList:** The list of the files that are members of the group, and the properties of those files. This is of type **SdfFileListType** (section [2.1.2.3.1.3.1.2](#Section_395e80b569974971ac8f9dd855334e7c)).

SdfFileGroupClassEnum

The **SdfFileGroupClassEnum** simple type specifies the enumeration values for the **Class** element of the file group.

- &lt;xs:simpleType name="SdfFileGroupClassEnum"&gt;
- &lt;xs:restriction base="xs:int"&gt;
- &lt;xs:minInclusive value="100002"/&gt;
- &lt;xs:maxInclusive value="100060"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **SdfFileGroupClassEnum** type.

| Enumeration value | Description                                                                              |
| ----------------- | ---------------------------------------------------------------------------------------- |
| 100002            | Database                                                                                 |
| 100003            | [**Data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075)                              |
| 100006            | Dimension                                                                                |
| 100010            | [**Cube**](#gt_a0c8d97b-322c-4117-8525-37e5f26751e7)                                     |
| 100016            | [**Measure group**](#gt_1f51f60a-8a0f-4b0d-9e7e-80cbd596e164)                            |
| 100021            | Partition                                                                                |
| 100053            | Data source view                                                                         |
| 100060            | [**Multidimensional expression (MDX)**](#gt_9b631ff5-dc89-45f0-a1c2-db6981e4804f) script |

SdfFileListType

The **SdfFileListType** complex type specifies the list of files that are in a file group as well as the properties of those files.

- &lt;xs:complexType name="SdfFileListType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="BackupFile" type="SdFileListBackupFileType"
- maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**BackupFile:** A complex type that specifies a file that is included in the Spreadsheet Data Model file.

SdfFileListBackupFileType

The **SdfFileListBackupFileType** complex type specifies the properties of a file that is included in the Spreadsheet Data Model file.

- &lt;xs:complexType name="SdFileListBackupFileType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Path" type="xs:string"/&gt;
- &lt;xs:element name="StoragePath" type="xs:string"/&gt;
- &lt;xs:element name="LastWriteTime" type="xs:long"/&gt;
- &lt;xs:element name="Size" type="xs:int"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Path:** The path of the file in the original source file system.

**StoragePath:** The storage path of the file in this spreadsheet data file. This value is the key that is used to match information with information in the virtual directory. This value matches the value of the **Path** element for the same file in the virtual directory.

**LastWriteTime:** The time that the file was last written. The value is the number of nanoseconds that have elapsed since midnight on January 1, 1601.

**Size:** The actual size, in bytes, of this file within the storage. The value does not include the end-of-file marker, or CRC marker, if one is used.

###### WriteEnum

The **WriteEnum** simple type enumerates the allowed values for the name of the **Write** element in the **SdfBackupLogType** type. The values specify the types of enabled access.

- &lt;xs:simpleType name="WriteEnum"&gt;
- &lt;xs:restriction base="xs:string"&gt;
- &lt;xs:enumeration value="ReadWrite"/&gt;
- &lt;xs:enumeration value="ReadOnly"/&gt;
- &lt;xs:enumeration value="ReadOnlyExclusive"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **WriteEnum** type.

| Enumeration value   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "ReadWrite"         | Read-write access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| "ReadOnly"          | Read-only access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| "ReadOnlyExclusive" | Read-only exclusive access. This enumeration value is in a different namespace-specifically, <http://schemas.microsoft.com/analysisservices/2010/engine/200/200>. When the element value is set to this enumeration value, the value of the **valuens** attribute ([\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.1.3](http://msdn.microsoft.com/en-us/library/91987baf-3e5f-48df-b357-8299f137cd44/)) on the element MUST be set to the namespace value. |

#### CryptKey.bin File

The CryptKey.bin file contains a cryptographic key. The key is used to encrypt and decrypt the connection strings and password data that are found in the [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) tabular model file (section [2.6.2](#Section_536cdc3781f54984b17359fc6ef64247)), which is inside the Spreadsheet Data Model file (section [2.1](#Section_49ca8d5609274cb2ad97bf73f0d91536)). The CryptKey.bin file that is stored in the Spreadsheet Data Model file is not the same as the CryptKey.bin file that is independently present on disk (if present at all).

The key inside the CryptKey.bin file is in its original form, even though it is also in the format of a key [**binary large object (BLOB)**](#gt_ad861812-8cb0-497a-80bb-13c95aa4e425) (section [2.1.2.4.1.1.2](#Section_f02458c4d25140a2b12240dd442ecf5a)) of BLOB type **SIMPLEBLOB** (section [2.1.2.4.1.1.2.1](#Section_6102c812108f49e1ba13b9bb9a8ca7af)). However, a session key (**SIMPLEBLOB** type) requires two keys to create a key BLOB. To leave the key BLOB in its original form, this situation is handled by using an exponent-of-one private key (section [2.1.2.4.2](#Section_3a6f9354682b48309728923e0d633693)).

The CryptKey.bin file is composed of a **CryptKeyHeader** structure (section [2.1.2.4.1.1.1](#Section_cd04831adc3d4a14aa9b3d01b547287e)), the key BLOB itself (section 2.1.2.4.1.1.2), and a **CryptKeyTrailer** structure (section [2.1.2.4.1.1.3](#Section_42ff8ffbcb804c05bf78ba34540ebd0d)).

##### CryptKey.bin File Format

The CryptKey.bin file format consists of a **CryptKeyHeader** structure (section [2.1.2.4.1.1.1](#Section_cd04831adc3d4a14aa9b3d01b547287e)) followed by the key BLOB (section [2.1.2.4.1.1.2](#Section_f02458c4d25140a2b12240dd442ecf5a)), which is a key data area containing a **BYTE** array that always contains a **PUBLICKEYSTRUC** BLOB header (section [2.1.2.4.1.1.2.1](#Section_6102c812108f49e1ba13b9bb9a8ca7af)) and the original key as well as other information as specified by the type of key BLOB. The proper key BLOB can be generated by using an exponent-of-one key and the original key (see section [2.1.2.4.2](#Section_3a6f9354682b48309728923e0d633693)). This is finally followed by a **CryptKeyTrailer** structure (section [2.1.2.4.1.1.3](#Section_42ff8ffbcb804c05bf78ba34540ebd0d)). These structures MUST be in this order and have no breaks between the areas or structures.

The file format MUST begin with the **CryptKeyHeader** structure, with no bytes preceding the structure. Likewise, no bytes can follow the **CryptKeyTrailer** structure in the file. No padding of any kind exists in the file, except for one case. Padding could exist between the key BLOB data and the beginning of the **CryptKeyTrailer** header. The **m_dwKeyDataSize** member of the **CryptKeyHeader** file MUST accurately account for this possible padding used by the key BLOB.

###### CryptKey.bin Structures

This section specifies the structures that are required by the CryptKey.bin file format.

CryptKeyHeader

The **CryptKeyHeader** structure stores configuration information for the CryptKey.bin file.

- struct CryptKeyHeader
- {
- GUID m_Magic;
- DWORD m_dwVersion;
- DWORD m_dwHeaderSize;
- DWORD m_dwKeyDataSize;
- DWORD m_dwTrailerSize;
- DWORD m_dwProvider;
- DWORD m_dwAlgorithm;
- DWORD m_dwFlags;
- };

**m_Magic:** A [**GUID**](#gt_f49694cc-c350-462d-ab8e-816f0103c6c1) that identifies the CryptKey.bin file as a valid file. This value MUST be set to the value in the following table.

| Name                | Value                                                                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CryptKey Magic GUID | {0x5d21bc98, 0x8d2d, 0x4ee6, {0xa8, 0xe5, 0xd0, 0x38, 0xaa, 0xc9, 0x44, 0x41}}<br><br>This value will resolve to the following GUID:<br><br>5d21bc98-8d2d-4ee6-a8e5-d038aac94441 |

**m_dwVersion:** The encryption key version. The value MUST be set to 0x00000004.

**m_dwHeaderSize:** The size, in bytes, of the **CryptKeyHeader** structure. The value MUST be set to 44 (hexadecimal 0x0000002C).

**m_dwKeyDataSize:** The size of the key BLOB, including the **PUBLICKEYSTRUC** structure as well as the key and any other required values.

**m_dwTrailerSize:** The size, in bytes, of the **CryptKeyTrailer** structure. The value MUST be set to 16 (hexadecimal 0x00000010).

**m_dwProvider:** The cryptographic provider that is used. Typically, the value is set to 0x00000001. The value MUST be set to one of the values in the following table.

| **Name**                                                                 | **Value**  |
| ------------------------------------------------------------------------ | ---------- |
| MS_DEF_PROV<br><br>"Microsoft Base Cryptographic Provider v1.0"          | 0x00000000 |
| MS_ENHANCED_PROV<br><br>"Microsoft Enhanced Cryptographic Provider v1.0" | 0x00000001 |

**m_dwAlgorithm:** The cryptographic algorithm that is used. Typically, the value is set to 0x00000007. The value MUST be set to one of the values in the following table.

| **Name**      | **Value**                                                                              |
| ------------- | -------------------------------------------------------------------------------------- |
| CALG_3DES     | One of the values in 0x00000000, 0x0000001, 0x0000002, 0x0000003, 0x0000004, 0x0000007 |
| CALG_RC2      | 0x00000005                                                                             |
| CALG_3DES_112 | 0x00000006                                                                             |

**m_dwFlags:** This value is unused and MUST be set to -1 (hexadecimal 0xFFFFFFFF).

Key BLOB

The key BLOB is composed of a **BYTE** array that contains a **PUBLICKEYSTRUC** BLOB header (section [2.1.2.4.1.1.2.1](#Section_6102c812108f49e1ba13b9bb9a8ca7af)) as well as the encrypted key for the CryptKey.bin file. There also might be other elements of the key BLOB beyond the **PUBLICKEYSTRUC** and the encrypted key. Those elements depend on the type of BLOB.

The key BLOB is correctly generated by using the **CryptExportKey** function ([\[MSDN-CRYPTO\]](https://go.microsoft.com/fwlink/?LinkId=89984)) with the key to be exported, an exponent-of-one private key as the public key, the _dwFlags_ parameter set to zero, and the _dwBlobType_ parameter set to **SIMPLEBLOB**. For more information about generating this key BLOB by using an exponent-of-one private key, see section [2.1.2.4.2](#Section_3a6f9354682b48309728923e0d633693).

PUBLICKEYSTRUC

The **PUBLICKEYSTRUC** structure, also known as the **BLOBHEADER** structure, indicates a key's BLOB type and the algorithm that the key uses. The information here pertains only to that needed by the CryptKey.bin file format. For more information about this structure and related information, see [\[MSDN-CRYPTO\]](https://go.microsoft.com/fwlink/?LinkId=89984).

- typedef struct \_PUBLICKEYSTRUC
- {
- BYTE bType;
- BYTE bVersion;
- WORD reserved;
- ALG_ID aiKeyAlg;
- } BLOBHEADER,
- PUBLICKEYSTRUC;

**bType:** The key BLOB type. The type that is used within CryptKey.bin is **SIMPLEBLOB**, so this member MUST be set to **SIMPLEBLOB**, as described in the following table.

| **Value**                               | **Meaning**               |
| --------------------------------------- | ------------------------- |
| **SIMPLEBLOB**<br><br>(hexadecimal 0x1) | The key is a session key. |

**bVersion:** The version number of the key BLOB format. This value MUST be greater than or equal to 2.

**reserved:** A member that is reserved and MUST be set to zero.

**aiKeyAlg:** One of the ALG_ID values that identifies the algorithm of the key contained by the key BLOB. The choice of algorithm MUST be the same as that specified in the **CryptKeyHeader** (section [2.1.2.4.1.1.1](#Section_cd04831adc3d4a14aa9b3d01b547287e)). However, the values that are used in this member are different than those that are used in the **CryptKeyHeader** and are described in the following table.

| **ALG_ID identifier** | **Value**  | **Description**                                                                                                                                                                                                                |
| --------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **CALG_3DES**         | 0x00006603 | Triple DES encryption algorithm. For more information about restraints on the use of this type of key, see \[MSDN-CRYPTO\].                                                                                                    |
| **CALG_3DES_112**     | 0x00006609 | Two-key triple DES encryption with the effective key length equal to 112 bits.                                                                                                                                                 |
| **CALG_RC2**          | 0x00006602 | RC2 block encryption algorithm. For more information about when this key can be used and its provider, see \[MSDN-CRYPTO\].<br><br>For the CryptKey.bin file, this algorithm is limited to an effective key length of 40 bits. |

CryptKeyTrailer

The **CryptKeyTrailer** structure stores configuration information for the CryptKey.bin file.

- struct CryptKeyTrailer
- {
- GUID m_Magic;
- };

**m_Magic:** A GUID that identifies the CryptKey.bin file as a valid file. This value MUST be set to the value in the following table.

| Name                | Value                                                                                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CryptKey Magic GUID | {0x5d21bc98, 0x8d2d, 0x4ee6, {0xa8, 0xe5, 0xd0, 0x38, 0xaa, 0xc9, 0x44, 0x41}}<br><br>This value will resolve to the following GUID:<br><br>5d21bc98-8d2d-4ee6-a8e5-d038aac94441 |

##### Creating an Exponent-of-One Private Key

As the **SIMPLEBLOB** type indicates a session key, both a source (private) key and a destination (public) key are required to create a valid key BLOB for the CryptKey.bin file. In the CryptKey.bin case, doing so is accomplished by using an exponent-of-one private key. This type of key is also called a NULL key because although it is accepted by the **CryptExportKey** function ([\[MSDN-CRYPTO\]](https://go.microsoft.com/fwlink/?LinkId=89984)), when it is used in that call as the public key, the resulting encryption and decryption do nothing to the private key to be exported. Therefore the private key to be exported is left in its original form.

To create the handle to the exponent-of-one private key, a valid key BLOB of type **SIMPLEBLOB** is required. This key BLOB is created such that the exponent of the key BLOB format is modified to an exponent of one. To obtain the handle of the exponent-of-one private key, the exponent-of-one key BLOB is used, along with the handle to the provider, in a call to the **CryptImportKey** function (\[MSDN-CRYPTO\]), as shown in the following pseudocode:

- CALL CryptImportKey with parameters (Handle-To CryptProvider,
- ExponentOfOnePrivateKeyBLOB,
- Size-Of ExponentOfOnePrivateKeyBLOB,
- 0,
- 0,
- Address-Of handleToExponentOfOnePrivateKey)

The handle to the cryptographic provider is obtained through a call to the **CryptAcquireContext** function (\[MSDN-CRYPTO\]) and MUST use one of the allowed CryptKey.bin providers as the provider string. Furthermore, the provider type MUST be set to **PROV_RSA_FULL**.

The providers that are allowed are listed (as strings) in the following table.

| Provider                                         | String name      |
| ------------------------------------------------ | ---------------- |
| "Microsoft Base Cryptographic Provider v1.0"     | MS_DEF_PROV      |
| "Microsoft Enhanced Cryptographic Provider v1.0" | MS_ENHANCED_PROV |

The key BLOB that is required by Cryptkey.bin can now be generated by calling **CryptExportKey** with the handle to the original key (the private key) to be exported, the handle of the exponent-of-one private key, the type set to **SIMPLEBLOB**, the flags value set to zero, a buffer to hold the returned key BLOB, and the length of the key BLOB. The call then returns the properly formatted key BLOB in the buffer parameter. The length of the key BLOB can be determined simply by making the same call to **CryptExportKey**, but with the buffer parameter (_BufferForExportedKeyBLOB_) set to zero.

The following pseudocode illustrates this call to create an exportable key BLOB:

- CALL CryptExportKey with parameters (Handle-To KeyToBeExported,
- Handle-To ExponentOfOnePrivateKey,
- SIMPLEBLOB,
- 0,
- Pointer-To BufferForExportedKeyBLOB,
- Pointer-To LengthOfExportedKeyBLOB)

This key BLOB, which is contained in _BufferForExportedKeyBLOB_, is then placed after the **CryptKeyHeader** (section [2.1.2.4.1.1.1](#Section_cd04831adc3d4a14aa9b3d01b547287e)) and before the **CryptKeyTrailer** (section [2.1.2.4.1.1.3](#Section_42ff8ffbcb804c05bf78ba34540ebd0d)) in CryptKey.bin.

The method of creating an exponent-of-one private key BLOB has been documented and is widely known. For more information, see [\[MSDOCS-PrivKeyBlobs\]](https://aka.ms/AAhrknm).

However, for convenience, the exponent-of-one private key BLOB is provided in the following table. The handle to this key BLOB is obtained by using **CryptImportKey**, as specified earlier in this section.

| Name                        | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ExponentOfOnePrivateKeyBLOB | const BYTE array\[\] =<br><br>{<br><br>0x07, 0x02, 0x00, 0x00, 0x00, 0xA4, 0x00, 0x00, 0x52, 0x53, 0x41, 0x32, 0x00, 0x02, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0xAB, 0xEF, 0xFA, 0xC6, 0x7D, 0xE8, 0xDE, 0xFB, 0x68, 0x38, 0x09, 0x92, 0xD9, 0x42, 0x7E, 0x6B, 0x89, 0x9E, 0x21, 0xD7, 0x52, 0x1C, 0x99, 0x3C, 0x17, 0x48, 0x4E, 0x3A, 0x44, 0x02, 0xF2, 0xFA, 0x74, 0x57, 0xDA, 0xE4, 0xD3, 0xC0, 0x35, 0x67, 0xFA, 0x6E, 0xDF, 0x78, 0x4C, 0x75, 0x35, 0x1C, 0xA0, 0x74, 0x49, 0xE3, 0x20, 0x13, 0x71, 0x35, 0x65, 0xDF, 0x12, 0x20, 0xF5, 0xF5, 0xF5, 0xC1, 0xED, 0x5C, 0x91, 0x36, 0x75, 0xB0, 0xA9, 0x9C, 0x04, 0xDB, 0x0C, 0x8C, 0xBF, 0x99, 0x75, 0x13, 0x7E, 0x87, 0x80, 0x4B, 0x71, 0x94, 0xB8, 0x00, 0xA0, 0x7D, 0xB7, 0x53, 0xDD, 0x20, 0x63, 0xEE, 0xF7, 0x83, 0x41, 0xFE, 0x16, 0xA7, 0x6E, 0xDF, 0x21, 0x7D, 0x76, 0xC0, 0x85, 0xD5, 0x65, 0x7F, 0x00, 0x23, 0x57, 0x45, 0x52, 0x02, 0x9D, 0xEA, 0x69, 0xAC, 0x1F, 0xFD, 0x3F, 0x8C, 0x4A, 0xD0, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x64, 0xD5, 0xAA, 0xB1, 0xA6, 0x03, 0x18, 0x92, 0x03, 0xAA, 0x31, 0x2E, 0x48, 0x4B, 0x65, 0x20, 0x99, 0xCD, 0xC6, 0x0C, 0x15, 0x0C, 0xBF, 0x3E, 0xFF, 0x78, 0x95, 0x67, 0xB1, 0x74, 0x5B, 0x60, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00<br><br>}; |

### Virtual Directory

Following the streamed-in files section (section [2.1.2](#Section_72e81524c51d43dd9f8f9edecbe73a41)) and any padding from that section to the Spreadsheet Data Model file page boundary (section [2.1](#Section_49ca8d5609274cb2ad97bf73f0d91536)), is the Spreadsheet Data Model virtual directory. The virtual directory lists all the files that are included in the instance of the Spreadsheet Data Model, except for the virtual directory itself.

No byte order mark (section [2.1.1.1](#Section_0932c259227c4426b816abf7abc57d35)) precedes the virtual directory. However, the virtual directory MUST be followed by padding with zeros to end of the page boundary, which is also the end of the Spreadsheet Data Model file.

The virtual directory is an [**XML document**](#gt_8fa90ece-7a01-4c00-af85-adbf0ed01882). The document node is the **VirtualDirectory** element.

#### VirtualDirectoryType

The **VirtualDirectoryType** complex type is the type of the **VirtualDirectory** element document node in the virtual directory section of the Spreadsheet Data Model file. **VirtualDirectoryType** contains the list of files.

- &lt;xs:complexType name="VirtualDirectoryType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="BackupFile" type="VirtualDirectoryBackupFileType"
- maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**BackupFile:** A complex type containing the information about each file that is included in the Spreadsheet Data Model.

#### VirtualDirectoryBackupFileType

The **VirtualDirectoryBackupFileType** complex type contains properties for each file that is included in the Spreadsheet Data Model instance.

- &lt;xs:complexType name="VirtualDirectoryBackupFileType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Path" type="xs:string"/&gt;
- &lt;xs:element name="Size" type="xs:unsignedLong"/&gt;
- &lt;xs:element name="m_cbOffsetHeader" type="xs:unsignedLong"/&gt;
- &lt;xs:element name="Delete" type="xs:boolean"/&gt;
- &lt;xs:element name="CreatedTimestamp" type="xs:long"/&gt;
- &lt;xs:element name="Access" type="xs:long"/&gt;
- &lt;xs:element name="LastWriteTime" type="xs:long"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Path:** The path of the file within the virtual directory. The value is used as a key to match the file to the backup log, which contains an identical entry for the storage path of a file in the backup log.

**Size:** The actual size, in bytes, of this file within the storage. The size includes the end-of-file marker, the CRC marker, if one is used.

**m_cbOffsetHeader:** The offset, in bytes, within the storage to the file. The value includes the header.

**Delete:** A value that is unused and MUST be ignored.

**CreatedTimestamp:** The time that the file was created. The value is the number of nanoseconds that have elapsed since midnight on January 1, 1601.

**Access:** The time that the file was accessed. The value is the number of nanoseconds that have elapsed since midnight on January 1, 1601.

**LastWriteTime:** The time that the file was last written. The value is the number of nanoseconds that have elapsed since midnight on January 1, 1601.

## File Name Generation

The metadata and data for each Spreadsheet Data Model is represented by a group of files that are automatically generated by the system and that are stored hierarchically in folders. The substrings within the generated names for the files have meaning. The method for the generation of the file names, by concatenation of the substrings that represent various properties of the file, is described in this section. The requirements for which files and folders are mandatory, and under what circumstances, are also described in this section. The file names are defined by using [**Augmented Backus-Naur Form (ABNF)**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) notation, as specified in [\[RFC5234\]](https://go.microsoft.com/fwlink/?LinkId=123096).

### Top-Level Files

The root folder for the stored files contains the database definition file and the database folder. Every [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) MUST have a database definition file.

The database definition file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rules:

- Integer = \*%x30-39
- Char = %x41-5A / %x61-7A / %x30-39 / %x23-2E / "!" / "=" / "@" / "\[" / "\]" /
- "^" / "{" / "}" / "~"
- UserID = \*Char
- DBPersistVersion = Integer
- DatabaseFolderName = UserID "." DBPersistVersion ".db.xml"

**UserID** is an identifier that is assigned by the user to an object. The characters in **UserID** MAY[&lt;3&gt;](#Appendix_A_3) be normalized. The **UserID** used in section [2.2.2](#Section_ee899b2229ee496fba0cf25f9c033443) and section [2.2.3](#Section_2724b80b8d284083b5e62f866caf5e69) follow the same definition. **DBPersistVersion** MUST be equal to the value of the **PersistLocation** element in the database definition stored in the database definition file.

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model. The **Integer** used in section 2.2.2 and section 2.2.3 follow the same definition.

The content of the database definition file is specified in section [2.6.4](#Section_220cbde1c685486ba1df07ff4be6965d).

### Database Folder

The root folder for the stored files is the database folder. Every [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) MUST have a database folder.

The database folder name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rules:

- DatabaseFolderName = UserID "." DBPersistVersion ".db"

The database folder contains all of the remaining folders and files that are specified in the structure. DBPersistVersion MUST equal the value of the PersistLocation element in the database definition for the corresponding database. The database definition file is described in section [2.2.1](#Section_ca7f367c1eca41afb8244a77c462ad7e).

### Database Folder Contents

The database folder contains the files and folders that are specified in the following subsections.

#### Data Source View Definition File

A [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) view definition file describes the structure of all data source views in the model. A [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) MUST have a data source view definition file.

The data source view definition file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- DSVVersion = Integer
- DataSourceViewDefinitionFileName = UserID "." DSVVersion ".dsv.xml"

**UserID** is an identifier that is assigned by the user to an object. The characters in **UserID** MAY[&lt;4&gt;](#Appendix_A_4) be normalized.

The content of the data source view definition file is specified in section [2.6.3](#Section_77f559d9ed7d467fb1f620aea4410502).

#### Cube Definition File

A cube definition file describes the structure of a cube. Every [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) MUST have a cube definition file.

The cube definition file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- CubeDefinitionFileName = UserID "." Integer ".cub.xml"

**UserID** is an identifier that is assigned by the user to an object. The characters in **UserID** MAY[&lt;5&gt;](#Appendix_A_5) be normalized.

The content of the cube definition file is specified in section [2.6.5](#Section_6123c4c160fd4d7683a46467421fede2).

#### Cube Folder

Every [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) MUST have a cube folder. The cube folder name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- CubeFolderName = UserID ".0.cub"

##### Cube Folder Folders

The cube folder MUST contain a [**measure group**](#gt_1f51f60a-8a0f-4b0d-9e7e-80cbd596e164) folder for each table that participates in the cube.

###### Measure Group Folder

Every cube folder MUST contain at least one [**measure group**](#gt_1f51f60a-8a0f-4b0d-9e7e-80cbd596e164) folder.

The measure group folder name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rules:

- TableID = UserID
- MeasureGroupFolderName = TableID "." Integer "." "det"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

Measure Group Folder Folders

Each [**measure group**](#gt_1f51f60a-8a0f-4b0d-9e7e-80cbd596e164) folder MUST contain a partition folder.

The partition folder name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- PartitionFolderName = TableID "." Integer "." "prt"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

Partition Folder Files

A partition information file MUST be generated in every partition folder.

The partition information file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- PartitionInfoFileName ::= "info" "." Integer "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the partition information file is specified in section [2.6.10.1](#Section_1d41fe8353a442a0a61de36029f37394).

Measure Group Folder Files

A partition metadata file MUST be generated in every [**measure group**](#gt_1f51f60a-8a0f-4b0d-9e7e-80cbd596e164) folder.

The partition metadata file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- PartitionFileName = TableID "." Integer "." "prt" "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the partition metadata file is specified in section [2.6.8](#Section_e7167bbc07cb453bb06072b04b75ac69).

##### Cube Folder Files

The following subsections specify name generation for the files that are contained in the cube folder.

###### Cube Information File

A cube information file MUST be generated in every cube folder.

The cube information file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- CubeInfoFileName = "info" "." Integer "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of cube information file is specified in section [2.6.10.3](#Section_b1e7573c1c164718bed37a812abfb4f2).

###### MDX Script Metadata File

A [**Multidimensional Expressions (MDX)**](#gt_9b631ff5-dc89-45f0-a1c2-db6981e4804f) script metadata file MUST be generated in the cube folder.

The MDX script metadata file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- MdxScriptFileName = "MdxScript" "." "0" "." "scr" "." "xml"

The content of the MDX script metadata file is specified in section [2.6.9](#Section_37b7ea6d12f749ed91978daf494edba2).

###### Measure Group Metadata File

A [**measure group**](#gt_1f51f60a-8a0f-4b0d-9e7e-80cbd596e164) metadata file MUST be generated in the cube folder.

The measure group metadata file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- MeasureGroupFileName = TableID "." "Integer" "." "det" "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the measure group metadata file is specified in section [2.6.7](#Section_0861668595e448eea31c733d6b94773f).

#### Data Source Definition File

A [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) definition file describes the structure of a single data source. A [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) MAY have one or more data source definition files.

A data source definition file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- DataSourceDefinitionFileName = UserID "." Integer ".ds.xml"

**UserID** is an identifier that is assigned by the user to an object. The characters in **UserID** MAY[&lt;6&gt;](#Appendix_A_6) be normalized.

The content of a data source definition file is specified in section [2.6.2](#Section_536cdc3781f54984b17359fc6ef64247).

#### Data Source Folder

Each model MAY[&lt;7&gt;](#Appendix_A_7) contain a [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) folder.

The data source folder name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rules:

- DataSourceID = UserID
- DataSourceFolderName = DataSourceID "." "0" "." "ds"

#### Dimension Definition File

A [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) definition file describes the structure of a single data source. A [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) MAY have one or more data source definition files.

A dimension definition file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- DimensionDefinitionFileName = UserID "." Integer ".ds.xml"

**UserID** is an identifier that is assigned by the user to an object. The characters in **UserID** MAY[&lt;8&gt;](#Appendix_A_8) be normalized.

The content of a dimension definition file is specified in section [2.6.6](#Section_f7381e33c04e409996d45966dbd38b42).

#### Dimension Folder

A model MUST contain one or more dimension folders. A model MUST have one dimension folder per table in the model instance.

The dimension folder name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- DimensionFolderName = TableID "." "0" "." "dim"

**TableID** is the name assigned by the user to a table in an instance of the power pivot model.

##### Metadata Files

The following subsections specify file name generation for metadata files that are contained in the dimension folder.

###### Table Metadata Files

A table metadata file MUST be generated for each table that is part of the model.

The table metadata file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- TableMetadataFileName = TableID "." Integer "." "tbl" "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the table metadata file is specified in section [2.5.3](#Section_d3f931058b2a4727955605f06ecd9f06).

###### Table Information File

A table information file MUST be generated for each table that is part of the model.

The table information file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- TableInfoFileName = "info" "." Integer "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the table information file is specified in section [2.6.10](#Section_5f09e82293fe4ac594b862313205eda1).

###### Table Relationship File

If a table has a defined relationship, a table relationship file MUST be generated.

The table relationship file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- RelId = UserID
- TableRelationshipFileName = "R\$" TableID "\$" RelID "." Integer "." "tbl" "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the table relationship file is described in section [2.5.3](#Section_d3f931058b2a4727955605f06ecd9f06).

###### Column Hierarchy Files

A column [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) file MUST be generated for each column in a table.

The column hierarchy file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rules:

- ColID = UserID
- ColHierFileName = "H\$" TableID "\$" ColID "." Integer "." "tbl" "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the column hierarchy file is specified in section [2.5.3](#Section_d3f931058b2a4727955605f06ecd9f06).

###### User Hierarchy Metadata File

If a table has a user-defined hierarchy, a user [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) metadata file MUST be generated.

The user hierarchy metadata file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rules:

- HierID = UserID
- UserHierFileName = "U\$" TableID "\$" HierID "." Integer "." "tbl" "." "xml"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the user hierarchy metadata file is described in section [2.5.3](#Section_d3f931058b2a4727955605f06ecd9f06).

##### Data Files

The following subsections specify file name generation for data files that are contained in the dimension folder.

###### Column Data Files

A data file MUST be generated for each column in a table.

The column data file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- ColDataFileName = Integer "." TableID "." ColID "." "0" "." "idf"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the column data file is specified in section [2.3.1](#Section_4d3887f864c84dbd9a02e4e95e64bfed).

###### Table Relationship Index File

A table relationship index file MUST be generated for a table if it has a defined relationship to another table in the model.

The table relationship index file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- TableRelationshipFileName = Integer "." "R\$" TableID "\$" RelId "." "INDEX" "." "0" "." "idf"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the table relationship index file is specified in section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

###### Column Hierarchy Position-to-Identifier File

A column [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) position-to-identifier file MUST be generated for each column in a table.

The column hierarchy position-to-identifier file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rules:

- ColHierPosToIDFileName = Integer "." "H\$" TableName "\$" ColName "." "POS_TO_ID" "." "0" "." "idf"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the column hierarchy position-to-identifier file is specified in section [2.4.1](#Section_a1207fafbbd8410aba43656b21f8a59d).

###### Column Hierarchy Identifier-to-Position File

A column [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) identifier-to-position file MUST be generated for a column if a dictionary file is also generated. To determine when the metadata indicates that a dictionary has been generated, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

The column hierarchy identifier-to-position file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- ColHierIDToPosFileName = Integer "." "H\$" TableID "\$" ColID "." "ID_TO_POS" "." "0" "." "idf"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the column hierarchy identifier-to-position file is specified in section [2.4.2](#Section_54a5d3d8c1bf4723af2f317577cf12b7).

###### Column Hierarchy Hash Table

A column [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) hash table file can be generated for a column, depending on the data that is contained in the column. A column hierarchy hash table file MUST be generated if the metadata indicates that a hash data dictionary is used (see sections [2.5.2.20](#Section_7c56429473e64d268b48b0cd805bfb37), [2.5.2.21](#Section_79da4414b5484bedbfec2ed201436757), and [2.5.2.22](#Section_050af63085a54890a48f190e24ec69a0)).

The column hierarchy hash table file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- ColHierHashTableFileName = Integer "." "H\$" TableID "\$" ColID "." "hidx"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the column hierarchy hash table file is specified in section [2.3.3](#Section_582bda42d62f4ce0998551fb88fe68ee).

###### Column Hierarchy Dictionary

A column [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) dictionary file can be generated for a column, depending on the data that is contained in the column. A column hierarchy dictionary file MUST be generated if the metadata indicates that a value data dictionary is used (see sections [2.5.2.18](#Section_97b3069230234d1cbf438d6b7d86ae1f) and [2.5.2.19](#Section_6cc04ca990fd452e9fe881591a8aeb76)).

The column hierarchy dictionary file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- ColHierDictionaryFileName = Integer "." TableID "." ColID "." "dictionary"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the column hierarchy dictionary file is specified in section [2.3.2](#Section_d6de072d52344099b090528322f829dc).

###### User Hierarchy Files

User-defined hierarchies comprise an optional feature that can be defined for a table.

Child Count File

A user hierarchy child count file MUST be generated if a user-defined [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) is present.

The user hierarchy child count file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- UserHierChildCountFileName = Integer "." "U\$" TableID "\$" HierID "." "CHILD_COUNT" "." "0" "." "idf"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the user hierarchy child count file is specified in section [2.4.4.1](#Section_f7775057e7564d06a45b1c1ff3422dfc).

First Child Position File

A user hierarchy first child position file MUST be generated if a user-defined [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) is present.

The user hierarchy first child position file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- UserHierFirstChildPosFileName = Integer "." "U\$" TableID "\$" HierID "." "FIRST_CHILD_POS" "." "0" "." "idf"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the user hierarchy first child position file is specified in section [2.4.4.2](#Section_1d0483a24ddd43dc8316c9527a8ca346).

Parent Position File

A user hierarchy parent position file MUST be generated if is a user-defined [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) is present.

The user hierarchy parent position file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- UserHierParentPosFileName = Integer "." "U\$" TableID "\$" HierID "." "PARENT_POS" "." "0" "." "idf"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the user hierarchy parent position file is specified in section [2.4.4.4](#Section_a2ec84d242f84a5393ca61b2be23b603).

Multilevel Identifier File

A user hierarchy multilevel identifier file MUST be generated if a user-defined [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) is present.

The user hierarchy multilevel identifier file name is generated as specified by the following [**ABNF**](#gt_24ddbbb4-b79e-4419-96ec-0fdd229c9ebf) rule:

- UserHierMultiLevelIdFileName = Integer "." "U\$" TableID "\$" HierID "." "MULTI_LEVEL_ID" "." "0" "." "idf"

**Integer** is an internal version number that is assigned by the system to each version of this object. This version number does not have to match the version number of other objects in the same model.

The content of the user hierarchy multilevel identifier file is specified in section [2.4.4.3](#Section_2fc33dd59a1a49779bdc9fcb57f14ed8).

## Storage of Data Values

Data is stored in the system by column. Each table is separated into its constituent columns, and a separate set of files is generated to represent the data in each column. Every unique row value in a column is assigned a data identifier. The data identifier values comprise a contiguous range of integers, which can start at any value. Data identifiers are represented as signed 32-bit integers and, as such, are limited to that addressable range.

The data in each column is evaluated heuristically and is either hash encoded or value encoded. String data is always hash encoded. Nonstring data can be either hash encoded or value encoded. Except for the hash dictionary and the value dictionary, all data is represented by data identifier and not by value.

All the column data storage files are stored with compression. Other files might or might not use compression. Different compression methods are used, depending on the file's data. Different file types, or even different files of the same type, have different requirements regarding which compression formats are allowed. For more information about the types of compression that are available for use, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

All the file formats use [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7) format.

The file format layouts are platform independent. A file that is written on one supported platform-for example, a 32-bit computer-is readable on a different, supported platform, such as a 64-bit computer, and vice versa.

Each column has an associated file that describes the metadata for the column. The file format for column metadata storage is plaintext XML. It is necessary to reference the XML metadata file to understand and decode the contents of the data files for the column. The identification of the proper XML file to use to decode a column data file is explained in section [2.2](#Section_f629ebb97cf2410fb56b2edce58dbcc9). The content of the column metadata XML file is explained in section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

### Column Data Storage

A column data storage file for each column in the source data table MUST be present. A separate file is used to store the column data for each column. An example of a generated file name for a column data storage file for a table that has the identifier "Table1" and a column that has the identifier "Cat" is 4.Table1.Cat.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2](#Section_f629ebb97cf2410fb56b2edce58dbcc9).

The system represents each unique data value in a column by an assigned data identifier for that unique value. In the [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) file format, the data identifier is always stored, but the data value is not stored. To decode the data identifiers into their actual values, the data dictionary (section [2.3.2](#Section_d6de072d52344099b090528322f829dc)) or value hash index (section [2.3.3](#Section_582bda42d62f4ce0998551fb88fe68ee)) is used. The system MAY[&lt;9&gt;](#Appendix_A_9) use any method for assigning data identifiers to values.

The column data file contains an array of the data identifier values that represent the values contained in each row of the column in the source data. In this file, one data identifier is represented per row in the source data column. The order in which the data identifiers appear can vary from the order in which they appear in the rows of the source data table. Partial sorting of values MAY[&lt;10&gt;](#Appendix_A_10) be performed to optimize compression.

The column data storage file is compressed by one of several methods, although it is always compressed by using a XMHybridRLE compression method (except for the special case of the **RowNumber** column, which uses XM123 compression as part of a hybrid). For a discussion of the types of compression that are available to be used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to understand and decode the contents of the column data storage file. An example of a file name for the file that contains the metadata for the data storage file for a table that has the identifier "Table1" is Table1.1.tbl.xml. The metadata file contains the metadata for all the columns of the table. For example, the metadata for the column "Cat" in table "Table1" is found in the **Columns** collection of the **XMSimpleTable** object in the metadata file. In the **Columns** collection, a **Column** item exists for every column in the table. The **Column** item in the **Column** collection for which the value of the **name** attribute is "Cat" contains the metadata for the "Cat" column. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

#### File Layout for Column Data Storage Files

All files with the .idf file name extension have the same file format layout. The meaning of the contents of the file depends on the type of file-for example, for a column data storage file, see section [2.3.1](#Section_4d3887f864c84dbd9a02e4e95e64bfed).

An .idf file is always compressed. The type of compression can vary. The compression can be XMHybridRLE compression (see section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b)), XMRENoSplit compression (see section [2.7.1](#Section_85c2024e34e743748fa08b4ca8fe4f2d)), or [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480) that uses XM123 compression if the file is a **RowNumber** column (see section [2.7.2](#Section_c6e2e96740c24b7da473c22621f30654) and section [2.7.3.16](#Section_1cf84136dae246ee99de91fb24fbffc4)). An .idf file is also divided into segments. Each segment contains a contiguous slice of rows for the specific column. An .idf file always contains at least one segment and possibly more. Segments are not identical. They can vary in both size (that is, the number of rows in the segment) and the compression method that is used to compress the data in the segment. The XML metadata for each segment specifies the compression method that is used (see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246)).

The first 8 bytes of each segment indicates the segment size in units. Each unit is 8 bytes. Therefore, the segment size multiplied by the unit size is the additional size of that segment when persisted to disk (in the file). For example, if the first 8 bytes of a particular segment is set to 0x02, 2 units exist, which translates into a segment size of 16 bytes. Following the first 8 bytes are 16 more bytes that contain the actual segment data. The first 8 bytes of a segment are not included in the overall segment size value that it holds. It is possible for a segment to be zero in size. In that case, the initial 8 bytes indicates this fact-that is, the 8 bytes are set to zero to indicate a segment size of zero. For an example of the general layout of an .idf file, see section [2.3.1.1.1](#Section_c049dea7d43442eb990362c1b53b89fb).

The segment size MUST accurately indicate the size of that segment in the .idf file; otherwise, a file validation error could occur. In particular, segments that use XMHybridRLE compression depend on the segment size to be accurate, and if it is not, data errors that occur when reading the file could cause data corruption or failure errors later.

The segment size refers to the size of the compressed segment when it is persisted to disk. This size differs from the size that a segment can be in memory. Because these in-memory segment sizes matter, they will be discussed here as well.

The size of an in-memory segment can vary, and its size is measured in rows. All in-memory segments that belong to the same column MUST be of equal size. Additionally, all in-memory segments have a minimum size and a maximum size that are measured in rows. All in-memory segments MUST also have a row count that is a power of two.

Two exceptions to these rules exist. First, the last segment does not have to comply with these restrictions. Second, segments that are compressed with a hybrid compression MUST treat both the primary segment and the sub segments as one unit, and the unit as a whole MUST meet these restrictions (except for the last primary segment and subsegment in that series of hybrid compressed segments). For more information about the segment size restrictions, including the exact values for the minimum and maximum rows that are required, see section [2.3.1.1.3](#Section_66a47541c99e4140b937ceb44385af39).

Regarding the column data storage file type, a column data storage .idf file is always compressed by using XMHybridRLE compression. Therefore, a column data storage file has a minimum of two segments. The first segment (the primary segment) is for the RLE part of the compression, and the second segment (the subsegment) is for the XMRENoSplit bit packing part of the compression. However, the layout of the primary segment does not include any size information regarding its subsegment. The subsegment, like its primary segment, follows the basic layout of all segments. This means that the first 8 bytes of the subsegment contains the size of the subsegment, just as the first 8 bytes of the primary segment contains only the size information for the primary segment (and thus excludes any size information for the subsegment). For an example of the general layout of an .idf file that uses hybrid compression, see section [2.3.1.1.2](#Section_21b1aa154c494f98951affa823f5ecd9). For more information about the hybrid compression of segments, see section 2.7.3.

Any unused trailing bytes within a segment are padded with zeros, but this padding is handled within the compression process. Extra padding with zeros could also exist at the end of the file, and this padding is not accounted for in any segment size value. However, unaccounted-for padding between segments cannot exist. The end-of-file padding is not included in the segment size calculation and is ignored if present.

##### General Layout of an .idf File

The following diagram shows the general layout of an .idf file. This layout applies to any .idf file.

| 0                  | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| SegmentSize        |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Segment (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| SegmentSize        |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Segment (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**SegmentSize (8 bytes):** The size of the segment that immediately follows this field.

**Segment (variable):** A segment. The size is specified by the value of the preceding **SegmentSize** field.

**SegmentSize (8 bytes):** The size of the segment that immediately follows this field.

**Segment (variable):** A segment. The size is specified by the value of the preceding **SegmentSize** field.

##### General Layout of an .idf File That Uses Hybrid Compression

The following diagram provides an example layout of a column data storage .idf file that has two primary segments and two sub segments.

| 0                     | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| SegmentSize           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Segment (variable)    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| SegmentSize           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| SubSegment (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| SegmentSize           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Segment (variable)    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| SegmentSize           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| SubSegment (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**SegmentSize (8 bytes):** The size of the primary segment that immediately follows this field.

**Segment (variable):** A primary segment. The size is specified by the value of the preceding **SegmentSize** field.

**SegmentSize (8 bytes):** The size of the subsegment that immediately follows this field.

**SubSegment (variable):** A subsegment that is associated with preceding primary segment. The size is specified by the value of the preceding **SegmentSize** field.

**SegmentSize (8 bytes):** The size of the primary segment that immediately follows this field.

**Segment (variable):** A primary segment. The size is specified by the value of the preceding **SegmentSize** field.

**SegmentSize (8 bytes):** The size of the subsegment that immediately follows this field.

**SubSegment (variable):** A subsegment that is associated with preceding primary segment. The size is specified by the value of the preceding **SegmentSize** field.

##### Segment Size Limitations for .idf Files

Segments in .idf files MUST follow certain size rules. First, all in-memory segments that belong to the same column (that is, the same .idf file when persisted to disk) MUST be of equal size. Second, all in-memory segments have a minimum size of 16,384 rows and a maximum size of 16,777,216 rows. Third, all in-memory segments MUST have a row count that is a power of two.

Only two exceptions to these segment size requirements exist.

First, the last segment of a partition does not need to be within the range of the minimum and maximum row counts, nor does it need to have a row count that is a power of two. The last segment can even be of zero size (the case of the last segment as an empty segment).

Second, when using [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480), both a primary segment and a subsegment that is associated with the primary segment exist. These two segments MUST be considered one unit when applying these rules because the two segments represent data from the same column.

The case of the last segment as an empty segment can occur when an empty table (that is, a table with no rows) exists. The reason is that every column belonging to that table MUST have at least one segment, and every column is required to have a column data storage file (.idf file). Therefore, the first segment is also the last segment and can bypass the restrictions, and therefore be zero (empty). In other words, because the two segments are treated as one unit, both the primary (RLE) segment and the subsegment (bit packing subsegment) are zero (empty).

Note again that this limitation for segments is measured in rows, not in 8-byte units. The reason is that the size of a row is variable, because the particular column might be a column of floating point values, integers, strings, or BLOBs. However, if these row count requirements are adhered to, the compressed segments (which are persisted to the Spreadsheet Data Model file as streamed-in .idf files) will be correct and will not generate any errors or undefined behavior when the file is read.

### Column Data Dictionary

Column data can have an associated data dictionary file generated. An example of a generated file name for a dictionary file for a table that has the identifier "Table1" and a column that has the identifier "Label" is 4.Table1.Label.dictionary. For an explanation of the interpretation of the substrings within the file name, see section [2.2](#Section_f629ebb97cf2410fb56b2edce58dbcc9).

The data dictionary contains information that is used to decode the value in the source data that a data identifier represents. The data dictionary file contains an array of unique values that appear in the source data. The file is ordered by data identifier so the first value in the file represents the lowest data identifier, the second value in the file represents the next-lowest data identifier, and so on. Dictionaries that contain only integer or floating point data are not compressed. Dictionaries that contain strings might have parts of the dictionary that are compressed. In the case of dictionaries that contain strings or BLOBs, although most parts of the dictionary file are not compressed, the specific strings or BLOBs might be compressed by using a Huffman compression. BLOBs are pre-encoded by means of [**base64 encoding**](#gt_179b9392-9019-45a3-880b-26f6890522b7) and are therefore treated as strings (and stored in a string dictionary). For a discussion of the type of Huffman compression that is used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to determine whether a data dictionary file is present for a data column. This metadata is contained in the same file as the column data storage file metadata (see section [2.3.1](#Section_4d3887f864c84dbd9a02e4e95e64bfed)). If a particular **XMRawColumn** object-specifically, the **XMRawColumn** object of the **Column** item in the **Columns** collection that has a name equal to the column name-has a **DataObject** in the **DataObjects** collection for which the value of the **class** attribute equals one of the values in the following list, the column MUST have a column data dictionary file generated.

- **XMHashDataDictionary&lt;XM_Real&gt;** (section [2.5.2.19](#Section_6cc04ca990fd452e9fe881591a8aeb76))
- **XMHashDataDictionary&lt;XM_Long&gt;** (section [2.5.2.18](#Section_97b3069230234d1cbf438d6b7d86ae1f))
- **XMHashDataDictionary&lt;XM_String&gt;** (section [2.5.2.22](#Section_050af63085a54890a48f190e24ec69a0))

For an explanation of how to interpret the XML metadata file see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

#### File Layout for a Column Data Dictionary

The column data dictionary file format layout varies depending on the type of dictionary that is persisted to the file. Dictionaries can be of type integer, real, or string, the latter of which includes BLOBs because they are precompressed by means of [**base64 encoding**](#gt_179b9392-9019-45a3-880b-26f6890522b7).

The first element in a dictionary file (that is, a file that has the .dictionary file name extension) is an enumeration value. Because the size of an enumeration value depends on the compiler, the number of bytes to be read (or written) is variable. For example, on a 32-bit system or application, a standard enumeration value is 4 bytes, unless it is specifically declared to use some other integer value. A standard enumeration value also defaults to 4 bytes on a 64-bit system or application, unless otherwise specified. The enumeration value used here defaults to 4 bytes.

The **XM_TYPE** enumeration (section [2.3.2.1.3.1](#Section_619a632a09a54d8780faf5c0fc9c2ded)) consists of four values, ranging from -1, which implies an invalid type, through the integer, real, and string types.

Depending on the dictionary type, the specifics of the file format layout vary. There are two basic cases: dictionaries of type integer (**XM_TYPE_LONG**) or real (**XM_TYPE_REAL**), and dictionaries of type string (**XM_TYPE_STRING**). For more information about the former, see section [2.3.2.1.1](#Section_f089c2a04f114cbeb2d389eabf62373c). For more information about the latter, see section [2.3.2.1.2](#Section_c1ebc0f5ccb14d14a6b59276aed28872).

The following diagram shows this first element (the dictionary type) in a dictionary file. The type is followed by any hash information (section [2.3.3.1.1](#Section_9acdddc2f21c444393cee73879e9dc63)), which is then followed by the main part of the dictionary.

| 0                          | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| DictionaryType             |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashInformation (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                        |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Dictionary (variable)      |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                        |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**DictionaryType (4 bytes):** The dictionary type. The value can be **XM_TYPE_LONG**, **XM_TYPE_REAL**, **XM_TYPE_STRING**, or **XM_TYPE_INVALID**.

**HashInformation (variable):** The hash information that is required for all dictionaries. An **XM_TYPE_STRING** dictionary has the option of not including any hash information in certain situations. For more information, see section [2.3.2.1.2.2](#Section_2bd1b39d0d654d3ab8f6a52aa7d1152a).

**Dictionary (variable):** The dictionary store. If the value of **DictionaryType** is **XM_TYPE_STRING**, this store consists of information, pages, and records. If the value of **DictionaryType** is **XM_TYPE_REAL** or **XM_TYPE_LONG**, this store consists of information plus numeric items and values.

##### XM_TYPE_LONG and XM_TYPE_REAL Data Dictionary Files

For a dictionary of type **XM_TYPE_LONG**, if the **OperatingOn32** element (section [2.5.2.21.1](#Section_ca80e0f9fc804f4d983b450c40357f1f)) is set to **true**, the dictionary will use 4-byte integers. If this element is set to **false**, the dictionary will use 8-byte integers. This change has an effect on how values, potentially including any hash information, are stored and interpreted in the file.

Note that the sizes of the first required five elements of the hash (see section [2.3.2.1.1.1](#Section_7ee54b7dd64941e59b53aa4a7deb9ecc)) are not affected by this information. The values that are contained by the hash bin and hash entry structure size elements (that is, two of the five elements) are affected, but the sizes are not.

The values that are contained by each of the required hash elements MUST be correct; otherwise, a file validation error could occur. For more information about the **XM_TYPE_LONG** and **XM_TYPE_REAL** hash data dictionary XML metadata values, see section [2.5.2.21](#Section_79da4414b5484bedbfec2ed201436757) and section [2.5.2.20](#Section_7c56429473e64d268b48b0cd805bfb37).

The following diagram shows the general layout of an **XM_TYPE_REAL** or **XM_TYPE_LONG** dictionary.

| 0                          | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| DictionaryType             |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashInformation (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                        |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| VectorOfValues (variable)  |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                        |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**DictionaryType (4 bytes):** The type of dictionary. The value MUST be **XM_TYPE_REAL** or **XM_TYPE_LONG**.

**HashInformation (variable):** The required hash elements for dictionary files.

**VectorOfValues (variable):** The set of real (64-bit) or integer (32-bit or 64-bit, depending on the range of values that are encountered) values. The values are not compressed.

###### Required Hash Elements

For integer and real dictionaries, the next five elements are hash elements (see section [2.3.3.1.1](#Section_9acdddc2f21c444393cee73879e9dc63)). For all dictionary files, the value of **cBins** MUST be set to **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT** (section [2.3.3.1.4.1](#Section_30af58add5ec4897a973525b1eef3f43)) to indicate that no further hash information is included.

The underlying system does not use any included hash information, other than the five required elements, in a dictionary. Therefore, there MUST NOT be any other hash information (other than those five elements) in a dictionary file, regardless of the type of dictionary.

###### Vector of Values

For **XM_TYPE_LONG** or **XM_TYPE_REAL** dictionaries, what now follows is a vector of either integer or double values. These values are the actual dictionary items, which are stored in a vector (or array), and are not compressed.

The number of dictionary items and the individual sizes of the dictionary items are encoded first. Therefore, at this point in the file, the next 8 bytes represent the number of elements in the vector. The following 4 bytes represent the size, in bytes, of each element in the vector. Therefore, the vector itself is of variable size-this size, in bytes, equals the number of elements multiplied by the element size.

The element size for a **XM_TYPE_LONG** dictionary also varies depending on whether the operating system is 32-bit or 64-bit because the element size reflects the size of a 32-bit integer or a 64-bit integer. For an **XM_TYPE_REAL** dictionary, the element size is the size of a double value.

The vector of values completes the format of a hash data dictionary of type **XM_TYPE_LONG** or **XM_TYPE_REAL**. Padding with zeros might exist at the end of the file, but such padding is ignored and not read.

The following diagram shows a general view of the layout of the vector of values.

| 0                         | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| elementCount              |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                       |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| elementSize               |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| VectorOfValues (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                       |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**elementCount (8 bytes):** The number of elements in the **XM_TYPE_REAL** or **XM_TYPE_LONG** dictionary.

**elementSize (4 bytes):** The size of each element.

**VectorOfValues (variable):** The vector of real or integer values in the dictionary.

##### XM_TYPE_STRING Data Dictionary Files

The layout for dictionaries of type **XM_TYPE_STRING** is different than that for dictionaries of type **XM_TYPE_LONG** and **XM_TYPE_REAL**. After the **XM_TYPE** information is read (see section [2.3.2.1](#Section_06ba2344f1464141bf5d6f9c4c53e099)), an XML metadata flag is checked to determine whether any hash information is included in the file.

For dictionaries of type **XM_TYPE_LONG** or **XM_TYPE_REAL**, this hash information is always present, but for dictionaries of type **XM_TYPE_STRING**, the information is present only if the flag value 0x01 is set in the **DictionaryFlags** element (section [2.5.2.22.1](#Section_a55c10ed5128496c884370b31a288bbd)) in the metadata for the dictionary.

For general information about **XM_TYPE_STRING** hash data dictionary metadata, see section [2.5.2.22](#Section_050af63085a54890a48f190e24ec69a0).

The following diagram shows the general layout of the **XM_TYPE_STRING** dictionary.

| 0                                  | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| DictionaryType                     |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashInformation (variable)         |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| PageLayoutInformation (variable)   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| DictionaryPages (variable)         |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| DictionaryRecordHandles (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**DictionaryType (4 bytes):** The type of the dictionary. The value MUST be **XM_TYPE_STRING**.

**HashInformation (variable):** The required hash elements.

**PageLayoutInformation (variable):** The information that pertains to the whole dictionary, excluding the hash information and the dictionary type that exist in the preceding fields. This field contains information such as whether compression is used (on at least one page), the string count, and the number of pages.

**DictionaryPages (variable):** One or more sets of information, each of which pertains to a single page. A set of information includes the string store.

**DictionaryRecordHandles (variable):** A vector of record handle structures, one per string.

###### BLOBs and Base64 Encoding

BLOBs are supported and stored in the **XM_TYPE_STRING** hash data dictionary format. The reason is that BLOBs are treated in the same manner as strings because they have already been encoded by using [**base64 encoding**](#gt_179b9392-9019-45a3-880b-26f6890522b7) before storage into a dictionary file.

BLOBs stored in Spreadsheet Data Model files MUST be encoded by using base64 encoding prior to any other compression and storage. For information about the Spreadsheet Data Model file format, see section [2.1](#Section_49ca8d5609274cb2ad97bf73f0d91536).

If BLOBs are being stored in an **XM_TYPE_STRING** hash data dictionary, the flag value 0x100 MUST be set in the **DictionaryFlags** element in the metadata for the dictionary (see section [2.5.2.22.1](#Section_a55c10ed5128496c884370b31a288bbd)).

Because they are strings (with only 64 character symbols used), BLOBs can also be compressed by using Huffman compression. So if compression is used on the string store, both the strings and the BLOBs will be compressed by using Huffman compression if they fall within all of the Huffman compression constraints.

For more information about **XM_TYPE_STRING** hash data dictionary metadata, including the dictionary flags that need to be set, see section [2.5.2.22](#Section_050af63085a54890a48f190e24ec69a0). For more information about the Huffman compression that is used, see section [2.7.4](#Section_f70b41f2ca6444a19e6f53e63f6a5ee9).

###### Required Hash Elements

If the flag value 0x01 (section [2.5.2.22.1](#Section_a55c10ed5128496c884370b31a288bbd)) is set, the file contains the five required hash elements, and the system will rebuild the hash table for the dictionary at run time-thus allowing fast lookups into the string dictionary, even if the dictionary has duplicate strings.

If the flag value 0x01 is not set, no hash information is contained in the file. This behavior is different than that for the **XM_TYPE_LONG** and **XM_TYPE_REAL** dictionaries (section [2.3.2.1.1.1](#Section_7ee54b7dd64941e59b53aa4a7deb9ecc)).

If the flag value 0x01 is not set, and therefore the five required hash elements are not included, no lookups will be allowed in the dictionary. Thus, it will be assumed that the dictionary contains only unique strings (so that no collisions will occur by having two strings that are identical but now cannot be correctly identified without hash information).

However, when the flag is set, only the first five (required) hash elements are present, and **cBins** MUST be set to the **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT** value (section [2.3.3.1.4.1](#Section_30af58add5ec4897a973525b1eef3f43)) to indicate that no further hash information is included.

The underlying system does not use any included hash information, other than the five required elements, in a dictionary. Therefore, there MUST NOT be any other hash information (other than those five elements) in a dictionary file, regardless of the type of dictionary.

For information about the required hash elements, see section [2.3.3.1.1](#Section_9acdddc2f21c444393cee73879e9dc63). For how this information is treated by the **XM_TYPE_LONG** and **XM_TYPE_REAL** hash data dictionaries, see section 2.3.2.1.1.1.

###### Dictionary Page Layout

**XM_TYPE_STRING** dictionaries (also referred to as _string dictionaries_) use a page system. This system is similar to the one in which column data storage files (.idf files) use segments (see section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e)). However, the two systems are not identical. Dictionary pages ought not to be confused with operating system pages.

An **XM_TYPE_STRING** dictionary divides the strings into pages. Each page can be of variable size within certain limitations. For more information about dictionary page sizes and the page count limit, see section [2.3.2.1.3.2](#Section_7adea9d000924f3883b3dbc31ac96551).

Each page can be compressed or not, independent of any other page. The compression that is used for string dictionary pages is a variation of Huffman compression, which is a widely known compression algorithm that is often used for compressing strings. The Huffman compression procedure that is used depends on whether the string is considered to originate from a single [**character set**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204) (such as ASCII-US or [**Unicode**](#gt_c305d0ab-8b94-461a-bd76-13b40cb8c4d8) using just the ASCII-US set) or from multiple character sets. Not all character sets, even though they are Unicode, can be compressed via this Huffman implementation. For more information about the Huffman compression algorithm that is implemented, see section [2.7.4](#Section_f70b41f2ca6444a19e6f53e63f6a5ee9). For particular information regarding the implications of character set choice, see section [2.7.4.1.4](#Section_3325dd4cbc9646c18c6b69394073c840).

Following any hash information in the file (see section [2.3.2.1.2.2](#Section_2bd1b39d0d654d3ab8f6a52aa7d1152a)), the subsequent fields consist of general information regarding the entire dictionary string store. Information that is specific to each page within the dictionary is discussed separately (section [2.3.2.1.2.4](#Section_a1df1ca8e942405f87f0959bdf047139)).

The next 8 bytes indicate the number of strings in the dictionary store. This value applies to the entire string store in the dictionary, so it includes all the pages in the string store. The following byte is a Boolean flag that indicates whether the store has compressed pages. If this value is set to **true**, at least one page in the dictionary's string store is compressed, but it does not necessarily mean that all the pages are compressed. The next 8 bytes indicate the length, in characters, of the longest string in the entire store. The final 8 bytes indicate the total number of pages in the dictionary's string store.

The following diagram shows the layout of the elements just discussed, beginning with the number of strings in the dictionary string store and ending with the total page count for the string store.

| 0                | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8                  | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| StoreStringCount |     |     |     |     |     |     |     |                    |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...              |     |     |     |     |     |     |     |                    |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| fStoreCompressed |     |     |     |     |     |     |     | StoreLongestString |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...              |     |     |     |     |     |     |     |                    |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...              |     |     |     |     |     |     |     | StorePageCount     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...              |     |     |     |     |     |     |     |                    |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...              |     |     |     |     |     |     |     |

**StoreStringCount (8 bytes):** The number of strings in the entire dictionary store (that is, in all the pages).

**fStoreCompressed (1 byte):** Boolean. A flag that indicates whether at least one page in the store is compressed. If the value is **true**, at least one page in the store is compressed.

**StoreLongestString (8 bytes):** The longest string, in number of characters, in the entire store.

**StorePageCount (8 bytes):** The number of pages in the entire dictionary store.

###### Dictionary String Store (Per Page) Information

Each page has the same format, beginning with general information for the page and then including the actual stored strings, either compressed or uncompressed depending on whether the page is marked as compressed.

Therefore, for each page, the first 8 bytes contain the mask state information for the page. This mask indicates whether the page is compressed by using Huffman compression. (In contrast, the **fStoreCompressed** flag (section [2.3.2.1.2.3](#Section_de4ba19dfeba43e584c1622878bdd1a3)) simply indicates whether at least one page is compressed.) For more information about the values that this mask can hold, see section [2.3.2.1.3.3](#Section_e216fe78346c47d4ad2972a7d62865af).

The mask state information is followed by a single byte containing a Boolean flag that indicates whether the page contains NULL values. The next 8 bytes contain the starting index that is used for locating the first record handle structure for the strings on this page. This index is zero-based because it refers to the vector of record handle structures for the dictionary. For more information about the **XM_TYPE_STRING** dictionary vector of record handles, see section [2.3.2.1.2.5](#Section_410567dee89b4262bc7c856fcd4740e8).

Therefore, a starting index of zero refers to the first element in the record handle vector, and that indexed record handle structure is the first record handle structure for the page. As another example, a starting index of 1045 implies that index 1045 of the record handle vector contains the first record handle of the page.

The next 8 bytes indicate the number of strings that are contained on this particular page. This number is followed by another single byte containing a Boolean flag that indicates whether this particular page is compressed. Both the mask state information and this Boolean flag MUST reflect the same state (compressed or not compressed).

The final 4 bytes contain a special mark that indicates the beginning of the page's string store. This mark MUST be set to the unsigned integer value 0xAABBCCDD (in decimal, 2,864,434,397).

After all the strings, another special mark indicates the end of the page's string store and the beginning of the next page (see section [2.3.2.1.2.4.3](#Section_b474383d769b4d34b666e1fc712779b7)).

For more information about the strings stored on uncompressed pages, see section [2.3.2.1.2.4.1](#Section_7a7bef7c1cca4594a811ee2128a89ce4). For more information about the strings stored on compressed pages, see section [2.3.2.1.2.4.2](#Section_64985b36dd1b44c48e241e7d00d8eb3f). For more information about the second string store page marker, see section 2.3.2.1.2.4.3. For more information about the record handles vector information that is stored at the end of a dictionary file, see section 2.3.2.1.2.5.

The following diagram shows a general layout of the page components just discussed.

| 0                  | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8               | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6                      | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ---------- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| PageMask           |     |     |     |     |     |     |     |                 |     |            |     |     |     |     |     |                        |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |                 |     |            |     |     |     |     |     |                        |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| PageContainsNULLs  |     |     |     |     |     |     |     | PageStartIndex  |     |            |     |     |     |     |     |                        |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |                 |     |            |     |     |     |     |     |                        |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     | PageStringCount |     |            |     |     |     |     |     |                        |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |                 |     |            |     |     |     |     |     |                        |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     | PageCompressed  |     |            |     |     |     |     |     | StringStoreBeginMark   |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |                 |     |            |     |     |     |     |     | StringStore (variable) |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                |     |     |     |     |     |     |     |                 |     |            |     |     |     |     |     |                        |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| StringStoreEndMark |     |     |     |     |     |     |     |                 |     |            |     |     |     |     |     |                        |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**PageMask (8 bytes):** The mask state information for this page.

**PageContainsNULLs (1 byte):** A Boolean flag that indicates whether the page contains NULL values. If the value is **true**, the page contains NULL values.

**PageStartIndex (8 bytes):** The starting index of the first record handle structure for the strings on this page.

**PageStringCount (8 bytes):** The number of strings on this page.

**PageCompressed (1 byte):** A Boolean flag that indicates whether the page is compressed. If the value is **true**, the page is compressed.

**StringStoreBeginMark (4 bytes):** A special mark that indicates the beginning of the actual strings in the store for this page.

**StringStore (variable):** The string store (that is, the actual strings in the store).

**StringStoreEndMark (4 bytes):** The special mark that indicates the end of the string store for this page.

Uncompressed Page Case

When the page is not compressed, the next 8 bytes after the general per-page information (section [2.3.2.1.2.4](#Section_a1df1ca8e942405f87f0959bdf047139)) indicate the number of characters that can still be stored on the page. In other words, these 8 bytes indicate the remaining amount of room, in characters, that are available in the store. This value is based on the page size, the current number of characters in the store, and other page information that is taking up room on the page.

These characters are of type **\_TCHAR** (section [2.1.1.2](#Section_9ac4d0fc21ee4ae4ba7cb1f782ad1a45)). The bytes are treated simply as a stream of characters of type **\_TCHAR**, without any knowledge of the actual bytes used per character symbol or of the [**character set**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204) that is used. Internally, the system uses [**Unicode**](#gt_c305d0ab-8b94-461a-bd76-13b40cb8c4d8).

The next 8 bytes contain the number of used characters in the stored character buffer. This value represents the number of characters in the string store buffer that have already been stored. It also represents the next free offset that can be written to. The value MUST be accurate, and the implied size (number of characters multiplied by the size of one character) MUST NOT exceed the actual allocated buffer size.

The next 8 bytes indicate the allocation size, in bytes, that is needed to hold the buffer of string character data. This value is followed by the set of uncompressed strings as one long byte buffer. The number of bytes in this byte buffer is defined by the allocation size. Each string in this character buffer MUST be terminated by the null character ('\\0'). All size calculations need to take this termination character requirement into account.

After this buffer, the second mark (see section [2.3.2.1.2.4.3](#Section_b474383d769b4d34b666e1fc712779b7)) is read. Then, a new page, if present, begins. This next page can again be either compressed or uncompressed.

Following the page-specific information for every page, a vector of record handles completes the dictionary file (see section [2.3.2.1.2.5](#Section_410567dee89b4262bc7c856fcd4740e8)).

The following diagram shows the layout of the uncompressed page elements just discussed.

| 0                                      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| RemainingStoreAvailable                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| BufferUsedCharacters                   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| AllocationSize                         |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| UncompressedCharacterBuffer (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**RemainingStoreAvailable (8 bytes):** The remaining number of characters that can be written to the character buffer.

**BufferUsedCharacters (8 bytes):** The number of characters that already exist in the character buffer. This value also indicates the beginning offset where additional characters can be written.

**AllocationSize (8 bytes):** The size of the character buffer.

**UncompressedCharacterBuffer (variable):** The character buffer. The size of this buffer is specified by **AllocationSize**. The buffer contains the uncompressed strings that are stored on this page. Each string in this character buffer MUST be terminated by the null character ('\\0').

Compressed Page Case

If the page is compressed, the format is more complicated than that of the uncompressed page case. The first 4 bytes contain the total number of bits in the store-that is, the bit offset of the end of the last compressed string in the store. This value is an unsigned integer value. This value is needed to determine the bits of the last string in the store, because the compressed strings are referenced by their bit offsets into the store. For all but the last string, subtracting the current string's offset from the next string's offset provides the current string's bit length.

The next 4 bytes identify the type of [**character set**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204)-in other words, the character set mode that is used. Strings can be of a single or of a multiple character set. If the character set is single, and if the single character set uses only two bytes per character (because of those two bytes, one will be the same for every character in the string), the Huffman encoding process can strip off the identifying character set information and store the one byte that identifies the character set separately from the actual stripped characters.

This procedure cannot be performed in the multiple character set case nor typically in the single character case when multibyte characters are used (in which more than one byte is used per actual character, not counting the character set identifier byte). In such situations, all the bytes MUST be stored and then used in the encoding and decoding process. Hence, the Huffman process needs to account for this difference.

The character set type identifier is an unsigned integer. For the values that identify the character set mode that is used for the page's string store, see section [2.3.2.1.3.4](#Section_77780429dd6446fb950d4770a507410a). For more information about the Huffman compression algorithm that is used, see section [2.7.4](#Section_f70b41f2ca6444a19e6f53e63f6a5ee9).

The next 8 bytes contain the allocation size, in bytes, of the actual compressed strings in the store.

If the character set mode is single, the next byte, which contains an unsigned value, indicates the character set that is used. Essentially, this byte would have been the upper byte of each character in the single character set string. If the character set mode is multiple, this byte MUST NOT be present in the file layout.

The next 4 bytes (**uiDecodeBits**) contain the maximum number of bits that are used to create a fast lookup table for Huffman decoding. This number is also referred to as the codeword length. The value is an unsigned integer. The valid range for **uiDecodeBits** is from 2 through 12. Although Huffman encoding supports codewords of 2 through 15 bits, the lookup table supports only 2 through 12 bits, and any codewords that use lengths greater than 12 (or possibly less in some cases) will be decoded through a Huffman tree traversal (rather than through the faster lookup table). This value does not reflect the actual size of the codewords that are used if the longest codeword is greater than 12, but this value MUST NOT be set any higher than 12. For more information about how this value is set and what its effects are, see section [2.7.4.1.2](#Section_690e69ab8041455fbbcc2f9cb6ebc839).

The next 128 bytes (**encodeArray**), which are read as a stream of unsigned 8-bit integer values, contain the encoded Huffman alphabet as an array. The system uses a Huffman alphabet of 256 characters, which is stored in an unsigned 8-bit integer array. This array contains the codeword length for each element in the alphabet.

The next 8 bytes (**ui64BufferSize**) contain an unsigned integer that indicates the size, in 8-bit integer units, of the buffer of the compressed strings. This value is expected to be the same as that of **AllocationSize**. Because the buffer consists of a stream of bytes, and the size of a byte is the same as the size of an unsigned 8-bit integer, this value is the same as the number of bytes that are needed to create that buffer.

The next set of bytes contains the set of compressed strings for the compressed page. The number of bytes equal the value of **ui64BufferSize**. These strings are compressed by using a constrained version of classic Huffman compression, which requires the encoded array to correctly decode the strings. Therefore, the information here MUST NOT be altered between the writing of the file by the system and the next reading of the file; otherwise, the decompression of the strings might fail.

For more information about the Huffman compression algorithm that is used, the variables here that are related to the Huffman compression, and how to encode and decode by using this constrained Huffman implementation, see section 2.7.4.

Following the buffer, the second mark (see section [2.3.2.1.2.4.3](#Section_b474383d769b4d34b666e1fc712779b7)) is read. Then, a new page, if present, begins. Again, the next page (if present) can be either compressed or uncompressed.

Following the page-specific information for every page, a vector of record handles completes the dictionary file (see section [2.3.2.1.2.5](#Section_410567dee89b4262bc7c856fcd4740e8)).

The following diagram shows the layout of the compressed page elements just discussed.

| 0                                 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8                       | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| StoreTotalBits                    |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| CharacterSetTypeIdentifier        |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| AllocationSize                    |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| …                                 |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| CharacterSetUsed (optional)       |     |     |     |     |     |     |     | uiDecodeBits            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| …                                 |     |     |     |     |     |     |     | encodeArray (128 bytes) |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| …                                 |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| …                                 |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ui64BufferSize                    |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| …                                 |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| CompressedStringBuffer (variable) |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| …                                 |     |     |     |     |     |     |     |                         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**StoreTotalBits (4 bytes):** The total number of bits in the store.

**CharacterSetTypeIdentifier (4 bytes):** A value that identifies whether the character set mode is single or multiple.

**AllocationSize (8 bytes):** The allocation size that is needed for the string store (that is, for the buffer).

**CharacterSetUsed (1 byte):** An identifier for the character set that is used. This value applies only to the single character set mode. This value is not present if the character set mode is multiple.

**uiDecodeBits (4 bytes):** The number of bits that are used in the lookup table for Huffman decoding.

**encodeArray (128 bytes):** The encoded Huffman alphabet array for decoding.

**Ui64BufferSize (8 bytes):** The size of the character buffer. This size is expected to be the same as the allocation size.

**CompressedStringBuffer (variable):** The buffer of compressed strings for this page.

Second Mark (End of Page Marker)

At the end of each page, 4 bytes contain a special mark that indicates the end of that page's string store. This mark MUST be set to the unsigned integer value 0xABCDABCD (in decimal, 2,882,382,797). For the general layout of a dictionary page (whether compressed or uncompressed), see section [2.3.2.1.2.4](#Section_a1df1ca8e942405f87f0959bdf047139).

###### Dictionary Record Handles Vector

What follows the pages and their information in the string dictionary is a vector of record handle structures. Record handles have a one-to-one relationship with the strings in all the string stores. That is, each string has a corresponding record handle, and each record handle has a corresponding string. This correspondence exists regardless of whether the string is compressed. Each record handle contains a bit or a byte offset and a page identifier that indicates which page holds the string that is associated with that record handle. For more information, see section [2.3.2.1.3.5](#Section_b0d954db002b4f2595febf996cc4d232).

For decoding the vector, the next 8 bytes (**elementCount**) in the file represent the number of elements in the vector (or array). This value is followed by 4 bytes (**elementSize**) that indicate the size of each element in the vector. Each element in the vector is a record handle structure and as such, has the size of a record handle structure (see section 2.3.2.1.3.5). Therefore, the vector of record handles is of variable size-specifically, **elementCount** multiplied by **elementSize**.

The vector of record handles is the last item in a hash data dictionary file. Extra padding with zeros might exist at the end of the file. If present, this information is ignored and not read by the system.

The following diagram shows a general view of the record handle elements just discussed, beginning with the number of records (**elementCount**) and ending with the vector of elements. It does not show the internal details of the record handle structure.

| 0                                         | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| elementCount                              |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                       |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| elementSize                               |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| VectorOfRecordHandleStructures (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                                       |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**elementCount (8 bytes):** The number of elements in the record handle vector.

**elementSize (4 bytes):** The size, in bytes, of each element (that is, of one record handle structure).

**VectorOfRecordHandleStructures (variable):** The vector of record handle structures.

##### Dictionary Structures, Enumerations, and Constants

This section contains information that is related to the data structures, enumerations, and other constants that are used by the hash data dictionary file format.

###### XM_TYPE Enumeration

The **XM_TYPE** enumeration is used to identify the type of hash data dictionary that is stored in the dictionary file. (Dictionary files have the .dictionary file name extension.)

- enum XM_TYPE
- {
- XM_TYPE_INVALID = -1,
- XM_TYPE_LONG = 0,
- XM_TYPE_REAL = 1,
- XM_TYPE_STRING = 2
- };

The following table describes the available enumeration values.

| Enumeration value | Meaning                                                                                                               |
| ----------------- | --------------------------------------------------------------------------------------------------------------------- |
| XM_TYPE_INVALID   | The data type is invalid.                                                                                             |
| XM_TYPE_LONG      | The dictionary holds integers.                                                                                        |
| XM_TYPE_REAL      | The dictionary holds real (floating point) values.                                                                    |
| XM_TYPE_STRING    | The dictionary holds strings. The strings might or might not be compressed and are stored per page in the dictionary. |

###### Page Size Limitations for an XM_TYPE_STRING Hash Data Dictionary

Each page that is persisted to disk within an **XM_TYPE_STRING** dictionary file is of variable size, up to a page size limit of 4,294,967,296 bytes if uncompressed or 536,870,912 bytes if compressed. No minimum page size exists.

The maximum number of pages in a dictionary file is 524,288.

###### Page Mask for an XM_TYPE_STRING Hash Data Dictionary

The **XM_TYPE_STRING** page mask contains compression information for the page.

The mask information is on a per-page basis and indicates whether the strings on the page have been compressed by using Huffman compression. The default mask value indicates that the string store for the page is not compressed.

The following table contains the mask values.

| Name                                       | Value |
| ------------------------------------------ | ----- |
| **XM_STRING_STORE_PAGE_OPTION_DEFAULT**    | 0x000 |
| **XM_STRING_STORE_PAGE_OPTION_COMPRESSED** | 0x001 |

###### Huffman Character Set Mode

The [**character set**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204) mode indicates the character set characteristics of the dictionary strings on that dictionary page.

During the Huffman compression of strings, one of two possible modes can be used: a single character set mode or a multiple character set mode. The former means that only one character set is used for the strings being compressed for that page in the dictionary. The latter means that more than one character set is being used for the strings being compressed for that page in the dictionary.

Single character set and multiple character set modes can also be used for other situations, such as the use of multibyte character sets and the Huffman compression of BLOBs that use [**base64 encoding**](#gt_179b9392-9019-45a3-880b-26f6890522b7). For more information, see section [2.7.4](#Section_f70b41f2ca6444a19e6f53e63f6a5ee9).

The following table lists the character set mode values for Huffman compression.

| Name                         | Value  |
| ---------------------------- | ------ |
| **XM_HUFFMAN_SINGLECHARSET** | 703121 |
| **XM_HUFFMAN_MULTICHARSET**  | 703122 |

###### Record Handle Structures for an XM_TYPE_STRING Hash Data Dictionary

The record handle structure contains bit or byte offset information and page identifying information for a particular string in the dictionary.

The record handle has a one-to-one correspondence with a particular, unique string in an **XM_TYPE_STRING** hash data dictionary string store. One record handle exists for each string in a dictionary file.

The record handle structure that is used depends on whether the string is compressed. For compressed strings, a bit offset is used. For uncompressed strings, a byte offset is used. The size of the structure member is identical for both the bit and the byte offset. The page identifier member is identical in meaning and size in both structures.

The **XM_CompressedStringRecordHandle** structure stores the bit offset and page identifier for a compressed string that exists in the vector of record handle structures used by the **XM_TYPE_STRING** hash data dictionary.

- struct XM_CompressedStringRecordHandle
- {
- unsigned \_\_int32 bitOffset;
- unsigned \_\_int32 pageID;
- };

**bitOffset**: The compressed string bit offset, starting with zero for the first string of each page. A bit offset is relative to its page, not to the entire dictionary.

**pageID**: The page identifier, which is a zero-based index (beginning at page zero and continuing through the total number of pages for the dictionary minus one).

The **XM_ConstantStringRecordHandle** stores the byte offset and page identifier for an uncompressed string that exists in the vector of record handle structures used by the **XM_TYPE_STRING** hash data dictionary.

- struct XM_ConstantStringRecordHandle
- {
- unsigned \_\_int32 byteOffset;
- unsigned \_\_int32 pageID;
- };

**byteOffset**: The uncompressed string byte offset, starting with zero for the first string of each page. A byte offset is relative to its page, not to the entire dictionary.

**pageID**: The page identifier, which is a zero-based index (beginning at page zero and continuing through the total number of pages for the dictionary minus one).

### Column Data Hierarchy Hash Index

Column data can have an associated value hash index file generated. An example of a generated file name for a column data [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) hash index file for a table that has the identifier "Table1" and a column that has the identifier "Cat" is 1.H\$Table1\$Cat.hidx. For an explanation of the interpretation of the substrings within the file name, see section [2.2](#Section_f629ebb97cf2410fb56b2edce58dbcc9).

The column data hierarchy hash index is a hash index file of the unique data identifier values that are present in the column. The file is neither ordered nor compressed.

It is necessary to reference the XML metadata file to determine whether a column data hierarchy hash index file is present. If a particular **XMRawColumn** object-specifically, the **XMRawColumn** object of the **Column** item in the **Columns** collection that has a name equal to the column name-has a **DataObject** in the **DataObjects** collection for which the class="XMValueDictionary&lt;XM_Real&gt;" (section [2.5.2.19](#Section_6cc04ca990fd452e9fe881591a8aeb76)) or for which the class="XMValueDictionary&lt;XM_Long&gt;" (section [2.5.2.18](#Section_97b3069230234d1cbf438d6b7d86ae1f)), the column MUST have a column data hierarchy hash index file generated. For an explanation of how to interpret the XML metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

#### File Layout for Hash Index Files

Unlike .idf files or **XM_TYPE_STRING** type dictionary files, hash index files-that is, files that have the .hidx file name extension-do not use any compression.

The description of the hash index file format layout (also referred to as the .hidx file format) is divided into sections.

##### Required Elements for All Files That Use Hashing

This section pertains to hash information that MUST be present in any file that uses a hash. Such files have either the .hidx or the .dictionary extension. These files include column data [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) hash index files (section [2.3.3](#Section_582bda42d62f4ce0998551fb88fe68ee)), relationship hash index files (section [2.4.3](#Section_55a2b0ea2fd84b2f84d1736648f0f8fd)), and dictionary files (section [2.3.2.1](#Section_06ba2344f1464141bf5d6f9c4c53e099)).

Whenever a hash is used (except in the case of dictionaries of type **XM_TYPE_STRING** as specified in section [2.3.2.1.2](#Section_c1ebc0f5ccb14d14a6b59276aed28872)), the first five elements of the hash table MUST be present. These elements are described in the remainder of this section.

The first 4 bytes represent an enumeration value that either identifies the hash algorithm used or equals the **XM_INVALID** value, which indicates that no hashing algorithm was specified in the persisted file. In most cases, there is no choice for the hashing algorithm, so the hashing algorithm does not need to be saved for future reference. However, this algorithm MUST be specified correctly; otherwise, an error could occur. For more information about the hash algorithm enumeration, see section [2.3.3.1.4.2](#Section_22bdc92aaeb04d88b62fb62482ded7ec).

Dictionary files need to include only the first five required elements, so no knowledge of the actual hashing algorithm (that is, the actual procedural code used) is needed. However, in hash index files (.hidx files), full hash information is required, so the actual hashing algorithm used to create this information MUST be the one that is specified in section [2.3.3.1.3](#Section_8a8986c9f09942a6a6ed27dfb9a1bafa). This hashing algorithm is the one that the system uses and expects. Also, as specified in the hash algorithm enumeration (section 2.3.3.1.4.2), the hash algorithm identifier is set to **XM_INVALID**.

The next 4 bytes contain the size, in bytes, of the **HashEntry** hash entry structure (section [2.3.3.1.4.5](#Section_db8c786ea4714458924d6807c8cf6a1d)). Each hash entry structure is this size, which is referred to here as **HashEntrySize**. This size varies depending on the hash policies that are in place. For more information about the **HashEntry** structure and hash policies, see section 2.3.3.1.4.5.

The next 4 bytes specify the size, in bytes, of the **HashBin** hash bin structure. This size is referred to as **HashBinSize** for this file format description. The structure varies in size because it includes **HashEntry** structures. For more information about the **HashBin** structure, see section [2.3.3.1.4.4](#Section_90abbd326f804bc894712c92f6cc0faf).

The next 4 bytes specify local entries or a local entry count, meaning the number of hash entries that are allowed per bin before an overflow occurs (section [2.3.3.1.4.6](#Section_807c46f84a5d42e6b3cb947cea327c3c)). If overflow hash entries (also called _collision entries_) exist, they are added sequentially to the end of the file.

The next 8 bytes specify the number of bins that are used in the hash. This number is referred to as **cBins** in this file format description. Depending on the data type, a minimum required value exists for the number of bins (also referred to as the minimum number of buckets for a hash). For more information about bin count minimums, see section [2.3.3.1.4.3](#Section_bcd24f7fc1c0427a9628c56af20062b8). The value of **cBins** either reflects the number of bins or is set to **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT** (section [2.3.3.1.4.1](#Section_30af58add5ec4897a973525b1eef3f43)).

If **cBins** is set to **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT**, that signals that the hash table was not created, so processing of the hash in the file is stopped at this point. Dictionary files (section 2.3.2.1) MUST set this value to **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT** to indicate that they do not include any hash table information beyond these required elements. For more information about **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT**, see section 2.3.3.1.4.1.

It is important to emphasize that even if **cBins** is set to stop any further hash table processing, the **HashBin** and **HashEntry** structures MUST be the correct, expected size for the current hash policy in place and the type of hash in use, the hash algorithm MUST be identified as expected by the system (section 2.3.3.1.4.2), and the local entries value MUST equal the **XM_HASH_ENTRY_COUNT_PER_BIN** calculated value (section 2.3.3.1.4.6), which depends on the hash policies that are in place and the type of hash.

If any of these values is incorrect, a file error will likely occur. For more information about all of these structures, see section [2.3.3.1.4](#Section_a155ecb71b484753b6b00c5ce867ed90). For a discussion about the effects of hash policies, see section 2.3.3.1.4.5.

The following diagram shows the common bytes that are required in any file containing hash information (that is, .hidx and .dictionary files). Note that string dictionaries comprise the only dictionary file type that can fully exclude any hash information, but there are ramifications to doing so (section [2.3.2.1.2.2](#Section_2bd1b39d0d654d3ab8f6a52aa7d1152a).) For more information about the actual structure of **HashBin** or **HashEntry**, section 2.3.3.1.4.4 or section 2.3.3.1.4.5, respectively.

| 0               | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| HashAlgorithm   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashEntrySize   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashBinSize     |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| LocalEntryCount |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| cBins           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**HashAlgorithm (4 bytes):** The hash algorithm specified.

**HashEntrySize (4 bytes):** The size of the **HashEntry** structure.

**HashBinSize (4 bytes):** The size of the **HashBin** structure.

**LocalEntryCount (4 bytes):** The number of hash entries that are allowed per bin before an overflow (collision) occurs.

**cBins (8 bytes):** Either the number of bins used in the hash or **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT**. The latter value is used by dictionaries.

##### Required Elements for Hash Index Files

The following subsections contain required information for hash index files (.hidx files). Note that an .hidx file also requires the elements discussed in section [2.3.3.1.1](#Section_9acdddc2f21c444393cee73879e9dc63).

###### Records and Hash Statistics

This section covers the number of records in the hash and any hash statistics that are included in the file. The next 8 bytes specify the number of records in the hash table. The next 8 bytes after that indicate the current mask to be used. This mask simply equals the number of bins minus one. The next byte contains a Boolean flag that indicates whether hash statistics were gathered and included in the file. If this value is **true**, hash statistics have been included in the file.

The hashing algorithm used to create the hash table is specified in section [2.3.3.1.3](#Section_8a8986c9f09942a6a6ed27dfb9a1bafa).

The rest of this section deals with the hash statistics. This data is present only if the flag that indicates the gathering of hash statistics is set to **true**. If the flag is set to **false**, the hash statistics data MUST NOT be included.

Because the hash statistics section is an optional section (indicated by the just-mentioned flag), some of the information in the section duplicates information that is found in previous elements. If hash statistics have been included, the next 8 bytes indicate the number of elements in the hash. The next 8 bytes following that indicate the number of bins available in the hash, and the following 8 bytes indicate the number of bins available that were actually used in the hash.

The next 8 bytes represent the number of elements that were available via fast access. An element is a fast access element if it is in the actual hash bin and therefore not an overflow (or collision) for that hash bin. An overflow element requires a longer access time.

The next 8 bytes contain the local entry size for each bin-in other words, the number of hash entries that can be contained in one bin before an overflow occurs. This size is the same as the local entry count mentioned in the five required elements (section [2.3.3.1.1](#Section_9acdddc2f21c444393cee73879e9dc63)). The next 8 bytes contain the maximum probes, or maximum chain count, for one bin. This value indicates the largest number of entries for one of the bins, over the range of all the bins. If this value is greater than the maximum number of hash entries that can be contained in a bin before an overflow occurs, at least one of the bins has had an overflow and thus has extra hash entries (also referred to as _collision entries_). These extra entries are added to the end of the file.

The next set of bytes represent a histogram. Of these bytes, the first 8 (**elementCount**) represent the number of elements in the histogram. The next 4 bytes (**elementSize**) represent the size, in bytes, of each element in the vector (or array). Therefore, the histogram itself is of variable size-specifically, **elementCount** multiplied by **elementSize**, in bytes. The histogram is a vector of elements of size **elementSize**. If the value of an element in the histogram vector is not zero, that value signifies the number of hash bins containing a certain number of entries in the bin-where the certain number is the array index number of that element. For example, if the histogram vector element at index 3 contains a value of 5, five hash bins each have three hash entries in their bin.

The histogram can contain empty array elements because it MUST include all the previous array elements up to the array elements that have nonzero values. The histogram can also include empty array elements following the last nonzero array element. If the number of entries signifies an overflow, the histogram will still show the total number of hash entries in a bin, including the overflow elements. Note that despite the fact that this value includes the total number of hash entries, a hash bin in reality can contain only the maximum number of elements already specified as the value of the **LocalEntryCount** field (section 2.3.3.1.1), and any overflow entries are chained internally and persisted to the file at the end of the file.

For example, if the histogram array element at index 3 contains a value of 9, three hash bins have nine entries each in their respective bins. If the maximum local entry count (or local entry size) for each bin is six, the implication is that each of those bins had an overflow and have three collision entries each (because nine minus six equals three) at the end of the file.

The following diagram shows the hash structure elements just discussed, beginning with the number of records and ending with the hash statistics histogram element.

| 0               | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8                          | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| --------------- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| NumberOfRecords |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| CurrentMask     |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashStats       |     |     |     |     |     |     |     | NumberOfElements           |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     | NumberOfBins               |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     | NumberOfUsedBins           |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     | FastAccessElements         |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     | LocalsSizePerBin           |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     | MaximumChain               |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     | elementCount               |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     | elementSize                |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     | HistogramVector (variable) |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...             |     |     |     |     |     |     |     |                            |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**NumberOfRecords (8 bytes):** The number of records in the hash table.

**CurrentMask (8 bytes):** The current mask to use.

**HashStats (1 byte):** A Boolean flag that specifies whether hash statistics have been included in the file. If the value is **true**, hash statistics have been included in the file. These hash statistics are the elements following this Boolean flag-from **NumberOfElements** through **HistogramVector**.

**NumberOfElements (8 bytes):** The number of elements in the hash.

**NumberOfBins (8 bytes):** The number of bins available in the hash.

**NumberOfUsedBins (8 bytes):** The number of bins that are actually used in the hash.

**FastAccessElements (8 bytes):** The number of elements with fast access.

**LocalsSizePerBin (8 bytes):** The number of hash entry structures that can be contained in one bin before an overflow occurs.

**MaximumChain (8 bytes):** The largest number of entries in a bin, over all the bins.

**elementCount (8 bytes):** The number of elements in the histogram vector.

**elementSize (4 bytes):** The size, in bytes, of each element in the histogram vector.

**HistogramVector (variable):** The vector of elements, each of which has the size that is specified by **elementSize**.

###### Hash Bin Entries

The next section of the hash includes the hash bins that are created and used during the hashing process. The number of entries, which appear in sequential bin order, is specified by **cBins**. Each entry is the size (**HashBinSize**) of the hash bin structure (**HashBin** structure). Each hash bin structure also contains an array of hash entries (**HashEntry** structures), up to the maximum number that is allowed per bin, so no overflow entries will exist within this structure. The sizes of the hash bin structure and the hash entry structure vary depending on several factors, including the operating system that is used and the current hash policies that are in place. For more information about the **HashBin** structure and the **HashEntry** structure, see section [2.3.3.1.4.4](#Section_90abbd326f804bc894712c92f6cc0faf) and section [2.3.3.1.4.5](#Section_db8c786ea4714458924d6807c8cf6a1d).

The following diagram shows a general view of the hash bin entries in a file. This particular example shows four **HashBin** entries that simply exist sequentially, one after another, in the file. The diagram does not show the details within each hash bin entry.

| 0                       | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| HashBinEntry (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                     |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashBinEntry (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                     |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashBinEntry (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                     |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| HashBinEntry (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                     |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**HashBinEntry (variable):** A **HashBin** structure.

**HashBinEntry (variable):** A **HashBin** structure.

**HashBinEntry (variable):** A **HashBin** structure.

**HashBinEntry (variable):** A **HashBin** structure.

###### Overflow Hash Entries

The final section of the file includes the collisions, if any, from any overflow in the hash bins. The next 8 bytes contain the total count of the collisions. This value includes the collisions for all the hash bins. This value is followed by the collision entries. Each collision entry is a **HashEntry** structure and, as such, is the size (**HashEntrySize**) of a hash entry. For more information about the **HashEntry** structure, see section [2.3.3.1.4.5](#Section_db8c786ea4714458924d6807c8cf6a1d).

Collisions are added sequentially to the end of file in the same order as their associated hash bins. Zero or more collisions might exist for a hash table. However, the 8 bytes that specify the count of collisions MUST be present, even if it contains a value of zero to indicate that no collisions exist.

The collision entries are the last elements in a hash index file (.hidx file). Padding with zeros might exist at the end of the file. If present, this padding is ignored and not read by the system.

The following diagram shows a general view of the collisions count and the collision hash entries in the file.

This particular example shows four collision **HashEntry** entries that simply exist sequentially, one after another, in the file. The details within the **HashEntry** structures are not shown.

Each of these collision entries corresponds to a hash bin that has one or more collisions. However, which collision entry corresponds to which hash bin cannot be gleaned from just the sequential collision entries here. The correspondence can, however, be inferred by looking at the **m_Count** member of each of the **HashBin** structures (section [2.3.3.1.4.4](#Section_90abbd326f804bc894712c92f6cc0faf)) to see whether the value of **m_Count** exceeds **XM_HASH_ENTRY_COUNT_PER_BIN** (section [2.3.3.1.4.6](#Section_807c46f84a5d42e6b3cb947cea327c3c)), which equals the value of the local entry count in the five required hash elements (section [2.3.3.1.1](#Section_9acdddc2f21c444393cee73879e9dc63)).

| 0                             | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| CollisionCount                |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| CollisionHashEntry (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| CollisionHashEntry (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| CollisionHashEntry (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| CollisionHashEntry (variable) |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                           |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**CollisionCount (8 bytes):** The total number of collisions over all the hash bins.

**CollisionHashEntry (variable):** The **HashEntry** structure for this collision entry.

**CollisionHashEntry (variable):** The **HashEntry** structure for this collision entry.

**CollisionHashEntry (variable):** The **HashEntry** structure for this collision entry.

**Collision HashEntry (variable):** The **HashEntry** structure for this collision entry.

##### Hashing Algorithms

The following hashing algorithm is used by hash index files (files with extension HIDX). This algorithm MUST be used to ensure proper hash table creation.

The hashing algorithm is shown in pseudocode.

- INPUT keyValue
- CREATE MagicConstant as an unsigned 32 bit integer
- CREATE cHashBitsUsed as 64 bit integer
- CREATE cBuckets as a double
- SET cBuckets to number of bins, also called buckets, to be used in hash
- SET MagicConstant to 0x12B9B6A5
- SET cHashBitsUsed to ( CEILING (LOG(cBuckets)/LOG(2.0)) )
- SET keyValue to (keyValue MultiplyBy MagicConstant)
- SET keyValue to (keyValue RIGHT_BITSHIFT by (32 - cHashBitsUsed))
- SET hashForKeyValue to keyValue
- OUTPUT hashForKeyValue

The hash and key value variable types can be determined by looking at the **HashEntry** structure (section [2.3.3.1.4.5](#Section_db8c786ea4714458924d6807c8cf6a1d)).

There is a minimum size for the number of bins used for proper hash table creation. The variable _cBuckets_ MUST use at least the minimum bin value. For the bin minimum values, please see section [2.3.3.1.4.3](#Section_bcd24f7fc1c0427a9628c56af20062b8).

##### Hash Structures, Enumerations and Constants

The following subsections contain information related to the data structures, enumerations, and other constants that are used by files that include hash information (that is, .hidx and .dictionary files).

###### XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT

The **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT** constant indicates that the bin count is invalid.

When the value of **cBins** (section [2.3.3.1.1](#Section_9acdddc2f21c444393cee73879e9dc63)) is set to this constant, it means that no further hash information is included in the file. This value is used by column data dictionary files (.dictionary files). For more information about dictionary files, see section [2.3.2](#Section_d6de072d52344099b090528322f829dc).

**XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT** is not used in hash index files (.hidx files) because by definition, these files are expected to have full hash information, with only the hash statistics being optional (section [2.3.3.1.2.1](#Section_0c41a99c646746c7b5fe0887090c4d55)).

The **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT** constant has a value of -1.

###### Hash Algorithm Enumeration and Constant

The **XMHashAlgorithm** enumeration indicates which **XM_TYPE_STRING** dictionary hash algorithm is in use. The **XM_INVALID** constant is used in all other cases.

In most hash algorithm scenarios, the hash algorithm value is set to **XM_INVALID**, which indicates that no hashing algorithm was specified in the persisted file. The algorithm is determined at run time based on the type of file and its data.

For hash index files (.hidx files) and column data dictionary files (.dictionary files) of type integer (**XM_TYPE_LONG**) or real (**XM_TYPE_REAL**), it is always the case that the hash algorithm value is set to **XM_INVALID**. For more information about the **XM_TYPE** enumeration, see section [2.3.2.1.3.1](#Section_619a632a09a54d8780faf5c0fc9c2ded).

| Name           | Value |
| -------------- | ----- |
| **XM_INVALID** | -1    |

However, for dictionaries of type **XM_TYPE_STRING**, the value is not **XM_INVALID** but MUST be one of values in the **XMHashAlgorithm** enumeration.

- enum XMHashAlgorithm
- {
- XM_HASH_ALGORITHM_SQL = 0,
- XM_HASH_ALGORITHM_FAST_CI = 1,
- XM_HASH_ALGORITHM_FAST_CS = 2
- };

The following table describes the enumeration values in **XMHashAlgorithm**.

| Enumeration value             | Meaning                                                                                                                                                                                                                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XM_HASH_ALGORITHM_SQL**     | The hash algorithm is the default algorithm. It will work for all string situations but SHOULD NOT be chosen if one of the other two values in **XMHashAlgorithm** can be used.                                                                             |
| **XM_HASH_ALGORITHM_FAST_CI** | This algorithm can be used if the locale identifier is 1033 and it is acceptable to ignore the case of the characters in the strings (that is, if the strings are case insensitive).                                                                        |
| **XM_HASH_ALGORITHM_FAST_CS** | This algorithm can be used if either the locale identifier is 1033 and the characters are case sensitive or the strings are [**BLOBs**](#gt_ad861812-8cb0-497a-80bb-13c95aa4e425) that use [**base64 encoding**](#gt_179b9392-9019-45a3-880b-26f6890522b7). |

###### Hash Bin Bucket Size Minimums

A minimum number of bins (or buckets) is required for hashes that are used in .hidx files.

In general, for all data other than string data, the minimum bin count is 16. For string data, there MUST be a minimum of 256 bins. Note that .hidx files contain integer data, not string data, as indicated by the **m_Key** and **m_Value** members in the **HashEntry** structure (section [2.3.3.1.4.5](#Section_db8c786ea4714458924d6807c8cf6a1d)).

| Name                                 | Value |
| ------------------------------------ | ----- |
| **XM_HASH_MINIMUM_BIN_COUNT**        | 16    |
| **XM_STRING_HASH_MINIMUM_BIN_COUNT** | 256   |

###### HashBin Structure

The **HashBin** structure contains information about the hash bins used.

The **HashBin** structure is system cache aligned and therefore varies in size according to the operating system and alignment requirements for that operating system. For alignment reasons, the chain pointer (the **m_rgChain** member) MUST be the first element in the structure. For 32-bit systems, padding is also added to the structure to ensure that the count-of-entries element is properly aligned.

The hash bin contains one or more hash entries. However, because of alignment issues and the variable size of the **HashEntry** structure (section [2.3.3.1.4.5](#Section_db8c786ea4714458924d6807c8cf6a1d)), it is possible for the local hash entry array (the **m_rgLocalEntries** member) to contain no hash entries, where **XM_HASH_ENTRY_COUNT_PER_BIN** evaluates to zero. In such a case, all the hash entries are referenced through the chain pointer, **m_rgChain**. (The chain pointer is an array of **HashEntry** structures.)

- DECLSPEC_ALIGN(SYSTEM_CACHE_ALIGNMENT_SIZE) struct HashBin
- {
- HashEntry\* m_rgChain;
- #ifndef \_WIN64
- unsigned \_\_int32 m_Padding;
- #endif
- unsigned \_\_int32 m_Count;
- HashEntry m_rgLocalEntries\[XM_HASH_ENTRY_COUNT_PER_BIN\];
- };

**m_rgChain:** The pointer for the chain of collisions, which is a chain of **HashEntry** structures that represent the overflow (collision) entries. The value is NULL when persisted to disk, and the collisions are added to the end of the file.

**m_Padding:** Padding for alignment purposes. This padding is included for 32-bit systems (the compiler constant **\_WIN64** is not defined) and excluded for 64-bit systems (**\_WIN64** is defined).

**m_Count:** The total number of **HashEntry** entries in the bin.

**m_rgLocalEntries:** An array of size **XM_HASH_ENTRY_COUNT_PER_BIN** that contains the locally stored **HashEntry** entries (not the overflow collision entries).

The **DECLSPEC_ALIGN** macro is defined as follows:

- #if (\_MSC_VER >= 1300) && !defined(MIDL_PASS)
- #define DECLSPEC_ALIGN(x) \_\_declspec(align(x))
- #else
- #define DECLSPEC_ALIGN(x)
- #endif

The **SYSTEM_CACHE_ALIGNMENT_SIZE** constant is defined as follows:

- #if defined(\_AMD64*) || defined(\_X86*)
- #define SYSTEM_CACHE_ALIGNMENT_SIZE 64
- #else
- #define SYSTEM_CACHE_ALIGNMENT_SIZE 128
- #endif

For more information about the **HashEntry** structure, see section 2.3.3.1.4.5. For more information about **XM_HASH_ENTRY_COUNT_PER_BIN**, see section [2.3.3.1.4.6](#Section_807c46f84a5d42e6b3cb947cea327c3c).

###### HashEntry Structure

The **HashEntry** structure contains information about the hash entries used.

In most cases, a hash entry structure contains a key/hash pair for the hash table. However, depending on the hash policies in use, the hash entry structure information can vary, including either more or less information. The hash key MUST be included. Other elements vary.

A hash policy defines which elements are required in the **HashEntry** structure. The hash policies vary according to internally defined variables that seek to balance load factors, storage issues, and processing speeds.

The hashes for **XM_TYPE_LONG**, **XM_TYPE_REAL**, and **XM_TYPE_STRING** hash data dictionaries are recalculated at run time, so only the basic, required elements for the hash are required in the file format (section [2.3.3.1.1](#Section_9acdddc2f21c444393cee73879e9dc63)), with **cBins** set to **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT** (section [2.3.3.1.4.1](#Section_30af58add5ec4897a973525b1eef3f43)). Even so, hash policies play a role in determining the expected size of the **HashBin** (section [2.3.3.1.4.4](#Section_90abbd326f804bc894712c92f6cc0faf)) and **HashEntry** structures and the value of the local entry count (section [2.3.3.1.4.6](#Section_807c46f84a5d42e6b3cb947cea327c3c)) because they all use the **HashEntry** structure.

However, for files with the .hidx file name extension, where full hash information is required, all the hashing information is included and MUST be accurate. For hash index files (.hidx files), the hash value (**m_Hash**) is included in **HashEntry**, along with the required element, the key (**m_Key**). The hashing algorithm used is also specified and MUST be used to generate the hash information (section [2.3.3.1.3](#Section_8a8986c9f09942a6a6ed27dfb9a1bafa)).

The following code shows the full **HashEntry** structure, which is defined by using the **DECLSPEC_ALIGN(X)** macro (section 2.3.3.1.4.4), where **X** = 1. The code includes comments that contain pseudocode to indicate which structure members will be included in the structure for various policy settings. Only **m_Key** is guaranteed to be in any **HashEntry** structure for any policy.

- DECLSPEC_ALIGN(1) struct HashEntry
- {
- // IF this policy is true (HASHPOLICY_INCLUDEHASH) THEN
- // include member m_Hash
- unsigned \_\_int32 m_Hash;
- // END IF
- // IF this policy is true (HASHPOLICY_INCLUDELENGTH) THEN
- // include member m_Len
- unsigned \_\_int32 m_Len;
- // END IF
- TKey m_Key; // Required member in all cases
- // IF this policy is true (HASHPOLICY_INCLUDEVALUE) THEN
- // include member m_Value
- TValue m_Value;
- // END IF
- };

**m_Hash:** The hashing value that is paired with the key value, **m_Key**. Including and using the hash instead of the value makes sense for simple types, where comparing the hashes has the same cost as comparing the values. It does not make sense for complex types or character data (strings).

**m_Len:** The length field. The meaning varies, depending on usage. For example, for strings, the length means the length of the string. Using this member increases the size of the structure and might result in more overflows (collisions).

**m_Key:** The key value that is associated with the hashing value, **m_Hash**. This member MUST be present in all cases. The data type for this value varies, depending on the type of the hash table being used, as shown in the following table.

| **File type**                        | **Data type for m_key (TKey resolution)** |
| ------------------------------------ | ----------------------------------------- |
| .hidx file                           | **Int32**                                 |
| **XM_TYPE_LONG** dictionary (32-bit) | **Int32**                                 |
| **XM_TYPE_LONG** dictionary (64-bit) | **Int64**                                 |
| **XM_TYPE_REAL** dictionary          | **DOUBLE**                                |
| **XM_TYPE_STRING** dictionary        | **Int32**                                 |

**m_Value:** The actual value that is associated with the key, **m_Key**. The data type for this value varies depending on the type of hash table that is being used, as shown in the following table.

| **File type**                        | **Data type for m_Value (TValue resolution)** |
| ------------------------------------ | --------------------------------------------- |
| .hidx file                           | **Int32**                                     |
| **XM_TYPE_LONG** dictionary (32-bit) | **Int32**                                     |
| **XM_TYPE_LONG** dictionary (64-bit) | **Int32**                                     |
| **XM_TYPE_REAL** dictionary          | **Int32**                                     |
| **XM_TYPE_STRING** dictionary        | **Int32**                                     |

The following table summarizes the relationship between a hash policy setting and the files that are affected by that setting. Note that the constant string hash policy is only for **XM_TYPE_STRING** dictionaries. This policy can be used only when each string mapped via the hash is guaranteed to be a unique string. **XM_TYPE_STRING** dictionaries can use this hash policy when the strings per page are guaranteed to be unique strings, with no duplicates on that page (section [2.3.2.1.2.2](#Section_2bd1b39d0d654d3ab8f6a52aa7d1152a)).

| Hash policy setting      | Affected files                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------ | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| HASHPOLICY_INCLUDEHASH   | Both .hidx and .dictionary files                         | This value (true) is the default for all hash policies.<br><br>Note that for XM_TYPE_STRING dictionaries, the data identifier is the key, but the length of the string is not stored separately from the hash value. Instead, the high-order word of the string hash and the low-order word of the string's length are combined into the stored hash value. This applies to both Huffman compressed strings and strings that are not compressed.<br><br>However, this does not apply if the constant string hash policy is being used, instead. In that case, the length is included separately. |
| HASHPOLICY_INCLUDELENGTH | XM_TYPE_STRING dictionaries (when full hash is included) | This value is **true** if the constant string hash policy is being used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| HASHPOLICY_INCLUDEVALUE  | XM_TYPE_STRING dictionaries (when full hash is included) | This value is **true** if the constant string hash policy is being used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

###### XM_HASH_ENTRY_COUNT_PER_BIN

The **XM_HASH_ENTRY_COUNT_PER_BIN** value dictates how many **HashEntry** structures (section [2.3.3.1.4.5](#Section_db8c786ea4714458924d6807c8cf6a1d)) can be contained in a **HashBin** structure (section [2.3.3.1.4.4](#Section_90abbd326f804bc894712c92f6cc0faf)) before an overflow occurs.

The **XM_HASH_ENTRY_COUNT_PER_BIN** value depends on the target architecture's cache line size as well as the **HashEntry** structure (section 2.3.3.1.4.5) being used, which varies in form and size depending on which hash policies are in effect.

For 32-bit and 64-bit applications, how to calculate the **XM_HASH_ENTRY_COUNT_PER_BIN** value is shown in the following pseudocode:

- IF application is 32 bit OR 64 bit THEN
- SET XM_HASH_ENTRY_COUNT_PER_BIN to ( (CacheLineSize MultiplyBy SYSTEM_CACHE_ALIGNMENT_SIZE - (8 + (Size-Of (unsigned 32 bit integer))) / (Size-Of (HashEntry structure) )
- END IF

For the definition of **SYSTEM_CACHE_ALIGNMENT_SIZE**, see section 2.3.3.1.4.4.

**CacheLineSize** is dependent on the hash policies that are in place (see section 2.3.3.1.4.5). However, in all cases in this document, **CacheLineSize** is equal to 1.

The hash entry structure (**HashEntry**) is variable and its size depends on the hash policies that are in place. For more information, see section 2.3.3.1.4.5.

### RowNumber Column

Every table MUST have a RowNumber file generated for the table. An example of a generated file name for a RowNumber file for a table that has the identifier "Table1" is 4.Table1.RowNumber.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2](#Section_f629ebb97cf2410fb56b2edce58dbcc9).

The RowNumber file is used to tell the system how many rows are contained in each data segment of the column data. This information is always encoded by using XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt; compression (section [2.7.3.16](#Section_1cf84136dae246ee99de91fb24fbffc4)).

It is necessary to reference the XML metadata file to understand and decode the contents of the RowNumber file. The metadata file for the RowNumber file is contained in the same file as the metadata for the column data (section [2.3.1](#Section_4d3887f864c84dbd9a02e4e95e64bfed)). The **Column** item in the **Column** collection for which the value of the **name** attribute is "RowNumber" contains the metadata for this file. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

#### File Layout for the RowNumber Column

The **RowNumber** column is a special case for column data storage files. In addition to generating a column data storage file (.idf file) for every column in a source data table, an additional .idf file is generated to represent a column of row numbers. This **RowNumber** column is an internally generated column, but as a result, does have its own column data storage file (.idf file). The purpose of a RowNumber file is to associate a row number index with each row of each segment, per segment, for the entire span of the column. As such, a **RowNumber** column provides a row number index that can be used to select a particular row or set of rows across columns. However, because the system generates these files and knows their function, it does not mean that each actual row number is encoded in the .idf file. In actuality, a more compact way is used.

In fact, although **RowNumber** columns do use XMHybridRLE compression, they use only XM123CompressionInfo subsegment compression. This hybrid combination is unlike the typical XMHybridRLE and XMRENoSplit case. The .idf file format layout is the same, but the subsegment is just a placeholder, and the RLE segment for each segment is encoded in a special way that details the row number information, which the system already knows how to interpret. For a detailed discussion of the compression used for the **RowNumber** column and how to interpret the information correctly, see section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b) and section [2.7.3.16](#Section_1cf84136dae246ee99de91fb24fbffc4).

## System-Generated Data Files

The system generates not only the files that represent the data but additional files, depending on the data. These additional files are described in this section.

### Column Data Position-to-Identifier Mapping

Column data can have a position-to-identifier mapping file. An example of a position-to-identifier mapping file name for a table that has the identifier "Table1" and a column that has the identifier "Label" is 1.H\$Table1\$Label.POS_TO_ID.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2.3.7.2.3](#Section_bf9e88f156ba497bbc038cd97901d0d6).

The position-to-identifier mapping file contains an array of data identifier values. The order of the array is by the sorted order of the underlying values that the data identifiers represent. The first value in the array corresponds to the data identifier for which the underlying value that the data identifier represents is first in sorted order. For example, if the values in the column are sorted, and the first value after sorting has a data identifier of 5, the first value in the array is 5. The second array value corresponds to the data identifier of the second entry when the column values are sorted, and so on.

The position-to-identifier mapping file is compressed by one of several methods, although it is always compressed by using an XMRENoSplit compression method and does not use XMHybridRLE compression. For a discussion of the types of compression available that are to be used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to understand and decode the contents of the column position-to-identifier mapping file. An example of a file name for the file that contains the metadata for the position-to-identifier mapping file for a column that has the identifier "net" in a table that has the identifier "Table1" is H\$Table1\$net.0.tbl.xml. The metadata for the position-to-identifier mapping column is found in the **Columns** collection of the **XMSimpleTable** object in the file. In the **Columns** collection, the **Column** item that has the name "POS_TO_ID" contains the metadata for this file. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

#### File Layout for Column Data Position-to-Identifier Mapping File

The column data position-to-identifier mapping file uses the same .idf file layout as the column data storage .idf file, including the use of segments and segment layout (section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e).) However, differences exist.

The position-to-identifier mapping file is a system-generated file and never uses XMHybridRLE compression but only XMRENoSplit compression. This fact also means that, at a minimum, a position-to-identifier mapping file always has one segment and is never associated with a subsegment. The reason is that sub segments are associated only with XMHybridRLE compression, which in turn is used only by column data storage .idf files and the special case of the **RowNumber** column data .idf file.

### Column Data Identifier-to-Position Mapping

Column data can have an identifier-to-position mapping file. A data identifier-to-position mapping file is generated only in the case where a value hash table has been generated. An identifier-to-position mapping file is not generated for a dictionary file. An example of a generated identifier-to-position mapping file name for a table that has the identifier "Table1" and a column that has the identifier "net" is 1.H\$Table1\$net.ID_TO_POS.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2.3.7.2.4](#Section_07ce9d6cbfc240ce851b305643b68ec5).

The identifier-to-position mapping file contains an array of position values that are zero-based numbers. These position values represent the positions within the sorted values of the underlying source data values that are represented by the data identifiers. The order of the array is by data identifier value, from lowest to highest. The first array value is the position within the set of source data values of the lowest-numbered data identifier, the second value is the position of the second-lowest data identifier value, and so on. For example, if the lowest-valued data identifier is sorted to the fifth position in the array of the source data values that are underling the data identifiers, the first value in this array will be 4 (because the array is zero-based). The second array item contains the position within the array of sorted source data values that is assigned to the second-lowest data identifier value, and so on.

The identifier-to-position mapping file is compressed by one of several methods, although it is always compressed by using an XMRENoSplit compression method and does not use XMHybridRLE compression. For a discussion of the types of compression that are available to be used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to understand and decode the contents of the column identifier-to-position mapping file. An example of a file name for the file that contains the metadata for the data identifier-to-position mapping file for a column that has the identifier "net" in a table that has the identifier "Table1" is H\$Table1\$net.0.tbl.xml. The metadata for the data identifier-to-position mapping column is found in the **Columns** collection of the **XMSimpleTable** object in the file. In the **Columns** collection, the **Column** item that has the name "ID_TO_POS" contains the metadata for this file. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

#### File Layout for Column Data Identifier-to-Position Mapping File

The column data identifier-to-position mapping file uses the same .idf file layout as the column data storage .idf file, including the use of segments and segment layout (section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e).) However, differences exist.

The identifier-to-position mapping file is a system-generated file and never uses XMHybridRLE compression but only XMRENoSplit compression. This fact also means that, at a minimum, an identifier-to-position mapping file always has one segment and is never associated with a subsegment. The reason is that sub segments are associated only with XMHybridRLE compression, which in turn is used only by column data storage .idf files and the special case of the **RowNumber** column data .idf file.

### Relationship Index

If a relationship between two tables in a [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) is defined, a relationship index is generated. Tabular data models require that the key column in one of the tables be unique (many-to-many relationships are not allowed). The relationship index file is generated for the table that is on the "many" side of the relationship. An example of a generated relationship index file name for the "many" table in the relationship is 73.R\$Table1\$c4047114-e5d3-4730-ab46-478baf7ae64f.INDEX.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2.3.7.2.2](#Section_bc201ebc070a427b91e76ef053a6c96d).

The relationship index file contains an array of integers. One integer exists in this file for each unique value in the join column of the table on the "many" side of the relationship. The first integer that is present in the file corresponds to the first unique value that is encountered, starting with the first row, in the join column of the "many" table. The second integer corresponds to the second unique value that is encountered in the join column, and so on. The integer value is the row number in the other table of the relationship (the "one" table) to which the row is joined. Row numbering is zero-based. If a row cannot be joined because no value match exists, the value -1 will appear in the relationship index file.

The relationship index file is compressed by one of several methods, although it is always compressed by using an XMRENoSplit compression method and does not XMHybridRLE compression. For a discussion of the types of compression that are available to be used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to understand and decode the contents of the relationship index file. An example of a file name for the file that contains the metadata for the relationship index file is R\$Table1\$c4047114-e5d3-4730-ab46-478baf7ae64f.73.tbl.xml. The metadata for the relationship index column is found in the **Columns** collection of the **XMSimpleTable** object in the file. In the **Columns** collection, the **Column** item that has the name "INDEX" contains the metadata for this file. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

#### File Layout for Relationship Index File

A relationship index file can have one of two file format forms: that of either an .idf file or an .hidx file. The relationship index file typically uses the same .idf file layout as the column data storage .idf file, including the use of segments and segment layout (section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e)). However, when the relationship index file uses the .idf file format layout, differences from a column data storage .idf file exist.

The relationship index .idf file is a system-generated file and never uses XMHybridRLE compression but only XMRENoSplit compression. This fact also means that a relationship index file always has one segment at a minimum and is never associated with a subsegment. The reason is that sub segments are associated only with XMHybridRLE compression. which in turn is used only by column data storage .idf files and the special case of the **RowNumber** column data .idf file.

Most of the time, the relationship index file uses the .idf file format. However, in some situations when sparse relationship information exists (which means that very large gaps exist between the column values with relationships), the relationship index file takes the form of an .hidx file (hash index file).

For example, if only two values exist for the column, one with a value of 2 and the other with a value of 5 billion, using an .idf file will generate rows for all the unused values between 2 and 5 billion. A hash table simply encodes the two key-value pairs of interest. The hash table encodes a key-value pair with the column value (the data identifier) as the hash key, and the row number as the hash value. For more information about the hash index file format file layout, see section [2.3.3](#Section_582bda42d62f4ce0998551fb88fe68ee).

### User Hierarchy System-Generated Files

A [**tabular data model**](#gt_459cc665-f840-4a96-a255-c558ae6fa07f) allows users to define hierarchies. A [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) is defined by its levels, where one column in the source data contains the value for a particular level. For example, a common hierarchy for geography has "Country/Region" at the top level, "State" at the next level down, and "City" at the level below "State". In this case, a column in the source data table exists that contains the value for each of the levels.

For each defined user hierarchy, the system generates four data files. These files consist of the child count file (section [2.4.4.1](#Section_f7775057e7564d06a45b1c1ff3422dfc)), the first child position file (section [2.4.4.2](#Section_1d0483a24ddd43dc8316c9527a8ca346)), the multilevel identifier file (section [2.4.4.3](#Section_2fc33dd59a1a49779bdc9fcb57f14ed8)), and the parent position file (section [2.4.4.4](#Section_a2ec84d242f84a5393ca61b2be23b603)). The integer values that appear in these files require understanding an in-memory data structure that is formed by the system. Note that this data structure is never materialized or seen by users.

A data structure is formed in which each combination of distinct values that actually exists at all of the levels is represented by rows in a table. The table starts at the highest level and descends through the levels. All row numbering that refers to the table is zero-based-that is, the first row is row 0.

The first _N_ rows in the table, which are numbered from 0 through (_N_ - 1), consist of all the distinct values at the highest level in the user hierarchy. The values are sorted by the collation for that column. For example, if the highest level in the user hierarchy is "Country/Region", and the countries that are present in the data are "United States" and "Canada", then row 0 in the table is for "Canada" (the first item in sort order), and row 1 in the table is for "United States".

The next _N_ rows in the table represent all the valid combinations of values that exist at the highest level and at the next-highest level in the user hierarchy. For example, if the next-highest level is "Area"; the United States has areas named "Northwest", "Northeast", "Southwest", and "Southeast"; and Canada has areas named "East" and "West"; six rows in the table will exist to represent the second level, and they are rows 2 through 7. Within each level, the values appear in sorted order under their common parent level, and the parent levels remain in the originally sorted order.

Therefore, for the first two levels in the example table, the rows of the in-memory table will be as shown in the following table.

| Row | Value                     |
| --- | ------------------------- |
| 0   | "Canada"                  |
| 1   | "United States"           |
| 2   | "Canada-East"             |
| 3   | "Canada-West"             |
| 4   | "United States-Northeast" |
| 5   | "United States-Northwest" |
| 6   | "United States-Southeast" |
| 7   | "United States-Southwest" |

The process just described is repeated recursively until valid combinations of items that exist at each level of the user hierarchy are represented in the table.

#### User Hierarchy Child Count

Every user hierarchy has a child count file. An example of a generated user hierarchy child count file name for a table that has the identifier "Table1" and a [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) that has the identifier "Geography" is 8.U\$Table1\$Geography.CHILD_COUNT.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2.3.7.2.7.1](#Section_58d1ed5253a043dca82d7354711a295c).

The user hierarchy child count file contains an array of integers. One integer exists in this file for each row in the in-memory tabular structure (section [2.4.4](#Section_7b84720fcf8e499088672200b6d7d1a6)) for the user hierarchy. The first integer that is present in the file corresponds to row 0 of the table, the second integer corresponds to row 1, and so on. The integer value represents the number of child items at the next level for the item in the table row. For example, the item "Canada", row 0, has 2 child items, and the item "United States", row 1, has 4 child items. So the first value in this example file is 2 (the number of child items of the item "Canada"), and the second value is 4 (the number of child items of the item "United States").

The user hierarchy child count file is compressed by one of several methods, although it is always compressed by using an XMRENoSplit compression method and does not XMHybridRLE compression. For a discussion of the types of compression that are available to be used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to understand and decode the contents of the user hierarchy child count file. An example of a file name for the file that contains the metadata for the user hierarchy child count file is U\$Table1\$Geography.0.tbl.xml. The metadata for the child count column is found in the **Columns** collection of the **XMSimpleTable** object in the file. In the **Columns** collection, the **Column** item that has the name "CHILD_COUNT" contains the metadata for this file. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

##### File Layout for User Hierarchy Child Count

The user hierarchy child count file uses the same .idf file layout as the column data storage .idf file, including the use of segments and segment layout (section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e).) However, differences exist.

The user hierarchy child count file is a system-generated file that never uses XMHybridRLE compression but only XMRENoSplit compression. This fact also means that a user hierarchy child count file always has one segment at a minimum and is never associated with a subsegment, because sub segments are associated only with XMHybridRLE compression, which in turn is used only by column data storage .idf files and the special case of the **RowNumber** column data .idf file.

#### User Hierarchy First Child Position

Every user hierarchy has a first child position file. An example of a generated user hierarchy first child position file name for a table that has the identifier "Table1" and a [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) that has the identifier "Geography" is 8.U\$Table1\$Geography.FIRST_CHILD_POS.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2.3.7.2.7.2](#Section_546c393714a34feab357cd5bf10c8b12).

The user hierarchy first child position file contains an array of integers. One integer exists in this file for each row in the in-memory tabular structure (section [2.4.4](#Section_7b84720fcf8e499088672200b6d7d1a6)) for the user hierarchy. The first integer that is present in the file corresponds to row 0 of the table, the second integer corresponds to row 1, and so on. The integer value is the row number of the row in the in-memory tabular structure that contains the first child of the item on this row. In the example, the first row, row 0, "Canada", has its first child at row 2, "Canada-East", so the first value in the file is 2. The second row of the table, row 1, "United States", has its first child in row 4, "United States-Northeast", so the second value in the file in this example is 4.

The user hierarchy first child position file is compressed by one of several methods, although it is always compressed by using an XMRENoSplit compression method and does not use XMHybridRLE compression. For a discussion of the types of compression that are available to be used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to understand and decode the contents of the user hierarchy first child position file. An example of a file name for the file that contains the metadata for the user hierarchy first child position file is U\$Table1\$Geography.0.tbl.xml. The metadata for the first child position column is found in the **Columns** collection of the **XMSimpleTable** object in the file. In the **Columns** collection, the **Column** item that has the name "FIRST_CHILD_POS" contains the metadata for this file. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

##### File Layout for User Hierarchy First Child Position

The user hierarchy first child position file uses the same .idf file layout as the column data storage .idf file, including the use of segments and segment layout (section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e).) However, differences exist.

The user hierarchy first child position file is a system-generated file and never uses XMHybridRLE compression but only XMRENoSplit compression. This fact also means that a user hierarchy first child position file always has one segment at a minimum and is never associated with a subsegment, because sub segments are associated only with XMHybridRLE compression, which in turn is used only by column data storage .idf files and the special case of the **RowNumber** column data .idf file.

#### User Hierarchy Multilevel Identifier

Every user hierarchy has a multilevel identifier file. An example of a generated user hierarchy multilevel identifier file name for a table that has the identifier "Table1" and a [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) that has the identifier "Geography" is 8.U\$Table1\$Geography.MULTI_LEVEL_ID.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2.3.7.2.7.4](#Section_03eb56f614904980b1c6331e2091f672).

The user hierarchy multilevel identifier file contains an array of integers. One integer exists in this file for each row in the in-memory tabular structure, which is described in section [2.4.4](#Section_7b84720fcf8e499088672200b6d7d1a6), for the user hierarchy. The first integer that is present in the file corresponds to Row 0 of the table, the second integer corresponds to Row 1, and so on.

The integer value in the file is the data identifier value that represents the data value at the lowest level represented on the table row. In the example, Row 0 is "Canada" so the integer value is the data identifier for "Canada" in the "Country/Region" column. Row 1 is "United States" so the next integer value in this file is the data identifier for "United States" in the "Country/Region" column. Row 2 is for "Canada-East" so the item at the lowest level represented in that table row is "East", and the third integer is the data identifier value for the item "East" in the "Area" column.

The user hierarchy multilevel identifier file is compressed by one of several methods, although it is always compressed by using an XMRENoSplit compression method and does not use XMHybridRLE compression. For a discussion of the types of compression that are available to be used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to understand and decode the contents of the user hierarchy multilevel identifier file. An example of a file name for the file that contains the metadata for the user hierarchy multilevel identifier file is U\$Table1\$Geography.0.tbl.xml. The metadata for the multilevel identifier column is found in the **Columns** collection of the **XMSimpleTable** object in the file. In the **Columns** collection, the **Column** item that has the name "MULTI_LEVEL_ID" contains the metadata for this file. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

##### File Layout for User Hierarchy Multilevel Identifier

The user hierarchy multilevel identifier file uses the same .idf file layout as the column data storage .idf file, including the use of segments and segment layout (see section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e).) However, differences exist.

The user hierarchy multilevel identifier file is a system-generated file that never uses XMHybridRLE compression but only XMRENoSplit compression. This fact also means that a user hierarchy multilevel identifier file always has one segment at a minimum and is never associated with a subsegment, because sub segments are associated only with XMHybridRLE compression, which in turn is used only by column data storage .idf files and the special case of the **RowNumber** column data .idf file.

#### User Hierarchy Parent Position

Every user hierarchy has a parent position file. An example of a generated user hierarchy parent position file name for a table that has the identifier "Table1" and a [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) that has the identifier "Geography" is 8.U\$Table1\$Geography.PARENT_POS.0.idf. For an explanation of the interpretation of the substrings within the file name, see section [2.2.3.7.2.7.3](#Section_9b4e1ae634914e2885e0a2063ed46b31).

The user hierarchy parent position file contains an array of integers. One integer exists in this file for each row in the in-memory tabular structure, which is described in section [2.4.4](#Section_7b84720fcf8e499088672200b6d7d1a6), for the user hierarchy. The first integer that is present in the file corresponds to Row 0 of the table, the second integer corresponds to Row 1, and so on.

The integer value in the file is the row number in the table that contains the parent item of the item in the table row. In the example, the first two rows are items at the highest level of the user hierarchy. Therefore, neither has a parent item and this fact is represented by the value -1. So the first two values in the file in this example are each -1. The next row in the table has the item "Canada-East". The parent item of "Canada-East" is "Canada". "Canada" is at Row 0 in the table, so in this example, the third value in the file is zero.

The user hierarchy parent position file is compressed by one of several methods, although it is always compressed by using an XMRENoSplit compression method and does not use XMHybridRLE compression. For a discussion of the types of compression available to be used, see section [2.7](#Section_d9db04571298486c9e7696366b838714).

It is necessary to reference the XML metadata file to understand and decode the contents of the user hierarchy parent position file. An example of a file name for the file that contains the metadata for the user hierarchy parent position file is U\$Table1\$Geography.0.tbl.xml. The metadata for the parent position column is found in the **Columns** collection of the **XMSimpleTable** object in the file. In the **Columns** collection, the **Column** item that has the name "PARENT_POS" contains the metadata for this file. For an explanation of how to interpret the metadata file, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246).

##### File Layout for User Hierarchy Parent Position

The user hierarchy parent position file uses the same .idf file layout as the column data storage .idf file, including the use of segments and segment layout (see section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e).) However, differences exist.

The user hierarchy parent position file is a system-generated file that never uses XMHybridRLE compression but only XMRENoSplit compression. This fact also means that a user hierarchy parent position file always has one segment at a minimum and is never associated with a subsegment, because sub segments are associated only with XMHybridRLE compression, which in turn is used only by column data storage .idf files and the special case of the **RowNumber** column data .idf file.

## Metadata Files

The system stores metadata in XML files. The following sections describe the XML files by using [**XML schema definition (XSD)**](#gt_c7e91c99-e45a-44c2-a08a-c34f137a2cae) fragments. For the general XSD fragment for any **XMObject** element, see section [2.5.1](#Section_23dde626b187405590e15a2333f11c5f). For the XSD fragment for each **XMObject** element based on its specific **class** attribute value, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd). All the types that are referenced in the text in the metadata sections use XML Schema types, as specified in [\[XMLSCHEMA1\]](https://go.microsoft.com/fwlink/?LinkId=90608) and [\[XMLSCHEMA2\]](https://go.microsoft.com/fwlink/?LinkId=90610).

### XMObject Document Node Element

The table metadata file, the table relationship metadata file, and the column data metadata files all have an **XMObject** element as the document root node. The **XMObject** element is a general element that contains an object that is used to represent objects of many different classes in the XML metadata files.

The general XSD fragment for the **XMObject** element is defined in this section. Because the **XMObject** element is used to represent many different types of objects, its XSD fragment contains a reference to xs:any and is therefore very general. Additional sections are provided that provide a more-specific complex type definition for the **XMObject** element when its **class** attribute contains a known value. For the XSD fragment for each **XMObject** element when the class is known, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd).

- &lt;xs:element name="XMObject" type="XMObjectType"/&gt;
- &lt;xs:complexType name="XMObjectType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Properties" type="XMObjectPropertiesType" minOccurs="0"/&gt;
- &lt;xs:element name="Members" type="XMObjectMembersType" minOccurs="0"/&gt;
- &lt;xs:element name="Collections" type="XMObjectCollectionsType" minOccurs="0"/&gt;
- &lt;xs:element name="DataObjects" type="XMObjectDataObjectsType" minOccurs="0"/&gt;
- &lt;/xs:all&gt;
- &lt;xs:attribute name="class" type="XMObjectClassNameEnum"/&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;/xs:complexType&gt;

**Properties:** An element that contains content described as xs:any. Depending on the class of the **XMObject** element, the actual content allowed is constrained, as specified in section 2.5.2.

**Members:** A collection of **Member** items of type **XMObjectMemberType** for the **XMObject** element. The **Member** items allowed for a specific **XMObject** element are constrained, as specified in section 2.5.2, depending on the value of the **class** attribute.

**Collections:** A collection of **Collection** items of type **XMObjectCollectionType** for the **XMObject** element. The **Collection** items allowed for a specific **XMObject** element are constrained, as specified in section 2.5.2, depending on the value of the **class** attribute.

**DataObjects:** A collection of **DataObject** items of type **XMObjectDataObjectType** for the **XMObject** element. The **DataObject** items allowed in the collection for a particular **XMObject** element are constrained, as specified in section 2.5.2, depending on the value of the **class** attribute.

**class:** An enumeration value that specifies the class of the **XMObject** element.

**name:** A string that specifies the object name.

**ProviderVersion:** An integer that specifies the version of the provider that wrote the object.

#### XMObjectPropertiesType

The **XMObjectPropertiesType** complex type holds the properties for an instance of an **XMObject** object.

The XSD fragment presented in this section is general and covers the definition of all element instances of type **XMObjectPropertiesType**. However, when the **class** attribute value of the containing **XMObject** element is known, the content of an element of type **XMObjectPropertiesType** is more constrained than indicated by the definition contained in this section. For the constrained definitions, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd).

- &lt;xs:complexType name="XMObjectPropertiesType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:any minOccurs="0" maxOccurs="unbounded"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**xs:any:** Any element as content.

#### XMObjectMembersType

The **XMObjectMembersType** complex type holds a collection of **Member** items for an instance of an **XMObject** object. Each **Member** item represents a property of the **XMObject** instance, but a **Member** item can contain complex content, whereas **XMObjectPropertiesType** (section [2.5.1.1](#Section_12498d44e67a4faa9dbcc8aa7be95b65)) holds elements of a simple type.

The XSD fragment presented in this section is general and covers the definition of all element instances of type **XMObjectMembersType**. However, when the **class** attribute value of the containing **XMObject** element is known, the content of an element of type **XMObjectMembersType** is more constrained than indicated by the definition contained in this section. For the constrained definitions, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd).

- &lt;xs:complexType name="XMObjectMembersType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Member" type="XMObjectMemberType" maxOccurs="unbounded"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Member:** A property of the **XMObject** instance that can contain complex content. In the general case, any **Member** can be contained in the collection of **Member** objects. However, the content of specific instances of the **XMObjectMembersType** type is constrained depending on the value of the **class** attribute of the containing **XMObject** element.

#### XMObjectCollectionsType

The **XMObjectCollectionsType** complex type holds collections of complex properties that pertain to the parent **XMObject** instance. Each **Collection** item represents a property of the **XMObject** instance. The collection can contain multiple instances of the same **Collection** item, and each instance can contain complex content. An example is a table, which can contain multiple column items in a collection.

The XSD fragment presented in this section is general and covers the definition of all element instances of type **XMObjectCollectionsType**. However, when the **class** attribute value of the containing **XMObject** element is known, the content of an element of type **XMObjectCollectionsType** is more constrained than indicated by the definition contained in this section. For the constrained definitions, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd).

- &lt;xs:complexType name="XMObjectCollectionsType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Collection" type="XMObjectCollectionType"
- maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Collection:** A property of the **XMObject** instance, which can contain multiple instances of the same property, and in which each instance can contain complex content. In the general case, any **Collection** can be contained in the collection of **Collection** objects. However, the content of specific instances of the **XMObjectCollectionsType** type is constrained depending on the value of the **class** attribute of the containing **XMObject** element.

#### XMObjectDataObjectsType

The **XMObjectDataObjectsType** complex type holds data objects for the parent **XMObject** instance. Each **DataObject** object in the collection represents a data object of the parent **XMObject** instance.

The XSD fragment presented in this section is general and covers the definition of all element instances of type **XMObjectDataObjectsType**. However, when the **class** attribute value of the containing **XMObject** element is known, the content of an element of type **XMObjectDataObjectsType** is more constrained than indicated by the definition contained in this section. For the constrained definitions, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd).

- &lt;xs:complexType name="XMObjectDataObjectsType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="DataObject" type="XMObjectDataObjectType"
- maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**DataObject:** A data object that is related to the **XMObject** instance. In the general case, any **DataObject** can be contained in the collection of **DataObjects**. However, the content of specific instances of the **XMObjectDataObjectsType** type are constrained depending on the value of the **class** attribute of the containing **XMObject** element.

#### XMObjectMemberType

The **XMObjectMemberType** complex type holds properties for one **Member** item of a parent **XMObject** instance. The properties for the member are held within another instance of an **XMObject** element that is nested within the **Member** element.

The XSD fragment presented in this section is general and covers the definition of all element instances of type **XMObjectMemberType**. However, when the **class** attribute value of the containing **XMObject** element is known, the content of an element of type **XMObjectMemberType** is more constrained than indicated by the definition contained in this section. For the constrained definitions, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd).

- &lt;xs:complexType name="XMObjectMemberType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Name" type="XMObjectMemberNameEnum" /&gt;
- &lt;xs:element name="XMObject" type="XMObjectType" minOccurs="0"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Name:** An enumeration value that specifies the name of the **Member** item.

**XMObject:** A nested instance of an **XMObject** element. The **XMObject** element contains the properties, members, collections, and data objects for the **Member** instance that has the name specified by the **Name** element.

#### XMObjectCollectionType

The **XMObjectCollectionType** complex type holds the data for one collection item of a parent **XMObject** instance. The properties for each item in the collection are held within another instance of an **XMObject** element that is nested within the **Collections** element.

The XSD fragment presented in this section is general and covers the definition of all element instances of type **XMObjectCollectionType**. However, when the **class** attribute value of the containing **XMObject** element is known, the content of an element of type **XMObjectCollectionType** is more constrained than indicated by the definition contained in this section. For the constrained definitions, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd).

- &lt;xs:complexType name="XMObjectCollectionType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Name" type="XMObjectCollectionNameEnum" /&gt;
- <xs:element name="XMObject" type="XMObjectType"
- minOccurs="0" maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Name:** An enumeration value that specifies the name of the **Collection** item.

**XMObject:** A nested instance of an **XMObject** element. The **XMObject** element contains the properties, members, collections, and data objects for the **Collection** object that has the name specified by the **Name** element.

#### XMObjectDataObjectType

The **XMObjectDataObjectType** complex type holds the data for one data object item in the collection of data objects for the parent **XMObject** instance. The properties for each item in the collection are held within another instance of an **XMObject** element that is nested within the **DataObject** element.

The XSD fragment presented in this section is general and covers the definition of all element instances of type **XMObjectDataObjectType**. However, when the **class** attribute value of the containing **XMObject** element is known, the content of an element of type **XMObjectDataObjectType** is more constrained than indicated by the definition contained in this section. For the constrained definitions, see section [2.5.2](#Section_99defc8e38d0430fad7471be19741abd).

- &lt;xs:complexType name="XMObjectDataObjectType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="XMObject" type="XMObjectType"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**XMObject:** A nested instance of an **XMObject** element, which contains the properties, members, collections, and data objects for a data object item in the collection of data objects.

#### XMObjectMemberNameEnum

The **XMObjectMemberNameEnum** simple type enumerates the allowed values for the name of a **Member** item in the **Members** collection of an **XMObject** object.

- &lt;xs:simpleType name="XMObjectMemberNameEnum"&gt;
- &lt;xs:restriction base="xs:string"&gt;
- &lt;xs:enumeration value="SegmentMap"/&gt;
- &lt;xs:enumeration value="TableStats"/&gt;
- &lt;xs:enumeration value="ColumnStats"/&gt;
- &lt;xs:enumeration value="SubSegment"/&gt;
- &lt;xs:enumeration value="CompressionInfo"/&gt;
- &lt;xs:enumeration value="ColumnSegmentStats"/&gt;
- &lt;xs:enumeration value="IntrinsicHierarchy"/&gt;
- &lt;xs:enumeration value="SubCompression"/&gt;
- &lt;xs:enumeration value="RLECompression"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMObjectMemberNameEnum** type.

| Enumeration value    | Description                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------- |
| "SegmentMap"         | The member contains a [**segment map**](#gt_52e360e3-0541-451e-93fb-f5ee8cc32cd2).                            |
| "TableStats"         | The member contains table statistics.                                                                         |
| "ColumnStats"        | The member contains column statistics.                                                                        |
| "SubSegment"         | The member contains information for a subsegment.                                                             |
| "CompressionInfo"    | The member contains information about compression.                                                            |
| "ColumnSegmentStats" | The member contains column segment statistics.                                                                |
| "IntrinsicHierarchy" | The member contains information about an [**intrinsic hierarchy**](#gt_03b4105f-6f7b-4ea5-8b95-d2e6ecbc6ee0). |
| "SubCompression"     | The member contains information about subcompression.                                                         |
| "RLECompression"     | The member contains information about RLE compression.                                                        |

#### XMObjectCollectionNameEnum

The **XMObjectCollectionNameEnum** simple type enumerates the allowed values for the name of a **Collection** item in the **Collections** collection of an **XMObject** object.

- &lt;xs:simpleType name="XMObjectCollectionNameEnum"&gt;
- &lt;xs:restriction base="xs:string"&gt;
- &lt;xs:enumeration value="Columns"/&gt;
- &lt;xs:enumeration value="Segments"/&gt;
- &lt;xs:enumeration value="Partitions"/&gt;
- &lt;xs:enumeration value="Relationships"/&gt;
- &lt;xs:enumeration value="UserHierarchies"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMObjectCollectionNameEnum** type.

| Enumeration value | Description                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Columns"         | The **Collection** item contains a collection of **Column** items. Each **Column** item represents a column in the source data table.                      |
| "Segments"        | The **Collection** item contains a collection of **Segment** items. Each **Segment** item represents a segment of the rows of a column in the source data. |
| "Partitions"      | The **Collection** item contains a collection of **Partition** items. Only one partition is supported.                                                     |
| "Relationships"   | The **Collection** item contains a collection of **Relationship** items. Each **Relationship** item describes a join relationship.                         |
| "UserHierarchies" | The **Collection** item contains a collection of user-defined hierarchies. Each **UserHierarchy** item describes a user-defined hierarchy.                 |

#### XMObjectClassNameEnum

The **XMObjectClassNameEnum** simple type enumerates the allowed values for the **class** attribute of an **XMObject** element. The content allowed in an instance of an **XMObject** element depends on the value of this attribute.

- &lt;xs:simpleType name="XMObjectClassNameEnum"&gt;
- &lt;xs:restriction base="xs:string"&gt;
- &lt;xs:enumeration value="XMSimpleTable"/&gt;
- &lt;xs:enumeration value="XMRawColumn"/&gt;
- &lt;xs:enumeration value="XMRelationship"/&gt;
- &lt;xs:enumeration value="XMRelationshipIndexSparseDIDs"/&gt;
- &lt;xs:enumeration value="XMRelationshipIndexDenseDIDs"/&gt;
- &lt;xs:enumeration value="XMHierarchy"/&gt;
- &lt;xs:enumeration value="XMUserHierarchy"/&gt;
- &lt;xs:enumeration value="XMHierarchyDataID2PositionHashIndex"/&gt;
- &lt;xs:enumeration value="XMColumnSegment"/&gt;
- &lt;xs:enumeration value="XMPartition"/&gt;
- &lt;xs:enumeration value="XMMultiPartSegmentMap"/&gt;
- &lt;xs:enumeration value="XMSegment1Map"/&gt;
- <xs:enumeration value=
- "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"/>
- <xs:enumeration value=
- "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;"/>
- &lt;xs:enumeration value="XMTableStats"/&gt;
- &lt;xs:enumeration value="XMColumnSegmentStats"/&gt;
- &lt;xs:enumeration value="XMColumnStats"/&gt;
- &lt;xs:enumeration value="XMValueDataDictionary<XM_Long&gt;"/>
- &lt;xs:enumeration value="XMValueDataDictionary<XM_Real&gt;"/>
- &lt;xs:enumeration value="XMHashDataDictionary<XM_Real&gt;"/>
- &lt;xs:enumeration value="XMHashDataDictionary<XM_Long&gt;"/>
- &lt;xs:enumeration value="XMHashDataDictionary<XM_String&gt;"/>
- &lt;xs:enumeration value="XMHashDataDictionary<XMVariantPtr&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<1&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<2&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<3&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<4&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<5&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<6&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<7&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<8&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<9&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<10&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<12&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<16&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<21&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<32&gt;"/>
- &lt;xs:enumeration value="XM123CompressionInfo"/&gt;
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>"
- />
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMREGeneralCompressionInfo&gt;"/>
- &lt;xs:enumeration value="XMRawColumnPartitionDataObject"/&gt;
- &lt;xs:enumeration value="XMRLECompressionInfo"/&gt;
- &lt;xs:enumeration value="XMRLEGeneralCompressionInfo"/&gt;
- &lt;xs:enumeration value="XMColumnSegmentDataObject"/&gt;
- &lt;xs:enumeration value="XMRelationshipIndex123DIDs"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMObjectClassNameEnum** type.

| Enumeration value                                                        | Description                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "XMSimpleTable"                                                          | The object specifies the metadata for a table.                                                                                                                                                                                                       |
| "XMRawColumn"                                                            | The object specifies the metadata for a column.                                                                                                                                                                                                      |
| "XMRelationship"                                                         | The object specifies the metadata for a relationship between two tables.                                                                                                                                                                             |
| "XMRelationshipIndexSparseDIDs"                                          | The object specifies the metadata for a relationship index in which the data identifiers are sparse.                                                                                                                                                 |
| "XMRelationshipDenseDIDs"                                                | The object specifies the metadata for a relationship in which the data identifiers are dense.                                                                                                                                                        |
| "XMHierarchy"                                                            | The object specifies the metadata for a [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682).                                                                                                                                                   |
| "XMUserHierarchy"                                                        | The object specifies the metadata for a user hierarchy.                                                                                                                                                                                              |
| "XMHierarchyDataID2PositionHashIndex"                                    | The object specifies the metadata for a hash index of data identifier-to-position mapping.                                                                                                                                                           |
| "XMColumnSegment"                                                        | The object specifies the metadata for a column segment.                                                                                                                                                                                              |
| "XMPartition"                                                            | The object specifies the metadata for a partition.                                                                                                                                                                                                   |
| "XMultiPartSegmentMap"                                                   | The object specifies the metadata for a [**segment map**](#gt_52e360e3-0541-451e-93fb-f5ee8cc32cd2) associated with partitions.                                                                                                                      |
| "XMSegment1Map"                                                          | The object specifies the metadata for a segment map for a column with a single segment.                                                                                                                                                              |
| "XMSegmentEqualMapEx<XMSegmentEqualMap_FastInstantiation"                | The object specifies the metadata for a segment map of equally sized segments (except that the size of the last segment can differ from that of the others). Note that fast instantiation is for predetermined segment sizes.                        |
| "XMSegmentEqualMapEx<XMSegmentEqualMap_ComplexInstantiation"             | The object specifies the metadata for a segment map of equally sized segments (except that the size of the last segment can differ from that of the others). Note that complex instantiation occurs when the segment size is determined at run time. |
| "XMTableStats"                                                           | The object specifies the metadata for table statistics.                                                                                                                                                                                              |
| "XMColumnStats"                                                          | The object specifies the metadata for column statistics.                                                                                                                                                                                             |
| "XMColumnSegmentStats"                                                   | The object specifies the metadata for column segment statistics.                                                                                                                                                                                     |
| "XMValueDataDictionary&lt;XM_Long&gt;"                                   | The object specifies the metadata for a value dictionary for values of type **long**.                                                                                                                                                                |
| "XMValueDataDictionary&lt;XM_Real&gt;"                                   | The object specifies the metadata for a value dictionary for values of type **real**.                                                                                                                                                                |
| "XMHashDataDictionary&lt;XM_Real&gt;"                                    | The object specifies the metadata for a hash dictionary for values of type **real**.                                                                                                                                                                 |
| "XMHashDataDictionary&lt;XM_Long&gt;"                                    | The object specifies the metadata for a hash dictionary for values of type **long**.                                                                                                                                                                 |
| "XMHashDataDictionary&lt;XM_String&gt;"                                  | The object specifies the metadata for a hash dictionary for values of type **string**.                                                                                                                                                               |
| "XMRENoSplitCompressionInfo&lt;1&gt;"                                    | The object specifies the metadata for NoSplit compression of 1 bit in length.                                                                                                                                                                        |
| "XMRENoSplitCompressionInfo&lt;2&gt;"                                    | The object specifies the metadata for NoSplit compression of 2 bits in length.                                                                                                                                                                       |
| "XMRENoSplitCompressionInfo&lt;3&gt;"                                    | The object specifies the metadata for NoSplit compression of 3 bits in length.                                                                                                                                                                       |
| "XMRENoSplitCompressionInfo&lt;4&gt;"                                    | The object specifies the metadata for NoSplit compression of 4 bits in length.                                                                                                                                                                       |
| "XMRENoSplitCompressionInfo&lt;5&gt;"                                    | The object specifies the metadata for NoSplit compression of 5 bits in length.                                                                                                                                                                       |
| "XMRENoSplitCompressionInfo&lt;6&gt;"                                    | The object specifies the metadata for NoSplit compression of 6 bits in length.                                                                                                                                                                       |
| "XMRENoSplitCompressionInfo&lt;7&gt;"                                    | The object specifies the metadata for NoSplit compression of 7 bits in length.                                                                                                                                                                       |
| "XMRENoSplitCompressionInfo&lt;8&gt;"                                    | The object specifies the metadata for NoSplit compression of 8 bits in length.                                                                                                                                                                       |
| "XMRENoSplitCompressionInfo&lt;9&gt;"                                    | The object specifies the metadata for NoSplit compression of 9 bits in length.                                                                                                                                                                       |
| "XMRENoSplitCompressionInfo&lt;10&gt;"                                   | The object specifies the metadata for NoSplit compression of 10 bits in length.                                                                                                                                                                      |
| "XMRENoSplitCompressionInfo&lt;12&gt;"                                   | The object specifies the metadata for NoSplit compression of 12 bits in length.                                                                                                                                                                      |
| "XMRENoSplitCompressionInfo&lt;16&gt;"                                   | The object specifies the metadata for NoSplit compression of 16 bits in length.                                                                                                                                                                      |
| "XMRENoSplitCompressionInfo&lt;21&gt;"                                   | The object specifies the metadata for NoSplit compression of 21 bits in length.                                                                                                                                                                      |
| "XMRENoSplitCompressionInfo&lt;32&gt;"                                   | The object specifies the metadata for NoSplit compression of 32 bits in length.                                                                                                                                                                      |
| "XM123CompressionInfo"                                                   | The object specifies the metadata for 123 compression.                                                                                                                                                                                               |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 1 bit in length.                                                                                                                                                                 |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 2 bits in length.                                                                                                                                                                |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 3 bits in length.                                                                                                                                                                |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 4 bits in length.                                                                                                                                                                |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 5 bits in length.                                                                                                                                                                |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 6 bits in length.                                                                                                                                                                |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 7 bits in length.                                                                                                                                                                |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 8 bits in length.                                                                                                                                                                |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>"  | The object specifies the metadata for hybrid NoSplit compression of 9 bits in length.                                                                                                                                                                |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>" | The object specifies the metadata for hybrid NoSplit compression of 10 bits in length.                                                                                                                                                               |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>" | The object specifies the metadata for hybrid NoSplit compression of 12 bits in length.                                                                                                                                                               |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>" | The object specifies the metadata for hybrid NoSplit compression of 16 bits in length.                                                                                                                                                               |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>" | The object specifies the metadata for hybrid NoSplit compression of 21 bits in length.                                                                                                                                                               |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>" | The object specifies the metadata for hybrid NoSplit compression of 32 bits in length.                                                                                                                                                               |
| "XMHybridRLECompressionInfo&lt;class XMRE123CompressionInfo&gt;"         | The object specifies the metadata for hybrid 123 compression.                                                                                                                                                                                        |
| "XMHybridRLECompressionInfo&lt;class XMREGeneralCompressionInfo&gt;"     | The object specifies the metadata for hybrid General compression.                                                                                                                                                                                    |
| "XMRawColumnPartitionDataObject"                                         | The object specifies the metadata for a partition.                                                                                                                                                                                                   |
| "XMRLECompressionInfo"                                                   | The object specifies the metadata for RLE compression.                                                                                                                                                                                               |
| "XMColumnSegmentDataObject"                                              | The object specifies the metadata for a data object for a column segment.                                                                                                                                                                            |
| "XMRLEGeneralCompressionInfo"                                            | The object specifies the metadata for general RLE compression.                                                                                                                                                                                       |

### XMObject Definitions by class Attribute

The general definition of the **XMObject** element is specified in section [2.5.1](#Section_23dde626b187405590e15a2333f11c5f). This section contains more-specific definitions for the content of an **XMObject** element, according to each available value of the **class** attribute on the **XMObject** element.

#### XMObject class="XMSimpleTable"

When the **class** attribute value for the **XMObject** element is "XMSimpleTable", the **XMObject** element contains the metadata for a table object, and the type of the **XMObject** element is **XMSimpleTableXMObjectType**.

- &lt;xs:complexType name="XMSimpleTableXMObjectType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Properties" type="XMSimpleTablePropertiesType"/&gt;
- &lt;xs:element name="Members" type="XMSimpleTableMembersType"/&gt;
- &lt;xs:element name="Collections" type="XMSimpleTableCollectionsType"/&gt;
- &lt;/xs:all&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMSimpleTable">
- &lt;/xs:attribute&gt;
- &lt;/xs:complexType&gt;

**Properties:** The property values for the **XMSimpleTable** object.

**Members:** A collection of **Member** complex type items, each of which contains a complex property for the **XMSimpleTable** object.

**Collections:** A collection of **Collection** complex type items, each of which contains a complex property for the **XMSimpleTable** object. The **Collection** complex property can be repeated multiple times.

**name:** The name of the **XMSimpleTable** object instance.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMSimpleTablePropertiesType

The **XMSimpleTablePropertiesType** complex type holds the specific properties that are allowed when the **XMObject** element is of class "XMSimpleTable".

- &lt;xs:complexType name="XMSimpleTablePropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Version" type="xs:int"/&gt;
- &lt;xs:element name="Settings"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="4367"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="RIViolationCount" type="xs:long"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Version:** The internal version number for this data. This version number is not required to match the version numbers of other objects within the same table or column.

**Settings:** A mask that describes settings for the table. The bits that are listed in the following table can be set.

| Bit    | Meaning                                                                               |
| ------ | ------------------------------------------------------------------------------------- |
| 0x1    | The table contains normal data.                                                       |
| 0x2    | The table contains an index.                                                          |
| 0x3    | The table has temporary content.                                                      |
| 0x4    | The table has an [**intrinsic hierarchy**](#gt_03b4105f-6f7b-4ea5-8b95-d2e6ecbc6ee0). |
| 0x5    | The table has a user hierarchy.                                                       |
| 0x100  | The table has been processed.                                                         |
| 0x1000 | The table uses an automatic NULL for an unknown member.                               |

**RIViolationCount:** The number of relational integrity violations in the **XMSimpleTable** object.

##### XMSimpleTableMembersType

The **XMSimpleTableMembersType** complex type holds a collection of **Member** items, each of which contains a property for the parent **XMSimpleTable** object.

- &lt;xs:complexType name="XMSimpleTableMembersType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Member" type="XMSimpleTableMemberType"
- minOccurs="2" maxOccurs="2"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Member:** A complex type element that contains a property for the parent **XMObject** element of class "XMSimpleTable". The value of the **Name** element for the two instances of this element in the **Members** collection MUST have one instance of each enumeration value from the **XMSimpleTableMemberNameEnum** type (section [2.5.2.1.2.2](#Section_771f0ee1b26a4e88ad4dbf2e4b072f44)).

###### XMSimpleTableMemberType

The **XMSimpleTableMemberType** complex type holds a **Member** item, which contains a property of the parent **XMSimpleTable** object.

- &lt;xs:complexType name="XMSimpleTableMemberType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Name" type="XMSimpleTableMemberNameEnum"
- minOccurs="0"/>
- &lt;xs:element name="XMObject"&gt;
- &lt;xs:complexType&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="XMObjectTypeBase"&gt;
- <xs:attribute name="class"
- type="XMSimpleTableXMObjectMemberClassNameEnum"/>
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Name:** The name of the **Member** object.

**XMObject:** A complex type that contains a nested instance of an **XMObject** element. The type of the element is an extension of **XMObjectTypeBase**. However, the actual content allowed in an instance is constrained and depends on the value of the **class** attribute of the **XMObject** element. The content of the **XMObject** element MUST follow the constraints depending on its **class** attribute value.

**class:** An enumeration value that specifies the class name of this **XMObject** element instance. When the **Name** element of the **Member** item has a particular value, the **XMObject** element of the **Member** item MUST have a specific value for the **class** attribute. The following table lists the constraints between the values of **Name** and **class**.

<div class="joplin-table-wrapper"><table><thead><tr><th><p>Value of Name element</p></th><th><p>Required value of class attribute</p></th></tr></thead><tbody><tr><td><p>"SegmentMap"</p></td><td><p>One of the following:</p><ul><li>"XMMultiPartSegmentMap"</li><li>"XMSegment1Map"</li><li>"XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;"</li></ul></td></tr><tr><td><p>"TableStats"</p></td><td><p>"XMTableStats"</p></td></tr></tbody></table></div>

###### XMSimpleTableMemberNameEnum

The **XMSimpleTableMemberNameEnum** simple type enumerates the allowed values for the name of a **Member** item in the **Members** collection of an **XMSimpleTable** object.

- &lt;xs:simpleType name="XMSimpleTableMemberNameEnum"&gt;
- &lt;xs:restriction base="XMObjectMemberNameEnum"&gt;
- &lt;xs:enumeration value="SegmentMap"/&gt;
- &lt;xs:enumeration value="TableStats"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMSimpleTableMemberNameEnum** type.

| Enumeration value | Description                                                                           |
| ----------------- | ------------------------------------------------------------------------------------- |
| "SegmentMap"      | The **Member** item is a [**segment map**](#gt_52e360e3-0541-451e-93fb-f5ee8cc32cd2). |
| "TableStats"      | The **Member** item contains table statistics.                                        |

###### XMSimpleTableXMObjectMemberClassNameEnum

The **XMSimpleTableXMObjectMemberClassNameEnum** simple type enumerates the allowed values for the class name of the **XMObject** element that is contained in a **Member** item in the **Members** collection of an **XMSimpleTable** object.

- &lt;xs:simpleType name="XMSimpleTableXMObjectMemberClassNameEnum"&gt;
- &lt;xs:restriction base="XMObjectClassNameEnum"&gt;
- &lt;xs:enumeration value="XMMultiPartSegmentMap"/&gt;
- &lt;xs:enumeration value="XMSegment1Map"/&gt;
- <xs:enumeration value=
- "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;"/>
- <xs:enumeration value=
- "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"/>
- &lt;xs:enumeration value="XMTableStats"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMSimpleTableXMObjectMemberClassNameEnum** type.

| Enumeration value                                                   | Description                                                                                                                                                     |
| ------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "XMMultiPartSegmentMap"                                             | The object contains a multipart [**segment map**](#gt_52e360e3-0541-451e-93fb-f5ee8cc32cd2), which is a segment map that is built on top of other segment maps. |
| "XMSegment1Map"                                                     | The object contains a segment map for a column that has just one segment.                                                                                       |
| "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;" | The object contains a segment map for equally sized segments. Complex instantiation occurs when the actual segment size is determined at run time.              |
| "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"    | The object contains a segment map for equally sized segments. Fast instantiation occurs when the actual segment size is determined at creation time.            |
| "XMTableStats"                                                      | The object contains table statistics.                                                                                                                           |

##### XMSimpleTableCollectionsType

The **XMSimpleTableCollectionsType** complex type holds a collection of **Collection** items, each of which contains a property for the parent **XMSimpleTable** object. **Collection** items can be repeated multiple times within the collection.

- &lt;xs:complexType name="XMSimpleTableCollectionsType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Collection" type="XMSimpleTableCollectionType"
- minOccurs="4" maxOccurs="4"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Collection:** A complex type element that contains a **Collection** item, which contains a property for the parent **XMObject** element of class **XMSimpleTable**. **Collection** items can be repeated within the collection.

The value of the **Name** element for the four instances of this element in the **Collections** collection MUST have one instance of each enumeration value from the **XMSimpleTableCollectionNameEnum** type (section [2.5.2.1.3.2](#Section_3d68ad992b8449f8a5d4827c2b24dc2b)).

###### XMSimpleTableCollectionType

The **XMSimpleTableCollectionType** complex type holds a **Collection** item, which contains a property of the parent **XMSimpleTable** object.

- &lt;xs:complexType name="XMSimpleTableCollectionType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Name" type="XMSimpleTableCollectionNameEnum"/&gt;
- &lt;xs:element name="XMObject" minOccurs="0" maxOccurs="unbounded"&gt;
- &lt;xs:complexType&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="XMObjectTypeBase"&gt;
- <xs:attribute name="class"
- type="XMSimpleTableXMObjectCollectionClassNameEnum"/>
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Name:** The name of the **Collection** object.

**XMObject:** A complex type that contains a nested instance of an **XMObject** element. The type of the element is an extension of **XMObjectTypeBase**. However, the actual content that is allowed depends on the value of the **class** attribute of the **XMObject** element instance.

The following attributes are added by extension for the **XMObject** element.

**class:** An enumeration value that specifies the class name of this **XMObject** element. When the **Name** element of the **Collection** item has a particular value, the **XMObject** element of the **Collection** item MUST have a specific value for the **class** attribute. The following table lists the constraints between the values of **Name** and **class**.

| Value of Name element | Required value of class attribute |
| --------------------- | --------------------------------- |
| "Partitions"          | "XMPartition"                     |
| "Columns"             | "XMRawColumn"                     |
| "Relationships"       | "XMRelationship"                  |
| "UserHierarchies"     | "XMUserHierarchy"                 |

**name:** The name of the **Collection** item.

###### XMSimpleTableCollectionNameEnum

The **XMSimpleTableCollectionNameEnum** simple type enumerates the allowed values for the name of a **Member** item in the **Collections** collection of an **XMSimpleTable** object.

- &lt;xs:simpleType name="XMSimpleTableCollectionNameEnum"&gt;
- &lt;xs:restriction base="XMObjectCollectionNameEnum"&gt;
- &lt;xs:enumeration value="Partitions"/&gt;
- &lt;xs:enumeration value="Columns"/&gt;
- &lt;xs:enumeration value="Relationships"/&gt;
- &lt;xs:enumeration value="UserHierarchies"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMSimpleTableCollectionNameEnum** type.

| Enumeration value | Description                                                                          |
| ----------------- | ------------------------------------------------------------------------------------ |
| "Partitions"      | **Collection** is a collection of items that pertain to each partition.              |
| "Columns"         | **Collection** is a collection of items that pertain to each column.                 |
| "Relationships"   | **Collection** is a collection of items that pertain to relationships for the table. |
| "UserHierarchies" | **Collection** is a collection of items that pertain to user-defined hierarchies.    |

###### XMSimpleTableXMObjectCollectionClassNameEnum

The **XMSimpleTableXMObjectCollectionClassNameEnum** simple type enumerates the allowed values for the class name of the **XMObject** element that is contained in a **Collection** item in the **Collections** collection of an **XMSimpleTable** object.

- &lt;xs:simpleType name="XMSimpleTableXMObjectCollectionClassNameEnum"&gt;
- &lt;xs:restriction base="XMObjectClassNameEnum"&gt;
- &lt;xs:enumeration value="XMPartition"/&gt;
- &lt;xs:enumeration value="XMRawColumn"/&gt;
- &lt;xs:enumeration value="XMRelationship"/&gt;
- &lt;xs:enumeration value="XMUserHierarchy"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMSimpleTableXMObjectCollectionClassNameEnum** type.

| Enumeration value | Description                                                                   |
| ----------------- | ----------------------------------------------------------------------------- |
| "XMPartition"     | The **XMObject** element contains a partition.                                |
| "XMRawColumn"     | The **XMObject** element contains information about a column.                 |
| "XMRelationship"  | The **XMObject** element contains information about a table relationship.     |
| "XMUserHierarchy" | The **XMObject** element contains information about user-defined hierarchies. |

#### XMObject class="XMTableStats"

When the **class** attribute value for the **XMObject** element is "XMTableStats", the **XMObject** element contains statistical information about the table, and the type of the **XMObject** element is **XMTableStatsXMObjectType**.

- &lt;xs:complexType name="XMTableStatsXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMTableStatsPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMTableStats"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMTableStatsPropertiesType

The **XMTableStatsPropertiesType** simple type contains the specific properties that are allowed when the **XMObject** element is of class "XMTableStats".

- &lt;xs:complexType name="XMTableStatsPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="SegmentSize" type="xs:long"/&gt;
- &lt;xs:element name="Usage"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="2"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**SegmentSize:** The number of rows in the segment.

**Usage:** An enumeration value for the usage of the table. One of the values in the following table can be set.

| Value | Meaning                         |
| ----- | ------------------------------- |
| 0     | The table usage is unknown.     |
| 1     | The table is a dimension table. |
| 2     | The table is a fact table.      |

#### XMObject class="XMRawColumn"

When the **class** attribute value for the **XMObject** element is "XMRawColumn", the **XMObject** element contains the metadata for a raw data column, and the type of the **XMObject** element is **XMRawColumnXMObjectType**.

- &lt;xs:complexType name="XMRawColumnXMObjectType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Properties" type="XMRawColumnPropertiesType"/&gt;
- &lt;xs:element name="Members" type="XMRawColumnMembersType"/&gt;
- &lt;xs:element name="Collections" type="XMRawColumnCollectionsType"/&gt;
- &lt;xs:element name="DataObjects" type="XMRawColumnDataObjectsType"/&gt;
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMRawColumn"/>
- &lt;/xs:complexType&gt;

**Properties:** A complex type that specifies the property values for the **XMRawColumn** object.

**Members:** A collection of **Member** complex type items, each of which contains a complex property for the **XMRawColumn** object.

**Collections:** A collection of **Collection** complex type items, each of which contains a complex property for the **XMRawColumn** object. The **Collection** complex property can be repeated multiple times.

**DataObjects:** A collection of **DataObject** complex type items, each of which contains an object with information about the column's data.

**name:** The name of the **XMRawColumn** object instance.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

**ProviderVersion:** The provider version.

##### XMRawColumnPropertiesType

The **XMRawColumnPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMRawColumn".

- &lt;xs:complexType name="XMRawColumnPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Settings"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="7994"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="ColumnFlags"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="63"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="Collation" type="xs:string"/&gt;
- &lt;xs:element name="OrderByColumn" type="xs:string"/&gt;
- &lt;xs:element name="Locale" type="xs:long"/&gt;
- &lt;xs:element name="BinaryCharacters" type="xs:unsignedInt"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Settings:** The settings for the column. The low order 5 bits (values 0x0 through 0x11) contain the column type. The remainder of the values can be combined with the column type.

The following table describes the values for the column type.

| Value | Meaning                                         |
| ----- | ----------------------------------------------- |
| 0     | The column has no settings.                     |
| 0x1   | The column contains basic data.                 |
| 0x2   | The column contains calculated data.            |
| 0x3   | The column contains a relationship line number. |

The following table describes the remainder of the values.

| Value  | Meaning                                                                                                                  |
| ------ | ------------------------------------------------------------------------------------------------------------------------ |
| 0x5    | The column contains data identifier-to-position mapping for a [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682). |
| 0x7    | The column contains position-to-data identifier mapping for a hierarchy.                                                 |
| 0x8    | The column contains the position of the parent item within the parent item's own level in a hierarchy.                   |
| 0x9    | The column contains the position of the child item within the child item's own level in a hierarchy.                     |
| 0x10   | The column contains a data identifier within a merged multilevel user hierarchy.                                         |
| 0x11   | The column contains a count of the child items within a merged multilevel hierarchy.                                     |
| 0x100  | NULLs are converted to zeros or spaces.                                                                                  |
| 0x200  | The column is trimmed on the left.                                                                                       |
| 0x400  | The column is trimmed on the right.                                                                                      |
| 0x800  | The column is a calculated column.                                                                                       |
| 0x1000 | The column needs defragmentation.                                                                                        |

**ColumnFlags:** The flags for the properties of the column. One or more of the values in the following table can be set. The value 0x8 MUST be set.

| Value | Meaning                                                                                |
| ----- | -------------------------------------------------------------------------------------- |
| 0     | No flags are set.                                                                      |
| 0x1   | The column cannot be NULL.                                                             |
| 0x2   | A constraint exists specifying that all the values in the column MUST be unique.       |
| 0x4   | The column is the primary key for the table.                                           |
| 0x8   | The column has an [**intrinsic hierarchy**](#gt_03b4105f-6f7b-4ea5-8b95-d2e6ecbc6ee0). |
| 0x10  | The column contains row numbers.                                                       |
| 0x20  | The column has an unsorted hierarchy.                                                  |

**Collation:** The name of the collation. The value MAY[&lt;11&gt;](#Appendix_A_11) be restricted to a string that is recognized as valid by the system.

**OrderByColumn:** The column by which to order the hierarchy.

**Locale:** An [**LCID**](#gt_c7f99c66-592f-4053-b62a-878c189653b6) that specifies the locale.

**BinaryCharacters:** The maximum number of characters in a string that uses base64 encoding and that represents a [**BLOB**](#gt_ad861812-8cb0-497a-80bb-13c95aa4e425).

##### XMRawColumnMembersType

The **XMRawColumnMembersType** complex type holds a collection of **Member** items, each of which contains a property for the parent **XMSimpleTable** object.

- &lt;xs:complexType name="XMRawColumnMembersType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Member" type="XMRawColumnMemberType"
- minOccurs="2" maxOccurs="2"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Member:** A property for the parent **XMObject** element of class **XMRawColumn**. The value of the **Name** element for the two instances of this element in the **Members** collection MUST have one instance of each enumeration value from the **XMRawColumnMemberNameEnum** type (section [2.5.2.3.2.2](#Section_ab15d1be587e4c34af42bb17c8545587)).

###### XMRawColumnMemberType

The **XMRawColumnMemberType** complex type holds a **Member** item that is a property of the parent **XMRawColumn** object.

- &lt;xs:complexType name="XMRawColumnMemberType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Name" type="XMRawColumnMemberNameEnum"
- minOccurs="0"/>
- &lt;xs:element name="XMObject"&gt;
- &lt;xs:complexType&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="XMObjectTypeBase"&gt;
- <xs:attribute name="class"
- type="XMRawColumnXMObjectMemberClassNameEnum"/>
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Name:** The name of the **Member** object.

**XMObject:** A complex type that contains a nested instance of an **XMObject** element. The type of the element is an extension of **XMObjectTypeBase**. However, the actual content allowed in an instance is constrained and depends on the value of the **class** attribute of the **XMObject** element. The content of the **XMObject** element MUST follow the constraints depending on its **class** attribute value

The following attribute is added by extension for the **XMObject** element.

**class:** An enumeration value that specifies the class name of this **XMObject** element instance. When the **Name** element of the **Member** item has a particular value, the **XMObject** element of the **Member** item MUST have a specific value for the **class** attribute. The following table lists the constraints between the values of **Name** and **class**.

| Value of Name element | Required value of class attribute |
| --------------------- | --------------------------------- |
| "IntrinsicHierarchy"  | "XMHierarchy"                     |
| "ColumnStats"         | "XMColumnStats"                   |

###### XMRawColumnMemberNameEnum

The **XMRawColumnMemberNameEnum** simple type enumerates the allowed values for the name of a **Member** item in the **Members** collection of an **XMRawColumn** object.

- &lt;xs:simpleType name="XMRawColumnMemberNameEnum"&gt;
- &lt;xs:restriction base="XMObjectMemberNameEnum"&gt;
- &lt;xs:enumeration value="IntrinsicHierarchy"/&gt;
- &lt;xs:enumeration value="ColumnStats"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMRawColumnMemberNameEnum** type.

| Enumeration value    | Description                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- |
| "IntrinsicHierarchy" | The **Member** item represents the [**intrinsic hierarchy**](#gt_03b4105f-6f7b-4ea5-8b95-d2e6ecbc6ee0) of a column. |
| "ColumnStats"        | The **Member** item contains column statistics.                                                                     |

###### XMRawColumnXMObjectMemberClassNameEnum

The **XMRawColumnXMObjectMemberClassNameEnum** simple type enumerates the allowed values for the class name of the **XMObject** element that is contained in a **Member** item in the **Members** collection of an **XMRawColumn** object.

- &lt;xs:simpleType name="XMRawColumnXMObjectMemberClassNameEnum"&gt;
- &lt;xs:restriction base="XMObjectClassNameEnum"&gt;
- &lt;xs:enumeration value="XMHierarchy"/&gt;
- &lt;xs:enumeration value="XMColumnStats"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMRawColumnXMObjectMemberClassNameEnum** type.

| Enumeration value | Description                                                                                                         |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| "XMHierarchy"     | The **XMObject** element specifies information about the [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682). |
| "XMColumnStats"   | The **XMObject** element specifies statistics about the column.                                                     |

##### XMRawColumnCollectionsType

The **XMRawColumnCollectionsType** complex type holds a collection of **Collection** items, each of which contains a property for the parent **XMRawColumn** object. **Collection** items can be repeated multiple times within the collection.

- &lt;xs:complexType name="XMRawColumnCollectionsType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Collection" type="XMRawColumnCollectionType"
- minOccurs="1" maxOccurs="1"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Collection:** A **Collection** item that is a property for the parent **XMObject** element of class **XMRawColumn**. **Collection** items can be repeated within the collection.

###### XMRawColumnCollectionType

The **XMRawColumnCollectionType** complex type holds a **Collection** item that is a property of the parent **XMObject** object.

- &lt;xs:complexType name="XMRawColumnCollectionType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Name" type="XMObjectCollectionNameEnum"
- fixed="Segments"/>
- <xs:element name="XMObject" type="XMColumnSegmentXMObjectType"
- maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Name:** The name of the **Collection** object.

**XMObject:** A complex type that contains a nested instance of an **XMObject** element. The value of the **class** attribute of this **XMObject** element MUST equal "XMColumnSegment".

##### XMRawColumnDataObjectsType

The **XMRawColumnDataObjectsType** complex type holds data objects for the parent **XMRawColumn** object instance.

- &lt;xs:complexType name="XMRawColumnDataObjectsType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="DataObject" type="XMRawColumnDataObjectType"
- minOccurs="2" maxOccurs="2"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**DataObject:** A data object that holds information related to the data in the raw column. The two instances of the **DataObject** element in the **DataObjects** collection MUST abide by the following rules:

- The value of the **class** attribute for one of the **DataObject** elements MUST be "XMRawColumnPartitionDataObject".
- The value of the **class** attribute for one of the **DataObject** elements MUST be one of the following:
  - "XMValueDataDictionary&lt;XM_Long&gt;"
  - "XMValueDataDictionary&lt;XM_Real&gt;"
  - "XMHashDataDictionary&lt;XM_Long&gt;"
  - "XMHashDataDictionary&lt;XM_Real&gt;"
  - "XMHashDataDictionary&lt;XM_String&gt;"

###### XMRawColumnDataObjectType

The **XMRawColumnDataObjectType** complex type holds the data for one data object item in the collection of data objects for the parent **XMObject** element.

- &lt;xs:complexType name="XMRawColumnDataObjectType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="XMObject"&gt;
- &lt;xs:complexType&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="XMObjectTypeBase"&gt;
- <xs:attribute name="class"
- type="XMRawColumnXMObjectDataObjectClassNameEnum"/>
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**XMObject:** A complex type that contains a nested instance of an **XMObject** element. The type of the element is an extension of **XMObjectTypeBase**. However, the actual content that is allowed in an instance is constrained and depends on the value of the **class** attribute of the **XMObject** element. The content of the **XMObject** element MUST follow the constraints depending on its **class** attribute value.

**class:** An enumeration value that specifies the class name of this **XMObject** element instance.

###### XMRawColumnXMObjectDataObjectClassNameEnum

The **XMRawColumnXMObjectDataObjectClassNameEnum** simple type enumerates the allowed values for the **class** attribute of the **XMObject** element that is contained in a **DataObject** item in the **DataObjects** collection of an **XMRawColumn** object.

- &lt;xs:simpleType name="XMRawColumnXMObjectDataObjectClassNameEnum"&gt;
- &lt;xs:restriction base="XMObjectClassNameEnum"&gt;
- &lt;xs:enumeration value="XMValueDataDictionary<XM_Long&gt;"/>
- &lt;xs:enumeration value="XMValueDataDictionary<XM_Real&gt;"/>
- &lt;xs:enumeration value="XMHashDataDictionary<XM_Real&gt;"/>
- &lt;xs:enumeration value="XMHashDataDictionary<XM_Long&gt;"/>
- &lt;xs:enumeration value="XMHashDataDictionary<XM_String&gt;"/>
- &lt;xs:enumeration value="XMRawColumnPartitionDataObject"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMRawColumnXMObjectDataObjectClassNameEnum** type.

| Enumeration value                       | Description                                                                    |
| --------------------------------------- | ------------------------------------------------------------------------------ |
| "XMValueDataDictionary&lt;XM_Long&gt;"  | The column has a value data dictionary of type **long**.                       |
| "XMValueDataDictionary&lt;XM_Real&gt;"  | The column has a value data dictionary of type **real**.                       |
| "XMHashDataDictionary&lt;XM_Long&gt;"   | The column has a hash data dictionary of type **long**.                        |
| "XMHashDataDictionary&lt;XM_Real&gt;"   | The column has a hash data dictionary of type **real**.                        |
| "XMHashDataDictionary&lt;XM_String&gt;" | The column has a hash data dictionary of type **string**.                      |
| "XMRawColumnPartitionDataObject"        | The **XMObject** specifies information about the partition for the raw column. |

#### XMObject class="XMRelationship"

When the **class** attribute value for the **XMObject** element is "XMRelationship", the **XMObject** element contains the metadata for a relationship description, and the type of the **XMObject** element is **XMRelationshipXMObjectType**.

- &lt;xs:complexType name="XMRelationshipXMObjectType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Properties" type="XMRelationshipPropertiesType"/&gt;
- &lt;xs:element name="DataObjects" type="XMRelationshipDataObjectsType"/&gt;
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMRelationship"/>
- &lt;/xs:complexType&gt;

**Properties:** The property values for the **XMRelationship** object.

**DataObjects:** A collection of **DataObject** complex type items, each of which contains an object that has information about the relationship.

**ProviderVersion:** The provider version.

**name:** The name of the **XMRelationship** object instance.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMRelationshipPropertiesType

The **XMRelationshipPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class " XMRelationship".

- &lt;xs:complexType name="XMRelationshipPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="PrimaryTable" type="xs:string"/&gt;
- &lt;xs:element name="PrimaryColumn" type="xs:string"/&gt;
- &lt;xs:element name="ForeignColumn" type="xs:string"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**PrimaryTable:** The name of the table in which the primary key column exists.

**PrimaryColumn:** The primary key column.

**ForeignColumn:** The foreign key column.

##### XMRelationshipDataObjectsType

The **XMRelationshipDataObjectsType** complex holds data objects for the parent **XMRelationship** object instance.

- &lt;xs:complexType name="XMRelationshipDataObjectsType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="DataObject" type="XMRelationshipDataObjectType"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**DataObject:** A data object item that holds information related to the data for the relationship.

##### XMRelationshipDataObjectType

The **XMRelationshipDataObjectType** complex type holds the data for one data object item in the collection of data objects for the parent **XMObject** element.

- &lt;xs:complexType name="XMRelationshipDataObjectType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="XMObject"&gt;
- &lt;xs:complexType&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="XMObjectTypeBase"&gt;
- <xs:attribute name="class"
- type="XMRelationshipXMDataObjectXMObjectClassNameEnum"/>
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**XMObject:** A complex type that contains a nested instance of an **XMObject** element. The type of the element is an extension of **XMObjectTypeBase**. However, the actual content allowed in an instance is constrained and depends on the value of the **class** attribute of the **XMObject** element. The content of the **XMObject** element MUST follow the constraints depending on its **class** attribute value.

**class:** An enumeration value that specifies the class name of this **XMObject** element instance.

##### XMRelationshipXMDataObjectXMObjectClassNameEnum

The **XMRelationshipXMDataObjectXMObjectClassNameEnum** simple type enumerates the allowed values for the **class** attribute of the **XMObject** element that is contained in a **DataObject** item in the **DataObjects** collection of an **XMRelationship** object.

- &lt;xs:simpleType name="XMRelationshipXMDataObjectXMObjectClassNameEnum"&gt;
- &lt;xs:restriction base="XMObjectClassNameEnum"&gt;
- &lt;xs:enumeration value="XMRelationshipIndexDenseDIDs"/&gt;
- &lt;xs:enumeration value="XMRelationshipIndexSparseDIDs"/&gt;
- &lt;xs:enumeration value="XMRelationshipIndex123DIDs"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMRelationshipXMDataObjectXMObjectClassNameEnum** type.

| Enumeration value               | Description                                                                                                                                     |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| "XMRelationshipIndexDenseDIDs"  | The object is a relationship index with dense data identifiers.                                                                                 |
| "XMRelationshipIndexSparseDIDs" | The object is a relationship index with sparse data identifiers.                                                                                |
| "XMRelationshipIndex123DIDs"    | The object is a relationship index that is used only for the **RowNumber** column (section [2.3.4](#Section_7d9074aabea740e2b5d822e9cadeb778)). |

#### XMObject class="XMRelationshipIndexSparseDIDs"

When the **class** attribute value for the **XMObject** element is "XMRelationshipIndexSparseDIDs", the **XMObject** element contains the metadata for relationship index where the data identifiers are sparse, and the type of the **XMObject** element is **XMRelationshipIndexSparseDIDsXMObjectType**.

- &lt;xs:complexType name="XMRelationshipIndexSparseDIDsXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRelationshipIndexSparseDIDsPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMRelationshipIndexSparseDIDs"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMRelationshipIndexSparseDIDsPropertiesType

The **XMRelationshipIndexSparseDIDsPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMRelationshipIndexSparseDIDs".

- &lt;xs:complexType name="XMRelationshipIndexSparseDIDsPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Flags"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="1"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Flags:** The flags for the relationship index. The only value that can be set is 0x01, which means that the index potentially has relational integrity violations.

#### XMObject class="XMRelationshipIndexDenseDIDs"

When the **class** attribute value for the **XMObject** element is "XMRelationshipIndexDenseDIDs", the **XMObject** element contains the metadata for a relationship index where the data identifiers are dense, and the type of the **XMObject** element is **XMRelationshipIndexDenseDIDsXMObjectType**.

- &lt;xs:complexType name="XMRelationshipIndexDenseDIDsXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRelationshipIndexDenseDIDsPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMRelationshipIndexDenseDIDs"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMRelationshipIndexDenseDIDsPropertiesType

The **XMRelationshipIndexDenseDIDsPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMRelationshipIndexDenseDIDs".

- &lt;xs:complexType name="XMRelationshipIndexDenseDIDsPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Records" type="xs:long"/&gt;
- &lt;xs:element name="TableName" type="xs:string"/&gt;
- &lt;xs:element name="Flags"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="1"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Records:** The count of records.

**TableName:** The table name. This value MUST be the same as the value of the **ID** element (section [2.6.6](#Section_f7381e33c04e409996d45966dbd38b42)) for the dimension that corresponds to this table.

**Flags:** The flags for the relationship index. The only value that can be set is 0x01, which means that the index potentially has relational integrity violations.

#### XMObject class="XMRelationshipIndex123DIDs"

When the **class** attribute value for the **XMObject** element is "XMRelationshipIndex123DIDs", the **XMObject** element contains metadata for a relationship index that is used only for the **RowNumber** column when that column is on the primary side of the relationship, and the type of the **XMObject** element is **XMRelationshipIndex123DIDsXMObjectType**. For more details about the **RowNumber** column, see section [2.3.4](#Section_7d9074aabea740e2b5d822e9cadeb778).

- &lt;xs:complexType name="XMRelationshipIndex123DIDsXMObjectType"&gt;
- &lt;xs:all&gt;
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMRelationshipIndex123DIDs"/>
- &lt;/xs:complexType&gt;

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMColumnStats"

When the **class** attribute value for the **XMObject** element is "XMColumnStats", the **XMObject** element contains statistical information about the column, and the type of the **XMObject** element is **XMColumnStatsXMObjectType**.

- &lt;xs:complexType name="XMColumnStatsXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMColumnStatsPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMColumnStats"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMColumnStatsPropertiesType

The **XMColumnStatsPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMColumnStats".

- &lt;xs:complexType name="XMColumnStatsPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="DistinctStates" type="xs:int"/&gt;
- &lt;xs:element name="MinDataID" type="xs:int"/&gt;
- &lt;xs:element name="MaxDataID" type="xs:int"/&gt;
- &lt;xs:element name="OriginalMinSegmentDataID" type="xs:int"/&gt;
- &lt;xs:element name="RLESortOrder" type="xs:long"/&gt;
- &lt;xs:element name="RowCount" type="xs:long"/&gt;
- &lt;xs:element name="HasNulls" type="xs:boolean"/&gt;
- &lt;xs:element name="RLERuns" type="xs:long"/&gt;
- &lt;xs:element name="OthersRLERuns" type="xs:long"/&gt;
- &lt;xs:element name="Usage"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="3"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="DBType"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:short"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="29"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="XMType"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:int"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="3"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="CompressionType"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:int"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="2"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="CompressionParam" type="xs:long"/&gt;
- &lt;xs:element name="EncodingHint"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:int"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="2"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:element name="AggCounter" type="xs:long"/&gt;
- &lt;xs:element name="WhereCounter" type="xs:long"/&gt;
- &lt;xs:element name="OrderByCounter" type="xs:long"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**DistinctStates:** The number of distinct values, including NULL, in the column.

**MinDataID:** The minimum data identifier for the column.

**MaxDataID:** The maximum data identifier for the column.

**OriginalMinSegmentDataID:** The minimum data identifier for a segment.

**RLESortOrder:** A value that is unused, MUST be -1, and MUST be ignored.

**RowCount:** The number of rows in the column segment.

**HasNulls:** A value that specifies whether the column has NULL values.

**RLERuns:** An estimate of the number of RLE runs.

**OthersRLERuns:** The number of RLE runs that are not solid runs. A solid run is a run of consecutive, identical values that cannot be compressed by RLE techniques.

**Usage:** An enumeration value that specifies the column usage. The values in the following table are used.

| Value | Meaning                                      |
| ----- | -------------------------------------------- |
| 0     | The column is the primary key for the table. |
| 1     | The column is the foreign key for the table. |
| 2     | The column contains BLOBs.                   |
| 3     | The column is a regular one.                 |

**DBType:** An enumeration value that specifies the [**OLE DB**](#gt_333f4fb1-4882-48df-bce6-f9961b408f31) type of the column. The values in the following table are used.

| Value | OLE DB type |
| ----- | ----------- |
| 0     | Empty       |
| 1     | Null        |
| 2     | I2          |
| 3     | I4          |
| 4     | Real4       |
| 5     | Real8       |
| 6     | Currency    |
| 7     | Date        |
| 11    | Boolean     |
| 18    | UI2         |
| 19    | UI4         |
| 20    | I8          |
| 21    | UI8         |
| 128   | Bytes       |
| 130   | Wide String |

**XMType:** An enumeration value. The values in the following table are used.

| Value | Meaning   |
| ----- | --------- |
| 0     | XM_Long   |
| 1     | XM_Real   |
| 2     | XM_String |

**CompressionType:** An enumeration value that specifies the type of compression. The values in the following table are used.

| Value | Type of compression                                                      |
| ----- | ------------------------------------------------------------------------ |
| 0     | Automatic (that is, determined by the system)                            |
| 1     | NoSplit (see section [2.7.1](#Section_85c2024e34e743748fa08b4ca8fe4f2d)) |

**CompressionParam:** Either the bit length for NoSplit compression or the bookmark distance for RLE compression.

**EncodingHint:** An enumeration value that specifies the type of encoding. The values in the following table are used.

| Value | Type of encoding                                               |
| ----- | -------------------------------------------------------------- |
| 0     | Automatic (that is, determined by the system)                  |
| 1     | [**hash**](#gt_b7e2b611-0af5-4fec-8af2-3f9ce7bad205) encoding  |
| 2     | [**value encoding**](#gt_41e3f27c-7eb1-4513-bf17-3edda894c54a) |

**AggCounter:** A value that is unused and MUST be ignored.

**WhereCounter:** A value that is unused and MUST be ignored.

**OrderByCounter:** A value that is unused and MUST be ignored.

#### XMObject class="XMHierarchy"

When the **class** attribute value for the **XMObject** element is "XMHierarchy", the **XMObject** element contains metadata about the [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) that represents the column, and the type of the **XMObject** element is **XMHierarchyXMObjectType**.

- &lt;xs:complexType name="XMHierarchyXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMHierarchyPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMHierarchy"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**name:** The name of the **XMHierarchy** object instance.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMHierarchyPropertiesType

The **XMHierarchyPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMHierarchy".

- &lt;xs:complexType name="XMHierarchyPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="SortOrder" type="xs:int"/&gt;
- &lt;xs:element name="IsProcessed" type="xs:boolean"/&gt;
- &lt;xs:element name="TypeMaterialization" type="xs:int"/&gt;
- &lt;xs:element name="ColumnPosition2DataID" type="xs:long"/&gt;
- &lt;xs:element name="ColumnDataID2Position" type="xs:long"/&gt;
- &lt;xs:element name="DistinctDataIDs" type="xs:long"/&gt;
- &lt;xs:element name="TableStore" type="xs:string"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**SortOrder:** An integer value that specifies the sort order. The values in the following table are valid.

| Value | Sort order |
| ----- | ---------- |
| 0     | Ascending  |
| 2     | Unsorted   |

**IsProcessed:** A Boolean value that specifies whether the [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) has been processed.

**TypeMaterialization:** An integer value that specifies the type of materialization. The values in the following table are valid.

| Value | Type of materialization                                                                                                                                      |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| -1    | The type of materialization is unspecified. This value MUST NOT be used if **IsProcessed** is not equal to FALSE.                                            |
| 0     | The hierarchy gets materialized as a table of two columns: one for position-to-data identifier mapping, and another for data identifier-to-position mapping. |
| 1     | The hierarchy gets materialized as a column for position-to-data identifier mapping and a hash for data identifier-to-position mapping.                      |
| 2     | No materialization occurs because the column is empty.                                                                                                       |
| 3     | No materialization occurs because an identity column is present.                                                                                             |

**ColumnPosition2DataID:** A long value that specifies whether a column position-to-data identifier index is used. The values in the following table are valid.

| Value | Meaning                                                 |
| ----- | ------------------------------------------------------- |
| 0     | A column position-to-data identifier index is used.     |
| -1    | A column position-to-data identifier index is not used. |

**ColumnDataID2Position:** A long value that specifies whether a data identifier-to-column position index is used. The values in the following table are valid.

| Value | Meaning                                                 |
| ----- | ------------------------------------------------------- |
| 1     | A data identifier-to-column position index is used.     |
| -1    | A data identifier-to-column position index is not used. |

**DistinctDataIDs:** The number of distinct data identifiers.

**TableStore:** The root name of the hierarchy metadata file that is generated by the system. This value includes neither the version number that is part of the file name nor the "tbl.xml" that appears at the end of the file name.

#### XMObject class="XMUserHierarchy"

When the **class** attribute value for the **XMObject** element is "XMUserHierarchy", the **XMObject** element contains metadata about user-defined [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682), and the type of the **XMObject** element is **XMUserHierarchyXMObjectType**.

- &lt;xs:complexType name="XMUserHierarchyXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMUserHierarchyPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMUserHierarchy"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**name:** The name of the **XMuserHierarchy** object instance.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMUserHierarchyPropertiesType

The **XMUserHierarchyPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMUserHierarchy".

- &lt;xs:complexType name="XMUserHierarchyPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="IsProcessed" type="xs:boolean"/&gt;
- &lt;xs:element name="TableStore" type="xs:string"/&gt;
- &lt;xs:element name="TableName" type="xs:string"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**IsProcessed:** A Boolean value that specifies whether the user hierarchy has been processed.

**TableStore:** A string value that specifies name and unique value combinations for a user hierarchy. The string is constructed as a series of interpretable parts, with a dollar sign (\$) as the separator. The names of the columns in the user hierarchy, from the top down, are included, and after each level's name is a zero-based starting number of unique values that exist at the levels numbered higher than the current level. The names that are used MUST match the **ID** element of the **Level** element of the **Hierarchy** element that is contained in the dimension (see section [2.6.6](#Section_f7381e33c04e409996d45966dbd38b42)).

For example, assume that a user hierarchy with 4 levels exists. Assume that from the top down, the levels are Country, State, City, and Customer. In the data for this hierarchy, 2 unique values exist for Country, 4 unique values exist for Country-State combinations, and 7 unique values exist for Country-State-City combinations. The string would then be "\$Country\$0\$State\$2\$City\$6\$Customer\$13\$".

In referring to levels, the "ALL" level is not included; the references are to the highest user-defined level, which is one level below the ALL level. The first component of the string is the dollar sign (\$). Then comes the column name that represents the highest level in the user hierarchy, which is "Country". Each substring component continues to be separated by a dollar sign (\$). The next component of the string is the number of unique combinations that are higher than this level. That value is "0" because no levels exist that are higher than this one. The next level name is "State". Because 2 countries exist, 2 unique values exist at levels above State, so the value "2" appears in the string. The next level name is "City". Because 4 unique combinations of Country-State and 2 unique countries exist, a total of 6 combinations exist at levels above the City level. Therefore, "6" is added to the string. The next and lowest level is "Customer". Because 7 unique Country-State-City values exist, and there already were 6 unique level values, 13 unique Country-State-City values now exist above the Customer level. Hence, the value "13" is added to the string value. The string value ends with a dollar sign (\$).

**TableName:** The root name of the user hierarchy metadata file that is generated by the system. This value includes neither the version number that is part of the file name nor the "tbl.xml" that appears at the end of the file name.

#### XMObject class="XMHierarchyDataID2PositionHashIndex"

When the **class** attribute value for the **XMObject** element is "XMHierarchyDataID2PositionHashIndex", the **XMObject** element contains metadata for the [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) data identifier-to-position hash index mapping, and the type of the **XMObject** element is **XMHierarchyDataID2PositionHashIndexXMObjectType**.

- &lt;xs:complexType name="XMHierarchyDataID2PositionHashIndexXMObjectType"&gt;
- &lt;xs:all/&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMHierarchyDataID2PositionHashIndex"/>
- &lt;/xs:complexType&gt;

**ProviderVersion:** The provider version.

**name:** The name of the **XMHierarchyDataID2PositionHashIndex** object instance.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMColumnSegment"

When the **class** attribute value for the **XMObject** element is "XMColumnSegment", the **XMObject** element contains metadata for a column segment, and the type of the **XMObject** element is **XMColumnSegmentXMObjectType**.

- &lt;xs:complexType name="XMColumnSegmentXMObjectType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Properties" type="XMColumnSegmentPropertiesType"/&gt;
- &lt;xs:element name="Members" type="XMColumnSegmentMembersType"/&gt;
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMColumnSegment">
- &lt;/xs:attribute&gt;
- &lt;/xs:complexType&gt;

**Properties:** The property values for the **XMColumnSegment** object.

**Members:** A collection of **Member** complex type items, each of which contains a complex property for the **XMColumnSegment** object.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMColumnSegmentPropertiesType

The **XMColumnSegmentPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMColumnSegment".

- &lt;xs:complexType name="XMColumnSegmentPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Records" type="xs:long"/&gt;
- &lt;xs:element name="Mask"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="2"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Records:** The number of records in the column segment.

**Mask:** A value that is unused and MUST be ignored.

##### XMColumnSegmentMembersType

The **XMColumnSegmentMembersType** complex type holds a collection of **Member** items, each of which contains a property for the parent **XMColumnSegment** object.

- &lt;xs:complexType name="XMColumnSegmentMembersType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Member" type="XMColumnSegmentMemberType"
- minOccurs="3" maxOccurs="3"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Member:** A complex type element that contains a complex **Member** item, which contains a property for the parent **XMObject** element. The value of the **Name** element for the three instances of this element in the **Members** collection MUST have one instance of each enumeration value from the **XMColumnSegmentMemberNameEnum** type (section [2.5.2.12.2.2](#Section_aa130be4596d46309db3367ef5954f0a)).

###### XMColumnSegmentMemberType

The **XMColumnSegmentMemberType** complex type holds a **Member** item that is a property of the parent **XMColumnSegment** object.

- &lt;xs:complexType name="XMColumnSegmentMemberType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Name" type="XMColumnSegmentMemberNameEnum"
- minOccurs="0"/>
- &lt;xs:element name="XMObject"&gt;
- &lt;xs:complexType&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="XMObjectTypeBase"&gt;
- <xs:attribute name="class"
- type="XMColumnSegmentXMObjectMemberClassNameEnum"/>
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Name:** The name of the **Member** object.

**XMObject:** A complex type that contains a nested instance of an **XMObject** element. The type of the element is an extension of **XMObjectTypeBase**. However, the actual content allowed in an instance is constrained and depends on the value of the **class** attribute of the **XMObject** element. The content of the **XMObject** element MUST follow the constraints depending on its **class** attribute value.

**class:** An enumeration value that specifies the class name of this **XMObject** element instance. When the **Name** element of the **Member** item has a particular value, the **XMObject** element of the **Member** item MUST have a specific value for the **class** attribute. The following table lists the constraints between the values of **Name** and **class**.

| Value of Name element | Required value of class attribute                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "SubSegment"          | "XMColumnSegment"                                                                                                                                        |
| "CompressionInfo"     | "XMHybridRLECompressionInfo class<XMRENoSplitCompressionInfo<_n_\>>", where _n_ = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 21, 32, or XM123CompressionInfo |
| "ColumnSegmentStats"  | "XMColumnSegmentStats"                                                                                                                                   |

###### XMColumnSegmentMemberNameEnum

The **XMColumnSegmentMemberNameEnum** simple type enumerates the allowed values for the name of a **Member** item in the **Members** collection of an **XMColumnSegment** object.

- &lt;xs:simpleType name="XMColumnSegmentMemberNameEnum"&gt;
- &lt;xs:restriction base="XMObjectMemberNameEnum"&gt;
- &lt;xs:enumeration value="SubSegment"/&gt;
- &lt;xs:enumeration value="CompressionInfo"/&gt;
- &lt;xs:enumeration value="ColumnSegmentStats"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMColumnSegmentMemberNameEnum** type.

| Enumeration value    | Description                                                                             |
| -------------------- | --------------------------------------------------------------------------------------- |
| "SubSegment"         | The **Member** item specifies information about the subsegment.                         |
| "CompressionInfo"    | The **Member** item specifies information about the compression for the column segment. |
| "ColumnSegmentStats" | The **Member** item specifies statistical information for the column segment.           |

###### XMColumnSegmentXMObjectMemberClassNameEnum

The **XMColumnSegmentXMObjectMemberClassNameEnum** simple type enumerates the allowed values for the **class** attribute of the **XMObject** element that is contained in a **Member** item for a member of a **XMColumnSegment** object.

- &lt;xs:simpleType name="XMColumnSegmentXMObjectMemberClassNameEnum"&gt;
- &lt;xs:restriction base="XMObjectClassNameEnum"&gt;
- &lt;xs:enumeration value="XMColumnSegment"/&gt;
- &lt;xs:enumeration value="XMColumnSegmentStats"/&gt;
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>"/>
- <xs:enumeration value=
- "XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;"/>
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMColumnSegmentXMObjectMemberClassNameEnum** type.

| Enumeration value                                                        | Description                                                                                                                                                                             |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "XMColumnSegment"                                                        | The object specifies information about the column segment.                                                                                                                              |
| "XMColumnSegmentStats"                                                   | The object specifies column segment statistics.                                                                                                                                         |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;1&gt;. For more details, see section [2.7.3.2](#Section_1e5fc6ecce42474595ce45234c4fc0d9).   |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;2&gt;. For more details, see section [2.7.3.3](#Section_1e9a5c2f099944a38e3f0bfa7c8f189c).   |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;3&gt;. For more details, see section [2.7.3.4](#Section_71c0797f7a9a4b429e3320b793984de9).   |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;4&gt;. For more details, see section [2.7.3.5](#Section_a75b1cc87a6b4a4389e93d8279736807).   |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;5&gt;. For more details, see section [2.7.3.6](#Section_6ae5ddada98943a0b0a58fa5dd7689da).   |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;6&gt;. For more details, see section [2.7.3.7](#Section_51319b44f8984618b99c59bfca08684e).   |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;7&gt;. For more details, see section [2.7.3.8](#Section_8c3038556487458ebfa0c7acbfd893d1).   |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;8&gt;. For more details, see section [2.7.3.9](#Section_0ef68fbfb8ca48589aa63252bdb8d241).   |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>"  | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;9&gt;. For more details, see section [2.7.3.10](#Section_ca4d75a90ff8452a93261554dc8ff129).  |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>" | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;10&gt;. For more details, see section [2.7.3.11](#Section_01936eeba5b54920b6b8a0e0ac93fad6). |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>" | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;12&gt;. For more details, see section [2.7.3.12](#Section_da07ed21b1da41819040a90dc952bbf7). |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>" | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;16&gt;. For more details, see section [2.7.3.13](#Section_a36cac4ae7104fa4bd5793982abe9a79). |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>" | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;21&gt;. For more details, see section [2.7.3.14](#Section_a57aa02ec18b442ebfa074172e6778f5). |
| "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>" | The column is compressed by means of hybrid RLE compression with XMRENoSplitCompression&lt;32&gt;. For more details, see section [2.7.3.15](#Section_c4cd2eac036445e5b5e60734496344bc). |
| "XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;"           | The column is compressed by means of hybrid RLE compression with XM123Compression. For more details, see section [2.7.3.16](#Section_1cf84136dae246ee99de91fb24fbffc4).                 |

#### XMObject class="XMPartition"

When the **class** attribute value for the **XMObject** element is "XMPartition", the **XMObject** element contains metadata about the [**partition**](#gt_2f24f458-7d39-47a2-93f7-de433ea85c75), and the type of the **XMObject** element is **XMPartitionXMObjectType**.

- &lt;xs:complexType name="XMPartitionXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMPartitionPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMPartition"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**name:** The name of the partition. This name is the same as the name of the source data table.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMPartitionPropertiesType

The **XMPartitionPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMPartition".

- &lt;xs:complexType name="XMPartitionPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="IsProcessed" type="xs:boolean"/&gt;
- &lt;xs:element name="Partition" type="xs:int"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**IsProcessed:** A Boolean value that specifies whether the partition has been processed.

**Partition:** An incremental identifier for the partition.

#### XMObject class="XMMultiPartSegmentMap"

When the **class** attribute value for the **XMObject** element is "XMMultiPartSegmentMap", the **XMObject** element contains mapping information for data segments, and the type of the **XMObject** element is **XMMultiPartSegmentMapXMObjectType**.

- &lt;xs:complexType name="XMMultiPartSegmentMapXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMMultiPartSegmentMapPropertiesType"/>
- &lt;xs:element name="Collections" type="XMMultiPartSegmentMapCollectionsType"/&gt;
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMMultiPartSegmentMap"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**Collections:** A collection of **Collection** complex type items, each of which contains a complex property for the **XMMultiPartSegmentMap** object. The **Collection** complex property can be repeated multiple times.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of the **XMObject** element.

##### XMMultiPartSegmentMapPropertiesType

The **XMMultiPartSegmentMapPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMMultiPartSegmentMap".

- &lt;xs:complexType name="XMMultiPartSegmentMapPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="FirstPartitionRecordCount" type="xs:long"/&gt;
- &lt;xs:element name="FirstPartitionSegmentCount" type="xs:long"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**FirstPartitionRecordCount:** A value that is unused and MUST be ignored.

**FirstPartitionSegmentCount:** A value that is unused and MUST be ignored.

##### XMMultiPartSegmentMapCollectionsType

The **XMMultiPartSegmentMapCollectionsType** complex type contains the collection properties that are allowed when the **XMObject** element is of class "XMMultiPartSegmentMap".

- &lt;xs:complexType name="XMMultiPartSegmentMapCollectionsType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Collection"
- type="XMMultiPartSegmentMapCollectionType"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Collection:** A collection of **Collection** complex type items, each of which contains a complex property for the **XMMultiPartSegmentMap** object. Each **Collection** item can be repeated multiple times.

##### XMMultiPartSegmentMapCollectionType

The **XMMultiPartSegmentMapCollectionType** complex type holds a **Collection** item that is a property of the parent **XMMultiPartSegmentMap** object.

- &lt;xs:complexType name="XMMultiPartSegmentMapCollectionType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Name" type="XMObjectCollectionNameEnum"
- fixed="Partitions"/>
- &lt;xs:element name="XMObject" minOccurs="0" maxOccurs="unbounded"&gt;
- &lt;xs:complexType&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="XMObjectTypeBase"&gt;
- <xs:attribute name="class" type=
- "XMMultiPartSegmentMapXMObjectCollectionClassNameEnum"/>
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Name:** The name of the **Collection** object.

**XMObject:** A complex type that contains a nested instance of an **XMObject** element.

###### XMMultiPartSegmentMapXMObjectCollectionClassNameEnum

The **XMMultiPartSegmentMapXMObjectCollectionClassNameEnum** simple type enumerates the allowed values for the class name of the **XMObject** element that is contained in a **Collection** item in the **Collections** collection of an **XMMultiPartSegmentMap** object.

- <xs:simpleType name=
- "XMMultiPartSegmentMapXMObjectCollectionClassNameEnum">
- &lt;xs:restriction base="XMObjectClassNameEnum"&gt;
- &lt;xs:enumeration value="XMSegment1Map"/&gt;
- <xs:enumeration value=
- "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"/>
- <xs:enumeration value=
- "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;"/>
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMMultiPartSegmentMapXMObjectCollectionClassNameEnum** type.

| Enumeration value                                                   | Description                                                                                                                                                                                                    |
| ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "XMSegment1Map"                                                     | A segment map for a column that has a single segment.                                                                                                                                                          |
| "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;" | A segment map of equally sized segments (except that the size of the last segment can differ from that of the others). Note that complex instantiation occurs when the segment size is determined at run time. |
| "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"    | A segment map of equally sized segments (except that the size of the last segment can differ from that of the others). Note that fast instantiation is for predetermined segment sizes.                        |

#### XMObject class="XMSegment1Map"

When the **class** attribute value for the **XMObject** element is "XMSegment1Map", the **XMObject** element contains mapping information for the first data segment, and the type of the **XMObject** element is **XMSegment1MapXMObjectType**.

- &lt;xs:complexType name="XMSegment1MapXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMSegment1MapPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMSegment1Map"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of the **XMObject** element.

##### XMSegment1MapPropertiesType

The **XMSegment1MapPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMSegment1Map".

- &lt;xs:complexType name="XMSegment1MapPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Records" type="xs:long"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Records:** The number of records in the segment map.

#### XMObject class="XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"

When the **class** attribute value for the **XMObject** element is "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;", the **XMObject** element contains metadata for a segment map of equally sized segments (except that size of the last segment can differ from that of the others), and the type of the **XMObject** element is **XMSegmentEqualMapEx_XMSegmentEqualMap_FastInstantiationXMObjectType**. Fast instantiation means that the segment size is predetermined and does not need to be determined at run time.

- <xs:complexType name=
- "XMSegmentEqualMapEx_XMSegmentEqualMap_FastInstantiationXMObjectType">
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMSegmentEqualMapEx_PropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMSegmentEqualMapEx_PropertiesType

The **XMSegmentEqualMapEx_PropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of either class "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;" or class "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"

- &lt;xs:complexType name="XMSegmentEqualMapEx_PropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Segments" type="xs:long"/&gt;
- &lt;xs:element name="Records" type="xs:long"/&gt;
- &lt;xs:element name="RecordsPerSegment" type="xs:long"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Segments:** The number of segments.

**Records:** The total number of records in all of the segments.

**RecordsPerSegment:** The number of records per segment.

#### XMObject class="XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;"

When the **class** attribute value for the **XMObject** element is "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;", the **XMObject** element contains metadata for a segment map of equally sized segments (except that size of the last segment can differ from that of the others), and the type of the **XMObject** element is **XMSegmentEqualMapEx_XMSegmentEqualMap_ComplexInstantiationXMObjectType**. Complex instantiation means that the segment size is determined at run time.

- <xs:complexType name=
- "XMSegmentEqualMapEx_XMSegmentEqualMap_ComplexInstantiationXMObjectType">
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMSegmentEqualMapEx_PropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMSegmentEqualMapEx&lt;XMSegmentEqualMap_ComplexInstantiation&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMValueDataDictionary&lt;XM_Long&gt;"

When the **class** attribute value for the **XMObject** element is "XMValueDataDictionary&lt;XM_Long&gt;", the **XMObject** element contains metadata for a value dictionary of **long** values, and the type of the **XMObject** element is **XMObject_ValueDictionaryLongType**.

- &lt;xs:complexType name="XMObject_ValueDictionaryLongType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="PropertiesValueDictionaryType"/>
- &lt;/xs:all&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMValueDataDictionary&lt;XM_Long&gt;"/>
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

**ProviderVersion:** The provider version.

##### PropertiesValueDictionaryType

The **PropertiesValueDictionaryType** complex type contains the specific properties that are allowed when the **XMObject** element is of either class "XMValueDictionary&lt;XM_Real&gt;" or "XMValueDictionary&lt;XM_Long&gt;".

- &lt;xs:complexType name="PropertiesValueDictionaryType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="DataVersion" type="xs:int"/&gt;
- &lt;xs:element name="BaseId" type="xs:long"/&gt;
- &lt;xs:element name="Magnitude" type="xs:double"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**DataVersion:** The internal version number for this data. This version number is not required to match the version numbers of other objects within the same table or column.

**BaseId:** A value that is part of the calculation used to map from a data identifier to a data value. To perform such a mapping, add this value to the data identifier, and then multiply by the value of the **Magnitude** element.

**Magnitude:** A value that is part of the calculation used to map from a data identifier to a data value. To perform such a mapping, add the value of the **BaseId** element to the data identifier, and then multiply by this value.

#### XMObject class="XMValueDataDictionary&lt;XM_Real&gt;"

When the **class** attribute value for the **XMObject** element is "XMValueDataDictionary&lt;XM_Real&gt;", the **XMObject** element contains metadata for a value dictionary of **real** values, and the type of the **XMObject** element is **XMObject_ValueDictionaryRealType**.

- &lt;xs:complexType name="XMObject_ValueDictionaryRealType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="PropertiesValueDictionaryType"/>
- &lt;/xs:all&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMValueDataDictionary&lt;XM_Real&gt;"/>
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**Class:** An enumeration value that specifies the class name of this **XMObject** element.

**ProviderVersion:** The provider version.

#### XMObject class="XMHashDataDictionary&lt;XM_Real&gt;"

When the **class** attribute value for the **XMObject** element is "XMHashDataDictionary&lt;XM_Real&gt;", the **XMObject** element contains metadata for a hash dictionary of **real** values, and the type of the **XMObject** element is **XMObject_HashDictionaryRealType**.

- &lt;xs:complexType name="XMObject_HashDictionaryRealType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="PropertiesHashDictionaryRealType"/>
- &lt;/xs:all&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMHashDataDictionary&lt;XM_Real&gt;"/>
- &lt;xs:attributeGroup ref="HashDictionaryAttributeGroup"/&gt;
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

**HashDictionaryAttributeGroup:** An attribute group that specifies the common attributes for all hash dictionary **XMObject** objects.

##### HashDictionaryAttributeGroup

The **HashDictionaryAttributeGroup** attribute group contains the attributes that are common to the **XMObject** objects for hash dictionaries.

- &lt;xs:attributeGroup name="HashDictionaryAttributeGroup"&gt;
- &lt;xs:attribute name="name"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:string"&gt;
- <xs:pattern value=
- "\\d\*\\.Table-\[a-zA-Z0-9\$^&'@{},=!\$#()%~\_\\\[\\\]\\.\\-\\+\]\*\\.dictionary"/>
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:attribute&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;/xs:attributeGroup&gt;

**name:** The name of the dictionary file. For information about the interpretation of the components of this attribute, see section [2.2.3.7.2.6](#Section_27a6305effdc4535901acc65a202b24f).

**ProviderVersion:** The provider version.

##### PropertiesHashDictionaryRealType

The **PropertiesHashDictionaryRealType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMHashDictionary&lt;XM_Real&gt;". This type is also the base type for extension for other hash dictionary **XMObject** types.

- &lt;xs:complexType name="PropertiesHashDictionaryRealType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="DataVersion" type="xs:int"/&gt;
- &lt;xs:element name="LastId" type="xs:int"/&gt;
- &lt;xs:element name="Nullable" type="xs:boolean"/&gt;
- &lt;xs:element name="Unique" type="xs:boolean"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**DataVersion:** The internal version number for this data. This version number is not required to match the version numbers of other objects within the same table or column.

**LastId:** The last data identifier value for this hash dictionary.

**Nullable:** A Boolean value that specifies whether this hash dictionary can contain NULL values.

**Unique:** A Boolean value that specifies whether all the values in this hash dictionary are unique.

#### XMObject class="XMHashDataDictionary&lt;XM_Long&gt;"

When the **class** attribute value for the **XMObject** element is "XMHashDataDictionary&lt;XM_Long&gt;", the **XMObject** element contains metadata for a hash dictionary of **long** values, and the type of the **XMObject** element is **XMObject_HashDictionaryLongType**.

- &lt;xs:complexType name="XMObject_HashDictionaryLongType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="PropertiesHashDictionaryLongType"/>
- &lt;/xs:all&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMHashDataDictionary&lt;XM_Long&gt;"/>
- &lt;xs:attributeGroup ref="HashDictionaryAttributeGroup"/&gt;
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

**HashDictionaryAttributeGroup:** An attribute group that specifies the common attributes for all hash dictionary **XMObject** objects.

##### PropertiesHashDictionaryLongType

The **PropertiesHashDictionaryLongType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMHashDataDictionary&lt;XM_Long&gt;".

- &lt;xs:complexType name="PropertiesHashDictionaryLongType"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="PropertiesHashDictionaryRealType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="OperatingOn32" type="xs:boolean"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**OperatingOn32:** A Boolean value that indicates whether the dictionary encoded values are 32-bit values.

The preceding description documents only the extended element in the **PropertiesHashDictionaryLongType** type. For a description of the elements in the base type, see section [2.5.2.20.2](#Section_4e794ccfb8c94478892f6a1aa2c478e7).

#### XMObject class="XMHashDataDictionary&lt;XM_String&gt;"

When the **class** attribute value for the **XMObject** element is "XMHashDataDictionary&lt;XM_String&gt;", the **XMObject** element contains metadata for a hash dictionary of **string** values, and the type of the **XMObject** element is **XMObject_HashDictionaryStringType**.

- &lt;xs:complexType name="XMObject_HashDictionaryStringType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="PropertiesHashDictionaryStringType"/>
- &lt;/xs:all&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMHashDataDictionary&lt;XM_String&gt;"/>
- &lt;xs:attributeGroup ref="HashDictionaryAttributeGroup"/&gt;
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

**HashDictionaryAttributeGroup:** An attribute group that specifies the common attributes for all hash dictionary **XMObject** objects.

##### PropertiesHashDictionaryStringType

The **PropertiesHashDictionaryStringType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMHashDictionary&lt;XM_String&gt;".

- &lt;xs:complexType name="PropertiesHashDictionaryStringType"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="PropertiesHashDictionaryRealType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="DictionaryFlags"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:long"&gt;
- &lt;xs:minInclusive value="0"/&gt;
- &lt;xs:maxInclusive value="263"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**DictionaryFlags:** A bitmask value in which zero or more of the flags that are described in the following table can be set.

| Flag value | Meaning                |
| ---------- | ---------------------- |
| 0x001      | Lookup is allowed.     |
| 0x002      | Storage is compressed. |
| 0x004      | This value is ignored. |
| 0x100      | Storage is page BLOB.  |

#### XMObject class="XMRENoSplitCompressionInfo&lt;1&gt;"

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;1&gt;", the object is compressed with XMRENoSplitCompression&lt;1&gt; compression (see section [2.7.1.1](#Section_070c724eea2240d5806f67985b385a72)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo1Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo1Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;1&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

**ProviderVersion:** The provider version.

##### XMRENoSplitCompressionInfoPropertiesType

The **XMRENoSplitCompressionInfoPropertiesType** complex type contains the properties for compression with XMRENoSplitCompression or XM123Compression.

- &lt;xs:complexType name="XMRENoSplitCompressionInfoPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="Min" type="xs:int"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**Min:** The minimum value of the input values that are contained in a compression instance.

#### XMObject class="XMRENoSplitCompressionInfo&lt;2&gt;"

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;2&gt;", the object is compressed with XMRENoSplitCompression&lt;2&gt; compression (see section [2.7.1.2](#Section_1412cde4cc994217988b21f9069cb5ae)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo2Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo2Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;2&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

**ProviderVersion:** The provider version.

#### XMObject class="XMRENoSplitCompressionInfo&lt;3&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;3&gt;", the object is compressed with XMRENoSplitCompression&lt;3&gt; compression (see section [2.7.1.3](#Section_79a1adc53ba242d9a0df09c394d0c2df)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo3Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo3Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;3&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;4&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;4&gt;", the object is compressed with XMRENoSplitCompression&lt;4&gt; compression (see section [2.7.1.4](#Section_0e3bb14d9bfa4965b123fbfe3f4b3e3a)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo4Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo4Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;4&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;5&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;5&gt;", the object is compressed with XMRENoSplitCompression&lt;5&gt; compression (see section [2.7.1.5](#Section_8421ca3bef2e4c768e6f70d932fd160c)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo5Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo5Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;5&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;6&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;6&gt;", the object is compressed with XMRENoSplitCompression&lt;6&gt; compression (see section [2.7.1.6](#Section_46414aff998c4136a1b850a4ad0b8bdc)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo6Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo6Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;6&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;7&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;7&gt;", the object is compressed with XMRENoSplitCompression&lt;7&gt; compression (see section [2.7.1.7](#Section_451868968f9a4ff189f928a28f093fed)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo7Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo7Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;7&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;8&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;8&gt;", the object is compressed with XMRENoSplitCompression&lt;8&gt; compression (see section [2.7.1.8](#Section_201455d166524b0b9dcf1648be6fe591)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo8Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo8Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;8&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;9&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;9&gt;", the object is compressed with XMRENoSplitCompression&lt;9&gt; compression (see section [2.7.1.9](#Section_923985e037e648609559eb1a10dd1fe4)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo9Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo9Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;9&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;10&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;10&gt;", the object is compressed with XMRENoSplitCompression&lt;10&gt; compression (see section [2.7.1.10](#Section_48338a27778445b09b54580d8f6f1508)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo10Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo10Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;10&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;12&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;12&gt;", the object is compressed with XMRENoSplitCompression&lt;12&gt; compression (see section [2.7.1.11](#Section_659993c9e44c48e199de5ca5e886c763)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo12Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo12Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;12&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;16&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;16&gt;", the object is compressed with XMRENoSplitCompression&lt;16&gt; compression (see section [2.7.1.12](#Section_49d85ca7b8fb433bb75d829ccc62afa2)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo16Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo16Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;16&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;21&gt;

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;21&gt;", the object is compressed with XMRENoSplitCompression&lt;21&gt; compression (see section [2.7.1.13](#Section_3364f1640b3f452d837af9992d115352)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo21Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo21Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;21&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMRENoSplitCompressionInfo&lt;32&gt;"

When the **class** attribute value for the **XMObject** element is "XMRENoSplitCompressionInfo&lt;32&gt;", the object is compressed with XMRENoSplitCompression&lt;32&gt; compression (see section [2.7.1.14](#Section_e256a49bf1d948e48812a4b33280b43a)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRENoSplitCompressionInfo32Type**.

- &lt;xs:complexType name="XMRENoSplitCompressionInfo32Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class"
- type="XMObjectClassNameEnum"
- fixed="XMRENoSplitCompressionInfo&lt;32&gt;"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XM123CompressionInfo"

When the **class** attribute value for the **XMObject** element is "XM123CompressionInfo", the object is compressed with XM123Compression compression (see section [2.7.2.1](#Section_7c03cad2bf48465f97a81185fda393b8)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XM123CompressionInfoXMObjectType**.

- &lt;xs:complexType name="XM123CompressionInfoXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRENoSplitCompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XM123CompressionInfo"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMRLECompressionInfo

When the **class** attribute value for the **XMObject** element is "XMRLECompressionInfo", the object is compressed with RLE Compression, the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMRLECompressionInfoXMObjectType**.

- &lt;xs:complexType name="XMRLECompressionInfoXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRLECompressionInfoPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMRLECompressionInfo"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMRLECompressionInfoPropertiesType

The **XMRLECompressionInfoPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMRLECompressionInfo".

- &lt;xs:complexType name="XMRLECompressionInfoPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="BookmarkBits" type="xs:long"/&gt;
- &lt;xs:element name="StorageAllocSize" type="xs:long"/&gt;
- &lt;xs:element name="StorageUsedSize" type="xs:long"/&gt;
- &lt;xs:element name="SegmentNeedsResizing" type="xs:boolean"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**BookmarkBits:** The distance between RLE bookmarks. This value is used to perform a left bit shift operation on 1, which yields the number of RLE records that are encoded between bookmarks. For example, if the value is 5, the operation 1 << 5 is performed. The result, 32, would be the number of RLE records between bookmarks.

**StorageAllocSize:** The allocated storage size, in 4-byte units, for the segment.

**StorageUsedSize:** The used storage size, in 4-byte units, for the segment.

**SegmentNeedsResizing:** A Boolean value that specifies whether an operation has occurred that requires the segment to be resized. This value MUST be **false**.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>", the object is compressed with [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480) and uses XMRENoSplitCompression&lt;1&gt; compression (section [2.7.3.2](#Section_1e5fc6ecce42474595ce45234c4fc0d9)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo1Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo1Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMHybridRLECompressionInfoMembersType

The **XMHybridRLECompressionInfoMembersType** complex type holds a collection of **Member** items, each of which contains a property for the parent **XMObject** object.

- &lt;xs:complexType name="XMHybridRLECompressionInfoMembersType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Member" type="XMHybridRLECompressionInfoMemberType"
- minOccurs="2" maxOccurs="2"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Member:** A complex type element that contains a property for the parent **XMObject** element. The value of the **Name** element for the two instances of this element in the **Members** collection MUST have one instance of each enumeration value from the **XMHybridRLECompressionInfoMemberNameEnum** type (section [2.5.2.39.3](#Section_8f98d0c3fa9f43269303e74a67f153b2)).

##### XMHybridRLECompressionInfoMemberType

The **XMHybridRLECompressionInfoMemberType** complex type holds a **Member** item that contains information about a complex property of the parent **XMObject** object.

- &lt;xs:complexType name="XMHybridRLECompressionInfoMemberType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Name"
- type="XMHybridRLECompressionInfoMemberNameEnum"/>
- &lt;xs:element name="XMObject"&gt;
- &lt;xs:complexType&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="XMObjectTypeBase"&gt;
- <xs:attribute name="class"
- type="XMHybridRLECompressionInfoXMObjectMemberClassNameEnum"/>
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;
- &lt;/xs:element&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Name:** The name of the **Member** object.

**XMObject:** A complex type that contains a nested instance of an **XMObject** element. The type of the element is an extension of **XMObjectTypeBase**. However, the actual content allowed in an instance is constrained and depends on the value of the **class** attribute of the **XMObject** element. The content of the **XMObject** element MUST follow the constraints depending on its **class** attribute value.

**class:** An enumeration value that specifies the class name of this **XMObject** element instance. When the **Name** element of the **Member** item has a particular value, the **XMObject** element of the **Member** item is constrained and MUST have a specific value for the **class** attribute. The following table lists the constraints between the values of **Name** and **class**

| Value of Name element | Required value of class attribute                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "RLECompression"      | "XMRLECompressionInfo"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| "SubCompression"      | The **class** attribute of the **XMObject** element MUST be either an instance of the "XM123CompressionInfo" class or an instance of the "XMNoSplitCompressionInfo<_n_\>" class, where _n_ is the same value as that in the class of the [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480). For example, if the containing **XMObject** element is of class "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>", _n_\=7 and the **class** of this **XMObject** element MUST be "XMRENoSplitCompressionInfo&lt;7&gt;", where _n_\=7, as well. |

##### XMHybridRLECompressionInfoMemberNameEnum

The **XMHybridRLECompressionInfoMemberNameEnum** simple type enumerates the allowed values for the name of a **Member** item in the **Members** collection of an **XMObject** object for the [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480) classes.

- &lt;xs:simpleType name="XMHybridRLECompressionInfoMemberNameEnum"&gt;
- &lt;xs:restriction base="xs:string"&gt;
- &lt;xs:enumeration value="RLECompression"/&gt;
- &lt;xs:enumeration value="SubCompression"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMHybridRLECompressionInfoMemberNameEnum** type.

| Enumeration value | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| "RLECompression"  | The **Member** item contains information about RLE compression. |
| "SubCompression"  | The **Member** item contains information about subcompression.  |

##### XMHybridRLECompressionInfoXMObjectMemberClassNameEnum

The **XMHybridRLECompressionInfoXMObjectMemberClassNameEnum** simple type enumerates the allowed values for the class name of the **XMObject** element that is contained in a **Member** item in the **Members** collection of an **XMSimpleTable** object.

- &lt;xs:simpleType name="XMHybridRLECompressionInfoXMObjectMemberClassNameEnum"&gt;
- &lt;xs:restriction base="XMObjectClassNameEnum"&gt;
- &lt;xs:enumeration value="XMRLECompressionInfo"/&gt;
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<1&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<2&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<3&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<4&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<5&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<6&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<7&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<8&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<9&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<10&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<12&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<16&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<21&gt;"/>
- &lt;xs:enumeration value="XMRENoSplitCompressionInfo<32&gt;"/>
- &lt;xs:enumeration value="XM123CompressionInfo"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;

The following table describes the enumeration values in the **XMHybridRLECompressionInfoXMObjectMemberClassNameEnum** type.

| Enumeration value                      | Description                                                                                                                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "RLECompressionInfo"                   | The **XMObject** object contains information about RLE compression.                                                                                                           |
| "XMRENoSplitCompressionInfo&lt;1&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;1&gt; compression. For more information, see section [2.7.1.1](#Section_070c724eea2240d5806f67985b385a72).    |
| "XMRENoSplitCompressionInfo&lt;2&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;2&gt; compression. For more information, see section [2.7.1.2](#Section_1412cde4cc994217988b21f9069cb5ae).    |
| "XMRENoSplitCompressionInfo&lt;3&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;3&gt; compression. For more information, see section [2.7.1.3](#Section_79a1adc53ba242d9a0df09c394d0c2df).    |
| "XMRENoSplitCompressionInfo&lt;4&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;4&gt; compression. For more information, see section [2.7.1.4](#Section_0e3bb14d9bfa4965b123fbfe3f4b3e3a).    |
| "XMRENoSplitCompressionInfo&lt;5&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;5&gt; compression. For more information, see section [2.7.1.5](#Section_8421ca3bef2e4c768e6f70d932fd160c).    |
| "XMRENoSplitCompressionInfo&lt;6&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;6&gt; compression. For more information, see section [2.7.1.6](#Section_46414aff998c4136a1b850a4ad0b8bdc).    |
| "XMRENoSplitCompressionInfo&lt;7&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;7&gt; compression. For more information, see section [2.7.1.7](#Section_451868968f9a4ff189f928a28f093fed).    |
| "XMRENoSplitCompressionInfo&lt;8&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;8&gt; compression. For more information, see section [2.7.1.8](#Section_201455d166524b0b9dcf1648be6fe591).    |
| "XMRENoSplitCompressionInfo&lt;9&gt;"  | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;9&gt; compression. For more information, see section [2.7.1.9](#Section_923985e037e648609559eb1a10dd1fe4).    |
| "XMRENoSplitCompressionInfo&lt;10&gt;" | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;10&gt; compression . For more information, see section [2.7.1.10](#Section_48338a27778445b09b54580d8f6f1508). |
| "XMRENoSplitCompressionInfo&lt;12&gt;" | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;12&gt; compression. For more information, see section [2.7.1.11](#Section_659993c9e44c48e199de5ca5e886c763).  |
| "XMRENoSplitCompressionInfo&lt;16&gt;" | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;16&gt; compression. For more information, see section [2.7.1.12](#Section_49d85ca7b8fb433bb75d829ccc62afa2).  |
| "XMRENoSplitCompressionInfo&lt;21&gt;" | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;21&gt; compression. For more information, see section [2.7.1.13](#Section_3364f1640b3f452d837af9992d115352).  |
| "XMRENoSplitCompressionInfo&lt;32&gt;" | The **XMObject** object describes XMRENoSplitCompressionInfo&lt;32&gt; compression. For more information, see section [2.7.1.14](#Section_e256a49bf1d948e48812a4b33280b43a).  |
| "XM123CompressionInfo"                 | The **XMObject** object describes XM123CompressionInfo compression. For more information, see section [2.7.2](#Section_c6e2e96740c24b7da473c22621f30654).                     |

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>", the object is compressed with [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480) and uses XMRENoSplitCompression&lt;2&gt; compression (see section [2.7.3.3](#Section_1e9a5c2f099944a38e3f0bfa7c8f189c)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo2Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo2Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;3&gt; compression (see section [2.7.3.4](#Section_71c0797f7a9a4b429e3320b793984de9)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo3Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo3Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;4&gt; compression (see section [2.7.3.5](#Section_a75b1cc87a6b4a4389e93d8279736807)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo4Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo4Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;5&gt; compression (see section [2.7.3.6](#Section_6ae5ddada98943a0b0a58fa5dd7689da)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo5Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo5Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;6&gt; compression (see section [2.7.3.7](#Section_51319b44f8984618b99c59bfca08684e)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo6Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo6Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;7&gt; compression (see section [2.7.3.8](#Section_8c3038556487458ebfa0c7acbfd893d1)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo7Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo7Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;8&gt; compression (see section [2.7.3.9](#Section_0ef68fbfb8ca48589aa63252bdb8d241)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo8Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo8Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;9&gt; compression (see section [2.7.3.10](#Section_ca4d75a90ff8452a93261554dc8ff129)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo9Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo9Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;10&gt; compression (see section [2.7.3.11](#Section_01936eeba5b54920b6b8a0e0ac93fad6)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo10Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo10Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;12&gt; compression (see section [2.7.3.12](#Section_da07ed21b1da41819040a90dc952bbf7)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo12Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo12Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;16&gt; compression (see section [2.7.3.13](#Section_a36cac4ae7104fa4bd5793982abe9a79)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo16Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo16Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;21&gt; compression (see section [2.7.3.14](#Section_a57aa02ec18b442ebfa074172e6778f5)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo21Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo21Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>", the object is compressed with hybrid compression and uses XMRENoSplitCompression&lt;32&gt; compression (see section [2.7.3.15](#Section_c4cd2eac036445e5b5e60734496344bc)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfo32Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfo32Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;"

When the **class** attribute value for the **XMObject** element is "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo< XM123CompressionInfo&gt;>", the object is compressed with [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480) and uses XM123 compression (see section [2.7.3.16](#Section_1cf84136dae246ee99de91fb24fbffc4)), the **XMObject** element contains the metadata for the compression, and the type of the **XMObject** element is **XMHybridRLECompressionInfoXM123Type**.

- &lt;xs:complexType name="XMHybridRLECompressionInfoXM123Type"&gt;
- &lt;xs:all&gt;
- <xs:element name="Members"
- type="XMHybridRLECompressionInfoMembersType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed=
- "XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<XM123CompressionInfo&gt;>"/>
- &lt;/xs:complexType&gt;

**Members:** A collection of **Member** items, each of which contains a complex property for the **XMObject** element.

**ProviderVersion:** The provider version.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

#### XMObject class="XMColumnSegmentStats"

When the **class** attribute value for the **XMObject** element is "XMColumnSegmentStats", the **XMObject** element contains statistical information for a column segment, and the type of the **XMObject** element is **XMColumnSegmentStatsXMObjectType**.

- &lt;xs:complexType name="XMColumnSegmentStatsXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMColumnSegmentStatsPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMColumnSegmentStats"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**name:** The name of the **XMColumnSegmentStats** object.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMColumnSegmentStatsPropertiesType

The **XMColumnSegmentStatsPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMColumnSegmentStats".

- &lt;xs:complexType name="XMColumnSegmentStatsPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="DistinctStates" type="xs:long"/&gt;
- &lt;xs:element name="MinDataID" type="xs:int"/&gt;
- &lt;xs:element name="MaxDataID" type="xs:int"/&gt;
- &lt;xs:element name="OriginalMinSegmentDataID" type="xs:int"/&gt;
- &lt;xs:element name="RLESortOrder" type="xs:long"/&gt;
- &lt;xs:element name="RowCount" type="xs:long"/&gt;
- &lt;xs:element name="HasNulls" type="xs:boolean"/&gt;
- &lt;xs:element name="RLERuns" type="xs:long"/&gt;
- &lt;xs:element name="OthersRLERuns" type="xs:long"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**DistinctStates:** The number of distinct values, including NULL, in the column segment.

**MinDataID:** The minimum data identifier for the column segment.

**MaxDataID:** An integer value that specifies the maximum data identifier for the column segment.

**OriginalMinSegmentDataID:** The minimum data identifier for a segment.

**RLESortOrder:** A value that is unused, MUST be-1, and MUST be ignored.

**RowCount:** The count of rows in this segment.

**HasNulls:** A Boolean value that specifies whether the segment has NULL values.

**RLERuns:** The number of RLE runs.

**OthersRLERuns:** The number of RLE runs that are not solid runs. A solid run is a run of consecutive, identical values that can be compressed by RLE techniques.

#### XMObject class="XMRawColumnPartitionDataObject"

When the **class** attribute value for the **XMObject** element is "XMRawColumnPartitionDataObject", the **XMObject** element contains information about the partition for the data object, and the type of the **XMObject** element is **XMRawColumnPartitionDataObjectXMObjectType**.

- &lt;xs:complexType name="XMRawColumnPartitionDataObjectXMObjectType"&gt;
- &lt;xs:all&gt;
- <xs:element name="Properties"
- type="XMRawColumnPartitionDataObjectPropertiesType"/>
- &lt;/xs:all&gt;
- &lt;xs:attribute name="ProviderVersion" type="xs:int"/&gt;
- &lt;xs:attribute name="name" type="xs:string"/&gt;
- <xs:attribute name="class" type="XMObjectClassNameEnum"
- fixed="XMRawColumnPartitionDataObject"/>
- &lt;/xs:complexType&gt;

**Properties:** A collection of properties for the **XMObject** element.

**ProviderVersion:** The provider version.

**name:** The name of the **XMRawColumnPartitionDataObject** object.

**class:** An enumeration value that specifies the class name of this **XMObject** element.

##### XMRawColumnPartitionDataObjectPropertiesType

The **XMRawColumnPartitionDataObjectPropertiesType** complex type contains the specific properties that are allowed when the **XMObject** element is of class "XMRawColumnPartitionDataObject".

- &lt;xs:complexType name="XMRawColumnPartitionDataObjectPropertiesType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="DataVersion" type="xs:int"/&gt;
- &lt;xs:element name="Partition" type="xs:int"/&gt;
- &lt;xs:element name="SegmentCount" type="xs:int"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**DataVersion:** The internal version number for this data. This version number is not required to match the version numbers of other objects within the same table or column.

**Partition:** An incremental number that identifies for the partition.

**SegmentCount:** The count of segments in the partition.

### Contents of the .tbl.xml Files

Each file that contains metadata for a [**table**](#gt_d3a7da8d-a597-4838-9756-25e30b640ba7) (.tbl.xml file) contains an **XMSimpleTable** object. These table metadata files differ according to which columns exist in the **Columns** collection of the **XMSimpleTable** object. The following table specifies which columns exist for each type of table metadata file.

| Type of table metadata file  | Example file name                                              | Columns collection content                                                                                                                              |
| ---------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Column hierarchy file        | H\$Table-Diet\$wt.0.tbl.xml                                    | One column collection item for each of the system-generated [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682) indexes: ID_TO_POS and POS_TO_ID. |
| User hierarchy metadata file | U\$Hierarchy\$1.0.tbl.xml                                      | One column collection item for each of the system-generated user hierarchy columns: CHILD_COUNT, FIRST_CHILD_POS, and MULTI_LEVEL_ID, PARENT_POS.       |
| Table relationship file      | R\$Table-Diet\$ec91bf00-f577-4c86-b7f8-8c5dcd44a2ac.64.tbl.xml | One column collection item for the system-generated relationship file column: INDEX.                                                                    |
| Table metadata file          | Table-Diet.31.tbl.xml                                          | One column collection item for each column in the source data table.                                                                                    |

## Model OLAP Files

The tables contained in one model are represented as an [**OLAP cube**](#gt_11427e13-37ed-49dd-8f0d-5f2b21f7aa4c). The OLAP cube metadata for the model is contained in a set of XML files. These files are derived from metadata complex type definitions, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2](http://msdn.microsoft.com/en-us/library/468209a3-c3db-4e7b-985b-e4396eeb40d3/), and modified as specified in the following subsections.

### Load Element Document Node

Every model [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) file has a **Load** element as the document node of the [**XML document**](#gt_8fa90ece-7a01-4c00-af85-adbf0ed01882). The **Load** element serves as the document node for the remainder of the OLAP object metadata description. The content of the **Load** element is analogous to the content of the **Create** command on the OLAP server, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [3.1.4.3.2.1.1.3](http://msdn.microsoft.com/en-us/library/81281208-2e24-4208-82a6-f43f99879626/).

- &lt;xs:element name="Load" type="LoadElementType"/&gt;
- &lt;xs:complexType name="LoadElementType"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="ParentObject" type="ObjectReferenceTabularModel"/&gt;
- &lt;xs:element name="ObjectDefinition" type="MajorObjectTabularModel"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**ParentObject:** A reference, as specified in section [2.6.1.2](#Section_5fdb47a38c184f9893104fe271b3526b), to the parent of the object that is defined by the **ObjectDefinition** element.

**ObjectDefinition:** A complex type element, as specified in section [2.6.1.1](#Section_41ac82e9c1064c7e91e334043d0d48f0), that contains the definition of an OLAP object.

#### MajorObjectTabularModel

The **MajorObjectTabularModel** complex type defines an [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) major object. This type is analogous to the **MajorObject** type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.1](http://msdn.microsoft.com/en-us/library/b38dcecd-e3a9-4c61-bd35-a7a426ca794e/), but contains fewer objects that are available to be defined within the **xs:choice** element. Additionally, the types of the elements extend the types as specified in \[MS-SSAS\] to add elements for tabular models.

- &lt;xs:complexType name="MajorObjectTabularModel"&gt;
- &lt;xs:choice&gt;
- &lt;xs:element name="Cube" type="CubeTabularModel"/&gt;
- &lt;xs:element name="Database" type="DatabaseTabularModel"/&gt;
- &lt;xs:element name="DataSource" type="DataSourceTabularModel"/&gt;
- &lt;xs:element name="DataSourceView" type="DataSourceViewTabularModel"/&gt;
- &lt;xs:element name="Dimension" type="DimensionTabularModel"/&gt;
- &lt;xs:element name="MdxScript" type="MdxScriptTabularModel"/&gt;
- &lt;xs:element name="MeasureGroup" type="MeasureGroupTabularModel"/&gt;
- &lt;xs:element name="Partition" type="PartitionTabularModel"/&gt;
- &lt;/xs:choice&gt;
- &lt;/xs:complexType&gt;

**Cube:** An element of type **CubeTabularModel** (section [2.6.5](#Section_6123c4c160fd4d7683a46467421fede2)), which is an extension of the **Cube** type (\[MS-SSAS\] section [2.2.4.2.2.9](http://msdn.microsoft.com/en-us/library/d40a289e-e3a8-488b-b0ce-bd388acf1807/)).

**Database:** An element of type **DatabaseTabularModel** (section [2.6.4](#Section_220cbde1c685486ba1df07ff4be6965d)), which is an extension of the **Database** type (\[MS-SSAS\] section [2.2.4.2.2.5](http://msdn.microsoft.com/en-us/library/f0a45420-af97-44e1-8744-1621e69c0bf2/)).

**DataSource:** An element of type **DataSourceTabularModel** (section [2.6.2](#Section_536cdc3781f54984b17359fc6ef64247)), which is an extension of the **DataSource** type (\[MS-SSAS\] section [2.2.4.2.2.6](http://msdn.microsoft.com/en-us/library/3923a7c5-6a41-444a-ac09-a04db51cd739/)).

**DataSourceView:** An element of type **DataSourceViewTabularModel** (section [2.6.3](#Section_77f559d9ed7d467fb1f620aea4410502)), which is an extension of the **DataSourceView** type (\[MS-SSAS\] section [2.2.4.2.2.7](http://msdn.microsoft.com/en-us/library/31069e1b-d650-4664-b987-908589f2e7f3/)).

**Dimension:** An element of type **DimensionTabularModel** (section [2.6.6](#Section_f7381e33c04e409996d45966dbd38b42)), which is an extension of the **Dimension** type (\[MS-SSAS\] section [2.2.4.2.2.8](http://msdn.microsoft.com/en-us/library/ed122253-df54-42a8-8905-0faa6e696b8b/)).

**MdxScript:** An element of type **MdxScriptTabularModel** (section [2.6.9](#Section_37b7ea6d12f749ed91978daf494edba2)), which is an extension of the **MdxScript** type (\[MS-SSAS\] section [2.2.4.2.2.10](http://msdn.microsoft.com/en-us/library/95331319-30d5-4c54-8e22-94fa4de40235/)).

**MeasureGroup:** An element of type **MeasureGroupTabularModel** (section [2.6.7](#Section_0861668595e448eea31c733d6b94773f)), which is an extension of the **MeasureGroup** type (\[MS-SSAS\] section [2.2.4.2.2.11](http://msdn.microsoft.com/en-us/library/da8a6ff0-01ea-491e-9041-c2d97f28544e/)).

**Partition:** An element of type **PartitionTabularModel** (section [2.6.8](#Section_e7167bbc07cb453bb06072b04b75ac69)), which is an extension of the **Partition** type (\[MS-SSAS\] section [2.2.4.2.2.13](http://msdn.microsoft.com/en-us/library/551f8a8a-1837-4575-a6ae-498a0423d2a0/)).

#### ObjectReferenceTabularModel

The **ObjectReferenceTabularModel** complex type specifies the parent object of the object that is being described. This type is a subset of the **ObjectReference** type as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [3.1.4.3.2.1.1.1](http://msdn.microsoft.com/en-us/library/26834101-a86b-4365-8e58-d6e4a6ad377d/).

- &lt;xs:complexType name="ObjectReferenceTabularModel"&gt;
- &lt;xs:all&gt;
- &lt;xs:element name="DatabaseID" type="xs:string" minOccurs="0"/&gt;
- &lt;xs:element name="CubeID" type="xs:string" minOccurs="0"/&gt;
- &lt;/xs:all&gt;
- &lt;/xs:complexType&gt;

**DatabaseID:** An element as specified in \[MS-SSAS\] section 3.1.4.3.2.1.1.1.

**CubeID:** An element as specified in \[MS-SSAS\] section 3.1.4.3.2.1.1.1.

#### TabularModelElementsGroup Group

The **TabularModelElementsGroup** group contains a group of elements that have been added to many of the [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) major object types, for the case of the tabular model.

- &lt;xs:group name="TabularModelElementsGroup"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="Ordinal" type="xs:int"/&gt;
- &lt;xs:element name="ObjectVersion" type="xs:int"/&gt;
- &lt;xs:element name="PersistLocation" type="xs:int"/&gt;
- &lt;xs:element name="System" type="xs:boolean"/&gt;
- &lt;xs:element name="DataFileList" type="xs:string"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:group&gt;

**Ordinal:** The position of this object within the collection of objects of this type.

**ObjectVersion:** The version number that will appear within the file name. For example, if the value is "10" for a dimension object, the file name will end in "10.dim.xml".

**PersistLocation:** The version number that will appear within the folder name. For example, if the value is "10" for a database object, the folder name will end in "10.db".

**System:** A Boolean value that MUST be set to **false**.

**DataFileList:** A semicolon-separated list of all the data files materialized for this object.

### DataSourceTabularModel

The **DataSourceTabularModel** complex type is extended from the **DataSource** base type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.6](http://msdn.microsoft.com/en-us/library/3923a7c5-6a41-444a-ac09-a04db51cd739/). The **DataSource** base type is an abstract type and has two types derived from it, both of which can be used in the [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) definition. They are the **OlapDataSource** type, as specified in \[MS-SSAS\] section [2.2.4.2.2.6.2](http://msdn.microsoft.com/en-us/library/93ff17f0-0025-42b9-b13b-735e184a6e48/), and the **RelationalDataSource** type, as specified in \[MS-SSAS\] section [2.2.4.2.2.6.1](http://msdn.microsoft.com/en-us/library/07dd3084-094f-463e-ab85-8134b148d3a2/).

The data source definition is contained in a data source definition XML file. An example of a generated data source definition XML file name is PushedDataSource-F052E9FD-98DA-441C-A0C0-B84DA82E5F25.0.ds.xml.

Every tabular model MUST have a data source defined.

- &lt;xs:complexType name="DataSourceTabularModel"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="DataSource"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:group ref="TabularModelElementsGroup"/&gt;
- &lt;xs:element name="PermissionFileList" type="xs:string"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**TabularModelElementsGroup:** A group of elements that is added to base [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) types for the tabular model derivations from those types. For more details, see section [2.6.1.3](#Section_df4fd6854a684db3a0ffc4bddfd14409).

**PermissionFileList:** A semicolon-separated list of the files included in the tabular model metadata that define user permissions for the data source.

### DataSourceViewTabularModel

The **DataSourceViewTabularModel** complex type is extended from the **DataSourceView** base type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.7](http://msdn.microsoft.com/en-us/library/31069e1b-d650-4664-b987-908589f2e7f3/).

The [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) view definition is contained in a data source view definition XML file. An example of a generated data source view definition XML file name is Sandbox.0.dsv.xml.

Every tabular model MUST have a data source view defined.

- &lt;xs:complexType name="DataSourceViewTabularModel"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="DataSourceView"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:group ref="TabularModelElementsGroup"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**TabularModelElementsGroup:** A group of elements that is added to base [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) types for the tabular model derivations from those types. For more details, see section [2.6.1.3](#Section_df4fd6854a684db3a0ffc4bddfd14409).

### DatabaseTabularModel

The **DatabaseTabularModel** complex type is extended from the **Database** base type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.5](http://msdn.microsoft.com/en-us/library/f0a45420-af97-44e1-8744-1621e69c0bf2/).

The database definition is contained in a database definition XML file. An example of a generated database definition XML file name is ImportDiet2.0.db.xml.

Every tabular model MUST have a database defined.

- &lt;xs:complexType name="DatabaseTabularModel"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="Database"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="DefaultCollationVersion" minOccurs="0" maxOccurs="1"&gt;
- &lt;xs:simpleType&gt;
- &lt;xs:restriction base="xs:string"&gt;
- &lt;xs:enumeration value="Earliest"/&gt;
- &lt;xs:enumeration value="80"/&gt;
- &lt;xs:enumeration value="90"/&gt;
- &lt;xs:enumeration value="100"/&gt;
- &lt;/xs:restriction&gt;
- &lt;/xs:simpleType&gt;
- &lt;/xs:element&gt;
- &lt;xs:group ref="TabularModelElementsGroup"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**DefaultCollationVersion:** An enumerated type that indicates what collation version MUST be used for string comparisons in the tabular model. The default value for this element if omitted is "Earliest", which indicates that the earliest collation version that supports an object's locale identifier MUST be used. Values "80", "90", and "100" indicate that the newest collation version (not to exceed version 8.0, 9.0, and 10.0, respectively) that supports an object's locale MUST be used.

**TabularModelElementsGroup:** A group of elements that is added to base [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) types for the tabular model derivations from those types. For more details, see section [2.6.1.3](#Section_df4fd6854a684db3a0ffc4bddfd14409).

### CubeTabularModel

The **CubeTabularModel** complex type is extended from the **Cube** base type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.9](http://msdn.microsoft.com/en-us/library/d40a289e-e3a8-488b-b0ce-bd388acf1807/).

The [**OLAP cube**](#gt_11427e13-37ed-49dd-8f0d-5f2b21f7aa4c) definition is contained in a cube definition XML file. An example of a generated cube definition XML file name is Model.33.cub.xml.

Every tabular model MUST have a cube defined.

When the cube is defined for a tabular model, the following rules MUST be followed:

- Each table that is included in the tabular model MUST be defined in the cube's **Dimensions** collection as a **Dimension** of type **CubeDimension**, as specified in \[MS-SSAS\] section [2.2.4.2.2.9.1](http://msdn.microsoft.com/en-us/library/7b4ec273-230d-4558-801f-3e7dff015ddc/).
- Each column in each table MUST be defined in the cube's **Attributes** collection as an **Attribute** of type **CubeAttribute**, as specified in \[MS-SSAS\] section [2.2.4.2.2.9.2](http://msdn.microsoft.com/en-us/library/021d907e-256d-4341-a10b-e13bf9af2523/).

- &lt;xs:complexType name="CubeTabularModel"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="Cube"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:group ref="TabularModelElementsGroup"/&gt;
- &lt;xs:element name="PermissionFileList" type="xs:string"/&gt;
- &lt;xs:element name="MeasureGroupFileList" type="xs:string"/&gt;
- &lt;xs:element name="PerspectiveFileList" type="xs:string"/&gt;
- &lt;xs:element name="AssemblyFileList" type="xs:string"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**TabularModelElementsGroup:** A group of elements that is added to base [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) types for the tabular model derivations from those types. For more details, see section [2.6.1.3](#Section_df4fd6854a684db3a0ffc4bddfd14409).

**PermissionFileList:** A semicolon-separated list of the files included in the tabular model metadata that define user permissions for the model.

**MeasureGroupFileList:** A semicolon-separated list of the files included in the tabular model metadata that define the [**measure groups**](#gt_1f51f60a-8a0f-4b0d-9e7e-80cbd596e164) for the model.

**PerspectiveFileList:** A semicolon-separated list of the files included in the tabular model metadata that define perspectives for the model.

**AssemblyFileList:** A semicolon-separated list of the files included in the tabular model metadata that define [**assemblies**](#gt_7d79c711-c9ae-4cd0-929d-96b521f69b67) for the model.

### DimensionTabularModel

The **DimensionTabularModel** type is extended from the **Dimension** base type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.8](http://msdn.microsoft.com/en-us/library/ed122253-df54-42a8-8905-0faa6e696b8b/).

The dimension definition is contained in a dimension definition XML file. An example of a generated dimension definition XML file name is Table-Diet.64.dim.xml.

Every tabular model MUST have a dimension defined.

A dimension MUST be defined for every table that is included in the tabular model.

The dimension MUST follow the following rules:

- An **Attribute** element of type **DimensionAttribute**, as specified in \[MS-SSAS\] section [2.2.4.2.2.8.1](http://msdn.microsoft.com/en-us/library/2865fe4f-5fbb-4ae6-b0cf-811b32b4a139/), MUST be defined for every column in the table.
- If the dimension represents a table that is a primary table in a table relationship, a **Relationships** collection of type **Relationships**, as specified in \[MS-SSAS\] section 2.2.4.2.2.8, MUST contain a **Relationship** element of type **Relationship**, as specified in \[MS-SSAS\] section [2.2.4.2.2.8.3](http://msdn.microsoft.com/en-us/library/ece33c56-d84f-4b74-beaa-36dd3912e6d8/), for each relationship defined in the tabular model.

- &lt;xs:complexType name="DimensionTabularModel"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="Dimension"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:group ref="TabularModelElementsGroup"/&gt;
- &lt;xs:element name="PermissionFileList" type="xs:string"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**TabularModelElementsGroup:** A group of elements that is added to base [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) types for the tabular model derivations from those types. For more details, see section [2.6.1.3](#Section_df4fd6854a684db3a0ffc4bddfd14409).

**PermissionFileList:** A semicolon-separated list of the files included in the tabular model metadata that define user permissions for the dimension.

### MeasureGroupTabularModel

The **MeasureGroupTabularModel** type is from the **MeasureGroup** base type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.11](http://msdn.microsoft.com/en-us/library/da8a6ff0-01ea-491e-9041-c2d97f28544e/).

The [**measure group**](#gt_1f51f60a-8a0f-4b0d-9e7e-80cbd596e164) definition is contained in a measure group definition XML file. An example of a generated measure group definition XML file name is Table-Diet.64.det.xml.

Every tabular model MUST have at least one measure group defined.

A measure group MUST be defined for every table in the tabular model.

Measure group definitions MUST follow the following rules:

- The measure group MUST contain a **Dimension** element of type **DegenerateMeasureGroupDimension**, as specified in \[MS-SSAS\] section [2.2.4.2.2.11.1.4](http://msdn.microsoft.com/en-us/library/93b29d4b-6d1f-4b14-b3b5-3ca3265068a7/).
- **DegenerateMeasureGroupDimension** MUST have an **Attribute** element of type **MeasureGroupDimensionAttribute**, as specified in \[MS-SSAS\] section [2.2.4.2.2.11.2](http://msdn.microsoft.com/en-us/library/193874f8-ee13-456f-8bed-08e1d7647fe4/), defined for every column in the table.
- If the table is a primary table in a table relationship, the measure group MUST have a **Dimension** element of type **ReferenceMeasureGroupDimension**, as specified in \[MS-SSAS\] section [2.2.4.2.2.11.1.3](http://msdn.microsoft.com/en-us/library/8c14f34b-7c02-4ad8-8e1e-723ee00c6f99/).
- **ReferenceMeasureGroupDimension** MUST have an **Attribute** element of type **MeasureGroupDimensionAttribute**, as specified in \[MS-SSAS\] section 2.2.4.2.2.11.2, defined for every column in the related table.

- &lt;xs:complexType name="MeasureGroupTabularModel"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="MeasureGroup"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:group ref="TabularModelElementsGroup"/&gt;
- &lt;xs:element name="AggregationDesignFileList" type="xs:string"/&gt;
- &lt;xs:element name="PartitionFileList" type="xs:string"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**TabularModelElementsGroup:** A group of elements that is added to base [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) types for the tabular model derivations from those types. For more details, see section [2.6.1.3](#Section_df4fd6854a684db3a0ffc4bddfd14409).

**AggregationDesignFileList:** A semicolon-separated list of the files included in the tabular model metadata that define **AggregationDesign** objects for the model, as specified in \[MS-SSAS\] section [2.2.4.2.2.12](http://msdn.microsoft.com/en-us/library/e4ea0908-ae0a-4592-8a5e-ea2f7873d9fe/).

**PartitionFileList:** A semicolon-separated list of the files included in the tabular model metadata that define [**partitions**](#gt_2f24f458-7d39-47a2-93f7-de433ea85c75) for the model.

### PartitionTabularModel

The **PartitionTabularModel** type is extended from the **Partition** base type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.13](http://msdn.microsoft.com/en-us/library/551f8a8a-1837-4575-a6ae-498a0423d2a0/).

The [**partition**](#gt_2f24f458-7d39-47a2-93f7-de433ea85c75) definition is contained in a partition definition XML file. An example of a generated partition definition XML file name is Table-LatLong.1.prt.xml.

Every tabular model MUST have at least one partition defined.

A partition MUST be defined for every table in the tabular model.

- &lt;xs:complexType name="PartitionTabularModel"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="Partition"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:group ref="TabularModelElementsGroup"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**TabularModelElementsGroup:** A group of elements that is added to base [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) types for the tabular model derivations from those types. For more details, see section [2.6.1.3](#Section_df4fd6854a684db3a0ffc4bddfd14409).

### MdxScriptTabularModel

The **MdxScriptTabularModel** complex type extends the **MdxScript** base type, as specified in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.10](http://msdn.microsoft.com/en-us/library/95331319-30d5-4c54-8e22-94fa4de40235/).

The [**Multidimensional Expressions (MDX)**](#gt_9b631ff5-dc89-45f0-a1c2-db6981e4804f) script definition is contained in an MDX script definition XML file. An example of a generated MDX script definition XML file name is MdxScript.0.scr.xml.

Every tabular model MUST have an MDX script defined.

Every MDX script MUST contain a command that defines at least one measure. The measure MAY[&lt;12&gt;](#Appendix_A_12) be defined with the following command:

- &lt;Command&gt;
- &lt;Text&gt;
- CALCULATE;
- CREATE MEMBER CURRENTCUBE.Measures.\[\_\_Count of Models\] AS 1;
- ALTER CUBE CURRENTCUBE UPDATE DIMENSION Measures,
- Default_Member = \[\_\_Count of Models\];
- &lt;/Text&gt;
- &lt;/Command&gt;

The **MdxScriptTabularModel** complex type is defined as follows:

- &lt;xs:complexType name="MdxScriptTabularModel"&gt;
- &lt;xs:complexContent&gt;
- &lt;xs:extension base="MdxScript"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:group ref="TabularModelElementsGroup"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:extension&gt;
- &lt;/xs:complexContent&gt;
- &lt;/xs:complexType&gt;

**TabularModelElementsGroup:** A group of elements that is added to base [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) types for the tabular model derivations from those types. For more details, see section [2.6.1.3](#Section_df4fd6854a684db3a0ffc4bddfd14409).

### OLAP Information Files

In addition to the standard [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) metadata information that is contained in the **Dimension** object (see section [2.6.6](#Section_f7381e33c04e409996d45966dbd38b42)), the **Partition** object (see section [2.6.8](#Section_e7167bbc07cb453bb06072b04b75ac69)), and the **Cube** object (see section [2.6.5](#Section_6123c4c160fd4d7683a46467421fede2)), an information file is generated that contains additional metadata information for those objects.

#### Partition Information File

The additional metadata information for the **Partition** object is contained in a partition information XML file. An example of a generated partition information XML file name is Info.33.xml.

The document node in the partition information file contains a **Partition** element.

- &lt;xs:element name="Partition" type="PartitionInformationType"/&gt;

**Partition:** A complex type element that specifies additional metadata information for the partition.

##### PartitionInformationType

The **PartitionInformationType** complex type holds additional metadata information about the partition, beyond the metadata information that is contained in the [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) **Partition** object (section [2.6.8](#Section_e7167bbc07cb453bb06072b04b75ac69)).

- &lt;xs:complexType name="PartitionInformationType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="DataVersion" type="xs:int"/&gt;
- &lt;xs:element name="RigidAggVersion" type="xs:int"/&gt;
- &lt;xs:element name="FlexAggVersion" type="xs:int"/&gt;
- &lt;xs:element name="DataIndexVersion" type="xs:int"/&gt;
- &lt;xs:element name="RigidIndexVersion" type="xs:int"/&gt;
- &lt;xs:element name="FlexIndexVersion" type="xs:int"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**DataVersion:** The internal version number for this object. This version number is not required to match the version numbers of other objects within the same table or column.

**RigidAggVersion:** A value that is unused and MUST be ignored.

**FlexAggVersion:** A value that is unused and MUST be ignored.

**DataIndexVersion:** A value that is unused and MUST be ignored.

**RigidIndexVersion:** A value that is unused and MUST be ignored.

**FlexIndexVersion:** A value that is unused and MUST be ignored.

#### Dimension Information File

The additional metadata information for the **Dimension** object is contained in a dimension information XML file. An example of a generated Dimension information XML file name is Info.33.xml.

The document node in the dimension information file contains a **Dimension** element.

- &lt;xs:element name="Dimension" type="DimensionInformationType"/&gt;

**Dimension:** A complex type element that specifies additional metadata information for the dimension.

##### DimensionInformationType

The **DimensionInformationType** complex type holds additional metadata information about the dimension, beyond the metadata information contained in the [**OLAP**](#gt_055c223a-52f1-4d41-b95b-d7c60eaa388f) **Dimension** object (section [2.6.6](#Section_f7381e33c04e409996d45966dbd38b42)).

- &lt;xs:complexType name="DimensionInformationType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="DataVersion" type="xs:int"/&gt;
- &lt;xs:element name="IndexVersion" type="xs:int"/&gt;
- &lt;xs:element name="DecodeStoreVersion" type="xs:int"/&gt;
- &lt;xs:element name="LevelStoreVersion" type="xs:int"/&gt;
- <xs:element name="Properties"
- type="DimensionInformationPropertiesType"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**DataVersion:** The internal version number for this object. This version number is not required to match the version numbers of other objects within the same table or column.

**IndexVersion:** A value that is unused and MUST be ignored.

**DecodeStoreVersion:** A value that is unused and MUST be ignored.

**LevelStoreVersion:** A value that is unused and MUST be ignored.

**Properties:** A complex type element that specifies additional properties for the dimension.

###### DimensionInformationPropertiesType

The **DimensionInformationPropertiesType** complex type holds a collection of properties for the dimension.

- &lt;xs:complexType name="DimensionInformationPropertiesType"&gt;
- &lt;xs:sequence&gt;
- <xs:element name="Property" type="DimensionInformationPropertyType"
- maxOccurs="unbounded"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**Property:** A complex type that specifies a single property in the properties collection for dimension information.

DimensionInformationPropertyType

The **DimensionInformationPropertyType** complex type specifies the information for one property instance for the dimension information object.

- &lt;xs:complexType name="DimensionInformationPropertyType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="ParentChild" type="xs:boolean"/&gt;
- &lt;xs:element name="Depth" type="xs:int"/&gt;
- &lt;xs:element name="Balanced" type="xs:boolean"/&gt;
- &lt;xs:element name="HasHoles" type="xs:boolean"/&gt;
- <xs:element name="MapDataset"
- type="DimensionInformationPropertyMapDatasetType"/>
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**ParentChild:** A value that is unused and MUST be ignored.

**Depth:** A value that is unused and MUST be ignored.

**Balanced:** A value that is unused and MUST be ignored.

**HasHoles:** A value that is unused and MUST be ignored.

**MapDataset:** A complex type that specifies additional mapping information for dimension information properties.

DimensionInformationMapDataSetType

The **DimensionInformationMapDatasetType** specifies the property information for a dataset map.

- &lt;xs:complexType name="DimensionInformationPropertyMapDatasetType"&gt;
- &lt;xs:sequence&gt;
- &lt;xs:element name="m_cbOffsetHeader" type="xs:long"/&gt;
- &lt;xs:element name="m_cbOffsetData" type="xs:long"/&gt;
- &lt;xs:element name="m_cRecord" type="xs:long"/&gt;
- &lt;xs:element name="m_cSegment" type="xs:long"/&gt;
- &lt;xs:element name="m_mskFormat" type="xs:long"/&gt;
- &lt;xs:element name="m_cbHeader" type="xs:long"/&gt;
- &lt;xs:element name="m_cPath" type="xs:long"/&gt;
- &lt;xs:element name="m_cData" type="xs:long"/&gt;
- &lt;xs:element name="m_cSegmentIndex" type="xs:long"/&gt;
- &lt;xs:element name="MapDataIndices" type="xs:long"/&gt;
- &lt;xs:element name="MinMaxValues" type="xs:long"/&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**m_cbOffsetHeader:** A value that is unused and MUST be ignored.

**m_cbOffsetData:** A value that is unused and MUST be ignored.

**m_cRecord:** A value that is unused and MUST be ignored.

**m_cSegment:** A value that is unused and MUST be ignored.

**m_mskFormat:** A value that is unused and MUST be ignored.

**m_cbHeader:** A value that is unused and MUST be ignored.

**m_cPath:** A value that is unused and MUST be ignored.

**m_cData:** A value that is unused and MUST be ignored.

**m_cSegmentIndex:** A value that is unused and MUST be ignored.

**MapDataIndices:** A value that is unused and MUST be ignored.

**MinMaxValues:** A value that is unused and MUST be ignored.

#### Cube Information File

The additional metadata information for the **Cube** object is contained in a cube information XML file. An example of a generated cube information XML file name is Info.21.xml.

The document node in the cube information file contains a **Cube** element.

- &lt;xs:element name="Cube" type="CubeInformationType"/&gt;

**Cube:** A complex type element that specifies additional metadata information for the cube.

##### CubeInformationType

The **CubeInformationType** complex type is empty.

- &lt;xs:complexType name="CubeInformationType"&gt;
- &lt;xs:sequence&gt;
- &lt;/xs:sequence&gt;
- &lt;/xs:complexType&gt;

**CubeInformationType** contains no elements.

## Compression

All data structures except for XML files are compressed. The compression algorithms are described in the following subsections. If the decompression algorithm is not simply a reversal of the compression algorithm, the decompression algorithm is also explained.

### XMRENoSplit Compression Algorithms

XMRENoSplit compression algorithms use range encoding, in which the algorithms use a minimum offset plus only the necessary number of bits to encode the entire range of data values, after the range's reduction by that minimum offset. This procedure reduces the numeric size of the values to be stored and, therefore, the number of bits that are required to hold each value. After this range reduction, a form of bit packing compression is used for which the data to be stored is compacted into a specified number of bits.

The storage area for the compressed value MUST be zeroed out prior to compressing the value and storing it in that area.

#### XMRENoSplitCompressionInfo&lt;1&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;1&gt;**, as specified in section [2.5.2.23](#Section_8915846a179944acb91a8c6e70fe5822).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.23). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 1.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage (_compressedStorage_) is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 1) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((1) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 63, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 63))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**values (8 bytes):** The set of values, each occupying 1 bit, in sequence and ordered low to high. In the sequence, the first value occupies Bit 0, the second value occupies Bit 1, and so on.

The _startBit_ offset followed the sequence of Bit 0, 1, 2, and so on, up to Bit 63 as the data was compressed into the 64-bit storage area. Any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 64 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

#### XMRENoSplitCompressionInfo&lt;2&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;2&gt;**, as specified in section [2.5.2.24](#Section_19583b63de2d440ca5ec9a51737a0690).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.24). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 2.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 2) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((2) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 62, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 62))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**values (8 bytes):** The set of values, each occupying 2 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 1, the second value occupies Bits 2 through 3, and so on.

The _startBit_ offset followed the sequence of Bit 0, 2, 4, and so on, up to Bit 62 as the data was compressed into the 64-bit storage area. Any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 32 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

#### XMRENoSplitCompressionInfo&lt;3&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;3&gt;**, as specified in section [2.5.2.25](#Section_db46c507836f4bd395d3b85c5fea7a77).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.25). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 3.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 3) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((3) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 61, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 61))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            | A   |

**values (63 bits):**The set of values, each occupying 3 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 2, the second value occupies Bits 3 through 5, and so on.

The _startBit_ offset followed the sequence of Bit 0, 3, 6, and so on, up to Bit 60 as the data was compressed into the 64-bit storage area. In addition to the end bit (Bit 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 21 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (1 bit):** The padding.

#### XMRENoSplitCompressionInfo&lt;4&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;4&gt;**, as specified in section [2.5.2.26](#Section_7facaeb4384d40c98b05da5cea8eacc2).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.26). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 4.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 4) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((4) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 60, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 60))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**values (8 bytes):** The set of values, each occupying 4 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 3, the second value occupies Bits 4 through 7, and so on.

The _startBit_ offset followed the sequence of Bit 0, 4, 8, and so on, up to Bit 60 as the data was compressed into the 64-bit storage area. Any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 16 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

#### XMRENoSplitCompressionInfo&lt;5&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;5&gt;**, as specified in section [2.5.2.27](#Section_37e159dec2ae42b9bf383a6631d61c69).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.27). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 5.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 5) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((5) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 59, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 59))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     | A   |     |            |     |

**values (60 bits):** The set of values, each occupying 5 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 4, the second value occupies Bits 5 through 9, and so on.

The _startBit_ offset followed the sequence of Bit 0, 5, 10, and so on, up to Bit 55 as the data was compressed into the 64-bit storage area. In addition to the end bits (Bit 60 through 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 12 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value

**A (4 bits):** The padding.

#### XMRENoSplitCompressionInfo&lt;6&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;6&gt;**, as specified in section [2.5.2.28](#Section_631633ad470e429980001f16c7d5530b).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.28). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 6.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 6) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((6) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 58, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 58))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     | A   |     |            |     |

**values (60 bits):** The set of values, each occupying 6 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 5, the second value occupies Bits 6 through 11, and so on.

The _startBit_ offset followed the sequence of Bit 0, 6, 12, and so on, up to Bit 54 as the data was compressed into the 64-bit storage area. In addition to the end bits (Bit 60 through 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 10 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value

**A (4 bits):** The padding.

#### XMRENoSplitCompressionInfo&lt;7&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;7&gt;**, as specified in section [2.5.2.29](#Section_e64c903737964d308485a8e7f31a22f4).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.29). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 7.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 7) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((7) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 57, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 57))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            | A   |

**values (63 bits):**The set of values, each occupying 7 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 6, the second value occupies Bits 7 through 13, and so on.

The _startBit_ offset followed the sequence of Bit 0, 7, 14, and so on, up to Bit 56 as the data was compressed into the 64-bit storage area. In addition to the end bit (Bit 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most nine values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (1 bit):** The padding.

#### XMRENoSplitCompressionInfo&lt;8&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;8&gt;**, as specified in section [2.5.2.30](#Section_fad47f9d18dd424583118352ceae7f76).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

The minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.30). The result of this subtraction (_idVal_ - _Min_) is then copied into the storage at that particular bit offset. The offset is a multiple of 8.

The following pseudocode illustrates this process:

- SET compressedStorage at offset = (idVal - Min) WHERE offset is multiple of 8

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompressing values from this method consists of a simple reversal of the compression process.

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**values (8 bytes):** The set of values, each occupying 1 byte, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 7, the second value occupies Bits 8 through 15, and so on.

The _startBit_ offset followed the sequence of Bit 0, 8, 16, and so on, up to Bit 56 as the data was compressed into the 64-bit storage area. For this compression algorithm, at most eight values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

No padding exists in the compressed storage area because the number of necessary bits is a multiple of 8. However, if the entire storage area is not used, the remaining storage area is set to zero. For example, if only three values are placed into the compressed storage area, all the remaining bits, from Bit 24 through 63, will be zero.

#### XMRENoSplitCompressionInfo&lt;9&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;9&gt;**, as specified in section [2.5.2.31](#Section_f667356d1a5441efbd165e7b2936d184).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.31). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 9.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 9) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((9) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 55, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 55))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            | A   |

**values (63 bits):**The set of values, each occupying 9 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 8, the second value occupies Bits 9 through 17, and so on.

The _startBit_ offset followed the sequence of Bit 0, 3, 6, and so on, up to Bit 54 as the data was compressed into the 64-bit storage area. In addition to the end bit (Bit 63), any unused bits, are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most seven values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (1 bit):** The padding.

#### XMRENoSplitCompressionInfo&lt;10&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;10&gt;**, as specified in section [2.5.2.32](#Section_97ab5cd0a82d4ebfb1b812badb9e1c61).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.32). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 10.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 10) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((10) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 54, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 54))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     | A   |     |            |     |

**values (60 bits):** The set of values, each occupying 10 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 9, the second value occupies Bits 10 through 19, and so on.

The _startBit_ offset followed the sequence of Bit 0, 10, 20, and so on, up to Bit 50 as the data was compressed into the 64-bit storage area. In addition to the end bits (Bit 60 through 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most six values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value

**A (4 bits):** The padding.

#### XMRENoSplitCompressionInfo&lt;12&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;12&gt;**, as specified in section [2.5.2.33](#Section_ef23ae4fa34f44dba0a5dd8ac07a1b1e).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.33). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 12.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 12) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((12) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 52, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 52))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     | A   |     |            |     |

**values (60 bits):** The set of values, each occupying 12 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 11, the second value occupies Bits 12 through 23, and so on.

The _startBit_ offset followed the sequence of Bit 0, 12, 24, and so on, up to Bit 48 as the data was compressed into the 64-bit storage area. In addition to the end bits (Bit 60 through 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most five values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value

**A (4 bits):** The padding.

#### XMRENoSplitCompressionInfo&lt;16&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;16&gt;**, as specified in section [2.5.2.34](#Section_0ec82b97025140389905bdc5fcc15d9a).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

The minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.34). The result of this subtraction (_idVal_ - _Min_) is then copied into the storage at that particular bit offset. The offset is a multiple of 16.

The following pseudocode illustrates this process:

- SET compressedStorage at offset = (idVal - Min) WHERE offset is multiple of 16

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompressing values from this method consists of a simple reversal of the compression process.

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6      | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| value1 |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     | value2 |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| value3 |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     | value4 |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**value1 (2 bytes):** The first value in the sequence.

**value2 (2 bytes):** The second value in the sequence.

**value3 (2 bytes):** The third value in the sequence.

**value4 (2 bytes):** The fourth value in the sequence.

In the sequence, **value1** occupies Bits 0 through 15, **value2** occupies Bits 16 through 31, and so on. The _startBit_ offset followed the sequence of Bit 0, 8, 16, and so on, up to Bit 56 as the data was compressed into the 64-bit storage area. For this compression algorithm, at most four values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value. No padding exists in the compressed storage area because the number of necessary bits is a multiple of 16. However, if the entire storage area is not used, the remaining storage area is set to zero. For example, if only three values are placed into the compressed storage area, all the remaining bits, from Bit 48 through 63, will be zero.

#### XMRENoSplitCompressionInfo&lt;21&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;21&gt;**, as specified in section [2.5.2.35](#Section_4c183738a8544e0ca6a7c67f09a88099).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into three phases

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.35). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 21.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the compressed storage, _compressedStorage_, is combined through a bitwise AND operation with a masking value, resulting in a masked off _compressedStorage_ that is named _maskedStorage_. The masking value, named _maskArrayValue_, is found in the masking array named _maskArray_, as specified in section [5](#Section_e0eb73abda1143608e01c0b407999ed3). The index into this array to obtain the correct masking value is calculated in the following manner: the bit count (in this case, 21) is multiplied by the storage data size (64 bits), and then a bitwise OR operation is performed on the multiplication result and the current offset into the storage area (_startBit_).

The following pseudocode illustrates this phase:

- SET maskArrayValue = maskArray at index \[((21) MULTIPLY (64)) BITWISE_OR (startBit)\]
- SET maskedStorage = (compressedStorage) BITWISE_AND (maskArrayValue)

In Phase 3, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the masked and compressed storage (_maskedStorage_). This operation generates the final result, named _maskedStorageWithValue_.

The following pseudocode illustrates this phase:

- SET maskedStorageWithValue = (maskedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompression does not require the use of the mask. One way to decompress a value that has been compressed with this compression method is to right bit shift the masked storage containing the value by the current offset into the storage, perform a bitwise AND operation on the result of the value 0xFFFFFFFFFFFFFFFF right bit shifted by 43, and then add _Min_.

Using the same definitions as earlier, the following pseudocode illustrates one way to decompress and retrieve the original compressed value from the storage:

- SET idVal = Min + ((maskedStorageWithValue RIGHT_BITSHIFT startBit) BITWISE_AND (0xFFFFFFFFFFFFFFFF RIGHT_BITSHIFT 43))

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1      | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| value1 |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            | value2 |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     | value3     |     |     |     |     |     |     |     |     |     |            |        |     |     |     |     |     |     |     |     |            | A   |

**value1 (21 bits):** The first value in the sequence.

**value2 (21 bits):** The second value in the sequence.

**value3 (21 bits):** The third value in the sequence.

In the sequence, **value1** occupies Bits 0 through 20, **value2** occupies Bits 21 through 41, and so on. The _startBit_ offset followed the sequence of Bit 0, 21, and 42 as the data was compressed into the 64-bit storage area. For this compression algorithm, at most three values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value. In addition to the end bit (Bit 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects.

**A (1 bit):** The padding.

#### XMRENoSplitCompressionInfo&lt;32&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMRENoSplitCompressionInfo&lt;32&gt;**, as specified in section [2.5.2.36](#Section_68f2ad18e7e94952a9b47488df2db064).

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

The minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.36). The result of this subtraction (_idVal_ - _Min_) is then copied into the storage at the particular bit offset. The offset is a multiple of 32.

The following pseudocode illustrates this process:

- SET compressedStorage at offset = (idVal - Min) WHERE offset is multiple of 32

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

Decompressing values from this method consists of a simple reversal of the compression process.

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| value1 |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| value2 |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**value1 (4 bytes):** The first value in the sequence.

**value2 (4 bytes):** The second value in the sequence.

In the sequence, **value1** occupies Bits 0 through 31, and **value2** occupies Bits 32 through 63. The _startBit_ offset followed the sequence of Bit 0 and then Bit 32 as the data was compressed into the 64-bit storage area. For this compression algorithm, at most two values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value. No padding exists in the compressed storage area because the number of necessary bits is a multiple of 32. However, if the entire storage area is not used, the remaining storage area is set to zero. For example, if only one value is placed into the compressed storage area, all the remaining bits, from Bit 32 through Bit 63, will be zero.

### XM123 Compression Algorithm

XM123 compression is used only in the special situation where the internally generated **RowNumber** column (section [2.3.4](#Section_7d9074aabea740e2b5d822e9cadeb778)) is serialized to disk. This column follows the same file format as any column data storage file (section [2.3.1](#Section_4d3887f864c84dbd9a02e4e95e64bfed)).

The storage area for the compressed value MUST be zeroed out prior to compressing the value and storing it in that area.

#### XM123CompressionInfo

This compression is never used standalone, even though it could be referenced in the XML metadata in what might appear at first look to be a standalone manner within the XML metadata, see section [2.5.2.37](#Section_217a770d8a494ea28f855de96a2a408c). It is always used as part of an XMHybridRLE compression and only for a particular special case. Please see section [2.7.3.16](#Section_1cf84136dae246ee99de91fb24fbffc4).

### XMHybridRLE Compression Algorithms

XMHybridRLE compression algorithms use two forms of compression in combination: run length encoding (RLE) and bit packing. As a result, these compression algorithms use two segments to represent all the values. The segments are referred to here as the _RLE segment_, or _primary segment_, and the _subsegment_, or _bit-packing subsegment_. The RLE segment contains a possible mix of RLE entries and bit-packing entries, the latter of which refer to bit-packed values that follow in the subsegment.

The first type of compression that is used in this [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480) is RLE. RLE is used only on appropriate data items-those that repeat often enough to make RLE an efficient compression choice. In RLE compression, two 4-byte values are used that together comprise the first type of entry in the RLE segment-the RLE entry. The first value of the RLE entry is the data value. The second value is the repeat count, which is the number of times that the data value repeats in a continuous sequence. The repeat count MUST be equal to or greater than 64. For an RLE run to be generated by the system, at least 64 consecutive items (that is, 64 identical records) MUST exist in that run of data. Otherwise, the individual items will be bit packed by using the chosen bit-packing algorithm in the related subsegment.

The second type of entry in the RLE segment is the bit-packing entry. The bit-packing entry also contains two 4-byte values. The first value is a negated 1-based offset into the subsegment data, and the second value is the count of the number of values that follow in the subsegment. The offset value is represented as the negative of itself to clearly distinguish it from the RLE entries. The bit-packed values exist in a separate bit-packing subsegment that follows the RLE segment.

The first bit-packing entry uses -1 as the first value (to indicate that it is the first data value in the subsegment) and then has the count of bit-packing items as the second value. Any subsequent bit-packing entries also have a negative offset value as the first value. This negative offset value is calculated by taking the previous negative bit-packing entry offset value, and subtracting from it the bit-packing entry count of that same entry.

Any number of RLE entries and bit-packing entries can exist in the RLE segment, and in any order. It is also possible for the RLE segment to have no RLE entries or no bit-packing entries in the RLE segment. In very rare cases, it is possible for both the segment and subsegment to be empty. For more information about segment minimum and maximum row sizes, see section [2.3.1.1.3](#Section_66a47541c99e4140b937ceb44385af39).

The bit-packed compression values follow the RLE segment. The bit-packed values are in the same order that they are referred to here but within their own, bit-packed subsegment. All the bit-packed values that are referenced (as bit-packing entries) within the RLE segment use the same type of bit-packing compression because only one type of bit-packing compression is allowed per segment. In other words, after the RLE segment, the bit-packing subsegment that is associated with the RLE segment uses a single bit-packing algorithm, such as that for **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>** in which each bit-packed entry is compressed by using 3 bits. For more information about the column data storage file format, see section [2.3.1](#Section_4d3887f864c84dbd9a02e4e95e64bfed).

For a diagrammed example of RLE entries mixed with bit-packing entries, see section [2.7.3.1](#Section_ef29562d2334472d8228aca5cbf7d0dc).

After the end of all the data entries (both the RLE entries and the bit-packing entries) in the RLE segment, any remaining storage area allocated for the RLE segment is zeroed out. The size of this padding depends on the amount of storage allocated and the amount used. These amounts can be found in the metadata information for this compression (see section [2.5.2.38.1](#Section_f61c9c7b0b2845ffb8291fddb840a6b1)).

Following the end of this segment (including any padding at the end of the segment), the next segment begins. This segment is called the _subsegment of the XMHybridRLE compression_ and contains the selected bit-packing compression sequence. For more information about the column data storage file format, which is the file format that uses this hybrid compression dual segment layout, see section 2.3.1.

The second part of the hybrid compression, the subsegment, involves using a bit-packing compression algorithm. This part is used for data items that are not suitable for RLE compression, and it uses a form of range encoding bit-packing compression in which the data to be stored (after that data has been offset by a minimum value) is compacted into a specified number of bits. The bit size that is chosen determines the bit-packing algorithm that is used to compress the data. The values that are bit packed in this segment conform to the sequence that is specified in the RLE segment.

Despite any name similarity, the range encoding bit-packing algorithm that is used in the hybrid compression is not necessarily the same as the range encoding bit-packing algorithm that is used in the nonhybrid case.

The storage area for the compressed value, whether RLE or bit packed, MUST be zeroed out prior to compressing the value and storing it in that area.

#### Conceptual Overview of RLE Entries and Bit-Packing Entries

The following bit diagram shows a sequence of RLE entries and bit-packing entries as described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). This conceptual overview is long to clearly show the pattern of negative offset values used in the bit-packing entries. The sequence includes several RLE entries and an occasional bit-packing entry.

As mentioned in section 2.7.3, any mix of RLE entries and bit-packing entries can exist. So in this conceptual overview, the number of RLE entries and the number of bit-packing entries is arbitrary. The count of values that is shown in each bit-packing entry can also be larger or smaller than that shown in this example. The count of values that is shown for an RLE entry MUST be greater than or equal to the required minimum of 64.

| 0                        | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| RLE_Entry_value          |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_repeat_count   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_value          |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_repeat_count   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_value          |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_repeat_count   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Bit_Packing_Entry_offset |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Bit_Packing_Entry_count  |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_value          |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_repeat_count   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_value          |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_repeat_count   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Bit_Packing_Entry_offset |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Bit_Packing_Entry_count  |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_value          |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_repeat_count   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Bit_Packing_Entry_offset |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Bit_Packing_Entry_count  |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_value          |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_repeat_count   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_value          |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| RLE_Entry_repeat_count   |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Bit_Packing_Entry_offset |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| Bit_Packing_Entry_count  |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| padding (variable)       |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...                      |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**RLE_Entry_value (4 bytes):** A value compressed with RLE.

**RLE_Entry_repeat_count (4 bytes):** The number of times that the preceding value appears sequentially in this RLE run.

**RLE_Entry_value (4 bytes):** A value compressed with RLE.

**RLE_Entry_repeat_count (4 bytes):** The number of times that the preceding value appears sequentially in this RLE run.

**RLE_Entry_value (4 bytes):** A value compressed with RLE.

**RLE_Entry_repeat_count (4 bytes):** The number of times that the preceding value appears sequentially in this RLE run.

**Bit_Packing_Entry_offset (4 bytes):** The offset into the subsegment. This offset is -1. Note that the first offset equals the first data value in the subsegment.

**Bit_Packing_Entry_count (4 bytes):** The number of values that will be using the subsegment bit-packing algorithm. This count is 5.

**RLE_Entry_value (4 bytes):** A value compressed with RLE.

**RLE_Entry_repeat_count (4 bytes):** The number of times that the preceding value appears sequentially in this RLE run.

**RLE_Entry_value (4 bytes):** A value compressed with RLE.

**RLE_Entry_repeat_count (4 bytes):** The number of times that the preceding value appears sequentially in this RLE run.

**Bit_Packing_Entry_offset (4 bytes):** The offset into the subsegment. This offset is -6. Note that -6 = -1 - 5 (the values from the previous bit-packing entry).

**Bit_Packing_Entry_count (4 bytes):** The number of values that will be using the subsegment bit-packing algorithm. This count is 20.

**RLE_Entry_value (4 bytes):** A value compressed with RLE.

**RLE_Entry_repeat_count (4 bytes):** The number of times that the preceding value appears sequentially in this RLE run.

**Bit_Packing_Entry_offset (4 bytes):** The offset into the subsegment. This offset is -26. Note that -26 = -6 - 20 (the values from the previous bit-packing entry).

**Bit_Packing_Entry_count (4 bytes):** The number of values that will be using the subsegment bit-packing algorithm. This count is 10.

**RLE_Entry_value (4 bytes):** A value compressed with RLE.

**RLE_Entry_repeat_count (4 bytes):** The number of times that the preceding value appears sequentially in this RLE run.

**RLE_Entry_value (4 bytes):** A value compressed with RLE.

**RLE_Entry_repeat_count (4 bytes):** The number of times that the preceding value appears sequentially in this RLE run.

**Bit_Packing_Entry_offset (4 bytes):** The offset into the subsegment. This offset is -36. Note that -36 = -26 - 10 (the values from the previous bit-packing entry).

**Bit_Packing_Entry_count (4 bytes):** The number of values that will be using the subsegment bit-packing algorithm. This count is 2.

**padding (variable):** The padding, which is unused but MUST be filled with zeros. The size, in bytes, is a multiple of 4.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<1&gt;>**, as specified in section [2.5.2.39](#Section_214821211ee4455799f1efea1f4c655a). The RLE portion of this compression follows the format that is described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit packing sub-segment portion of the compression is as follows.

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into two phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.39). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 1.

The following pseudocode illustrates this phase:

SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.1](#Section_070c724eea2240d5806f67985b385a72).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**values (8 bytes):** The set of values, each occupying 1 bit, in sequence and ordered low to high. In the sequence, the first value occupies Bit 0, the second value occupies Bit 1, and so on.

The _startBit_ offset followed the sequence of Bit 0, 1, 2, and so on, up to Bit 63 as the data was compressed into the 64-bit storage area. Any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 64 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>**, as specified in section [2.5.2.40](#Section_f8e597f78fef43d3a77c4faafe404c8c). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into two phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.40). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 2.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.2](#Section_1412cde4cc994217988b21f9069cb5ae).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**values (8 bytes):** The set of values, each occupying 2 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 1, the second value occupies Bits 2 through 3, and so on.

The _startBit_ offset followed the sequence of Bit 0, 2, 4, and so on, up to Bit 62 as the data was compressed into the 64-bit storage area. Any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 32 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>**, as specified in section [2.5.2.41](#Section_ea7f23f4b54d49c5b229aea6d986a8c9). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into two phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.41). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 3.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

- SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.3](#Section_79a1adc53ba242d9a0df09c394d0c2df).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            | A   |

**values (63 bits):**The set of values, each occupying 3 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 2, the second value occupies Bits 3 through 5, and so on.

The _startBit_ offset followed the sequence of Bit 0, 3, 6, and so on, up to Bit 60 as the data was compressed into the 64-bit storage area. In addition to the end bit (Bit 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 21 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (1 bit):** The padding.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<4&gt;>**, as specified in section [2.5.2.42](#Section_71b820a7468c4a1da1530977ac7e248c). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

If each value to be compressed is named _idVal,_ for example, then each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

The process described above is divided into two phases:

- In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ is specified in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.42). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 4.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit
- In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

- SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.4](#Section_0e3bb14d9bfa4965b123fbfe3f4b3e3a).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |

**values (8 bytes):** The set of values, each occupying 4 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 3, the second value occupies Bits 4 through 7, and so on.

The _startBit_ offset followed the sequence of Bit 0, 4, 8, and so on, up to Bit 60 as the data was compressed into the 64-bit storage area. Any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 16 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<5&gt;>**, as specified in section [2.5.2.43](#Section_fa666497636b4a539bae660244c80fed). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

If each value to be compressed is named _idVal,_ for example, then each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

The process described above is divided into two phases:

- In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.43). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 5.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit
- In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

- SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.5](#Section_8421ca3bef2e4c768e6f70d932fd160c).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     | A   |     |            |     |

**values (60 bits):**The set of values, each occupying 5 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 4, the second value occupies Bits 5 through 9, and so on.

The _startBit_ offset followed the sequence of Bit 0, 5, 10, and so on, up to Bit 55 as the data was compressed into the 64-bit storage area. In addition to the end bits (Bits 60 through 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 12 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (4 bits):** The padding.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<6&gt;>**, as specified in section [2.5.2.44](#Section_c2d4327cdade4e2b986775f1a84b70c0). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

If each value to be compressed is named _idVal,_ for example, then each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

The process described above is divided into two phases:

- In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.44). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 6.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit
- In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

- SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.6](#Section_46414aff998c4136a1b850a4ad0b8bdc).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     | A   |     |            |     |

**values (60 bits):**The set of values, each occupying 6 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 5, the second value occupies Bits 6 through 11, and so on.

The _startBit_ offset followed the sequence of Bit 0, 6, 12, and so on, up to Bit 54 as the data was compressed into the 64-bit storage area. In addition to the end bits (Bits 60 through 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 10 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (4 bits):** The padding.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<7&gt;>**, as specified in section [2.5.2.45](#Section_3a8f9bda9f4d47b2a70cd7f781cdb393). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

If each value to be compressed is named _idVal,_ for example, then each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

The process described above is divided into two phases:

- In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.45). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 7.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit
- In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

- SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.7](#Section_451868968f9a4ff189f928a28f093fed).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            | A   |

**values (63 bits):**The set of values, each occupying 7 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 6, the second value occupies Bits 7 through 13, and so on.

The _startBit_ offset followed the sequence of Bit 0, 7, 14, and so on, up to Bit 56 as the data was compressed into the 64-bit storage area. In addition to the end bit (Bit 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 9 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (1 bit):** The padding.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<8&gt;>**, as specified in section [2.5.2.46](#Section_7052afbc1ff04b77a6d70c47ae7367cc). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is identical to the 8-bit compression format that is used in XMRENoSplit compression, as specified in section [2.7.1.8](#Section_201455d166524b0b9dcf1648be6fe591). For metadata information, see section 2.5.2.46.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<9&gt;>**, as specified in section [2.5.2.47](#Section_29a3351e1eb94ea18bc4d0da9f20b75f). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into two phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.47). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 9.

The following pseudocode illustrates this phase:

SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.9](#Section_923985e037e648609559eb1a10dd1fe4).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            | A   |

**values (63 bits):**The set of values, each occupying 9 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 8, the second value occupies Bits 9 through 17, and so on.

The _startBit_ offset followed the sequence of Bit 0, 9, 18, and so on, up to Bit 54 as the data was compressed into the 64-bit storage area. In addition to the end bit (Bit 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 7 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (1 bit):** The padding.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<10&gt;>**, as specified in section [2.5.2.48](#Section_16b7a68bd17b49a4b2a5acfc280557e6). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into two phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.48). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 10.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

- SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.10](#Section_48338a27778445b09b54580d8f6f1508).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     | A   |     |            |     |

**values (60 bits):**The set of values, each occupying 10 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 9, the second value occupies Bits 10 through 19, and so on.

The _startBit_ offset followed the sequence of Bit 0, 10, 20, and so on, up to Bit 50 as the data was compressed into the 64-bit storage area. In addition to the end bits (Bits 60 through 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 6 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (4 bits):** The padding.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<12&gt;>**, as specified in section [2.5.2.49](#Section_2b04179711c14ec0a734bb9d5a9bdbea). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into two phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.49). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 12.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

- SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.11](#Section_659993c9e44c48e199de5ca5e886c763).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| values |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     | A   |     |            |     |

**values (60 bits):**The set of values, each occupying 12 bits, in sequence and ordered low to high. In the sequence, the first value occupies Bits 0 through 11, the second value occupies Bits 12 through 23, and so on.

The _startBit_ offset followed the sequence of Bit 0, 12, 24, and so on, up to Bit 48 as the data was compressed into the 64-bit storage area. In addition to the end bits (Bits 60 through 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most 5 values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (4 bits):** The padding.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<16&gt;>**, as specified in section [2.5.2.50](#Section_0a06d2377ccc4fb7a251ef012c8e4b37). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is identical to the 16-bit compression format that is used in XMRENoSplit compression, as specified in section [2.7.1.12](#Section_49d85ca7b8fb433bb75d829ccc62afa2). For metadata information, see section 2.5.2.50.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<21&gt;>**, as specified in section [2.5.2.51](#Section_d46f5a1d9a954ff4bd7d4be295187031). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is as follows.

Assume that each value to be compressed is named _idVal_. Each _idVal_ value will be compressed into the compressed storage in the following manner: The maximum size of the value to be compressed MUST NOT exceed 32 bits. Assume that the resulting compressed storage area data value is named _compressedStorage_. The entire compressed storage area is a multiple of 64 bits, so each _compressedStorage_ data value (the section of storage that is being written to) is 64 bits in size. For more details about the actual values that are compressed by using this type of compression, see section [2.3](#Section_0cfe0bea60cb43eb9af3a3ff62610c61) and section [2.4](#Section_a713d4decb324086a8b62c5bbd3ae6ea).

To simply this explanation, the process is divided into two phases.

In Phase 1, the minimum value (_Min_) is subtracted from the value to be compressed. The value of _Min_ can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.51). The result of this subtraction (_idVal_ - _Min_) is then left bit shifted by the current bit offset into the storage. Assume that this offset is named _startBit_, and the resulting value after the bit shifting and subtraction is named _shiftedVal_. The offset (_startBit_) is a multiple of 21.

The following pseudocode illustrates this phase:

- SET shiftedVal = (idVal - Min) LEFT_BITSHIFT startBit

In Phase 2, the data value is placed into the compressed storage. A bitwise OR operation is performed on the value (_shiftedVal_) and the compressed storage (_compressedStorage_). This operation generates the final result, named _storageWithValue_.

The following pseudocode illustrates this phase:

- SET storageWithValue = (compressedStorage) BITWISE_OR (shiftedVal)

Within the value, the order of the value's bits is [**little-endian**](#gt_079478cb-f4c5-4ce5-b72b-2144da5d2ce7). Within the compressed storage, however, individual values are placed low to high, with the first value occupying the lowest bits, the second value occupying the next-lowest bits, and so on. All the file formats use little-endian values. It is only the way individual values are ordered within the file that is being emphasized here, because that specific ordering is required.

The same decompression method that is used in XMRENoSplit compression can be used here. For more information, see section [2.7.1.13](#Section_3364f1640b3f452d837af9992d115352).

The following diagram shows the compressed data values.

| 0      | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 1<br><br>0 | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 2<br><br>0 | 1      | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 3<br><br>0 | 1   |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
| value1 |     |     |     |     |     |     |     |     |     |            |     |     |     |     |     |     |     |     |     |            | value2 |     |     |     |     |     |     |     |     |            |     |
| ...    |     |     |     |     |     |     |     |     |     | value3     |     |     |     |     |     |     |     |     |     |            |        |     |     |     |     |     |     |     |     |            | A   |

**value1 (21 bits):** The first value in the sequence.

**value2 (21 bits):** The second value in the sequence.

**value3 (21 bits):** The third value in the sequence.

In the sequence, **value1** occupies Bits 0 through 20, **value2** occupies Bits 21 through 41, and so on. The _startBit_ offset followed the sequence of Bit 0, 21, and 42 as the data was compressed into the 64-bit storage area. In addition to the end bit (Bit 63), any unused bits are thus only padding, and the value of the padding depends on the result of the various masking effects. For this compression algorithm, at most three values exist in the 64-bit compressed storage value, and the process will begin again at Offset 0 with the next _compressedStorage_ value.

**A (1 bit):** The padding.

#### XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<32&gt;>**, as specified in section [2.5.2.52](#Section_c6e88e40fc3042bc9a915953a96cd48c). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). The bit-packing subsegment portion of the compression is identical to the 32-bit compression format that is used in XMRENoSplit compression, as specified in section [2.7.1.14](#Section_e256a49bf1d948e48812a4b33280b43a). For metadata information, see section 2.5.2.52.

#### XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;

This section specifies the compression algorithm that is used when the compression metadata specifies the compression to be of type **XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;**, as specified in section [2.5.2.53](#Section_0f0a9a78f2384a329d243c76fd651d3c). The RLE portion of this compression follows the format described in section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b). However, only the bit-packing entry is used in the RLE portion, except that in this case, the value that is associated with the bit-packing entry (which typically contains the subsegment offset and the count of items that will follow in the bit-packing compression subsegment) is used differently here. The offset is set to -1, as expected for the first bit-packing entry; however, the count now represents the number of rows that exist in the segment. The rest of the RLE segment is unused and padded with zeros. The bit-packing subsegment portion of the compression is as follows.

Nothing is stored by using bit packing in this situation, except for 8 bytes that are set to zero to indicate that the subsegment itself, which contains the bit-packing compression, is zero bytes in size. For more information about the file format layout, including how the sizes of different sections of the file are indicated, see section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e).

The minimum value (_Min_) is not used in the actual compression. It is used when recreating the correct offset value for the row number. The _Min_ value can be found in the XML metadata file that is associated with the data file containing the compressed data (see section 2.5.2.53). The _Min_ value that is stored in the XML metadata is actually an offset. Together, the number of rows for the segment and the _Min_ value for the segment allow the creation of the correct overall row number for the entire column, which could be composed of multiple segments. The _Min_ value is a 32-bit value.

The reason is that this compression is used for the internally created **RowNumber** column (section [2.3.4](#Section_7d9074aabea740e2b5d822e9cadeb778)), and that column is zero indexed through the total number of rows in the column.

For example, the first _Min_ value that is stored, for the first segment, is zero. Therefore, the range of rows for that segment is from _Min_ through _Min_ plus the total number of rows for that segment minus one. The minus one is because of zero indexing. For a total of five rows in the first segment, the indexing ranges from _Min_ through _Min_ + 4, where the offset is zero. For the next segment, the offset is the next index beyond the last value in the previous segment. Again, if five rows exist in the next segment, the index will range from _Min_ + 5 through _Min_ + 9, where the offset (the value that is stored) is 5. Moving from one segment to the next, the row numbers thus continue sequentially without any breaks.

For this compression, the maximum that can be indexed is 2 billion (hexadecimal 0x77359400). This number includes the _Min_ value. In other words, the _Min_ value plus the last row number is, at most, 2 billion.

### Huffman Compression

Huffman compression is the only type of compression that is used when strings are stored and compressed in a dictionary file. String data is not stored in the column data storage files but in a dictionary file-specifically, in an **XM_TYPE_STRING** dictionary file. (For more information about **XM_TYPE_STRING** dictionaries, see section [2.3.2.1.2](#Section_c1ebc0f5ccb14d14a6b59276aed28872). For more information about the per-page string store information in particular, see section [2.3.2.1.2.4](#Section_a1df1ca8e942405f87f0959bdf047139).) The strings might be compressed. BLOBs are also stored in **XM_TYPE_STRING** dictionaries after they have been encoded by means of [**base64 encoding**](#gt_179b9392-9019-45a3-880b-26f6890522b7). Therefore, stored BLOBs are treated as single [**character set**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204) strings and can be successfully compressed by using Huffman compression, as well.

If any of the strings are compressed, the compression used is always classic Huffman encoding. Although Huffman encoding has many forms, the Huffman tree and algorithm-especially of classic Huffman encoding-is well known and will not be discussed in detail here.

In short, in Huffman encoding, the algorithm determines the probability that a particular symbol from the assigned Huffman alphabet will be encountered in the stream of symbols being encoded. Using this statistical knowledge of the frequencies of different symbols in the alphabet being used, a binary tree of 2 × _N_ - 1 nodes can be constructed, where _N_ represents the number of symbols used in the text being encoded. (Note that _N_ can be the size of the Huffman alphabet or less than the size of the Huffman alphabet being used.) Symbols that have the greatest frequency of occurrence in the text to be encoded are assigned higher positions in the binary tree than symbols that have a lower frequency of occurrence. The binary tree that is constructed does not need to be a balanced binary tree.

#### Huffman Implementation Constraints

In the implementation of Huffman encoding that is used here, further constraints and guidelines exist and are explained in the following subsections.

##### Classical Unbalanced Huffman Tree

As stated in section [2.7.4](#Section_f70b41f2ca6444a19e6f53e63f6a5ee9), in this implementation, Huffman tree creation employs a traditional, classical approach that uses the frequency of occurrence of a symbol in the text to be encoded to build the binary tree [**hierarchy**](#gt_a07fc05d-cdb0-442c-984a-dd3589b9f682). Additionally, this method does not require that the tree be balanced.

Therefore, encodings MUST follow a classic Huffman approach, but the tree that is generated does not need to be a balanced tree.

##### Minimum and Maximum Codeword Sizes

This implementation of Huffman encoding does not support the encoding of symbols that are either zero bits or 1 bit in length, but it does limit the maximum size of codewords. Therefore, it is important that for this Huffman implementation, codeword lengths be limited to a range that has a minimum and a maximum value.

The length of each codeword MUST be greater than or equal to 2 bits and less than or equal to 15 bits.

However, the decode bits value (**uiDecodeBits**) that is specified in the dictionary file MUST NOT exceed 12-even when more than 12 bits are used for codewords-otherwise, an error will occur. (For more information about **uiDecodeBits**, see section [2.3.2.1.2.4.2](#Section_64985b36dd1b44c48e241e7d00d8eb3f).)

The system creates lookup tables that handle codewords of a size only up to 12 bits. Any codewords that are longer than 12 bits in length require traditional Huffman tree traversal techniques for decoding. Therefore, when setting the decode bits value (**uiDecodeBits**) in the **XM_TYPE_STRING** hash data dictionary file (section [2.3.2.1.2](#Section_c1ebc0f5ccb14d14a6b59276aed28872)), consider the following guidelines for deciding what value to set as the **uiDecodeBits** size.

First, if the longest codeword is 8 bits or less, it is suggested that **uiDecodeBits** be set to that longest codeword value.

Second, if the longest codeword is greater than 12 bits, it is suggested that **uiDecodeBits** be set to 12. Setting **uiDecodeBits** to any value greater than 12 will result in an error.

Third, if the longest codeword is greater than or equal to 9 but less than 12 bits, it is suggested that **uiDecodeBits** be set to the codeword size that includes 99 percent of all the compressed bits in the encoded text (meaning the encoded text for that Huffman encoding on that dictionary page).

The total number of compressed bits can be determined by summing over all codewords and using the value equal to the frequency of each codeword multiplied by the number of bits in that codeword, as shown in the following pseudocode:

- FOR all Codewords
- SET totalCompressedBits = totalCompressedBits + (codewordFrequency MULTIPLY numberOfBitsInCodeword )
- END FOR

The smallest codeword bit size that corresponds to 99 percent coverage is the value to use for **uiDecodeBits** to help ensure that almost all of the bits are found via the fast lookup tables and that only a few, infrequently used bytes are left out of the table.

##### Huffman Alphabet Size

The Huffman alphabet size that is used in this implementation is limited to 256 symbols or less and is byte oriented. This means that this Huffman encoding algorithm encodes bytes rather than actual characters. The algorithm has no real knowledge of the languages being used.

Some languages-those that fit into 128-bit [**character sets**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204), such as [**ASCII**](#gt_79fa85ca-ac61-467c-b819-e97dc1a7a599)-have a one-to-one relationship between a character and an encoded byte. Other languages require multiple bytes to encode a character. In both cases, the characters are simply encoded byte by byte in the Huffman tree without regard to how any of these single or multiple bytes relate to each other. In other words, the Huffman implementation has no knowledge of the meaning of the individual bytes and simply encodes each byte according to its frequency of occurrence in the string byte stream.

The encoded Huffman alphabet array that is contained within the dictionary page for those compressed strings reflects the byte's numeric value. This numeric value is used as the index into the array, and the content of the array index item is the codeword size that is used for that index (byte) value. A byte value is 8 bits and can therefore be represented as a numeric value from 0 through 255. If the codeword size that is used is zero, the meaning is that the index (byte) value was not used in the tree.

The actual frequencies used to generate the Huffman tree (and therefore the resulting codeword assignments) are not persisted to the dictionary file. Even so, the encoded array of bytes and their corresponding codeword sizes, and the knowledge that the minimum codeword size is required to be 2 bits, can be used to reconstruct the original, classic Huffman tree.

It is critical that the encoded Huffman alphabet array be correct and adhere to the criteria detailed here for this Huffman implementation. The array MUST encode the codeword lengths for each used alphabet character (byte value) as well as set unused elements to zero. Those codeword lengths MUST be from 2 through 15 bits, and the classic Huffman tree approach MUST be used when deciding symbol-to-codeword assignment. For an example of a Huffman tree implementation that uses these criteria, see section [2.7.4.2](#Section_2a1f1eeb14cc4ce9917962bce6b7eeee).

##### Single and Multiple Character Set Modes

This Huffman encoding implementation supports both single [**character set**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204) encoding and multiple character set encoding. For single character set encoding, where the entire text that is encoded uses one character set, the upper byte is not encoded but is instead stored separately. For more information about setting single versus multiple character set mode, see section [2.3.2.1.2.4.2](#Section_64985b36dd1b44c48e241e7d00d8eb3f). During the decoding process, this character set value MUST be added back to each decoded symbol to recreate a valid character in the byte stream.

By contrast, in multiple character set encoding, where the text to be encoded contains two or more character sets that are intermixed in some way, both the upper and the lower byte MUST be encoded during Huffman encoding, but the decoding process does not require any character set byte to be added back to the stream. Therefore, encoding and decoding processes need to take these differences into account when deconstructing and reconstructing the characters.

A multiple byte character set does not necessarily use only the multiple character set mode. A multiple byte character set can use a single character set mode. It depends on whether the specified bytes (the first byte, the third, the fifth, and so on) in the byte stream are the same.

For example, in the [**Unicode**](#gt_c305d0ab-8b94-461a-bd76-13b40cb8c4d8) version of [**ASCII**](#gt_79fa85ca-ac61-467c-b819-e97dc1a7a599), the first byte is the same as the third byte, which is the same as the fifth, and so on. This is because those bytes represent the character set and are each the upper byte of a 2-byte character. A single character set mode works fine in this situation. Those bytes, each alternating with the byte that actually contains the character code, can safely be pulled out of the byte stream and added back to each character byte later, during the decoding process.

However, if the character set uses multiple bytes per character, not counting the byte that designates the character set (the language), the first byte might not be the same as the third byte or the fifth byte. In such a case, using a multiple character set mode helps to ensure that each byte is encoded in the stream and that none are removed.

Even so, it still depends on the individual characters within that language. It is possible that the strings being compressed, even though they are multiple-byte characters, still have duplicate alternative bytes in the byte stream, mimicking a single byte character set. This can happen if only a few strings with only a few characters are being encoded. In this case, the single character set mode can be used and will not cause any data corruption or loss.

##### Huffman Information Provided in an XM_TYPE_STRING Dictionary

The **XM_TYPE_STRING** hash data dictionary file format (section [2.3.2.1.2](#Section_c1ebc0f5ccb14d14a6b59276aed28872)) supports having multiple pages, either compressed or uncompressed. Each compressed page contains its own Huffman alphabet encoding array with the codeword sizes of the symbols, the [**character set**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204) mode, the character set value (in the case of single character set mode), the size of the longest codeword used for the internally generated lookup table, and the actual encoded bit stream for that page's strings. For more information about compressed pages, see section [2.3.2.1.2.4.2](#Section_64985b36dd1b44c48e241e7d00d8eb3f). A discussion about how these items are used follows.

As already mentioned, the **XM_TYPE_STRING** dictionary file contains the information that is needed to decode the Huffman encoded strings for that page of that dictionary. This includes the decode bits value (**uiDecodeBits**), which represents a maximum codeword length that is used in the faster, internally generated lookup table. It does not mean that only codewords up to that maximum length were used in the Huffman tree. For example, if **uiDecodeBits** is 4, that does not mean that only codewords of a size up to 4 (that is, 2, 3, and 4) exist, but that typically no codewords are generated that are more than 4 bits in length. (For more information about **uiDecodeBits**, see section 2.3.2.1.2.4.2.)

For **uiDecodeBits** values less than or equal to 8, typically only codewords of that length or less were used, but for values greater than 8, the chances of having codewords greater than the **uiDecodeBits** value are more likely to occur. Codewords can actually go up to 15 bits in length. For more information, see section [2.7.4.1.2](#Section_690e69ab8041455fbbcc2f9cb6ebc839).

The dictionary also includes the encoded Huffman alphabet used. Again, this is an array of values, where the index of the array represents the symbol value (the numeric value of the byte being encoded), and the contents of that indexed item is the length of the codeword used for that symbol. In the dictionary file, this array is compacted down to use only 128 bytes, placing data in both the upper and lower bytes. Therefore, by treating the upper and lower bytes as individual elements, a Huffman alphabet array of 256 bytes can be generated. For more information about the layout of the stored variables just discussed, see section 2.3.2.1.2.4.2.

From this codeword length array, the knowledge of a classic Huffman tree, and the information detailed here regarding the constraints and guidelines that are used in the encoding process, a Huffman tree can be reconstructed. After that is accomplished, the codeword (bit sequence) for each byte symbol can be determined by walking the tree to that particular symbol.

At this point, the codewords for each byte symbol are used to decode the compressed strings (the bit stream). If the stream is using a single character set, the character set value (a byte value) is added back into the odd bytes (the first byte, the third, and so on) of the stream, and the actual byte stream of characters is then reconstructed from the encoded bit stream. For an example of this process, see section [2.7.4.2](#Section_2a1f1eeb14cc4ce9917962bce6b7eeee).

Note that the codewords (bit sequences) are encoded without breaks in the bit stream. Therefore, if one string takes 15 bits to fully encode (as a series of codewords that together total 15 bits), and the next string takes 10 bits, the resulting bit stream of encoded text will be 25 bits. No padding exists between strings.

The vector of record handle structures that is contained at the end of the dictionary file provides the page number and bit offset for each compressed string in the dictionary (or the page number and byte offset for uncompressed strings). Using those record handle structures, the continuous bit stream of compressed strings can be correctly divided before decoding them into a byte stream (see section [2.3.2.1.2.5](#Section_410567dee89b4262bc7c856fcd4740e8)).

#### Conceptual Overview of a Huffman Tree

To demonstrate how Huffman encoding is used, this section provides a conceptual overview. The field names **uiDecodeBits** and **encodeArray** come from the **XM_TYPE_STRING** hash data dictionary (section [2.3.2.1.2](#Section_c1ebc0f5ccb14d14a6b59276aed28872)).

Assume that a data column containing two strings representing gender exists. The strings are "Female" and "Male" and appear to use the [**ASCII**](#gt_79fa85ca-ac61-467c-b819-e97dc1a7a599) [**character set**](#gt_5004b992-4a9c-41c9-b65c-b2e7a2b04204). Internally, they actually use [**Unicode**](#gt_c305d0ab-8b94-461a-bd76-13b40cb8c4d8) because Unicode contains the ASCII character set. The strings are stored in a dictionary and are Huffman encoded. The dictionary page that contains the encoded strings has the character set (a value of zero, which indicates English) and indicates that the strings are using single character set Huffman mode. The page also indicates that the value of the lookup table decode bits (**uiDecodeBits**) is 3, which means that the characters in the strings were most likely encoded with 3-bit codewords and 2-bit codewords (see section [2.7.4.1.2](#Section_690e69ab8041455fbbcc2f9cb6ebc839)). Single-bit codewords are not allowed.

The dictionary also has an encoded array (**encodeArray**) of the Huffman alphabet used. The indexes of this array correspond to the Huffman alphabet symbols (byte symbols), and the content of each indexed element indicates the codeword length that is used for that symbol (byte) in the encoded string. The symbols themselves are bytes, not characters, and vary in value from 0 through 255, which is also why the size of the Huffman alphabet array is fixed at 256 elements.

In this conceptual overview, almost all the array elements are equal to zero (that is, the codeword size equals zero), which means that those byte symbols are not used, except for the elements at the following indexes:

- The element at index 70 contains a value of 3.
- The element at index 77 contains a value of 3.
- The element at index 97 contains a value of 3.
- The element at index 101 contains a value of 2.
- The element at index 108 contains a value of 2.
- The element at index 109 contains a value of 3.

Note that the preceding index values (70, 77, 97, 101, 108, and 109) correspond to the ASCII numeric character values for the letters, 'F', 'M', 'a', 'e', 'l', and 'm'.

Because the strings are using English (ASCII), this behavior is expected because a one-to-one relationship exists between the byte value and the character value in ASCII (or in Unicode using this character set). This would not be the case if the character set used needed more than one byte per character.

The dictionary also has the encoded strings as a bit stream. Note that this is a bit stream, not a byte stream. In this case, the encoded bit stream will be decoded as the string "FemaleMale", which will then be a continuous byte (not bit) stream of decoded characters. Remember that the character set upper byte will be added back to each of these bytes. The bit stream itself is 25 bits in length with the following sequence '1000011111001001011100100'.

The following diagram shows a classic Huffman tree that is created by using the frequency of occurrence for each character. Frequencies (from the original string stream "FemaleMale") are shown in the diagram.

However, this tree also shows that symbols with 2-bit codewords are at one level (the top level that is allowed), symbols with 3-bit codewords are at the next level down, and so on through all the codeword values. In this case, only 2-bit and 3-bit codeword levels exist. The symbol byte values (101 and 108 on the 2-bit level, and the next four symbol byte values on the 3-bit level) are placed according to a classic Huffman implementation, where the lowest value goes to the leftmost node, the next-highest value goes to the right of that node, and so on across the level.

![Huffman tree example](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAj0AAAHKCAYAAADo7vo9AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAP+lSURBVHhe7L0FuHVF2bgP5meB+CmCiNIlXdKNICktLY0ggiglLd0gIN1S0t0lCAKS0ikt6tddv/X/38N7b56z3Oec/b5n77P3Pue5r2tdq2dNPvPMM7NmJquSJOkr/vu//3vC0Qf8y7/8S/Xaa69VDzzwQHX++edXxxxzTHXxxRdXTzzxRPXnP/+5PP+///u/E56uqv/3//5f2f/nf/5n9T//8z/lGDj+53/+58b9//u//yv7JEmSsUIqPUnSw6CAoLCw/cd//MeEqx8oLCg6W265ZbX44otXM8wwQ7XoootW2267bbXnnntW3/3ud6sFFligmnHGGaulllqqOuOMM6q33357wttVUW7kX//1XwecAwpQKj1Jkow1UulJkh4nWmNQUFB+9t9//2r22WevfvnLX1bPPPNMQ0Hh/r//+78XJYlr//Vf/1Xdeeed1UYbbVTNO++81XnnnVeeQ2mC6HadVHqSJBlrpNKTJD0MyomWHhQYrDsoL0cccUSxAr3zzjvlXjPqCg3PbrLJJtUGG2xQ3lVBEp6P1qQkSZKxRio9SdLDqNCgkDBGZ/XVV6+efvrp6p/+6Z/+SkHRshOVHY4Z1xM59dRTq2WXXba4IbgV39MSlCRJMpZIpSdJepx/+7d/q55//vlq/vnnr5566qkJVz+EgcpYbaLFBwUonmPZYUMpgueee65acMEFqxdffLFch7qylCRJMtZIpSdJehwsNWuttVax8AiWGbqmUHhUWoRrjseJVh4VHvj7v//76qabbqr23nvvxgBn3kPBkhzTkyTJWCOVniTpcb73ve9VF1xwQbHmgHuxWysqNaC1BuWobrlxLM8qq6xSXXfddUXZicoTSlVdmUqSJOl3UulJki5iFxQKSxy/g9UFHnrooWqxxRYrxxB/LW+HUoIl6Bvf+EZx13E8KFH4IZWeJEnGGqn0JEkXUbmJ428izLdz4YUXlmOVEK02g70zMWDh+cEPflCdeeaZE6582A2W3VtJkow1UulJki6iAtPMqvKnP/2p+upXv9rozvIZ/9pqh9ID99xzT5ngEPiGXV+p9CRJMtZIpSdJegAUDJUMlBmUoVtuuaVaZ511GtYg0AqDctJMUZoU6Nqabrrpqj/+8Y/l3O+1y/0kSZJeIZWeJOkBVHSAPdadQw45pDruuOP+as6cdltg+Dbz9tx1110TrnxogUqSJBlLpNKTJF1GK0/srsKis/3221cnnnhiOee+3U4sMArtsMTgBt1lO+ywQ3XOOedMuPphF1qSJMlYIpWeJOkyKjt1C85mm21WnXLKKeWYe1pfVH7aYY1B6eH7O++8c3X66ac3FKns2kqSZCySSk+SdJFo4VHpcUzNxhtvXF177bXV3/3d35Vz0MoDcazPSGFNrvPPP79YmFSm6kpYkiRJv5NKT5L0ACozKjKM49lvv/2qY489tvrHf/zHcg2cpyd2hQ2HXVW4WZ/Y0O+tsMIKZTV2aadClSRJ0iuk0pMkXcRuJBWT2GV18cUXV+uvv345/od/+IeyF5QS/+QaCqw1cWkJiRYjlqSYccYZyyrsKkXN3kmSJOl3UulJki6i4qKyE8fSvPTSS9Xss8/eUECYtwcch9MqzbqpVLKwHL3yyitlVmbgWf2QK60nSTLWSKUnSbpIXPpBVGjYL7300gN+Jf+nf/qniVJ4BKWKd/0O5yo3Bx10UHXYYYeVY9BP0eqUJEkyFkilJ0m6iIoFiowKSVRqbrjhhmrFFVeccPbhmB4sNa0oPz5TV6qwMKnc0LX17rvvlutea6XrLEmSpN9IpSdJegCUEhUTLDBxIPFCCy1UPfDAAwO6vuJfVsOBIhPdi3Pw7LvvvtWuu+5ajlV4IMf0JEkyFkmlJ0m6TFR2hGucM7D4scceq1ZfffUymDn+fRWVlKHAgqPSE5Wf3/72t9VKK61Uur1QovRHs0HVSZIkY4FUepKky0RFpFmXFQrJRRddVG2zzTZFEeGZaK0Ziqi4oET53htvvFGtvPLK1RNPPFHOteygVOmHVHqSJBlrpNKTJD2M1hf2xxxzTFF8/ItLpaRumfG8Pi5Hy9Dzzz9fLb/88tU111xTzpMkScYLqfQkSQ+j1cX9mWeeWc0///zVm2++OaCrK867A3RZAYpOtApdd9111VJLLVU9++yzE64kSZKMH1LpSZIeB8WF9ba0+jzzzDPV9NNPX+22227Vyy+/3LDgsHdsDl1Z/unFtUsvvbRaa621qnXWWaf6/e9/X677XpIkyXghlZ4k6WFQXlRi2IRBzaeddlo1yyyzVHPMMUdZkf2EE06o7rvvvuqmm24qv7qzWOkGG2xQTTfddNWaa65ZXX/99eXderdXkiTJeCGVniTpYVgiQliDS2tOhDE6rJC+5557VjPMMEP1ta99rXRh8Sv6FVdcUbrCQEsRNBswnSRJMtZJpSdJehy6thy87J9eXGP1dcfrHH300cXi84Mf/KB0ZW211VbFCnTiiSeW+0w+CLyvwuO4nyRJkvFCKj1J0uO8//77ZY+lBkuPig6WH7q0pp122mrHHXcsv6GDv5+/8MIL1UYbbVQtuuii1a233tpYrZ3309KTJMl4JJWeJOlh/CsLy46gBB166KFlMPNPfvKT6r333ivXUYhUeOIg5XvvvbfacMMNq0UWWaS68soryzWUntjdlSRJMh5IpSdJOkz8ZXywiQhRQNj8+yrir+koNzvvvHM188wzl/E7/p01FHyD9xkE/cgjjxTlhzl6rr766glPfGgZ4pmoXOGPOHg6HkP9PEmSpNdJpSdJRoGoIKAEqVzwF5ZEJQjlRwXprbfeqrbddttq9tlnr44//vjSTdWqlSYqMbp3zz33VKusskpZ0+uhhx4q13DTyQ3d62fei4ob/ozKW5IkSb+QSk+SdBi6qBxHE7udHGMTFQisNygdKDWvvvpqmVeHyQgZqMxzXNeNVn89Z8CzStKf//znxvcef/zx0uXFul4vvfRSucazUUGLihjwzfq1JEmSfiGVniTpMIN1A6G8qIBEy83DDz9cbbrpptWss85aXX755ROuDlRyWv3zqq6gaMUBxwsxp8/cc89drD9MdghROcP/dIHFdbnwbyvda0mSJL1EKj1J0kGiMiN0afkLutYflJ+bb765Wm655Uq3EwuMChYhlA6ejYpPM7frqOSgJPnbOtQVFp676qqryrfXW2+96pVXXmm4Hy1RoMUpSZKk30ilJ0k6TOxeisqGEw8ygeCKK65Ylom4/fbbBygVHNctRShJg1mPmhHH4zDGJ47zgXif755//vnVPPPMU22yySYDJkfkuyhP+ilag5IkSfqBVHqSpMNEJUNLDcoPXVff+MY3SlfWjTfe2PiLSuIion/5y18GdGm1qnA4BqdumVFp0k3PUYCw+nB+6qmnVl/60peqvfbaq1h+kiRJ+p1UepKkg6hUoMD46zkTCjJeh/WyGEwcLS1xzA1gJYrYzQWxq6sVeD5aiOy28lpUpKKiduCBB1YLL7xwUX6cABHqfk2SJOl1UulJkiFAMdDyUYdrKgpYUrSmoFzUFRKUiJNOOqmaccYZi2WHP7OaudmrYJliQsT55puv2nvvvRtjkgZTfIi3ZhYm0PqUJEky2qTSkyQtQmXNIGQVHSvuqBjFyhwrD+9sueWWZamIH/3oR0XZES0tvUxc84uwEXYsPvzthRIEKEQqeVitVOa0YPEeVi7io9VuuSRJkk6QSk+SDAEVNpW1XVNixR4rca55nXlv9thjj2qKKaaozjrrrIbFgz0KUj8oPOJ8QmB3G3+C/fjHP66mnnrq6uSTT24oPdHiJXVrEFav+t9jSZIko0EqPUkyBLECp2JnbI7XUHC4piUD3nzzzbLI51xzzVUGAjMZIPd5z4qe9/qt0ve3+TqEn8VOZ5hhhuq4446bcPWDSRABhYf4wuoTrWRAvCRJkowmqfQkyTBglalbZrToyOuvv15tt912ZRFQLB9QH4SMghCtHv1g7VF5ARQXlRYVGe//8Y9/rHbYYYei/JxyyinlGnFUV2y4RriJh1R6kiQZbVLpSZJhoHLWusMei4fKC2tXsYwDys5pp51WrgFKAPAcVhK7f/oRwkCXVF1JiecqcK+99lqZ3JABz5dcckm5RpzhhnGWJEnSLVLpSZIhGKw75qabbirrYrF21fXXXz/h6gfWHKkrOlT6dIOhQKhE9TqEP4YDv7MJ4YgTGNoFhuVr3XXXrb71rW8V5UeliL1WsuhOkiTJaJBKT5IMg4oPlTXLQyyzzDJF4bnyyivLdS0Y3PePJeC6SgD34pgY3OyX7h38jrIWu+PwPwpPDIPKDM85seKDDz5Yrb/++tVSSy01QDmMg6OTJElGi1R6kjEPFTPWisGUDCtroMKO3TC+49IMDFJ+4IEHigLTL9aabuIAb+Js5ZVXrpZddtmy1AYQz6RLtCRFxaoev1G5jGmUJEnSKqn0JGOaoawp3Iu/omN9qFe0WHaYPZmumueff74M3PXPq2jVSQaHAd0qltddd12x+mywwQbFCiTEe+zuwpLEO0wXENOQ82hRSpIkmRhS6UnGPFSoKCjROsPeLhauR2sDg5APOuigsu7UxhtvXD333HPFskCFK/U/s5LmxDiLx9dee2214IILlkHgt9xyywBrWzP43T0qRUMps0mSJIORSk8yrlABiliZYsXZd999SzfWT37yk7LIJ6goAZWt53GMTjI4xJndi8QdCqRKC11dSyyxRLH8OFt1tL7FQdJ1HGuVJEnSKqn0JOMCKlkrWuCYwbYoOlgRWFKBCQV333338ucRqNw4aBeokLNbq3VQcKLSCChAWnYc8HzuuedWs8wyS7XTTjtVb731VrlmPMduR57Pv76SJJlUUulJxjRRQan/MYXCs88++1TzzjtvtdtuuzW6u3wm7mP3F1CZD9clk3wIcUX8RiuOyku05hx11FFlgsPvf//75Vnjnb1pWe9qTJIkaZVUepIxD0pLHPT62GOPFYsC60YdffTRjYHJsbvKAbOxksYiFM9zIO3wEGeDdQNGxRFLTnzuvPPOqz7/+c9Xe+65Z/Xiiy+Wa1FhRYHN7q0kSSaWVHqSMU200DzyyCPV9773vWr++ecvFgWJ1iCsD7FyBe7Ha/X7yfCg3KDkkB5sdldxDThXAeKayuUJJ5xQzTTTTGXxVu6jjGohsmssSZKkVVLpSXoaW/9UcFaUVHwvvPBCOddKExfw5Hrs/mCw7He+851qySWXLCueqwjl2JD+gLRlgPnss89e7bfffsV6BFjaTEOtbnZRQiqnSZLUSaUn6XliN8Zvf/vbao011igT3S266KLVz372s3Ldyi9adu65555q6aWXrlZcccUy347wjFaFpLeJ6cnfXaQ363rtuuuuE65+mPZaftgvtNBC1e9+97tyniRJIqn0JD0PSo+KyjbbbFPGe9AFwjbzzDM3/raym4puLGb+XW655UrFFytDj7EGRatA0pvY/UW6ab3705/+VO21117Vpz/96aIE0xWmVYcV3jfbbLOi9HAvSZIkkkpP0tNQoaHsaJlByaFrC1CEUG5uuOGGRmufP7IuvfTS6vHHHy/n8c8gK1DIQcj9QxxzBXR5eo20F6+xn3POOatHH320nCdJkkgqPUnPY/cW1pk55phjwGzIJ598cqOrA8XIcT9xPAeTDOoGStT777/feC7pD0hblNyoADFzNrzxxhtlT5q+/fbb5ZjZnl955ZVynCRJIqn0JD0NFRkbSgz7BRZYoHGdipC/ek488cRSIWq9sQsLeE6w9ERlKA5+TnoT0pT0bDYoOV6LUwnAKqusUsZ0JUmSRFLpSXoaKzYqPio2urcY0KqCs8MOO1SHHXZY47loCeD5ZssY0D2CtSfpL1Ba6cYk7e3upDtT7OIExvTYxZkkSSKp9CQ9T7TcMM8Og1VVcqjcVGzqCo/QteV4nvgnmBVn0ruYXrHrEjw2H3Df9OfewgsvXD377LPlPEmSRFLpSToKFVAcQEzlhEJiZWalFbueeMcK7Pnnn6/uvPPOcsxfO7zLX1n8rr744ouXNbPspoqKTlSAkrELeUUFiHxw2WWXVWuttVYZyEweYbyXSjH5A8uQeU/LEGPE6gPbvWeeBI6johzzdZIk/UEqPUlHiZUJlU20tHDMfSstcF4WWumbbrppWYTyoYcealQ2KjN/+MMfyj52b8RlDKIClIxd6hYgIF+prLCP3WFYCVnR/cknnyznMf/IYFMZ8B2UoVSok6R/SaUn6TgoMlZMtI6pNKiMbE1znzlYqJx+/etfVyussELptrrwwgsbFYzP6k69YkLJia1wn0/GB+Qd8oBKNXkhKsHRKnPmmWeW7q911lmn/PkVFZ+olPOOY8mi8g7kQxX0JEn6h1R6ko5CJRKtLlQUsbLw+De/+U3542aRRRaprr/++nLNCggFhkrMistWPBUPShHPRYVH6hVVMvYYyqJnPiFvRMXG68znxMB4xom99tpr5ZpKdl2hUdlOkqS/SaUn6Thad6g4YosbZeWaa66pllpqqeqb3/xmdccdd0y48+Hv5O+8807Zg5UVuP5SvEblhsUoXkvGFygr5DW7tKLii3VQ64+WQiw5KD+s60V3avyrj2dwLyo8uIcSnnksSfqTVHqSjtLM2kLFQxfDYostVhYCjTPnUsGgDMWuCXBCQt2LLXwqICsmKrpslY8vyCsoyUOle5zQslmeRJE5/fTTq9lmm63acssty4SWw6ElMkmS/iGVnqTjoJRQQdDFcPbZZ5curPXWW6965plnyn2uq+TECglrDi3tuGI6x3Y9sEfJ4V27JQSLUrbGxwfkgWhBNE9ozYmTUJrPeB5Fp56/uH/88ccXy8/3v//9kgdVpsib5r0kSfqTVHqSjkJFQQVzwgknlN+IWTD0pZdeKveoTKKyopLC83Ulpj5w2corEpWctPaMD+ppHpWfCM8NpbDU8wu/uTPT99e//vXqkEMOaSx5wXPZvZUk/UsqPcmQxMqAFjRQeViBUAFIVESofGhhH3DAAdW0005b7bLLLuUdnrdboNlsyUnSS5CH99lnn2ruueeu9t1330Yed8LMZsoP5SReN99bfrjXrIstSZLOk0pPMiwIelvQCm6wAqiPbXjqqaeqn/zkJ9V0001XHX744Y1FIGkta8EZqtWdJL2C+RQlZ7/99it/e2H5iVA2Yhkgjw+Vv2lI1C1LSZKMDqn0JEMShTmt09haBe57/Mgjj1SbbLJJ+RPr2GOPLX/CREtQVJjee++9CUdJ0tugwJhfUVZ22mmnaq655ipjfyBabWJ+ZzA0ZUOliHvRApQkyeiTSk8yJFGgM+AT6w4CPCpDr7/+ehmrM++881ZnnHFG+bMqtmRpJUclyXezAkh6HfKoeRnlR6vlm2++We28887V1FNPXZa+QLHhPoo9x/UxaXV4Lru4kmT0SaUnGRYsNs3M8UzlzzpHjHc46qijJlz9sEuAwceOfQCUnaHM/knSa0SFJ6LCjvKz2WablRnEzzvvvHINeJ4N5Sc2ECDLQZJ0j1R6kiFx3A6tV+cuufnmm6tvfetb1TzzzFPdeOONAwYka8qvW3FQgGLLVneTpF8gz5qvtey4pwGwww47lEVwL7/88vJMROWH92M3b5Iko0sqPcmwMFcJwv3ee+8tyg4big/CPio3UZHxepwjhVZzfAY3k6SXIY8OttQFikzM/1g1H3zwwWrllVeuFlxwweq22277K+U+Kjyp+CfJ6JNKTzIsF1xwQZk9edVVV61uvfXWCVc/JAr+2A1WH/gczfzDjXlIkl6CvIySYv6Oeb5ZXmbh3BVXXLGUmauuumrC1Q8GOsd3kyQZXVLp6XPi3yLgGBqtKI4dQNBGywpCXOHr4EuI7l188cXV1772tTJI+e677x7wfprok2R47rvvvmqllVaqlltuueqBBx4o1yh3Wo9UmKLVKJYtyxz37B7mvs8mSTJxpNIzRogDI21NKiSjhSVaXyAKT/+yYibaL37xi9VWW21VVp+Og5EBAR3dTJKkOY6Du/3228tg5zXWWKOM/wHL0J/+9KeyB7uD4wzksazF7uIkSSaeVHr6HNcNwvSOwsIWrTUqNSg68TpKEsqMFh+EKUtFzDDDDGVAJoOT62Z73OD5aPFJkqQ1KDf83s5g54022qj6wx/+MOHOB1AOY5lD8UHhiWuDqfTYoEmSZOJIpafPiRYeqHdv1bu/QEUHUG6YaZb5Rvbaa68iVKM1CKHLFq8lSdI69QH/jAviD69vfOMb1Zprrlnm/qFsqfCg7NQbHJRnGzYQ3UuSpHVS6RkDoNjUFRIEp9fco7iwojkwv8h2221XffnLX66OPPLIIkQZZ6DSNJxQxc04aDlJkubEriqUFyw3KDU0OJjbB+Vnt912q959990JT31gueUZGzUcW94cD5Rr1yXJxJNKT5+DcqKpu/5rLUKS+3ZlAQIX0/pMM81UnXrqqeVa3RrEe1zjXYQ0e67pnsI3SZKhsaxQBuPYnQhlk4bHLLPMUm2++ealQRKxLEIse1kOk2TiSaVnjPD73/9+gEUn7hG4999/f7XuuutW008/fUPZofXoIElblJzbMuVa3YIkaelJkuFpNhcPFhqtOjY4LGdnnXVWKaO77LJLedduaqA8a91hUd8kSSaeVHr6HJQUfi3/6le/2hCgKCMKx6uvvrq0HpdaaqnqzDPPLNcgmtzjexIHT0Ld6oOQHkwhSpLkQ+L4HBsXoPXV8ueeZ7D80PW8//77l8lBKXNae1CGpplmmjIGL0mSiSOVni6DIFN50HqiUiEIx9jiA5USFJnJJpusmnzyycux1h1mg11++eXL7LCXXnppuQbcV/Cm0pIkvQflkvJOWT3ggAPKH5VMI0G5VSGizLNtueWWDWttVK6aWZiSJEmlp2dA0amPn2GLLUPu0eqT008/vZpiiimqj3/840UAfuELX6jOPvvs6pvf/Ga17LLLVtddd92EJz8At6JgTJKkN1EeAD8f7LnnntXXv/71au+9964+8pGPlPL+yU9+shzTsNGyG8f1aTkSlKkoX7LRk4xHUunpERBCg4GlRwFF64/za6+9ttHaQ/B97GMfK8d0Yz3xxBPlWcFtLUCi8EuSpHsMpnxwjXsqPlh233rrrWrWWWctDR3L/kc/+tFS9uedd97qvffeazyrpQcrEBsNHmRAtCwnyXgklZ4ug1BrpnwgmBR4tt4ch6PC85nPfKb69Kc/XY7p3kL4oQAh2ACrDm4g8KKgowWo20mSdA/K/lCND7uu4Pnnn28oPCg7Kj5sn/jEJ8oip6+++uqEpz9o2AxGVKiSZDyRSk+XqQsmlRT2KCrOwErLjXMW/4zCTgsPXVvsP/e5z5U+//fff7+8Jwq5KGCHErZJknQeyiDbUNYXurRpwDCfD2Xchg5lnT1LxrBnm2qqqaq77rqrYdmlzLMhZ9iG+1aSjHVS6ekyCCA3BWCEcy095557brHuINymnHLKhsLDhqXHY4Qj1hwEJUoTSpRCL5KDHZOku8Ty3wzH4LHg71prrVXG8Xz2s59tyAE3LLyM7WObdtppyyrvdZAlKj5JMl5JpafLIOyaKSSco5TQSoNzzjmnYdJG8LFX0fn85z9f9vPMM0+1yCKLlHE9tPZ8VxB2mMvr30qSpLsMpvjEhomzqXPtzjvvrK6//vrqsMMOKzOrs5K71l4UIH5pP+mkk4rFp5m7yIb8qSEZj6TS0yNEwcRA5WeffbYItjPOOKM64ogjqg033LDaYostysSCtPp+97vfVbfeemt5Pv6xERUaTdxca6YA1a8lSdI9BlN84nITWG2F8q3iEsf+MDcXf3sxwSFKERMeIjOY6VmZkCTjlVR6Rol6V5LnKB4qKo8++miZSJAlIuaaa65qhRVWqHbeeedq1113Lb+lsjoz/febbbZZWbBQovJCd5YCMM3YSTJ2iEpO3VqLQnPCCSdUyy23XPnDC4vvaqutVub5+c53vlNkxxxzzFHNPvvs1YEHHtj400tUphxDmCRjlVR6RoFoiYkzHaucvPTSS6W/HkHF7MqxZYeQi8oL09dfeeWV1fe+971q7rnnrm688cYJdwbOsgxpyUmS/gd54OzNwHGUCccff3y1zDLLVN///verhx56aIBCpDKDBQl5w/pf22+/fVGMjjrqqAGNMRUe3MeNtAolY5FUejqMQsW9ggQhxDGmaFpimKARNI67QfCotLhXYeKcgcovv/xyteKKK1annXbaADM3gi6awZMk6U/q427iX5koKViADzrooNLdrSJE2Y8Nnr/85S8Tjj4cF4ScoAsMy9Dbb79droHfiw2vJBlLpNIzCmiBQamJ/fYsG7HBBhuUSccQUnXFCLhmK8/rWogQbgi6rbfeumzgPfb1GVmTJOlPVEYo7xy//vrrReFhrE60AkUlievKmmj9QY6o1NClzt+ezz33XDlHVmmZju4myVghlZ4OY4tL07GtMdbDwsyMUtNs8U+UlnorD2HF++xVnnSfLq9NNtmkHENUrpIk6U9UVpARyg5YeOGFyySlyA9lAPc5Zu9xXdlpxiuvvFLGEDIuSOpd5UkyVkilp8NoeQGFETOrMn6H8TkKJYQXSgrPa/HhWRUX980EF/30tM4wc5988skNBUthmCRJ/6I8wLJLo2iNNdao7rvvvnKtGTaOPI6yA+tNlElMfMj9F198sVp66aXLtewaT8YyqfSMEpqTEWCzzTZbMU/XicIoPh/hGRSlZsoP/fWzzDJLcbv+XpIk/YnWXxQWVlv/4Q9/WMb3cW6jCcUFmRCVnGbEe/GnCt47/PDDqx/96EcN2RF/wEiSsUIqPaOAfeMIkV/84hfVT3/609J1xUaLDIETzdDNWlq23CKasqNwuummm6q11167HGeLLUn6H5QQGznTTTdd43dzZQJyoG7VjcoNxzaWgGdVpLgXZQvu/93f/V3+up6MWVLp6TAKK0CQMM8OJuWo5IwEFRuFHkJsvvnmK9ae2JJLkqT/QE6olOy///7VwQcfXK5FuTIStC4rK/j9fYcddijH2WhKxiKp9IwCCq0HHnigWn755UvLLbbERkLdHc5//OMfV8ccc0zbvpEkSfdA+UA54ffyBx98sNHAid3hI0GFB4v0G2+8Uc0777xFsUqlJxmLpNIzCiCkUECYHZV+c4WW+5ES//JCwXr44YfLxIVJkvQ/yA4mMP36179ezrUSt0vpsavLxtkCCyxQ5v1plzUpSXqJVHpGAZUeWmr3339/Q2i1qyUVhZ9uszhpu5SqJEm6gzKCsXrID0A5aZdCovu6xzkzOzP2MJWeZCySSs8ooCJCS425MNpp6dFtBZRu/u3f/m35JT5Jkv7F8szCw/y1ReOJrV3j9ZQfoMWH5Sn22WefAfeSZKyQSk+H0WQMX/va1wasdNwOoaJbWnt0k4UFX3vttXKcJEn/wlgb5t/aa6+9GkpPO8fbKDvsJj/ppJOqnXbaqRwnyVgjlZ4OE5UeBgg++eSTRWhBOyw9ugUKRNzl19O4Tk+SJP0JSs/ZZ59d7bjjjgNkRjvkh2jlgSOPPLLafffdJ5wlydgilZ5RAuWHGU/vvffeCVfaN6an3rUFH/vYx9o20DFJku5go+biiy+uttxyyzKHTjuJ43acT2zXXXctkyDWl8FJkrFAKj0dBqGltWfDDTesrrjiinJMNxRKD/soeDhG2EQLznD4DqD4MKX8nHPO2VYTeJIk3YEpLl5++eWyMChY1qNSEi3KoMV3OJQz0dKz/vrrVxdddNGEsyQZW6TS02FsPcE555xTrbPOOuU4LhOBcGJDeYkKUF2QNSMKNpeuOPfccwcsPpokSX+iYsMCoIzTe/XVV8s5E5yKDat6Q6nVhhONIxtIf/nLX6qpppqqHCfJWCSVng4TFRf+uJh22mnLNYRLHRSYKKhatdTEFh+Kz2qrrVbdddddLQu9JEl6F63CP/nJT0q3kw2m+CNEM6WnVWI3+AUXXFCtvvrqE86SZOyRSs8oQCtNmOL9Zz/7WTlGWWmm2CC8WjFNA4KP5xVcjz32WLXwwgvnEhRJMkZARlDGn3jiiWqppZYq1/70pz+V/UiJCg/f2XTTTasbb7yxHLdiaU6SfiOVng5j64s9Ss7bb79dzTTTTA3rDEoLwgXho5Chiyv2sbeCCwTSSrvsssvKcTOFKkmS/qFehrfbbrvq2GOPLceDNYyUOa2A+8oixhtiJYZ2D5hOkl4hlZ4O4xgdBJTmaObcYB6MaI1B+EQBF1dOHw6VpfPOO69ab731yjHkSslJMjZwbOA777xTLbvsstXjjz9ezpspOMgDtlaVH57DcrTQQguVAdPKkyQZi6TSMwqg7Kj8qMxsscUW1SmnnDLATB0HMWPpaUX4YCFiHM8LL7xQLbHEEuUaClZ2byVJ/6PigjzQ+vv0009XCy64YFGEsNLULT6806rC488P/GDxq1/9qhzXZVWSjCVS6ekwWnfsxkIYadHh11D+6FLxiUpPq2N6gEHLLBKI4iPRrSRJ+pf33ntvwtGH3U7XX399WYuLxg2KT6tKTh0aTWussUZ15plnlnNlUxzrkyRjiVR6ugwDm7fZZpvqj3/8Y6NvvW6lqStDjv/ht9VDDjmkWnnllRvC0FmYs2srScYOKDWxIYSVh5XXF1100er2228v91R8kA82skBZgEJjIwwefPDBaqWVVmrMHQZ1a3OSjDVS6ekBbr311mrqqacu07+j/ADCSSFm6wvBpiBjhta55pqrOuywwxpKUpy7I03TSdL/RCUldncjG/gr9K233qrWXnvtapVVVqnuuOOO8jt7VFx4jnPfRZY88sgjpTuLyQ7529MuLr5lwytJxiqp9HQZWmyYr1FSUGBmnnnm0l+/7bbbVmeddVbpurrqqquqW265pdpzzz3L31mTTTZZtfnmm1dvvPFG9eyzzxZ3EGwqOrbQosBMkqT/sMEDKDBR8QEaQlh5b7rppmrdddctEwsedNBB1b777luusaEMsXI6y1jMOOOM1YorrlhdffXVE1z4ANyty4uUH8lYJJWeHoNJC/kz4+c//3lZA2fJJZcsi4ciqBBc9OVDNHUjGFV4EIwqPXUBmSRJfxGtNpRnzrUA18HSi/ygy5uV0uebb77qS1/6UpEdu+22W/lx4vXXX29MboiFh64wu8uFY2RKVLiSZKyQSk8PQJ97fQwOrSwGOK+55pplltRFFlmkev755xv3EH7sEVAKQY5VhrKVliT9TyzHlG+VE8o8ZR2FhQYP+wgDk5EZN9xwQzX99NOXCQchLosDUakC3B1MqUqSsUAqPV3GcToKM4UQ1pqNNtqoDDZEoNGVxV8WTz31VLkPvKOFp1kLMFqDkiTpPyjTlPNmjRiux8HGyIB33323LGzMfF3KA96l62vnnXduPB/H/wnvp8xIxjqp9PQIChsEFcJnl112qU4//fTGwGauMTHZN7/5zWKiBhUlhFqcQVWztAMUkyTpXyjnlvVmMJgZ7rzzzrIo6XXXXVfOIf4JijzhT08bTjSmVHTcItm9lYxFUunpMig5ChtbdAxiRkCJa3dxDwG39NJLV88991y5FgVTveWXJMnYADnBhgxAUWEP/m21xx57lMlJ49+foGxxLrC77767/ObOjxHNQIYgU4ZSspKkn0mlp8MgPOyComXFVm9B2R/PswceeGB1+OGHD2h1Kdg0STNYkQHOb775ZuM5v8FeszbCMUmS/oDyX/9lXOUFYoPGwcjPPPNMWYR07733LuegLHD8jgqPll/eRfE5+uijG7Kiju+qZAnH+HGw95Kk10mlZ5SIZmYECUKFa1EB2muvvcqvpgoZ9io1Kka8i8BhKnp+X49jfFCG5M9//vOEoyRJehkbQxHkgkoOxyo/yASVmNNOO61YfX/961+Xc5QRZAr7KEMicSwPihKzwjMOCOrPqvggg9i4H59Ja1DSj6TS02FQUKKwoJVVt/QgPE488cTqBz/4QUOQxHdouUXLj8oNf3Mtv/zy1b333lvO+ZZu17+RJEnvYTml7Fr22UcLD2Vfy44wWHn77bdvKCy8Yzc44K5u82dotCCp+Lz22mvV5ZdfXn5pf/LJJ8s1lC+ULfwT/QD4g+uSMibpR1LpGQUUOFFwRQHC76Xf/e53yzGtq/q4HM8ZyCyaql955ZXqW9/6VrH82Fr09/co6JIk6T1iGaVxU7f4qAgBk5hi1ZltttnKr+h2Y0U3kBUqI+yRMbqptZlrWnHg0Ucfreaff/7qyiuvLOe4p9vNFBvej42wJOknUukZRexywoKjoDr33HPL76XCPQUdz0QhWBeImrlxd/HFFy8tN4VUXXFKkqT3sOFTVySQASoelnsaR8zWTjmvywjkRt0yE2WADa4oQ7gWr9NdzlqAgp9wk29x32/yrZQvSb+SSk+HsYsK4cExSomtLKaCZzkJhEt9ckJQ6IECDSEVxwcxfw+g+Hz729+uHn744SKgFKZJkvQ2lGnLK4pF3brCDwtMNEj3t8SurAjv17uzII7l8Z6Kluccn3feedUyyyxTLMdRicJP0V9RNiVJP5FKzygQTc7CXBos+ocCg3BR8VGhsUUW30M4qUQxricqPyhSb7/9dpmEjAUFIU3QSdL7RKsJyoll/v3336/OPvvsovDwq7lonUEeUO59HtkQlR3cij838JzyQ/miYhN/dWcR0mWXXbas+6c1GXwX8LOWnyTpJ1Lp6TAIEYUDSggC64UXXqgWW2yxptYd4DmUIE3KCCsVGNxTUIEtOAXfq6++Wiw+tNRS6UmS3sdyilKhQsMA5R133LEsEqrigSyIFp5ozY3HKD717qfott9TQYp/evIccofxg/wkcc455zS+H5WelC1Jv5JKzwhRcUHoqIzQ+lLRsUWlUMIKw8BjlJR2m4h1D4G00EILVb///e/LOTRrsWW/fJJ0lqiMKB/Yq3A0K4vMrMz4Gqw83YYxPltssUWxBOlX/K7/Y/i8zzUbYUnSa6TS02ZsTYFWGK6x0XrjLwkGIraT2M2FMEKosiwFJmq60aJFSatRCqUk6TwoAigB7KOF1vKn8kAjiQbSGWecUWQEXUy9AP68/fbbSyMK+VVf2gZZokUaCKuKUAxvkvQKqfSMEIUW/e+CkmGBtwXHeBuUEFpMCojBurcmFk3NfktzNb+4brXVVtUVV1xRzutEBS1Jks6AUhAbGcgGlCDlAOcoE3POOWf1s5/9rFxrl2xoB/ifOcEYW/SrX/2qodTEKTSAcESLVS+FIUkklZ4O8oc//KHsUS5mmGGGovgAQsNur3Zgt1bsLlMZo1trrbXWqm677bbGNZQkBW6SJJ3FRgllLi4MzHXK580331zNOOOMZUmJdsqFdoAio8KGYrbJJpuU1dpVaLAyx8YTso1zw5wkvUYqPW1AAeCv6Ag3W0MvvfRStdxyy5XBy9zX3N0p9APYEkNoofgwoZkCrNeEa5KMRShnWn2Fxgld32wHHXRQmafLmZWBxkmvKQ3INMNx6qmnluUvkG2ChceGFDIudrknSS+RSs8IQYGhsMdfR+lWAlpGq622WhmYCFEQ8F47BzJHIRn/8LCrC7+xzs6NN95YzntRsCbJWATLh7JBmFl5pZVWqo466qiGXIhWFdAy223wkwoPcovt/vvvL2OPsCBr6VHpkV7xf5JEUulpA7F/3sHLgFC77LLLynFUeBASse97pMS5OKK7th6dgwPTOnMDXX/99dnfniSjgA2baFndf//9yx+cLhQqyBAaIr1khdX/UaGxUfX6669Xq6yySnXcccc1Bjgj21SC0pqc9CKp9IwQhIEtGhUJWkUs4sdfD4BSJLH7qZ0mYAVN/BZozfG6/fJXXXVVOU+SpLM4XQRj/JhDa/fddx/Q5YUlJTZWsKREOdFtYkPOMUn4Ubbbbrtqp512ali429mgS5J2k0rPMMTWSrSoxONoNUH5YF4LpnPvFRRC/mGGH/mT7JJLLinnsRWn4IpdXwpoFaskGU+Q/2k0sLd7RywbWD9i15RywzJHI4OFQpnlGMaKYmDD7fzzzy9/dz311FPlnDhShihf0rqc9AKp9LRAbJXFvy8g9ltT0JlB9cILL2yc9wL4UYGsGRo23njj6vTTTy+Cq+5XzNoIZoS34VeI8SyCLCpLSTJeqOd9FRzKBxW7ZclGwoYbblhmN44NpShT+hllApapl19+ufrmN79Zxg0aB3aFKScJt/EVxx4myWiRSk8L1C0cKg6x0FL4WRDwlFNO6anCbLdWFLIObmYhQ5S0e+65pwhrn9H/dUUIQc81wlq/lyRjkWaKPeXEskBlz96xL5QNyxxz28w999zVpZdeWs4hjpEZK5YPFRqUGWQlYxnp7ooNQlBBirPDJ8lok0rPMCjAooBCYCkMvb/XXntVBx98cDmGXirYmtIRSArsqAzxy+wFF1xQzlXwVGqwAvFMNN0DAsw4SJKxSlTwY7kHGwlc4zg2BA444IBqvvnmK4N9KUMoAHEC07EE4Y7rdxEXrNm19tprF+uP1q96l54yKElGk1R6WkDhplk2mmcpzPTT80cG2JqBKAS7hf6JrTGJXXWbb755WaRUEFDN/K9wN06SZDxAnqeSjkoP51hurLwpY6+88kq11FJLVYccckhpKNTLUCx/Wn36mTjgOiqIjA285ZZbqnnnnbcM4FZeoACq/NUbUkkyGqTS0yIPPfRQdeyxx1ZvvfVWOY8Cy2UeKNgO7GumMHQDlZ34BwZ+9DyaoB2LZPcdLTS2Rx99tJwj3DlPC08yHiHfx3IdK23KxX333VcWCmWv5SOWO6eOoMyNpQofRU6lhngQrqPgMJ8PstOfJCDH8yTdIpWeYaBwfuc736m233776uc//3k166yzNib4Q3BFk20syAi2XlF8VFLwUxRKUfDSHRfPUXyYFn/HHXes1lxzzaa/0I4lwZ0kzdCaK1Hh1+rJzOeHH354tcIKK1RPPvlko+Hjsw5gVlZofR0rjYeo2AGyJFq8icO99967jB9EjtB46hXZmIw/UukZBiw7mGgBheGiiy4qv6SDBbtupo4tn24T/aZ/o+ITLT2iMsO4BAYksoyGRPN8kox1WGphsC4ceO6558rAXcb0AeXeckZZqVs0VBAcAN3vKCtQZOIPH1wnLpQv3OO39nnmmacofyqGSTLapNIzDAxOZvIteeONN6rZZ5+9HPeKYjNSomIUlRoE1QMPPDBA6YGxEu4kERSQqITQuFlggQXKr+YsFuzM6mA3F2Vj0UUXLXuIlk/H+Yx3VG6QJcQbaxBec801AxRJ4u3EE0+sNtpoowG/9Y8VS1jSW6TSMwyYrY855pjye7fMPPPMY6pAouhEgY2AUvl55JFHyjgFhRfCXIFeb8UmST9CWVaRx0qDJZQu7VtvvbVcu+OOO6pVV121WC0c/E8ZYBmJ+DOAFh6gvGSl/SE2rIiTKEuBpXGwpjOfEdT/8kqSdpJKzzAceOCB1cknn1yOUQZo4U0zzTTlfCwItdjVxeDLqPwAA7gXX3zxUimkMErGIlHpYc9v1jPNNFM5B8rIjDPOWMpHLAPIA6FSt6GAQtSs23g8Ux8CAMS1cUg3Ilazt99+u5xn/CWdIpWeYWCphllmmaXRinvwwQdLq4QCO1ZacnUhjWJHSxWB9Oyzz5ZZVkHLDooRx9mSTfqdmIdVfB5//PFq4YUXHmC5WWaZZcpfWaClk3frFp0oF2J32XiGeCQu2Igb4sg4BOQM036wCKvEbvYkaSep9AwDBRaBh8WDArvttttWRx99dLmnkOxnUGBi65WBllEBwoS/1lprlb52hTj7KLSSpF+pKywQlR7z/JJLLlndfffd5ZhKmko5vivRUtrMujEeiXIS2YLsUKkxvuhGX3DBBcsx8ZZd50mnSKVnGBhwd8MNN1SLLbZY9ZWvfKX60Y9+VArkWCqUCm8Ekq1bJhTbYIMNSj87Zuetttqq+v3vf1+UnzgIMUn6Ha0PwD52b3FOxUz3FnPOcK7FAjhGCaLhQNnJxsBAiCdlSiQqjMgTpsdYYoklSvw5T1hae5JOkEpPC9QLn62TsVj5E9ZmgtuJ1SJxPFCS9CtR6aGCrg9kZnLONdZYoyg30ZLj4P46lKH43HiGeCV+m8kUrqE0Euf8+r/KKqsMaEwS30nSblLpaQELH5aQsWZ2teWq2Vns4uKe1xnIiYDinWattyTpV8jnbOIv68suu2wZw8e51omY973GHmuP53X3xjsqlcRJVAg5x6JMd+LXvva16rvf/W6xtKXCk3SKca/0IMAoeFbsg7XexjMKLDCeEPA33XRTOY5CjGedgC0Vo6TbqISYh93HvIllRgUl5mXy+HCTEyadRcsz6WhaAo2yZungc5lGyWCMG6WHQoBAi8IOARgLBwUMQUerjuPkA+oVBCBYnnrqqWrjjTcu5womya6vpFcwz7rHWhvLfrOyzrgSnuHZKCNiHleBSjrLVVddVdIBRQf57ABx04V9PM50SYZizCs9scKut9I8jl1Wm266aXX//feXY60a4xniqN76Nd5oAV9++eXV2muvXc4hxm+SdBtb/jEP1znrrLOqI488siEHBhurhzsxfw/lZtIeUEiff/75apFFFqmefvrpRrd7pC5zSKdUfJLBGPNKz1CKi602hBfbDjvsUJ133nkDZllNBsYhQiieI1yuvvrqapNNNinHKpnGbZL0CtEayTFjR/g7cZdddmmMIYkWythgomKN70MsB0nnsJuRv0ivvPLKklYxLUinelogi1IGJc0Yl2N6MI9SkIRzFgxk/h1bb++++27ZJwO7AREkUcAgcNhYm2j99dcv8aewyZZw0gtYlsnDlHUUGypRJsM755xzSv5GHjieL+Zb8nbM+7Ei5b2ks8Q4ZvX2H/7wh6WBFdfoUiGNaZUkgzEulJ56RR0FF6bsPffcszrppJNKgWFT6DXr6x+PECdR+HBMfCpgiE8qEiw+m222WRnInH9fJL0AfxwC6z1RKcJpp51W/sx67LHHBlSSsby/9dZbZR9lhZD/uR7fTTqHS1MAiilyZumlly6/udfTALnULM2SRMaNpQdBVbc8MFiR1X3pz7flwDO0+rLgDERBLyo9XqMVhqLDeCgWEOQ4LT1JtyGPquwwueA888xTHXrooQ1Lr2NEyMdsDpIF/0Ks47NJ57GxRTpFhYbxPfPPP3+ZOPaNN94o14DnVYRiQzdJZMwrPVE4xUFw7733XnX99ddXW2+9dRGKbFoneIeCk5X2h+MaiBOPwXhlbwWCwOGZG2+8sSg+KXSSbmOeZazenHPOWZY7QA5EC0GsKIHjKCu4T172ufhs0nnqclh5Q6P129/+dumitNEa0ybld9KMMaH0xMxNpo+VsxUv1/0rAxPpNddc0/jdOhkZVAaCEkSc33777dW6667bUCRj10FUmOK7VjSkj4ItScgLlN3hlI2Yr8xLdLsy4R1r5mGNBPOWzyf9DeN8kOX8gGK6xzoBGRTrBGVOKq/jkzGh9ETFBszgZHwFm5UveypkhGAOVm4PsVVsGlBJYXreaKONGgoPFVAUNKSFFVSzCii6m4xPKMP1yolKizIeKzLzWBzgisVxpZVWKpYAn1XxgfinVtKfKDf4q2uaaaYpy+VEWRJlCPkmTj7bTOYkY5++V3rsg1epUUDG386joGMWYdfRqQvTZOIhDmM3VhQyHN92223lLxkrGAeWRoHjMc9zX/eiFSgZn8S8heLSrMySf+pdGYzbWXPNNctg5bryjBtRYUr6F5RdFRlk/uyzz16deeaZjXMgb8S5l5Ar0fKcjC/GhKUnttgYq6NgVBFyQCICcIUVVijPJO0jKjB0HShQTAe6EldbbbWGEKIiM01iZWW3A/cRTKn0JEI+icqLeY485nWe4S8t/sw64IADBlR05CnzJe/GActJ/6NyjAyhu2v33Xcv51FJjg3jOCFtMr4YE0qPrTYrUM8Rhlak9913Xxn0htUnFoRk5NRbzbFCsuK55ZZbyuKNseVuZcVeRSeS6ZSQB8hfMW9wjNJCniF/ee+ee+6p5phjjsaM6uQrLIfKAElleuwQLTbKISw/zLI999xzV08++eSALs9IXW4l44O+V3pUdBRsr732WtnHDM3vjSuvvHKZkCwSK+Bk0qESIS6jxUdia/vhhx8uig9WnmjhIa18N5XSJEJeqFds9cqKc2ZWXmKJJRoWnDh2YygrUdLfIHeQ/aRxvcuK5StWXHHFogyD+YZ0j/InGV+MCUsP828o7JZZZpnq7LPPLgUB4cbEVghDzN6gckQBSaHXPohLFR+O661pBc4TTzxR0kNhFdMjKqUpmBKJ+SB2S2DF+fWvf12WJzjllFMmXP3gV2YgL8axeyg+sVvL7o6kf6nLcJUfu8//8Ic/lAYvS42Ijd3s4hqf9L3SE1t9/KXxkY98pPrEJz5RZl1FyM0888zFesCxLQGO64UlmTSaKSbErfEb08dnH3rooTK2Kg42R1GdfvrpS9oouJIEVIxBRQVLzs9//vNqscUWq5599tlyjeeiIhMV75gPOY4WyKR/Qc5ouVO+KHtIf48PP/zwMnfYK6+8Us4H6/JKxj5jwtJjpqc//2Mf+1hReiabbLJq3nnnrR544IFyD0Gnhk+F6jvJ6GDco9QQ96+//nq10EILFcXn4osvLulF2jFDtgpP7KJI+hfTHqyEROUjVkKkP/lEYllFsWGJCNZf+sEPfjDhapIMDhYd8t1dd91VZA5TloD5EmXJfBkbxOQ1FCfzYlScY/5M+osxofQAf2ZNNdVUpfJk+9u//duyv+KKKyY8MXDQW2ba0cHWV4xvhQot9FlnnbX66Ec/WhQe0muWWWYpFWG9ckz6HyoZKw7S17xBlxPnWmmihcZuCt6l/DIu7Ktf/Wp19913/1UXapIMBcoPXZ90h15wwQWN+sB8yJ48pbIjHpMHlWPsU0b1J32v9NhFsvbaa5dK8+Mf/3hD8fnUpz5Vurvo7yfDukE0mSedQ8HAnrFXChBa65dcckk1xRRTNNJNC93xxx9fnostq6Q/sbxFJUe4FsfYxEZJPAbK6957710tv/zyxSqU3VNJK6DomAfBOdu22GKL8lu743rITzEvxolro6UxNt6yt6A/GROWHsyVVJaf/vSnGxVoPMfqwy/TdWImTzqHA0vBig8LHGnDhmLK/jOf+Uyx+NAtmZa4sUFdeYHYioZYwXDPtCevoBg9+OCD1ZJLLlmddNJJ5TrPsKlQJ8lwYEU0X5lvfvazn5WxhcziLFgWuc/zKktRWU9Fp/8ZE0rPVlttVX3xi18sFSeVJpUnXSacM9DReTveeeedxkSGccBj0jmaKS+//OUvq8knn3yAomN6ee3ggw/OSm0MYBrGyiJaaZgodLbZZquuu+66CVc+GDuBUsNzzK6LwvP4448PGPieeSNpFWVQVJRVaH7zm99UM800U3XrrbeW+8Cv7l//+tcb9QZEi2Xmvf6m75UefnP+0pe+1KgwPWZ//vnnl2fiMhTR1NmsFZq0H4VJnAn7qaeeKuufaeVB6Zl66qkbVjqOs3ur/1HZaab80t3J+ArSe7755ivnVCi2yjfddNNq1113LcqO75Mnsms6aRUaucqfmG/IT+Yp9quvvnq1zz77lPNvfvObJU8ydowpT+rUu2mT/qLvlZ499tijjN1xICzbj3/848YkhXWtnAyefwWNLrEbEQFExWW6PPPMM+UvHNOOzfE9xxxzTHkm6V+sIKxghDxx0EEHlfT+5Cc/WfbbbLNNeZ7J5GaYYYayiKRWIfJLXdnJyidpFfMKsj82dmMeorvry1/+csmL/BTzN3/zN9Vuu+32V4qPSlTSn/S90uMfWyg9LGzJJIR2YZG5zdQIz2iihMy8nSfGed2ypiWHyox+9R133LGkpWOxpp122nI/6V9MY8sc5RHrz5133lm6OB28TsOF/frrr18GK8euLPNNbKxkwyVpBfKOcj4q3uRLrZDc5x4TXcY/gN2uvfba8hyyzHwMOb6nPylKj0KF1peJ2ktjXshcZtxYcTKnC5ly8cUXry699NLGPTJwrw1Sjv628I2W4OZ7Vj5AXMZKpdvEBWNfeOGF0q1BK4u01dpDZakCa4s/hqnbdDN9u01d+JMultf6PfIdf8xMM800JX3t3oyWWuItK5RkNLCeYI+VByXcLnbHHdIIY14x8nSsV8yjXK8rQ5l/e5ei9EThTOKh8JhoJmC3tpjJqFgUpkwvzgBIFB9nZIU4ZgfrTjM3R3OL/hF+uY1m1dECv8Tv9kL8RGHBmA7j63e/+1218847l3l7NC9TmZIHfMfKsZtbL6VvN6A8Eg+kTV0JNb+RZrFrarnlliuVyWc/+9my/9znPtcYyM5YPCaQi0pkknQSlPANNtigYW1E2aHLlTyp1Xn++eef8PQHdST1Evm7nk/J72yUiSjbkt5hsnnmmaf0n5Owbmi7/EHDMQnfzc1Mx2bfP1s0QzLXy5RTTtk4p/Voy7GZm6O52Vrg77LZZ5+9UTFQKEbD2tKsMgJ+I1966aWb+nk0N9OMeCLNSGO22PKPaWsrjI280czN0dy6nb7dRquWIPBRcGycgMcotSwHENOwvn3hC18ocXnHHXeUOEySTvPb3/62+spXvlIGLjfLk2zIoI022qipPCV/o/zUG0CpuPcmk1HBsHBfBC3WhDWRu7nVoTsELdp7aOqxgkEQK4zrbo32BlQC+BHzKccoHKPZCqAwUjBtbfNtKhQKczM/j+ampQA/6UcsUAoM7nHMs3W4V3dvtDfodvp2G9JnsO5wZ1SmPDLfDpY78h2tapRGuzFpSX//+9+vrr766vJ8ro2UjAbKQmQOv6iTB/mTkIa/edM/gumSve222xqyabDua+rPVHh6l/8/LT8cy6yAQpirvXYbtWcyJcpZXbgOVbn0WhdDjOtuQFyRtlTQgKWk2yBwBL/F9KznP4QME9mRN916iW6nb7ew4iD9SDMUP5QclW3gnCVHiCOtePwafMQRRwyYD0VivkiSTmKDOcob1mw89dRTyxxR5FXHnmGF9HnyPXmcvE2e533yO9fdkt5jMjTawZQDW7LdhowVhSCVtgparPjIeHEMUDzuFrEgUWgoIGwocaNRKEjb+neMO/zTbewO0Y/s8R/XBMtJXdmtK0Tdotvp223qZSyWU8smcbHddtuV+GG5mJNPPrm8V09T01y5Mx7iL+k+5DO3ZnUhK7Nffvnl1WqrrVYsQCuuuGK5Tv5ult+FfJ/0HpMxdocWNIlNoiGITDyEdy+AP6hc6pYArUD4NypovaKsga1dwsBYhm5BAYyKBNC12UuYnkJejHmQtCdtudYradwr6dtNSAu6nE0rZAnzZNFa5ndfxvHssMMOZZVrW8mxsiAOTXuVqPhHX5J0CvNsVMAt07H7ijxOvr7hhhtKFxhzTF1zzTWly/bVV18t7iCfqKfIw71UByUD+f8bXx+29mOrVaGjBtytDVTCgMrbc/ZkrngfeA+hWnerG5v+AeNawV5v6XaCWPhMX+KGeKSSrvu3GxtCJvqTY88VSihs9fjivWbujeYG7ruRvr2ACgwWujPOOKNaeOGFq+mnn778pbXGGmuUmW7XWmutaplllinT+3/jG98olQYDmyWWYd2rK+lJ0kms86JCTnc63Vx0zU433XSlu2vzzTcvM4WTt1m7iwHQCy64YHXaaac1FCVlQtJ7FKVHgROFeEw0MkFUiIB3FOr1BCbzKPi5F4WX5kPe9b3odjymVejzXrcy5F2OY0XOuc9zHAUp/vEdv6v50XD4LhWt73rNdzyHVlqjvsd3GbgZC9RogR/0h3vCFxXewcC/xgXHhF83iHvDwzWe89w4jffr8eU94Dimvenkt6De8vIbuKsftRiI7/O8xDSE6G9w2RIVbN3kmeh+zMPdTN9OY1kGW7RA+C3brJE111xzlW4sphsYrGwQTyxBst9++5XByywiSjk33nAvlZ1ktDCvuSdvKysYb8bA+z333LN6+umnyzUgr0a5RF7nPjPLo9Rj2RTkB24r25A9uq/MSkaXYZWeuEI2Ao8EY5p41k3afvvtq6OOOqq6++67S8KrREgUZhIrLjKC3+FZ/IG2TJ9/rFxwO1aIvGMmJRMdd9xxpYUJuME36t81owHHVGys9B1X2AVMlWTyrbfeuvglgp+YpOqCCy5omOmHw/DxzX5VeoBF+EiXjTfeuDrssMPKZJCAO7GSUhFxD+YvYUxWfA7hQlpo1TGP8B7pix/MW1yjEn755ZdLOtX/PFShcdwSe/JoVHRIi1/84hfVd77znTIXkHlcJe6QQw6pVllllWqvvfZqpDPvmIfY614vpG8nMfykjXEaZQLhZqwDE0rW08IB880gz7zxxhvVLrvsUuZI4Tg+n39vJaPFW2+9NeHog/KM/MEquffee5d8GMs9+dZzUI5ZNgCZgkWIBa7rxOeS7jCs0gNRGLEa8pxzzlmdc8451aOPPloqQjKIIPjqrW2FoRWCC09acXDdd6gAmYUXP+GHqOzEBStjRUoldeihhw64BlSUtlL9NgoUYw3233//UumjoVvZssdcSZhYfZdjwgkUBNb0wqS5yCKLDPDXUBiP3awUY3q6J65aUXrgueeeq5jP6ac//Wn1+9//vqySvtRSS1VPPvnkhCc+hEIdlSAhHYjfqHyo3Bx//PFFwYgWBTCucC/eIy6ZkBI/AZWw+ce0BLpQED4OPLSyxiqx5pprlpW7UZh5xnihGwYlCaUYRZq05phvxrQz/XshfUcD00poLJAGLP3iNP1A+Cl3MR2EtK9fJ93uvffekgZYgEArUTM3kqSdKDfI3+Rd6iomx7z99tvL9YhlXer5HBmgsv7www+Xbl7WFkR2xUWvVXxarUOS9jKs0oPCE1vZVHYoBXVISCovLSckKBo0lQqglDz00EOlPxQrChns5ptvLq1EFg3VD/vuu2+10047VaeffnppiV900UUlY+EH3uFe9AOZ9eCDDy7uA5o3lVZ9sUoypCB8qbwRtGROoEXL2itcU3tn0BrfssJFQbrwwgsbSl6swAejFyrFmJ7uW1V6COPPf/7zEmb8jgJiQUdgOFg1QpcFz51wwgnVI488Uv3oRz8qaY61iFXxad1jGaB1Tz5BAUXZ5T3yA3FsevOt8847ryw1cuCBB5Zr+OmJJ55opAPXSDsWDAQrTb592WWXDZhNlXxKRc3z5mvGmBAOBB4TdUbmnXfeCUcfYN6QXkjfThMVTsY4AHFHA4CBnJbdqOwiN8gfxIv5L8YNx7pLHqBVzAzrcUqCJOk0MZ9Rthm3E7uyuGYeHixfxnwO7KmX6DX49re/Xf7+AvK7Cs9QVtCkswyr9AiJjxZLxULfPV1aQIKbkCgadHkBlRWWAfrugYqF/n4qG8x/M800U5nhktY2Fd3uu+9evonyQuua5SUQqCghl1xySXGD63RLUHFSieIeUClTaQLCGMVq3XXXHaCUEEaEK3u+Q6ZbeeWVyzeATIo7mDQ9BwaoYSHgHTI2c4ossMAC5bgVjEee71dLD11PKA6meaz4uYYlhfChbKDYrrPOOsX9RRddtCweiXKLYkO8keaco+jSogLuff7zn6/OPvvs8j7fMs3JT5tssklZk4v8NccccxS3sTLgtq2lAw44oOEeeZIKmPQnvfhNOlbcDDzEDeAZ3sVaCOQbrEA33nhjddVVV5WuF/JKXUjxDfJ4L6RvJ7G8gOlOuCmz5IsIYVeRBJVj4F6zuHEwM+lFI2nuuecu59BqGUuSkUDZRo5suOGGRV6QT6nrlBER8nQs94BsiQp/5L777isNNq3MsXxEmZSMHsMqPSQmAt5zKjaUA5QYWmYoBbTQEVAILSoUTXzMUMuq58BEeAo9Kj27HIBzlkRAqKJUocDgJ86p/FZaaaWSGZnMLGYaKkfOqbCouMxEvGtlSGaLwlcIDwoVlafjFugOQemJ8UF4hHOUJMZ7gBaFoTDe+lXpMb7PPffcYvWga5N0YGyPYDmhiwK3URp4FlBK6AKVqaeeuhF+8hR5B37yk59Up5xySjlG2cRyhEKLSZg0RjExTVBgaIkxrgxhIqSxikkUQJiXyT9813TWmqNgY+Chgw/JyyjUhIOp6R0rJij4UZnuhfTtJLHsEFbyPMopFlfCrPJneQPyTLNKgPd5juejTPFdyi95hwGhWSEko4GKNeM3v/e975XjCPmQ/Fkv1+Rd3o3dVsgFrrO3bkDG0PNAY13FB/fM+8noM6zSAx5r/VCpIWHPP//80nfJGBig64IuKbqnEIzAcyg1JjpjRDAjIhy5hhlQJciuDmHcyBJLLFEUG7o3BDdVSLhH1xoQFsMTKycg43JNIUv3CKZHKkvuHXvssaV7DTjHHcaNEH7fYdwB/mkV465flR7Qz7772GOPlfREQQDGPSEwmJuFcVC4TcVGPGlJI/6w/Dj7LgoIChSQdlgEfY84RtmhC5Ip4YF8QkW52GKLla4trH24Z7pYOZv2XmddHZQ0IR1UtgRFl19QUdBR5nmXje43rJooTsA3Yp7CrV5I39GAsmrYscq5CCyQLqKMAN4hzoaKEyoVFSSOkS2kFzIhupsknQJZxOK3MZ+Svy3bYL2hfKnDs8iAZtBtzlIWDP3QTRuTyejTktKDMFLg2VqOLTG6FRg7wTO33nprEVrLLrtsaY1zDbeoPNjzHhURXR1CJYZVAOGH4oFmrPBEgdpmm23KmidWqMLvhICFhj+K6hmSb3MNd2OGNnNSKeMXoUsDfwMClzEhdpkA11DCqJBbxXjsZqUY09M98dKK0oN/KaBWQJxzjEVOpRZmnnnm0m1JWgDuE5eM4+F9votCwRgq/YDFBUFCejP2yzxG1ybdX5yTb1SWeQ83sSqhGKF44R/di3Gr0kP3KZY58q3PoUihjHHON7BUkdZMnoebQHrhBooVSh5EQeXgfN0cy0pPLOs0MOyyJsymGccqnlC39NTLJvFGPjL+4ru47zeSpNPQ4Dn66KPLMfnWPE3eJF/X8y7n8TrHotwByo1dwo47jffr7iajQ0tKj90GDDLE9LzVVlsV5ebFF1+sdtxxx1JpILQUjrSkY+uafnu6IshMZBAqIiZ74hsIPpQeuiB4HysP3QtUQCghrFyNYoL7VHhUiLiHkqRgpGvCMRm4yR84q6++ejkXK20yNZUXVgQsPWeddVbR6vEXGZQKkq4WKlXGEPGnD3APa9aVV15ZFCHmImkF4xH3+1HpIc3ozqQr8KabbippwdgaupkYf6N7KDykqQKAtCQPoCSqmKAYEW88wzXmtMBih/uMEaGr8Ve/+lUZ14GSC+QvBj3/4Q9/KIrQqquuWt7n21gHrVzJF7hHOpmf6VpjegHyjeORACskg3Bxg/cYrG66oGSh0KGs4S8sfSrgCixN13zH8HczfTuNaUq5oUzQvRiF90iou0N8Ur5Z4ygrhWQ0mGqqqUqes45oN8gEZAYWUqk3CpLRY1ilh3tqq0ClhVLA79vrrbfeX415oFVO5cQgRwUaQpOuEDIV7lGJYNERWuEoF3yTygmtmF+Y119//aL4mEEwD9IVgdJBxQVUygyOvvPOO8t32OhuoY/WyhZsSXKNypsuFdzCwkB4rNjo0sD/DHK+/vrryzXnccCaxNghKv0jjzyypULi97tZKcb0dE86tKL0mIYoI4y9YWAvcWu3FZA/Lr744jIOBgwj6YDC7DdpTdmKAv/Aw8pCfG655ZbVFltsURTLCN9jPBFKrlYfvonCIowD8g8+IK/gPtfIe1iT6L7Sb/whhuKz2267FYFEONnoo6cbFUWJcUUoW2AYwDDE/NXN9O0kMY/TyKF7MU4d0S5Qko074hKFmXyRJJ2EbnIsvzZkoN3KNvma+ofGHEMAoFMKVjI8wyo9QqLFhPK+ygTnVBqMkaFFDzHz0FcfKwStR16LXQdQ14T9DmhRitf4ln7CH/5RJipcHltxRT/y26xhjG7rbqywo0VhKHy3X5Ue4yOmPaAkGueEjV8zESCmK/dMQ7/vnzrc4x3j08GA9fgkDXQv5oeYV1TIcU9MOxQkvst3/BZ77kdFvi7w/KYQ9hiu+K7x2c307SQqvYSPKRywhNbTqR3Y6BDWN3LMWJJ0CuYcw5JsnlZeQDvKsvKBPX+H8Ueo1zpRjpLhGVbpUehFyBT1isHZJxnYHFvcYIWpmzFTeQ2ozMxoCkHGTliJxcrJ+YDi+3W/xnuAP7QUgOMyqMSsVKOy4/gl/IvfeCZWrq2gH7pZKeIH/eGeNG9F6QHi1bjlfY5jPKDMbLbZZhPOPohn78f4FBWPOrjNdRTWmJYeE3fmO47NR2C8ohDXK1AH3kdUnCPxOcNAPEUli2+anzk2PruZvqMB8YBFlK5tMR5GgmlofiE++RYKD/M7JUknwXrsOEQg79Xz5EiI8oCeBepGr7Wj/CQTz7BKD1jBWAlEYsawQrKSsLKqZyKVF92zAiQTxO/Gii+64THwPNdwQ/f1L/fY1xW0SPwe72uNiJaiWEH6DSrW6L/B0H3e61elJ0I8x/gHlAXCZ9yA+SQqN6aLx+A7UbFQGOhXlFLzDO55P7oRFWb3XPM9FFbcQ5GNfopdNT4bLTmRGG7Cx3f1I8djVekxLemeZOmPetqNhHpeokyx8es61p4k6SR02TPEwTzO3jLdDqVEd4Fxp5Qfr9XzfjI6DKv0cC9WSBGvI/xiRQK8h3CMCRsrs1hh8Jzv42YUppxTYfluzESD+asZKC5ac/hevWLjWszk+tvv+S7PeNwKhrGblWJMT/eEq1WlB2WALcY9x8R/vAZax+rXoS5EPCct6ulh2qpwxndVNlFYhlJoAX8Q5nq8xzxbjxvAPzxjeqMERwuS/vWdbqZvpzGOWW2aSURj+WwXxDNxZ/wxmzcVUpJ0EsZpYulBpsT8B+0oy1GmMFaU7+luJ8pRMjzDKj0QryPsh9JQ7XYCElW3B0voZt0MVnh+t/49BKTfwT3O+Q7HVGRWdByroOgPiBaaun94x8rQe74b3fCbw2EYcKsflZ56V1GMOysq3MLao9tay0w39jGejQOej+6RVlaw3PM50iM+B/U8gfs8g58g5lPcYotpi9u6b37j+3Zx1fNFhOfGk9JjGWU8Aj8vEOZW8n6rEGfEn2kHP/zhD3NMT9JxsCiyeHZdntTlzUihzDB2iClYlBHKjmR0aUnpASqLaFlBQPmMFUlUYOIxFYSZiD0ZrO4+7sUxNBAFK8d8P2ZG/cO9untg5sI93eJXe2aUjWGhYvdZ/c3vyswzpCBWMIMVXivor25WivhBf7gnPlpReqSu/JjmQ2F8xTCTflyv+ye6FwWQbgjPmZZYXziO6a878T3uM+kl+D7P8x2vx/DZzQX6Vfdi3sUtj7k/VpUew8iU+vyyDjG9RgLxZXr6Hcocf27W/+JLknZz9dVXlzUe63ImyoB2QJ7mJwCm4hiLMqKfaFnpGQwzC/uo6NQrOpWHmLn8hoqQ78TnoV7h+hz+9rmYSbXu+C0FNO8xcI15hWL46gIct5i7xQmrRoLfwS/9rPQMhuFRETQvgfmhmbWN96K/YhqYlsSZ90Wl172oxMb49RmmQWCeqJiPcJd5l1zrKX6f43qeGwz91830HU2Yi4kZ1cGwm76ce+y+FeqNCKaIiHOaJEknmXLKKcuPONF6W5cvQ6GcQ74pR+rvY/2edtppyzGyYqzLiV5mxEqPqHwwcZl/RZEZPAZa5nVhGJUbMkNs5XOs32KlGq00dcxMZkQzH27zLSexE93luag4MeuyEx6OBOOxm5ViTE/3xGM7lB7SiK5Gl5fAXeLUdDX+Y3ekccCzpi8Y/zEPmN742/d0k3tRuOA2xCUSgIkop5lmmuIu7piuLC/BJHjCPd1oFeOzm+nbaeyuJK5Z/JXZ1/0L0oHgpEVdURyqnIrx7TeAOZdY1iSua5QknYA8yoS7l1566YQrH45LrDeGByPKjFifxaUsmLOM7i3wee8lo8uIlR4SOb6PFYWJB+utN58BnlMpYbJDJoITzpl1V1SSzIjA+1Rg3sNtuzp0F2IGVAAz6y/mTDBTG1bHk+A2YUhLT2swUSSzW0chQVxyThrENAFmdWZiQGEcDcs9xLiJFZ7KEJUu/o/TDkSi0koamv5cN4/xjRlnnLEc40eWNon5JObbeH0weiF9O4kC2vJDo8ZlWIwfnolpbBxE5XUoYpxRppntm8kwk2Q0YMFrliQiH1oHxL93h8JGlw0qQN5YbgDLJfOYsQRPrHPGmqzoF0as9EBUaFhTi2UhuKZQdKV1ZqNktVkqPe6x0WqkK4lrtLxp5blQJRMdmjFQVhhnw3NCxrJ1SYYSxu2AYahXui6OCmRa1nJi1t/XX3+9XCNjYqEarHKdGPRDNyvFmJ7u26X04B4zGLOuFuCu3wCUFwbAsryIczkxyzbdTXSTsNwDS35g+iVtWTpCxYP8gvKJFamu/HLOmCvT3zS3oq0r3eQrIP5dZR0QeKD7kWhFGgzD2s307TSxfAPLxDgTOwprVG6ID+LAyqMVLJ+UO2ZBR+mBWHEkSScgj7FtvvnmpW4ClJZ6nh+KKCdiXYO8o2ywWgBKj+VEWTMWZUU/0BalR8g8tPhdJT0KLQYl0tpm4CgTnK2zzjrlOms2MTiSsTZUcPzWx5ID7PlFloyBZQbTIPMpYCHQfZQr1vnCusS09VSeVJpf/vKXS2VmGLQANMvIvMvK8MwJwjIKLGnhe1GYTyq6RVyMRaWHiop00HJD+Cz4dCuxRhrdSfvss08p+MACsigerHGFlQhhw1TwLA3C8ibAshYoUi5J4mKzLC2BwkQ+Y702lkZgLbdPfvKTZZ0vUNlWGPEe/mLjHnmmng5RWJlPmuWXOr2Qvp3Elil7FRkUHZaCMb6Jg6hkWu5Nh6GIFQaVBA0glv4gHltROpNkJJi/6V5lfUHWlyTvUfZbyX+Wd+oKZUHM9+Rl6jPLThzu0Ur3b9J+Rqz0mGmABKWboj6TKs9w3d+BAUWHZQtQVOKq5VRgWHqEsSDbb799OcYdtOSZZpqp+I/KFKUpdmvwTFxcMmZENsPKO6z3RQUsmNQZYQ/RryPB749VpQdYjwyBEfMC30FZRYm0wKPAoLBSWaKwAIKFZxlnpdWGuIpdnggUlFryAsowa3QhMKxcgTQ3bHyPd4hrN+B5npltttnKvllakEd0pxV8tpvp22mIE7sbtX4+8MADpfHCWnUQlUbTO5bL4SDtv/vd7zbW2ovuJUmnwYLMWm/IJWRjq3nXfIqyJI5Poz7caaedivUSOaEylHm7u4xY6bFSscJjHg9a7IDiQEVFC2666aYr9xigSKsd5eLll18uK6zTuhO6MmjFA5kDCwGWG35hZe0SVuNGUaFSwzrEt+qZCKGrgiS0RGOY6LPFLawPrMiO+1TSVKithr0VdGssKz0on6x4DoTTjTXYiF/SCysaXZ9Y6+jjxrIT4R7pSPzQtcm4G95FCNGdwmrndHcxd0scYE4aq6CS7sYv6W/ehGi1m3766SccfVChx3wSFbdW6IX07STGDfklDjZGCbrkkkuK1U3Fx1YscRLjeyiIbxQeyrZyI0lGC8p/LPMXXHBBkTtca1UWxOdsuDHAH+u340JVotJ62X3aovTEPZWZXRSCFs2vwdEEboWEdk2FqRb80EMPFaVIoXnNNddUa665ZsM/+JV7VDJkKLu6zHj1TMVzusW7hhVoqVKJxrDiJ87Z8+5I0e1uVor4QX+4Jx7apfTQTUXlB1GBQOl59dVXG/FvGj/22GPFMgTeQykG/EWFijXG+HeP28yeSpohXIxL3I3ppeAB3Reem2WWWSacfUA0M9fdHI5eSN9OYnhMVxsUQNgZa0dXF4uRQhwHZ3oPhT8y0BqGWEZbeT9JRoJ5jLrJvM7QCPK0f6QORaxvVP7vuOOOYplmr5vmaeSE34yyMhk9WlJ6OCbx4jWJiU4iLr300kXpobXOQFX2vIdVhV8DASXoiiuuqF544YWyzT777CUzUEExsPVrX/ta0Yx1m7lBrrvuusb3mcqb59mrSWtSZ4wHVgPMjQhnMhjvuQl+4E8ULApUzMA7uFnX8Am77ojXhsN3ulkpxrC7J82j0uMzXCdc9Twh+J97MT9gydlggw1Kl8ddd91VBqCT9nRnMXYLqxppS1cX97HwYW0hjRE2bOQBlCEg3bEKsuSBMO6HAfG4iYVP8Ae/hmIJ4j5+Iv30m+EArzlfhpiW8R3SC9wDz9TT3He6mb7dhvJD+V5rrbVKHlDpNK5ivBFfxBE/LdASRvmloQOxEqjHc5J0iliHme/ogVh55ZWLhZqfZOrlOjbgASs1P8jQQMc6zftJb9KS0lMn3iMzUKEh9KnEtttuuyIAEWYoH+z564pv7LjjjuWcriT678koXGcgMdYepgMn09F9sfHGGxdLDBmSsT9kJJQfRtlrSaIipLskCksyKMIUoVonVoBAC//yyy8vg6Q/+9nPFqF93nnnlXs8S+UZKz2ouzEcxlU3K8WYnu4Jh0oPfppUfxGHDDinZcOgcKYbYPwWfdm4ySBnri233HJFkaFFTxozoJ084KrdF154YWld0b0IVJy77rprNccccxR3UYDoXqELhMHPQLqT9xgXhnKF1TCCYCLeeY5w813O8Rso4IiLeviNp8HgHdz3uW6mbzcx/MQlaUv5Js1IWyyA/DXH35G33HJLUVa5NtVUU5VB6tyLlqFY+bQ6piJJRkocHqFMAGQb4zyRS1/96ldLFyx/qjKLMz/MkN9ZH2633XYrdRN531nEkQ/tGheatJdhlR4qFe5zjkBHuJMxfKeOz/IeuAeUCASbvx03qyBw3+tRCALvO8ldXdNW8QIyK/7g/fgN/F13s47hFt4x7BxH95r5v47udbNSxA/6wz3xQ9obtmbpqV/Z43/T1msxH3CfQq6VzNY+AsU5L6JwAd6P+K55Rre5rhsx/mIeYDyJaYuSE79VD5tTEwDuRTchXsNN/MMef5jHxPjoZvp2G9MNSFPSir/sUHBorDABJA0h/sI76qijytisOig5Nl6Iyyg3kqSTkN8sx+TBZgo39Q6Nd37aYOwnspOxoChBNMSwMmee7Q+GVXqGw4qHjMOxCV9/3y4k8J6VC9/XD/UKCvjtT+paOd+18ozuWElGJYdv4T+ewQ8+a2Wm3+t+0J8SvzMchhX3e1HpieGI4eQ5/NwKMU2suCC6zXEcOxPH3ZhWQFqannZZAt9QWYZm+Sz6XTcgfjdeb5YWXOMZwl6/H78lXutm+nYbGyJQb91itWWKAFZNB/MEg9mBfBDzSbN4T5JOYfllX5eFyjUH6Huf7ljGqDoFByD3rAuRU1F2Jb1Fy0pP/RqZoplmG59D4YiVDAJOLVqztgKO51RQuBZn5AWEqc+6jxUnxExbD1MdrlupE44YFu6R4eMzgh+pRGO4hsLvd7NSxA/6wz3xQ9rXlQDOfQaIlxivPFMPA2kaW/ucq2gQbtxUGVLB8bvcj3EflVTgvbof/RbHPI8bCJroB9At00u/APt6/sU9nonh47kYfuEZ7vVC+naTGN6o8AKTsmHpYZzdnHPOOaBRBFFZlpj+UVlNkk4Q6xDyXpR9wLl5EvmCnKHLHksmYxlPOeWUUvYlNszq8ijpDYZVehBq3K9XBhGEkwKPisCKBWKGIPPwnJkIoVfPGM0EXax01KY1kftd/Mu3eBZ/1is0rkd3xDCxx23XEhL9yrv4LYZnsPiIGI+814tKT4wn7g3nP94zjevxGS02YNrGys304jt8m/jVD97jnHc8B9zWHb+LclX3L+d1ZbgVCHs9PIKbfqceR8ZnN9O325A2lnktPaQh3QC33357iZONNtqo/BVD1yLxbDkG0pm8QhzijnHqPklGA/MfcibKLED2Kx+mnnrqMqYHGKvIH4jkcesG5Y9lIukthlV66nCdxFW4kzkQcHVhjxCz0ooTN0VixqoPaNT8HStJiBVhXWEy09XRz/q7Wdjq71oR19GtZpV+M/wW7/Si0hPDEP3Gc5pouY7/fTfCtaioxvcA9/1GPY4j3GumrOgW6RHTxG/yPfNaXcjg7xg+w8A13TJM9WeBitn7kRgO73NtPCo9g6XpvvvuWwZ5AunCn3sM9ATjqB7fQvm3sZEknYb8OZiCUi/P/DTBDzrke2QIS+E4zxz52fqp3gBMeodhlR4S1nMSkl/M+UOKjdmTORcqH4WV79uis0LTPdFt8BkzWlRwcMfrsauLd63AVILIwHWFKMI7hBk3YqbmOPrHeIn+YGkF/lZimQTXkhoK3epmpRjDFMNG2gvXYwWGUsFfc/x6yV9RbHRTRIWmLihi6x33SAPDq5LCNb/D3vwSr5mexn9Ujv1GjEfv8w2uew93oh9xWzfrlSrX9QPgJr/Cs8YU0yWQz6NbumN88u54tfQQF8Yf6UMjhzEPxBfxY5wwnYWrWXON541T3h+qzCZJJyDfWYYBuRDPwbKOPGFKE/48jXn13HPPLX+d+lyzgdBJ7zCs0gNqrUceeWSZ44QBXGi7TCrGEhEIL5/32boiEq0BEDNXHPxohomaMv6zYsO9eA+hqeD0m3X4Trynn9gbdhSb+IwC24qQczI8y2fQp8ucQ8wNg+YPsS/XijnGC8e9qPR4DvGY34w/8YlPFPPtwgsvXJYGYaoBMQ7jO2A6EV42wxsFgXGOkhsVFhUq3TQNwHTQHd2AqMBw7DO8Y5pyPT4H3ot5wO+h1PMb6p577lksFnPNNVeZKDPmVdI5+m+8Kj2xDLJnwVB+64WYTszgzG+/5p2oJCdJL2M55/d1ZAOYt5Fh/MnFEiqW/9g4HIy6PEpGh2GVHioGEpI9Sg9zpkQQXAg6JwNkb2XCbK2sXo4JEHiOzMC4GVrQTFxIaxqYg4VJ6yC+X7eyHHPMMaUrjOfxIxPhwU033VTmemFSPMEdJiC86KKLyt9j+M8J8AT/0CcLPI9lg/jQDxCVrMgPf/jD8leKcYX7HtfjtJuVIn7QH9F/pL3gr1jpE2/1mYu1xDEHEs8zrsoxGliBmKOCNIhxB6yyzmSUrLnlIpVWfGD86j4KEFbEs846q0x2p59QZlA6sLqcc845RcioDAHHpJ8TWaqI8neR38M9QFARRr6Jf00vUBjFcDBPkOu08R39qt/Gs9JD3BlnpBmKDZBexqvd18gPJnFTSUqSXsbyjWykbuNPxNjTAMgS8jeNYP70irIEucA5G/Ik8333GVbpiTARIP2XJLAVAkoPgo6ZKBdbbLGycCTTcTOnAQKOeQywBrk2E5UkK2yznACTEn7pS18qcxwA63GhCOEfKkK+pZLCZGfM+ou1heeciRkLBJYIvsEkg2RK4O8vJo1CA0dZY1Alv88yoBITuxUtAvqXv/xlOUb5YZLC3/72t+U8auJkcn/NVXnDCoKSxb16HGrZ8ryblWJMT/f417SP14BzurOYkMtrVvIUcJaIIG2ZhJA4J66ZbI5uPxYEpRuD54kDzL6bbbZZsY4x4ST5ADexnpA3gDzE/C0uL4HiRNzyDhMJku7kNwbFkndQPlgVn3QnbYHfSFmzjblgcBv/oGgx4aSCBiWHPApcQ6kj72ptgmiRJM24R3yQ77bYYosi/HwePxl341npURYwDo+8QdnyGqBwmo+OPfbYxgSUSdIvUK7pxtpkk00a52LD/NZbbx2wjmQzSybvIXuUG8noM6zSg/CywmPxTwQ7lQvLN7BcBM/tvffeRemJMEMvFYFQ2WCVoeI7//zzi2AkA5BJnEmX1dOdvpvvUvGhBFGpUnkJShLLFuBvFCAsOUKXBOZHup1UgABFjZYns8K6HAZjVqi4uW5FRsUKZlgtBDGTUonTzUd8iGElQ6MsxbiEXlV68E/dT5yz7gwz57J+FhUZ8XTbbbeV+/POO2+x2OgWacjfDMQVAoB4wZJHJYhiQXwQ/6QlaUrakgdQeuwuYuArE3/xbRRVLQO4x3TwPIdSStcqz5B/WNKCfAYoJKyar9LCffyD/3mXPLzDDjuUZ3if9MZiROuNcEQBhf9i3kVRn3LKKYulEXi/ni/Gq9JjPABpQxeglQBxw2accJ10Ic0ow7FRkSS9io0m1oRkFvGIdaNKPjKNMT9RftRB9qbi0z2GVXoijG+gpR5XW4YTTzyxbEBlQtcEChF9+yw9wF8bvIeSwXW7GICMZPcXs7airCgkmduDypVlJ1ByULaoELHqMP8HYOnB2kJlx3t8E0sNVgOWJjDDRrBGAQpQXMcJyLz2xyq83ZORFfK4SyXKrLOxosMfZnieNR67WSnG9HSv0iP4L1ZCpCFKKKAUxooMZQi8Rj83yicWGa05hx56aLEMsgSFUNHNP//85RhFGWsgEOcsHMvMpqQlCjX5guVEsCSRZ7Aeco8lDoS8QvrjD/yqAhXBErTzzjuXY/Ihla4QZsIWsSwA3WMoOijsDFyPaZdKz4cQZ1hLbZgQB1YC7kkj8wtpQtdwkvQDlHFkC4siI/cp61FOgF3p3GcQv8sg8W6z57mu7EhGl2GVHitChBdaLF0XQuuYBKWrCkFmBcIMylpi1IR5Dmh5M3aHsTwIQSpIrAQcUyndfffd5TnG/aAw0b2FQKUyBb6Bm7iNm1S4LliIXxlgTeWIJYHF4giHwhbrAe+gRKE4UQFbCXI9VlhxIJp+N04ch0R8oIhJ7BoR38GNXlV6vK/fOCZNUCRIYxVHrhMOF+zkHCUXRQTlwHjCbd5hXTMGAAPxSdpaMaJAY9nhHdIHJQkFknFcKlugn3AT5Vhll/zoCt34Awsf6W4lq+UOBZ08h3K79dZbl2tSNz/zDcA/uInVkYHrdJMZB+YLn+U56Gb6dhvKKooq8RkVZ+LE+PA68cZfjzRompWXJOlFLrjggkZvBnk4WjiVBYznQXYgcygPsQ6R8Sgfeo1hlR7hGWahxBqDALMSAFa+pq+eayoYVG605q1YGEdDJUKrm/E5QHcHY3qwAAFWHCw0wEJvjN9gfg++zSAxBq8K43OAd6j8nCocJcg/qlBq6AIBFoej6wo/Yj369Kc/XbpEELyGn+t0iTk4OoKidd9995VV4IE4WHzxxRvjgahkY5wYD71QKcb0dE+YTXvDL4SDLsdoVaGQq8CiyESLCUov4zRs7aCc3HDDDUX5RYFB2SF9UGroJgPGZNHaJz7IByi85C8g7zDey0qTgckotgycZmyWXV/4EUsPMKAcy5v36GLjXcJCHplvvvlKNynppN+5zqK1CjCElXFB/zwVM+4yszBKnX9tmM643wvp200IL+McUAxVYoiLmKeicmN8uQ5XkvQDyCTqJCB/C/m8bi1G2bnsssvKeMQoJyG+O95kRa/QktKj4sKfU9tuu20j4RRuDDylpS62shn7wngP+vAZfIoigLJAZkBrZsX05Zdfvowf4Xu01Gm5YyVCKNK1QbcGUOEgXGnRM4iW+7jHQOS4gCTP4A6gxNDFRYVKtxcKkOHiO3fccUc5NvNRSWO5cewGcM/7VH6EBz9gUXIwdRTw0XqA1cHvEVe9qPTE8HENf7IRF8SZyo7PUOHT7QS4ZdjpxyaeiVcUY5RVYHVt0h9lBYU3WgoRJMQl37E7DHCXFdZRkHgXCw1xicLJsz7DH3n+UcV93KCbDQWZgcfmU4SVyjoYB1gSGXwtKjOECQUMhYowYV0iX+CG4TWP61Y307ebkL6UZeLBOIGo6BBnxhPxQzyjIE8zzTTlWpL0Msh0uthpNFHOzefkY/O1siU2iJB5TP0R16bzPow3WdErtKT0dBKsJf6hhaC01W2F1S5URtijDPHnz2hkOuOxm5ViTE/3pDlp32mMd77LOCGUCFFQdBqUF76NwLFrFNyPhF5I305jOlkmiTcFPhY0rZ92LRqvWjtBYe8zWORo9GARBMu98RmVpiTpJFERAfIv+dCyzNQY/EwB5u2o4IP5FniPvI/Fh3oGpSfKOstA0h26rvRgmcEqUK8sEIL1zDgpGDawj5WWKd1So1FBGY/jVekBwkwlxgB2uqDsJhsNUHa22mqr0kqLEA/RKjep9EL6jhaWH8OMxRaLmOVUpUgFhrioW9d8BuguZtCncA+3TJd2lP8kaRVkYr38co3pMbQIN8uT5G3zt5CXKQdYelyN3UaAZSCWhWT06LrSE/tDyVD4hcygn0aK4eDXZIndYZ3G7xOm8ar0xFZRNPVGS0AnoatOCD9pYMU8UnohfTsJ4YtlkVYqZZZxc1hpLb+E27iIyqTvKuA5j1YcujCpGIw37vvOaFkCk/GLeRaQCbH8kg+RUYxLVIZERaXVss4wDabwUN75Xlp8ukPXlR6JmUn/tAMyWKxco0Cumyg7gfE4npWeukXF1tJot+Q7YWLuhfTtJDGNYhnljzi6iSWmsXEby3F9vI/xhMLD9AT1Mt8upTRJhiLKgZi/uU4eZUJTfojh2DzKc5QLy/5QUPfwLmMN+cHDd2IjPBlduq70kHmiEIy0S/Dhtu4TLjJcs+91AuNxPCs9gMJhxTea3VsIHcLaLC+1Q+nqhfTtNPyBQviUE/xE4N+Txm2sPHwuXosNDzCeeJbJLhkXRP7genwvSToJ+Y88Z54FrwFTa/BncoQyH5+PRFkLPsdEqEx/QVlRDo5FWdEPdF3pqaNm3G7qYzpGC+NxvCo9g3VR4I9uxAX5q50Wvl5I305iV5QTPzJGCuFNeAHFMVYAXDcO2Md7xlWEtGAOFP70hPjMWIvLpDdBRmm5iQ0hzpk2JXaPD6eQm+dj3rULmClX+JtYMn93h64rPWQIM1w9EyhYRwIZWnfRsj1GmLfD/eEwHrtZKcb0dD9aSo/h5bvEP+nB8WjEPTD4tm5lQHAZDyNFd7qZvp2knk6MwWHB0MHC6fVm97lG3LP3Pu4Th8z9xKSF4nxLSdJpohU4NoiYJsWuLUGWqBghQ+tyhHOej9dVqoBpMq6++upyPFoyMBlI15Ue4XsxE7Tz+yhW7WzdTwyGo5uVYkxP96Ol9ICtoxj2dqZvqzh5IrTr+7rTzfTtNKYfk0sys7Xn7slLhDuW32jhY7xPXcZEuEY3Au4nyWgT86qWTRpLLK3kOlrRAuTzXDdfR2Iep1z4PHtkEAq+i2wno89kn/rUpxpjLEwsW1n1FnIyaVBgiMuoYI5m3FqQ+XZsqYyW0jPW6Xb6jgT9a55QkUGgR+WGWdNZud7f1psJ+5GA+8yGHudRipVRknQS8zqQB6kLWXOPZXHirMqUCxs2E9PAsdFNOWOKFpcvsjzFBgPUf/5I2sf/L6cnq7785S8Xgc02xRRTlP1HPvKRxrXcJn2bfPLJy/7zn/98WanbAlTP5J2EAkdhi5UIy0Kw8Grdv7lN3NYL6TtSFPjRGlpv+DC3FUtzABUCikm7w8jM2y5FkiSjQczD8ZjZ3plDCqUkWm4irSo9lC+etdwgi1nehvUfIZY7GqiOAUo6Q2nqR62S/k0Sf2K02GRwLDBkfJUO4tt47jQxbS1c9mHnuImR0+30bRdaVwiPSpDCF0WE5WcAueCz7kdCrFBYg40lRCCtPMloEPNwzHOnnXZaY5FrqdeLWkdbhQaEZYsfAzbaaKPq5ptvblyzLPSLlbhfKUqPlSCRH015JCoJkdukb3YtCdesDI33ThILpoWJgm4Br/s3t4nbup2+I0Uhrl9jfkEesA4dc4zw9yP5xq7wdig8oDv6gzl7WKAWf7TrG0kyFPV8Rr4nz7PWopAfkZ+xfLTSqInPW8aUw0zwydqCnFuubKTidnw3aR+NQR0I76jpEuGtJGoyPFhYiEvjEwHPcb3C7BQWICpkYUBdNKsmk06303ek6G8FLvnEsQbrr79+df7555djwqVy4v12EOUOFc2qq65a8qvfSpJOotKjfOQXdWZhhigzyY/xvFXI35Qx3+VYxYflLVw0mef82aJfZEc/MhljO+qgkSpwyBC5TfpWhwqSuB3NTB0rDyorKzlo5ufcWt/qdCN9R4otSvOF3Z78vUK3FuFRSEcFRbP8SIhxaD5lkca77rqrHCdJJ4my0Tx+zTXXVGuttVY5jvdlYhUfZQHvxfJjedtwww2riy66aEBZSKWnczQsPSg6CDsS3kTNiB85dBdSqdhy1cQZjzsNhYnvWYA5J42dcC6ZdHohfUeCeaI+9osW59JLL11mko1ghldwN1P6Jha/r+IFWJYY75Akncb8B+Rr8vQGG2xQXXfddaUu5H5dyeFas+vN4DnLCe7XBykjI1B+Zp999sY8VVrg21G+kr9mwJgeiMKHxDCBc5u0DWLm5Zot5FjRdApbE+z9rteg7t/cJm6DbqZvO7GlC3RrnXnmmeUY4U6Yopxop0JnPMX4mnrqqXMuk2RUiHUeZYD5tsByTZmeVAUkWkNjPo9ljeNnnnmmTAkhI/lmMjQNS0+SJOMPFBqVNwQ05/fff3+x8owWsdIRxjr8+Mc/blQOsZLoV6Uy6T1ULMxTt912W5mewTIxGlDmaIjus88+jQk69ZdlI1qIvNas3CTDk0pPkoxjVHoU8nTX8ds4gzlHQ6jyfahXPu+9915Zyd0B0/iPe+zjuIgkGSkoHOZDLJwXX3xxIx92mqjMw3zzzdeYD6sZ+IthJ1kGJp1UepIkaXRXsRzE4YcfPqoTpNnSBYS6Yxq+//3vV0cddVQ55n7slk3Tf9IuyFfmfyYYJe+PZv5SsWePsj/vvPOWcxodUSl66623Jhx9MM/PaFqjxhKp9CTJOAehj5BnckCm3heVj05THx/EOYoQg6mZFZc5gupkSzdpB1p4GKD/xBNPDMj/o6FUqMir3KD0X3XVVdXqq69ezmMZ5J7+beeYuvFGKj1JMo5R2NKqXGSRRapHHnmknCtcO00U3lHAO5UGv8w7oBoYxxMtPkkyEmJeYlkIZmIeTYUiWpRQarSw7rDDDtURRxxRjimjltP4B1iO6Zk0UulJknEO43gOPfTQ0rUFVgSjofj4DYV6rHCoBJgRmta31xH6CnvuJ8lI0aLz1a9+tSx8S54cra4j8z/jdJyVmbxOGVx88cWrhx9+uFwjr1tGJJX/SSOVniQZx2BdYXFFBlDagkTgj/Z4gdh6rXdnrbHGGtUFF1ww4ezDSmo0W+TJ2AWF4tFHHy1KRl2x6DTNvmfXLQOa+ZPs/fffL+c8i5LEPtdNnHRS6UmScQzm9SWXXLL67W9/W86pABCsozWQk9aqSowWHIU+Sg1+uf3224viI/oxSdoBefDAAw+sDjnkkHIe899oQF7GD07BELut9tprrzKY34aA1h3KjP5MJo5UepKkj1FAKjARhHUrjc9ERQELD88h7Pfbb79GazLOwq71pdvgfxSzX//61xOufKCsjZZilowN6uUA5dmyQv5ioVvv9ZJSveKKK5b5g+rgR8JkuNwbpiwfzUmlJ0n6GAWdrT4EOdAiZKO1GoUi43d8BkVp9913b5jYXewQemUJGiufBx54oLr22muL/6Gu2CVJM6j4o0XE38MtA/D2229XRx999AAlgfE1vZDH8ANdWZtuumk5pqzyWztoibJ8e641KGlOKj1J0scoqBGICD8FHgIwmsKjIFRIIvhRJsTKgb3P9BJWVAh+B30myVCY76PiI/whWFcQ4liZXrCUqKTxV2X0a31MD3618UI56SVLVa+RSk+S9DEIN1ukCD6PVVqw5sTrnHvPigABqgUFvG6XWTdR6OMX/OV5s0osSepExWU46w0NhWgB6hUMg93NKjeUY8sD6HefT8WnOan0JEmfo1lborC77777qp133rnaddddq2uuuaZcs8UYLT6AsIzdWrHC6CYoOPqRmWjh5JNPbhwnyVC4bIMKz2uvvVZtuOGG1Xe/+90yL0+9K5fy1Ct5H/B7MyX/rrvuKptQrqO/s2HQnFR6kqTPqSs9KjNPP/10mXvkjjvuqK644opqhhlmKL+noxQ5+R/vqiRx7ASBvdLiRYhHQc5EhYxv+MpXvjLhSpIMTr1sYO1ZZ511qrPPPrvMAbXyyitXV1999YS7HygOvWbtsUxSDvAfY3qOPPLIas4556xOOOGEhn+5FxWdVHqak0pPkvQ5UTFAgVGJ4a8sLCL+7soEhHvssUfD0qPiYxdYnWbXRhtN+rZiUdpYLmOJJZYYYNpPkmaoELBnoyEwxxxzNKw5NAiWXnrp6s033yzPiV1I3cayClqqKBMsCLzjjjuWVdmjYhef74Xy24uk0pMkYwBbdVHQLbrooqV7C7D+3H///UXAew4qSCg+ClUEvtd7gTjeyAHMU0wxRdknyXCQ1y0XBxxwQHXQQQcNsIJMM800E46qokz0Glh69H8cwH/YYYdVxxxzTCm3sbzybC+V314jlZ4k6XPi2JzY6mPukccff7zR+qOVy5wfKhG+18vEQZu22hHqs8wySzmGZkKeikAlLknIHygMxx13XLF4mpdQ9qeffvpyHPNLLwziF/K+ZZi8bvlFgdt///3Lsb+xS69YqnqRVHqSpM9RQCPoFNy0DpdddtnqhhtuKOcoQ3feeWe18MILl3Pol+4hwhLDCCybodJGmKkMrByylZsIg5Rjlw/dQTvttNOEsw+YddZZy5585KBmlKJeyUf4i7yNf7BQ6S9mamZsDxBG8z9lIYY5GUgqPUnS59hqVdAhJFES9t1332L+1pSPkGSq/V6ZaXlSUNGJlh5B2PdSZZX0BioyKP5YPr/1rW81JuK87rrrqpVWWmlAYwF6JQ+R3/Wb45CAMFGWUeIsz9yjrPuM7yUDSaUnSfqYZsLZLq4XXnihmm222aqrrrqqDNhEUWAVaRWHfiD+Tky4+OOGgczzzDNP9dxzz5Xf1mMcREFvPCTjF5R/GwN//OMfyzl/bJ166qnVU089Va299tplMdtYJrQm2pjoJnTJNbPaMFkhPyrQsHEl9joqcMlAUulJkj6GVp0VvcLRriBgxuXtttuumPSvvPLKCVc/oF9WarYbjkrowgsvrI499thql112KUsHoMRxH8WHeIhKTy9UWkl3sUxEBZjByrvttlu13nrrVeedd17DMmJ+8TwOGu4FCAt+evnll6szzjijLEbK35inn3569e677zbG+qSlc2hS6UmSPgchbX8+KPTYx/W0IvGPqF4ntlhphWv9IcyxJYzCY4UFKfwT8gablpw33nij7KNCHK08Ma9FBbpb0F2F/+oKfPz7LB6D1q0YruRDUulJkj6nmXCmwo/CkJZu/KMD5aAflAL9iBC3tc4x15tZcrjeD+FKRo/3339/wtFALDfxzyfKCPmrFxSeCMoY+VqFJpZlygVlnX39XvLXpNKTJH0Mrblo3RhM4CEMAeGoUtAvykHsmmim6BB+w5ckEfML5cSywoZSE/M/12wksO+V/KSfDEdUxmK+b6akxXKTfEgqPUkyRoh/ZSnYxwuEV6wI+qkLL+ksKDxRySGP9IvSPxRRsXGMHuU+locYTo7Hk1xoRio9SdLHYPaOAg5uvPHG6rbbbptwNvahe4Lf8cFB3L02CDXpDlb4Kgevv/56WWQUxsqYF/5g1BKEZYi/NW+//fZyDi5Dg6IXy0X84WE8kUpPkvQxmr9RfNhYm4rlJxBodWVoLEIY+XuLv9NYVNXKLX/XTYD8QWWv9e/444+vdt1113Js2elnYhlH+bF7m6kq+K1dVHzE+BiPpNKTJH0OLVYFOEtPMAvzWGnFDoctXNYYY5bmaMofL3GQDE1UDGgQaAUdK40Cuqtivseaw2/5Cy20UOniVcExvJyPBYVvUkmlJ0n6HCv3c889t9pmm23KMYwXa4fCnMVU77333nI83sctJH8Nv6vPPPPMY87KYZdVfVmZU045pcxHhELEhvXXcjGeGwSp9CRJn4NJm/l4vvGNbxQTN4wnoebYBJYUYIZdSCtPAlbyKDrMvLztttuOybEsNnD8mQFLDmHfeOONy6Sk8a9HFKC09CRJ0pc4Ud8aa6xRBjDapx+XbxjLKOxRchDmiy22WPXYY4+Va2ntSWKXzlprrVW6trSMjJXuLbHs29VF/memZhpD3LM8qPT5/HgjlZ4k6XNOPPHEaocddhgwJ4mCb6xjV4VK3kEHHVT99Kc/TYUn+SumnHLKARMVjgVrh4pLvcsuhu3Xv/516fqtd3+NNaWvVVLpSZIeJ1ptPLblhnCba665qhdffLFcj4y1sQvNiModxwhyxm2gABJHtGpVBomP8RAnyV9z2WWXVd/5znfKMflkvCjFKjb83ciadZYFyka97AgyJXaHjTVS6UmSHsaxKQglVomGqAStueaa1cUXX1yOeTZW6uNlRtYYR2wHHHBAEfLNiJVdWoPGB5SJ9ddfv7rooovKuRX6eCgfWnxQclZfffUy0D+GG6WI8mMZioxVxSeVniTpYajEm5mhEeSXXHJJo/UKcYDmeLJo1Gde5i+deeaZpzF2g7iwJUtcjqe4ST4Y9zXttNM28omKQLOKfixiOXjyySereeedd4C1R2gAUDairEmlJ0mSUUdrRLTuILQR5AsssECZYRZsvVm5+xfXeEChHmFsz89+9rNyTJxEa9B4qeySD8rNo48+Wi211FITrnyQB8biH1zNMK8znodjuvm23HLLhpyAqOggR8Z6+UilJ0l6GAWSSo/KzY9//OPqiCOOKMf8ri4+hzUjCrPxgAoNYX/hhRfKXytxPTIxXmzxJ2ObH/zgB9UvfvGLARY+16kaDygTbEDR1YeVGLDm0ICKXb2Uj7EsO1LpSZIeBmEUK2cEGP3yK6ywQrnnJlHZGavm6YhhJ8yxUkPZ+e53v1tdffXVE6582OVnKzctPuODr33ta2V5FhhvaW+et7HEOd18WInjMhV1RWcsy45UepKkh1H4KLwwyy+88MLV008/PaCSr/fPjzeIpyi0URQffPDBat111238pmyLN5r2k7HNww8/XC2yyCKNMjFYt85YhrIQlRgsw5QN5vby5wiIv7SPZStoKj1J0gcgkBDcRx55ZLX33ns3BHZdONmdg0I0Xip3W7FWbLFLa4YZZqjeeuutcuw4Dp4bj4rheIQ5mw488MByHCv+8ZL+Mcx0Y6n4Iz8OPvjg6rjjjmt09TnRJ4zlMU+p9CRJl9FKgyCO1huh0kaBef7558skY1ouxstgzJFw/fXXlz/ciD8VRJSkWBkk/Qvp2sziadn4yle+0hjzRkVvY8HKf7zDAO/f/OY3RfbUG1JjtYyk0pMkXSa2sABBXv8NG7BaPPTQQ+U4ziybDA6VH7+vO6YjKpg5pqf/UeGhzLAJFfjLL79cuoL//Oc/T7j6oYUnGwwf8Nxzz1VLLLHEAAuxys9YLR+p9CRJl1EQu4f6GJ399tuv2n///cs5SlIU8MnQHHPMMU0nK0xrT/9jxUxaqgC5ZwbiPfbYY4CCM9atGJPCCSecUJaxMZ6IUxWfsUgqPUnSRVR0UGIYtxOFDcdszzzzTLX44ouXbpmoGI3lwYbtghYscTvHHHNUb775ZrmWFd7YwfIQK2rKBcdLLrlk6bqJ0K0Vy9B4RwWR1dgvvPDCcmw8pqUnSZK2ExWXaL3h2AG6rA594403FgGlkKLiVjglQ0Mlx+BvBoH7h0paysYmVtSMg5tpppkG/KoNnkPmgYHxMd1005VV2WEsd5+n0pMkXQblJVp8ojn+lFNOqTbccMOG0IZmMxAng4Ngd3yHg1pjfCb9TUxLK/HLL7+8zNMElKm6da/ZtfGKf28xczXLVMBYblCl0pMkXQYBowCOlh/m4kEIKaAVRO6zpTo8tvypGDfbbLMyDT9xPFZN9+MNGguxHFg2mJ/p5ptvLuekdb2sUJ6ym+tDVHwOPfTQ8os/5WWsKoWp9CRJF6kLXgUNf5xsvvnm5Zdr/+RCeNuqjWbpZGiMq8cff7yaa665ynEqPWMDlZyo/DDQ/3Of+9xfWfMsa1zP8XAfQJxZFvx5gr+57rjjjnI8FkmlJ0lGAQVLFMQIGYW20HWFILrlllsGrKCeTBookVHB2WCDDYoFIP4dp1JEpRi7FvO35v4gli0GKlN21llnnVK2ojIEPMPzdcvPeIb8HxtfL730UukKVhaBXeo8h8JYVyj7iVR6kqSD1JUahAiCI/52jlUnChH+OJpqqqkGzCycjAyUH7ZrrrmmWmmllco1FB//7oKYBmkJ6A9UXqMSy/IKLDAKlD+2upJDGYwV/XglKvzkeeOEbuD11luvnGtpfu+998q+30mlJ0lGAZUfW6V2Y0VhTaVLJUy31kUXXfRXgjqZeJz40fiGOeecs6w9JFgHfI50Ig2oDOoKa9KbUE5iA4JJPCGWrTo838/WinYR83hd0d96662rq666qqEgGsccU56aTaDaD6TSkySjAAIWYREFLQOVuQZcRwAx4/Kqq66aFW4HUOG88soryzQAQMVIXLPEh4qP2ApOehdm2v7Tn/5UjqmUmdphxRVXbGol5X6Wq7/GJTlsGLhncPNss81W/nwElCLi9fXXXy/n/UoqPUnSQYZqTa699tpl3I7dW/SbzzLLLKVPHf7yl7+UfTIyENRWdghyFM255567VJhnnHFGGdz8rW99q9xnHM9rr71WjlVIk97lggsuqCabbLIyx8wPf/jD6tvf/naZj0nqkxHa+Eg+AEVQi1hU8m0AsEr9YostVmQT0z1sscUWxZJGvPZrF3AqPUnSQeoCVxAgf/M3f1MENosiMnPsbrvtVp1++umNCfSSkUP8x64tBfVWW21VTTnllNVnPvOZ6pOf/GRRfLIy7D+uu+66Mv6NchS32WefvQxmRrFtZvUBu2uSD+MijutR8TnooIOq73//+0XZ+dSnPlV95CMfqS699NJyrx9JpSdJRgErXyvdm266qQgQBPSXvvSlskeooAzFv42SkWNLFmvP1VdfXU099dQNhdONitNnbPHWu7uS3gOlh/T79Kc/XX5Tp0L+2Mc+Vq5NM800ZWbmwcb2DGWFHW9oCWVvdxdyiK5DrKGWE+KZ+F155ZXLM/1IKj1J0kHqrUkr1F133bX6xCc+0ah8P/vZz5b9sssuW7344oulmyVboiNHKw+zzc4444wN4f35z3++7Kkksfhw/Morr5RnoV9N9+ONN954o5GmbFruOD7ppJMGKDaUp3ielr2B+TwuPYF1DBm0/PLLN+IWhcfjv/3bv63eeeedCU/3F6n0JMkoYGuT1hPbN77xjSI8FNAKEvYIl7E8OdhoYgsWIb7jjjsOsPAQ956zv+2228qzVIZpBegPqHhNzy984QtlT/lhgdlMw+GxfNQbWPfff3/pdtdqxkYDQcUHKzWzN/s+aKHWQtqrFutUepKkgyB4FQy2LN9+++2GEGH/9a9/vSFYPv7xj5c+dMi/h9oD1h7jfqONNirx/MUvfrER5yg8xDtmfCtK4j4rzd6HdCUNrYy12jHPTNI6yikVFpQg/nKk652yYYOMbYoppij7pZdeujGBZzNZNVi3YrdJpSdJOkxs8SBMzj333IYAocX00Y9+tBwjsJktGAGSCk97iPHIMfH/gx/8oBH/xD1jQTimy9EWb7/OQTIeoUuL9LMR4XQESevYMEP5id1+/O3Iwq2TTz75AKs0ihD7Z599dsKTH6AS1Mvdw6n0JEmHwdJgCwrhwm+1/nGioOZX9boAScWnfZAG0YTP4qNaBxDo7FmigmfYchBzf0AF7VgtxshRnphzCWLXS9Ic4o94ig0zzlFajD+6hpn/iIHhxLN7ur5cyV6rjgqTg6F7kVR6kqTDIAjsYmHP2IPYV86yCLSQEBwKjaR92OpUwNtttd122zXSACvbkksuWe6p8ORg5v6A39O11u21114TrvZu90ovglyK8WXeV/FhzzIUTKthmUHBnHbaacuzbLghHOeYniQZh8SKk98/H3nkkYbQ+PKXv1xts802E+4OXOAy5+ppD1rLFMixBcqEawhxuxcZqwCmWbQMJb3LoosuWrpbZp555jLRp+XICjsZnBhHKD2WE6/HRhgNAsrE9ddfP2AcIlYg4ZleVzZT6UmSDhIrTiwIjBtBUDAZ3s9+9rNyXSFRFxax5ZRMOn/4wx/KPgp40wXFh5l87Wak0kz6C7olGRvHQHRA6elVK0OvQTxp+QSPUfwpLyg9lJV6dxVlinJDmZlvvvkGNNJ6XW6l0pMkHQYB4sDYWWedtczJc/fdd5dzZ4u1EsYyMdgMssnEo6ITFUoEPfGtcCa+d9555yLA77vvvnIN4R8rg6Q3IR2ZLXjBBRccMA4rKrjJ0KjQoOBo2SFelUmx7FBWjFve48cLrD78kcq70Vrdq8pPKj1Jz2Phca8CwezFwxELL5UYx1ZmUUh6jZa/2DXSrPLTTVtCYLdIVFq4pyB56qmnSqvoj3/8YxEcuE+YvB8FRl3xiUKc56Mgivd4r+5f3NVvQ8UZyoBu+Xw70C3cbtYCx8/GgX6PFpd6eHAvClTjgueMN56pfy+2RmM6u8YZLdef//znA9Izxq3v1931Ga6Zp2I811vJ+h3/Eu4Y1xw3iyPgut+K77QD3Cbchp19Pd4Hw+dino3x1syv8RrP+t243hzpShnxHn8SidfggAMOKJNP1uPGPBXzCsRyJjzje3X/Kgf8pue6PxTmzeh+BD/HuIppz88NcewfG4PusUqy2S2rlZJnHZTv/FOcc92/rXTP2eB9hkHgnjvAn2fjH1tscZ4rB45zHH9pd9oA/eLmhKBsjsFii9/wd3i2+jQE8Vo9Xggf94wTw8O5x+znmWeeVHqS3kfBURcOK6ywQiPTD7Y50zEFi19bKYgUkFgALfQUYCc4Y/NXWO5TeLgfC1ssuLipAOCbFmTf5RiB4TNsCJ64bpCCqX7OO2y4hRu8hz8szGx+w+9G4USYeJZ78TpbFH5RuOCvOeecc0JsTzq4EcMYv+G3iS+FnUtyeE44Y5yxxdmU4z3CZzx43Tg03nzWjXd4VmHKxlgr9vW4ql+L3yYv8K26MGZjsCd785Np5L6e5wiD7nQ6faIiGBVpJ89sZTOOyWPGv+Uu5mnued97Mb7I34Q3xnG8z7vei3HGxoKjHhM38TtsMR75jsfxOePec7dYzs0nPBfTf7DNvIobCyywQIlblKeoAKE8RaXfY8oAz3KO7GPvuVsdFLIoJz2O1yB+33RXmYtKenyOvKJSH/MKxHd8pv7NuvIvUbmOz3DcLIz4Q3+piKq0822+q/JomAClvKTlhPMk6VliS83MTmFAmAwHhcCCY+GiQMSWvm66t6DEVhdQmGJhZ2AycJ13m1kP/CbPKAzc+x2FA8/qh2ZQ2BEEPMc7Fniw8oqFPApGvukzUZDoBvvo/3fffbcI9ZGCG7glfCN+U7Ts4Mfo5xge45nNeI3pgXteB+MyXhPzlM8YduIXd7huurQCfq3P7eM3CAPu1wWx4Yz5m3v6CWJcdSJ96uAn8i4t94lBfxIPHhMu455rHLN5n+NmYSWeLCPGGc8aX6SL7or3iD+2aM3x2fiO3zX/mNb1pRX0E8Tvtpo/dJ/8jcJEGtYVBtypyxriDvkWv98M8isbbsZ8FP0X40ILpO8B367HA2hZY6//cMv3LLP6kXejNQ6IL+83szJzn/f4fvQn/ueeZQXq8QYx/8T75AfzBH73uaKMlqMk6XFiAbbQ0VKmQA21CQUgVkq6EeEb8RkLHIUmCky7Y6L74DndV4DgtuCJz1jAFe4Quwe8rh/q4RHu+w39jttRgMRjQQDxjSjkeI5rPk8rdaToRt1t4NtRUHtMOKNA5noMv2E2bhBoHkuzdISYjrzXLE59Bj9E/+l33+E8um1cKrBNl/hN8wbonspMzCt8A7c7nT7At4hnKzagcuD73BtqAxRV3uW8rvj5zGDpLISTeIoVF+XB7/iOirvEtIrlR8xHxK3xS/pE/1jWYvrxTd0zviHGEd/Wf4NtMT7qjTT9wz7mEeAazze7jruDwfNsg/m5GTEP4369nEIMR/QT8ThYXPpd4jPiud+t+6+u3NTjwPf1I0p6LCcoY83kO98rlroJ50nS00SBZiFppaWLkKwXYM6Zc+L4448vA1effvrpARYGqFtqKPSxIHndAooSoUDir6z4LJWaFZt+4X3d4B38ovBo1qKJBZ9C/eSTT1a/+93vyjgh/qT49a9/Xe4pEC+++OIy83O0siAYbIlFQYSfovsKuLqQnhR0oy40jYdYmRn/pC/hYP2xc845p3rmmWcGxJ/v4I7HxrfhMI8oDHkOocc3HnjggcY6W8C3iHPfZa/wxh3i6oknnqjuvPPOci0+V8drjz32WEkb0oh3H3rooXId926//fZy/sILL1S//e1vG2k0WPp3Mn1iyxx3/TbdSK2gn4WxNYcddlj1m9/8ZsKVD9IgPsex6eL3Bgu76XjeeecNyMvmFfZ1Pxgm0uvee+8tx5ZNMO8Tp8Yr+YtvkV5nnXVW9fvf/75cB8r2TTfdVKaboNyRfqRpqyC7+I7pxfejohHRj0DXXqzMCUM8B56/6667Snm/9dZbByyaiwyL5ca4rH9fN1966aWyB/1x7LHHNsoW76h0kk7RDa0+cPjhh5c9900b5Xc9L+AnztlTHsBv+9yll15aFo+N7xEGrHIXXHBBkQ/6JdYTyPjoRy2YqfQkPY2ZmEKhoAOOESIUoqE2iS3ENddcs0xEx4J5Bx54YPn74PTTTy+FjcpOQRELjAWRwmaFKLFCgnnnnXfC0cBKV2FLmKLb+O2rX/1quc93NAPzDOFWWAH3zj777Gr11Vcv4y4WWWSRMuCROUqA9xlDwt9IRx11VFkfh8Kv/4G4Mz6jkECQcd3wtFPpwU3cjpVaTFvhOVbOJkxbbrlldfTRR5exWwwAb/augtC4AoS0ecX7KgrE8SGHHFLSHoiXqKDaZYlbph0VBs//9Kc/Lddxu55+fgf3qAC22mqr4uf555+/pBXjRY444ogieBdffPGS/5hfZpVVVinjQ1C8wXAZnk6nD/CtenhoUBCWWJaabYCS8fjjj5fwsrYZZWm55ZarZpttthJ3Pof/TUOucQ8oT17nmHvmUVlsscVK5QZay0xj342VItD4OOGEE0r6RrcsZ5ZH3eMvsPXXX7868cQTS7lhDTzcvuKKK6plllmmpBezqbMhM/ie8TDYRlwaTsYwWbYHQ38StnqjzvAK+eB73/tekWf4lfyJHNhjjz0mPPEhuhvzk+Fnb54S42SGGWYo340yT1nCO8St8pL44BozZPuMaUJcRDfi91CUmcqDcsFzvON7uLXttttWp512WjXTTDM14o+11ZCzu+yyS5ETlDHTFWJ6A+4CcZpKT9LTKNCAwmdhAAZOtoIFnfdp4VPRxIoOoW2laGuSwkUBQpgjuKwUaO2dcsoppaACLVpahq+++mo5p8KmoAIF9cILL2x8y4JOgUUh8TdPoEBHsATEgku4LdAKBmGysHXXXbf4ESXhJz/5SblOBbvhhhuWViDwfbYYpxKFEN/FrXYpPbgVwxK/pYCLgnfllVeuTj755EZ4iSPj13gHrXH+uYNlhQrmmmuuqS6//PKS7qQHaUDrHBDQxD1/aWEdO/jgg0ua40fT6bnnnquOO+64stK0Ah1FCQuGkD4vvvjihLMPULCC+UW+9a1vFT/U457WKgqQedR8aL6QTqUP7hrPEboBrKxbgfWuqHTBvKnFhXiyggWOjTvike9jSSHOgXRlzh0sGIA/UDqwstxyyy1lIUzCz3uUTdzDYkbex1ID3CfNjjnmmEacozRRniOkGe5gmXNgOJUz32Sldu4Rjpie5C3KVasQH7yP0mPFz3eJ+5jOfMt05jrpG88tIzyH/8i3NA4Mn/HNN5Bfb775ZjknjgDrFPkMN7jPsjco87iDf4gD0sA44hs2pi666KIiR3gfv3DPdLruuusa5QSYgywqOKZjLB+UNdwgL9MYQOGk3EeOPPLI6kc/+lE5JizINcot7yyxxBKN8NGoW2+99Up5tgzzDPHCFmU9cZpKT9LzUDhigREyMAVwqC1CQaCSQVBo9uYa8KwKiwUWYYU1BaGAyZaVuWlVMIsyFdXaa69djrfeeusiIPUj7tMKofXFM7RCgHDwB8ePf/zjUnhpvb788stFYPAd/MI3Ma0TNlr/9UoSEHp+i/tYex5++OFyTOWKgLIS5ZgWlHFhhQQIUd3nvhUT7iOksU6MFNywggK+oV/qYSN+AAVu8803L++YPkDrE8G39957N64jpLfffvsSLtKOtYCct2WLLbYogpTWMGmyzz77lHcw2bN+ENf5TZ00QTDjJpaBpZZaqig4rM+FW1zHIsi3CAtClNY1Lf8Yn/rfPRAGLHP4K1acCmIm1jvzzDNLnjNMKnPEU6fTB3DPylW/q1Dx3aE2K1TCt+OOOzbejxUN8YxC4jsccw0oJ8svv3wpK+xXXHHFstHyp/Lkd3T45je/WawvpDVlauGFFy5uAXFIGcQNyhRdHoDC4wSgpBPLvZC2pgNxa5xTec8999wNN0kPLIx1JQnFYtVVVy0VrHl5uA2IY/4gM78Y35Rj7jXDNJD4HPH72muvFaUEZQW4r1ygm4vlOQwfYIl7/fXXS/xjhfvOd75TFt8l/2OhI09zjiwC/Mgv3pSl3XffvSh6WLngwQcfLA21/fbbr6QRSilpz/dIN6GRiAKNH7mHH/WTcUNYWC+NtNGSwzPIMhQtw01DiDRBYeZvPTC8lFPSGzfNg7FsAuEpf/9NOE+SnoVMb8Z3T2avC4XBiK0Q3qMCoxKkcFPQsMhQQNgwb//yl78s37nkkkuq1VZbrbyH0mOrAxAE9KEL5/ZJ4zaFz0JHBUsLHuFA4RQKNBU8IPyjEnDPPfdMOPoA7ymwFRj0dyP0vU9l4PgeCj9WELoa8IsCAhAAUSCPJH6HAjf8bvyGx2AFAFQ2dA+RDghPBDWKDvHBPYQ5XQu+T0X11ltvlWO6CFX2DDffpnJCKaSrCVBoWH6C73Kf8QIos0Bl8P7775dj4oxKBSFLa5T3rMz5JpYD0xhi/CrYuUZFTCUR4T4CnvDppu+YX0cjfaLbpgPnrbptBUOlRZceFSGVKMqk+ZD4I14Bfy+00EJFsUNhogzSpUg8ouTTgieP8xzWG87J2ygsV111VXGDeELJYbwX1gvcE9IOiw3uo8CqNAHWQir9ZvDt2BjiWcLi2B7jCauuS8fYOBqKGLd0Y5qmEd32GExfzwE3iKfoBvmS8kA+RcGnMQW8h1LDuD5AEcQaQtyhHGLhwR2eo1FE44hvAgqMFjMUJ/Mj737ta18rsgy5iYVZv9BIIT3wH+/ob+5jgTVvA/csNz6HVRWlN4K/sO75LOUNxRc36cJHbgONVfIb4fI7MY4ixGkqPUnPQ8GwcLhvVej7vFjB8D6DmOkKoZCqjDBTMq1KoGVj4Ud47r///uUYeAblCUHENyiwtApxn9aRApHCh6WHlg4tVEzzPE9BZkAtSgrnCFxA4Fv5AOcKHQs/eA0hhLVIqBwQ4BZ6BAVWKalXsMD3jSf3rcbvcOCGwjR+w2OI4TWM+I9uJraddtqpCHUqWCrATTbZpFSodImwaCiKDt9ASTLcpGOcx4Z4wCJGBYvZnMpCUIioMBC8WBlA5ZKWJdepJKhEAb+TvlHAxvhEyeJ9Ni1RwDPEv3mDbzFAt47xFSuGGHfQrvSJbpsOnE+K21jiUAbJf6QZ8U8FSbgpA6QJcYkFzfjFQiqUxzgejufJz/iLSpY0BOKX8oiySuve7lzyhuUPsPLQxQV8j/v4xXBShrSecZ01pEhvLDmUfco45VbFDiindAu1SozbSVF6yAPN3hHjkbhDISNPbbvttuXatddeW+KNcKPwEPdAfNGty3VAkSAege+h9KiwarVBQSeOSA+69FG0iDvzqI0CQMHlHvlc/xlGrhtGIazEM0oOz/MdwKpEmpOmvIf/VXAZdL3xxhsXWYBc5brLkNhFrMU0Qpym0pP0PBYYj6FVoW8/d8SC6p4WJYoBhQt3KdhYdhB6FCCuIRTs3uA9BIWVINCa18yMW7RiEVYIOxQbKgJawueff355BlCSnLAsjicQhbMQdip4hQLdZFQuwLOMEaJbgBYPfuY5hD7dPJyDQggUpiOJ3+HADb8dv+GxlY7nYF89ENc8s+yyyzYUBFqvdKfQkmV8leloBco5lh4rUNKVSoEKAPhTTgHNd7HYUdGhEDkey4qOd+hGQFHCOmT8eb+eRqRPTEP8ZL4A45xKBUWZ9/GD1zn3uF5heAztSp/otmHhvFW3KV/EhUq44BaKJNZM7lEB04WC5ZQ0I474DhUkz5JXaWCwTAvpxzUsBJQzwJLKfcsUXZUMOGbQNBVf/D5WANygHFBGjU8xvMA949nKEr/wRyQVe4RGD0o24P9msqVOjNtJUXosO3Xwo2HWTfI5MoXwA3GALEIZYG++JO/Tpcp7XCOdkHe4iZUVxQkLGuWOiR5Bf/EsXVbka//Ywo8oofvuu2859/tSjye+y2bY8DeKpA0OIE/RBUrDUhgzRjeb4cbvln3SCsVMS+9gEKep9CQ9z1BCoRXsJwYqPwqT1hEqNKw8CjOg1YJZnW4u4JsIBVuNwH0KpJU2ChJCGWWHLhcG1wHdT3SzAOZgrA2YY/E/lSjjPXiHmYiB6woAFCXOKdi2yhBMgKBGYaJlHYUKY1NoqSmQ+DZdQ7G1qp91a6TxOxRRcMdveCyx0iItGHfgewwARsg6mBmwcNHqju7Yzw90NcYJ9ohLlR6UxT333LPEKxXdOuusU5166qnlHuMIMNMDg2b5DoJUq4JCdocddijWACucurAlPPxFw3NApQekG+lNujAgFhD6wn2/ITG+3LcrfaLb+pHziXUbZduuFfIqeR0FkvFw5jP+BMIK4zl85StfmXD0QZckXcGi0kPcrrHGGmVAOpAP6MrEbfI/CpFWDNKONAQUIipKw8V4FboxjV+vC+EmP1A+aahglTV9aVBgEaZctaLsSIzbSVF6IlzjfdwiDzE+EasO8oI4Jy423XTTYuGyPBEHxDHpAeS1vfbaqzxj+JFJDkIH5IpTLND9iIwEupOwxgB/h9LwwL/IOn4OofGI/5CNxBP+pTsaiw1paXmuxzvvML2A5ROIYxoGyFXkFVYbGiZMY0H6mYbkAf7gwi9g/NKAqX8HiNORl5ok6TCtCoVmxApeQUChRzGgRUILiL95wMqHAmN3CqA0YTpmIB2FDT9gYdHSwzUEqvNcOBAXIc8xrS8LPFYKCi/Cn4GfVHIIrKh0ISDwn3+42BLFP3yLSgAFTLM+YdN9nqEVzN80fMOw8YyVje4pIEYSv8OBG/otfsPjqOwY/ygbxB+WEIQeFgLjQj/TRYLFAHCfyoqxTQg64gClB6WEc8LN2ACEI+eMb2DMENY5lCniS3d5j0oTYY/wtkuF+CYP+Bxxjx/EVrRgraJCYoxJDCPfp0Kh0iAd8bvpElGoQ4wv9+1Kn+i2lQTnrbqNP3gPhQTFhHyHooIiSddkhHyvNcCZjx2wThlg/AznxDFpyDnWUZ/DbZYIoZJGEdbf/JHJNymzjsEjj1OxqygB5S1aPdmT5/w9mwHuWAdxC8sUEDbSiUYPSmxMFxSP4YhxOxKlh/fq7xJnKO80sogTlAtkEtcBNzjWegm4z/idX/ziF+Wc8ND9iuVHecd4KRQp8jTKBOmGrMSixpgoG1T+Is99lCuVQaxB+pVyy/04Nsd8BiiTyE7KEuPbUNpUYJHdNEYIG7KMhgcQLhRT8gLdkVqDLGeE2XisQ5yOvNQkSYdpRSgMRrOCZuEGCyeVphUXSpHCOX4bt1SiFHiex0oPQapi4X0Kon7RPfDYwbPS7NmIXUAxLPjB5/VP9BfEc/3GO77nvtX4HQ7cwC2I3/AYopWE9OBe7I/nGoqBShFhRkDi/xieZn34EdyJ8UWaxPOI+SL6UxCuCljTSfCj3STe81w3eddrkRgW8w/E+HLfrvSJbltGOJ8Yt6NfCVuME9w03I61oXUupqlYYYt+qysYppsKo+daGET3ox8hKprxG1FOxGd0h/s8b5iGI8btSAYysx/sm8Y3frQs6Xesk3RnkbeMW9wxPnE3lj/cMm8TpzEOvK4/mpUB5Fi9TMW8TrgMk3FtvsddZZL3opVev8T0BdJWyzpuGM74rhCnqfQkPQ+FJBZ+aFXoWyApMM2EIddiwYbpp59+QFdKfC8Kdf0iFNRYcYktI/AdBQZEIcH7USApBBBMfJd7XjMMgxVyBQfv+F3Dihu6wz3vu281focDN4y/+A2PIVZIMa6MZ8NHeNholcbfo7kW3YOYvrRAfZZ4rKe3/lNpMt5sueoW/vGe8F3c0691jGP29e/GCp73Y3ogvP1WjC/37Uqf6Hb8Xqtum1cJS12Ri3mcbie6lX0evO/368qh59Fd3ud+rCjFytt75CXdNg2F+CPf6YfoL9PdZ0wX3SeeuOf1oYhxOxKlB3iX68B18hN+4LiuoAB5ioHIWI4lypr4vO7GfMw149K8YTxaTrke4yHGI9/yPcDtqGAB8RvLP98knPEalnfR/5bV+O2Yxs0UHiBOU+lJeh4KtYXfvUKhFRRiEIVOFACA4I6Fnmc9Z6+QcB8Lpm7xjpVZvTArWIBjBUJUlHzHb0Q/eo/3dEv/xW9xTT8oFLhm3PE934ORxu9Q4IZ+jd/wWP9x7nMxDoHrMY6iYAXDzj4KWYjhtPL0OxDfBd/32Xo8iV0i8Rph0W3dISzxe173GvuYnjxvWHWbfTwGnm9H+kS39RvnE+N2LF/4K+Y1MA5NU8Jo/uY5vss1iccQ00BihR0rO541HBDfxW/GbcxPfi/muXifb/m9mPfi84MR43ZSlJ56XMZj3KqXeyAfehzlR0xfMM8ZtuhWPCbMvMPGs83CENMAxSbGDWONIPodv3iOe/jFvdcJg8qL8a6fJboZ/RDzR4Q4TaUn6XnI2GZu9wqFkYI7CgMLlucWML7pPVuGCIUoXCQKCwpevK+7EJ8DvuH9Zq0U7qkgRMEr0e3oVivwvPHqvl3xixsxHt17PBzGk26AaUDcGr8IzOh+tA4ggBHEUVjzXt0fpBeVBNeMvyhIqQh9XgGtcHXvN+K36q1biWEaiuhP9+1Kn+i2YeZ8YtzGLzG/EYeGX7djfEA8t4I0rXXL/C5RuYo0K4egu7HiN51ipcz3TAuVnei/el6CZt9rRozbkQ5kbkb9PeLQMOhv7wnn9WsqNhAtKxDTwTQwHn0n5nGfj5Y+4Xnv+270C+Gu552ogIrfn1iI05GXmiTpMGT+egFpl9AH3KoLWIVbvcsD6pWYFSjwHO8qFL0u0R2PBxPmFHbcsYB7Dgg3NtyPXUJcG6ySHQzc0J/u2xW/uIFbEL/hcSs0E3DNWnXxOQVnFJjGHf6pC9JmiqbfIJ18NxLDwLHfVNjHilVlynw2MWkU48t9u9Inum1+5HxS3NYdIS/iTzbSxgqZvRgfXuM549rjmNYQn/F9nyEN6mnLtei3WAbrYRfOec8GBmlJuvK8z9bfaUZ0vxNKj+7VFYmouPAM8YWbder+MR24Hu81k1GkA8/oLt8m7gnrYHHj9dhw4xrfxb06dbnM90zfWL5ahThtT62RJB1kJEKhFSh0FnALe71AUSj5pgWcQhsLPPBMLKQce98971jwEaIIo2ZKlPieJmJQOHiv3qLCfeKpWUurGZ2MX9zQn/EbHg8H7xKvPE+c65aVnEI6ooBWkSHOidOhvmmcmjbCddIHN4B8oR+EOV2Ae/F9n+Oa7kerQ0znoYjx5R6325E+0W39zvmkuE1+1y0wzgbDOLES8xw8ju6Z1sQzcYd/iYf4ns+4j2VL/1guUAx8DrfIU83y1cRMRlgnxm0nlB6p56X6jxGA23zf7/EN09yGU1SeiIOonADXiW/lo+HhWfO74Db+4no93PyizreaxQfvUE54r67AOmP2pEKctqfWSJIOYiH1GCZWKAyGhR4sgLFigqgARWFC4bRQR2UHuK57fMNCzNZMuPOMxwje+Azf5xdq5qgABbICCBAO/CoaZxpulU7GL27gFsRveDwcUSjqjhBnumOFW1f0iB+fMa2t2IR3eAb3/Z5KbR3c8Lu6y/wtzDED9e879ifC79xxeYThiN9y3670iW4bP5xPjNuxfEC9oiK/kv/Zx3JC2vDNmNeBc/O4fiK8dXcl/rUXLRIxnXm/bl3gN3gmqmzWODBPoPDwp6BdRSjS+I/wNMsfdWLcdlLpAeIWuaOihx/rsqwVmqUHkCa4D6ZFXe5BLEd1iD/c4Dd2/iqLecd32JvuQJzwbZZyYf4kaKbUtQJxOvJSkyQdpl1CYSiY98FCZ0GOhT3ifQqvz0TBy3X9SeGNfhaFqO8jqKKA8lndZa4Kl8Tg+7HQ8w38zoR3zEILvBe/NxSdjF/c0B/xGx63Ql1xMJ6MZ+LDNHHfTCjGyg0/mX6+I8QlW/RjXRHVD7yLQsrU/F6LliGxMiatWAOMyRdbJcaX+3alT3TbiobzVt3GH/WKlXiFaJ1sBnHnN6NFxmvEoZViPY2gWXkB3fJdwxfTDyhTccJRvqs7ph+TfTJ3j2GK6O5QxLjthNKD8lFXOiFew02+i5uEg3tsxCn3uK4fDH+UhzGeed/rxqfv8JzX3KNokh4qScpSGmhMDSL4BT8Z/oiykr/Q4gSkkwJx2r5aI0k6hAXSY2hVKLQCE9Ix2WAscBRCC7d7K0lg7ZoIE+VR0SLcKNj4z2OJFWcUHnGgpBVzXcgyAy2mXfzIwqfMXsrSDEzOxQyq/MbNL8FMsMYzfqcVeN6wu29X/OKGQjF+w+PhYDZYZjUm7nCH99jXK1owzFRkxK3fZVJJ5/EgTaxAeUZ/4L7pES0E9cq4mb+x9DCRHu6SNkziBnR74SazQTPpGooO6cokd0x2F90eihhf7tuVPtFtwgect+q2cQzGP+9znUnnCLvh9DsxbYD8z7tMrGe64hcmqXSiOtMtxhnPMrmdxIq+mfVGfI4yTzrgF/zEdf3FOWnFfFhxPTCuseGfZnmwTozbTlt6UCyIH8KOYu2ixbgV4ybCPd5hgkK6uAgb4WL5EJZ9wU38FN93vBDfMc1VakCZZzmLmPbM4I1V2rgU0xnid3WTZUuMo1bivw5x2p5aI0k6CJncjO5+UoRCMyhgCFbWbqEASlQaKNx8T2i9ONEaYFVh2Yg46yhw7HsWZM6jkmOBpwBTsBWKsRIGZmxWwDNLMbMIowQxuy/r5OAnlrSIFUf8zlB0Mn5xwziI3/B4OFjnh9Wuo/IoXNNthS5pwTxLgoWFmYK1kvFd45U0MZ1NNytVhK3HUbjyvO9wne8zu7LT9jt7rKtbA7PNMvszyhduopjG+8MR48t9u9Inum1e5HxS3DYO2RNHpAOrr0uzMsA3TUNa/+RlKzq6P5hRvG7VjBWsmEZxUD/+8Drf9vuAGyybwdIKPKffgfxhHiEumBFcrPCNq+GIcdsJpSfGn+8CS7A4iznhjvewwNGYiPKBWZ2ZOd74YvZjLDG6DXRNcc4+dhU6dg4sM0A68m3img2/mjfoqmKhX/AeG37Tbb7FOc8bb8yE3iz9W4U4HXmpSZIOMxKh0AosNUBrXWEbBSVLFjC1/dRTT13W6KJgbrPNNtXHP/7xas011yxLJbBaOgvzMX09ApL1ZqiQUUyo7Oi/3m+//YqbTM3PonmMJeB5LDR8l/dc1qIuGPmmggtlCAsPM60SBz4bBcPE0sn4xQ3cgvgNj4cDZcWVnoFwEl+8f9lllxUlgzEXrKnEd0ijySefvMQ5S4CwvhVKE8uNsLyES4W4FAkWMypX3EXAYlViuQnukTYIWCwCTHVvOMwfEK1CpBNLV9x8880lX5AHcJMVxkl/x/Eo+Fslxpf7dqVPdBv/A+etum2ei0qpx6yNxnpMuk+4uXfNNdeUJRO4T7oBCjtKEulJ+WKRVroNSTsUfiY3JC2uvvrqsqI25dUlLPA3ZZG1mihHPM+zKKPkByt3vm0aguEFFhNG6aLxQ5645JJLJtwZaEHyfcId3x+MGLedsvToJ/IU38ENygxyKYaXvEq4iCusw4SXtQEpR8QpG1ZKxjGxvAQWLpZyQTFE/mDFpAt90UUXLe+r7LA+HcoI7xD/PEtDQ4tnHf1EerDRGGAVeMooFiqWk8FKSHnFskN6ECbLnWVnUuQdcdqeWiNJOshIhcJwYE1gnSxQwFEYGaeBYLB1R0F0LSu6m4ACDlhfeB4QPLTmmTXYgkkljFBGmH/mM58p69ZwTMuIsCBcqHyBd3QXoqket/ETK4zTxUZXDi1WBTDvxXdboZPxixsKufgNj4eDAcIIUyGcxA+mexQMlQ6UEtZa4hwlSOEPCNNYARBvcd0sBDSDxFGwUJhYggTBb7wjkEnPiP4A8orHfAs/UyHTRYC/fvWrXxU3UabMX62GH2J8uW9X+kS3zUOct+q27wLxEGHNJ/J4tKKw4C/pZpmiIkXhIK5ZzJKFgH2euOOeLX/SnArX+yioPAMoUKwTxfewiJIepDFrd1lJ+h5pEP2Ev7F8OHYMyxLrOrWDGLedUHp4LirhQPmP8ojwc414pBEmxBOKDqDMkDaCgk7cAzKKxgNryQldX8Qt4UJR5NzyRdxyjjLTCpRHZKVpguLrAsCAMkz3cZ1JsfgQp+2pNZKkg4xEKAwHwpZxB7RqEB7xOwhV/rRBqUAAUHGxojNEoch7CHK6t4S/DFjNGyWJ/vKNN964uEHlyorECgjhHIEYhaItVJ9F+CCgsULQosI93KclVrcc8E69EhqMTsYvbuj/+A2Ph4PuEUzvtCqjVYW0QVBi8cKixmKipAGwOCIgkBH0dD26+CVxQvyTNgh2lEbTht9oUYDAisT9YEpovRLDeofyRIWDf1gkk+dxf++9924oFsZJK8T4ct+u9IluT4rSI7oBVEack250V4FWAeIa6wt5FiUVixuWS6BFf9NNN5Vj4pu8zTPGMRYA0pnrpB1jQrCokS/4FlCR1+MWv6DocN0wAt+w3NAthlWXHwGodFGi7H4ZCTFuO2XpMUzKD/I4q9Uz8Ff3AOsyljOUQ5Qfxpkhz5Ar5FvTCpB1xK/5H2s3ChINLixFKEk01ADrjN2KllHSO5aZwcB/WLj333//RtyQD7CyAooQDQnGXSIPeZ5r0fo2MRCnIy81SdJhyOgWXvftEvpQtyYIJlxaHHR/oaygHGEBoCLFfKxfKKxUpLQyEaKcY21gnAeCk1YKbiBAqBARqsCKxVEINyvIVCB14cH78df0+OcY31B4tEon4xc3rITiNzweDiw0cfwUAo+WOMrJoYceWgQ7CgZKDQOHUTCosIC4JS4Qog6IRcATf9ddd11JE67zPvGMW1gbiG/8Z4XIsa1KjlV6CJdWCNzlOiZ5LHoIfyoVW7soV6aZFUmrccBzPuu+XekT3TYvct6q274TlW7z66yzztqYV8XnqMAYPEwcURbYkw7cJ50YOGycEmf+5UalSmVLZXjrrbcWixDdiI5b0fIKppXlIi5wikKgX/UT36NLDSWaMst7fCtaPiaVGLedUnq0kMTf9WmUETc2fMifZ5xxxgALJ3nUd1B+HPgMlC2UJCC/kpddsZ6wsJHOfPtLX/pSuQ7GvWV+OEgLGgR8D4gfFDKuCQoWctdwQio9yZhmpEJhKCg8CF9aRkJh5m8f+roZF8C3FB58n3NaPSo4QMFECANuIlyiiRahjeDhWwj3OnfffXdDGCus/SaCJFoXEFC0gEXhDVEwtEon4xc3FIDxGx4PBxWiXY9RuUOZwGIgpIPKBK1+4sHKF+XVRRf5LgoqYxuMN97Fj3Rz0qK10gWeoWLWbfdUGLECUwhjtdDiZ6sXdtttt2LdANO1VWJ8uW9X+kS3jQ/OW3Xbd8y7pjV84QtfKNYD8yRxd/rpp5fxHxG+xz0sY4wBAtyj9Y/lxXRE4aFLRf8C8c59Gy1+izRE2VEpgpge+hd4x1+hcY9zGjU0YkZKjNtOKD3EW3QTv+MGCicyJYLVlLKE1cR0euedd4pswiLp88QN3bmMjcJtxqUhC1F8Yhnkd35g0DTwXb7POyirUf4NBvGCEoyC6zmWbM+B8VtYYcH4wY/N4nI4iNORl5ok6TBkdDO7+3YJfcAkjluMF8AKQGuU37+1CjDYEoHrYDugYFLpKsBpqVDh0UJBkGAZosXCfRSU9ddfv9zDqkQlTDisKNkjZB3TAwrvWIkAghuTvr+moxBFYS68FwX7UHQyfnHDMMRveDwctLw/8pGPFMFH65t4ZxAsYE2ju4SKkTTiPnCfMTV0gWASR9kgzkkjxm6QPrhHtxhjq+jCZGwIFTQKqcLUynaOOeZojOWK6UIYeBYlhsqHcyxFWASNe4Q4zyDY6YrDTc5pYev+cMT4ct+u9Iluq8BwPrFuEy/4yZY+4SetKD8omSjq5FviH+WGsoTli/TjmG+Sp3nuxBNPLAoLyiblgnE/N9xwQ3GXMsrAcsaB8J7vaumxmwVIc8oklTaYDynXhtV0orsT/9KVzR5roYPeR0KM205ZeghDbBThBl1OKP/EC/HAjxhYlq+//voy8HillVZqDF4mHxK/PIt8w9r26quvFgsrXVgMHie//vCHPyxjE5FrdHNRxlAunTAw5meeQ4a2AnIvWq7pfrO8AWOJbLSYXsSj8nNiIE7bU2skSQcZqVAYCipFBDUtTCoruqKwxlDIFJJ0f9DvTAsJVDJoGcV+f8zhdLM4fgG/Irj5QwJhr5WAYwsvIBD95dlxPPVCzbHv40e6eJoJUN9pdm8wOhm/uGE8xm94PBy8izKCEL7xxhuL5cfxOUCaYfXhd9sIrVpbh1RyWF/oKrOyI41QQKkEcFtlhl9pwTREoSHdEfqkmf42LWJ8Ad1lzZQZ3o+/Xk8MMb7i99qRPtHtSVV6iDvjT+UHsHwSx5QRLKd0dZE/+Q4VK0qg+R6ouElbnjeu6LIkLUlDwNJA/kc5ifkgWnSA9EFpsczyTcuG4YwWN57/5S9/Wcoq0BAyD4yEGLedUnrAMBlv5Deu6R55kvjFXcJKPKqgis/GeOE95R1+5xn+TlVOAW6STr6vNcgyMhT6G/gW57ptOWKiRIjPRvk5MRCnIy81SdJhKEwWKPftEvqgMERgx8KMkOCa34R4LPEdwG8USgqtbgsChPsSCzLCJraUIb6vwIyCk8oAP/mebk+MUOB9w+W+XfGLG/opfsPj4YjPRaVBQQh2R5FeHltJ1gU7mF6kBfHkO6RFjDf9zXWfASt4njV96nkgpnPsEuB5KoP6t4Yixpf7dqVPdNu8yPnEuF23MtTBamNYrQhjvieuPOc4ukEZqucf4tp4pyz4JxjP+WxM4zq+SzqaNj6HP1qprFslxm0nlB7CEt30/UgMj4qEe+A+SlJ0h/vmc/HcMsWecEW3ZGLiEHdMN4j5KeYTv4c/m5XrViBO21NrJEkHGYlQGA4LGO5a6NnHiopvcc091Au6gjQWRoSEzwPdKs2wQtBN3uHY67oNHsfWGHju91qtUKGT8YsbCrT4DY9bAUEXn49xbThjeI0DKj4FNULY67inn0BBCu59L8ZzzAdgesU0p/IQnlX44/9oOYjfH44YX+55vx3pE922guF8Ytw2rgivcaISYdxwHXdjuDmO8aOiClHJFNz0WxDTAkwrw2GewG3ei2kZv+Xz5ivPzQsjIcZtpyw9vq+/TQP2Hhtv7A078eE7ojyM8RzLlumiPyU+U28ADEX0N9/kWLejH2IZi2k+sRCnIy81SdJhLNQeQ6tCoV6AEDpeo6AqdKPAxu0oDOqCwUKtm9yPwkyBH933Wb7tdyQKY93hOf0ZBbSFPypC0T3djwIDrIwVTlFwxG+5nxihOxS44bfiN+J3ol+iv+P1GL8cxzjh3HhmH1vthDe+G93nfvwGfvJdn9Nd3Ylp5T3fAY51071x7vP6x+9HP0AU8BDjK8ZbO9Inum0+51y39Tvgb5+Jccpx/TkwXLHl7jXyqN+N70L8RnyXuI/nkehGPOZ7xjvgNu7GOI8NHP1O+vsM39XNmB9EZdbnecawxbidFKWH5y3rXPN+VFygHoc+J/rNuIWh3nHZFol5PCpGuqG7nHtc9wN4TzeMj5hGXIvnUZ7FtCBedIfrQ1n3hDhNpSfpeSg8FiD3CoXhoJDVlQyIwpNCFluk0Ew4KWgsuPiBwkkhxF9cZ09h5H0FDdfqFRlYaC3EFNr4XcNKgY9CYDDoRojvAN8dTDAqHHjH99y3Gr/DgRsxHtx7HKEVSRxzz0rRcBOOWDkJwtk4i4qgaRXj01aqaawfTBvT1b3v4gfDIM0EazP/QfQXbpoOuun3SCevmWYQ48t9u9Inuq0/OI9u8y3vAXmLOCQs9TDEsVAQ873XiE+vc828yp4yoH9MJ56p513zhXGrG9GaFt8hvXQX8Dd+MJ/wXdwwPKIfIjE94/PR78D3Y9xOqqUnxj3v8/2YP8RrhCnGr9eNM74RFZeY/5tZuP2+70N9EWDKFu4aH4TdsPqtaAWFGLeGm2/E9+I39Uf0P88OlmbN0o44HXmpSZIOQya3ULiPQqEVYmFSQCIMogADWwuAAKDgxFaP37fQeQ7xuC6U+CaCwG/XvxuxEPMMz+PvWICjMEcQWAFzPT7ntwRhyLW6MMDf+t39xMbvYOCG4Ynf8Bj/xzgX41dMu7rgFO7jlmHGfd8Bwmyc4x+fq8cF8A2fjekY04H3+Z5hi2nLt2OYCUusBGLaOx4Fd33HvcT4cs8z7Uif6HasVHSba5yzj0qCGA+AwmH8eA3In5zHaxArNOMOeN48zTO8ZyXLsZW08amfvM7eMJF++ol0MG7r5RO8xrt8Nz6D/3CHexzrd9KS/OI3IIZVf3A+qUoP3yOMXIt+4rv19Ijj3qJbEPMd4JayhHyo3yyPNhJi3iXcukuacD2GCf94H2K8+C3cjeWY9w0XfuV90xL8hv6B+H6Uf0Bcx3iKEKcjLzVJ0mEoBBYk91EoDAV/hzCTK78i8+sxvxTzi3KsaBUKQuGJQhgsWBQon+f3WAo119jzzGACJgqGulDgW7awdK8ZuMnmN6KbXqOwxwKvIMAKRDwAAiWGbyTxOxy4od/iNzwGfv3n12J+s+WXZH4Z5o8s/MgWhVoMJ+E3nqNA5LrC1nCa3n6XZ4hnz02HWIlEwat7fkehqzuCH30PP8ZwmhaEwTBF+MXeuU1ww3SM8eW+XekT3TYcnOt2zCcRpgVwegfmNmJGcytBiOkR4xH4js/xjuEkTDEuo1IE+KXuFuh/0L+kF+5Fi4Buc8w9GzNRUeAZ00nIE3XFnBnRXYeKX7OdX4j8aF6BGLeTovSwr8M1/Ex54fdx1qdiMkJmIuePNeLAMAJjCXUX/xmv3vecuDLeIqSl1yyDMX2FtPE7ppNxPphFNqZ3XRGSmA84jvINGczv96znJs3iWIjTVHqSnmcooTAc/OLMHBX8ssyvr/yKzm+0EQqOhS8WMAoXlVMUYhItEbFioEBb6HALZUMUFFHIgAIlCgDALe9Ff+Efv0l8aNKPwiT6iXkumGaeSioKqxinkxq/wxEFd7PvERYqTuYA4XdxhLbTAPieGJcIRyss4iwKQZ6pvxcrSr6r1UA/xDipt5whul/HOCctqRDi+9H9mF/E+0x1wNwkzKfCXDX1CpbnfNZ9u9Inum3+4zy6TX42/5m3aUDwezfpxZxUlDMwLptVPORJ4ydWcOZVwqQfYpoR/9Gf4Nw7QP73e7xX/zZuxrA1UziB78R5fqBe9s2DLFnBr/OEg9/naVSpLPEt/eqea5Oi9Jj3aBTh76iQMZcQ0wDU8yzfwB3ciHmXY9KJ67rDc/gtTtvAnnzNdZ4F9lz3GeAPyjgVRyxHKFrGefRzPLbs6Fdgr/WTuDW+8LvPAOfkP+YRmnPOOYtf4n38FOWhEKep9CQ9D4VCYeCeDN6K0KeQs/ChhU0hxlwTVDTnn39+WQWbyQdxmxXQmSANJYFJs/wei0ZSuFjIj4VHmcyOe0w+yEKSwrFLD1BgmYmXmWlZ/4k5YfA3kxTiNt//4he/WCwdCg72KCkoKMw+y8R6PIeARfCxobSxBhHPIqyY9I2Jx6wo9LNCCuFDuJmlFRAmURjyvO+4bzV+hwM3FEbxGx6Dlh2x0t96661LC46JB0kjIOxbbLFFsdjxHuEG4sW1hNZee+0yIzaVARuzaqMkIQTJB6z+zDHfueiii0prnVYySxEAfmOiwyOPPLLELZO2XXHFFSUeSVPmc2EGW1r6rAHGzL31idjw82233VbcYnkD8okVRqwMSAfjggnyWPMIYsUc48t9u9Inuq2/ONftOEYGVN6Ywdi1mohLKyfSjCU+iEvyPJCHseRhjSCvmx9oiDCBHtYKVsSn7Hmd9eqEhgoTEuI/4oWyQ/qgeO25554TnqrKNZQRJs4jH/ziF7+YcKcqaUb+oPwyKSWKNTMO43fKBmEmzZjvh7xEniGfCWUrKkCUPdIPP6H44ZeoqBEfMW15biSWHq8L7rDQJ+U/Wqr4JhOhukq5kzaiHJBnUaxJF5Q78j9yDUsRK9pTbog78inzX2EZJr0JNw0SLHqCfEJGUj6IV54j7pgwlAkPiWdmfz733HPL88QX/iIfcB/rDGWZ7xn/uIF7yGZg4kqs8iovynDLkXvkMvOhAWHy+WYQp6n0JD3PUEJhOFhPBoHEjJ8ISyoyKkAE9ic+8YmyCCSFD6HELK8ubcB3EMS0wplkjZacrUsUDmaNRfC4GCnChoLNTKJMoU7hQxgw7T7PMUkaK6PzHDMDI6ARLMDspeecc04R6AgGBAUFmgnc8DMrFqP4CAoAE/XhFu4iRHQL8AfgnhUZ15jdVrgX43RS43c4mgnu+D3A/4SJZQeIG8JPnGEBQnCzCCUVIe8gtJkAEAGIUqEyhKKowoCiw8rMgrKnIgUsuoifWHYCIav/qOicGRZBigJLOtBFOtVUU5XrHDMDLe5xj+UsENJUGkxqicAlLRDq+JdnUATwn4oM6abAFq4xc3dczV0FI8aX+3alT3TbvMJ53W3iO1b6xCEKB0o9efyWW24p1+3yIW5pcDDTL3nd1vuuu+7aWNMJJYjKlHhh1l8qTEDBp1IF7qFUkO7AuyiRWhWoFFFg8B/5m/tMlMeEojR2gLW6qGyx8FEOKE8oy8xMzBpehAvFgUociAf8ieJMuoBxBDEvAeWfcmu5I+9aQce4ndQxPYBChfv41bFTxAnxRBlg9mS6RnmPsKKMC4o9SqTWNcJPnsQ9FB7DQxcd7+JXlCnkppCezKxN2UI5dBkczlEeL7744pL/8YeKMktXoCjhV2bVpvtWcA/w/+23316OSXdm6ybOCS/xirwWy4xKtnmSPId8iET5FiFOR15qkqTDtCIUBgOFBmHIUgUUIPaAMkMBFwQA57Q2WTJAxQSlg1Yrlh2gkHOPtWUQDhR+lCXhnMJNgaSVhVs8e8opp5Q1avAPFZstVMLBOc8hiKk8FZhgeBHQKF0UfJ6JFSIgBHCLLRKFLBWVgiNWuiOJ3+HADf0Uv+Ex8Y7FBgWReEVhJK4Aaw4zLVvxYM52mQLinOcJE8I8rp2GEEeYA2k0++yzl2P8gTAk/gDhTWsed0g3FGCULJ6hFQ2kBX5lzArHPM9MwlwznYhL8hZKE/GN8hUFPNRbn3wDcMfKEnddbXq00ie6TVwB59Ft8rxpACgIKChUZFjoiDcqTPwcV+smzFS+xjFpxrIfWHZYvHKFFVYozxGPKIpUXlR2HFMWqdCAVjxjiHiOxgdlhzxAHFPhU764ZzoD/nXhWSwGNEaIM8NKxcws6yijXMPKRhryTePBshPTwnR0j0KFlZAGCpgnALdi3E6K0hPzjf4SlHmUbmaGR8HEn7iP9YTZx4H3sUKiiNJwIr7I48Q9ljDyNfAejQkaAYDSiOJuumPNxA3gu1qOUAxRXCi3pJvKKn6lgeCyPV/5yleKIgVaxHgG/2N5BSxLzoht+ZCYBjGOgTyBwkUYlDVQfw6I01R6kp5nKKEwHLQkbbGoKAAWIFouYKsRxYJF9CjwFGCENxUogjxWYnvssUd10kknlUKGUmTLlcoBQYoCQ187woWCj9kXtxhTRGGmBUMlIFQaCCD8pJCwkBteWmYoA7jN+BdAaChE47Hh5DwKC1rWCtHY/z6S+B0O3FAQxW94DMQvQjMKLPyNYEZJ9FkqTaxsxCkCmvgkfWnlIYhjpcA54ecaXSjsDTuVI+En/WkdkzZsVBSMDaCyiu7hDsoV0HKlqyTCffIJA0uxMtDajX7hfqxMgbByPcYDlW5s2TaLL/ftSp/otv7jPLrNt3zG/ER8uCCnlgKeQaFxSRAqNypKFBTSkYqJe3RXUX6orAAFBIsLlSzlg7RAESZ+gHQhrfAHcUv5ZIkR3CLtWTICLOdWdljrgO9cddVV5VgrhOHhGRQWyj4QB4bR70NMP/dYN8gn+DeWV92Ox7wzEksP3xeVZBpVDqAGw40igxKEW+R5GhRYT3Xb9+l2jPFMemJpAcqYli/cIM5RiDgmzmhoEGa/iX+xuFFm/Q5u0M0FdIdiYeee77DHPdKU8oxiJMonyyzuG+/41zAAec7V/MVv1CFOR15qkqTDUFAsSO7rQmEwMI3Tt0yLhXfZU3gQshRwCxfClsULY4VGwaLw7LfffmVMAQUQ4YMQp7WJe1TWWI8shFiE9tprr3LMAGqErK0lKgG+jSUAZUlQgFB8gNWiFcy4SThRYniXLhvuY6ZXAID92QoIiC0lnscdLCeC321xcWy8um81focDN3AL4jc8Jm5QSrTuEGYFPAKT9KNrBAHLMYobGKeAsmmlRQVImtFlpjCnMlQIEpdUVIBlJY7bAFvsVph+h3P8gWWDrg/AT3YZAC1VLFEsxAj4i3DSBWnFTNj0C2loPGA9QXlmc4xGs/hy3670iW6bpziPbscKV8iH9S4FIJ5QRgwjFp043ok8h3tU1qYZUOlRHgnXs88+WyoyIA2xZNCVQ57GGkR3TcQ0cvwK8Q5a61SWze+UedxlY9wcChXd2rFMUYliWVWhi/AeXXo0UMwvfhMoh7FsAW6PZCAzbsYyDViyaJzV3cRfdh8B8UXXOjBeCeiORPnEIqoMpAzaECQNVUrxO2N/bJBhIUUeRr/SWNAapCykUaLihBUUK6Yw+F2wruMPGoO4adxhwWPMZQwffolljnMaIoQFCIsKaDOI01R6kp5nKKEwHIz7wOQahReFgv5jKkaw0CNsqYAZM4DyQiVGQaXbiUJJNxfmXIQpyhECCWGNOwxUZWwOLWC6qxCCl19+eTnH+oN1iJYsyhYVJ4MpKcwUcJQqnmFwIWMbsBhQ+dFCw6xPWIFjTcGGB4Xnk5/8ZPEHIARioeecVh4VPAOqcZc+dN2EkcTvcOCG34rf8BiIFxRHwhQrWOI1CkfARI/wJTzEOWmBWyiOtBTpPsG8b4UHdFNiike4IoRpWVKJ8B6KIEoK8U83iBU0lbpQsZlXgGPGMVCZkuaM+cIthD7hVQALLWRawCoz5A0FO1BJkCeocNg4tuKAGF/u25U+0W3yCnAe3Tb9otKAQkrL3neskKlcKUf+BUUZoauKBgX5EIslA2YBJYdBtSgexCNWB/2CtYIuFO5RfjnGLb6D1YDySdnkfeILBYV3ouJPGqo08BzjbmisEMdYZyh/WIxYxd/Bs0Cjg3xh9zfhR4nDbxxjeUIeoODRVUo4yF9YNurEuJ0UpafZ85Rv/poiDchrKPKEmzxDGULBwC+GHTeQPw7+p/woR2iAEZ+ElbzvuCpA8ZxyyilL2iELCSMQF/yyT5ziHnsUFCx5KI9+F5lEnBs+vokfiDcUKvxFead84QcUsii7eJdxlco64wZ4F4WIZ1B2SXvylvHlGLI6xGkqPUnPY6HxGCZG6FMYgQJhgQSUmVi5AOcIc5QaBKHfo3DiDi0rxn/wdwTwPKs90y1BnzXnVm6AcMItxhDR9YG/2eMX3UbIeoxAwSpAXzeKWVQC1lhjjSKkveY7Ctv4LMIDQYswpBKi5YYQwv+xmw9wR7fcT0z8DgVu4BbEb3hMPPgbrViBEndAuBSIPI/Fh+4R0kmIdyxaWB8Is61+IE6vvfba8mcP6U9FEX9NpuuFAcx0Q3IfMzxxDyrEdHsqkBHCuMHfeLaceY6/lkgjoDVKmAgn+cZ113jXPIe/zI+kC111bByD92J8uW9X+kS3B1N6vI5/xe4iiBUV3SA+F9OdPIh107yqAkUjAKsEyrsVLu4Rv/wxR3wQD6QRcEx+wB0sGOYR4NmI5R4IA/mMNFPBIZ+hwFBpQywX+BcLXSxTphvQcMAdvk96+eu4ac5GPMS4ndTuLfxJuC0Xgn9imkhcjDemDe+TX33HdAX8Tpwy5od3fEYLpbLT8sC7+JX7+pky5feMN/bmA9zwGHyPAc8MtObc93iOb1gG8Ltxp7/daxkH3jNvxW8JcTryUpMkHYbCYAFxT4ZuRehHoWAhoPDYIuQaG5WUhcXCZQHEjShwUHowxQqFr65IIABw14IJuBNb+LipgME/fNdvRxA0VLqa/CFW2oLgiu8bV2A88AzUn5vU+B0O3DDe4zc8FtMAjA/w3Xp4DUdUIAS3aUkSb17HHd3yGsKS4xjmSBSmvmOesPXpHmhpYt0zHKY9fo9uNSP6Px5DjK/o13akT3Rb/3Ku2/F7g2Fa1SGurAStvMQwmo4oNVhgTM/4vRgfuMM5/iIPe6/uB8oj972Ou3WlAbDunX322RPOPkA3o/+Bsou/cJdj/OB39G/0N+/HuB3JmJ4IYdFfcU/4fB/4vv7xOvGNX4xn94CihyVGxQbME/E5wk4cGZZ63PtNywpYfnEnykAaGFhCo6UajFfzB/CeaUh4yAvmK75pA0R0K0KcjrzUJEmHIYNbaN0PJRSa0awAQF0IUYBjoa+bSbnvYGcrMgu5wrKZYLOg8ywFP7rbrEKMLTLAUkSLGDN+vA60SCUKCQQhYcE/fLceBwqldsTvYOCG8RO/4XGkWbwh/Iy7KCzB51U8CA/pwzsqpSog9QqvHhe4FQWu1jriLwp8qIcHcJ8/hPweEP/xO1YUvI+w5hg3rLgiXGsWX+7blT7Rbf3Ked1tw0zcWD6cgI57hpWN9wmrbvsu6eQYGDDc3Ce+mf4BzN/GO24Qr7oTiXFH2teVK4j5xgra/EC3DPctC7hHGYp5EX/Hc92IxDBG8DsQL5Oq9HgfxYF4qJd//Gw8+L5pCU61IT6jrMA93uc6FmHQvehfrDqmr/AccU6e4DjKFNENrsXrxqODsclbUX75XixTgH+N55gnOI7ux2MhTkdeapKkw8TC4j4KhaHgeQqqhTgWEoQq17lmIaKgcY1NwcExBY97FsR6RUjBp9CCBZdvRwGFe1EY8V1bQAheWj0QhSpCRKEUK24rHuMDUJ68rj8jVgi4FcEN3XHfavwOB24Y5/Eb8Rh/eR6pVy7EnRWYSgnxE9MKjAPj1jQw3ApR0stvEHcK7GYQBr9hXonvR4h7r8c0i3khQtgNBxvHMT449tx9u9Inum34ONdt/Wx+8lmIecy4dR/TIyovoqJPWElT8wiNgficrffoHulqGnO9Xha55zXfZyZl3xG+a37S3xH8ob+gnt6xnPu+eageZvw5KUpPs/wl+p1v6k++w6Y/BP8R5+Zd86VuQMyfxJvfrsebGJYYJtw1DHyP7yoXwXQXvsn78RuUbeM2uk2YYrh8Jl7Dz8ZFMwWYOE2lJ+l5hhIKw6Gw5D0KkOf1Cgj3uOZ94JxCq0DjGQWBz3EtVmyxgFtgLYSeU1h1E7wew1lvMUps9eAHwxTDozDgG9yPgk2hEMMZv+ueZ9pRqeKG4Y/f8LgO4XCTKNQJj0KOuPY5wwyE2+cNpwIwPicxLnDbZ/kWlVf0i2nlPhLjGT8Yxnr6cJ33ecbr+hc89l6ML/c80470iW4bD5zX3fY5nzV/mo/JV94D3MKPphVxQ5iJW68RtzEeYyVFOumfWKZiWau/X49n33cPfLse5/V39J9hI1xeE5cy8RnRLZ83TnB3JJae6CcVKsDdweIQN2J46vgt3PQZ/O91iOUG9/gWbhrOWJ7i+J86lg3vRaUVDFMMW4zbGIb4jOAf3YLBFDXidOSlJkk6jIKOQodwtcC1Q+iPd1TiVKYUeFQ0n/rUp8rxSMANKy3d9lt+OxmcTqdPrCStNKhsmK08aQ/IK9IReaWiFfN+yrfOQVxSZlTWUulJ+gJaCWTeqO1j4ua35JKJcxvRxi+77KeYYorGNebDYT9SoltsfsNv5jb81sn0ASpaKoTYQv/c5z7X+FZuk75NPvnkZf/5z3++/P6thSxaJVK+dW77+Mc/3ig/n/70p6vPfOYzqfQkvU00ZWoitXUau3qSScdWUGz1NzMhTyrRLb5Rr2CToelk+sSuDBisWzWZNIzf2IVE2lkOUr51lmhRs0sylZ6kp9HUC2ZgzMAKEIRKbpO+xfilwrMfPVawI0W3cDtWqpqecxt8G430gTgGgsqX71ApN/NTbq1vcQwScI14BdIw5VvntwjxnUpP0vMgJKwghb8AbBklk45xKwjbuqBuB7gZzfd8U+GfDE6n00fliQo3ji2pVxbJpIOcIh3N71rujG/TOOVbZyCPm8/pNkylJ+l5YlcILVKFByCgc5v0DYjfZpYDf/keCc3c4FumaTM/5fbhBp1MH+A7lqn6d+r+yW3itjooMqRnVFxTvnVua1ZuUulJeh4yL4IhVpS0iuozcCYTj8KX+KS1zziCZoJipOAmbvMNW7TttFiMVUYjfeq/+zP2ActDtDAlkwZdksZlVF7jccq3zkO+9i/SVHqSnsZWD3vHM8SWkMIit0nbYlzGSq6dFWt0K36DbzfzU24fbp1OH75BBct37E6J40nq/slt4jZAiRGuKccYxGz6sk/51v4tlhkgj6fSkyRJkiTJuCCVniRJkiRJxgWp9CRJkiRJMi5IpSdJkiRJknFBKj1JkiRJkowLUulJkiRJkmRckEpPkiRJkiTjglR6kiRJkiQZF6TSkyRJkiTJuCCVniRJkiRJxgWp9CRJkiRJMi5IpSdJkiRJknFBKj1JkiRJkowLUulJkiRJkmRckEpPkiRJkiTjglR6kiRJkiQZF0z2v//7vxUb/M///E/13//93+X4//7v/8qWJEmSDM6//du/Vf/1X/9VjqPM5HqSJL1FsfSg9FhALbT/+Z//WfZJkiTJ8CAzU9FJkt6mWHrgn//5n8teVH60+OSWW2655TZw+4//+I8iO5GjnMtf/vKXCUdJkvQSk9XNsrRUYuFNkiRJBkcZyvAA+ad/+qcJR0mS9BKT/b//9//Kwb/+67+WfXZrJUmStAZjIP/lX/6lHCNL/+Ef/qEcg8pQkiS9QxnTg4m2DkrQv//7vzfMuLnllltuuQ3cADnZrLGY43uSpPeYjJaKpth333230WpJkiRJhkbFBjmq1Rx56ljJJEl6i2LpobBSaBdffPFqsskmqz760Y9Wk08+eTnOLbfccsut+Tb11FNXb7/9dhGmDhFwbI+WoCRJeofGmB4KKspOFtQkSZLW+NjHPlYttdRSje4turpABQhUgpwDDdKiniTdIZWeJEmSSQRrzwsvvFDNM888jd/UY1cX1Mf20PWVSk+SdIdUepIkSSYRlB54+eWXqzXXXLP64x//WM7jn1taepC1HidJ0h1S6UmSJJlEVHrgzjvvrNZYY43qz3/+czn/x3/8x7JXxmIBilafnB4kSUafVHqSJEkmEZUeu7ZefPHFaq655mooOio+QteW1p60+iTJ6JNKT5IkySTCQOZosUHJefrpp6tvf/vb1euvvz7h6sBBzBynwpMk3SGVniRJkkkEpQdYf4tJXh3L8+ijj1arrrpqGesD3MvBy0nSfVLpSZIkmUTimB4tPuyRq48//ni12mqrVW+++Wa5rqyV+nmSJJ1nVJQe566Ig/jqM5a+//77ZY9/fE6/2ELyHVeEp1WlmZg9W7P3o3BBIPFeXHpD07N7vlMfZIhbuB/jJ87FUf8tFXg2ukM49G+zVZj1k3vdxF/xW67vU58LRLchrgEkuOsz7psJ3voka4QhhsP45934l4rpYxxxz/vmAd7RLff1Ff55J46F8F1nDud+jG/iJ6YnxLgA7us/7+m3Zn4ybLobW+nGbT19Bf9yDzeMC/wb86/fBp/hvbhQpfkR/8bnOW5mNcCvvBOfhXrY/v7v/77s8RN+lGZ+EvJEDEuMX49jfvQbxt+f/vSnsq+ntRg3MfzRD9yvyxHjB3/X/cs13Yx5Q7/Wy0dMK/Ccvd+N8cN13Efp8TvGJXuPn3rqqWqFFVao3nnnnXJu+Jv5yfBAWoWSpDN0XOmpCyQE1hZbbFGddNJJ5XzttdceICwBIYIA+Lu/+7sBQjIKBYWIwiNWKlxTeOp2FDKGGcFiRaDbClTu8dzBBx/c+JZuobBEoWQFvdlmm1XHHntsCfO6665brgHnPo+b/t1hvOCu3/UbhgWisEUAx7DEOAHueY2w4bd6GnCf9I5h2HXXXYsfeE4hzzP413dxj83406/cP/7446t77rmnnAPX9Lf+IS11qz6LLc9QUXof+H49fPgt5gmVZfDZ6EaMK4jfwB3yST1vGH546623Gi11no/3rKyIN66bZs8991zZx7gTrhGHfJdj3uG87k/Dwt7v1NEv5j/TBXCTb5sG+sNn4rMxrwHhIV30U1QQcFf/4HaMD4jh0F3yWVRiQTcJX/Sn8B0GBcdy04y6csz3eVcsV6S7brz33ntlz7eNZ+Bd/MG8O1D/ZvSjcTCc0sOe7y277LINmaSfjSv9KLgXy2aSJO2j40qPUOAVRsstt1x1xBFHlOM555yz7FEkaBHNN998ZZt55pnLTKfsn3zyyfKM7w9WCSCU6gI80kyw4i/DrDDSfdxaYIEFGt///9q781/rkqqM461RBBICzSA44oRNojEGnI0mRtFEE4ORScWI2tA0IAEUUVFxwjhEMaKAQKvMILOIgAqRdgKi8QcwGkQj0Rj/i6ufor83qze3u6F5733N2/UkJ+ecvWuvWrWqdq1nr6pddUTOt47T5MWf+7mfW7/pPTtUdta5Tafgd04fypde0s+0UKcJsxP3Pct2dEQzD5hOoevY+p3vfOf6nVz60yn7dJ1r6pSlcV7ZEdnSzzynY5o2CZWT3FnH9CjvSW7C8dVgiKDCV33VV60hBmCTyvXXf/3XJ1//9V9/ct/73ne1vx/4gR9Y+dKjNIi5t3A+7/M+7+QrvuIrTl75yleu46BdVBfpS/5b3vKWk7ve9a4nD3rQg06++Iu/+ORHfuRH1nkOnty/+qu/OvmGb/iGk/vf//7L3myWw5OuunAsO1X+v/3bvz25xz3usX6H2gtoi49//ONPfvZnf3Y9LEBlSV9RB+353//939fx1pQB9SU9PboO6ILA/8mf/MlNR04+Sv5v/MZvnDzykY88Pd49SNYznvGMVd7P+ZzPOfmiL/qik9/7vd87LdtMV9np8ZjHPGaRhM///M8/+czP/MyTV7ziFetctgC/X/jCF6660zboMs/DkTh8z/d8z5Ln3vzKr/zKm93XiO3b3va2pScbfcZnfMbJk5/85NN7fMqnd232tkiPsiI9H/rQhz5qcnOoHl0z63RjY+PS46puTjfbeZCe6YDr7L7lW75lRUTkrXMB+XIIz3zmM0/e8573rKjB3/3d3506ra71XYejQ+b8GyrSeYZZjtLP88fwNtCnTq60Ol5OMsf64Q9/eH2D9Do83zre7/zO7zz5pV/6pdXZcnwg72RlaxDur0w6fHbKkSpTcEy6OlZOobLN72SVDugsb8fkkR0qe/n4/9mf/dlr8mXl7xvoVhmSX37g99d93dedPO1pT7tZfYecIVRWSI9J5shKT3mVH9v1hN55yEnMfEUPH/CAB6z2XPupPK7lUB/72Meu/+pN+h/8wR9c/+n3x3/8x4u0aIfw+te//uRzP/dzP4r8ZhOy5c9hIkfqA7HgPF/3utetNMr1Hd/xHctJ01ma7/qu7zp5whOesM4rX44/udJwluQgYF/6pV+6jk+yAk960pNOvuZrvmY54F/+5V9exyKdvv/jP/5jPWhw9j5wJC7H4VZRFvohB+R+8IMfXMfTURl+93d/9+TBD37wyT3vec+TBz7wges4sKl74E1vetPJF3zBF5z80z/90/r/rne9az3QNNSl/mc7AjKRzLe+9a3r/1/+5V+uunTfVYd/8Ad/sOoHwdTu0qm20nfH1c1DH/rQRTq0eXn+2I/92Mm3fuu3npJOdtAXvfzlL1/nq78/+qM/WvUx7131kuzbIj0grWu0J22vtjrzBvl2DGoHGxsblw7nTnrImx2bG/7Zz372yWtf+9r1/0u+5EtOnZgOAWmoEwkRDukMN1kA7Mu+7MtWpxp0pL/zO7+zFgjjSDxJe+rV2b761a9e/3V8njQDeb/6q7+6OtVv/MZvPPnu7/7u9bQX6M3R5PwAEfNUK4rwfd/3fadPzfDjP/7jpxEBMusYQZn8n86Zcy269eIXv3jVQR37L/7iL67IACJhMuT3fu/3njr45L773e9eBJIzNTz1p3/6p6fy2VcnL6LxW7/1W+sY9PRrOIoD5jREJJA0jk19sQsn+LjHPW45e0/I733ve29Wj//4j/94cu211y6neP311y/7Puc5z1nn5FGdzs7/h3/4h1d56fv93//9y3nP9vYzP/Mzy66c7ROf+MTleDtPzq/92q99VPvkJMqjPP/+7/9+kR1Ebtad83/zN3+zdJ7E4e1vf/up0+YU1etTnvKU9T9wgG9+85tX/WR/9SFvNtdulW1CnSBUznuLh4yGyugtesO+1dmxbN0HXoHm6KU9C8iYj7r+lV/5lXUsRxu0JTK0Z3onu/YQItkgX6Tjsz7rs07+7d/+bR2Dyk9v7cI9iVTJrzoA96mHmIDkeLBx/9eW573uPtdGfvInf/KmIx8BwvfSl770lBAgvx/4wAdWHT3kIQ9ZxyC9J3EAdaSf+Yd/+If1O/21j/e9733rtygl4jiBTLpHuiehtgZ0/1hID0T0tAP5FLmcUUogK9v0vbGxcelw7qQHdKzymU5TxyPPOnxPpJy/Dk9nK+qgw/XbE490HLxOkSMTfRGqRnTqxDgFztcxDkpY3dOcp3pPcAgE504XT7+gU/uzP/uzlR/H9amf+qnLMel86CsPT6ry8MR/r3vdaz2xcqxC90V0OIvZgfekPZ/W+q0Tve6665aTuvHGG1fHK0rkGPs7/+Vf/uXLkTzrWc9auvtN15zK7//+76/hgt/+7d9ezhNBKVrxghe8YF3PDoY0HvWoRy279DT/jne8Y9nmec973io356zz9lsn7GMvIYRQOB6BMhRUx22eyzXXXLPsyQ6GGdTddHAwnRAbInIIBnJmKAbhAmWWF4KAtCKWhhZ+/dd/fZ2nt7YgoiACUJvJnrPNyrP2wD7ID3umC5J6n/vc59QpaZsct7Sl4ZToo04jBdoRIjYhn+pc20HYyKCf4/TPkZrnY6gssCWbcMblOx1e+lXf6qHhLefoVTn7Rty1SefTiy7JR4yQ8VB9wnTsoQicBwz2L9IG8ixfZS8KBfJXJ9pcbaKoHhshSUCv6dhdo91FOCMvZGs7EElwf4kWG54kZ95n8k+37OA+Fj3OFuzCFs1D+4mf+InVhoEsMhBI9dc1MEmdNLdFeuSTzpXVPamu5lDszONol42NjUuHcyc9dQigY40MQL+7wYXKdXo+97vf/Zbj5mxABKYOW6fkY+jga7/2a9cx4LgaM/ckJZohVA6V09P2n//5n6/fOZk6Mp0RR/wLv/ALpwRBBOD973//uv6bvumblh5zOMZ5TjPMCEKdNgc17UBHZZ1yHNMxBw4e4QschUgYGJpQ7oYAyPZhX2VhJ0/1EEFAUsjjDOR9ww03LP1yFp56PQnDD/3QDy1yqczkcVhIyNOf/vR1DIkU/QkmJXNwOabqM/uC66ZjZWvDCT1pc4byheqD7rO9IGtnIadSHQcOsUgPPaRDPgy5QOkR6Hvf+96LFMhTPZun0r2gnrQLjqp6nE6KfTj3GenRfsxbowOZZBsqVXfly96cJmJ2jE5MUgPIsYhH9qjMkJ6iKBEKSFey2JQOHDt9ku3bZ9rO+WRqH4iZayeqVxCBi8BOuH+dm3X4bd/2bav9TYiupavzMzIJHna6JhIKP/VTP3Xyzd/8zTf9+wgqR+26cmj/DdGVl2OIk7QiPbMMbGCoUNknjrb6WCM96nfaQaRUufY6PhsbF4tzJz2goyC3jlYnMzv5HMhXf/VXr45mdg7pw+kiLKIBhqG8KYXQPPzhD19p6C96IfKgwwJREhGS2UEjU3Xg9NEpcxaIAlKBOOU4ODOkRiSFDE+cnvwe8YhHrMiM8L1OkeN2/qwnwjrfaWfy2FpZkDplIDNSR47fnKHfZIjC6OCTx3mJiPQfIhXsgODoRLPffMLmiOebVuzlaZ7z14GzmaiEYR7DajZS5PCLvPj9oz/6o+t3deUaTp4+2Zus6pweiBTHz9mIchVdoqdoEluzrzoRfQtHR+P/nPcU2Lx0iIpyIqzTmRgSNB8EqiN2pkuElbMW6QHy6K582l32zq7VuQnsnJh8O2d4tTk06rxIApBrqO2TPumT1jBeiAhnNzBh29we9Up2ebJzeYF6MXQU2H8STRHKhsimPQO5x3KB+oo8zutK89M//dOnES3o/nM/qUtlyW6GFt03E8l0HeKhnU07I/i9DVla9yZypM9IZ/bouuoWtBXtG9FwvPapjYuGgkiPe5H82pb7RVtxLLlQfux7W6Snttd94nj20fb3Oj4bGxeLCyE9Hwt0HKIFHGedCNR56YA4HtCJ6jikm52bJ/gZddEZu0YZ63wQF0MowLFxtOYr5GSQgzlM47zOCURi/vmf/3l1gNMpTX1nxwvZt44OODvkKlsrQ+fJdVxni8AFv5G88jLc5NXaHM+UTzYnC2TRSRSiN8s8NRftCpwzvYCT4XjILr9ZRs6dQ4fyR0hFyECepc8WkdX+S6MuEDdwnLPhhB72sIctZ9YbfmwyHYD/R9JTmunkOTWObqZV9+wD6dIEW2BHjkhUK2g7nLroDyhb9e+3shhmNNQ5yTx7sCW91JW5MSBfQ0uO0dH1IbvN8gLScZzTM68DhAHJAPolq7bB1iJ6E9lr2s7vrvWNqNaeQsQBzOXSNit7+anf2gQ4z0ZsNdsIVBZty307z2m7sz5Anbh/9RmlTYayp192dO92P1V3Io3d2x62yIIIiocm/UEon9oNIK2gzMmFhvNuCx6YRLe00fKdbXhjY+PS4rKTntlRePrX0YQ6AR3I85///DXsNd+eonPX64g4BcMXjumghK7nE6iyFkEBT8Wca45bx2NoQ6cMOrIcp+EEE3AbwoHp4GA6AtAxH4+BMDtZXgOmd53p7Ow8XRvSAPnQgX2AvjrKoi1BlMCwis7b5O1sQy55QumOcQCvec1r1jmEy3EOiiNmA8NMojxdb0hGu1AW8kXdnM+5Acc0bcNetSVzgExONmE6mWzTm3FAd3bIoXBCHGRtAM4a3po6BPZRLpGeHJ10tXVtoreqALmaURgRKfOnXFMZtAMkhT7JaU4Gm6irIkggneidIRjlUgeigq961atuSvGRiduiaPJhF3KnQwV2ooP6b/5YRJ9cdeLbMZN6zUPJxumZbHOIRFqyT8d9ugcgHSq/9uRhgi4grWt9pEGmEcUJMpWdDWYdshFbNXw85xUZkvbAoW1p8/LWHmdkUt6VS1lFk6TtWLqzScf8dl8jYNnO0GJDV3Qw0Vt7DMrqhQUEDMia8nzgTne6083mOnUPqxe6KMOtfcBQr3Kwp2P1K2y7sbFxaXHZSU/56cw4AI4zojA7Yp2MzlfHjhiJRHgDSFSgN6jMeZjREZ2uTj7okDi35m54+0uEQxTJm1c6W4TA+L7OkW04yIZ9zOdBHsxpEQ7nLA1zNbcGXEPvOkXQmSlT5eLgEQtRJEQAyfIfacseIjnNTwJkbj5Nc9rm/ZhMTA/Ohf6A0AjVI4reEGtoBuglvQ6fs3ruc5+7HILOW6SH7jpxQykmRnNCyKO1U4ruWM/nzne+87IbO1x77bVr2FA52PhYdjBxWTTI223NxTA0gACyBzsaSjPMRQ6S8bKXvWxdy0He2kTm2U7khzDRDcGln/bCeWZbpE27MAHbvC/Obq5Dg8yoC6RYG7FmD3vl0JDw6jIiIF8E2mRnk8wRGq+wI3zdY16T1n5f9KIXrbphY69ET8wyuY58kRSTzbUJdaYenKeD82Rw6PLzxp6JxYhF5UUmnO9tPGRhRmDono6RAjZ2H2gr8nV/sGlv3ElvqNB9iIBry/QSDYvkeEChE1uwCduwUW0i2/lOV0N97lHl1c4QUENbkTRAgER5tCHRXeURIZwkofsE1BfC7F7W3rVBD1DezqrcIAKqLTvPzg0Tw2xjkJ20yauvvnq1ZS9B+O5jXy596q19ZnrzyrLJxsbG+eCykx6gg06FIzD8wGnmVOjTmDfokHSEwuAcVk+MIPLRq7WuR1J0clC5eisH5MnZcUQcvE7cOiGIQs7H22SzI9Ip69hFanTm3qzKGQZ51QHrfCMBs4N1nGPiKMw34ISKepDnPwejHNLSORKQPhwyRyrKwjHO14rpxclxguwU0pUsT5ccukiONDkreSoDW5mwjFxOGcrxhje8YUVv2I2dLQXgjbnK7Xp65xz8RyJElLydo06RKQ6Zrc29YXvkAgH0llfXgTwN3fR/Qj2WD1vTmzMmX54N67FhjtMbbhywN9vUO0zHihgjejaN7K0t5zoPtaPaqugWcsAuSCbCA7ONcs7m3iDr5i1N5wzJZ0dl8a08yuGBACHk5EG+0pu07pjz3shDVJoTxW5ksAUy6ENGEQyY7bL60xa0QfK0Md/0mJEZQ6TuBR/n5KsOg7piA7ZgE7ZpAnY2Y/Puj9q1e8yDhfsCQe717urYcCRip00iYvoN+c66oX9yywvxMn9Ou7dEBCQT6PvUpz51PQQgP/OhY9oI5nVI1WyngS3lfWufCaQJug9neTY2Ni4N/l+Qnp6ipnPoxk+/OrA6wEgJfeuow+xIQ2m6PtTRymc6oGM6SCd5y9f/5LpWhGTaE6Ye8kI60t05x0pDVo60NBPlNTtcmG/y9Pv4ZJo+9BP1COkr37PqPvv0Tc68BmZezqdneXIKH0sHntyJbOPcf//3f6/fs/zVGf2mXelQfUE60mMORyhzC/WB/9LOeosokn8kuEC3ypoOlTdb1F5809/xbCptti9915dmlqU0sx6c95+c6gUqt/L40NOH/PJwzSxvZZCP3+SSM+3rGNs7Ro7/s15mmyifrpd/ukNlnKgMx7aeDStr+ZDtv/TJq7xAXnq4R45ks/Kr384lu+9pp3SYkE5bry0ez5+F5NFbtAfm/byxsXFpcVU3ps7hcpCeOqUj6qDm9+xIoY7ROZ2hDmR2GL2NUx6V1ffslCbZcr3OvrymvOlsbs1Ork03OvnoCI/XlD+c5UxzZKAM5Ob8yGsbBpDHWR0xkF3nGiIQR/vrtMHxqW9yfbOd8+xeemCrYz7VH1Qex7Jr9obKJl8fzicdziKhyp/+bJMNoO8cWLInJvkBeuWYIT2OkKb6Ivdow9qOdP2eOMuRl44ObHTMtzy6Njsf63vK9nvqNssWqp+Z30x3JAf0dOyY77x+DiUm62gHes06oasy1b6gqNJcz2bqc7RReZQmHee91e9pl9mGJ9hGumzqtzzKtzpwrx/v31kPt4XuhUgPveU1ddzY2Lg0uOykJ8hfJ1IHcLzh/aebNDnssyDNrXXaMM/r2Oos2SIHDDkE5Knf5JU+Oa7R0Z/1xHqEDlbaOkXypj70rw4cd16nWgcbZqeabiHbSXMkC2eRB2ixRqgOQL6TFNLJsakzHafdcgDS+bDXUf/5v9/TxiFbB/kcHcxM4zdnOusi56l+2YR903faesLxbMwe/s8I2SwvlJ8y+H1W+eQx5c5ypAdUf12HnGWTY1vIZn0nRx7y6/6mb2X0HWFOF3B8ytZWksuuPjO9cs66CsmI1PgvbbJm3Ux5QN9jJDJ7VDbHZr7kTZmVWXnqK+jegwhb0Ck9j3aC2Q+Vf/pnxykT6DTvna67NXRvkX23u93tZtfMutjY2Lg0uOykp/zrUPo/O8PZ2dbhgGtmx1CH07HZgZz1RD7/+z3/Hx0/zCfTW7LTWc5rdqqVE45lUk7Q6fd7Qqeqky2PdKzDT3Zypy7TbqHy9F2HL+/0Dcmc+vs9nU/1kb1mWnB81qv8ugb6DslOrxzMMd/IA9kzT/afMifJmHUN2bv0Z5U3m5Qm+55Vt5DM9J42nYQAZn2nm295lM907M5NeWzk/6zDMNvBHMrrerJmnse2MusIzipPZZ86umbqAaXrWt/0K8909XDgXMfdE+k4Zcx2ANJNvWDey9D1vuf1s22SMeVMHbtmlq36lC75kJxb+kDlKtKjnZ51v25sbHziuOyk57yhfMeO13/lVOYc4XGoCJzvNzl1TjrHs5zVWY4SPM1NpwHJyv6TUHUMpqz5VFl655MFM5/qUid9zH92qrNDBzLTYX4f81Fex5Nd+aduE/0vfXn6nrKnLqXtu3T+Vy7f02bH+gbXZT9OMDmzvfs9y0vfPiGHNx1kuk1ZDZnMY+TUdugoDx/lTefyTybQtbTkOXesL3BcmmRNvYueTOI37eS6CFPEiLxZL10r7Tw+f888Z9ln9GYen9fCrZ27EsGWoKxXYv+7sfH/DVc86YHb6king6ljn0+sOSs4a/zfOZ36JC5hOgEy2Tubp1f/OePyn8NQnBMnN8tB5/R2fc44zHL2uzLNtNN5w3SmQdmmg5y2mVBW11ce8L/8py1C+Ut3LMMkJ8nMFmfVIyA28pn6fqyYNj1Cfn2O6JrqP/LAbmeVGWZZqz/12wcmQYFZ/zDPK/dsf52jb5GOqfvMvyEWesy6zeaVb14/281sh0c0rw7kebRRqGzy6JpjmisR2Uy5N+nZ2Dh/3CFIDyinMk5nyDHUyXOkHJT/deL+z86dbZwjy3GfSU66DpLrGkSpayGHRE4kajqbnPqRBIA8c6RknjXfJlTWdA6l4yj97hhU/zkn1yVz6i99ZU8nOoez5g7RZ+qk7POaoNwzqgXkz7pLFsco/TG/yki3aUd5Ol65KtNZqEyun3kfScSsu9aMYsfOl15ec3FNZXRtNhdtrJ6avNu14BwipUxh/ob5Srn8kq0sbFX66ru2FKa82mlRULpmh2O9ySdb+n2UC/NYc21m+5v3xbFcVyqqb/bcpGdj4/xxxZMe5auM0G+OzIJ/1mrhSKxxYjG2YMl+q+CCDlknXKfs+HSk84l0rikUIbn++uvXWiIhHTiRnEfHLLdvkUaw2KDF0UrDqZzlTI5QhzmTnEfy6Xp09M5Npw7Hp2znp3NP3pRl7RnruQQEo+umk2THylG+nLu1V9gqmfKYTj/dy/sIx8n1mU5z6jjb9zzOXuTP+vB/5s/5H6+3ttJLXvKSRWZqHzDLi4jQZ9bdPM8Gx3p1TLsM/s9y08NKvkD36ttxemij1q6xWOfUa7bbCWW1UKQd8K3/NDHtBN0XZHVOvumnbNmJXFu3WFPnqIsyu55dLTppAUpEsDbR95WMabNNejY2zh9XPOmZnfGEztUCdFb+1flaXM0idjpyDsQielZtFUGYDsmqwSYc6sR14NJyaNNuMz/nrTBrIUNI1nR6gYOghz2UnLeCsVWSySO/PPyXdpIQ/yfBKe10/tJM3Yoy5TDZZDpFaef1UFr6dS496G2BuolpF+lnuSMU2cQCixaGy9nNvDlHx8sfyJp1cxxeVF5pKnMOmlznALGYNjnCatYWyAtFPThwe3gps4UytZdWVzYnJt3Z04a2FuYLyPCcUBzowZZIkgUn2ZKNHJ86KrMVua0kXfkrDyCO9LHvlzZsteQJdopQsYlrreJtxWJbXViZ2OrftmqovrQV13lQcM9YuE9dlO8t2fC6665b20iwoxWyWyE9vdns7ne/+1oEks62qbDI5pHkXamojOy8Sc/Gxvnjiic9MDvPHJ/yehXY1hU6WFsV2LW5Tt5xjseKr4Dg6Iw5A534jAqFHKI8OLscn802yZlDNnP4KPIBVopt40PfLYM/64XDrEz0muRnYpIZSB/XZAeYDnjKyhbz6Xz+rgx0k1aEyrYPwFmzq+PT/jDzBiSADKsF2+H8CHM8ImMRognnOk6OeqjskxTItzLBJHCz3CIeiIOtORBc5EOa7Kg8dgq3ajDI2yre97jHPdZ/kF6928LBfWU16SMpg7lWEB2tfo0YuKZtP5QhG9qmAzmwnUSEPbCDPaSQl7ZGUWYROCs2zygkdC3721izDVXh0Y9+9PpA7QOJQlzYpW07pt1h2lgkip5tAkw/qzO3uje5iOMf/uEfnt47tp+wejMc28mViOqVzTbp2dg4f9whSM8sUx0yKLttCMDQSp0+cmA3ak/TlsKv0/fEbzsA+1qJCuXU7Q2EDOnAPVVbwr4OG0k4RgvaSdx+Vddcc81yiOll6ICTRYTsV2WTSM4iB0230nLCnDOiIG/bJrQbtmiB7ROcR544Uk/woimBXFtH2KrCvj+2gLDFB9DfVhWiCXajtvniDTfcsM4BZ83x2TmcIySDg5tbRXzoQx9aG3c6Tj/DdXNiq0gCYskGIgyiJqIi6uUsIucYIsHp04v9lKc1hlxnCwsOXH7SILNTlm0zkKs5dBTU5yQRMMlApFH0j3zbJYDj6hlRViaYbU79t5EuHX3YtzoFx8BxOshX1E8dQXkH+YiKTEIEiLttFqDyIDyIUJj5gp3GkTOobSHb9p4KrmFHMt0bNl+dyG7SkYHgGdIVufO/80iNyBiIGrXzfPYyxKVcrp/lulJRGdlok56NjfPHHYL09DQKynd8gpxDA6VFEt7znvesp872OkJsXM85F+lhP8RBFMhvE1A5bvsVBf+RKjZGShAjT+Rg4qshCPsYTdBR+mN9pCsHJNpgf60cI5Jj486u4TjtzC5ywRlx9jk/T9bve9/7VtTKjux0lw5h43AQGmQkPe3lZPPInLq5HyINvgHB4cDa5wqkty9UsO+RfZ+A/khWc51cb0+u6ZyVv/bZN3l050TVD0Jl13w628Ec8YiMmEuCpEqbPW1QWfTOseTC8Tdb20zTprAh560ObXw5CQR70aFomPy0p3agn3U526DfnfObbdQjW3a8tkAe3URPkE3HoaFC0SHDosF5pI1uM0oHbKY8CI6Ndyubcqtn1yB4UzfwINDmtKE2GFzDztogZCd7gKkzUAb1AZUbmdJuivxc6ajNqadNejY2zh93CNJza5gdd7/ZQjQBQfHkycEhMe1ijvTkTIOoiyfmt7zlLetJ24ak5OnMi7BwMuYEib6A69n/Gc94xtogk2OQXrojZl6e+jl2jgo6Jz9RmX4jW20s6RqEjEMB9Sx6Y+J0bWC++SOiYod14ATpZX4GeaJQNiotKhQRs5FmQzLIjEnikHzzNwyRgA1KkSZyOy8aYudsxyBHqny1S+XgEDlME3WRHBERTt8karvkz6gIm842XR0fbSyP8g3k2Iy2+VjaRdezc0OP6Y+EqMcISI4ekSvSM+vRbzJDstkT6UZWOoYQAB1dUySmsmZHtnAtKLcP8oHAhGSB88hjdZXNtfu73OUua4hq2pM+IjGIJtBllmHWp4hlUafkIt4icBBxg4YOzZUypJhtr3RkKzbcpGdj4/xxhyc9lZcdckhsoWP3tOsYsqOjbtKrJ/eGq1wvEiAiIKqCCJi3MOemIEAIhLTC/Ry1YR9hfvNgOFYOPAcXprOZDtnvD3zgAyd3vetd19CaD50QhoiZMiA9dspOjrIYRgIOGQFB3jjZ6QgRAlEku9YHTosTE5UCBMfkXPmkt2Ecw1vyI1ckhxwfkQs7thuyYwfkiM4TrmHDOXeGLpEHYFuyRBvow/HLs/pDKg09OW8oqzfoRDnm3ClQbvoHetHdse4LBIJec1hOPvJoV/xel0eE7OQ9IV/lFOmbmHWdDrO+RRUjkBB56yMiUpSEjWofyFXDR+Xxwhe+cOmWHcuvaApyjwyXv7ZgorIJxoiy/Ka+yCpyMutF/tOWftPfw0MQ1UQKPUSwIWLTywLBg4NIkPlHU/6VitoZe23Ss7Fx/rjDkx6dLyh/joNNdOyecnX2N9544ykB4ETN6TF3gnP+13/91xVdMDSUwxTCN8cFyOLIDW+A30V6gms44GzvmvSqfsBvaYHTu/Od73yaLkxH0XyUSWhyQq4TgUAcgFxljXCIZj33uc9dOlUuk5RFh+jqCb65LkCet9REGvw2IZvjPg57FAXhnOXPYctXPgga+4RjWxRxQeSmA0YoONciN8rPUXPaiKWhnpkepj3gSAZAGfyX35wH5bgPZ40UN2T0X//1X4sIcdbKjGBFIrQXbUL9WZ+G/YCt5ZFNIB2USxub9Slf0E4RBm10gjxDYt6Eqt2woXk0CHGY5AqUIzKrPPQxl0z0p3uCHvJ3rQcA83Em2Dj9QBlf8IIXLHIM7ANIj7Kxj2hRQ13kqkNz2rSt8r3SUT2p9016NjbOH3d40pNTmY5Rh82hmLcwkbPkrHtyN9cFuZidtGhPk0AdF3UQyQHDQ6IRZOX8fIskpItrcuLqZ+rWb0/pokYmF0csOB0OjBwyRZ+aY0OOur366qtP65gzF+3hcHJYnI68kTTzmWbeyiQ/1yNAj3jEI9Zx/w2NIT2GUlxvmE+0DClsIjhHJzpCF3OYGtoAaTjnOaeHTtmEfZCA3myjszxNqhWJAdGvojkIgGEbc5agMksrmgDVWSTAPZAtk4P8NTRVnQBS6+2tSMorXvGKFUXruuAa5KG32iZmm/E7wqnMCGNzj0Ltha3e/e53r4ghfenftdqFtjuHh5Agw4lFdso3mwDSM9dYEk3zUVfaatf4j0g2B21GaZybeP/73790VHfZ2FDvjHqJ+vSqP3ixQKQqgnWlI5tt0rOxcTG4w5Oeys+517FzIN/+7d++QvjTGXFo/htOEnVwrf+eoj39GtLiPDi5hz70oacO9Pj2VkNcHDwi4WnYG11HpxRm5z/rx6u+8vVkjAzIR7QhIFuGfoCu5HjKLjoRMUoGvSMi0ou60FFZOXTlDgiHIRHnXWMOkIhXURFlMA/KEBe70A8p8tZaBItz8wYWYuJ6BEwZnI9MTKKBhEornbIhHiJXEQrOlJ4cp6E0DlbkKVnKK7IgHWKRLZVlkjv5I6ecu3qSh4iPaE0wwdt5Q2jKhOCJjAHb+Yg0qWu6kkMfMiIv9KJD9Q4IM7sgA9dcc82yr4gJsCkbyE+b+bRP+7RlA+QkyNdr79oB+9NxRs/kqV2SpczpgvC4xkR29awtiF4G9kJyyTPnRjtC9ls5OmRrkIe36UxwV0fqlj1AWyTzjW984zrPjiJiyozURXavdKgvYLdNejY2zh93eNITOIDZYb/+9a8/JR/ZCDhEqzUjQjXborYAABHsSURBVJ3XSZs38bKXvWw5UB22p1zgYLzZJX3yXcehcDRve9vbVkRi5hUpyOEfHUBycpbvete71gRREYwiDV7j9jHMA+qVo+ltrOoZARIVEM0weRWKHsDb3/72RcjoGebwkLexlNsx+ZlgPefReMrntL0BJwqlTOXN4XobyxtPhutcl6OdZKehEZAHWfRhJ3ZOH/8NmSBeyB5dIjNsJl8LUh7tWRq2d45ehjbVC9uY82K4p4iVOga2VX7Da94+g2TTyVAXGdqLSbsz70lkga3oR2f1KL2365Sn/ICOyXvnO9+5SJA8GpYK9DZB3urK1cckdtUBdFyUT3l81Ic06iHSzw7sLW9p/a6tkkG3Wa7uG+kNa4noSFe7ZWdtzVwfEbgXvehFq72kz1nLClxpyEZ39P53Y+OisEnP/6FONlvA/M3ZTUc/nQsnVtqcQ/JyANOB68iLAAGyM8lQUZizkNy+gdOhQzJCzgiq03mMjPRw7TwXKudcQK8yQlEC5TvresjJHxHJg0mE6ERu5ZkOH3KYbJts9mc318x6g2zlfLZ1LCIwcUtt/6y0ZCTbdT7yT0bn6DPr/1j3QfrKk12h8ihv7elYxgm6znJUh3PYjQ7Zoryqv9nOj1D3yZY+PRw7tvXsUXmVbUa0Zhkqd3KSdUdAdmCrTXo2Ns4fm/T8H3JQwAn0n8OY53TOdeqzY54deI7s+HQtzXQo7A23ZO8c6JQ9nbbz8kq+tI5Nx+gY5zTJTb/TM4cznfEkNvNpW17pm17l51y/5TmJITgmz/I92q/jcFYadp9koHrIjpDjhpx8srI9Gcmh87Rf6Bo2yRbJzu6hcgEZU+epD8zrJhHqmr7Zw7XkzXpJR9/KIN1RvzBtdSTpgU2m7adO2dV5Npry4CgzGbXRiVlHkM7kpnflrIxTzysZ7AtstEnPxsb5Y5OeC8J0SpzbsVOfDjGnoG7mddLM+pmOPJCbk8mhT7LVMUhW6af82gVwho6ny8wjnEUecmTJ4hDTxbGOl458sh2fcoI8Z1nom92mbmGWx+9ZJr/p7Nu5rot4nOW8pY8YzPNkpHP6Q7o5PsmQcsx6uKXfgcyurxzT/se6mPZMB6iM6QdHXcD5ytk5bWzm4/wx342PH9UFW+7+d2Pj/LFJzzkjQpIjOg6VsH9pOKWcaQQApFE/1Q0H6Hz/fUt7dF7HunRdacic198SigaEOUQRGUpmOs9IERzfaDqeVzaf6aDpyi5kHssF2RPSr+uP6elUGvJ8zkKEKoIh3SRZ0LlJCm5JXvUX/vM///OmXx8BWZOgTBxtFGa55d08I7bSdorA1KZAHbluHjtLPn0q34S06mfi1trMxseO2uXufzc2LgZX7Zvu/HGWU5zkIeRwJnGYhIFDI2uSg+mMqjvfHY8ATGcJOe3pCP2e/6cDJGeSn+nQj84d5E9WTlj+dD+2r0ig9Mk5K8oi3SQz0mZXMqdcZYus+Gavzsun39Ipk+/s49y0b5AXvbJbmPYC6cia99WROJ1VvjDLFI4yYZ4/Emk4qwy1Cah9STflzjSz7bG9tMn1/9imNj5+zHay+9+NjfPHJj0XgPm2CmfhNWpv4LB1xML30VHlUOf8icD5mm+j3siZJAD8n2SEA8uhHZ/muz6QUzuYTrD5PV3fufTmzCMmk6DAJAd+u6Y8LA1gL7N0OF7LqbNZmLpGQqYdw7SHN8i8Xj2Pzd/gzSkLLnoTT1nTTx5TJ/lPIiOdsh9JwLE+oWNdY5K4N+8qEzJSGvU+7T/lSx95qhzJIHuSvqJBfU+S41p5zGNAB29VeQNszus6i2Bt3H7s/ndj42KxSc85IyecQ2qBvRwQePXXIni2FbAOjfVsfLwiDNM5z8XggDOejlH9HR3YxCQfyFgOdjro5HXsSBTSQbrjMMnRAUsTMelYOrCN815ntu4M3aceriMPKbLGDbimPIpEuG6WS5oZTfEGmLVgvAIepn6u91q8tXSs72PNmF71p0/2ZOuZD9ySrY/1TufIg/w679V4aztVpiPhA8fmcWnnfxurWmvJq+HglXfliPikQ5A/TBKVPlD9K6v1qmw30jUhfTc+Mez+d2PjYrFJzwWCE0Jm3vrWt9505CP7EX36p3/6zXYjt4oxcmRBtxxQxIGzUWeTHIB649w4Q9d0HXD68/9ZmA6wvKB8RCSOMqYznVEeuhz1c35GrKy3Eyx+aAViIJMuU7bdzO91r3ut347PNirP/kdIJjFJZ4QGeeLcjxEZ5Em0xcJ4E2xN9iQYfs8hu/JO735PHbJnxKJzoiaI2FyZGpw/Di0dZYB8Kp+yIaDOI7NtPNt1U173vO8IrOuqs2l7hMoCk+94xztuRiS15SPh3fj4sfvfjY2LxSY9F4AmsFowr80gORbO06J2ohCBc8rpTBJhJV9bO3jqtkqvXc4hp2ahusc85jFLvm0HRE9c19M+WP3WqrqiKr5FBuTBudsmw4q5PlYW5gTpwRFa6M6mqqItVju2pUHOVv7ymc4YWbOFhdV7bTZqKA8iBdI/+clPXqvz2kDUCsMPf/jDlyxyfdq7y+rLVrO2qrA8IgxvfvObVxmswGzLDORhtt1Xv/rVa5VnK01bmfhud7vbiqpMcNrK7x5gTysSG95ii9Ymso2HFbfZdW4mSg/pLA5IFzZpawYgcxIJQ2e22WAT5XUN2E7Cis/Saw+G4axibKVlKx5buLF7VHSQfvL8i7/4i7WytG1QgA3kpc6s6oxIaTM+2hSibQVvemcnhMaCgNVd+RTFSXebxD7xiU9c5107yc/GJ4ZsvvvfjY2LwSY9FwR2Rhrs0ZQzASsQW9Z/bt4JkZXSGr5AZkSAEALDDrYbCFZFtmEnx/6GN7xhnfcBjvCVr3zlcrgcpUiSDVTt8A5+c+pW//WxxcBTnvKUUydnGwmrDhs2ec1rXrP0OAs5S9svvOQlL1np5ad87QWF2NjSAYkSPUBO/LebeXja0562yIrol1Wir7322rXHVuCobZNAF3I5ZWQNEKvXvva1awgR8RMBQRTvdKc7fRT5Coa2kDOkB8khH9gXMbP6M0Jjyw55VU56Ixds97jHPW6VJdmTBIrm2VYCGWQTxKbIllWq2TfyavsLm8AiceSRj1xF9tSNtiBv5VLv8nLM3mPqDEm0/xY5bZeizYhkdb8rA7ted911p5GrSHaEFqQ31FfkSHusj9iRnk8c1cfufzc2Lgab9FwQPB3bg6ktFXKcnBnnZviFY7Q3lL2UOCnIATknMpNTRWw4ywkyc54IwxyuQRJy5mRycJyloS9558A4NZGpdmO33QDH67jr0ns6vxkpKP9gN26OGiEDk4QbzkmWoaX2hxIRMZyCHJArDwSAjs2DskeTbUIgHcyHaosNkbB2jwdOne0RjNo7+J19TZQWAass9ECCfANdbZYqH5AOITLRVx1GTsmMPCRLFMk8oSDPiAYi9oVf+IXrOp/IDdiRvaiP/H1EnRDSZGdD84Ka08MObDjBTnS3ZQWI/khTe5z5Voe1NXZvLy7tJJvPazZuH2qP2sTufzc2zh+b9JwzpmOwuSbkIENvd3HuogBPf/rTV3SkjTQ5UU5fhGZGKebkXBEPjrXNQ0UlODnOUR2bIG3vp5wkIGImSxv6ERUSwTEsZZiMbOfljWTYXNTu8M9//vNPh99qOzAnZiMCIhnIDTJDlkgR2DfLkBW4nn6GZhAVEKly3bQbZ3uf+9znpn8nJ/e85z2XfMNEj3zkI9cwlnKbEK79iqiJEJGRA0csIgWREuWgg48Ii+iJuqGTvbYilTl60Tf1ELkSOaP7BPse7WMeF2Kn7iIrQZ0ob/edfdQQNIRVPSJeCE1AzCKQXaM8dNUGHENUkWT6lh+SZXgNgQJ6t0t+afQBtc3aSXkgwUXKImyzLW3cPtRGdv+7sXEx2KTnnMGebAuIx4yQcFbHIQIOiFNBDhCNhrn8zmmD4+S1Qafz5skEG4XOp31OsM055ZEOohecao4akIXp0OjP0XPchnI46WPECsgw78X5IiSAhCBz2prhFuRq7qll3olIgnxEYyKHQL68DNfkbBEejh0mOapMV1999SkZBMNLbKX8c0LvBL1EpECe9DCkM0kK/ZSFLRxH6CbpUT5pIlXB0BuyCHTsPBKkTslEzgwtIlXN93FexIrNgWx2MgQHERR2p+uNN964dBBds+v7hDRILBJlvpJ8zAsCcqYdj2VwHimdNpVP9t64/dj978bGxWKTngsAB8JxeILneDsG5rXYjZuj5ZDVAzzzmc9ckQfgsBAJ1xa5uOGGG1YkIDhvMjNIYx4KBycfzlNacz2C/JAIb++ICHG+kQpwXY4wnYAuymGYxG9oYqv0IjpFbUSw5CO64LjzhvIadkMckD5zU8jU9jhk5fZ2V23TvBWRhtqmqIZoR4REHtLSR8QJiTMBGMGLXIn0FKEJ0iYT6SkCBYiS6JEhJvmQZa4Q2eVreEuEKPIxwWZkO2d4SySNnoG+bGwiMxInrd3473//+59G81wr2sc22fohD3nImiclPRm1B/UfKUZkkWDXd12ghwiP6BMZs25NbI5Eg/qSh/pVbnN70m2SpI3bj9r47n83Ni4Gm/ScMyI34Cn9ec973vqds+LAOCxv3Ih4PPvZz15OkpP2lk6RCdGP66+//uTnf/7n1/CRoRUTeTk1zrKhHlEAH05NpCeH7M2dT/mUTzl50pOedPKsZz1rOXlOG5AOkaDHPvaxS76JxP6D4RbDW0gYgmbiq4hIDnyWD173utett47IME/GW1miNMhB8Iq+ScLO00dZIkrkImjyVA66muQsMhFEKPw3edhk5dK0tg5ChDxY8BDRMyT0yZ/8ySf/8i//svRFWrKr9q/Ni6whBHPxPXKUVfTKm2/syQ7A7sicieV+dx8Fx7qXkFqkjX2f85znrDV0vHUG5i4V2TLUJQ/DlCJI0rONSBCQyS4ibtm9+iU/0uONQGUW+TNBvuFT5RZFMqkbaQ6Ip/bIpvKXLmIH2iECXVRSnpv0XBrs/ndj42KxSc85I6fEri9/+cuXc+a8wDkfURnzeMxNEW1APP7nf/5npQF1w0kiRF6/NjcDAZnwBN7r6ByaoRLEBnLkrnGMg0QGRC9y+pzhb/7mby7C4tV6QyU5VpOmETERGASj17mh9pKTdI3Xt70NhSCZM4QYkCdqAsrmzSHRA7p6ndrbZXPhReRAmdlChGuSJmVFJBAVZMk5cuiiTPDSl750lQVxMtyDUGbTdK586kOUzDXVDdDXMfOjvOmGZEKEjy2UC6rneT9B5MoQHSKIaNIbiQLkATkDNmQD5PXRj370IqpvetObTieg001aQ5fpDmSIpFlxuuPqGpF2fBK5D3/4w2uyfBEb+lYeBNIHKgeYPD2jhKB8lXnj9mP3vxsbF4tNei4AnFmOxavU3qxiZw5qOo5pe0NN87/IRcNXHee4ONWj8zlubDknGU/QqYgTGREGx3KKEBGYw1+GPG7N6ZVnukYC2GLKDpGmZJ6ls3PZMZ2m8w+VCTh8aWrnxzlUQCZ5M3qRHslPZ7LTgczkdWyeCzNPx6WZNihfedGjyEw287/fE9Jmh6AO05lNs4U8/EaYRZKO9lZP8phtjiwES9QvwtpQprRn6bTx8WH3vxsbF4tNei4QbC2qYxihLSZgOg/OsP/ToZlfYnJwx6az57j6H3GB6aAh56qOp4OfEZZ5fY55pj3KJKs2NHXK2eZcpSnqIV0ylbU0MPNyrvJOvcqPHv2OkE3d5u+cO7gm5w0zz0luQnnPe0MZpszKMG0gn66Z+ZW2fJGiI8kC1882QKfKO5F+6S7PqX8yEcn73ve+azgUjjaZ5XM98mz+lWgXTNscydbG7UP1ufvfjY2LwSY9GxsbG5cJu//d2LhYbNKzsbGxcZmw+9+NjYvFJj0bGxsblwm7/93YuFhs0rOxsbFxmbD7342Ni8UmPRsbGxuXCbv/3di4WGzSs7GxsXGZsPvfjY2LxSY9GxsbG5cJu//d2LhYbNKzsbGxcZmw+9+NjYvFVW4yN5wFzO5yl7usm64bcWNjY2Pj/GGhyKuuumr1xWEu2rmxsXFpcNVN3ws2pLQZoZtvf/Znf/Znfy7mc/e73319h7kC+cbGxqXCycn/AhQtV9ncnjn7AAAAAElFTkSuQmCC)

Figure 1: Huffman tree example

In the preceding diagram, walking down the tree-either left (0) or right (1) to each leaf node-shows how the codewords for each character are generated. Therefore, after constructing a Huffman tree, the resulting codewords can be used to decode the bit stream that contains the encoded strings. The bit stream is purely a continuous stream of bits. Errors could result if this bit stream is treated as a series of integers, words, or other types because doing so could induce format errors.

### Xpress Compression

The entire database can be persisted to disk as a Spreadsheet Data Model file (section [2.1](#Section_49ca8d5609274cb2ad97bf73f0d91536)). This file will be compressed by using Xpress compression, as specified in [\[MS-WUSP\]](%5bMS-WUSP%5d.pdf#Section_b8a2ad1d11c44b64a2cc12771fcb079b) section [2.1.1](http://msdn.microsoft.com/en-us/library/3e24630e-8000-4894-a967-315df7ed996e/). This compression is separate from and in addition to any compression that occurs within any individual file contained in the Spreadsheet Data Model file.

# Structure Examples

## tbl.xml Metadata File

The following example shows the content of a tbl.xml file, as specified in section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246), for a table. As required, this tbl.xml file has an **XMObject** element as its document node (section [2.5.1](#Section_23dde626b187405590e15a2333f11c5f)), with the value of the **class** attribute as "XMSimpleTable" (section [2.5.2.1](#Section_cebcbc893ceb4a8394ebfa26fca0c416)). This metadata file contains the metadata for the example multiple-segment .idf column data file that is described in section [3.2](#Section_38f20e24dfab4bcda17343ecabe8a91e).

- <XMObject xmlns="<http://schemas.microsoft.com/analysisservices/imbi>"
- xmlns:imbi200=
- "<http://schemas.microsoft.com/analysisservices/2010/imbi/200>"
- xmlns:imbi200_200=
- "<http://schemas.microsoft.com/analysisservices/2010/imbi/200/200>"
- xmlns:xsd="<http://www.w3.org/2001/XMLSchema>"
- xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>"
- class="XMSimpleTable"
- name="Table_1_51adc096-9274-4394-b47d-a2fcabfbc1de"
- ProviderVersion="0">
- &lt;Properties&gt;
- &lt;Version xsi:type="xsd:int"&gt;1&lt;/Version&gt;
- &lt;Settings xsi:type="xsd:long"&gt;4353&lt;/Settings&gt;
- &lt;RIViolationCount xsi:type="xsd:long"&gt;0&lt;/RIViolationCount&gt;
- &lt;/Properties&gt;
- &lt;Members&gt;
- &lt;Member&gt;
- &lt;Name&gt;SegmentMap&lt;/Name&gt;
- &lt;XMObject class="XMMultiPartSegmentMap" ProviderVersion="0"&gt;
- &lt;Properties&gt;
- &lt;FirstPartitionRecordCount xsi:type="xsd:long"&gt;0
- &lt;/FirstPartitionRecordCount&gt;
- &lt;FirstPartitionSegmentCount xsi:type="xsd:long"&gt;0
- &lt;/FirstPartitionSegmentCount&gt;
- &lt;/Properties&gt;
- &lt;Collections&gt;
- &lt;Collection&gt;
- &lt;Name&gt;Partitions&lt;/Name&gt;
- <XMObject class=
- "XMSegmentEqualMapEx&lt;XMSegmentEqualMap_FastInstantiation&gt;"
- ProviderVersion="0">
- &lt;Properties&gt;
- &lt;Segments xsi:type="xsd:long"&gt;3&lt;/Segments&gt;
- &lt;Records xsi:type="xsd:long"&gt;2101256&lt;/Records&gt;
- &lt;RecordsPerSegment xsi:type="xsd:long"&gt;1048576
- &lt;/RecordsPerSegment&gt;
- &lt;/Properties&gt;
- &lt;/XMObject&gt;
- &lt;/Collection&gt;
- &lt;/Collections&gt;
- &lt;/XMObject&gt;
- &lt;/Member&gt;
- &lt;Member&gt;
- &lt;Name&gt;TableStats&lt;/Name&gt;
- &lt;XMObject class="XMTableStats" ProviderVersion="0"&gt;
- &lt;Properties&gt;
- &lt;SegmentSize xsi:type="xsd:long"&gt;0&lt;/SegmentSize&gt;
- &lt;Usage xsi:type="xsd:int"&gt;0&lt;/Usage&gt;
- &lt;/Properties&gt;
- &lt;/XMObject&gt;
- &lt;/Member&gt;
- &lt;/Members&gt;
- &lt;Collections&gt;
- &lt;Collection&gt;
- &lt;Name&gt;Partitions&lt;/Name&gt;
- <XMObject class="XMPartition"
- name="Table_1_51adc096-9274-4394-b47d-a2fcabfbc1de"
- ProviderVersion="0">
- &lt;Properties&gt;
- &lt;IsProcessed xsi:type="xsd:boolean"&gt;true&lt;/IsProcessed&gt;
- &lt;Partition xsi:type="xsd:int"&gt;0&lt;/Partition&gt;
- &lt;/Properties&gt;
- &lt;/XMObject&gt;
- &lt;/Collection&gt;
- &lt;Collection&gt;
- &lt;Name&gt;Columns&lt;/Name&gt;
- &lt;XMObject class="XMRawColumn" name="RowNumber" ProviderVersion="1"&gt;
- &lt;Properties&gt;
- &lt;Settings xsi:type="xsd:long"&gt;1025&lt;/Settings&gt;
- &lt;ColumnFlags xsi:type="xsd:long"&gt;31&lt;/ColumnFlags&gt;
- &lt;Collation/&gt;
- &lt;OrderByColumn/&gt;
- &lt;Locale xsi:type="xsd:long"&gt;1033&lt;/Locale&gt;
- &lt;BinaryCharacters xsi:type="xsd:unsignedInt"&gt;0&lt;/BinaryCharacters&gt;
- &lt;/Properties&gt;
- &lt;Members&gt;
- &lt;Member&gt;
- &lt;Name&gt;IntrinsicHierarchy&lt;/Name&gt;
- <XMObject class="XMHierarchy"
- name="\[Hierarchy for column RowNumber\]"
- ProviderVersion="0">
- &lt;Properties&gt;
- &lt;SortOrder xsi:type="xsd:int"&gt;0&lt;/SortOrder&gt;
- &lt;IsProcessed xsi:type="xsd:boolean"&gt;true&lt;/IsProcessed&gt;
- &lt;TypeMaterialization xsi:type="xsd:int"&gt;3&lt;/TypeMaterialization&gt;
- &lt;ColumnPosition2DataID xsi:type="xsd:long"&gt;-1&lt;/ColumnPosition2DataID&gt;
- &lt;ColumnDataID2Position xsi:type="xsd:long"&gt;-1&lt;/ColumnDataID2Position&gt;
- &lt;DistinctDataIDs xsi:type="xsd:long"&gt;2101256&lt;/DistinctDataIDs&gt;
- &lt;TableStore/&gt;
- &lt;/Properties&gt;
- &lt;/XMObject&gt;
- &lt;/Member&gt;
- &lt;Member&gt;
- &lt;Name&gt;ColumnStats&lt;/Name&gt;
- &lt;XMObject class="XMColumnStats" ProviderVersion="0"&gt;
- &lt;Properties&gt;
- &lt;DistinctStates xsi:type="xsd:int"&gt;2101256&lt;/DistinctStates&gt;
- &lt;MinDataID xsi:type="xsd:int"&gt;3&lt;/MinDataID&gt;
- &lt;MaxDataID xsi:type="xsd:int"&gt;2101258&lt;/MaxDataID&gt;
  100.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  101.&lt;/OriginalMinSegmentDataID&gt;
  102.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  103.&lt;RowCount xsi:type="xsd:long"&gt;2101256&lt;/RowCount&gt;
  104.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  105.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  106.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0&lt;/OthersRLERuns&gt;
  107.&lt;Usage xsi:type="xsd:int"&gt;3&lt;/Usage&gt;
  108.&lt;DBType xsi:type="xsd:short"&gt;3&lt;/DBType&gt;
  109.&lt;XMType xsi:type="xsd:int"&gt;0&lt;/XMType&gt;
  110.&lt;CompressionType xsi:type="xsd:int"&gt;0&lt;/CompressionType&gt;
  111.&lt;CompressionParam xsi:type="xsd:long"&gt;0&lt;/CompressionParam&gt;
  112.&lt;EncodingHint xsi:type="xsd:int"&gt;1&lt;/EncodingHint&gt;
  113.&lt;AggCounter xsi:type="xsd:long"&gt;0&lt;/AggCounter&gt;
  114.&lt;WhereCounter xsi:type="xsd:long"&gt;0&lt;/WhereCounter&gt;
  115.&lt;OrderByCounter xsi:type="xsd:long"&gt;0&lt;/OrderByCounter&gt;
  116.&lt;/Properties&gt;
  117.&lt;/XMObject&gt;
  118.&lt;/Member&gt;
  119.&lt;/Members&gt;
  120.&lt;Collections&gt;
  121.&lt;Collection&gt;
  122.&lt;Name&gt;Segments&lt;/Name&gt;
  123.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  124.&lt;Properties&gt;
  125.&lt;Records xsi:type="xsd:long"&gt;1048576&lt;/Records&gt;
  126.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  127.&lt;/Properties&gt;
  128.&lt;Members&gt;
  129.&lt;Member&gt;
  130.&lt;Name&gt;SubSegment&lt;/Name&gt;
  131.<XMObject class="XMColumnSegment"
  132.ProviderVersion="0">
  133.&lt;Properties&gt;
  134.&lt;Records xsi:type="xsd:long"&gt;1048576&lt;/Records&gt;
  135.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  136.&lt;/Properties&gt;
  137.&lt;Members&gt;
  138.&lt;Member&gt;
  139.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  140.<XMObject class="XM123CompressionInfo"
  141.ProviderVersion="0">
  142.&lt;Properties&gt;
  143.&lt;Min xsi:type="xsd:int"&gt;3&lt;/Min&gt;
  144.&lt;/Properties&gt;
  145.&lt;/XMObject&gt;
  146.&lt;/Member&gt;
  147.&lt;Member&gt;
  148.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  149.<XMObject class="XMColumnSegmentStats"
  150.ProviderVersion="0">
  151.&lt;Properties&gt;
  152.&lt;DistinctStates xsi:type="xsd:long"&gt;0&lt;/DistinctStates&gt;
  153.&lt;MinDataID xsi:type="xsd:int"&gt;2&lt;/MinDataID&gt;
  154.&lt;MaxDataID xsi:type="xsd:int"&gt;2&lt;/MaxDataID&gt;
  155.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  156.&lt;/OriginalMinSegmentDataID&gt;
  157.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  158.&lt;RowCount xsi:type="xsd:long"&gt;0&lt;/RowCount&gt;
  159.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  160.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  161.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0&lt;/OthersRLERuns&gt;
  162.&lt;/Properties&gt;
  163.&lt;/XMObject&gt;
  164.&lt;/Member&gt;
  165.&lt;/Members&gt;
  166.&lt;/XMObject&gt;
  167.&lt;/Member&gt;
  168.&lt;Member&gt;
  169.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  170.<XMObject class=
  171."XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;"
  172.ProviderVersion="0">
  173.&lt;Members&gt;
  174.&lt;Member&gt;
  175.&lt;Name&gt;RLECompression&lt;/Name&gt;
  176.<XMObject class="XMRLECompressionInfo"
  177.ProviderVersion="0">
  178.&lt;Properties&gt;
  179.&lt;BookmarkBits xsi:type="xsd:long"&gt;24&lt;/BookmarkBits&gt;
  180.&lt;StorageAllocSize xsi:type="xsd:long"&gt;32
  181.&lt;/StorageAllocSize&gt;
  182.&lt;StorageUsedSize xsi:type="xsd:long"&gt;2&lt;/StorageUsedSize&gt;
  183.&lt;SegmentNeedsResizing xsi:type="xsd:boolean"&gt;false
  184.&lt;/SegmentNeedsResizing&gt;
  185.&lt;/Properties&gt;
  186.&lt;/XMObject&gt;
  187.&lt;/Member&gt;
  188.&lt;Member&gt;
  189.&lt;Name&gt;SubCompression&lt;/Name&gt;
  190.<XMObject class="XM123CompressionInfo"
  191.ProviderVersion="0">
  192.&lt;Properties&gt;
  193.&lt;Min xsi:type="xsd:int"&gt;3&lt;/Min&gt;
  194.&lt;/Properties&gt;
  195.&lt;/XMObject&gt;
  196.&lt;/Member&gt;
  197.&lt;/Members&gt;
  198.&lt;/XMObject&gt;
  199.&lt;/Member&gt;
  200.&lt;Member&gt;
  201.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  202.<XMObject class="XMColumnSegmentStats"
  203.ProviderVersion="0">
  204.&lt;Properties&gt;
  205.&lt;DistinctStates xsi:type="xsd:long"&gt;0&lt;/DistinctStates&gt;
  206.&lt;MinDataID xsi:type="xsd:int"&gt;3&lt;/MinDataID&gt;
  207.&lt;MaxDataID xsi:type="xsd:int"&gt;1048578&lt;/MaxDataID&gt;
  208.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  209.&lt;/OriginalMinSegmentDataID&gt;
  210.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  211.&lt;RowCount xsi:type="xsd:long"&gt;1048576&lt;/RowCount&gt;
  212.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  213.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  214.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0&lt;/OthersRLERuns&gt;
  215.&lt;/Properties&gt;
  216.&lt;/XMObject&gt;
  217.&lt;/Member&gt;
  218.&lt;/Members&gt;
  219.&lt;/XMObject&gt;
  220.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  221.&lt;Properties&gt;
  222.&lt;Records xsi:type="xsd:long"&gt;1048576&lt;/Records&gt;
  223.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  224.&lt;/Properties&gt;
  225.&lt;Members&gt;
  226.&lt;Member&gt;
  227.&lt;Name&gt;SubSegment&lt;/Name&gt;
  228.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  229.&lt;Properties&gt;
  230.&lt;Records xsi:type="xsd:long"&gt;1048576&lt;/Records&gt;
  231.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  232.&lt;/Properties&gt;
  233.&lt;Members&gt;
  234.&lt;Member&gt;
  235.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  236.<XMObject class="XM123CompressionInfo"
  237.ProviderVersion="0">
  238.&lt;Properties&gt;
  239.&lt;Min xsi:type="xsd:int"&gt;1048579&lt;/Min&gt;
  240.&lt;/Properties&gt;
  241.&lt;/XMObject&gt;
  242.&lt;/Member&gt;
  243.&lt;Member&gt;
  244.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  245.<XMObject class="XMColumnSegmentStats"
  246.ProviderVersion="0">
  247.&lt;Properties&gt;
  248.&lt;DistinctStates xsi:type="xsd:long"&gt;0
  249.&lt;/DistinctStates&gt;
  250.&lt;MinDataID xsi:type="xsd:int"&gt;2&lt;/MinDataID&gt;
  251.&lt;MaxDataID xsi:type="xsd:int"&gt;2&lt;/MaxDataID&gt;
  252.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  253.&lt;/OriginalMinSegmentDataID&gt;
  254.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1
  255.&lt;/RLESortOrder&gt;
  256.&lt;RowCount xsi:type="xsd:long"&gt;0&lt;/RowCount&gt;
  257.&lt;HasNulls xsi:type="xsd:boolean"&gt;false
  258.&lt;/HasNulls&gt;
  259.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  260.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0
  261.&lt;/OthersRLERuns&gt;
  262.&lt;/Properties&gt;
  263.&lt;/XMObject&gt;
  264.&lt;/Member&gt;
  265.&lt;/Members&gt;
  266.&lt;/XMObject&gt;
  267.&lt;/Member&gt;
  268.&lt;Member&gt;
  269.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  270.<XMObject class=
  271."XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;"
  272.ProviderVersion="0">
  273.&lt;Members&gt;
  274.&lt;Member&gt;
  275.&lt;Name&gt;RLECompression&lt;/Name&gt;
  276.<XMObject class="XMRLECompressionInfo"
  277.ProviderVersion="0">
  278.&lt;Properties&gt;
  279.&lt;BookmarkBits xsi:type="xsd:long"&gt;24
  280.&lt;/BookmarkBits&gt;
  281.&lt;StorageAllocSize xsi:type="xsd:long"&gt;32
  282.&lt;/StorageAllocSize&gt;
  283.&lt;StorageUsedSize xsi:type="xsd:long"&gt;2
  284.&lt;/StorageUsedSize&gt;
  285.&lt;SegmentNeedsResizing xsi:type="xsd:boolean"&gt;
  286.false&lt;/SegmentNeedsResizing&gt;
  287.&lt;/Properties&gt;
  288.&lt;/XMObject&gt;
  289.&lt;/Member&gt;
  290.&lt;Member&gt;
  291.&lt;Name&gt;SubCompression&lt;/Name&gt;
  292.<XMObject class="XM123CompressionInfo"
  293.ProviderVersion="0">
  294.&lt;Properties&gt;
  295.&lt;Min xsi:type="xsd:int"&gt;1048579&lt;/Min&gt;
  296.&lt;/Properties&gt;
  297.&lt;/XMObject&gt;
  298.&lt;/Member&gt;
  299.&lt;/Members&gt;
  300.&lt;/XMObject&gt;
  301.&lt;/Member&gt;
  302.&lt;Member&gt;
  303.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  304.&lt;XMObject class="XMColumnSegmentStats" ProviderVersion="0"&gt;
  305.&lt;Properties&gt;
  306.&lt;DistinctStates xsi:type="xsd:long"&gt;0
  307.&lt;/DistinctStates&gt;
  308.&lt;MinDataID xsi:type="xsd:int"&gt;1048579&lt;/MinDataID&gt;
  309.&lt;MaxDataID xsi:type="xsd:int"&gt;2097154&lt;/MaxDataID&gt;
  310.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  311.&lt;/OriginalMinSegmentDataID&gt;
  312.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  313.&lt;RowCount xsi:type="xsd:long"&gt;1048576&lt;/RowCount&gt;
  314.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  315.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  316.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0&lt;/OthersRLERuns&gt;
  317.&lt;/Properties&gt;
  318.&lt;/XMObject&gt;
  319.&lt;/Member&gt;
  320.&lt;/Members&gt;
  321.&lt;/XMObject&gt;
  322.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  323.&lt;Properties&gt;
  324.&lt;Records xsi:type="xsd:long"&gt;4104&lt;/Records&gt;
  325.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  326.&lt;/Properties&gt;
  327.&lt;Members&gt;
  328.&lt;Member&gt;
  329.&lt;Name&gt;SubSegment&lt;/Name&gt;
  330.<XMObject class="XMColumnSegment"
  331.ProviderVersion="0">
  332.&lt;Properties&gt;
  333.&lt;Records xsi:type="xsd:long"&gt;4104&lt;/Records&gt;
  334.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  335.&lt;/Properties&gt;
  336.&lt;Members&gt;
  337.&lt;Member&gt;
  338.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  339.<XMObject class="XM123CompressionInfo"
  340.ProviderVersion="0">
  341.&lt;Properties&gt;
  342.&lt;Min xsi:type="xsd:int"&gt;2097155&lt;/Min&gt;
  343.&lt;/Properties&gt;
  344.&lt;/XMObject&gt;
  345.&lt;/Member&gt;
  346.&lt;Member&gt;
  347.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  348.<XMObject class="XMColumnSegmentStats"
  349.ProviderVersion="0">
  350.&lt;Properties&gt;
  351.&lt;DistinctStates xsi:type="xsd:long"&gt;0
  352.&lt;/DistinctStates&gt;
  353.&lt;MinDataID xsi:type="xsd:int"&gt;2&lt;/MinDataID&gt;
  354.&lt;MaxDataID xsi:type="xsd:int"&gt;2&lt;/MaxDataID&gt;
  355.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  356.&lt;/OriginalMinSegmentDataID&gt;
  357.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1
  358.&lt;/RLESortOrder&gt;
  359.&lt;RowCount xsi:type="xsd:long"&gt;0&lt;/RowCount&gt;
  360.&lt;HasNulls xsi:type="xsd:boolean"&gt;false
  361.&lt;/HasNulls&gt;
  362.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  363.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0
  364.&lt;/OthersRLERuns&gt;
  365.&lt;/Properties&gt;
  366.&lt;/XMObject&gt;
  367.&lt;/Member&gt;
  368.&lt;/Members&gt;
  369.&lt;/XMObject&gt;
  370.&lt;/Member&gt;
  371.&lt;Member&gt;
  372.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  373.<XMObject class=
  374."XMHybridRLECompressionInfo&lt;class XM123CompressionInfo&gt;"
  375.ProviderVersion="0">
  376.&lt;Members&gt;
  377.&lt;Member&gt;
  378.&lt;Name&gt;RLECompression&lt;/Name&gt;
  379.<XMObject class="XMRLECompressionInfo"
  380.ProviderVersion="0">
  381.&lt;Properties&gt;
  382.&lt;BookmarkBits xsi:type="xsd:long"&gt;24
  383.&lt;/BookmarkBits&gt;
  384.&lt;StorageAllocSize xsi:type="xsd:long"&gt;32
  385.&lt;/StorageAllocSize&gt;
  386.&lt;StorageUsedSize xsi:type="xsd:long"&gt;2
  387.&lt;/StorageUsedSize&gt;
  388.&lt;SegmentNeedsResizing xsi:type="xsd:boolean"&gt;
  389.false&lt;/SegmentNeedsResizing&gt;
  390.&lt;/Properties&gt;
  391.&lt;/XMObject&gt;
  392.&lt;/Member&gt;
  393.&lt;Member&gt;
  394.&lt;Name&gt;SubCompression&lt;/Name&gt;
  395.<XMObject class="XM123CompressionInfo"
  396.ProviderVersion="0">
  397.&lt;Properties&gt;
  398.&lt;Min xsi:type="xsd:int"&gt;2097155&lt;/Min&gt;
  399.&lt;/Properties&gt;
  400.&lt;/XMObject&gt;
  401.&lt;/Member&gt;
  402.&lt;/Members&gt;
  403.&lt;/XMObject&gt;
  404.&lt;/Member&gt;
  405.&lt;Member&gt;
  406.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  407.<XMObject class="XMColumnSegmentStats"
  408.ProviderVersion="0">
  409.&lt;Properties&gt;
  410.&lt;DistinctStates xsi:type="xsd:long"&gt;0
  411.&lt;/DistinctStates&gt;
  412.&lt;MinDataID xsi:type="xsd:int"&gt;2097155&lt;/MinDataID&gt;
  413.&lt;MaxDataID xsi:type="xsd:int"&gt;2101258&lt;/MaxDataID&gt;
  414.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  415.&lt;/OriginalMinSegmentDataID&gt;
  416.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  417.&lt;RowCount xsi:type="xsd:long"&gt;4104&lt;/RowCount&gt;
  418.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  419.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  420.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0&lt;/OthersRLERuns&gt;
  421.&lt;/Properties&gt;
  422.&lt;/XMObject&gt;
  423.&lt;/Member&gt;
  424.&lt;/Members&gt;
  425.&lt;/XMObject&gt;
  426.&lt;/Collection&gt;
  427.&lt;/Collections&gt;
  428.&lt;DataObjects&gt;
  429.&lt;DataObject&gt;
  430.&lt;XMObject class="XMValueDataDictionary<XM_Long&gt;"
  431.ProviderVersion="0">
  432.&lt;Properties&gt;
  433.&lt;DataVersion xsi:type="xsd:int"&gt;1&lt;/DataVersion&gt;
  434.&lt;BaseId xsi:type="xsd:long"&gt;-3&lt;/BaseId&gt;
  435.&lt;Magnitude xsi:type="xsd:double"&gt;1.&lt;/Magnitude&gt;
  436.&lt;/Properties&gt;
  437.&lt;/XMObject&gt;
  438.&lt;/DataObject&gt;
  439.&lt;DataObject&gt;
  440.<XMObject class="XMRawColumnPartitionDataObject" name=
  441."1.Table_1_51adc096-9274-4394-b47d-a2fcabfbc1de.RowNumber.0.idf"
  442.ProviderVersion="0">
  443.&lt;Properties&gt;
  444.&lt;DataVersion xsi:type="xsd:int"&gt;1&lt;/DataVersion&gt;
  445.&lt;Partition xsi:type="xsd:int"&gt;0&lt;/Partition&gt;
  446.&lt;SegmentCount xsi:type="xsd:int"&gt;3&lt;/SegmentCount&gt;
  447.&lt;/Properties&gt;
  448.&lt;/XMObject&gt;
  449.&lt;/DataObject&gt;
  450.&lt;/DataObjects&gt;
  451.&lt;/XMObject&gt;
  452.&lt;XMObject class="XMRawColumn" name="Column_1" ProviderVersion="1"&gt;
  453.&lt;Properties&gt;
  454.&lt;Settings xsi:type="xsd:long"&gt;1025&lt;/Settings&gt;
  455.&lt;ColumnFlags xsi:type="xsd:long"&gt;8&lt;/ColumnFlags&gt;
  456.&lt;Collation/&gt;
  457.&lt;OrderByColumn/&gt;
  458.&lt;Locale xsi:type="xsd:long"&gt;1033&lt;/Locale&gt;
  459.&lt;BinaryCharacters xsi:type="xsd:unsignedInt"&gt;0&lt;/BinaryCharacters&gt;
  460.&lt;/Properties&gt;
  461.&lt;Members&gt;
  462.&lt;Member&gt;
  463.&lt;Name&gt;IntrinsicHierarchy&lt;/Name&gt;
  464.&lt;XMObject class="XMHierarchy" name="\[Hierarchy for column Column_1\]" ProviderVersion="0"&gt;
  465.&lt;Properties&gt;
  466.&lt;SortOrder xsi:type="xsd:int"&gt;0&lt;/SortOrder&gt;
  467.&lt;IsProcessed xsi:type="xsd:boolean"&gt;true&lt;/IsProcessed&gt;
  468.&lt;TypeMaterialization xsi:type="xsd:int"&gt;0&lt;/TypeMaterialization&gt;
  469.&lt;ColumnPosition2DataID xsi:type="xsd:long"&gt;0&lt;/ColumnPosition2DataID&gt;
  470.&lt;ColumnDataID2Position xsi:type="xsd:long"&gt;1&lt;/ColumnDataID2Position&gt;
  471.&lt;DistinctDataIDs xsi:type="xsd:long"&gt;8&lt;/DistinctDataIDs&gt;
  472.&lt;TableStore&gt;H\$Table_1_51adc096-9274-4394-b47d-a2fcabfbc1de\$Column_1&lt;/TableStore&gt;
  473.&lt;/Properties&gt;
  474.&lt;/XMObject&gt;
  475.&lt;/Member&gt;
  476.&lt;Member&gt;
  477.&lt;Name&gt;ColumnStats&lt;/Name&gt;
  478.&lt;XMObject class="XMColumnStats" ProviderVersion="0"&gt;
  479.&lt;Properties&gt;
  480.&lt;DistinctStates xsi:type="xsd:int"&gt;0&lt;/DistinctStates&gt;
  481.&lt;MinDataID xsi:type="xsd:int"&gt;3&lt;/MinDataID&gt;
  482.&lt;MaxDataID xsi:type="xsd:int"&gt;10&lt;/MaxDataID&gt;
  483.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2&lt;/OriginalMinSegmentDataID&gt;
  484.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  485.&lt;RowCount xsi:type="xsd:long"&gt;2101256&lt;/RowCount&gt;
  486.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  487.&lt;RLERuns xsi:type="xsd:long"&gt;12&lt;/RLERuns&gt;
  488.&lt;OthersRLERuns xsi:type="xsd:long"&gt;1&lt;/OthersRLERuns&gt;
  489.&lt;Usage xsi:type="xsd:int"&gt;3&lt;/Usage&gt;
  490.&lt;DBType xsi:type="xsd:short"&gt;20&lt;/DBType&gt;
  491.&lt;XMType xsi:type="xsd:int"&gt;0&lt;/XMType&gt;
  492.&lt;CompressionType xsi:type="xsd:int"&gt;0&lt;/CompressionType&gt;
  493.&lt;CompressionParam xsi:type="xsd:long"&gt;0&lt;/CompressionParam&gt;
  494.&lt;EncodingHint xsi:type="xsd:int"&gt;0&lt;/EncodingHint&gt;
  495.&lt;AggCounter xsi:type="xsd:long"&gt;0&lt;/AggCounter&gt;
  496.&lt;WhereCounter xsi:type="xsd:long"&gt;0&lt;/WhereCounter&gt;
  497.&lt;OrderByCounter xsi:type="xsd:long"&gt;0&lt;/OrderByCounter&gt;
  498.&lt;/Properties&gt;
  499.&lt;/XMObject&gt;
  500.&lt;/Member&gt;
  501.&lt;/Members&gt;
  502.&lt;Collections&gt;
  503.&lt;Collection&gt;
  504.&lt;Name&gt;Segments&lt;/Name&gt;
  505.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  506.&lt;Properties&gt;
  507.&lt;Records xsi:type="xsd:long"&gt;1048576&lt;/Records&gt;
  508.&lt;Mask xsi:type="xsd:long"&gt;1&lt;/Mask&gt;
  509.&lt;/Properties&gt;
  510.&lt;Members&gt;
  511.&lt;Member&gt;
  512.&lt;Name&gt;SubSegment&lt;/Name&gt;
  513.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  514.&lt;Properties&gt;
  515.&lt;Records xsi:type="xsd:long"&gt;0&lt;/Records&gt;
  516.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  517.&lt;/Properties&gt;
  518.&lt;Members&gt;
  519.&lt;Member&gt;
  520.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  521.&lt;XMObject class="XMRENoSplitCompressionInfo<2&gt;"
  522.ProviderVersion="0">
  523.&lt;Properties&gt;
  524.&lt;Min xsi:type="xsd:int"&gt;3&lt;/Min&gt;
  525.&lt;/Properties&gt;
  526.&lt;/XMObject&gt;
  527.&lt;/Member&gt;
  528.&lt;Member&gt;
  529.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  530.<XMObject class="XMColumnSegmentStats"
  531.ProviderVersion="0">
  532.&lt;Properties&gt;
  533.&lt;DistinctStates xsi:type="xsd:long"&gt;0
  534.&lt;/DistinctStates&gt;
  535.&lt;MinDataID xsi:type="xsd:int"&gt;2&lt;/MinDataID&gt;
  536.&lt;MaxDataID xsi:type="xsd:int"&gt;2&lt;/MaxDataID&gt;
  537.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  538.&lt;/OriginalMinSegmentDataID&gt;
  539.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1
  540.&lt;/RLESortOrder&gt;
  541.&lt;RowCount xsi:type="xsd:long"&gt;0&lt;/RowCount&gt;
  542.&lt;HasNulls xsi:type="xsd:boolean"&gt;false
  543.&lt;/HasNulls&gt;
  544.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  545.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0
  546.&lt;/OthersRLERuns&gt;
  547.&lt;/Properties&gt;
  548.&lt;/XMObject&gt;
  549.&lt;/Member&gt;
  550.&lt;/Members&gt;
  551.&lt;/XMObject&gt;
  552.&lt;/Member&gt;
  553.&lt;Member&gt;
  554.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  555.<XMObject class=
  556."XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"
  557.ProviderVersion="0">
  558.&lt;Members&gt;
  559.&lt;Member&gt;
  560.&lt;Name&gt;RLECompression&lt;/Name&gt;
  561.&lt;XMObject class="XMRLECompressionInfo" ProviderVersion="0"&gt;
  562.&lt;Properties&gt;
  563.&lt;BookmarkBits xsi:type="xsd:long"&gt;14
  564.&lt;/BookmarkBits&gt;
  565.&lt;StorageAllocSize xsi:type="xsd:long"&gt;32
  566.&lt;/StorageAllocSize&gt;
  567.&lt;StorageUsedSize xsi:type="xsd:long"&gt;10
  568.&lt;/StorageUsedSize&gt;
  569.&lt;SegmentNeedsResizing xsi:type="xsd:boolean"&gt;
  570.false&lt;/SegmentNeedsResizing&gt;
  571.&lt;/Properties&gt;
  572.&lt;/XMObject&gt;
  573.&lt;/Member&gt;
  574.&lt;Member&gt;
  575.&lt;Name&gt;SubCompression&lt;/Name&gt;
  576.&lt;XMObject class="XMRENoSplitCompressionInfo<2&gt;"
  577.ProviderVersion="0">
  578.&lt;Properties&gt;
  579.&lt;Min xsi:type="xsd:int"&gt;3&lt;/Min&gt;
  580.&lt;/Properties&gt;
  581.&lt;/XMObject&gt;
  582.&lt;/Member&gt;
  583.&lt;/Members&gt;
  584.&lt;/XMObject&gt;
  585.&lt;/Member&gt;
  586.&lt;Member&gt;
  587.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  588.&lt;XMObject class="XMColumnSegmentStats" ProviderVersion="0"&gt;
  589.&lt;Properties&gt;
  590.&lt;DistinctStates xsi:type="xsd:long"&gt;0&lt;/DistinctStates&gt;
  591.&lt;MinDataID xsi:type="xsd:int"&gt;3&lt;/MinDataID&gt;
  592.&lt;MaxDataID xsi:type="xsd:int"&gt;6&lt;/MaxDataID&gt;
  593.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  594.&lt;/OriginalMinSegmentDataID&gt;
  595.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  596.&lt;RowCount xsi:type="xsd:long"&gt;1048576&lt;/RowCount&gt;
  597.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  598.&lt;RLERuns xsi:type="xsd:long"&gt;4&lt;/RLERuns&gt;
  599.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0&lt;/OthersRLERuns&gt;
  600.&lt;/Properties&gt;
  601.&lt;/XMObject&gt;
  602.&lt;/Member&gt;
  603.&lt;/Members&gt;
  604.&lt;/XMObject&gt;
  605.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  606.&lt;Properties&gt;
  607.&lt;Records xsi:type="xsd:long"&gt;1048576&lt;/Records&gt;
  608.&lt;Mask xsi:type="xsd:long"&gt;1&lt;/Mask&gt;
  609.&lt;/Properties&gt;
  610.&lt;Members&gt;
  611.&lt;Member&gt;
  612.&lt;Name&gt;SubSegment&lt;/Name&gt;
  613.<XMObject class="XMColumnSegment"
  614.ProviderVersion="0">
  615.&lt;Properties&gt;
  616.&lt;Records xsi:type="xsd:long"&gt;0&lt;/Records&gt;
  617.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  618.&lt;/Properties&gt;
  619.&lt;Members&gt;
  620.&lt;Member&gt;
  621.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  622.&lt;XMObject class="XMRENoSplitCompressionInfo<2&gt;"
  623.ProviderVersion="0">
  624.&lt;Properties&gt;
  625.&lt;Min xsi:type="xsd:int"&gt;3&lt;/Min&gt;
  626.&lt;/Properties&gt;
  627.&lt;/XMObject&gt;
  628.&lt;/Member&gt;
  629.&lt;Member&gt;
  630.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  631.<XMObject class="XMColumnSegmentStats"
  632.ProviderVersion="0">
  633.&lt;Properties&gt;
  634.&lt;DistinctStates xsi:type="xsd:long"&gt;0
  635.&lt;/DistinctStates&gt;
  636.&lt;MinDataID xsi:type="xsd:int"&gt;2&lt;/MinDataID&gt;
  637.&lt;MaxDataID xsi:type="xsd:int"&gt;2&lt;/MaxDataID&gt;
  638.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  639.&lt;/OriginalMinSegmentDataID&gt;
  640.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1
  641.&lt;/RLESortOrder&gt;
  642.&lt;RowCount xsi:type="xsd:long"&gt;0&lt;/RowCount&gt;
  643.&lt;HasNulls xsi:type="xsd:boolean"&gt;false
  644.&lt;/HasNulls&gt;
  645.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  646.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0
  647.&lt;/OthersRLERuns&gt;
  648.&lt;/Properties&gt;
  649.&lt;/XMObject&gt;
  650.&lt;/Member&gt;
  651.&lt;/Members&gt;
  652.&lt;/XMObject&gt;
  653.&lt;/Member&gt;
  654.&lt;Member&gt;
  655.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  656.<XMObject class=
  657."XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<2&gt;>"
  658.ProviderVersion="0">
  659.&lt;Members&gt;
  660.&lt;Member&gt;
  661.&lt;Name&gt;RLECompression&lt;/Name&gt;
  662.<XMObject class="XMRLECompressionInfo"
  663.ProviderVersion="0">
  664.&lt;Properties&gt;
  665.&lt;BookmarkBits xsi:type="xsd:long"&gt;14
  666.&lt;/BookmarkBits&gt;
  667.&lt;StorageAllocSize xsi:type="xsd:long"&gt;32
  668.&lt;/StorageAllocSize&gt;
  669.&lt;StorageUsedSize xsi:type="xsd:long"&gt;10
  670.&lt;/StorageUsedSize&gt;
  671.&lt;SegmentNeedsResizing xsi:type="xsd:boolean"&gt;
  672.false&lt;/SegmentNeedsResizing&gt;
  673.&lt;/Properties&gt;
  674.&lt;/XMObject&gt;
  675.&lt;/Member&gt;
  676.&lt;Member&gt;
  677.&lt;Name&gt;SubCompression&lt;/Name&gt;
  678.&lt;XMObject class="XMRENoSplitCompressionInfo<2&gt;"
  679.ProviderVersion="0">
  680.&lt;Properties&gt;
  681.&lt;Min xsi:type="xsd:int"&gt;3&lt;/Min&gt;
  682.&lt;/Properties&gt;
  683.&lt;/XMObject&gt;
  684.&lt;/Member&gt;
  685.&lt;/Members&gt;
  686.&lt;/XMObject&gt;
  687.&lt;/Member&gt;
  688.&lt;Member&gt;
  689.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  690.<XMObject class="XMColumnSegmentStats"
  691.ProviderVersion="0">
  692.&lt;Properties&gt;
  693.&lt;DistinctStates xsi:type="xsd:long"&gt;0
  694.&lt;/DistinctStates&gt;
  695.&lt;MinDataID xsi:type="xsd:int"&gt;3&lt;/MinDataID&gt;
  696.&lt;MaxDataID xsi:type="xsd:int"&gt;6&lt;/MaxDataID&gt;
  697.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  698.&lt;/OriginalMinSegmentDataID&gt;
  699.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  700.&lt;RowCount xsi:type="xsd:long"&gt;1048576&lt;/RowCount&gt;
  701.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  702.&lt;RLERuns xsi:type="xsd:long"&gt;4&lt;/RLERuns&gt;
  703.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0&lt;/OthersRLERuns&gt;
  704.&lt;/Properties&gt;
  705.&lt;/XMObject&gt;
  706.&lt;/Member&gt;
  707.&lt;/Members&gt;
  708.&lt;/XMObject&gt;
  709.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  710.&lt;Properties&gt;
  711.&lt;Records xsi:type="xsd:long"&gt;4104&lt;/Records&gt;
  712.&lt;Mask xsi:type="xsd:long"&gt;1&lt;/Mask&gt;
  713.&lt;/Properties&gt;
  714.&lt;Members&gt;
  715.&lt;Member&gt;
  716.&lt;Name&gt;SubSegment&lt;/Name&gt;
  717.&lt;XMObject class="XMColumnSegment" ProviderVersion="0"&gt;
  718.&lt;Properties&gt;
  719.&lt;Records xsi:type="xsd:long"&gt;8&lt;/Records&gt;
  720.&lt;Mask xsi:type="xsd:long"&gt;0&lt;/Mask&gt;
  721.&lt;/Properties&gt;
  722.&lt;Members&gt;
  723.&lt;Member&gt;
  724.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  725.&lt;XMObject class="XMRENoSplitCompressionInfo<3&gt;"
  726.ProviderVersion="0">
  727.&lt;Properties&gt;
  728.&lt;Min xsi:type="xsd:int"&gt;3&lt;/Min&gt;
  729.&lt;/Properties&gt;
  730.&lt;/XMObject&gt;
  731.&lt;/Member&gt;
  732.&lt;Member&gt;
  733.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  734.<XMObject class="XMColumnSegmentStats"
  735.ProviderVersion="0">
  736.&lt;Properties&gt;
  737.&lt;DistinctStates xsi:type="xsd:long"&gt;0
  738.&lt;/DistinctStates&gt;
  739.&lt;MinDataID xsi:type="xsd:int"&gt;2&lt;/MinDataID&gt;
  740.&lt;MaxDataID xsi:type="xsd:int"&gt;2&lt;/MaxDataID&gt;
  741.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;
  742.2&lt;/OriginalMinSegmentDataID&gt;
  743.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1
  744.&lt;/RLESortOrder&gt;
  745.&lt;RowCount xsi:type="xsd:long"&gt;0&lt;/RowCount&gt;
  746.&lt;HasNulls xsi:type="xsd:boolean"&gt;false
  747.&lt;/HasNulls&gt;
  748.&lt;RLERuns xsi:type="xsd:long"&gt;0&lt;/RLERuns&gt;
  749.&lt;OthersRLERuns xsi:type="xsd:long"&gt;0
  750.&lt;/OthersRLERuns&gt;
  751.&lt;/Properties&gt;
  752.&lt;/XMObject&gt;
  753.&lt;/Member&gt;
  754.&lt;/Members&gt;
  755.&lt;/XMObject&gt;
  756.&lt;/Member&gt;
  757.&lt;Member&gt;
  758.&lt;Name&gt;CompressionInfo&lt;/Name&gt;
  759.<XMObject class=
  760."XMHybridRLECompressionInfo&lt;class XMRENoSplitCompressionInfo<3&gt;>"
  761.ProviderVersion="0">
  762.&lt;Members&gt;
  763.&lt;Member&gt;
  764.&lt;Name&gt;RLECompression&lt;/Name&gt;
  765.<XMObject class="XMRLECompressionInfo"
  766.ProviderVersion="0">
  767.&lt;Properties&gt;
  768.&lt;BookmarkBits xsi:type="xsd:long"&gt;6
  769.&lt;/BookmarkBits&gt;
  770.&lt;StorageAllocSize xsi:type="xsd:long"&gt;32
  771.&lt;/StorageAllocSize&gt;
  772.&lt;StorageUsedSize xsi:type="xsd:long"&gt;12
  773.&lt;/StorageUsedSize&gt;
  774.&lt;SegmentNeedsResizing xsi:type="xsd:boolean"&gt;
  775.false&lt;/SegmentNeedsResizing&gt;
  776.&lt;/Properties&gt;
  777.&lt;/XMObject&gt;
  778.&lt;/Member&gt;
  779.&lt;Member&gt;
  780.&lt;Name&gt;SubCompression&lt;/Name&gt;
  781.&lt;XMObject class="XMRENoSplitCompressionInfo<3&gt;"
  782.ProviderVersion="0">
  783.&lt;Properties&gt;
  784.&lt;Min xsi:type="xsd:int"&gt;3&lt;/Min&gt;
  785.&lt;/Properties&gt;
  786.&lt;/XMObject&gt;
  787.&lt;/Member&gt;
  788.&lt;/Members&gt;
  789.&lt;/XMObject&gt;
  790.&lt;/Member&gt;
  791.&lt;Member&gt;
  792.&lt;Name&gt;ColumnSegmentStats&lt;/Name&gt;
  793.&lt;XMObject class="XMColumnSegmentStats" ProviderVersion="0"&gt;
  794.&lt;Properties&gt;
  795.&lt;DistinctStates xsi:type="xsd:long"&gt;0&lt;/DistinctStates&gt;
  796.&lt;MinDataID xsi:type="xsd:int"&gt;3&lt;/MinDataID&gt;
  797.&lt;MaxDataID xsi:type="xsd:int"&gt;10&lt;/MaxDataID&gt;
  798.&lt;OriginalMinSegmentDataID xsi:type="xsd:int"&gt;2
  799.&lt;/OriginalMinSegmentDataID&gt;
  800.&lt;RLESortOrder xsi:type="xsd:long"&gt;-1&lt;/RLESortOrder&gt;
  801.&lt;RowCount xsi:type="xsd:long"&gt;4104&lt;/RowCount&gt;
  802.&lt;HasNulls xsi:type="xsd:boolean"&gt;false&lt;/HasNulls&gt;
  803.&lt;RLERuns xsi:type="xsd:long"&gt;4&lt;/RLERuns&gt;
  804.&lt;OthersRLERuns xsi:type="xsd:long"&gt;1&lt;/OthersRLERuns&gt;
  805.&lt;/Properties&gt;
  806.&lt;/XMObject&gt;
  807.&lt;/Member&gt;
  808.&lt;/Members&gt;
  809.&lt;/XMObject&gt;
  810.&lt;/Collection&gt;
  811.&lt;/Collections&gt;
  812.&lt;DataObjects&gt;
  813.&lt;DataObject&gt;
  814.&lt;XMObject class="XMHashDataDictionary<XM_Long&gt;" name=
  815."1.Table_1_51adc096-9274-4394-b47d-a2fcabfbc1de.Column_1.dictionary"
  816.ProviderVersion="0">
  817.&lt;Properties&gt;
  818.&lt;DataVersion xsi:type="xsd:int"&gt;1&lt;/DataVersion&gt;
  819.&lt;LastId xsi:type="xsd:int"&gt;10&lt;/LastId&gt;
  820.&lt;Nullable xsi:type="xsd:boolean"&gt;false&lt;/Nullable&gt;
  821.&lt;Unique xsi:type="xsd:boolean"&gt;false&lt;/Unique&gt;
  822.&lt;OperatingOn32 xsi:type="xsd:boolean"&gt;true&lt;/OperatingOn32&gt;
  823.&lt;/Properties&gt;
  824.&lt;/XMObject&gt;
  825.&lt;/DataObject&gt;
  826.&lt;DataObject&gt;
  827.<XMObject class="XMRawColumnPartitionDataObject" name=
  828."1.Table_1_51adc096-9274-4394-b47d-a2fcabfbc1de.Column_1.0.idf"
  829.ProviderVersion="0">
  830.&lt;Properties&gt;
  831.&lt;DataVersion xsi:type="xsd:int"&gt;1&lt;/DataVersion&gt;
  832.&lt;Partition xsi:type="xsd:int"&gt;0&lt;/Partition&gt;
  833.&lt;SegmentCount xsi:type="xsd:int"&gt;3&lt;/SegmentCount&gt;
  834.&lt;/Properties&gt;
  835.&lt;/XMObject&gt;
  836.&lt;/DataObject&gt;
  837.&lt;/DataObjects&gt;
  838.&lt;/XMObject&gt;
  839.&lt;/Collection&gt;
  840.&lt;Collection&gt;
  841.&lt;Name&gt;Relationships&lt;/Name&gt;
  842.&lt;/Collection&gt;
  843.&lt;Collection&gt;
  844.&lt;Name&gt;UserHierarchies&lt;/Name&gt;
  845.&lt;/Collection&gt;
  846.&lt;/Collections&gt;
  847.&lt;/XMObject&gt;

## Multiple-Segment Column Data .idf File

This example shows a hexadecimal dump of the column data .idf file (section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e)) that corresponds to the metadata contained in section [3.1](#Section_6425629e551746ca8707b7edf6ba674c).

In the metadata, the **XMRawColumn** object has a **Segments** collection with three **XMColumnSegment** objects, so three segments have been created for this column.  
Six segments actually exist in total because each segment has a subsegment. Because this is a column data .idf file, the compression that is used is required to be XMHybridRLE compression (section [2.7.3](#Section_91ec6bb2098a440abbf95acbfe70dc0b)). This means that each segment has a subsegment member, and the class of the **SubSegment** **XMObject** element provides the compression that is used for that segment. The **SubCompression** member of the **SubSegment** object provides the minimum data identifier value in the segment. (For information about interpreting the XML metadata, see section [2.5](#Section_bf44ae01b0a94363a062808bbadb2246)). In the metadata for this column, the compression and minimum data identifier are as follows:

- Segment 1 has XMHybridRLE using XMRENoSplit compression 2-bit (section [2.7.3.3](#Section_1e9a5c2f099944a38e3f0bfa7c8f189c)) with a minimum data identifier of 3.
- Segment 2 has the same compression characteristics as Segment 1.
- Segment 3 has XMHybridRLE using XMRENoSplit compression 3-bit (section [2.7.3.4](#Section_71c0797f7a9a4b429e3320b793984de9)) with minimum data identifier of 3.

The preceding information enables the interpretation of binary contents of the column data .idf file.

The segment size indicator (section 2.3.1.1) exists at Byte 0x00 for the first segment, which is the primary (RLE) segment for the [**hybrid compression**](#gt_986bb1a7-1919-42e8-8b71-4575f78a4480) (section 2.7.3). Because this is a hybrid compression, a bit-packing subsegment also exists, even if that subsegment is empty.

The segment size indicator is an 8-byte value, so Bytes 0x00 through 0x07 represent the 8-byte segment size indicator. In this example, it contains the value 0x10 (decimal 16), which indicates that 16 units exist in the segment. This value does not include the segment size indicator. Each unit is 8 bytes, so 128 bytes exist in the first (primary) segment. Therefore, this first segment runs from Byte 0x08 through Byte 0x87. This segment contains a few RLE entries.

Following this primary (RLE) segment is the subsegment. The subsegment also has a segment size indicator. This indicator exists in Bytes 0x88 through 0x8F. The value is 0x01 (decimal 1). A subsegment, even if no bit-packed elements exist, needs to have at least one unit in the segment. In Bytes 0x90 through 0x97, as indicated by the segment size, there is only one unit and it is zero.

The second segment (again, as required, composed of both the primary RLE segment and the bit-packing subsegment) begins with a segment size indicator for the primary segment (Bytes 0x98 through 0x9F), which is followed by the primary RLE segment (Bytes 0xA0 through 0x11F), which is then followed by the segment size indicator for the subsegment (Bytes 0x120 through 0x127), which is finally followed by the subsegment (Bytes 0x128 through 0x12F). Again, this subsegment is empty and therefore has the minimum required size of 1 unit.

The third segment (composed of both the primary RLE segment and the bit-packing subsegment) begins with its primary segment size indicator (Bytes 0x130 through 0x137), which is followed by the primary segment (Bytes 0x138 through 0x1B7), which is then followed by the subsegment segment size indicator (Bytes 0x1B8 through 0x1BF), which is finally followed by the subsegment (Bytes 0x1C0 through 0x1C7).

Unlike the previous combinations of RLE segments and bit-packing sub segments, this third set has bit-packed values as well as RLE-compressed values. It will therefore be described in more detail.

The primary segment contains RLE entries and one bit-packing entry (section 2.7.3). The RLE entries consist of two 4-byte values: a data value and a repeat value. The bit-packing entries are also composed of two 4-byte values. The first value is a negated 1-based offset into the subsegment data, and the second value is the count of the number of values that will follow in the subsegment.

The RLE entries are as follows and are referenced by their start bytes:

- Byte 0x138, Byte 0x13C: (data value = 0x00000003, repeat value = 0x00000400)
- Byte 0x140, Byte 0x144: (data value = 0x00000004, repeat value = 0x00000400)
- Byte 0x148, Byte 0x14C: (data value = 0x00000005, repeat value = 0x00000400)
- Byte 0x150, Byte 0x154: (data value = 0x00000006, repeat value = 0x00000400)

So the RLE entries are (3, 1024), (4, 1024), (5, 1024) and (6, 1024).

The bit-packing entry begins at Byte 0x158 and is easy to recognize because it is -1 (hexadecimal 0xFFFF). Following the negated 1-based offset is the count at Byte 0x15C. The count value is 0x08 (decimal 8). So, the subsegment contains 8 bit-packed values. In this case, these values are compressed by using hybrid bit-packing compression XMRENoSplit 3-bit (section 2.7.3.4), so each value is represented by 3 bits. The eight values therefore require 24 bits (3 bytes) in total. Bytes 0x1C0 through 0x1C2 contain the eight compressed values.

Each compressed value needs to be decompressed and have the minimum value added back in, so these bytes decompress to the sequence 7, 8, 9, 10, 9, 10, 9, 10.

The **ColumnSegmentStats** (see section 3.1 and section [2.5.2.54.1](#Section_b312227c6c1c439db36a6d2d35cfc346)) for this third segment (combination segment) indicates that 4104 rows (**RowCount**) ought to exist. Adding the RLE counts and the 8 bit-packed values results in 4 × 1024 + 8, which equals 4104 data values that correspond to the number of rows.

The metadata also shows that four RLE runs (**RLERuns**) and one other RLE run that is not a solid run (**OthersRLERuns**) ought to exist. In this segment, four RLE entries and one bit-packing entry (which is the other RLE run just mentioned) exist.

The value of **MinDataID** is 3, and the value of **MaxDataID** is 10, which correspond to the value of 3 in the first RLE entry and the 10 values in the decompressed bit-packed values (with a minimum of 3 added back during the decompression).

The actual run of data values (from both the RLE segment and the bit-packing subsegment) includes the values 3, 4, 5, 6, 7, 8, 9, and 10.

- 00000000 10 00 00 00 00 00 00 00-03 00 00 00 00 00 04 00 ................
- 00000010 04 00 00 00 00 00 04 00-05 00 00 00 00 00 04 00 ................
- 00000020 06 00 00 00 00 00 04 00-00 00 00 00 00 00 00 00 ................
- 00000030 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000040 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000050 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000060 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000070 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000080 00 00 00 00 00 00 00 00-01 00 00 00 00 00 00 00 ................
- 00000090 00 00 00 00 00 00 00 00-10 00 00 00 00 00 00 00 ................
- 000000A0 03 00 00 00 00 00 04 00-04 00 00 00 00 00 04 00 ................
- 000000B0 05 00 00 00 00 00 04 00-06 00 00 00 00 00 04 00 ................
- 000000C0 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 000000D0 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 000000E0 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 000000F0 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000100 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000110 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000120 01 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000130 10 00 00 00 00 00 00 00-03 00 00 00 00 04 00 00 ................
- 00000140 04 00 00 00 00 04 00 00-05 00 00 00 00 04 00 00 ................
- 00000150 06 00 00 00 00 04 00 00-FF FF FF FF 08 00 00 00 ................
- 00000160 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000170 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000180 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 00000190 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 000001A0 00 00 00 00 00 00 00 00-00 00 00 00 00 00 00 00 ................
- 000001B0 00 00 00 00 00 00 00 00-01 00 00 00 00 00 00 00 ................
- 000001C0 AC EF FB 00 00 00 00 00- ........

## Dictionary File

This example shows a hexadecimal dump that illustrates the contents of the dictionary file (section [2.3.2.1](#Section_06ba2344f1464141bf5d6f9c4c53e099)) corresponding to the data in the column that is shown in section [3.2](#Section_38f20e24dfab4bcda17343ecabe8a91e).

In the metadata, the **XMRawColumn** object has a **DataObjects** collection. Within this collection is a **DataObject XMObject** of class "XMHashDataDictionary&lt;XM_Long&gt;" (section [2.5.2.21](#Section_79da4414b5484bedbfec2ed201436757)). Therefore, the dictionary is an integer dictionary. The **XM_TYPE_LONG** dictionary contains integers. However, **XM_TYPE_LONG** dictionaries can contain either 32-bit integers or 64-bit integers (section [2.3.2.1.1](#Section_f089c2a04f114cbeb2d389eabf62373c)). The properties for this object show that the **OperatingOn32** attribute (section [2.5.2.21.1](#Section_ca80e0f9fc804f4d983b450c40357f1f)) is set to **true**. The dictionary therefore contains 32-bit integer values. The metadata properties also show that the dictionary contains neither NULL values (**Nullable** is **false**) nor unique values (**Unique** is **false**). Because the values are not guaranteed to be unique, hash information is required to ensure that all the values in the dictionary can be retrieved.

In the binary file, the first 4 bytes (Bytes 0x00 through 0x03) indicate the dictionary type, **XM_TYPE**. The value here is zero. In the **XM_TYPE** enumeration (section [2.3.2.1.3.1](#Section_619a632a09a54d8780faf5c0fc9c2ded)), zero corresponds to the **XM_TYPE_LONG** dictionary. This confirms what the metadata has already shown.

**XM_TYPE_LONG** dictionaries are required to have five hash elements (section [2.3.2.1.1.1](#Section_7ee54b7dd64941e59b53aa4a7deb9ecc)). These elements identify the hashing algorithm (section [2.3.3.1.4.2](#Section_22bdc92aaeb04d88b62fb62482ded7ec)), the sizes of the **HashBin** (section [2.3.3.1.4.4](#Section_90abbd326f804bc894712c92f6cc0faf)) and **HashEntry** (section [2.3.3.1.4.5](#Section_db8c786ea4714458924d6807c8cf6a1d)) structures, the local entry count (section [2.3.3.1.4.6](#Section_807c46f84a5d42e6b3cb947cea327c3c)), and the number of bins used in the hash. The number of bins value is set to **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT**, which is -1 (section [2.3.3.1.4.1](#Section_30af58add5ec4897a973525b1eef3f43)).

Looking at the bytes shows that the hash algorithm (Bytes 0x04 through 0x07) is set to 0xFFFF (decimal -1). This is as expected because -1 corresponds to the value of **XM_INVALID**, the required setting for **XM_TYPE_LONG** dictionaries.

Moving to the next element (Bytes 08 through 0x0B) the **HashEntry** size is set to 8, which means that the **HashEntry** structure is 8 bytes in size. Next (Bytes 0x0C through 0x0F) shows that the **HashBin** size is set to 0x40 (decimal 64), which means that the **HashBin** structure is 64 bytes in size.

The next set of bytes (Bytes 0x10 through 0x13) refers to the local entry count, which is the number of hash entries that a hash bin can contain before an overflow (or collision) occurs. The value is 6, so the hash bin (or bucket) can contain 6 **HashEntry** structures within the **HashBin** structure before it needs to start adding collision entries to the chain pointer. For more information, see section 2.3.3.1.4.4.

The last of the required hash elements is the number of bins. This value is set to **XM_HASH_BIN_VECTOR_INVALID_BIN_COUNT**. The next 8 bytes (Bytes 0x14 through 0x1B) represent the bins value. The value is 0xFFFFFFFF (decimal -1). So, the bins value has been properly set and indicates that no more hash information is included in the dictionary.

The rest of the bytes are related to the dictionary itself, not to the type or the hash. **XM_TYPE_LONG** dictionaries contain just the type information, the required hash elements, and vector of dictionary values. The latter are the actual dictionary items stored in a vector (or array) and are not compressed. So, the next information is the element count and the element size for that vector. The element count is 8 bytes in length. The element size is a 4-byte value. The element count (Bytes 0x1C through 0x23) is 8, so 8 elements exist in the vector. The element size (Bytes 0x24 through 0x27) is 4, which means that each element in the vector is 4 bytes in size.

The vector of values can now be parsed. The values are as follows and are referenced by their start bytes:

- Byte 0x28: value = 0x00000001
- Byte 0x2C: value = 0x00000002
- Byte 0x30: value = 0x00000003
- Byte 0x34: value = 0x00000004
- Byte 0x38: value = 0x0000270F (decimal 9999)
- Byte 0x3C: value = 0x0000270E (decimal 9998)
- Byte 0x40: value = 0x0000270D (decimal 9997)
- Byte 0x44: value = 0x0000270C (decimal 9996)

The vector of integer dictionary values therefore consists of the sequence 1, 2, 3, 4, 9999, 9998, 9997, 9996.

From this sequence, it is clear that no NULL values exist, as expected, but also that the dictionary values are unique. No duplicates exist.

- 00000000 00 00 00 00 FF FF FF FF-08 00 00 00 40 00 00 00 ............@...
- 00000010 06 00 00 00 FF FF FF FF-FF FF FF FF 08 00 00 00 ................
- 00000020 00 00 00 00 04 00 00 00-01 00 00 00 02 00 00 00 ................
- 00000030 03 00 00 00 04 00 00 00-0F 27 00 00 0E 27 00 00 .........'...'..
- 00000040 0D 27 00 00 0C 27 00 00- .'...'..

# Security

## Security Considerations for Implementers

The Spreadsheet Data Model file is compressed as a whole by means of Xpress compression (section [2.7.5](#Section_3e3dac063f4548a593d4abacd4b34000)). However, neither the entire Spreadsheet Data Model file nor any file contained within it is encrypted. Therefore, to prevent data tampering in general, taking reasonable precautions to prevent unauthorized access to any of the created Spreadsheet Data Model files is suggested.

Additionally, the file formats of the individual files contained within the Spreadsheet Data Model file are sensitive to data tampering. Neither the XML files nor the hash index files (.hidx files), which are also binary, are compressed. In fact, because all the compression algorithms that are used by the files are documented, the data inside the binary files is just as exposed as the metadata in the XML files. Even minor binary changes-whether benign or malicious-or malformed XML data can cause file format read errors, data corruption or alteration, and possibly undefined system behavior.

For example, various files within the Spreadsheet Data Model file use the .idf extension and have the same file format (section [2.3.1.1](#Section_84e0a86753ea4819a75eee1cea29db4e)). This file format, in particular, is highly dependent on the segment size indicators being accurate. Inaccuracies could result in load errors or undefined behavior.

As another example, various files and structures, including the overall file format layout of the Spreadsheet Data Model itself (section [2.1](#Section_49ca8d5609274cb2ad97bf73f0d91536)), follow particular memory alignment rules. These alignment rules, as well as the specified byte sizes of different elements within the file formats, are designed to be independent of the operating system environment. This design could result in the padding of structures or file format elements. As a result, file and structure sizes can vary. If the files or structures do not correctly adhere to these alignment rules, load errors or undefined behavior can result.

In addition to the protection of [**data sources**](#gt_e091613c-6901-4874-b9b2-27273ead1075) and data integrity, strict adherence to this specification is thus crucial to prevent read or run-time errors.

The actual data that is saved in the Spreadsheet Data Model can change over time. This changeability refers not just to the original data that is processed and saved in various ways within the Spreadsheet Data Model file but also to how that data is processed by the system. The result is that the number and type of files being saved, as well as the particular data that is saved in each file, can change. Again, such changes need to be expected, and proper security procedures for file protection are recommended to differentiate between a valid file that has changed and an invalid file that has been tampered with.

The CryptKey.bin file (section [2.1.2.4](#Section_de3e7547d6c14faa95d0ad6da4b97501)) contains the key BLOB that is needed to decrypt and encrypt the password and connection strings for the Spreadsheet Data Model. This key BLOB is in its original form. Because the key is exposed in this manner, care needs to be taken to ensure that a strong key-in other words, one that is not easily broken-is used.

## Index of Security Fields

| Security field                                                                                                                                                                                                                          | Section                                                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| The **ConnectionString** property                                                                                                                                                                                                       | [2.1.2.1.1](#Section_9fdfbe0e76ad41e38c06918d7bf70bc4) |
| The **SvrEncryptPwdFlag** property                                                                                                                                                                                                      | [2.1.2.3.1](#Section_35cdb4315b4149c8a2b9cc30083d1e4e) |
| The CryptKey.bin file                                                                                                                                                                                                                   | [2.1.2.4](#Section_de3e7547d6c14faa95d0ad6da4b97501)   |
| The **QueryImpersonationInfo** property, as described in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.2.6](http://msdn.microsoft.com/en-us/library/3923a7c5-6a41-444a-ac09-a04db51cd739/) | [2.6.2](#Section_536cdc3781f54984b17359fc6ef64247)     |
| The **ConnectionStringSecurity** property, as described in \[MS-SSAS\] section 2.2.4.2.2.6                                                                                                                                              | 2.6.2                                                  |
| The **ConnectionString** property, as described in \[MS-SSAS\] section 2.2.4.2.2.6                                                                                                                                                      | 2.6.2                                                  |
| The **QueryImpersonationInfo** property, as described in \[MS-SSAS\] section 2.2.4.2.2.6                                                                                                                                                | 2.6.2                                                  |
| The **DataSourceImpersonationInfo** property, as described in \[MS-SSAS\] section [2.2.4.2.2.5](http://msdn.microsoft.com/en-us/library/f0a45420-af97-44e1-8744-1621e69c0bf2/)                                                          | [2.6.4](#Section_220cbde1c685486ba1df07ff4be6965d)     |

# Appendix A: Compression Mask for XMRENoSplit Compression Algorithms

The following single-dimension array contains hexadecimal values that are used in XMRENoSplit compression algorithms:

- const maskArray\[\]=
- {
- 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFFFFE, 0xFFFFFFFFFFFFFFFD, 0xFFFFFFFFFFFFFFFB, 0xFFFFFFFFFFFFFFF7, 0xFFFFFFFFFFFFFFEF, 0xFFFFFFFFFFFFFFDF, 0xFFFFFFFFFFFFFFBF, 0xFFFFFFFFFFFFFF7F, 0xFFFFFFFFFFFFFEFF, 0xFFFFFFFFFFFFFDFF, 0xFFFFFFFFFFFFFBFF, 0xFFFFFFFFFFFFF7FF, 0xFFFFFFFFFFFFEFFF, 0xFFFFFFFFFFFFDFFF, 0xFFFFFFFFFFFFBFFF, 0xFFFFFFFFFFFF7FFF, 0xFFFFFFFFFFFEFFFF, 0xFFFFFFFFFFFDFFFF, 0xFFFFFFFFFFFBFFFF, 0xFFFFFFFFFFF7FFFF, 0xFFFFFFFFFFEFFFFF, 0xFFFFFFFFFFDFFFFF, 0xFFFFFFFFFFBFFFFF, 0xFFFFFFFFFF7FFFFF, 0xFFFFFFFFFEFFFFFF, 0xFFFFFFFFFDFFFFFF, 0xFFFFFFFFFBFFFFFF, 0xFFFFFFFFF7FFFFFF, 0xFFFFFFFFEFFFFFFF, 0xFFFFFFFFDFFFFFFF, 0xFFFFFFFFBFFFFFFF, 0xFFFFFFFF7FFFFFFF, 0xFFFFFFFEFFFFFFFF, 0xFFFFFFFDFFFFFFFF, 0xFFFFFFFBFFFFFFFF, 0xFFFFFFF7FFFFFFFF, 0xFFFFFFEFFFFFFFFF, 0xFFFFFFDFFFFFFFFF, 0xFFFFFFBFFFFFFFFF, 0xFFFFFF7FFFFFFFFF, 0xFFFFFEFFFFFFFFFF, 0xFFFFFDFFFFFFFFFF, 0xFFFFFBFFFFFFFFFF, 0xFFFFF7FFFFFFFFFF, 0xFFFFEFFFFFFFFFFF, 0xFFFFDFFFFFFFFFFF, 0xFFFFBFFFFFFFFFFF, 0xFFFF7FFFFFFFFFFF, 0xFFFEFFFFFFFFFFFF, 0xFFFDFFFFFFFFFFFF, 0xFFFBFFFFFFFFFFFF, 0xFFF7FFFFFFFFFFFF, 0xFFEFFFFFFFFFFFFF, 0xFFDFFFFFFFFFFFFF, 0xFFBFFFFFFFFFFFFF, 0xFF7FFFFFFFFFFFFF, 0xFEFFFFFFFFFFFFFF, 0xFDFFFFFFFFFFFFFF, 0xFBFFFFFFFFFFFFFF, 0xF7FFFFFFFFFFFFFF, 0xEFFFFFFFFFFFFFFF, 0xDFFFFFFFFFFFFFFF, 0xBFFFFFFFFFFFFFFF, 0x7FFFFFFFFFFFFFFF, 0xFFFFFFFFFFFFFFFC, 0xFFFFFFFFFFFFFFF9, 0xFFFFFFFFFFFFFFF3, 0xFFFFFFFFFFFFFFE7, 0xFFFFFFFFFFFFFFCF, 0xFFFFFFFFFFFFFF9F, 0xFFFFFFFFFFFFFF3F, 0xFFFFFFFFFFFFFE7F, 0xFFFFFFFFFFFFFCFF, 0xFFFFFFFFFFFFF9FF, 0xFFFFFFFFFFFFF3FF, 0xFFFFFFFFFFFFE7FF, 0xFFFFFFFFFFFFCFFF, 0xFFFFFFFFFFFF9FFF, 0xFFFFFFFFFFFF3FFF, 0xFFFFFFFFFFFE7FFF, 0xFFFFFFFFFFFCFFFF, 0xFFFFFFFFFFF9FFFF, 0xFFFFFFFFFFF3FFFF, 0xFFFFFFFFFFE7FFFF, 0xFFFFFFFFFFCFFFFF, 0xFFFFFFFFFF9FFFFF, 0xFFFFFFFFFF3FFFFF, 0xFFFFFFFFFE7FFFFF, 0xFFFFFFFFFCFFFFFF, 0xFFFFFFFFF9FFFFFF, 0xFFFFFFFFF3FFFFFF, 0xFFFFFFFFE7FFFFFF, 0xFFFFFFFFCFFFFFFF, 0xFFFFFFFF9FFFFFFF, 0xFFFFFFFF3FFFFFFF, 0xFFFFFFFE7FFFFFFF, 0xFFFFFFFCFFFFFFFF, 0xFFFFFFF9FFFFFFFF, 0xFFFFFFF3FFFFFFFF, 0xFFFFFFE7FFFFFFFF, 0xFFFFFFCFFFFFFFFF, 0xFFFFFF9FFFFFFFFF, 0xFFFFFF3FFFFFFFFF, 0xFFFFFE7FFFFFFFFF, 0xFFFFFCFFFFFFFFFF, 0xFFFFF9FFFFFFFFFF, 0xFFFFF3FFFFFFFFFF, 0xFFFFE7FFFFFFFFFF, 0xFFFFCFFFFFFFFFFF, 0xFFFF9FFFFFFFFFFF, 0xFFFF3FFFFFFFFFFF, 0xFFFE7FFFFFFFFFFF, 0xFFFCFFFFFFFFFFFF, 0xFFF9FFFFFFFFFFFF, 0xFFF3FFFFFFFFFFFF, 0xFFE7FFFFFFFFFFFF, 0xFFCFFFFFFFFFFFFF, 0xFF9FFFFFFFFFFFFF, 0xFF3FFFFFFFFFFFFF, 0xFE7FFFFFFFFFFFFF, 0xFCFFFFFFFFFFFFFF, 0xF9FFFFFFFFFFFFFF, 0xF3FFFFFFFFFFFFFF, 0xE7FFFFFFFFFFFFFF, 0xCFFFFFFFFFFFFFFF, 0x9FFFFFFFFFFFFFFF, 0x3FFFFFFFFFFFFFFF, 0x0000000000000000, 0xFFFFFFFFFFFFFFF8, 0xFFFFFFFFFFFFFFF1, 0xFFFFFFFFFFFFFFE3, 0xFFFFFFFFFFFFFFC7, 0xFFFFFFFFFFFFFF8F, 0xFFFFFFFFFFFFFF1F, 0xFFFFFFFFFFFFFE3F, 0xFFFFFFFFFFFFFC7F, 0xFFFFFFFFFFFFF8FF, 0xFFFFFFFFFFFFF1FF, 0xFFFFFFFFFFFFE3FF, 0xFFFFFFFFFFFFC7FF, 0xFFFFFFFFFFFF8FFF, 0xFFFFFFFFFFFF1FFF, 0xFFFFFFFFFFFE3FFF, 0xFFFFFFFFFFFC7FFF, 0xFFFFFFFFFFF8FFFF, 0xFFFFFFFFFFF1FFFF, 0xFFFFFFFFFFE3FFFF, 0xFFFFFFFFFFC7FFFF, 0xFFFFFFFFFF8FFFFF, 0xFFFFFFFFFF1FFFFF, 0xFFFFFFFFFE3FFFFF, 0xFFFFFFFFFC7FFFFF, 0xFFFFFFFFF8FFFFFF, 0xFFFFFFFFF1FFFFFF, 0xFFFFFFFFE3FFFFFF, 0xFFFFFFFFC7FFFFFF, 0xFFFFFFFF8FFFFFFF, 0xFFFFFFFF1FFFFFFF, 0xFFFFFFFE3FFFFFFF, 0xFFFFFFFC7FFFFFFF, 0xFFFFFFF8FFFFFFFF, 0xFFFFFFF1FFFFFFFF, 0xFFFFFFE3FFFFFFFF, 0xFFFFFFC7FFFFFFFF, 0xFFFFFF8FFFFFFFFF, 0xFFFFFF1FFFFFFFFF, 0xFFFFFE3FFFFFFFFF, 0xFFFFFC7FFFFFFFFF, 0xFFFFF8FFFFFFFFFF, 0xFFFFF1FFFFFFFFFF, 0xFFFFE3FFFFFFFFFF, 0xFFFFC7FFFFFFFFFF, 0xFFFF8FFFFFFFFFFF, 0xFFFF1FFFFFFFFFFF, 0xFFFE3FFFFFFFFFFF, 0xFFFC7FFFFFFFFFFF, 0xFFF8FFFFFFFFFFFF, 0xFFF1FFFFFFFFFFFF, 0xFFE3FFFFFFFFFFFF, 0xFFC7FFFFFFFFFFFF, 0xFF8FFFFFFFFFFFFF, 0xFF1FFFFFFFFFFFFF, 0xFE3FFFFFFFFFFFFF, 0xFC7FFFFFFFFFFFFF, 0xF8FFFFFFFFFFFFFF, 0xF1FFFFFFFFFFFFFF, 0xE3FFFFFFFFFFFFFF, 0xC7FFFFFFFFFFFFFF, 0x8FFFFFFFFFFFFFFF, 0x1FFFFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFFFF0, 0xFFFFFFFFFFFFFFE1, 0xFFFFFFFFFFFFFFC3, 0xFFFFFFFFFFFFFF87, 0xFFFFFFFFFFFFFF0F, 0xFFFFFFFFFFFFFE1F, 0xFFFFFFFFFFFFFC3F, 0xFFFFFFFFFFFFF87F, 0xFFFFFFFFFFFFF0FF, 0xFFFFFFFFFFFFE1FF, 0xFFFFFFFFFFFFC3FF, 0xFFFFFFFFFFFF87FF, 0xFFFFFFFFFFFF0FFF, 0xFFFFFFFFFFFE1FFF, 0xFFFFFFFFFFFC3FFF, 0xFFFFFFFFFFF87FFF, 0xFFFFFFFFFFF0FFFF, 0xFFFFFFFFFFE1FFFF, 0xFFFFFFFFFFC3FFFF, 0xFFFFFFFFFF87FFFF, 0xFFFFFFFFFF0FFFFF, 0xFFFFFFFFFE1FFFFF, 0xFFFFFFFFFC3FFFFF, 0xFFFFFFFFF87FFFFF, 0xFFFFFFFFF0FFFFFF, 0xFFFFFFFFE1FFFFFF, 0xFFFFFFFFC3FFFFFF, 0xFFFFFFFF87FFFFFF, 0xFFFFFFFF0FFFFFFF, 0xFFFFFFFE1FFFFFFF, 0xFFFFFFFC3FFFFFFF, 0xFFFFFFF87FFFFFFF, 0xFFFFFFF0FFFFFFFF, 0xFFFFFFE1FFFFFFFF, 0xFFFFFFC3FFFFFFFF, 0xFFFFFF87FFFFFFFF, 0xFFFFFF0FFFFFFFFF, 0xFFFFFE1FFFFFFFFF, 0xFFFFFC3FFFFFFFFF, 0xFFFFF87FFFFFFFFF, 0xFFFFF0FFFFFFFFFF, 0xFFFFE1FFFFFFFFFF, 0xFFFFC3FFFFFFFFFF, 0xFFFF87FFFFFFFFFF, 0xFFFF0FFFFFFFFFFF, 0xFFFE1FFFFFFFFFFF, 0xFFFC3FFFFFFFFFFF, 0xFFF87FFFFFFFFFFF, 0xFFF0FFFFFFFFFFFF, 0xFFE1FFFFFFFFFFFF, 0xFFC3FFFFFFFFFFFF, 0xFF87FFFFFFFFFFFF, 0xFF0FFFFFFFFFFFFF, 0xFE1FFFFFFFFFFFFF, 0xFC3FFFFFFFFFFFFF, 0xF87FFFFFFFFFFFFF, 0xF0FFFFFFFFFFFFFF, 0xE1FFFFFFFFFFFFFF, 0xC3FFFFFFFFFFFFFF, 0x87FFFFFFFFFFFFFF, 0x0FFFFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFFFE0, 0xFFFFFFFFFFFFFFC1, 0xFFFFFFFFFFFFFF83, 0xFFFFFFFFFFFFFF07, 0xFFFFFFFFFFFFFE0F, 0xFFFFFFFFFFFFFC1F, 0xFFFFFFFFFFFFF83F, 0xFFFFFFFFFFFFF07F, 0xFFFFFFFFFFFFE0FF, 0xFFFFFFFFFFFFC1FF, 0xFFFFFFFFFFFF83FF, 0xFFFFFFFFFFFF07FF, 0xFFFFFFFFFFFE0FFF, 0xFFFFFFFFFFFC1FFF, 0xFFFFFFFFFFF83FFF, 0xFFFFFFFFFFF07FFF, 0xFFFFFFFFFFE0FFFF, 0xFFFFFFFFFFC1FFFF, 0xFFFFFFFFFF83FFFF, 0xFFFFFFFFFF07FFFF, 0xFFFFFFFFFE0FFFFF, 0xFFFFFFFFFC1FFFFF, 0xFFFFFFFFF83FFFFF, 0xFFFFFFFFF07FFFFF, 0xFFFFFFFFE0FFFFFF, 0xFFFFFFFFC1FFFFFF, 0xFFFFFFFF83FFFFFF, 0xFFFFFFFF07FFFFFF, 0xFFFFFFFE0FFFFFFF, 0xFFFFFFFC1FFFFFFF, 0xFFFFFFF83FFFFFFF, 0xFFFFFFF07FFFFFFF, 0xFFFFFFE0FFFFFFFF, 0xFFFFFFC1FFFFFFFF, 0xFFFFFF83FFFFFFFF, 0xFFFFFF07FFFFFFFF, 0xFFFFFE0FFFFFFFFF, 0xFFFFFC1FFFFFFFFF, 0xFFFFF83FFFFFFFFF, 0xFFFFF07FFFFFFFFF, 0xFFFFE0FFFFFFFFFF, 0xFFFFC1FFFFFFFFFF, 0xFFFF83FFFFFFFFFF, 0xFFFF07FFFFFFFFFF, 0xFFFE0FFFFFFFFFFF, 0xFFFC1FFFFFFFFFFF, 0xFFF83FFFFFFFFFFF, 0xFFF07FFFFFFFFFFF, 0xFFE0FFFFFFFFFFFF, 0xFFC1FFFFFFFFFFFF, 0xFF83FFFFFFFFFFFF, 0xFF07FFFFFFFFFFFF, 0xFE0FFFFFFFFFFFFF, 0xFC1FFFFFFFFFFFFF, 0xF83FFFFFFFFFFFFF, 0xF07FFFFFFFFFFFFF, 0xE0FFFFFFFFFFFFFF, 0xC1FFFFFFFFFFFFFF, 0x83FFFFFFFFFFFFFF, 0x07FFFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFFFC0, 0xFFFFFFFFFFFFFF81, 0xFFFFFFFFFFFFFF03, 0xFFFFFFFFFFFFFE07, 0xFFFFFFFFFFFFFC0F, 0xFFFFFFFFFFFFF81F, 0xFFFFFFFFFFFFF03F, 0xFFFFFFFFFFFFE07F, 0xFFFFFFFFFFFFC0FF, 0xFFFFFFFFFFFF81FF, 0xFFFFFFFFFFFF03FF, 0xFFFFFFFFFFFE07FF, 0xFFFFFFFFFFFC0FFF, 0xFFFFFFFFFFF81FFF, 0xFFFFFFFFFFF03FFF, 0xFFFFFFFFFFE07FFF, 0xFFFFFFFFFFC0FFFF, 0xFFFFFFFFFF81FFFF, 0xFFFFFFFFFF03FFFF, 0xFFFFFFFFFE07FFFF, 0xFFFFFFFFFC0FFFFF, 0xFFFFFFFFF81FFFFF, 0xFFFFFFFFF03FFFFF, 0xFFFFFFFFE07FFFFF, 0xFFFFFFFFC0FFFFFF, 0xFFFFFFFF81FFFFFF, 0xFFFFFFFF03FFFFFF, 0xFFFFFFFE07FFFFFF, 0xFFFFFFFC0FFFFFFF, 0xFFFFFFF81FFFFFFF, 0xFFFFFFF03FFFFFFF, 0xFFFFFFE07FFFFFFF, 0xFFFFFFC0FFFFFFFF, 0xFFFFFF81FFFFFFFF, 0xFFFFFF03FFFFFFFF, 0xFFFFFE07FFFFFFFF, 0xFFFFFC0FFFFFFFFF, 0xFFFFF81FFFFFFFFF, 0xFFFFF03FFFFFFFFF, 0xFFFFE07FFFFFFFFF, 0xFFFFC0FFFFFFFFFF, 0xFFFF81FFFFFFFFFF, 0xFFFF03FFFFFFFFFF, 0xFFFE07FFFFFFFFFF, 0xFFFC0FFFFFFFFFFF, 0xFFF81FFFFFFFFFFF, 0xFFF03FFFFFFFFFFF, 0xFFE07FFFFFFFFFFF, 0xFFC0FFFFFFFFFFFF, 0xFF81FFFFFFFFFFFF, 0xFF03FFFFFFFFFFFF, 0xFE07FFFFFFFFFFFF, 0xFC0FFFFFFFFFFFFF, 0xF81FFFFFFFFFFFFF, 0xF03FFFFFFFFFFFFF, 0xE07FFFFFFFFFFFFF, 0xC0FFFFFFFFFFFFFF, 0x81FFFFFFFFFFFFFF, 0x03FFFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFFF80, 0xFFFFFFFFFFFFFF01, 0xFFFFFFFFFFFFFE03, 0xFFFFFFFFFFFFFC07, 0xFFFFFFFFFFFFF80F, 0xFFFFFFFFFFFFF01F, 0xFFFFFFFFFFFFE03F, 0xFFFFFFFFFFFFC07F, 0xFFFFFFFFFFFF80FF, 0xFFFFFFFFFFFF01FF, 0xFFFFFFFFFFFE03FF, 0xFFFFFFFFFFFC07FF, 0xFFFFFFFFFFF80FFF, 0xFFFFFFFFFFF01FFF, 0xFFFFFFFFFFE03FFF, 0xFFFFFFFFFFC07FFF, 0xFFFFFFFFFF80FFFF, 0xFFFFFFFFFF01FFFF, 0xFFFFFFFFFE03FFFF, 0xFFFFFFFFFC07FFFF, 0xFFFFFFFFF80FFFFF, 0xFFFFFFFFF01FFFFF, 0xFFFFFFFFE03FFFFF, 0xFFFFFFFFC07FFFFF, 0xFFFFFFFF80FFFFFF, 0xFFFFFFFF01FFFFFF, 0xFFFFFFFE03FFFFFF, 0xFFFFFFFC07FFFFFF, 0xFFFFFFF80FFFFFFF, 0xFFFFFFF01FFFFFFF, 0xFFFFFFE03FFFFFFF, 0xFFFFFFC07FFFFFFF, 0xFFFFFF80FFFFFFFF, 0xFFFFFF01FFFFFFFF, 0xFFFFFE03FFFFFFFF, 0xFFFFFC07FFFFFFFF, 0xFFFFF80FFFFFFFFF, 0xFFFFF01FFFFFFFFF, 0xFFFFE03FFFFFFFFF, 0xFFFFC07FFFFFFFFF, 0xFFFF80FFFFFFFFFF, 0xFFFF01FFFFFFFFFF, 0xFFFE03FFFFFFFFFF, 0xFFFC07FFFFFFFFFF, 0xFFF80FFFFFFFFFFF, 0xFFF01FFFFFFFFFFF, 0xFFE03FFFFFFFFFFF, 0xFFC07FFFFFFFFFFF, 0xFF80FFFFFFFFFFFF, 0xFF01FFFFFFFFFFFF, 0xFE03FFFFFFFFFFFF, 0xFC07FFFFFFFFFFFF, 0xF80FFFFFFFFFFFFF, 0xF01FFFFFFFFFFFFF, 0xE03FFFFFFFFFFFFF, 0xC07FFFFFFFFFFFFF, 0x80FFFFFFFFFFFFFF, 0x01FFFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFFF00, 0xFFFFFFFFFFFFFE01, 0xFFFFFFFFFFFFFC03, 0xFFFFFFFFFFFFF807, 0xFFFFFFFFFFFFF00F, 0xFFFFFFFFFFFFE01F, 0xFFFFFFFFFFFFC03F, 0xFFFFFFFFFFFF807F, 0xFFFFFFFFFFFF00FF, 0xFFFFFFFFFFFE01FF, 0xFFFFFFFFFFFC03FF, 0xFFFFFFFFFFF807FF, 0xFFFFFFFFFFF00FFF, 0xFFFFFFFFFFE01FFF, 0xFFFFFFFFFFC03FFF, 0xFFFFFFFFFF807FFF, 0xFFFFFFFFFF00FFFF, 0xFFFFFFFFFE01FFFF, 0xFFFFFFFFFC03FFFF, 0xFFFFFFFFF807FFFF, 0xFFFFFFFFF00FFFFF, 0xFFFFFFFFE01FFFFF, 0xFFFFFFFFC03FFFFF, 0xFFFFFFFF807FFFFF, 0xFFFFFFFF00FFFFFF, 0xFFFFFFFE01FFFFFF, 0xFFFFFFFC03FFFFFF, 0xFFFFFFF807FFFFFF, 0xFFFFFFF00FFFFFFF, 0xFFFFFFE01FFFFFFF, 0xFFFFFFC03FFFFFFF, 0xFFFFFF807FFFFFFF, 0xFFFFFF00FFFFFFFF, 0xFFFFFE01FFFFFFFF, 0xFFFFFC03FFFFFFFF, 0xFFFFF807FFFFFFFF, 0xFFFFF00FFFFFFFFF, 0xFFFFE01FFFFFFFFF, 0xFFFFC03FFFFFFFFF, 0xFFFF807FFFFFFFFF, 0xFFFF00FFFFFFFFFF, 0xFFFE01FFFFFFFFFF, 0xFFFC03FFFFFFFFFF, 0xFFF807FFFFFFFFFF, 0xFFF00FFFFFFFFFFF, 0xFFE01FFFFFFFFFFF, 0xFFC03FFFFFFFFFFF, 0xFF807FFFFFFFFFFF, 0xFF00FFFFFFFFFFFF, 0xFE01FFFFFFFFFFFF, 0xFC03FFFFFFFFFFFF, 0xF807FFFFFFFFFFFF, 0xF00FFFFFFFFFFFFF, 0xE01FFFFFFFFFFFFF, 0xC03FFFFFFFFFFFFF, 0x807FFFFFFFFFFFFF, 0x00FFFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFFE00, 0xFFFFFFFFFFFFFC01, 0xFFFFFFFFFFFFF803, 0xFFFFFFFFFFFFF007, 0xFFFFFFFFFFFFE00F, 0xFFFFFFFFFFFFC01F, 0xFFFFFFFFFFFF803F, 0xFFFFFFFFFFFF007F, 0xFFFFFFFFFFFE00FF, 0xFFFFFFFFFFFC01FF, 0xFFFFFFFFFFF803FF, 0xFFFFFFFFFFF007FF, 0xFFFFFFFFFFE00FFF, 0xFFFFFFFFFFC01FFF, 0xFFFFFFFFFF803FFF, 0xFFFFFFFFFF007FFF, 0xFFFFFFFFFE00FFFF, 0xFFFFFFFFFC01FFFF, 0xFFFFFFFFF803FFFF, 0xFFFFFFFFF007FFFF, 0xFFFFFFFFE00FFFFF, 0xFFFFFFFFC01FFFFF, 0xFFFFFFFF803FFFFF, 0xFFFFFFFF007FFFFF, 0xFFFFFFFE00FFFFFF, 0xFFFFFFFC01FFFFFF, 0xFFFFFFF803FFFFFF, 0xFFFFFFF007FFFFFF, 0xFFFFFFE00FFFFFFF, 0xFFFFFFC01FFFFFFF, 0xFFFFFF803FFFFFFF, 0xFFFFFF007FFFFFFF, 0xFFFFFE00FFFFFFFF, 0xFFFFFC01FFFFFFFF, 0xFFFFF803FFFFFFFF, 0xFFFFF007FFFFFFFF, 0xFFFFE00FFFFFFFFF, 0xFFFFC01FFFFFFFFF, 0xFFFF803FFFFFFFFF, 0xFFFF007FFFFFFFFF, 0xFFFE00FFFFFFFFFF, 0xFFFC01FFFFFFFFFF, 0xFFF803FFFFFFFFFF, 0xFFF007FFFFFFFFFF, 0xFFE00FFFFFFFFFFF, 0xFFC01FFFFFFFFFFF, 0xFF803FFFFFFFFFFF, 0xFF007FFFFFFFFFFF, 0xFE00FFFFFFFFFFFF, 0xFC01FFFFFFFFFFFF, 0xF803FFFFFFFFFFFF, 0xF007FFFFFFFFFFFF, 0xE00FFFFFFFFFFFFF, 0xC01FFFFFFFFFFFFF, 0x803FFFFFFFFFFFFF, 0x007FFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFFC00, 0xFFFFFFFFFFFFF801, 0xFFFFFFFFFFFFF003, 0xFFFFFFFFFFFFE007, 0xFFFFFFFFFFFFC00F, 0xFFFFFFFFFFFF801F, 0xFFFFFFFFFFFF003F, 0xFFFFFFFFFFFE007F, 0xFFFFFFFFFFFC00FF, 0xFFFFFFFFFFF801FF, 0xFFFFFFFFFFF003FF, 0xFFFFFFFFFFE007FF, 0xFFFFFFFFFFC00FFF, 0xFFFFFFFFFF801FFF, 0xFFFFFFFFFF003FFF, 0xFFFFFFFFFE007FFF, 0xFFFFFFFFFC00FFFF, 0xFFFFFFFFF801FFFF, 0xFFFFFFFFF003FFFF, 0xFFFFFFFFE007FFFF, 0xFFFFFFFFC00FFFFF, 0xFFFFFFFF801FFFFF, 0xFFFFFFFF003FFFFF, 0xFFFFFFFE007FFFFF, 0xFFFFFFFC00FFFFFF, 0xFFFFFFF801FFFFFF, 0xFFFFFFF003FFFFFF, 0xFFFFFFE007FFFFFF, 0xFFFFFFC00FFFFFFF, 0xFFFFFF801FFFFFFF, 0xFFFFFF003FFFFFFF, 0xFFFFFE007FFFFFFF, 0xFFFFFC00FFFFFFFF, 0xFFFFF801FFFFFFFF, 0xFFFFF003FFFFFFFF, 0xFFFFE007FFFFFFFF, 0xFFFFC00FFFFFFFFF, 0xFFFF801FFFFFFFFF, 0xFFFF003FFFFFFFFF, 0xFFFE007FFFFFFFFF, 0xFFFC00FFFFFFFFFF, 0xFFF801FFFFFFFFFF, 0xFFF003FFFFFFFFFF, 0xFFE007FFFFFFFFFF, 0xFFC00FFFFFFFFFFF, 0xFF801FFFFFFFFFFF, 0xFF003FFFFFFFFFFF, 0xFE007FFFFFFFFFFF, 0xFC00FFFFFFFFFFFF, 0xF801FFFFFFFFFFFF, 0xF003FFFFFFFFFFFF, 0xE007FFFFFFFFFFFF, 0xC00FFFFFFFFFFFFF, 0x801FFFFFFFFFFFFF, 0x003FFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFF800, 0xFFFFFFFFFFFFF001, 0xFFFFFFFFFFFFE003, 0xFFFFFFFFFFFFC007, 0xFFFFFFFFFFFF800F, 0xFFFFFFFFFFFF001F, 0xFFFFFFFFFFFE003F, 0xFFFFFFFFFFFC007F, 0xFFFFFFFFFFF800FF, 0xFFFFFFFFFFF001FF, 0xFFFFFFFFFFE003FF, 0xFFFFFFFFFFC007FF, 0xFFFFFFFFFF800FFF, 0xFFFFFFFFFF001FFF, 0xFFFFFFFFFE003FFF, 0xFFFFFFFFFC007FFF, 0xFFFFFFFFF800FFFF, 0xFFFFFFFFF001FFFF, 0xFFFFFFFFE003FFFF, 0xFFFFFFFFC007FFFF, 0xFFFFFFFF800FFFFF, 0xFFFFFFFF001FFFFF, 0xFFFFFFFE003FFFFF, 0xFFFFFFFC007FFFFF, 0xFFFFFFF800FFFFFF, 0xFFFFFFF001FFFFFF, 0xFFFFFFE003FFFFFF, 0xFFFFFFC007FFFFFF, 0xFFFFFF800FFFFFFF, 0xFFFFFF001FFFFFFF, 0xFFFFFE003FFFFFFF, 0xFFFFFC007FFFFFFF, 0xFFFFF800FFFFFFFF, 0xFFFFF001FFFFFFFF, 0xFFFFE003FFFFFFFF, 0xFFFFC007FFFFFFFF, 0xFFFF800FFFFFFFFF, 0xFFFF001FFFFFFFFF, 0xFFFE003FFFFFFFFF, 0xFFFC007FFFFFFFFF, 0xFFF800FFFFFFFFFF, 0xFFF001FFFFFFFFFF, 0xFFE003FFFFFFFFFF, 0xFFC007FFFFFFFFFF, 0xFF800FFFFFFFFFFF, 0xFF001FFFFFFFFFFF, 0xFE003FFFFFFFFFFF, 0xFC007FFFFFFFFFFF, 0xF800FFFFFFFFFFFF, 0xF001FFFFFFFFFFFF, 0xE003FFFFFFFFFFFF, 0xC007FFFFFFFFFFFF, 0x800FFFFFFFFFFFFF, 0x001FFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFF000, 0xFFFFFFFFFFFFE001, 0xFFFFFFFFFFFFC003, 0xFFFFFFFFFFFF8007, 0xFFFFFFFFFFFF000F, 0xFFFFFFFFFFFE001F, 0xFFFFFFFFFFFC003F, 0xFFFFFFFFFFF8007F, 0xFFFFFFFFFFF000FF, 0xFFFFFFFFFFE001FF, 0xFFFFFFFFFFC003FF, 0xFFFFFFFFFF8007FF, 0xFFFFFFFFFF000FFF, 0xFFFFFFFFFE001FFF, 0xFFFFFFFFFC003FFF, 0xFFFFFFFFF8007FFF, 0xFFFFFFFFF000FFFF, 0xFFFFFFFFE001FFFF, 0xFFFFFFFFC003FFFF, 0xFFFFFFFF8007FFFF, 0xFFFFFFFF000FFFFF, 0xFFFFFFFE001FFFFF, 0xFFFFFFFC003FFFFF, 0xFFFFFFF8007FFFFF, 0xFFFFFFF000FFFFFF, 0xFFFFFFE001FFFFFF, 0xFFFFFFC003FFFFFF, 0xFFFFFF8007FFFFFF, 0xFFFFFF000FFFFFFF, 0xFFFFFE001FFFFFFF, 0xFFFFFC003FFFFFFF, 0xFFFFF8007FFFFFFF, 0xFFFFF000FFFFFFFF, 0xFFFFE001FFFFFFFF, 0xFFFFC003FFFFFFFF, 0xFFFF8007FFFFFFFF, 0xFFFF000FFFFFFFFF, 0xFFFE001FFFFFFFFF, 0xFFFC003FFFFFFFFF, 0xFFF8007FFFFFFFFF, 0xFFF000FFFFFFFFFF, 0xFFE001FFFFFFFFFF, 0xFFC003FFFFFFFFFF, 0xFF8007FFFFFFFFFF, 0xFF000FFFFFFFFFFF, 0xFE001FFFFFFFFFFF, 0xFC003FFFFFFFFFFF, 0xF8007FFFFFFFFFFF, 0xF000FFFFFFFFFFFF, 0xE001FFFFFFFFFFFF, 0xC003FFFFFFFFFFFF, 0x8007FFFFFFFFFFFF, 0x000FFFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFE000, 0xFFFFFFFFFFFFC001, 0xFFFFFFFFFFFF8003, 0xFFFFFFFFFFFF0007, 0xFFFFFFFFFFFE000F, 0xFFFFFFFFFFFC001F, 0xFFFFFFFFFFF8003F, 0xFFFFFFFFFFF0007F, 0xFFFFFFFFFFE000FF, 0xFFFFFFFFFFC001FF, 0xFFFFFFFFFF8003FF, 0xFFFFFFFFFF0007FF, 0xFFFFFFFFFE000FFF, 0xFFFFFFFFFC001FFF, 0xFFFFFFFFF8003FFF, 0xFFFFFFFFF0007FFF, 0xFFFFFFFFE000FFFF, 0xFFFFFFFFC001FFFF, 0xFFFFFFFF8003FFFF, 0xFFFFFFFF0007FFFF, 0xFFFFFFFE000FFFFF, 0xFFFFFFFC001FFFFF, 0xFFFFFFF8003FFFFF, 0xFFFFFFF0007FFFFF, 0xFFFFFFE000FFFFFF, 0xFFFFFFC001FFFFFF, 0xFFFFFF8003FFFFFF, 0xFFFFFF0007FFFFFF, 0xFFFFFE000FFFFFFF, 0xFFFFFC001FFFFFFF, 0xFFFFF8003FFFFFFF, 0xFFFFF0007FFFFFFF, 0xFFFFE000FFFFFFFF, 0xFFFFC001FFFFFFFF, 0xFFFF8003FFFFFFFF, 0xFFFF0007FFFFFFFF, 0xFFFE000FFFFFFFFF, 0xFFFC001FFFFFFFFF, 0xFFF8003FFFFFFFFF, 0xFFF0007FFFFFFFFF, 0xFFE000FFFFFFFFFF, 0xFFC001FFFFFFFFFF, 0xFF8003FFFFFFFFFF, 0xFF0007FFFFFFFFFF, 0xFE000FFFFFFFFFFF, 0xFC001FFFFFFFFFFF, 0xF8003FFFFFFFFFFF, 0xF0007FFFFFFFFFFF, 0xE000FFFFFFFFFFFF, 0xC001FFFFFFFFFFFF, 0x8003FFFFFFFFFFFF, 0x0007FFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFFC000, 0xFFFFFFFFFFFF8001, 0xFFFFFFFFFFFF0003, 0xFFFFFFFFFFFE0007, 0xFFFFFFFFFFFC000F, 0xFFFFFFFFFFF8001F, 0xFFFFFFFFFFF0003F, 0xFFFFFFFFFFE0007F, 0xFFFFFFFFFFC000FF, 0xFFFFFFFFFF8001FF, 0xFFFFFFFFFF0003FF, 0xFFFFFFFFFE0007FF, 0xFFFFFFFFFC000FFF, 0xFFFFFFFFF8001FFF, 0xFFFFFFFFF0003FFF, 0xFFFFFFFFE0007FFF, 0xFFFFFFFFC000FFFF, 0xFFFFFFFF8001FFFF, 0xFFFFFFFF0003FFFF, 0xFFFFFFFE0007FFFF, 0xFFFFFFFC000FFFFF, 0xFFFFFFF8001FFFFF, 0xFFFFFFF0003FFFFF, 0xFFFFFFE0007FFFFF, 0xFFFFFFC000FFFFFF, 0xFFFFFF8001FFFFFF, 0xFFFFFF0003FFFFFF, 0xFFFFFE0007FFFFFF, 0xFFFFFC000FFFFFFF, 0xFFFFF8001FFFFFFF, 0xFFFFF0003FFFFFFF, 0xFFFFE0007FFFFFFF, 0xFFFFC000FFFFFFFF, 0xFFFF8001FFFFFFFF, 0xFFFF0003FFFFFFFF, 0xFFFE0007FFFFFFFF, 0xFFFC000FFFFFFFFF, 0xFFF8001FFFFFFFFF, 0xFFF0003FFFFFFFFF, 0xFFE0007FFFFFFFFF, 0xFFC000FFFFFFFFFF, 0xFF8001FFFFFFFFFF, 0xFF0003FFFFFFFFFF, 0xFE0007FFFFFFFFFF, 0xFC000FFFFFFFFFFF, 0xF8001FFFFFFFFFFF, 0xF0003FFFFFFFFFFF, 0xE0007FFFFFFFFFFF, 0xC000FFFFFFFFFFFF, 0x8001FFFFFFFFFFFF, 0x0003FFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFF8000, 0xFFFFFFFFFFFF0001, 0xFFFFFFFFFFFE0003, 0xFFFFFFFFFFFC0007, 0xFFFFFFFFFFF8000F, 0xFFFFFFFFFFF0001F, 0xFFFFFFFFFFE0003F, 0xFFFFFFFFFFC0007F, 0xFFFFFFFFFF8000FF, 0xFFFFFFFFFF0001FF, 0xFFFFFFFFFE0003FF, 0xFFFFFFFFFC0007FF, 0xFFFFFFFFF8000FFF, 0xFFFFFFFFF0001FFF, 0xFFFFFFFFE0003FFF, 0xFFFFFFFFC0007FFF, 0xFFFFFFFF8000FFFF, 0xFFFFFFFF0001FFFF, 0xFFFFFFFE0003FFFF, 0xFFFFFFFC0007FFFF, 0xFFFFFFF8000FFFFF, 0xFFFFFFF0001FFFFF, 0xFFFFFFE0003FFFFF, 0xFFFFFFC0007FFFFF, 0xFFFFFF8000FFFFFF, 0xFFFFFF0001FFFFFF, 0xFFFFFE0003FFFFFF, 0xFFFFFC0007FFFFFF, 0xFFFFF8000FFFFFFF, 0xFFFFF0001FFFFFFF, 0xFFFFE0003FFFFFFF, 0xFFFFC0007FFFFFFF, 0xFFFF8000FFFFFFFF, 0xFFFF0001FFFFFFFF, 0xFFFE0003FFFFFFFF, 0xFFFC0007FFFFFFFF, 0xFFF8000FFFFFFFFF, 0xFFF0001FFFFFFFFF, 0xFFE0003FFFFFFFFF, 0xFFC0007FFFFFFFFF, 0xFF8000FFFFFFFFFF, 0xFF0001FFFFFFFFFF, 0xFE0003FFFFFFFFFF, 0xFC0007FFFFFFFFFF, 0xF8000FFFFFFFFFFF, 0xF0001FFFFFFFFFFF, 0xE0003FFFFFFFFFFF, 0xC0007FFFFFFFFFFF, 0x8000FFFFFFFFFFFF, 0x0001FFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFF0000, 0xFFFFFFFFFFFE0001, 0xFFFFFFFFFFFC0003, 0xFFFFFFFFFFF80007, 0xFFFFFFFFFFF0000F, 0xFFFFFFFFFFE0001F, 0xFFFFFFFFFFC0003F, 0xFFFFFFFFFF80007F, 0xFFFFFFFFFF0000FF, 0xFFFFFFFFFE0001FF, 0xFFFFFFFFFC0003FF, 0xFFFFFFFFF80007FF, 0xFFFFFFFFF0000FFF, 0xFFFFFFFFE0001FFF, 0xFFFFFFFFC0003FFF, 0xFFFFFFFF80007FFF, 0xFFFFFFFF0000FFFF, 0xFFFFFFFE0001FFFF, 0xFFFFFFFC0003FFFF, 0xFFFFFFF80007FFFF, 0xFFFFFFF0000FFFFF, 0xFFFFFFE0001FFFFF, 0xFFFFFFC0003FFFFF, 0xFFFFFF80007FFFFF, 0xFFFFFF0000FFFFFF, 0xFFFFFE0001FFFFFF, 0xFFFFFC0003FFFFFF, 0xFFFFF80007FFFFFF, 0xFFFFF0000FFFFFFF, 0xFFFFE0001FFFFFFF, 0xFFFFC0003FFFFFFF, 0xFFFF80007FFFFFFF, 0xFFFF0000FFFFFFFF, 0xFFFE0001FFFFFFFF, 0xFFFC0003FFFFFFFF, 0xFFF80007FFFFFFFF, 0xFFF0000FFFFFFFFF, 0xFFE0001FFFFFFFFF, 0xFFC0003FFFFFFFFF, 0xFF80007FFFFFFFFF, 0xFF0000FFFFFFFFFF, 0xFE0001FFFFFFFFFF, 0xFC0003FFFFFFFFFF, 0xF80007FFFFFFFFFF, 0xF0000FFFFFFFFFFF, 0xE0001FFFFFFFFFFF, 0xC0003FFFFFFFFFFF, 0x80007FFFFFFFFFFF, 0x0000FFFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFE0000, 0xFFFFFFFFFFFC0001, 0xFFFFFFFFFFF80003, 0xFFFFFFFFFFF00007, 0xFFFFFFFFFFE0000F, 0xFFFFFFFFFFC0001F, 0xFFFFFFFFFF80003F, 0xFFFFFFFFFF00007F, 0xFFFFFFFFFE0000FF, 0xFFFFFFFFFC0001FF, 0xFFFFFFFFF80003FF, 0xFFFFFFFFF00007FF, 0xFFFFFFFFE0000FFF, 0xFFFFFFFFC0001FFF, 0xFFFFFFFF80003FFF, 0xFFFFFFFF00007FFF, 0xFFFFFFFE0000FFFF, 0xFFFFFFFC0001FFFF, 0xFFFFFFF80003FFFF, 0xFFFFFFF00007FFFF, 0xFFFFFFE0000FFFFF, 0xFFFFFFC0001FFFFF, 0xFFFFFF80003FFFFF, 0xFFFFFF00007FFFFF, 0xFFFFFE0000FFFFFF, 0xFFFFFC0001FFFFFF, 0xFFFFF80003FFFFFF, 0xFFFFF00007FFFFFF, 0xFFFFE0000FFFFFFF, 0xFFFFC0001FFFFFFF, 0xFFFF80003FFFFFFF, 0xFFFF00007FFFFFFF, 0xFFFE0000FFFFFFFF, 0xFFFC0001FFFFFFFF, 0xFFF80003FFFFFFFF, 0xFFF00007FFFFFFFF, 0xFFE0000FFFFFFFFF, 0xFFC0001FFFFFFFFF, 0xFF80003FFFFFFFFF, 0xFF00007FFFFFFFFF, 0xFE0000FFFFFFFFFF, 0xFC0001FFFFFFFFFF, 0xF80003FFFFFFFFFF, 0xF00007FFFFFFFFFF, 0xE0000FFFFFFFFFFF, 0xC0001FFFFFFFFFFF, 0x80003FFFFFFFFFFF, 0x00007FFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFFC0000, 0xFFFFFFFFFFF80001, 0xFFFFFFFFFFF00003, 0xFFFFFFFFFFE00007, 0xFFFFFFFFFFC0000F, 0xFFFFFFFFFF80001F, 0xFFFFFFFFFF00003F, 0xFFFFFFFFFE00007F, 0xFFFFFFFFFC0000FF, 0xFFFFFFFFF80001FF, 0xFFFFFFFFF00003FF, 0xFFFFFFFFE00007FF, 0xFFFFFFFFC0000FFF, 0xFFFFFFFF80001FFF, 0xFFFFFFFF00003FFF, 0xFFFFFFFE00007FFF, 0xFFFFFFFC0000FFFF, 0xFFFFFFF80001FFFF, 0xFFFFFFF00003FFFF, 0xFFFFFFE00007FFFF, 0xFFFFFFC0000FFFFF, 0xFFFFFF80001FFFFF, 0xFFFFFF00003FFFFF, 0xFFFFFE00007FFFFF, 0xFFFFFC0000FFFFFF, 0xFFFFF80001FFFFFF, 0xFFFFF00003FFFFFF, 0xFFFFE00007FFFFFF, 0xFFFFC0000FFFFFFF, 0xFFFF80001FFFFFFF, 0xFFFF00003FFFFFFF, 0xFFFE00007FFFFFFF, 0xFFFC0000FFFFFFFF, 0xFFF80001FFFFFFFF, 0xFFF00003FFFFFFFF, 0xFFE00007FFFFFFFF, 0xFFC0000FFFFFFFFF, 0xFF80001FFFFFFFFF, 0xFF00003FFFFFFFFF, 0xFE00007FFFFFFFFF, 0xFC0000FFFFFFFFFF, 0xF80001FFFFFFFFFF, 0xF00003FFFFFFFFFF, 0xE00007FFFFFFFFFF, 0xC0000FFFFFFFFFFF, 0x80001FFFFFFFFFFF, 0x00003FFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFF80000, 0xFFFFFFFFFFF00001, 0xFFFFFFFFFFE00003, 0xFFFFFFFFFFC00007, 0xFFFFFFFFFF80000F, 0xFFFFFFFFFF00001F, 0xFFFFFFFFFE00003F, 0xFFFFFFFFFC00007F, 0xFFFFFFFFF80000FF, 0xFFFFFFFFF00001FF, 0xFFFFFFFFE00003FF, 0xFFFFFFFFC00007FF, 0xFFFFFFFF80000FFF, 0xFFFFFFFF00001FFF, 0xFFFFFFFE00003FFF, 0xFFFFFFFC00007FFF, 0xFFFFFFF80000FFFF, 0xFFFFFFF00001FFFF, 0xFFFFFFE00003FFFF, 0xFFFFFFC00007FFFF, 0xFFFFFF80000FFFFF, 0xFFFFFF00001FFFFF, 0xFFFFFE00003FFFFF, 0xFFFFFC00007FFFFF, 0xFFFFF80000FFFFFF, 0xFFFFF00001FFFFFF, 0xFFFFE00003FFFFFF, 0xFFFFC00007FFFFFF, 0xFFFF80000FFFFFFF, 0xFFFF00001FFFFFFF, 0xFFFE00003FFFFFFF, 0xFFFC00007FFFFFFF, 0xFFF80000FFFFFFFF, 0xFFF00001FFFFFFFF, 0xFFE00003FFFFFFFF, 0xFFC00007FFFFFFFF, 0xFF80000FFFFFFFFF, 0xFF00001FFFFFFFFF, 0xFE00003FFFFFFFFF, 0xFC00007FFFFFFFFF, 0xF80000FFFFFFFFFF, 0xF00001FFFFFFFFFF, 0xE00003FFFFFFFFFF, 0xC00007FFFFFFFFFF, 0x80000FFFFFFFFFFF, 0x00001FFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFF00000, 0xFFFFFFFFFFE00001, 0xFFFFFFFFFFC00003, 0xFFFFFFFFFF800007, 0xFFFFFFFFFF00000F, 0xFFFFFFFFFE00001F, 0xFFFFFFFFFC00003F, 0xFFFFFFFFF800007F, 0xFFFFFFFFF00000FF, 0xFFFFFFFFE00001FF, 0xFFFFFFFFC00003FF, 0xFFFFFFFF800007FF, 0xFFFFFFFF00000FFF, 0xFFFFFFFE00001FFF, 0xFFFFFFFC00003FFF, 0xFFFFFFF800007FFF, 0xFFFFFFF00000FFFF, 0xFFFFFFE00001FFFF, 0xFFFFFFC00003FFFF, 0xFFFFFF800007FFFF, 0xFFFFFF00000FFFFF, 0xFFFFFE00001FFFFF, 0xFFFFFC00003FFFFF, 0xFFFFF800007FFFFF, 0xFFFFF00000FFFFFF, 0xFFFFE00001FFFFFF, 0xFFFFC00003FFFFFF, 0xFFFF800007FFFFFF, 0xFFFF00000FFFFFFF, 0xFFFE00001FFFFFFF, 0xFFFC00003FFFFFFF, 0xFFF800007FFFFFFF, 0xFFF00000FFFFFFFF, 0xFFE00001FFFFFFFF, 0xFFC00003FFFFFFFF, 0xFF800007FFFFFFFF, 0xFF00000FFFFFFFFF, 0xFE00001FFFFFFFFF, 0xFC00003FFFFFFFFF, 0xF800007FFFFFFFFF, 0xF00000FFFFFFFFFF, 0xE00001FFFFFFFFFF, 0xC00003FFFFFFFFFF, 0x800007FFFFFFFFFF, 0x00000FFFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFE00000, 0xFFFFFFFFFFC00001, 0xFFFFFFFFFF800003, 0xFFFFFFFFFF000007, 0xFFFFFFFFFE00000F, 0xFFFFFFFFFC00001F, 0xFFFFFFFFF800003F, 0xFFFFFFFFF000007F, 0xFFFFFFFFE00000FF, 0xFFFFFFFFC00001FF, 0xFFFFFFFF800003FF, 0xFFFFFFFF000007FF, 0xFFFFFFFE00000FFF, 0xFFFFFFFC00001FFF, 0xFFFFFFF800003FFF, 0xFFFFFFF000007FFF, 0xFFFFFFE00000FFFF, 0xFFFFFFC00001FFFF, 0xFFFFFF800003FFFF, 0xFFFFFF000007FFFF, 0xFFFFFE00000FFFFF, 0xFFFFFC00001FFFFF, 0xFFFFF800003FFFFF, 0xFFFFF000007FFFFF, 0xFFFFE00000FFFFFF, 0xFFFFC00001FFFFFF, 0xFFFF800003FFFFFF, 0xFFFF000007FFFFFF, 0xFFFE00000FFFFFFF, 0xFFFC00001FFFFFFF, 0xFFF800003FFFFFFF, 0xFFF000007FFFFFFF, 0xFFE00000FFFFFFFF, 0xFFC00001FFFFFFFF, 0xFF800003FFFFFFFF, 0xFF000007FFFFFFFF, 0xFE00000FFFFFFFFF, 0xFC00001FFFFFFFFF, 0xF800003FFFFFFFFF, 0xF000007FFFFFFFFF, 0xE00000FFFFFFFFFF, 0xC00001FFFFFFFFFF, 0x800003FFFFFFFFFF, 0x000007FFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFFC00000, 0xFFFFFFFFFF800001, 0xFFFFFFFFFF000003, 0xFFFFFFFFFE000007, 0xFFFFFFFFFC00000F, 0xFFFFFFFFF800001F, 0xFFFFFFFFF000003F, 0xFFFFFFFFE000007F, 0xFFFFFFFFC00000FF, 0xFFFFFFFF800001FF, 0xFFFFFFFF000003FF, 0xFFFFFFFE000007FF, 0xFFFFFFFC00000FFF, 0xFFFFFFF800001FFF, 0xFFFFFFF000003FFF, 0xFFFFFFE000007FFF, 0xFFFFFFC00000FFFF, 0xFFFFFF800001FFFF, 0xFFFFFF000003FFFF, 0xFFFFFE000007FFFF, 0xFFFFFC00000FFFFF, 0xFFFFF800001FFFFF, 0xFFFFF000003FFFFF, 0xFFFFE000007FFFFF, 0xFFFFC00000FFFFFF, 0xFFFF800001FFFFFF, 0xFFFF000003FFFFFF, 0xFFFE000007FFFFFF, 0xFFFC00000FFFFFFF, 0xFFF800001FFFFFFF, 0xFFF000003FFFFFFF, 0xFFE000007FFFFFFF, 0xFFC00000FFFFFFFF, 0xFF800001FFFFFFFF, 0xFF000003FFFFFFFF, 0xFE000007FFFFFFFF, 0xFC00000FFFFFFFFF, 0xF800001FFFFFFFFF, 0xF000003FFFFFFFFF, 0xE000007FFFFFFFFF, 0xC00000FFFFFFFFFF, 0x800001FFFFFFFFFF, 0x000003FFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFF800000, 0xFFFFFFFFFF000001, 0xFFFFFFFFFE000003, 0xFFFFFFFFFC000007, 0xFFFFFFFFF800000F, 0xFFFFFFFFF000001F, 0xFFFFFFFFE000003F, 0xFFFFFFFFC000007F, 0xFFFFFFFF800000FF, 0xFFFFFFFF000001FF, 0xFFFFFFFE000003FF, 0xFFFFFFFC000007FF, 0xFFFFFFF800000FFF, 0xFFFFFFF000001FFF, 0xFFFFFFE000003FFF, 0xFFFFFFC000007FFF, 0xFFFFFF800000FFFF, 0xFFFFFF000001FFFF, 0xFFFFFE000003FFFF, 0xFFFFFC000007FFFF, 0xFFFFF800000FFFFF, 0xFFFFF000001FFFFF, 0xFFFFE000003FFFFF, 0xFFFFC000007FFFFF, 0xFFFF800000FFFFFF, 0xFFFF000001FFFFFF, 0xFFFE000003FFFFFF, 0xFFFC000007FFFFFF, 0xFFF800000FFFFFFF, 0xFFF000001FFFFFFF, 0xFFE000003FFFFFFF, 0xFFC000007FFFFFFF, 0xFF800000FFFFFFFF, 0xFF000001FFFFFFFF, 0xFE000003FFFFFFFF, 0xFC000007FFFFFFFF, 0xF800000FFFFFFFFF, 0xF000001FFFFFFFFF, 0xE000003FFFFFFFFF, 0xC000007FFFFFFFFF, 0x800000FFFFFFFFFF, 0x000001FFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFF000000, 0xFFFFFFFFFE000001, 0xFFFFFFFFFC000003, 0xFFFFFFFFF8000007, 0xFFFFFFFFF000000F, 0xFFFFFFFFE000001F, 0xFFFFFFFFC000003F, 0xFFFFFFFF8000007F, 0xFFFFFFFF000000FF, 0xFFFFFFFE000001FF, 0xFFFFFFFC000003FF, 0xFFFFFFF8000007FF, 0xFFFFFFF000000FFF, 0xFFFFFFE000001FFF, 0xFFFFFFC000003FFF, 0xFFFFFF8000007FFF, 0xFFFFFF000000FFFF, 0xFFFFFE000001FFFF, 0xFFFFFC000003FFFF, 0xFFFFF8000007FFFF, 0xFFFFF000000FFFFF, 0xFFFFE000001FFFFF, 0xFFFFC000003FFFFF, 0xFFFF8000007FFFFF, 0xFFFF000000FFFFFF, 0xFFFE000001FFFFFF, 0xFFFC000003FFFFFF, 0xFFF8000007FFFFFF, 0xFFF000000FFFFFFF, 0xFFE000001FFFFFFF, 0xFFC000003FFFFFFF, 0xFF8000007FFFFFFF, 0xFF000000FFFFFFFF, 0xFE000001FFFFFFFF, 0xFC000003FFFFFFFF, 0xF8000007FFFFFFFF, 0xF000000FFFFFFFFF, 0xE000001FFFFFFFFF, 0xC000003FFFFFFFFF, 0x8000007FFFFFFFFF, 0x000000FFFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFE000000, 0xFFFFFFFFFC000001, 0xFFFFFFFFF8000003, 0xFFFFFFFFF0000007, 0xFFFFFFFFE000000F, 0xFFFFFFFFC000001F, 0xFFFFFFFF8000003F, 0xFFFFFFFF0000007F, 0xFFFFFFFE000000FF, 0xFFFFFFFC000001FF, 0xFFFFFFF8000003FF, 0xFFFFFFF0000007FF, 0xFFFFFFE000000FFF, 0xFFFFFFC000001FFF, 0xFFFFFF8000003FFF, 0xFFFFFF0000007FFF, 0xFFFFFE000000FFFF, 0xFFFFFC000001FFFF, 0xFFFFF8000003FFFF, 0xFFFFF0000007FFFF, 0xFFFFE000000FFFFF, 0xFFFFC000001FFFFF, 0xFFFF8000003FFFFF, 0xFFFF0000007FFFFF, 0xFFFE000000FFFFFF, 0xFFFC000001FFFFFF, 0xFFF8000003FFFFFF, 0xFFF0000007FFFFFF, 0xFFE000000FFFFFFF, 0xFFC000001FFFFFFF, 0xFF8000003FFFFFFF, 0xFF0000007FFFFFFF, 0xFE000000FFFFFFFF, 0xFC000001FFFFFFFF, 0xF8000003FFFFFFFF, 0xF0000007FFFFFFFF, 0xE000000FFFFFFFFF, 0xC000001FFFFFFFFF, 0x8000003FFFFFFFFF, 0x0000007FFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFFC000000, 0xFFFFFFFFF8000001, 0xFFFFFFFFF0000003, 0xFFFFFFFFE0000007, 0xFFFFFFFFC000000F, 0xFFFFFFFF8000001F, 0xFFFFFFFF0000003F, 0xFFFFFFFE0000007F, 0xFFFFFFFC000000FF, 0xFFFFFFF8000001FF, 0xFFFFFFF0000003FF, 0xFFFFFFE0000007FF, 0xFFFFFFC000000FFF, 0xFFFFFF8000001FFF, 0xFFFFFF0000003FFF, 0xFFFFFE0000007FFF, 0xFFFFFC000000FFFF, 0xFFFFF8000001FFFF, 0xFFFFF0000003FFFF, 0xFFFFE0000007FFFF, 0xFFFFC000000FFFFF, 0xFFFF8000001FFFFF, 0xFFFF0000003FFFFF, 0xFFFE0000007FFFFF, 0xFFFC000000FFFFFF, 0xFFF8000001FFFFFF, 0xFFF0000003FFFFFF, 0xFFE0000007FFFFFF, 0xFFC000000FFFFFFF, 0xFF8000001FFFFFFF, 0xFF0000003FFFFFFF, 0xFE0000007FFFFFFF, 0xFC000000FFFFFFFF, 0xF8000001FFFFFFFF, 0xF0000003FFFFFFFF, 0xE0000007FFFFFFFF, 0xC000000FFFFFFFFF, 0x8000001FFFFFFFFF, 0x0000003FFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFF8000000, 0xFFFFFFFFF0000001, 0xFFFFFFFFE0000003, 0xFFFFFFFFC0000007, 0xFFFFFFFF8000000F, 0xFFFFFFFF0000001F, 0xFFFFFFFE0000003F, 0xFFFFFFFC0000007F, 0xFFFFFFF8000000FF, 0xFFFFFFF0000001FF, 0xFFFFFFE0000003FF, 0xFFFFFFC0000007FF, 0xFFFFFF8000000FFF, 0xFFFFFF0000001FFF, 0xFFFFFE0000003FFF, 0xFFFFFC0000007FFF, 0xFFFFF8000000FFFF, 0xFFFFF0000001FFFF, 0xFFFFE0000003FFFF, 0xFFFFC0000007FFFF, 0xFFFF8000000FFFFF, 0xFFFF0000001FFFFF, 0xFFFE0000003FFFFF, 0xFFFC0000007FFFFF, 0xFFF8000000FFFFFF, 0xFFF0000001FFFFFF, 0xFFE0000003FFFFFF, 0xFFC0000007FFFFFF, 0xFF8000000FFFFFFF, 0xFF0000001FFFFFFF, 0xFE0000003FFFFFFF, 0xFC0000007FFFFFFF, 0xF8000000FFFFFFFF, 0xF0000001FFFFFFFF, 0xE0000003FFFFFFFF, 0xC0000007FFFFFFFF, 0x8000000FFFFFFFFF, 0x0000001FFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFF0000000, 0xFFFFFFFFE0000001, 0xFFFFFFFFC0000003, 0xFFFFFFFF80000007, 0xFFFFFFFF0000000F, 0xFFFFFFFE0000001F, 0xFFFFFFFC0000003F, 0xFFFFFFF80000007F, 0xFFFFFFF0000000FF, 0xFFFFFFE0000001FF, 0xFFFFFFC0000003FF, 0xFFFFFF80000007FF, 0xFFFFFF0000000FFF, 0xFFFFFE0000001FFF, 0xFFFFFC0000003FFF, 0xFFFFF80000007FFF, 0xFFFFF0000000FFFF, 0xFFFFE0000001FFFF, 0xFFFFC0000003FFFF, 0xFFFF80000007FFFF, 0xFFFF0000000FFFFF, 0xFFFE0000001FFFFF, 0xFFFC0000003FFFFF, 0xFFF80000007FFFFF, 0xFFF0000000FFFFFF, 0xFFE0000001FFFFFF, 0xFFC0000003FFFFFF, 0xFF80000007FFFFFF, 0xFF0000000FFFFFFF, 0xFE0000001FFFFFFF, 0xFC0000003FFFFFFF, 0xF80000007FFFFFFF, 0xF0000000FFFFFFFF, 0xE0000001FFFFFFFF, 0xC0000003FFFFFFFF, 0x80000007FFFFFFFF, 0x0000000FFFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFE0000000, 0xFFFFFFFFC0000001, 0xFFFFFFFF80000003, 0xFFFFFFFF00000007, 0xFFFFFFFE0000000F, 0xFFFFFFFC0000001F, 0xFFFFFFF80000003F, 0xFFFFFFF00000007F, 0xFFFFFFE0000000FF, 0xFFFFFFC0000001FF, 0xFFFFFF80000003FF, 0xFFFFFF00000007FF, 0xFFFFFE0000000FFF, 0xFFFFFC0000001FFF, 0xFFFFF80000003FFF, 0xFFFFF00000007FFF, 0xFFFFE0000000FFFF, 0xFFFFC0000001FFFF, 0xFFFF80000003FFFF, 0xFFFF00000007FFFF, 0xFFFE0000000FFFFF, 0xFFFC0000001FFFFF, 0xFFF80000003FFFFF, 0xFFF00000007FFFFF, 0xFFE0000000FFFFFF, 0xFFC0000001FFFFFF, 0xFF80000003FFFFFF, 0xFF00000007FFFFFF, 0xFE0000000FFFFFFF, 0xFC0000001FFFFFFF, 0xF80000003FFFFFFF, 0xF00000007FFFFFFF, 0xE0000000FFFFFFFF, 0xC0000001FFFFFFFF, 0x80000003FFFFFFFF, 0x00000007FFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFFC0000000, 0xFFFFFFFF80000001, 0xFFFFFFFF00000003, 0xFFFFFFFE00000007, 0xFFFFFFFC0000000F, 0xFFFFFFF80000001F, 0xFFFFFFF00000003F, 0xFFFFFFE00000007F, 0xFFFFFFC0000000FF, 0xFFFFFF80000001FF, 0xFFFFFF00000003FF, 0xFFFFFE00000007FF, 0xFFFFFC0000000FFF, 0xFFFFF80000001FFF, 0xFFFFF00000003FFF, 0xFFFFE00000007FFF, 0xFFFFC0000000FFFF, 0xFFFF80000001FFFF, 0xFFFF00000003FFFF, 0xFFFE00000007FFFF, 0xFFFC0000000FFFFF, 0xFFF80000001FFFFF, 0xFFF00000003FFFFF, 0xFFE00000007FFFFF, 0xFFC0000000FFFFFF, 0xFF80000001FFFFFF, 0xFF00000003FFFFFF, 0xFE00000007FFFFFF, 0xFC0000000FFFFFFF, 0xF80000001FFFFFFF, 0xF00000003FFFFFFF, 0xE00000007FFFFFFF, 0xC0000000FFFFFFFF, 0x80000001FFFFFFFF, 0x00000003FFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFF80000000, 0xFFFFFFFF00000001, 0xFFFFFFFE00000003, 0xFFFFFFFC00000007, 0xFFFFFFF80000000F, 0xFFFFFFF00000001F, 0xFFFFFFE00000003F, 0xFFFFFFC00000007F, 0xFFFFFF80000000FF, 0xFFFFFF00000001FF, 0xFFFFFE00000003FF, 0xFFFFFC00000007FF, 0xFFFFF80000000FFF, 0xFFFFF00000001FFF, 0xFFFFE00000003FFF, 0xFFFFC00000007FFF, 0xFFFF80000000FFFF, 0xFFFF00000001FFFF, 0xFFFE00000003FFFF, 0xFFFC00000007FFFF, 0xFFF80000000FFFFF, 0xFFF00000001FFFFF, 0xFFE00000003FFFFF, 0xFFC00000007FFFFF, 0xFF80000000FFFFFF, 0xFF00000001FFFFFF, 0xFE00000003FFFFFF, 0xFC00000007FFFFFF, 0xF80000000FFFFFFF, 0xF00000001FFFFFFF, 0xE00000003FFFFFFF, 0xC00000007FFFFFFF, 0x80000000FFFFFFFF, 0x00000001FFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFF00000000, 0xFFFFFFFE00000001, 0xFFFFFFFC00000003, 0xFFFFFFF800000007, 0xFFFFFFF00000000F, 0xFFFFFFE00000001F, 0xFFFFFFC00000003F, 0xFFFFFF800000007F, 0xFFFFFF00000000FF, 0xFFFFFE00000001FF, 0xFFFFFC00000003FF, 0xFFFFF800000007FF, 0xFFFFF00000000FFF, 0xFFFFE00000001FFF, 0xFFFFC00000003FFF, 0xFFFF800000007FFF, 0xFFFF00000000FFFF, 0xFFFE00000001FFFF, 0xFFFC00000003FFFF, 0xFFF800000007FFFF, 0xFFF00000000FFFFF, 0xFFE00000001FFFFF, 0xFFC00000003FFFFF, 0xFF800000007FFFFF, 0xFF00000000FFFFFF, 0xFE00000001FFFFFF, 0xFC00000003FFFFFF, 0xF800000007FFFFFF, 0xF00000000FFFFFFF, 0xE00000001FFFFFFF, 0xC00000003FFFFFFF, 0x800000007FFFFFFF, 0x00000000FFFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFE00000000, 0xFFFFFFFC00000001, 0xFFFFFFF800000003, 0xFFFFFFF000000007, 0xFFFFFFE00000000F, 0xFFFFFFC00000001F, 0xFFFFFF800000003F, 0xFFFFFF000000007F, 0xFFFFFE00000000FF, 0xFFFFFC00000001FF, 0xFFFFF800000003FF, 0xFFFFF000000007FF, 0xFFFFE00000000FFF, 0xFFFFC00000001FFF, 0xFFFF800000003FFF, 0xFFFF000000007FFF, 0xFFFE00000000FFFF, 0xFFFC00000001FFFF, 0xFFF800000003FFFF, 0xFFF000000007FFFF, 0xFFE00000000FFFFF, 0xFFC00000001FFFFF, 0xFF800000003FFFFF, 0xFF000000007FFFFF, 0xFE00000000FFFFFF, 0xFC00000001FFFFFF, 0xF800000003FFFFFF, 0xF000000007FFFFFF, 0xE00000000FFFFFFF, 0xC00000001FFFFFFF, 0x800000003FFFFFFF, 0x000000007FFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFFC00000000, 0xFFFFFFF800000001, 0xFFFFFFF000000003, 0xFFFFFFE000000007, 0xFFFFFFC00000000F, 0xFFFFFF800000001F, 0xFFFFFF000000003F, 0xFFFFFE000000007F, 0xFFFFFC00000000FF, 0xFFFFF800000001FF, 0xFFFFF000000003FF, 0xFFFFE000000007FF, 0xFFFFC00000000FFF, 0xFFFF800000001FFF, 0xFFFF000000003FFF, 0xFFFE000000007FFF, 0xFFFC00000000FFFF, 0xFFF800000001FFFF, 0xFFF000000003FFFF, 0xFFE000000007FFFF, 0xFFC00000000FFFFF, 0xFF800000001FFFFF, 0xFF000000003FFFFF, 0xFE000000007FFFFF, 0xFC00000000FFFFFF, 0xF800000001FFFFFF, 0xF000000003FFFFFF, 0xE000000007FFFFFF, 0xC00000000FFFFFFF, 0x800000001FFFFFFF, 0x000000003FFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFF800000000, 0xFFFFFFF000000001, 0xFFFFFFE000000003, 0xFFFFFFC000000007, 0xFFFFFF800000000F, 0xFFFFFF000000001F, 0xFFFFFE000000003F, 0xFFFFFC000000007F, 0xFFFFF800000000FF, 0xFFFFF000000001FF, 0xFFFFE000000003FF, 0xFFFFC000000007FF, 0xFFFF800000000FFF, 0xFFFF000000001FFF, 0xFFFE000000003FFF, 0xFFFC000000007FFF, 0xFFF800000000FFFF, 0xFFF000000001FFFF, 0xFFE000000003FFFF, 0xFFC000000007FFFF, 0xFF800000000FFFFF, 0xFF000000001FFFFF, 0xFE000000003FFFFF, 0xFC000000007FFFFF, 0xF800000000FFFFFF, 0xF000000001FFFFFF, 0xE000000003FFFFFF, 0xC000000007FFFFFF, 0x800000000FFFFFFF, 0x000000001FFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFF000000000, 0xFFFFFFE000000001, 0xFFFFFFC000000003, 0xFFFFFF8000000007, 0xFFFFFF000000000F, 0xFFFFFE000000001F, 0xFFFFFC000000003F, 0xFFFFF8000000007F, 0xFFFFF000000000FF, 0xFFFFE000000001FF, 0xFFFFC000000003FF, 0xFFFF8000000007FF, 0xFFFF000000000FFF, 0xFFFE000000001FFF, 0xFFFC000000003FFF, 0xFFF8000000007FFF, 0xFFF000000000FFFF, 0xFFE000000001FFFF, 0xFFC000000003FFFF, 0xFF8000000007FFFF, 0xFF000000000FFFFF, 0xFE000000001FFFFF, 0xFC000000003FFFFF, 0xF8000000007FFFFF, 0xF000000000FFFFFF, 0xE000000001FFFFFF, 0xC000000003FFFFFF, 0x8000000007FFFFFF, 0x000000000FFFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFE000000000, 0xFFFFFFC000000001, 0xFFFFFF8000000003, 0xFFFFFF0000000007, 0xFFFFFE000000000F, 0xFFFFFC000000001F, 0xFFFFF8000000003F, 0xFFFFF0000000007F, 0xFFFFE000000000FF, 0xFFFFC000000001FF, 0xFFFF8000000003FF, 0xFFFF0000000007FF, 0xFFFE000000000FFF, 0xFFFC000000001FFF, 0xFFF8000000003FFF, 0xFFF0000000007FFF, 0xFFE000000000FFFF, 0xFFC000000001FFFF, 0xFF8000000003FFFF, 0xFF0000000007FFFF, 0xFE000000000FFFFF, 0xFC000000001FFFFF, 0xF8000000003FFFFF, 0xF0000000007FFFFF, 0xE000000000FFFFFF, 0xC000000001FFFFFF, 0x8000000003FFFFFF, 0x0000000007FFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFFC000000000, 0xFFFFFF8000000001, 0xFFFFFF0000000003, 0xFFFFFE0000000007, 0xFFFFFC000000000F, 0xFFFFF8000000001F, 0xFFFFF0000000003F, 0xFFFFE0000000007F, 0xFFFFC000000000FF, 0xFFFF8000000001FF, 0xFFFF0000000003FF, 0xFFFE0000000007FF, 0xFFFC000000000FFF, 0xFFF8000000001FFF, 0xFFF0000000003FFF, 0xFFE0000000007FFF, 0xFFC000000000FFFF, 0xFF8000000001FFFF, 0xFF0000000003FFFF, 0xFE0000000007FFFF, 0xFC000000000FFFFF, 0xF8000000001FFFFF, 0xF0000000003FFFFF, 0xE0000000007FFFFF, 0xC000000000FFFFFF, 0x8000000001FFFFFF, 0x0000000003FFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFF8000000000, 0xFFFFFF0000000001, 0xFFFFFE0000000003, 0xFFFFFC0000000007, 0xFFFFF8000000000F, 0xFFFFF0000000001F, 0xFFFFE0000000003F, 0xFFFFC0000000007F, 0xFFFF8000000000FF, 0xFFFF0000000001FF, 0xFFFE0000000003FF, 0xFFFC0000000007FF, 0xFFF8000000000FFF, 0xFFF0000000001FFF, 0xFFE0000000003FFF, 0xFFC0000000007FFF, 0xFF8000000000FFFF, 0xFF0000000001FFFF, 0xFE0000000003FFFF, 0xFC0000000007FFFF, 0xF8000000000FFFFF, 0xF0000000001FFFFF, 0xE0000000003FFFFF, 0xC0000000007FFFFF, 0x8000000000FFFFFF, 0x0000000001FFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFF0000000000, 0xFFFFFE0000000001, 0xFFFFFC0000000003, 0xFFFFF80000000007, 0xFFFFF0000000000F, 0xFFFFE0000000001F, 0xFFFFC0000000003F, 0xFFFF80000000007F, 0xFFFF0000000000FF, 0xFFFE0000000001FF, 0xFFFC0000000003FF, 0xFFF80000000007FF, 0xFFF0000000000FFF, 0xFFE0000000001FFF, 0xFFC0000000003FFF, 0xFF80000000007FFF, 0xFF0000000000FFFF, 0xFE0000000001FFFF, 0xFC0000000003FFFF, 0xF80000000007FFFF, 0xF0000000000FFFFF, 0xE0000000001FFFFF, 0xC0000000003FFFFF, 0x80000000007FFFFF, 0x0000000000FFFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFE0000000000, 0xFFFFFC0000000001, 0xFFFFF80000000003, 0xFFFFF00000000007, 0xFFFFE0000000000F, 0xFFFFC0000000001F, 0xFFFF80000000003F, 0xFFFF00000000007F, 0xFFFE0000000000FF, 0xFFFC0000000001FF, 0xFFF80000000003FF, 0xFFF00000000007FF, 0xFFE0000000000FFF, 0xFFC0000000001FFF, 0xFF80000000003FFF, 0xFF00000000007FFF, 0xFE0000000000FFFF, 0xFC0000000001FFFF, 0xF80000000003FFFF, 0xF00000000007FFFF, 0xE0000000000FFFFF, 0xC0000000001FFFFF, 0x80000000003FFFFF, 0x00000000007FFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFFC0000000000, 0xFFFFF80000000001, 0xFFFFF00000000003, 0xFFFFE00000000007, 0xFFFFC0000000000F, 0xFFFF80000000001F, 0xFFFF00000000003F, 0xFFFE00000000007F, 0xFFFC0000000000FF, 0xFFF80000000001FF, 0xFFF00000000003FF, 0xFFE00000000007FF, 0xFFC0000000000FFF, 0xFF80000000001FFF, 0xFF00000000003FFF, 0xFE00000000007FFF, 0xFC0000000000FFFF, 0xF80000000001FFFF, 0xF00000000003FFFF, 0xE00000000007FFFF, 0xC0000000000FFFFF, 0x80000000001FFFFF, 0x00000000003FFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFF80000000000, 0xFFFFF00000000001, 0xFFFFE00000000003, 0xFFFFC00000000007, 0xFFFF80000000000F, 0xFFFF00000000001F, 0xFFFE00000000003F, 0xFFFC00000000007F, 0xFFF80000000000FF, 0xFFF00000000001FF, 0xFFE00000000003FF, 0xFFC00000000007FF, 0xFF80000000000FFF, 0xFF00000000001FFF, 0xFE00000000003FFF, 0xFC00000000007FFF, 0xF80000000000FFFF, 0xF00000000001FFFF, 0xE00000000003FFFF, 0xC00000000007FFFF, 0x80000000000FFFFF, 0x00000000001FFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFF00000000000, 0xFFFFE00000000001, 0xFFFFC00000000003, 0xFFFF800000000007, 0xFFFF00000000000F, 0xFFFE00000000001F, 0xFFFC00000000003F, 0xFFF800000000007F, 0xFFF00000000000FF, 0xFFE00000000001FF, 0xFFC00000000003FF, 0xFF800000000007FF, 0xFF00000000000FFF, 0xFE00000000001FFF, 0xFC00000000003FFF, 0xF800000000007FFF, 0xF00000000000FFFF, 0xE00000000001FFFF, 0xC00000000003FFFF, 0x800000000007FFFF, 0x00000000000FFFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFE00000000000, 0xFFFFC00000000001, 0xFFFF800000000003, 0xFFFF000000000007, 0xFFFE00000000000F, 0xFFFC00000000001F, 0xFFF800000000003F, 0xFFF000000000007F, 0xFFE00000000000FF, 0xFFC00000000001FF, 0xFF800000000003FF, 0xFF000000000007FF, 0xFE00000000000FFF, 0xFC00000000001FFF, 0xF800000000003FFF, 0xF000000000007FFF, 0xE00000000000FFFF, 0xC00000000001FFFF, 0x800000000003FFFF, 0x000000000007FFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFFC00000000000, 0xFFFF800000000001, 0xFFFF000000000003, 0xFFFE000000000007, 0xFFFC00000000000F, 0xFFF800000000001F, 0xFFF000000000003F, 0xFFE000000000007F, 0xFFC00000000000FF, 0xFF800000000001FF, 0xFF000000000003FF, 0xFE000000000007FF, 0xFC00000000000FFF, 0xF800000000001FFF, 0xF000000000003FFF, 0xE000000000007FFF, 0xC00000000000FFFF, 0x800000000001FFFF, 0x000000000003FFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFF800000000000, 0xFFFF000000000001, 0xFFFE000000000003, 0xFFFC000000000007, 0xFFF800000000000F, 0xFFF000000000001F, 0xFFE000000000003F, 0xFFC000000000007F, 0xFF800000000000FF, 0xFF000000000001FF, 0xFE000000000003FF, 0xFC000000000007FF, 0xF800000000000FFF, 0xF000000000001FFF, 0xE000000000003FFF, 0xC000000000007FFF, 0x800000000000FFFF, 0x000000000001FFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFF000000000000, 0xFFFE000000000001, 0xFFFC000000000003, 0xFFF8000000000007, 0xFFF000000000000F, 0xFFE000000000001F, 0xFFC000000000003F, 0xFF8000000000007F, 0xFF000000000000FF, 0xFE000000000001FF, 0xFC000000000003FF, 0xF8000000000007FF, 0xF000000000000FFF, 0xE000000000001FFF, 0xC000000000003FFF, 0x8000000000007FFF, 0x000000000000FFFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFE000000000000, 0xFFFC000000000001, 0xFFF8000000000003, 0xFFF0000000000007, 0xFFE000000000000F, 0xFFC000000000001F, 0xFF8000000000003F, 0xFF0000000000007F, 0xFE000000000000FF, 0xFC000000000001FF, 0xF8000000000003FF, 0xF0000000000007FF, 0xE000000000000FFF, 0xC000000000001FFF, 0x8000000000003FFF, 0x0000000000007FFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFFC000000000000, 0xFFF8000000000001, 0xFFF0000000000003, 0xFFE0000000000007, 0xFFC000000000000F, 0xFF8000000000001F, 0xFF0000000000003F, 0xFE0000000000007F, 0xFC000000000000FF, 0xF8000000000001FF, 0xF0000000000003FF, 0xE0000000000007FF, 0xC000000000000FFF, 0x8000000000001FFF, 0x0000000000003FFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFF8000000000000, 0xFFF0000000000001, 0xFFE0000000000003, 0xFFC0000000000007, 0xFF8000000000000F, 0xFF0000000000001F, 0xFE0000000000003F, 0xFC0000000000007F, 0xF8000000000000FF, 0xF0000000000001FF, 0xE0000000000003FF, 0xC0000000000007FF, 0x8000000000000FFF, 0x0000000000001FFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFF0000000000000, 0xFFE0000000000001, 0xFFC0000000000003, 0xFF80000000000007, 0xFF0000000000000F, 0xFE0000000000001F, 0xFC0000000000003F, 0xF80000000000007F, 0xF0000000000000FF, 0xE0000000000001FF, 0xC0000000000003FF, 0x80000000000007FF, 0x0000000000000FFF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFE0000000000000, 0xFFC0000000000001, 0xFF80000000000003, 0xFF00000000000007, 0xFE0000000000000F, 0xFC0000000000001F, 0xF80000000000003F, 0xF00000000000007F, 0xE0000000000000FF, 0xC0000000000001FF, 0x80000000000003FF, 0x00000000000007FF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFFC0000000000000, 0xFF80000000000001, 0xFF00000000000003, 0xFE00000000000007, 0xFC0000000000000F, 0xF80000000000001F, 0xF00000000000003F, 0xE00000000000007F, 0xC0000000000000FF, 0x80000000000001FF, 0x00000000000003FF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFF80000000000000, 0xFF00000000000001, 0xFE00000000000003, 0xFC00000000000007, 0xF80000000000000F, 0xF00000000000001F, 0xE00000000000003F, 0xC00000000000007F, 0x80000000000000FF, 0x00000000000001FF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFF00000000000000, 0xFE00000000000001, 0xFC00000000000003, 0xF800000000000007, 0xF00000000000000F, 0xE00000000000001F, 0xC00000000000003F, 0x800000000000007F, 0x00000000000000FF, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFE00000000000000, 0xFC00000000000001, 0xF800000000000003, 0xF000000000000007, 0xE00000000000000F, 0xC00000000000001F, 0x800000000000003F, 0x000000000000007F, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xFC00000000000000, 0xF800000000000001, 0xF000000000000003, 0xE000000000000007, 0xC00000000000000F, 0x800000000000001F, 0x000000000000003F, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xF800000000000000, 0xF000000000000001, 0xE000000000000003, 0xC000000000000007, 0x800000000000000F, 0x000000000000001F, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xF000000000000000, 0xE000000000000001, 0xC000000000000003, 0x8000000000000007, 0x000000000000000F, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xE000000000000000, 0xC000000000000001, 0x8000000000000003, 0x0000000000000007, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0xC000000000000000, 0x8000000000000001, 0x0000000000000003, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x8000000000000000, 0x0000000000000001, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000, 0x0000000000000000
- };

# Appendix B: Product Behavior

The information in this specification is applicable to the following Microsoft products or supplemental software. References to product versions include updates to those products.

- Microsoft Excel 2013
- Microsoft SQL Server 2008 R2
- Microsoft SQL Server 2012
- Microsoft Excel 2016
- Microsoft Excel 2019
- Microsoft Excel 2021
- Microsoft Excel LTSC 2024

Exceptions, if any, are noted in this section. If an update version, service pack or Knowledge Base (KB) number appears with a product name, the behavior changed in that update. The new behavior also applies to subsequent updates unless otherwise specified. If a product edition appears with the product version, behavior is different in that product edition.

Unless otherwise specified, any statement of optional behavior in this specification that is prescribed using the terms "SHOULD" or "SHOULD NOT" implies product behavior in accordance with the SHOULD or SHOULD NOT prescription. Unless otherwise specified, the term "MAY" implies that the product does not follow the prescription.

[&lt;1&gt; Section 2.1.2.3.1](#Appendix_A_Target_1): Excel 2013 restricts the collation name to a list of strings that can be obtained by executing the following query against SQL Server 2008 R2:

- SELECT \* FROM FN:HELPCOLLATIONS() WHERE NAME NOT LIKE 'SQL%'

[&lt;2&gt; Section 2.1.2.3.1.1](#Appendix_A_Target_2): Excel 2013 accepts only strings that can be obtained by executing the following query against SQL Server 2008 R2:

- SELECT \* FROM FN:HELPCOLLATIONS() WHERE NAME NOT LIKE 'SQL%'

[&lt;3&gt; Section 2.2.1](#Appendix_A_Target_3): Excel 2013 normalizes **UserID** as described in [\[MS-SSAS\]](%5bMS-SSAS%5d.pdf#Section_854a72f2d6374be3b60f6a44422e80c9) section [2.2.4.2.1.2](http://msdn.microsoft.com/en-us/library/eb0f207a-b101-4f17-9e43-22caf709213b/).

[&lt;4&gt; Section 2.2.3.1](#Appendix_A_Target_4): Excel 2013 normalizes **UserID** as described in \[MS-SSAS\] section 2.2.4.2.1.2.

[&lt;5&gt; Section 2.2.3.2](#Appendix_A_Target_5): Excel 2013 normalizes **UserID** as described in \[MS-SSAS\] section 2.2.4.2.1.2.

[&lt;6&gt; Section 2.2.3.4](#Appendix_A_Target_6): Excel 2013 normalizes **UserID** as described in \[MS-SSAS\] section 2.2.4.2.1.2.

[&lt;7&gt; Section 2.2.3.5](#Appendix_A_Target_7): Excel 2013 generates a [**data source**](#gt_e091613c-6901-4874-b9b2-27273ead1075) folder for the model. The folder is empty.

[&lt;8&gt; Section 2.2.3.6](#Appendix_A_Target_8): Excel 2013 normalizes **UserID** as described in \[MS-SSAS\] section 2.2.4.2.1.2.

[&lt;9&gt; Section 2.3.1](#Appendix_A_Target_9): Excel 2013 assigns data identifiers in the order in which each unique value is encountered in the source data.

[&lt;10&gt; Section 2.3.1](#Appendix_A_Target_10): Excel 2013 uses partial sorting to optimize compression.

[&lt;11&gt; Section 2.5.2.3.1](#Appendix_A_Target_11): Excel 2013 restricts the collation name to a list of strings that can be obtained by executing the following query against SQL Server 2008 R2:

- SELECT \* FROM FN:HELPCOLLATIONS() WHERE NAME NOT LIKE 'SQL%'

[&lt;12&gt; Section 2.6.9](#Appendix_A_Target_12): Excel 2013 inserts the text for the command as stated in the document.

# Change Tracking

This section identifies changes that were made to this document since the last release. Changes are classified as Major, Minor, or None.

The revision class **Major** means that the technical content in the document was significantly revised. Major changes affect protocol interoperability or implementation. Examples of major changes are:

- A document revision that incorporates changes to interoperability requirements.
- A document revision that captures changes to protocol functionality.

The revision class **Minor** means that the meaning of the technical content was clarified. Minor changes do not affect protocol interoperability or implementation. Examples of minor changes are updates to clarify ambiguity at the sentence, paragraph, or table level.

The revision class **None** means that no new technical changes were introduced. Minor editorial and formatting changes may have been made, but the relevant technical content is identical to the last released version.

The changes made to this document are listed in the following table. For more information, please contact [dochelp@microsoft.com](mailto:dochelp@microsoft.com).

| Section                                                                     | Description                         | Revision class |
| --------------------------------------------------------------------------- | ----------------------------------- | -------------- |
| [6](#Section_fb3a525b39964328ac4b037fe1204cf4) Appendix B: Product Behavior | Updated list of supported products. | Minor          |

# Index

A

[Applicability](#section_b2e94ae6795e407cb5051ffa48cedaf9) 14

C

[Change tracking](#section_fcc7501a722e437b9582e6a4d61a0077) 234

[Column data dictionary](#section_d6de072d52344099b090528322f829dc) 43

[Column data hierarchy hash index](#section_582bda42d62f4ce0998551fb88fe68ee) 57

[Column data identifier-to-position mapping](#section_54a5d3d8c1bf4723af2f317577cf12b7) 71

[Column data position-to-identifier mapping](#section_a1207fafbbd8410aba43656b21f8a59d) 70

[Column data storage](#section_4d3887f864c84dbd9a02e4e95e64bfed) 39

[Common data types and fields](#section_9a79dd4258ca41bc8edc469f290e7bbb) 15

[Compression](#section_d9db04571298486c9e7696366b838714) 153

[Compression Mask for XMRENoSplit compression algorithms](#section_e0eb73abda1143608e01c0b407999ed3) 216

[Contents of the .tbl.xml files](#section_d3f931058b2a4727955605f06ecd9f06) 142

[CubeTabularModel](#section_6123c4c160fd4d7683a46467421fede2) 146

D

[Data types and fields - common](#section_9a79dd4258ca41bc8edc469f290e7bbb) 15

[Database folder](#section_ee899b2229ee496fba0cf25f9c033443) 31

[Database folder contents](#section_2724b80b8d284083b5e62f866caf5e69) 31

[DatabaseTabularModel](#section_220cbde1c685486ba1df07ff4be6965d) 145

[DataSourceTabularModel](#section_536cdc3781f54984b17359fc6ef64247) 144

[DataSourceTabularViewModel](#section_77f559d9ed7d467fb1f620aea4410502) 145

Details

[column data dictionary](#section_d6de072d52344099b090528322f829dc) 43

[column data hierarchy hash index](#section_582bda42d62f4ce0998551fb88fe68ee) 57

[column data identifier-to-position mapping](#section_54a5d3d8c1bf4723af2f317577cf12b7) 71

[column data position-to-identifier mapping](#section_a1207fafbbd8410aba43656b21f8a59d) 70

[column data storage](#section_4d3887f864c84dbd9a02e4e95e64bfed) 39

[common data types and fields](#section_9a79dd4258ca41bc8edc469f290e7bbb) 15

[compression](#section_d9db04571298486c9e7696366b838714) 153

[content of the .tbl.xml files](#section_d3f931058b2a4727955605f06ecd9f06) 142

[CubeTabularModel](#section_6123c4c160fd4d7683a46467421fede2) 146

[database folder](#section_ee899b2229ee496fba0cf25f9c033443) 31

[database folder contents](#section_2724b80b8d284083b5e62f866caf5e69) 31

[DatabaseTabularModel](#section_220cbde1c685486ba1df07ff4be6965d) 145

[DataSourceTabularModel](#section_536cdc3781f54984b17359fc6ef64247) 144

[DataSourceViewTabularModel](#section_77f559d9ed7d467fb1f620aea4410502) 145

[DimensionTabularModel](#section_f7381e33c04e409996d45966dbd38b42) 147

[file name generation](#section_f629ebb97cf2410fb56b2edce58dbcc9) 30

[files section](#section_72e81524c51d43dd9f8f9edecbe73a41) 17

[Huffman compression](#section_f70b41f2ca6444a19e6f53e63f6a5ee9) 191

[Load element document node](#section_c2444469a1624cf289f0d01a0553521c) 142

[MdxScriptTabularModel](#section_37b7ea6d12f749ed91978daf494edba2) 149

[MeasureGroupTabularModel](#section_0861668595e448eea31c733d6b94773f) 147

[metadata files](#section_bf44ae01b0a94363a062808bbadb2246) 76

[model OLAP files](#section_6bd8ed6126234bcdbe1d8b6993c880f9) 142

[OLAP information files](#section_5f09e82293fe4ac594b862313205eda1) 149

[PartitionTabularModel](#section_e7167bbc07cb453bb06072b04b75ac69) 148

[relationship index](#section_55a2b0ea2fd84b2f84d1736648f0f8fd) 72

[RowNumber column](#section_7d9074aabea740e2b5d822e9cadeb778) 69

[spreadsheet data model header](#section_b5189435d6c5498c896f53a079be0c79) 15

[storage format of the stream](#section_49ca8d5609274cb2ad97bf73f0d91536) 15

[storage of data values](#section_0cfe0bea60cb43eb9af3a3ff62610c61) 39

[system-generated data files](#section_a713d4decb324086a8b62c5bbd3ae6ea) 70

[top level files](#section_ca7f367c1eca41afb8244a77c462ad7e) 31

[user hierarchy system-generated files](#section_7b84720fcf8e499088672200b6d7d1a6) 72

[virtual directory](#section_0e526ce8f0344a21b43f9b3c930d9ca0) 29

[XM123 compression algorithm](#section_c6e2e96740c24b7da473c22621f30654) 173

[XMHybridRLE compression algorithms](#section_91ec6bb2098a440abbf95acbfe70dc0b) 173

[XMObject definitions by class attribute](#section_99defc8e38d0430fad7471be19741abd) 86

[XMObject document node element](#section_23dde626b187405590e15a2333f11c5f) 76

[XMRENoSplit compression algorithms](#section_85c2024e34e743748fa08b4ca8fe4f2d) 153

[Xpress compression](#section_3e3dac063f4548a593d4abacd4b34000) 196

[Dictionary File example](#section_d2ba3805410d4a3cb5b9fac7e4fcb8e0) 211

[DimensionTabularModel](#section_f7381e33c04e409996d45966dbd38b42) 147

E

Examples

[Dictionary File](#section_d2ba3805410d4a3cb5b9fac7e4fcb8e0) 211

[Multiple-Segment Column Data .idf File](#section_38f20e24dfab4bcda17343ecabe8a91e) 209

[tbl.xml Metadata File](#section_6425629e551746ca8707b7edf6ba674c) 197

F

[Fields - security index](#section_d63ce43257c24e5da2e26c3e0db971ce) 214

[Fields - vendor-extensible](#section_2b5a8556e2314019b6aa531fb3f06a76) 14

[File name generation](#section_f629ebb97cf2410fb56b2edce58dbcc9) 30

[Files section](#section_72e81524c51d43dd9f8f9edecbe73a41) 17

G

[Glossary](#section_a087638030c744f6811a76b6ea4f5fc6) 10

H

[Huffman compression](#section_f70b41f2ca6444a19e6f53e63f6a5ee9) 191

I

[Implementer - security considerations](#section_d8acffa76cc4477eb1b1fa39758428bc) 214

[Index of security fields](#section_d63ce43257c24e5da2e26c3e0db971ce) 214

[Informative references](#section_9a6dd72f0d764842b867c5c7978fa1f8) 13

[Introduction](#section_a89e7525f1d742219d06036db839554f) 10

L

[Load element document node](#section_c2444469a1624cf289f0d01a0553521c) 142

[Localization](#section_ac671d12a9c74c25acd3959d019feef2) 14

M

[MdxScriptTabularModel](#section_37b7ea6d12f749ed91978daf494edba2) 149

[MeasureGroupTabularModel](#section_0861668595e448eea31c733d6b94773f) 147

[Metadata files](#section_bf44ae01b0a94363a062808bbadb2246) 76

[Model OLAP files](#section_6bd8ed6126234bcdbe1d8b6993c880f9) 142

[Multiple-Segment Column Data .idf File example](#section_38f20e24dfab4bcda17343ecabe8a91e) 209

N

[Normative references](#section_07a7a3263fa1490584202f6b2d139d90) 12

O

[OLAP information files](#section_5f09e82293fe4ac594b862313205eda1) 149

[Overview (synopsis)](#section_02d7bdea513a4eaebfedf65d44b92d7a) 13

P

[PartitionTabularModel](#section_e7167bbc07cb453bb06072b04b75ac69) 148

[Product behavior](#section_fb3a525b39964328ac4b037fe1204cf4) 232

R

[References](#section_303e6eaa142b4fb6a787a4fb1e6365eb) 12

[informative](#section_9a6dd72f0d764842b867c5c7978fa1f8) 13

[normative](#section_07a7a3263fa1490584202f6b2d139d90) 12

[Relationship index](#section_55a2b0ea2fd84b2f84d1736648f0f8fd) 72

[Relationship to protocols and other structures](#section_14b8a20b4f16458ba90a3731d1f130d9) 13

[RowNumber column](#section_7d9074aabea740e2b5d822e9cadeb778) 69

S

Security

[field index](#section_d63ce43257c24e5da2e26c3e0db971ce) 214

[implementer considerations](#section_d8acffa76cc4477eb1b1fa39758428bc) 214

[Spreadsheet data model header](#section_b5189435d6c5498c896f53a079be0c79) 15

[Storage format of the stream](#section_49ca8d5609274cb2ad97bf73f0d91536) 15

[Storage of data values](#section_0cfe0bea60cb43eb9af3a3ff62610c61) 39

Structures

[column data dictionary](#section_d6de072d52344099b090528322f829dc) 43

[column data hierarchy hash index](#section_582bda42d62f4ce0998551fb88fe68ee) 57

[column data identifier-to-position mapping](#section_54a5d3d8c1bf4723af2f317577cf12b7) 71

[column data position-to-identifier mapping](#section_a1207fafbbd8410aba43656b21f8a59d) 70

[column data storage](#section_4d3887f864c84dbd9a02e4e95e64bfed) 39

[compression](#section_d9db04571298486c9e7696366b838714) 153

[contents of the .tbl.xml files](#section_d3f931058b2a4727955605f06ecd9f06) 142

[CubeTabularModel](#section_6123c4c160fd4d7683a46467421fede2) 146

[database folder](#section_ee899b2229ee496fba0cf25f9c033443) 31

[database folder contents](#section_2724b80b8d284083b5e62f866caf5e69) 31

[DatabaseTabularModel](#section_220cbde1c685486ba1df07ff4be6965d) 145

[DataSourceTabularModel](#section_536cdc3781f54984b17359fc6ef64247) 144

[DataSourceTabularViewModel](#section_77f559d9ed7d467fb1f620aea4410502) 145

[DimensionTabularModel](#section_f7381e33c04e409996d45966dbd38b42) 147

[file name generation](#section_f629ebb97cf2410fb56b2edce58dbcc9) 30

[files section](#section_72e81524c51d43dd9f8f9edecbe73a41) 17

[Huffman compression](#section_f70b41f2ca6444a19e6f53e63f6a5ee9) 191

[Load element document node](#section_c2444469a1624cf289f0d01a0553521c) 142

[MdxScriptTabularModel](#section_37b7ea6d12f749ed91978daf494edba2) 149

[MeasureGroupTabularModel](#section_0861668595e448eea31c733d6b94773f) 147

[metadata files](#section_bf44ae01b0a94363a062808bbadb2246) 76

[model OLAP files](#section_6bd8ed6126234bcdbe1d8b6993c880f9) 142

[OLAP information files](#section_5f09e82293fe4ac594b862313205eda1) 149

[overview](#section_9a79dd4258ca41bc8edc469f290e7bbb) 15

[PartitionTabularModel](#section_e7167bbc07cb453bb06072b04b75ac69) 148

[relationship index](#section_55a2b0ea2fd84b2f84d1736648f0f8fd) 72

[RowNumber column](#section_7d9074aabea740e2b5d822e9cadeb778) 69

[spreadsheet data model header](#section_b5189435d6c5498c896f53a079be0c79) 15

[storage format of the stream](#section_49ca8d5609274cb2ad97bf73f0d91536) 15

[storage of data values](#section_0cfe0bea60cb43eb9af3a3ff62610c61) 39

[system-generated data files](#section_a713d4decb324086a8b62c5bbd3ae6ea) 70

[top level files](#section_ca7f367c1eca41afb8244a77c462ad7e) 31

[user hierarchy system generated files](#section_7b84720fcf8e499088672200b6d7d1a6) 72

[virtual directory](#section_0e526ce8f0344a21b43f9b3c930d9ca0) 29

[XM123 compression algorithm](#section_c6e2e96740c24b7da473c22621f30654) 173

[XMHybridRLE compression algorithms](#section_91ec6bb2098a440abbf95acbfe70dc0b) 173

[XMObject definitions by class attribute](#section_99defc8e38d0430fad7471be19741abd) 86

[XMObject document node element](#section_23dde626b187405590e15a2333f11c5f) 76

[XMRENoSplit compression algorithms](#section_85c2024e34e743748fa08b4ca8fe4f2d) 153

[Xpress compression](#section_3e3dac063f4548a593d4abacd4b34000) 196

[System-generated data files](#section_a713d4decb324086a8b62c5bbd3ae6ea) 70

T

[tbl.xml Metadata File example](#section_6425629e551746ca8707b7edf6ba674c) 197

[Top level files](#section_ca7f367c1eca41afb8244a77c462ad7e) 31

[Tracking changes](#section_fcc7501a722e437b9582e6a4d61a0077) 234

U

[User hierarchy system-generated files](#section_7b84720fcf8e499088672200b6d7d1a6) 72

V

[Vendor-extensible fields](#section_2b5a8556e2314019b6aa531fb3f06a76) 14

[Versioning](#section_ac671d12a9c74c25acd3959d019feef2) 14

[Virtual directory](#section_0e526ce8f0344a21b43f9b3c930d9ca0) 29

X

[XM123 compression algorithm](#section_c6e2e96740c24b7da473c22621f30654) 173

[XMHybridRLE compression algorithms](#section_91ec6bb2098a440abbf95acbfe70dc0b) 173

[XMObject definitions by class attribute](#section_99defc8e38d0430fad7471be19741abd) 86

[XMObject document node element](#section_23dde626b187405590e15a2333f11c5f) 76

[XMRENoSplit compression algorithms](#section_85c2024e34e743748fa08b4ca8fe4f2d) 153

[Xpress compression](#section_3e3dac063f4548a593d4abacd4b34000) 196