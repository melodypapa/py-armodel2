"""CompuGenericMath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 374)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
)


class CompuGenericMath(ARObject):
    """AUTOSAR CompuGenericMath."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "level": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # level
    }

    def __init__(self) -> None:
        """Initialize CompuGenericMath."""
        super().__init__()
        self.level: Optional[PrimitiveIdentifier] = None


class CompuGenericMathBuilder:
    """Builder for CompuGenericMath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuGenericMath = CompuGenericMath()

    def build(self) -> CompuGenericMath:
        """Build and return CompuGenericMath object.

        Returns:
            CompuGenericMath instance
        """
        # TODO: Add validation
        return self._obj
