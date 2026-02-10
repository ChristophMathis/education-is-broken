# Proposal 3: Causal Chains

## Evaluation

The critique is valid and consequential. Both causal chains suffer from the same structural problem: the book presents technological capability as if it automatically produces market adoption. In reality, there are friction points -- network effects, signalling inertia, and employer incentives -- that can indefinitely sustain the old system even when technically superior alternatives exist.

**On 3.1 (AI to unbundling):** Chapter 02 correctly identifies what AI can do and why the bundle is vulnerable. But it does not answer the hardest question: if the intelligence factory can deliver better learning, why would students and employers stick with universities? The answer is not that they would not, but that unbundling is not automatic. It requires a tipping point where the prestige value of a degree becomes smaller than the value of demonstrated capability. This is an equilibrium problem, not just a capability problem, and the chapter does not model the equilibrium shift.

**On 3.2 (skills rhetoric to hiring practice):** The contradiction between "81% of employers say they use skills-based hiring" and "most still require degrees" is real, and it points to a deeper issue: employers may rationally prefer degrees even when they have access to better information about candidate skills. The chapter provides the data but not the economic model that explains it. Why would a hiring manager spend time and money learning to interpret a complex signalling stack when a degree offers a simple, legible, legally defensible filter? What would change their incentive?

Both gaps can be filled with the same kind of reasoning: identify the rational incentives that sustain the status quo, then specify the threshold conditions under which those incentives flip.

---

## Proposed Solution for 3.1 (AI to Unbundling)

**Placement:** In Chapter 02, after the section "From Credentials to Portfolios" (around line 35-43), insert a new subsection titled "The Unbundling Threshold: Network Effects and Prestige Inertia."

**Proposed text:**

### The Unbundling Threshold: Network Effects and Prestige Inertia

Unbundling does not happen just because better tools exist. It happens when the incentives that hold the bundle together weaken enough to create a cascade. Understanding when -- and whether -- that happens requires looking at what actually keeps universities together in the first place.

The traditional university bundle is held together by two interlocking incentives, each stronger than it appears:

**Network effects.** Students do not attend Harvard for the lectures alone. They attend for access to peers, faculty, and alumni who themselves attended Harvard. This creates a self-reinforcing cycle: employers hire from Harvard because Harvard graduates are disproportionately successful; talented students attend Harvard because employers hire from it; the success of graduates makes the network more valuable. The degree is the formal credential, but the network is the real product. AI tutors, no matter how good, cannot replicate this. A student learning quantum mechanics from the best AI tutor in the world is not building a relationship with someone who will sit beside her in a startup ten years later.

**Prestige inertia.** Even when alternatives are superior in measurable ways, institutional prestige is sticky. A degree from an Ivy League university signals not just capability but access -- it certifies that you survived a gauntlet that most people did not attempt. Employers use this signal partly because it works, but also because it is legally defensible and culturally understood. When everything else is uncertain, saying "we hire from top schools" is a safe decision. Changing that decision requires not just demonstrating that portfolios work better, but accepting the social and legal risk that comes with being wrong about a person who looks good on paper but fails on the job.

These are not technical problems. They are equilibrium problems. The bundle persists not because it is optimal, but because everyone coordinated on it. For unbundling to happen, three conditions must be met:

1. **Employer confidence in alternatives must exceed employer confidence in degrees.** This is not a small gap to close. Degrees have been filtered through decades of hiring experience. Portfolios, micro-credentials, and skills assessments are newer, messier, and require more judgment to interpret. The risk of making a bad hire using a portfolio feels higher, even if the statistical likelihood is lower. This perception gap persists until the evidence becomes overwhelming and the social cost of ignoring it becomes public and visible.

2. **The value of the network must erode.** If the best people still cluster in traditional universities, then the degree retains value as a network gateway regardless of what it certifies academically. This erosion happens if: (a) the quality of peers becomes available through other mechanisms -- bootcamps, online cohorts, professional associations -- (b) remote work and distributed teams reduce the value of physical proximity, and (c) employers start matching candidates based on what they can do rather than where they went to school, breaking the feedback loop that sends the best students to the best universities.

3. **A critical mass must defect together.** This is the coordination problem. A single employer dropping degree requirements gains nothing if all other employers still use them as a filter. A single student skipping university gains nothing if employers still expect degrees. But if enough employers simultaneously shift, the signal travels backward: students stop incurring the cost of degrees, universities scramble to adapt, and the threshold flips. The tech industry approached this threshold in certain roles; most of the economy has not.

The realistic implication is this: unbundling will not be universal or inevitable. It will be sectoral. In technology, design, and parts of business where demonstrated work is easily verifiable and prestige-neutral (you can assess a programmer by looking at her code regardless of where she learned), unbundling can happen rapidly. The existence of alternatives -- bootcamps, self-taught learning, open-source contribution -- plus the rise of remote work, plus the genuine gap between what universities teach and what tech companies need, have already eroded the bundle significantly for software engineers.

In sectors where prestige inertia is stronger -- management consulting, law, medicine, investment banking -- the bundle will persist even as the intelligence factory grows. These sectors have built institutional moats: they hire from specific universities, those universities produce disproportionately successful recruits, and the cycle perpetuates. Breaking it would require not just that an alternative emerge, but that a critical mass of employers in the field simultaneously believe the alternative is less risky than the status quo. That is a harder coordination problem.

The bandwidth that AI creates may accelerate unbundling, but it does not guarantee it. The intelligence factory is not coming to obliterate the university. It is coming to pressure each function to justify itself on its own merits. Which functions can justify themselves will depend not on what is technically possible, but on what employers believe they can trust, and what students believe will give them access to opportunity.

---

