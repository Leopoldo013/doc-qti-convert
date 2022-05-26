

def manipula_xml_1(indent, correta, pergunta, a, b, c, d, e, resposta, justificativa):
    manifest = '''<?xml version='1.0' encoding='UTF-8'?>
<assessmentItem xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:ns9="http://www.imsglobal.org/xsd/apip/apipv1p0/imsapip_qtiv1p0" xmlns:ns8="http://www.w3.org/1999/xlink" title="" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" adaptive="false" timeDependent="false" identifier="QUE__{}_1">
    <responseDeclaration cardinality="single" baseType="identifier" identifier="RESPONSE">
        <correctResponse>
            <value>{}</value>
        </correctResponse>
    </responseDeclaration>
    <outcomeDeclaration identifier="SCORE" cardinality="single" baseType="float">
        <defaultValue>
            <value>0</value>
        </defaultValue>
    </outcomeDeclaration>
    <outcomeDeclaration identifier="FEEDBACKBASIC" cardinality="single" baseType="identifier" />
    <outcomeDeclaration identifier="MAXSCORE" cardinality="single" baseType="float">
        <defaultValue>
            <value>0</value>
        </defaultValue>
    </outcomeDeclaration>
    <itemBody>
        <div>
            <p>
                {}
            </p>
        </div>
        <choiceInteraction responseIdentifier="RESPONSE" maxChoices="1" shuffle="true">
            <simpleChoice identifier="answer_1" fixed="true">
                <p>
                    {}
                </p>
            </simpleChoice>
            <simpleChoice identifier="answer_2" fixed="true">
                <p>
                    {}
                </p>
            </simpleChoice>
            <simpleChoice identifier="answer_3" fixed="true">
                <p>
                    {}
                </p>
            </simpleChoice>
            <simpleChoice identifier="answer_4" fixed="true">
                <p>
                    {}
                </p>
            </simpleChoice>
            <simpleChoice identifier="answer_5" fixed="true">
                <p>
                    {}
                </p>
            </simpleChoice>
        </choiceInteraction>
    </itemBody>
    <responseProcessing>
        <responseCondition>
            <responseIf>
                <match>
                    <variable identifier="RESPONSE" />
                    <correct identifier="RESPONSE" />
                </match>
                <setOutcomeValue identifier="SCORE">
                    <variable identifier="MAXSCORE" />
                </setOutcomeValue>
                <setOutcomeValue identifier="FEEDBACKBASIC">
                    <baseValue baseType="identifier">correct_fb</baseValue>
                </setOutcomeValue>
            </responseIf>
            <responseElse>
                <setOutcomeValue identifier="FEEDBACKBASIC">
                    <baseValue baseType="identifier">incorrect_fb</baseValue>
                </setOutcomeValue>
            </responseElse>
        </responseCondition>
    </responseProcessing>
    <modalFeedback showHide="show" outcomeIdentifier="FEEDBACKBASIC" identifier="correct_fb">
        <div>
            <div>
                <p>
                    <span>A resposta correta é</span>
                   {}
                </p>
            </div>
            <div>
                <p>
                    <span>Justificativa</span>
                    
                </p>
            </div>
            <div>
                <p>
                    {}
                </p>
            </div>
        </div>
    </modalFeedback>
    <modalFeedback showHide="show" outcomeIdentifier="FEEDBACKBASIC" identifier="incorrect_fb">
        <div>
            <div>
                <p>
                    <span>A resposta correta é</span>
                    {}
                </p>
            </div>
            <div>
                <p>
                    <span>Justificativa</span>
                    <span>&#xa0;</span>
                </p>
            </div>
            <div>
                <p>
                    {}
                </p>
            </div>
        </div>
    </modalFeedback>
</assessmentItem>'''.format(indent, correta, pergunta, a, b, c, d, e, resposta, justificativa, resposta, justificativa)
    return manifest


