# Survey Form Options

## LinkedIn International Track

Use `create_linkedin_expert_form.gs` to create a private Google Form and its
private response spreadsheet:

1. Open https://script.google.com with the researcher's Google account.
2. Create a standalone Apps Script project.
3. Paste the generated `.gs` file and run
   `createArchitectureViewpointExpertForm` once.
4. Review the generated form. Keep the edit URL and response spreadsheet
   private; place the participant URL directly in the approved recruitment post.
5. The form performs screening and consent itself and closes automatically
   after three complete eligible submissions.
6. Do not enable response summaries, quiz mode, public result access, or Google-account email
   collection.
7. Freeze and export responses before revealing the manuscript, code, or AVDM
   reference classifications.

Export the private response sheet as CSV, then convert each response into the
existing analysis format:

```powershell
backend\venv\Scripts\python.exe paper\validation\convert_google_form_responses.py path\to\responses.csv
```

The converter assigns E1-E3 by eligible submission order, excludes contact
email from analysis, and refuses to overwrite an existing frozen participant workbook.
After conversion, run `analyze_expert_ratings.py` normally.

Google Forms is preferred over a shared Google Sheet because participants
cannot see or modify one another's responses. The existing E1-E3 Excel files
remain the offline fallback.

## China Track

Google Forms may be inaccessible or unreliable in mainland China. Use the
existing CN1-CN3 Excel workbooks, or build an equivalent private form in
Tencent Questionnaire, Wenjuanxing, or another service whose privacy terms are
acceptable.

`china_question_bank.csv` contains the exact 61 item IDs, English viewpoint
names, definitions, options, and required flags. Preserve the English technical
content and the three labels. Do not publish the form URL in the public
recruitment post; send it privately after screening and consent.

Form-platform exports must be converted to the same item-ID/rating matrix before
running `analyze_expert_ratings.py`. Payment and contact details must remain in
a separate private tracker, not in the response form.

### Tencent Questionnaire

1. Sign in at https://wj.qq.com and create a questionnaire with the text or
   low-code editor.
2. Enable question-setting syntax in the editor so `[必答]` and `[选答]` are
   recognized.
3. Paste the full content of `tencent_questionnaire_import.txt`.
4. Confirm that all 61 viewpoint items are single-choice questions with exactly
   `Mandatory`, `Recommended`, and `Optional`, and that every item is required.
5. Confirm that `===分页===` produced the case page, layer pages, and final
   confirmation page.
6. In the visual editor, configure No answers to recent architecture practice,
   multinational project experience, or consent, and Yes to prior model
   exposure, to terminate as ineligible before the rating pages.
7. Enable anonymous collection if compatible with the selected distribution
   mode; do not enable WeChat identity authorization, public voting results, or
   respondent access to statistics.
8. Run one desktop and one mobile test. Export questionnaire text and raw CSV
   after data freeze.

Official syntax documentation: https://wj.qq.com/docs/survey-dsl/content/grammar

### Wenjuanxing

1. Sign in at https://www.wjx.cn, create a questionnaire, and select text import
   or `从文本创建`.
2. Paste `wenjuanxing_questionnaire_import.txt` and inspect every recognized
   question before publishing.
3. Manually mark the screening, consent, all 61 viewpoint ratings, and two final
   confirmations as required. Keep layer rationale fields optional.
4. Add page breaks by layer in the visual editor; text import does not reliably
   preserve pagination.
5. Prefer Wenjuanxing's informed-consent control for the full consent text and
   retain a real decline option.
6. Configure ineligible answers to terminate before ratings. Set questionnaire
   and result visibility to non-public, and do not expose statistics.
7. Avoid WeChat authorization, SMS verification, email invitations, or IP-only
   restrictions if describing responses as anonymous. The participant code is
   sufficient for this three-person study.
8. Run desktop and mobile tests, then export responses by option text and retain
   the questionnaire version and codebook.

Official text-import documentation: https://www.wjx.cn/help/help.aspx?helpid=138
