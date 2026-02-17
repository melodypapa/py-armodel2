"""FormulaLanguage module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage.formula_expression import (
        FormulaExpression,
    )

__all__ = [
    "FormulaExpression",
]
