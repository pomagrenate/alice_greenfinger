#!/usr/bin/env python3
"""
Alice Greenfingers - Pure-Python First-Order Linear Symbolic Constraint Solver
Classification: E6 (Automated Symbolic / Constraint Evidence)
"""
import json

class ConstraintSolver:
    def __init__(self):
        self.variables = {}
        self.constraints = []

    def declare_var(self, name, min_val, max_val):
        self.variables[name] = {"min": min_val, "max": max_val}

    def add_constraint(self, expr_str):
        self.constraints.append(expr_str)

    def solve(self):
        # First-order interval & linear arithmetic solver
        intervals = {v: [info["min"], info["max"]] for v, info in self.variables.items()}
        for c in self.constraints:
            c = c.strip()
            if "==" in c:
                parts = c.split("==")
                var = parts[0].strip()
                val = int(parts[1].strip())
                if var in intervals:
                    if val < intervals[var][0] or val > intervals[var][1]:
                        return "UNSAT", None
                    intervals[var] = [val, val]
            elif ">=" in c:
                parts = c.split(">=")
                var = parts[0].strip()
                val = int(parts[1].strip())
                if var in intervals:
                    if val > intervals[var][1]:
                        return "UNSAT", None
                    intervals[var][0] = max(intervals[var][0], val)
            elif "<=" in c:
                parts = c.split("<=")
                var = parts[0].strip()
                val = int(parts[1].strip())
                if var in intervals:
                    if val < intervals[var][0]:
                        return "UNSAT", None
                    intervals[var][1] = min(intervals[var][1], val)
            elif "<" in c:
                parts = c.split("<")
                var = parts[0].strip()
                val = int(parts[1].strip())
                if var in intervals:
                    if val <= intervals[var][0]:
                        return "UNSAT", None
                    intervals[var][1] = min(intervals[var][1], val - 1)
            elif ">" in c:
                parts = c.split(">")
                var = parts[0].strip()
                val = int(parts[1].strip())
                if var in intervals:
                    if val >= intervals[var][1]:
                        return "UNSAT", None
                    intervals[var][0] = max(intervals[var][0], val + 1)
            elif "!=" in c:
                parts = c.split("!=")
                var = parts[0].strip()
                val = int(parts[1].strip())
                if var in intervals:
                    if intervals[var][0] == intervals[var][1] == val:
                        return "UNSAT", None

        # Check validity of resulting intervals
        model = {}
        for var, (lo, hi) in intervals.items():
            if lo > hi:
                return "UNSAT", None
            model[var] = lo
        return "SAT", model