manifest_banco1 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco2 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
       <dependency identifierref="assessmentItem00002"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco3 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
    <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
      <dependency identifierref="assessmentItem00002"/>
      <dependency identifierref="assessmentItem00003"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00003.xml" identifier="assessmentItem00003" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00003.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco4 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
      <dependency identifierref="assessmentItem00002"/>
      <dependency identifierref="assessmentItem00003"/>
      <dependency identifierref="assessmentItem00004"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00003.xml" identifier="assessmentItem00003" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00003.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00004.xml" identifier="assessmentItem00004" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00004.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco5 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
      <dependency identifierref="assessmentItem00002"/>
      <dependency identifierref="assessmentItem00003"/>
      <dependency identifierref="assessmentItem00004"/>
      <dependency identifierref="assessmentItem00005"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00003.xml" identifier="assessmentItem00003" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00003.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00004.xml" identifier="assessmentItem00004" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00004.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00005.xml" identifier="assessmentItem00005" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00005.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco6 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
      <dependency identifierref="assessmentItem00002"/>
      <dependency identifierref="assessmentItem00003"/>
      <dependency identifierref="assessmentItem00004"/>
      <dependency identifierref="assessmentItem00005"/>
      <dependency identifierref="assessmentItem00006"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00003.xml" identifier="assessmentItem00003" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00003.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00004.xml" identifier="assessmentItem00004" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00004.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00005.xml" identifier="assessmentItem00005" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00005.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00006.xml" identifier="assessmentItem00006" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00006.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco7 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
      <dependency identifierref="assessmentItem00002"/>
      <dependency identifierref="assessmentItem00003"/>
      <dependency identifierref="assessmentItem00004"/>
      <dependency identifierref="assessmentItem00005"/>
      <dependency identifierref="assessmentItem00006"/>
      <dependency identifierref="assessmentItem00007"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00003.xml" identifier="assessmentItem00003" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00003.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00004.xml" identifier="assessmentItem00004" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00004.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00005.xml" identifier="assessmentItem00005" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00005.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00006.xml" identifier="assessmentItem00006" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00006.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00007.xml" identifier="assessmentItem00007" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00007.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco8 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
      <dependency identifierref="assessmentItem00002"/>
      <dependency identifierref="assessmentItem00003"/>
      <dependency identifierref="assessmentItem00004"/>
      <dependency identifierref="assessmentItem00005"/>
      <dependency identifierref="assessmentItem00006"/>
      <dependency identifierref="assessmentItem00007"/>
      <dependency identifierref="assessmentItem00008"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00003.xml" identifier="assessmentItem00003" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00003.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00004.xml" identifier="assessmentItem00004" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00004.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00005.xml" identifier="assessmentItem00005" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00005.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00006.xml" identifier="assessmentItem00006" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00006.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00007.xml" identifier="assessmentItem00007" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00007.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00008.xml" identifier="assessmentItem00008" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00008.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco9 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <dependency identifierref="assessmentItem00001"/>
      <dependency identifierref="assessmentItem00002"/>
      <dependency identifierref="assessmentItem00003"/>
      <dependency identifierref="assessmentItem00004"/>
      <dependency identifierref="assessmentItem00005"/>
      <dependency identifierref="assessmentItem00006"/>
      <dependency identifierref="assessmentItem00007"/>
      <dependency identifierref="assessmentItem00008"/>
      <dependency identifierref="assessmentItem00009"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00003.xml" identifier="assessmentItem00003" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00003.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00004.xml" identifier="assessmentItem00004" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00004.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00005.xml" identifier="assessmentItem00005" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00005.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00006.xml" identifier="assessmentItem00006" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00006.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00007.xml" identifier="assessmentItem00007" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00007.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00008.xml" identifier="assessmentItem00008" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00008.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00009.xml" identifier="assessmentItem00009" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00009.xml"/>
    </resource>
   </resources>
</manifest>'''

manifest_banco10 = '''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="man00001"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:csm="http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0"
  xmlns:imsmd="http://ltsc.ieee.org/xsd/LOM"
  xmlns:imsqti="http://www.imsglobal.org/xsd/imsqti_metadata_v2p1"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p2.xsd http://ltsc.ieee.org/xsd/LOM imsmd_loose_v1p3.xsd http://www.imsglobal.org/xsd/imsqti_metadata_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_metadata_v2p1.xsd http://www.imsglobal.org/xsd/imsccv1p2/imscsmd_v1p0 http://www.imsglobal.org/profile/cc/ccv1p2/ccv1p2_imscsmd_v1p0.xsd">
  <metadata>
    <schema>QTIv2.1</schema>
    <schemaversion>2.0</schemaversion>
  </metadata>
  <organizations/>
  <resources>
    <resource href="qti21/question_bank00001.xml" identifier="question_bank00001" type="imsqti_test_xmlv2p1">
      <file href="qti21/question_bank00001.xml"/>
      <dependency identifierref="assessmentItem00001"/>
      <dependency identifierref="assessmentItem00002"/>
      <dependency identifierref="assessmentItem00003"/>
      <dependency identifierref="assessmentItem00004"/>
      <dependency identifierref="assessmentItem00005"/>
      <dependency identifierref="assessmentItem00006"/>
      <dependency identifierref="assessmentItem00007"/>
      <dependency identifierref="assessmentItem00008"/>
      <dependency identifierref="assessmentItem00009"/>
      <dependency identifierref="assessmentItem00010"/>
    </resource>
    <resource href="qti21/assessmentItem00001.xml" identifier="assessmentItem00001" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00001.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00002.xml" identifier="assessmentItem00002" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00002.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00003.xml" identifier="assessmentItem00003" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00003.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00004.xml" identifier="assessmentItem00004" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00004.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00005.xml" identifier="assessmentItem00005" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00005.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00006.xml" identifier="assessmentItem00006" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00006.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00007.xml" identifier="assessmentItem00007" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00007.xml"/>
    </resource>
    <resource href="qti21/assessmentItem00008.xml" identifier="assessmentItem00008" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00008.xml"/>
    </resource>
     <resource href="qti21/assessmentItem00010.xml" identifier="assessmentItem00010" type="imsqti_item_xmlv2p1">
      <file href="qti21/assessmentItem00010.xml"/>
    </resource>
   </resources>
