#!/usr/bin/env python3

import argparse
from dataclasses import dataclass


@dataclass
class RelationshipState:
    name: str
    baseline_confidence: int
    change_counter: int
    repair_counter: int
    drift_score: int
    emotional_activation: str


class RelationshipEvaluator:

    def evaluate(self, state: RelationshipState):

        activation_factor = {
            "low": 1.0,
            "medium": 0.8,
            "high": 0.5
        }.get(state.emotional_activation, 1.0)

        cc = state.change_counter
        rc = state.repair_counter
        ds = state.drift_score * activation_factor

        if state.baseline_confidence < 30:
            return {"status": "NO_STABLE_BASELINE", "recommendation": "observe only"}

        if cc < 2:
            return {"status": "NOISE", "recommendation": "no action", "cc": cc, "rc": rc, "ds": ds}

        cluster = cc >= 3

        if rc >= cc:
            return {"status": "STABLE_WITH_REPAIR", "recommendation": "maintain investment", "cc": cc, "rc": rc, "ds": ds}

        if ds <= -2:
            return {"status": "NEGATIVE_DRIFT", "recommendation": "reduce investment", "cc": cc, "rc": rc, "ds": ds}

        if cluster:
            return {"status": "CLUSTER_DETECTED", "recommendation": "monitor trend", "cc": cc, "rc": rc, "ds": ds}

        return {"status": "UNCLEAR", "recommendation": "collect more data", "cc": cc, "rc": rc, "ds": ds}


HELP_TEXT = """
Relationship State Machine Evaluator

This tool helps you evaluate whether a relationship is:
- stable
- unstable
- or structurally mismatched

It does NOT predict emotions or certainty.
It evaluates behavioral patterns over time.

------------------------------------------------------------
INPUT EXPLANATION
------------------------------------------------------------

--name
  Who you are evaluating (label only)

--baseline (0–100)
  How consistent this person has been in behavior toward you.

  Think:
  "Do they behave in a predictable way over time?"

  Low (0–29):
    - inconsistent or situational contact
  Medium (30–69):
    - some pattern exists, but irregular
  High (70–100):
    - stable, predictable interaction pattern

------------------------------------------------------------

--cc (Change Counter)
  How many *real, sustained behavioral changes* you’ve observed.

  Counts ONLY if change persists over time.

  Examples:
    + reply behavior changes permanently
    + emotional tone shifts for weeks
    + initiation drops or increases consistently

  NOT:
    - one bad day
    - one slow reply
    - one cancelled plan

------------------------------------------------------------

--rc (Repair Counter)
  How many times the relationship naturally returned to baseline after tension.

  Examples:
    + conflict → resolution → normal behavior returns
    + distance → reconnection without force
    + misunderstanding → repair + stability restored

------------------------------------------------------------

--ds (Drift Score)
  Overall direction of the relationship over time.

  Scale:
    +2 to +5 = improving
    0        = stable
    -1       = slight decline
    -2       = clear decline
    -3 or less = strong deterioration

------------------------------------------------------------

--activation (low / medium / high)
  How emotionally "loud" this person feels in your mind.

  low:
    calm, infrequent thoughts

  medium:
    regular thoughts, moderate emotional involvement

  high:
    frequent thinking, strong emotional pull,
    tendency to over-interpret signals

------------------------------------------------------------

INTERPRETATION IDEA

This tool assumes:
- relationships are pattern-based systems
- not single-event decisions
- stability comes from repeated behavior over time
"""

def build_parser():
    parser = argparse.ArgumentParser(
        description="Relationship State Machine Evaluator",
        epilog=HELP_TEXT,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("--name", required=True, help="Label for the person/system")

    parser.add_argument(
        "--baseline",
        type=int,
        default=50,
        help="0–100: consistency of behavior over time (higher = more predictable)"
    )

    parser.add_argument(
        "--cc",
        type=int,
        default=0,
        help="Change Counter: number of sustained behavioral changes observed"
    )

    parser.add_argument(
        "--rc",
        type=int,
        default=0,
        help="Repair Counter: number of successful returns to baseline after tension"
    )

    parser.add_argument(
        "--ds",
        type=int,
        default=0,
        help="Drift Score: overall trend (-3 strong decline to +5 improvement)"
    )

    parser.add_argument(
        "--activation",
        type=str,
        default="low",
        choices=["low", "medium", "high"],
        help="Emotional activation level (how strongly you mentally react to this person)"
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    state = RelationshipState(
        name=args.name,
        baseline_confidence=args.baseline,
        change_counter=args.cc,
        repair_counter=args.rc,
        drift_score=args.ds,
        emotional_activation=args.activation
    )

    engine = RelationshipEvaluator()
    result = engine.evaluate(state)

    print("\n--- RESULT ---")
    print(result)


if __name__ == "__main__":
    main()