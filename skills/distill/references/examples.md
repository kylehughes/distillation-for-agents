# Contrasting examples

Every scenario is invented and its relevant rules are stated here. Clinical, legal, and financial vocabulary illustrates reasoning; it does not supply guidance for a real case. Treat these as teaching examples, not independent evidence of generalization.

## Contents

- [Combine branches while retaining obligations](#combine-branches-while-retaining-obligations)
- [Retain state needed after the next event](#retain-state-needed-after-the-next-event)
- [Preserve conditions in a plain-language explanation](#preserve-conditions-in-a-plain-language-explanation)
- [Compress a note without resolving uncertainty](#compress-a-note-without-resolving-uncertainty)
- [Distinguish cash timing from a total](#distinguish-cash-timing-from-a-total)
- [Replace a workflow while preserving its functions](#replace-a-workflow-while-preserving-its-functions)
- [Correct a mistaken starting model](#correct-a-mistaken-starting-model)
- [Preserve expressive ambiguity](#preserve-expressive-ambiguity)
- [Learn the distinctions of an unfamiliar domain](#learn-the-distinctions-of-an-unfamiliar-domain)
- [Recognize an adequate stopping point](#recognize-an-adequate-stopping-point)

## Combine branches while retaining obligations

**Task.** Simplify registration instructions for a fictional workshop. Participants may be students or employees. The supplied policy says that everyone with a valid invitation receives a badge and a confirmation message; everyone without an invitation is sent to the registration desk. Participant category has no effect on registration. The current instructions repeat both branches separately for students and employees.

**Useful reduction.** Use two invitation-based branches. For a valid invitation, issue the badge and send the confirmation. Otherwise direct the participant to registration.

**Check.** Compare the actions for all four combinations of category and invitation status. Each combination must retain the same complete action list. The confirmation message is an obligation even though it does not change which branch is selected.

**Failure.** “Invited participants get badges” is shorter but loses both the confirmation and the handling of other participants. Merging branches is successful only when their effects remain complete.

**Transfer.** Remove a variable when it does no work for the task; retain relationships and downstream actions that still do work.

## Retain state needed after the next event

**Task.** Simplify the display model for a fictional reading device. While disconnected, every device shows “offline.” After reconnection, a device with a valid access token must resume its saved page automatically; a device with an expired token requests sign-in. Token validity is locally available.

**Useful reduction.** Present one offline status to the reader while retaining token validity internally or recomputing it reliably on reconnection. Hide transport diagnostics that the reader does not need.

**Check.** Simulate reconnection for both token conditions. The simpler presentation must still support the two required later actions. Verify that recomputation is available at that point rather than merely assuming it.

**Failure.** Erasing token information and always requiring sign-in simplifies storage by violating the required automatic resumption. Treating every disconnected device as ready to resume violates the other branch.

**Transfer.** A simple surface and an adequate internal model can have different levels of detail. Present equivalence does not establish equivalence under future events.

## Preserve conditions in a plain-language explanation

**Task.** Explain this invented license rule: “The organizer may publish a recording only if every identifiable speaker has consented and the recording contains no restricted material. Even when both conditions hold, publication remains optional.” These supplied rules are the complete authority for the example.

**Useful explanation.** “The organizer can choose to publish only when all identifiable speakers consent and the recording contains no restricted material.”

**Check.** Examine a consenting group with restricted material, an unrestricted recording with one nonconsenting speaker, and a recording satisfying both conditions. Publication is unavailable in the first two cases and optional in the third.

**Failure.** “The organizer publishes recordings with consent” loses a condition and turns permission into an obligation. “Consent allows publication” incorrectly suggests that consent is sufficient by itself.

**Transfer.** Preserve modality, conjunctions, scope, and necessary conditions. Use the actual authoritative text and context for a real document.

## Compress a note without resolving uncertainty

**Task.** Summarize an invented research-clinic note for a colleague: “Participant reports lightheadedness after the morning capsule. The symptom was not observed by staff. Hydration status was not recorded. Cause has not been determined. No decision about causation has been made.” The task is faithful summarization, with no treatment recommendation requested.

**Useful summary.** “Participant reports lightheadedness after the morning capsule; staff did not observe it, hydration was unrecorded, and the cause remains undetermined.”

**Check.** Preserve the reporter, temporal order, lack of staff observation, and uncertainty. Remove the repeated statement about unresolved causation.

**Failure.** “Capsule caused lightheadedness” changes temporal association into causation. “No lightheadedness observed” alone can misleadingly erase the participant's report. “Hydration normal” invents a finding.

**Transfer.** Compress repeated wording while retaining evidential status. A summary should not become more certain than its source.

## Distinguish cash timing from a total

**Task.** Explain whether an invented project can pay an invoice on Tuesday. It has 500 credits available Monday, must pay 900 credits Tuesday, and will receive 800 credits Thursday. No other resources, credit arrangements, or payments are available. All these amounts and dates are certain within the example.

**Useful representation.** Show the dated cash sequence. Tuesday has a 400-credit shortfall; Thursday's receipt arrives after the required payment date. The project would have 400 credits remaining after all listed receipts and payments, but that end-period total does not establish Tuesday's ability to pay.

**Check.** Calculate resources available at the decision time, then distinguish that result from the eventual total. If the receipt moves to Monday, the Tuesday answer changes. If only the invoice's descriptive label changes, it does not.

**Failure.** “The project has a positive balance overall” answers the wrong question. Inventing a loan or assuming the payment can be delayed changes the supplied constraints.

**Transfer.** Preserve time when timing changes feasible actions. Do not merge a flow across a period with resources available at a particular moment.

## Replace a workflow while preserving its functions

**Task.** Reduce the effort of a fictional weekly review meeting. Its observed functions are assigning one owner to each unresolved issue, exposing dependencies, and recording a decision. A separate shared board already supports all three functions. In this example, every participant has access, and ambiguous issues can be escalated to a short discussion.

**Candidate.** Move routine items to the board, retain the discussion route for ambiguity, and test the change on a limited group under the existing authorization. Use explicit owner and decision fields so the replacement performs the established functions.

**Check.** Examine unresolved ownership, missed dependencies, decision accessibility, total participant effort, and escalation use. Compare these with the earlier process before claiming success.

**Failure.** Deleting the meeting without a replacement can move coordination into private messages and memory. Counting calendar minutes alone misses that transfer. Conversely, retaining the entire meeting merely because it once served a purpose ignores evidence that its functions now have substitutes.

**Transfer.** Distinguish removing an activity from removing its functions. A proposed replacement remains a proposal until the relevant behavior is observed.

## Correct a mistaken starting model

**Task.** Simplify a fictional archive's lending guide using its supplied policy. Originals may be viewed only in the reading room. Digitized copies may be viewed remotely. A copy request requires attribution in either setting. The current guide says, “Digitized materials require no restrictions.”

**Useful correction.** Organize the guide by the two independent questions: where the material may be viewed and what attribution a copy request requires. State that original material stays in the reading room, digitized copies support remote viewing, and attribution remains required for either kind of copy request.

**Check.** Examine remote viewing of a digitized copy, attempted remote viewing of an original, and copy requests for both forms. The current guide fails because it expands one permission into the absence of all obligations.

**Failure.** Preserving the current guide's rule would preserve its error. Merely adding many exceptions around it would leave a misleading organizing principle.

**Transfer.** Find the authority beneath an existing description. Correct the structure when it confuses independent dimensions.

## Preserve expressive ambiguity

**Task.** Shorten a fictional scene brief. A gardener finds a gate open. One neighbor thinks the absent owner returned; another thinks wind moved the gate. Neither explanation is confirmed. The intended effect is quiet uncertainty, and the scene must end with the gardener deciding to inspect the path rather than announcing an answer.

**Useful brief.** “An open gate makes one neighbor suspect the owner has returned; another blames the wind. Keep the cause unresolved and the tone quiet; end with the gardener inspecting the path.” Retain both concrete interpretations because they guide the later scene.

**Check.** Read the revision for shared observation, distinct interpretations, unresolved cause, tone, and the required final action. Use qualitative judgment for tone, and direct comparison for explicit constraints.

**Failure.** Revealing that the wind opened the gate makes the account simpler by removing a required experience. A generic sentence about mystery may also lose the particular tension between the neighbors.

**Transfer.** Preserve intentional ambiguity and expressive function. Some losses can be checked mechanically; others require informed judgment rather than a fabricated score.

## Learn the distinctions of an unfamiliar domain

**Task.** Produce a concise guide to a fictional beacon language. A triangle selects the eastern path; a square selects the western path. One pulse means proceed normally; two pulses mean wait for an escort. Hue is decorative and has no meaning. These are the complete supplied semantics.

**Useful guide.** Separate destination from action: shape selects the path, and pulse count selects whether to proceed or wait. Omit hue from the operational guide while retaining the two-dimensional rule.

**Check.** Evaluate all four shape/count combinations. Change hue and confirm that the action remains the same. Change the pulse count while keeping shape fixed and confirm that the required action changes.

**Failure.** Keeping only shape yields the destination but loses the escort requirement. Keeping only pulse count yields the action but loses the path. Applying a familiar traffic-color convention invents semantics absent from the supplied system.

**Transfer.** Derive the relevant distinctions from the domain's evidence. A concise factorization can be simpler than enumerating every combination, provided the combination rule remains explicit.

## Recognize an adequate stopping point

**Task.** Make a fictional equipment-return rule easier to understand while preserving the item, deadline, and required act: “Return borrowed lenses by noon Friday.” The intended readers understand every term, and there is no evidence of confusion or a request for a different format.

**Useful result.** Retain the sentence: it already expresses the required act, item, and deadline clearly. Conclude that no worthwhile improvement is established for this task, without claiming global minimality.

**Check.** Proposed deletion of “borrowed” broadens the item category. Deleting “noon” changes the deadline. Abbreviation creates a different presentation without an evidenced benefit for these readers.

**Failure.** Inventing exceptions, a flowchart, or a verification procedure manufactures complexity around an adequate instruction.

**Transfer.** Stop when the task is adequately served. The skill should improve the result, not require a visible transformation as proof that it was used.
