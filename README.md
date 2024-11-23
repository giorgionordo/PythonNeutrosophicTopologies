# Python Neutrosophic Topologies Framework
A framework extension for dealing with families of neutrosophic sets and building/verifying neutrosophic topologies


Giorgio Nordo - Dipartimento MIFT, Università di Messina, Italy
www.nordo.it   |  giorgio.nordo@unime.it 

---
## NSfamily: A New Class for Neutrosophic Topologies

The **`NSfamily`** class is a powerful new addition to the Python Neutrosophic Sets (**PYNS**) framework. It is designed to enhance the framework's capability to handle **neutrosophic families**, enabling systematic construction and manipulation of **neutrosophic topologies**. By providing tools to verify closure properties, manage unions and intersections, and construct bases and sub-bases, `NSfamily` bridges a significant gap in the PYNS framework. 

This enhancement makes it easier for researchers and practitioners to explore **neutrosophic topology**, a generalization of classical topology tailored to handle uncertainty, inconsistency, and incomplete information.

---

## Key Features of the `NSfamily` Class

- **Flexible Initialization**:
  - Create an `NSfamily` from individual sets, lists/tuples of sets, or even another `NSfamily`.
  - Automatically ensures all sets share the same universe.

- **Subset, Superset, and Equality Operations**:
  - Methods like `isSubset()` and `isSuperset()` check containment relationships.
  - Supports operator overloading for comparisons (`<=`, `>=`, `==`, `!=`).

- **Set Operations**:
  - Perform union, intersection, and difference between families.
  - Compute complements of all neutrosophic sets in the family.
  - Operator overloading allows intuitive usage (e.g., `+`, `&`, `-`, `~`).

- **Topology Construction**:
  - Generate a **neutrosophic base** from a sub-base using `getNSBase()`.
  - Build a complete **neutrosophic topology** from a base or sub-base using `getNSTopologyByBase()` or `getNSTopologyBySubBase()`.

- **Validation**:
  - Verify whether a family forms a valid neutrosophic topology with `isNeutrosophicTopology()`.
  - Ensure closure under union and intersection with `NSunionClosed()` and `NSintersectionClosed()`.

---

## Example Usage

Here's an example of how to use the `NSfamily` class to generate a neutrosophic topology from a sub-base:

```python
from pyns.ns_universe import NSuniverse
from pyns.ns_set import NSset
from pyns.ns_family import NSfamily

# Define a universe
U = NSuniverse("a,b,c")

# Create some neutrosophic sets
A1 = NSset(U, "(0.4,0.4,0.3), (0.1,0.1,0.1), (0.2,0.2,0.2)")
A2 = NSset(U, "(0.1,0.2,0.9), (0.9,0.1,0.3), (0.5,0.3,0.4)")

# Initialize a neutrosophic family
S = NSfamily(A1, A2)

# Generate the neutrosophic topology
T = S.getNSTopologyBySubBase()

# Check if it is a valid topology
print(f"Is T a neutrosophic topology? {T.isNeutrosophicTopology()}")

# Display the topology
print(f"Neutrosophic topology:\n{T}")
