"""ValueList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 350)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 314)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 459)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 222)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class ValueList(ARObject):
    """AUTOSAR ValueList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "v": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # v
    }

    def __init__(self) -> None:
        """Initialize ValueList."""
        super().__init__()
        self.v: Optional[Numerical] = None


class ValueListBuilder:
    """Builder for ValueList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueList = ValueList()

    def build(self) -> ValueList:
        """Build and return ValueList object.

        Returns:
            ValueList instance
        """
        # TODO: Add validation
        return self._obj
