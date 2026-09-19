// Generated from public/case_x_fixture.json.
// Keep this form private until all expert ratings are frozen.

function createArchitectureViewpointExpertForm() {
  const layers = [{"name": "Application", "items": [{"id": "A5", "viewpoint": "Application Domain Boundary", "definition": "Clarify service boundaries and domain ownership."}, {"id": "A6", "viewpoint": "Application Resilience Pattern", "definition": "Define fallback, retry, and graceful degradation strategy."}]}, {"name": "Architecture Governance & Decision", "items": [{"id": "AGD1", "viewpoint": "Architecture Decision View", "definition": "Decision rationale. What architectural decisions were made and why?"}, {"id": "AGD2", "viewpoint": "Evolution & Change Impact View", "definition": "Change analysis. What is impacted by a proposed change?"}, {"id": "AGD3", "viewpoint": "Quality Attribute Trade-off View", "definition": "Trade-off reasoning. How are quality attributes balanced?"}, {"id": "AGD4", "viewpoint": "Cost & Value View", "definition": "Economic impact. What are the costs and expected value?"}, {"id": "AGD5", "viewpoint": "Team-Architecture Alignment View", "definition": "Organizational fit. Are teams aligned with the architecture?"}]}, {"name": "Business / Organization", "items": [{"id": "B1", "viewpoint": "Business Capability View", "definition": "Capability structure. What business capabilities exist and which are critical?"}, {"id": "B2", "viewpoint": "Business Process View", "definition": "End-to-end workflows. How do business processes execute across domains?"}, {"id": "B3", "viewpoint": "User / Actor View", "definition": "Users and roles. Who interacts with the system and in what roles?"}, {"id": "B4", "viewpoint": "Organizational Ownership View", "definition": "Accountability and governance. Who owns systems, data, and decisions?"}, {"id": "B5", "viewpoint": "Interaction & Influence View", "definition": "Cross-domain influence. How do organizational units influence each other?"}]}, {"name": "Container / Component / Technical Service", "items": [{"id": "C1", "viewpoint": "Container View", "definition": "Runtime containers. What are the main runtime units?"}, {"id": "C2", "viewpoint": "Component View", "definition": "Internal modularity. How are components structured within containers?"}, {"id": "C3", "viewpoint": "Technical Service View", "definition": "Service responsibility. What capability boundary does each service own?"}, {"id": "C4", "viewpoint": "Technical Stack View", "definition": "Technology choices. Which languages, frameworks, and platforms are used?"}, {"id": "C5", "viewpoint": "Communication & Protocol View", "definition": "Interaction mechanisms. How do components communicate?"}]}, {"name": "Context & Application", "items": [{"id": "A1", "viewpoint": "System Context View", "definition": "System boundary. What is inside and outside the system?"}, {"id": "A2", "viewpoint": "Application Functional View", "definition": "Functional decomposition. How are application functions grouped?"}, {"id": "A3", "viewpoint": "Application Interaction View", "definition": "Application collaboration. How do applications interact and depend on each other?"}, {"id": "A4", "viewpoint": "User Role-Application Mapping View", "definition": "Access responsibility. Which roles can access which applications?"}]}, {"name": "Data Architecture", "items": [{"id": "D1", "viewpoint": "Business Data Flow View", "definition": "Business data movement. How does data support business processes?"}, {"id": "D10", "viewpoint": "Logical Data Model View", "definition": "Logical schema. How are entities logically related?"}, {"id": "D11", "viewpoint": "Physical Data Model View", "definition": "Physical schema. How is data physically implemented?"}, {"id": "D2", "viewpoint": "Data Derivation & Evolution View", "definition": "Data transformation. How is data derived and transformed?"}, {"id": "D3", "viewpoint": "Data Lineage View", "definition": "Traceability. Where does data originate and propagate?"}, {"id": "D4", "viewpoint": "Data Asset View", "definition": "Ownership and value. What data assets exist and who owns them?"}, {"id": "D5", "viewpoint": "Conceptual Data Entity View", "definition": "Business entities. What core business entities exist?"}, {"id": "D6", "viewpoint": "Data Quality View", "definition": "Quality assurance. Is data accurate, complete, and timely?"}, {"id": "D7", "viewpoint": "Data Compliance Flow View", "definition": "Regulatory paths. Does data usage comply with regulations?"}, {"id": "D8", "viewpoint": "Data Pipeline View", "definition": "Technical pipelines. How is data processed technically?"}, {"id": "D9", "viewpoint": "Data Sovereignty View", "definition": "Residency constraints. Where is data stored and restricted?"}]}, {"name": "Deployment / Infrastructure / Networking", "items": [{"id": "DIN1", "viewpoint": "Application Deployment Location View", "definition": "Deployment topology. Where are applications deployed?"}, {"id": "DIN2", "viewpoint": "Network Topology View", "definition": "Network segmentation. How is the network structured?"}, {"id": "DIN3", "viewpoint": "Infrastructure Composition View", "definition": "Infrastructure layout. What infrastructure components exist?"}, {"id": "DIN4", "viewpoint": "Resource & Capacity View", "definition": "Scaling and capacity. How are resources allocated and scaled?"}]}, {"name": "Governance", "items": [{"id": "AGD6", "viewpoint": "Control Traceability Matrix", "definition": "Trace controls to policies, systems, and responsible roles."}, {"id": "AGD7", "viewpoint": "Architecture Decision Record", "definition": "Document decision rationale and approval trail."}]}, {"name": "Infrastructure", "items": [{"id": "DIN5", "viewpoint": "Disaster Recovery", "definition": "Define backup, restore, and regional failover strategy."}, {"id": "DIN6", "viewpoint": "Scalability and Capacity", "definition": "Plan horizontal and vertical scaling with bottleneck controls."}]}, {"name": "Integration", "items": [{"id": "IP7", "viewpoint": "Interface Contract Stability", "definition": "Specify APIs, versioning, and compatibility guarantees."}, {"id": "IP8", "viewpoint": "Dependency and Interaction Map", "definition": "Capture cross-system dependencies and communication paths."}]}, {"name": "Integration & Processing", "items": [{"id": "IP1", "viewpoint": "Application Integration View", "definition": "Business-level integration. How do applications exchange data?"}, {"id": "IP2", "viewpoint": "Technical Integration View", "definition": "Technical constraints. What latency, throughput, or coupling constraints exist?"}, {"id": "IP3", "viewpoint": "System Processing View", "definition": "Execution semantics. How are requests processed end-to-end?"}, {"id": "IP4", "viewpoint": "Activity View", "definition": "Action paths. What actions and decisions occur during execution?"}, {"id": "IP5", "viewpoint": "Process Flow View", "definition": "Workflow execution. How do workflows orchestrate services?"}, {"id": "IP6", "viewpoint": "Sequence Interaction View", "definition": "Call ordering. What is the interaction sequence?"}]}, {"name": "Operations & Reliability", "items": [{"id": "OR1", "viewpoint": "Operations View", "definition": "Incident handling. How are incidents managed operationally?"}, {"id": "OR2", "viewpoint": "Resilience & DR View", "definition": "Recovery strategy. What are RPO/RTO objectives?"}, {"id": "OR3", "viewpoint": "Reliability & SLO View", "definition": "Reliability targets. What service levels are required?"}, {"id": "OR4", "viewpoint": "Monitoring & Observability View", "definition": "System visibility. How is system health observed?"}, {"id": "OR5", "viewpoint": "Operational Feedback View", "definition": "Learning loops. How do operations inform evolution?"}]}, {"name": "Security", "items": [{"id": "SCR11", "viewpoint": "Identity and Access Control", "definition": "Map authentication, authorization, and least privilege controls."}]}, {"name": "Security, Compliance & Risk", "items": [{"id": "SCR1", "viewpoint": "Security Control View", "definition": "Control mechanisms. What controls enforce security policy?"}, {"id": "SCR2", "viewpoint": "Threat & Risk Modeling View", "definition": "Threat analysis. What threats and risks exist?"}, {"id": "SCR3", "viewpoint": "Attack Path View", "definition": "Adversarial traversal. How could an attacker move through the system?"}, {"id": "SCR4", "viewpoint": "Service Authentication View", "definition": "Service trust. How do services authenticate each other?"}, {"id": "SCR5", "viewpoint": "User Authentication View", "definition": "User identity. How are users authenticated?"}, {"id": "SCR6", "viewpoint": "Authorization & Access Control View", "definition": "Access enforcement. Who is authorized to do what?"}, {"id": "SCR7", "viewpoint": "Compliance Boundary View", "definition": "Regulatory scope. Which regulations apply and where?"}]}];
  const form = FormApp.create('Independent Expert Study: Architecture Viewpoint Prioritization');
  form.setDescription(
    'Independent, unfunded personal research. Estimated completion time: 30-45 minutes. ' +
    'The scenario is fictional. Do not search for the underlying model, manuscript, preprint, ' +
    'source code, or reference output before submitting. A US$75 net-equivalent honorarium is ' +
    'offered as modest compensation for your time and does not depend on your ratings. ' +
    'The form closes after three complete eligible responses.'
  );
  form.setCollectEmail(false);
  form.setProgressBar(true);
  form.setConfirmationMessage(
    'Your response has been recorded. The researcher will contact eligible participants using the private email supplied in this form.'
  );

  const responseSheet = SpreadsheetApp.create(
    'PRIVATE - Architecture Viewpoint Expert Study Responses'
  );
  form.setDestination(FormApp.DestinationType.SPREADSHEET, responseSheet.getId());

  form.addSectionHeaderItem()
    .setTitle('Study information and consent')
    .setHelpText(
      'Purpose: compare experienced architects independent viewpoint priorities with a configurable decision model.\n' +
      'Data: contact email is used only for communication/payment and is excluded from analysis. Role category, experience range, ratings, and rationales are analyzed pseudonymously.\n' +
      'Participation is voluntary. You may request withdrawal before September 17, 2026. Do not include employer or client confidential information. Completing the study does not confer authorship. No formal institutional ethics approval is claimed.'
    );
  const emailValidation = FormApp.createTextValidation()
    .requireTextIsEmail()
    .setHelpText('Used privately for eligibility confirmation and honorarium only; excluded from the analysis dataset.')
    .build();
  form.addTextItem()
    .setTitle('Private contact email')
    .setValidation(emailValidation)
    .setRequired(true);
  form.addCheckboxItem()
    .setTitle('Eligibility confirmation')
    .setChoiceValues([
      'I have at least five years of professional architecture experience and have performed architecture design or review within the last two years.'
    ])
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('Current architecture role')
    .setChoiceValues(['Software Architect', 'Solution Architect', 'Systems Architect', 'Enterprise Architect', 'Other'])
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('Architecture experience range')
    .setChoiceValues(['5-9', '10-14', '15-19', '20+'])
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('Architecture design or review work within the last two years')
    .setChoiceValues(['Yes', 'No'])
    .setRequired(true);
  form.addCheckboxItem()
    .setTitle('Relevant experience areas')
    .setChoiceValues(['Data', 'Integration', 'Security', 'Compliance', 'Cloud', 'AI/ML', 'Other'])
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('Previous exposure to the decision model, software, or manuscript')
    .setChoiceValues(['No', 'Yes'])
    .setRequired(true);
  form.addMultipleChoiceItem()
    .setTitle('Previous collaboration with the researcher on this model, manuscript, or scenario')
    .setChoiceValues(['No', 'Yes'])
    .setRequired(true);
  form.addCheckboxItem()
    .setTitle('Consent and independence confirmation')
    .setChoiceValues([
      'I consent to participate, will complete the task independently, and understand that participation does not confer authorship.'
    ])
    .setRequired(true);

  form.addPageBreakItem().setTitle('Case X: Fictional Cross-Border Data Platform');
  form.addSectionHeaderItem()
    .setTitle('Project brief')
    .setHelpText("This is a fictional benchmark and does not represent an actual company or project. A new custom data-integration platform will interact with 6-20 external systems and modify 21-50 existing applications. It spans 4-10 data centers and multiple cloud providers within a single region, uses 6-10 technology-stack kinds and 3-5 integration-technology kinds, and includes cross-border data flow, more than one million personal-data records, more than 100,000 sensitive-data records, and government/security-classified data. No non-standard authentication or authorization is reported.");
  form.addSectionHeaderItem()
    .setTitle('Rating definitions')
    .setHelpText(
      'Mandatory: omission would leave unacceptable decision, compliance, or operational exposure.\n' +
      'Recommended: materially useful, but deferrable with an explicit rationale.\n' +
      'Optional: low expected decision value under the stated scenario.'
    );

  layers.forEach((layer) => {
    form.addPageBreakItem().setTitle(layer.name);
    layer.items.forEach((item) => {
      form.addMultipleChoiceItem()
        .setTitle(item.id + ' - ' + item.viewpoint)
        .setHelpText(item.definition)
        .setChoiceValues(['Mandatory', 'Recommended', 'Optional'])
        .setRequired(true);
    });
  });

  form.addPageBreakItem().setTitle('Final confirmation');
  form.addParagraphTextItem()
    .setTitle('Optional rationale or insufficient-information notes')
    .setHelpText(
      'Complete only when needed. Use one line per item in the format: item_id: rationale or missing information. Do not include confidential employer or client information.'
    )
    .setRequired(false);
  form.addCheckboxItem()
    .setTitle('Independent completion confirmation')
    .setChoiceValues([
      'I completed the ratings independently and did not consult the model, manuscript, source code, preprint, or another participant.'
    ])
    .setRequired(true);
  form.addCheckboxItem()
    .setTitle('Confidentiality confirmation')
    .setChoiceValues([
      'I did not include confidential employer, client, system, or project information.'
    ])
    .setRequired(true);

  ScriptApp.newTrigger('handleArchitectureExpertSubmission')
    .forForm(form)
    .onFormSubmit()
    .create();

  Logger.log('EDIT URL: ' + form.getEditUrl());
  Logger.log('PARTICIPANT URL: ' + form.getPublishedUrl());
  Logger.log('PRIVATE RESPONSE SHEET: ' + responseSheet.getUrl());
}

