# Relationship State Machine Evaluator

A command-line tool for evaluating relationship dynamics using behavioral patterns over time, rather than single events or emotional interpretation.

This is a heuristic system, not a predictive model. It helps structure uncertainty in interpersonal relationships by focusing on observable stability patterns.

------------------------------------------------------------

## CORE IDEA

Instead of asking:
“What does this single interaction mean?”

We ask:
“Is there a consistent behavioral pattern over time?”

The system reduces overreaction to short-term signals by focusing on recurring patterns across time.

------------------------------------------------------------

## INSTALLATION

git clone https://github.com/yourusername/relationship-state-machine.git
cd relationship-state-machine
python3 relationship_cli.py --help

------------------------------------------------------------

## USAGE

python relationship_cli.py \
  --name "Person A" \
  --baseline 70 \
  --cc 2 \
  --rc 1 \
  --ds -1 \
  --activation medium

------------------------------------------------------------

## INPUT PARAMETERS

--name
Label for the person or system being evaluated.

------------------------------------------------------------

--baseline (0–100)

Measures how consistent behavior is over time.

Think:
“Do they behave in a predictable and stable way across weeks/months?”

0–29  → no stable pattern
30–69 → partial consistency
70–100 → highly stable pattern

------------------------------------------------------------

--cc (Change Counter)

Counts sustained behavioral changes, not single events.

Counts when:
- communication drops consistently
- emotional tone shifts over time
- initiation patterns change permanently

Does NOT count:
- single slow reply
- one cancelled plan
- temporary mood swings

------------------------------------------------------------

--rc (Repair Counter)

Counts how often the system returns to baseline after disruption.

Examples:
- conflict → resolution → normal interaction resumes
- distance → reconnection without forcing
- misunderstanding → natural repair

------------------------------------------------------------

--ds (Drift Score)

Represents overall trajectory:

+2 to +5 → improving
0        → stable
-1       → slight decline
-2       → clear decline
-3       → strong deterioration

------------------------------------------------------------

--activation (low / medium / high)

How emotionally “loud” the person is in your mind:

low:
- calm, occasional thoughts

medium:
- regular thoughts, moderate emotional engagement

high:
- frequent mental loops
- strong emotional salience

------------------------------------------------------------

## OUTPUT STATES

- NO_STABLE_BASELINE
- NOISE
- STABLE_WITH_REPAIR
- NEGATIVE_DRIFT
- CLUSTER_DETECTED
- UNCLEAR

------------------------------------------------------------

## EXAMPLE

python relationship_cli.py \
  --name "Person A" \
  --baseline 75 \
  --cc 1 \
  --rc 2 \
  --ds 0 \
  --activation medium

Output:

status: STABLE_WITH_REPAIR
recommendation: maintain investment
cc: 1
rc: 2
ds: 0.0

------------------------------------------------------------

## DESIGN PHILOSOPHY

- Relationships are pattern-based systems
- Stability emerges from repeated behavior over time
- Uncertainty should be updated periodically, not continuously
- Emotional activation can distort interpretation of signals

------------------------------------------------------------

## LIMITATIONS

This system:
- does NOT predict intentions or feelings
- does NOT compute real probabilities
- does NOT guarantee outcomes
- depends on subjective estimation of inputs

It is a structuring tool, not a truth model.

------------------------------------------------------------

## FUTURE IMPROVEMENTS

1. Event-based logging mode

python relationship_cli.py --event "communication dropped for 2 weeks"
python relationship_cli.py --event "reconnection after conflict"

Automatically updates state over time.

------------------------------------------------------------

2. Persistent memory (SQLite)

Track each person over time:
- CC history
- RC cycles
- drift trends

------------------------------------------------------------

3. Time-series visualization

- stability curves
- drift graphs
- repair frequency charts

------------------------------------------------------------

4. Interactive CLI mode

> add event: slow replies
> add event: reconnection
> status

------------------------------------------------------------

## LICENSE

MIT License