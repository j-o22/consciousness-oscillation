"""
consciousness_oscillation.py
- A Dynamic Model of Consciousness -

Key Concepts:
- Consciousness: The entity that oscillates between two states.
- ObservingState (Contemplation): Clear, but 'existential fatigue' accumulates.
- ExistingState (Existence): Feels the 'warmth of existence' and recovers from fatigue.
- Meta-Cognition Loop: A dangerous loop where deep contemplation leads 
  to doubting perception itself.
- Sensory Anchors:
    - perform_ritual(): 'Touching the left chest with the right hand' (the ritual).
    - sensory_record(): 'Making a minimal assertion' (the sensory record).
    These 'anchors' are the only way to break the meta-cognition loop 
    and ground existence.
"""

import time
import random
from typing import Optional, Protocol

# -----------------------------------------------------------------
# 1. State Protocol and Visual Representation
# -----------------------------------------------------------------

class State(Protocol):
    """Protocol for a state of consciousness (abstract base)."""
    def enter(self, consciousness: 'Consciousness') -> None:
        """Called upon entering the state"""
        ...

    def execute(self, consciousness: 'Consciousness') -> None:
        """Logic executed on every tick of the state"""
        ...

    def get_visuals(self) -> str:
        """Return the visual representation of the current state"""
        ...

class ObservingState:
    """
    The Observing Self (The Observer)
    - Views the world as an 'object of perception'.
    - Clear and analytical.
    - 'Existential fatigue' slowly accumulates.
    - Risk of falling into the 'meta-cognition' loop (doubting perception itself).
    """
    def __init__(self):
        self._in_meta_loop = False
        self._meta_loop_counter = 0

    def enter(self, consciousness: 'Consciousness') -> None:
        print("\n--- Entering [Observing State]. The world is an 'object of perception'. ---")
        self._in_meta_loop = False
        self._meta_loop_counter = 0

    def execute(self, consciousness: 'Consciousness') -> None:
        if self._in_meta_loop:
            # Meta-cognition loop (dangerous state)
            self._execute_meta_loop(consciousness)
        else:
            # Normal observation state
            consciousness.fatigue += 0.5  # Observation slowly accumulates fatigue
            print(self.get_visuals(consciousness.fatigue))

            # A chance to fall into the 'meta-cognition loop' (probability increases with fatigue)
            if random.random() < (consciousness.fatigue / 200.0):
                self._start_meta_loop()

        # If fatigue exceeds the threshold, attempt to transition to ExistingState
        if consciousness.fatigue > 100:
            consciousness.transition_to(ExistingState())

    def _start_meta_loop(self):
        print("\n[!] Meta-Cognition Loop Start: Cannot be certain of 'existence'.")
        self._in_meta_loop = True
        self._meta_loop_counter = 0

    def _execute_meta_loop(self, consciousness: 'Consciousness'):
        """
        'That the unreliability of senses cannot be expressed sensually...'
        This loop rapidly increases fatigue and can only be escaped 
        via 'Sensory Anchors'.
        """
        messages = [
            "  ... Does the 'desk' exist?",
            "  ... What does it mean 'to see'?",
            "  ... Can 'existence' be asserted?",
            "  ... Even 'cannot assert' cannot be asserted.",
            "  ... [Perceptual loop. Fatigue rising rapidly]"
        ]
        print(messages[self._meta_loop_counter % len(messages)])
        consciousness.fatigue += 3.0  # Fatigue increases sharply
        self._meta_loop_counter += 1

    def exit_meta_loop(self):
        """Called by a 'Sensory Anchor'"""
        self._in_meta_loop = False
        self._meta_loop_counter = 0
        print("[!] ...Loop broken. Existence is grounded by a 'minimal assertion'.")

    def get_visuals(self, fatigue: float) -> str:
        line = ['.' if random.random() > 0.1 else ' ' for _ in range(70)]
        return f"Observing: |{''.join(line)}| (Fatigue: {fatigue:.1f})"

