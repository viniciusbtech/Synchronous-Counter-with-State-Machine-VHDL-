Synchronous Counter with Finite State Machine (VHDL)
Description

This project implements a synchronous counter using a Finite State Machine (FSM) in VHDL.
The counter has 8 states, and on every clock cycle it transitions to the next state while producing a specific 4-bit output.

The system also includes an asynchronous reset, which forces the machine back to the initial state (s0).

How It Works

The circuit is controlled by two main signals:
clk – Clock signal responsible for synchronizing state transitions.
reset – When set to '1', it resets the machine to the initial state.
The state machine contains 8 states (s0 to s7).
For each state:
A specific 4-bit value is assigned to the output q.
The next state is defined.

Code Structure

The project is organized into the following main parts:

1. Entity Declaration

Defines the inputs and outputs of the circuit.

clk   : clock input
reset : reset input
q     : 4-bit output
2. State Machine Definition

The states are defined using an enumerated type:

type state_type is (s0, s1, s2, s3, s4, s5, s6, s7);
Two signals are used:
state → current state
next_state → next state

3. Sequential Process

This process updates the current state on the rising edge of the clock.
if rising_edge(clk) then
    state <= next_state;
end if;

If the reset signal is active:
state <= s0;

4. Combinational Process

This process determines:
the next state
the output value (q)
It is implemented using a case statement based on the current state.

Requirements
To simulate or synthesize this project, you can use VHDL tools such as:
ModelSim
Intel Quartus
Xilinx Vivado
GHDL

Possible Applications
This type of implementation can be used in:
Digital controllers
Sequential logic systems
FPGA-based designs
Educational projects involving Finite State Machines (FSM)