## Proposed Solution for 3.2 (Skills Rhetoric to Hiring Practice)

**Placement:** In Chapter 05, after the section "Employer Confusion and the Trust Gap" (around line 131-139), insert a new subsection titled "The Rational Inertia of Degree Requirements."

Alternatively or additionally, expand Chapter 08's section "Feedback Loops: How Hiring Reshapes Education" (around line 103-126) with a subsection on the economic incentives that sustain degree requirements despite skills-based hiring adoption.

**Proposed text (Chapter 05 placement):**

### The Rational Inertia of Degree Requirements

The gap between "81% of employers use skills-based hiring" and "most still require degrees" is not a contradiction. It is rational. Understanding why reveals why the shift to portfolios is slower than the technology and the data would suggest.

From a hiring manager's perspective, the decision tree looks like this:

**Cost of screening by degree:** Low. It is simple, fast, legally defensible, and based on decades of calibration. If you filter for candidates from accredited universities with a minimum GPA, you are following a standard that any candidate can understand and challenge. If you make a bad hire, you can point to the credential and claim you followed reasonable procedure. The credential does not require interpretation. Everyone knows what a degree from Stanford means.

**Cost of screening by skills:** High in three ways. First, it demands expertise. Interpreting a GitHub profile, a portfolio of projects, and performance on skills assessments requires judgment. This judgment is harder to systematize and easier to challenge as biased. Second, it demands infrastructure. You need assessment tools, people trained to interpret them, and time in the interview process to evaluate them. Third, and most important, it concentrates legal risk on the hiring manager. If you hire someone based on a portfolio and they fail spectacularly, you cannot point to an industry standard that you followed. You made a judgment, and if the judgment was wrong, that is on you in a way that degree requirements are not.

**Cost of false positives:** When screening by degree, the main risk is hiring someone with a credential who cannot perform. This risk is managed through other filters -- interview quality, reference checks, trial projects. When screening by skills, the main risk is hired someone without a credential who cannot perform. This feels different. In a lawsuit or a regulator question, the question "Why did you hire someone without a degree for a role that traditionally requires one?" is harder to answer than "Why did you hire someone with a degree who turned out to be incapable?" The former puts you on the defensive about your process; the latter puts you on the defensive about your judgment. Corporations have legal departments and insurance models built around the latter, not the former.

This is not theoretical. In regulated professions -- law, medicine, engineering -- degrees are hard gates not because they perfectly predict performance, but because they are the legally defensible basis for gatekeeping. You cannot open yourself to the liability of hiring an unaccredited lawyer, even if that person might perform well.

In less regulated fields, the pattern is subtler but real. A hiring manager at a bank or a Fortune 500 company who eliminates degree requirements is making an individual decision to take on individual risk. A hiring manager who maintains degree requirements is following industry practice and can share the risk across an entire sector. Until the industry standard shifts, individual incentives point toward maintaining the status quo.

This means that skills-based hiring will not replace degree requirements until one of three things happens:

1. **Risk is pooled at the industry level.** If a critical mass of major employers in a sector simultaneously commit to hiring without degree requirements and report positive outcomes, the decision shifts from individual to collective. At that point, an individual hiring manager can say "our industry has moved to skills-based hiring, and we follow that practice." This creates legitimacy and shared liability. Tech is approaching this threshold in some roles; most sectors are far from it.

2. **Skills assessment becomes as legible as degrees.** Right now, interpreting a portfolio is harder than reading a resume. If a standardized, transparent, industry-recognized system emerged for certifying skills -- something more credible than the current fragmented landscape of micro-credentials and bootcamp certificates -- then the cost of screening by skills would drop significantly. Blockchain-based credentials with immutable metadata, combined with widespread employer training on interpretation, could move the needle here, but it requires sustained coordination that has not yet emerged.

3. **The cost of maintaining degree requirements becomes visible and high.** This happens when employers explicitly demonstrate that degree filters are excluding high-performing candidates or when the talent shortage becomes acute enough that degree requirements become economically painful. Europe is approaching this in tech -- the unfilled IT positions are not hypothetical, and the pain is driving regulatory and employer-level coordination toward skills-based alternatives. But in most of the labor market, the pain is not yet visible enough to justify changing a process that works well enough.

The implication is that the timeline for shifting from degree-based to portfolio-based hiring is not driven by the capability of assessment technology. It is driven by the coordination problem of shifting industry standards and the regulatory timing of reducing legal risk. In technology, where this coordination is most advanced and the pain is most acute, the shift is visible and ongoing. In most other sectors, it is slower and more patchy. This is not because hiring managers are irrational or stubborn. It is because the rational incentives that have made degree requirements standard are still very much in place.

The shift from "we plan to adopt skills-based hiring" to "we actually do it at scale" requires not just better tools. It requires a change in the risk calculus, a change in industry norms, and often a change in regulation. All three are possible, but none is automatic.

---

## Summary of Additions

These two passages fill the causal gaps by:

**For 3.1:** Explaining that unbundling requires a threshold shift in three equilibrium conditions: (a) employer confidence in alternatives, (b) erosion of network value, and (c) critical mass coordination. This shows why unbundling may happen in some sectors (tech) but not others (medicine, law) and explains what would accelerate or block it.

**For 3.2:** Modeling the rational incentives that keep degree requirements in place despite skills-based hiring rhetoric: low cost and high defensibility of degrees, high cost and legal risk of skills-based assessment, and the coordination problem of shifting industry standards. This shows why the shift is slower than technology alone would predict and identifies the three concrete conditions that would change the calculus.

Both additions keep Krishan's voice: direct, evidence-based, dismissive of technological determinism, and focused on the structural incentives that actually shape behavior.