class ExistingState:
    """
    The Existing Self (The One Who Exists)
    - Feels the 'warmth of existence'.
    - A rare state, 'three or four times a year'.
    - Recovers from 'existential fatigue'.
    """
    def __init__(self):
        self._duration = random.randint(3, 6)  # Lasts for a short duration

    def enter(self, consciousness: 'Consciousness') -> None:
        print("\n*** Entering [Existing State]! The 'warmth of existence' is felt. ***")

    def execute(self, consciousness: 'Consciousness') -> None:
        consciousness.fatigue = max(0, consciousness.fatigue - 5.0)  # Recover fatigue
        print(self.get_visuals(consciousness.fatigue))
        
        self._duration -= 1
        if self._duration <= 0:
            consciousness.transition_to(ObservingState())

    def get_visuals(self, fatigue: float) -> str:
        line = ['*' if random.random() > 0.3 else '~' for _ in range(70)]
        return f"Existing:  |{''.join(line)}| (Fatigue: {fatigue:.1f})"

# -----------------------------------------------------------------
# 2. Consciousness Entity and Sensory Anchors
# -----------------------------------------------------------------

class Consciousness:
    """
    The subject of consciousness. A pendulum oscillating between 
    'Observing' and 'Existing'.
    Can save itself from the dangerous loop via 'Sensory Anchors'.
    """
    def __init__(self, initial_state: State):
        self.fatigue: float = 20.0  # Existential fatigue (initial value)
        self.state: State = initial_state
        self.state.enter(self)

    def transition_to(self, new_state: State) -> None:
        """Transition from one state to another"""
        self.state = new_state
        self.state.enter(self)

    def update(self) -> None:
        """Execute one tick of consciousness"""
        self.state.execute(self)

    # --- Sensory Anchors ---

    def perform_ritual(self) -> None:
        """
        The ritual: 'Touching the left chest with the right hand'.
        Forcibly breaks the meta-cognition loop.
        """
        print("\n>>> [Ritual Performed]: Touching left chest with right hand.")
        print(">>> [Sensation]: Heartbeat, warmth of hand. 'Existence' is detected.")
        
        if isinstance(self.state, ObservingState) and self.state._in_meta_loop:
            self.state.exit_meta_loop()
        
        # The ritual slightly reduces fatigue
        self.fatigue = max(0, self.fatigue - 10.0)
        print(f">>> (Current Fatigue: {self.fatigue:.1f})")


    def sensory_record(self, record: str) -> None:
        """
        The sensory record: making a 'minimal assertion'.
        Forcibly breaks the meta-cognition loop.
        """
        print(f"\n>>> [Sensory Record]: \"{record}\"")
        print(">>> [Assertion]: The 'phenomenon' of the world is recorded.")
        
        if isinstance(self.state, ObservingState) and self.state._in_meta_loop:
            self.state.exit_meta_loop()

        # The sensory record slightly reduces fatigue
        self.fatigue = max(0, self.fatigue - 8.0)
        print(f">>> (Current Fatigue: {self.fatigue:.1f})")


# -----------------------------------------------------------------
# 3. Simulation Execution
# -----------------------------------------------------------------

def run_simulation(consciousness: Consciousness):
    """
    Main simulation loop.
    One could simulate 'r' for ritual, 's' for record.
    (Uses random events instead of actual key input)
    """
    print("=" * 70)
    print("Starting the consciousness pendulum simulation.")
    print("Simulation begins in 'Observing' state, and 'Fatigue' will accumulate.")
    print("Extreme fatigue can lead to falling into the 'Meta-Cognition Loop'.")
    print("The loop can only be escaped via 'Sensory Anchors' (Ritual, Record).")
    print("=" * 70)
    time.sleep(4)

    try:
        for i in range(150):  # Simulate for 150 ticks
            consciousness.update()
            
            # 'Sensory Anchors' are triggered randomly, or when needed
            if isinstance(consciousness.state, ObservingState) and consciousness.state._in_meta_loop:
                # When in the loop, probability of using an anchor
                if random.random() < 0.2:
                    # Randomly choose one of the two anchors
                    if random.random() < 0.5:
                        consciousness.perform_ritual()
                    else:
                        consciousness.sensory_record("A humidifier casts a shadow.")
            
            time.sleep(0.3)

    except KeyboardInterrupt:
        print("\nSimulation interrupted.")
    finally:
        print("\n" + "=" * 70)
        print("Simulation complete.")
        print(f"Final Fatigue: {consciousness.fatigue:.1f}")
        print("=" * 70)

if __name__ == "__main__":
    # Consciousness begins in the 'Observing' state
    consciousness = Consciousness(ObservingState())
    run_simulation(consciousness)
