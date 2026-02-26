"""GlobalConstraints module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
        DataConstr,
    )
    from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr_rule import (
        DataConstrRule,
    )
    from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.phys_constrs import (
        PhysConstrs,
    )
    from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.internal_constrs import (
        InternalConstrs,
    )
    from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.scale_constr import (
        ScaleConstr,
    )

__all__ = [
    "DataConstr",
    "DataConstrRule",
    "InternalConstrs",
    "PhysConstrs",
    "ScaleConstr",
]
