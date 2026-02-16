"""VariationPoint AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.condition_by_formula import (
    ConditionByFormula,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class VariationPoint(ARObject):
    """AUTOSAR VariationPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "blueprint": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # blueprint
        "sw_syscond": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ConditionByFormula,
        ),  # swSyscond
    }

    def __init__(self) -> None:
        """Initialize VariationPoint."""
        super().__init__()
        self.blueprint: Optional[DocumentationBlock] = None
        self.sw_syscond: Optional[ConditionByFormula] = None


class VariationPointBuilder:
    """Builder for VariationPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariationPoint = VariationPoint()

    def build(self) -> VariationPoint:
        """Build and return VariationPoint object.

        Returns:
            VariationPoint instance
        """
        # TODO: Add validation
        return self._obj