function handleArchitectureExpertSubmission(event) {
  const answers = {};
  event.response.getItemResponses().forEach((itemResponse) => {
    answers[itemResponse.getItem().getTitle()] = itemResponse.getResponse();
  });
  const ratingCount = Object.keys(answers).filter((title) =>
    /^[A-Za-z0-9_]+ - /.test(title) &&
    ['Mandatory', 'Recommended', 'Optional'].includes(answers[title])
  ).length;
  const eligible =
    answers['Architecture design or review work within the last two years'] === 'Yes' &&
    answers['Previous exposure to the decision model, software, or manuscript'] === 'No' &&
    answers['Previous collaboration with the researcher on this model, manuscript, or scenario'] === 'No' &&
    Boolean(answers['Eligibility confirmation']) &&
    Boolean(answers['Consent and independence confirmation']) &&
    Boolean(answers['Independent completion confirmation']) &&
    Boolean(answers['Confidentiality confirmation']) &&
    ratingCount === 61;
  if (!eligible) return;

  const lock = LockService.getScriptLock();
  lock.waitLock(30000);
  try {
    const properties = PropertiesService.getScriptProperties();
    const countKey = 'ELIGIBLE_RESPONSE_COUNT_' + event.source.getId();
    const count = Number(properties.getProperty(countKey) || '0') + 1;
    properties.setProperty(countKey, String(count));
    if (count >= 3) {
      event.source.setAcceptingResponses(false);
      event.source.setCustomClosedFormMessage(
        'Recruitment is complete. Thank you for your interest in supporting this research.'
      );
    }
  } finally {
    lock.releaseLock();
  }
}
