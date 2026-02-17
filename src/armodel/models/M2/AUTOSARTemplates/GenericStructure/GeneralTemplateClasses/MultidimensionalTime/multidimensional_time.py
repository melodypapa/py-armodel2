"""MultidimensionalTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 164)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 109)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 165)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_MultidimensionalTime.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CseCodeType,
    Integer,
)


class MultidimensionalTime(ARObject):
    """AUTOSAR MultidimensionalTime."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "cse_code": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cseCode
        "cse_code_factor": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # cseCodeFactor
    }

    def __init__(self) -> None:
        """Initialize MultidimensionalTime."""
        super().__init__()
        self.cse_code: Optional[CseCodeType] = None
        self.cse_code_factor: Optional[Integer] = None


class MultidimensionalTimeBuilder:
    """Builder for MultidimensionalTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultidimensionalTime = MultidimensionalTime()

    def build(self) -> MultidimensionalTime:
        """Build and return MultidimensionalTime object.

        Returns:
            MultidimensionalTime instance
        """
        # TODO: Add validation
        return self._obj