</manifest>'''


def imsManifest(perguntas):
    if perguntas == 1:
        return manifest_banco1
    if perguntas == 2:
        return manifest_banco2
    if perguntas == 3:
        return manifest_banco3
    if perguntas == 4:
        return manifest_banco4
    if perguntas == 5:
        return manifest_banco5
    if perguntas == 6:
        return manifest_banco6
    if perguntas == 7:
        return manifest_banco7
    if perguntas == 8:
        return manifest_banco8
    if perguntas == 9:
        return manifest_banco9
    if perguntas == 10:
        return manifest_banco10


def bancoManifest(perguntas, titulo):
    if perguntas == 1:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
         </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 2:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
         </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 3:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
            <assessmentItemRef identifier="assessmentItem00003" href="assessmentItem00003.xml" />
        </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 4:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
            <assessmentItemRef identifier="assessmentItem00003" href="assessmentItem00003.xml" />
            <assessmentItemRef identifier="assessmentItem00004" href="assessmentItem00004.xml" />
         </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 5:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
            <assessmentItemRef identifier="assessmentItem00003" href="assessmentItem00003.xml" />
            <assessmentItemRef identifier="assessmentItem00004" href="assessmentItem00004.xml" />
            <assessmentItemRef identifier="assessmentItem00005" href="assessmentItem00005.xml" />
        </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 6:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
            <assessmentItemRef identifier="assessmentItem00003" href="assessmentItem00003.xml" />
            <assessmentItemRef identifier="assessmentItem00004" href="assessmentItem00004.xml" />
            <assessmentItemRef identifier="assessmentItem00005" href="assessmentItem00005.xml" />
            <assessmentItemRef identifier="assessmentItem00006" href="assessmentItem00006.xml" />
        </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 7:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
            <assessmentItemRef identifier="assessmentItem00003" href="assessmentItem00003.xml" />
            <assessmentItemRef identifier="assessmentItem00004" href="assessmentItem00004.xml" />
            <assessmentItemRef identifier="assessmentItem00005" href="assessmentItem00005.xml" />
            <assessmentItemRef identifier="assessmentItem00006" href="assessmentItem00006.xml" />
            <assessmentItemRef identifier="assessmentItem00007" href="assessmentItem00007.xml" />
        </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 8:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
            <assessmentItemRef identifier="assessmentItem00003" href="assessmentItem00003.xml" />
            <assessmentItemRef identifier="assessmentItem00004" href="assessmentItem00004.xml" />
            <assessmentItemRef identifier="assessmentItem00005" href="assessmentItem00005.xml" />
            <assessmentItemRef identifier="assessmentItem00006" href="assessmentItem00006.xml" />
            <assessmentItemRef identifier="assessmentItem00007" href="assessmentItem00007.xml" />
            <assessmentItemRef identifier="assessmentItem00008" href="assessmentItem00008.xml" />
        </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 9:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
            <assessmentItemRef identifier="assessmentItem00003" href="assessmentItem00003.xml" />
            <assessmentItemRef identifier="assessmentItem00004" href="assessmentItem00004.xml" />
            <assessmentItemRef identifier="assessmentItem00005" href="assessmentItem00005.xml" />
            <assessmentItemRef identifier="assessmentItem00006" href="assessmentItem00006.xml" />
            <assessmentItemRef identifier="assessmentItem00007" href="assessmentItem00007.xml" />
            <assessmentItemRef identifier="assessmentItem00008" href="assessmentItem00008.xml" />
            <assessmentItemRef identifier="assessmentItem00009" href="assessmentItem00009.xml" />
        </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
    if perguntas == 10:
        return '''<?xml version="1.0" encoding="UTF-8"?>
<assessmentTest xmlns="http://www.imsglobal.org/xsd/imsqti_v2p1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsqti_v2p1 http://www.imsglobal.org/xsd/qti/qtiv2p1/imsqti_v2p1.xsd" identifier="question_bank00001" title="{}">
    <testPart identifier="question_bank00001_1" navigationMode="nonlinear" submissionMode="simultaneous">
        <assessmentSection identifier="question_bank00001_1_1" visible="false" title="Section 1">
            <assessmentItemRef identifier="assessmentItem00001" href="assessmentItem00001.xml" />
            <assessmentItemRef identifier="assessmentItem00002" href="assessmentItem00002.xml" />
            <assessmentItemRef identifier="assessmentItem00003" href="assessmentItem00003.xml" />
            <assessmentItemRef identifier="assessmentItem00004" href="assessmentItem00004.xml" />
            <assessmentItemRef identifier="assessmentItem00005" href="assessmentItem00005.xml" />
            <assessmentItemRef identifier="assessmentItem00006" href="assessmentItem00006.xml" />
            <assessmentItemRef identifier="assessmentItem00007" href="assessmentItem00007.xml" />
            <assessmentItemRef identifier="assessmentItem00008" href="assessmentItem00008.xml" />
            <assessmentItemRef identifier="assessmentItem00009" href="assessmentItem00009.xml" />
            <assessmentItemRef identifier="assessmentItem00009" href="assessmentItem00010.xml" />
        </assessmentSection>
    </testPart>
</assessmentTest>'''.format(titulo)
